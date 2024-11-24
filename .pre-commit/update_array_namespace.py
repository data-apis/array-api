from __future__ import annotations

import sys
import ast
import argparse
from pathlib import Path
from copy import deepcopy
from collections import defaultdict


def _function_to_protocol(
    stmt: ast.FunctionDef, typevars: list[str]
) -> tuple[ast.ClassDef, list[str], str]:
    stmt = deepcopy(stmt)
    name = stmt.name
    docstring = ast.get_docstring(stmt)
    stmt.name = "__call__"
    stmt.body = [ast.Raise(exc=ast.Name(id="NotImplementedError"), cause=None)]
    stmt.args.posonlyargs.insert(0, ast.arg(arg="self"))
    stmt.decorator_list.append(ast.Name(id="abstractmethod"))
    args = ast.unparse(stmt.args)
    typevars = [typevar for typevar in typevars if typevar in args]

    # Construct the protocol
    cls_def = ast.ClassDef(
        name=name,
        decorator_list=[ast.Name(id="runtime_checkable")],
        keywords=[],
        bases=[
            ast.Subscript(
                value=ast.Name(id="Protocol"),
                slice=ast.Tuple(elts=[ast.Name(typevar) for typevar in typevars]),
            )
        ],
        body=[stmt],
    )
    if docstring is not None:
        cls_def.body.insert(0, ast.Expr(value=ast.Constant(docstring, kind=None)))
    if sys.version_info >= (3, 12):
        cls_def.type_params = []
    return cls_def, typevars, name + (f"[{', '.join(typevars)}]" if typevars else "")


def _attributes_to_protocol(
    name, attributes: list[tuple[str, str, str | None, list]], typevars: list[str]
) -> tuple[ast.ClassDef, set[str], str]:
    body = []
    for attribute, type, docstring, _ in attributes:
        body.append(
            ast.AnnAssign(
                target=ast.Name(id=attribute),
                annotation=ast.Name(id=type) if type is not None else None,
                simple=1,
            )
        )
        if docstring is not None:
            body.append(ast.Expr(value=ast.Constant(docstring)))

    typevars = set([x for attribute in attributes for x in attribute[3]])
    return (
        ast.ClassDef(
            name=name,
            decorator_list=[ast.Name(id="runtime_checkable")],
            keywords=[],
            bases=[
                ast.Subscript(
                    value=ast.Name(id="Protocol"),
                    slice=ast.Tuple(elts=[ast.Name(typevar) for typevar in typevars]),
                )
            ],
            body=body,
        ),
        typevars,
        name + (f"[{', '.join(typevars)}]" if typevars else ""),
    )


def main(out_name: str = "_namespace.py") -> None:
    # main working directory
    draft_path = Path("src") / "array_api_stubs" / "_draft"

    # get module bodies
    body_module = {
        path.stem: ast.parse(path.read_text("utf-8")).body
        for path in draft_path.rglob("*.py")
        if path.name != out_name
    }
    body_typevars = body_module.pop("_types")
    body_module.pop("__init__")

    # Get all TypeVars
    typevars = []
    for b in body_typevars:
        if isinstance(b, ast.Assign):
            value = b.value
            if isinstance(value, ast.Call):
                if value.func.id == "TypeVar":
                    typevars.append(value.args[0].s)
    print(typevars)

    # Dict of module attributes per submodule
    module_attributes = defaultdict(list)

    # Import `abc.abstractmethod`, `typing.Protocol` and `typing.runtime_checkable`
    out = ast.Module(body=[], type_ignores=[])
    out.body.append(
        ast.Expr(value=ast.Constant("Auto generated Protocol classes (Do not edit)"))
    )
    out.body.append(
        ast.ImportFrom(
            module="typing",
            names=[
                ast.alias(name="Protocol", alias=None),
                ast.alias(name="runtime_checkable", alias=None),
            ],
        ),
    )
    out.body.append(
        ast.ImportFrom(
            module="abc",
            names=[ast.alias(name="abstractmethod", alias=None)],
        ),
    )

    # Create Protocols with __call__, representing functions
    for submodule, body in body_module.items():
        for b in body:
            if isinstance(b, (ast.Import, ast.ImportFrom)):
                out.body.insert(0, b)
            elif isinstance(b, ast.FunctionDef):
                cls_def, typevars_, type = _function_to_protocol(b, typevars)
                module_attributes[submodule].append((b.name, type, None, typevars_))
                out.body.append(cls_def)
            elif isinstance(b, ast.Assign):
                id = getattr(b.targets[0], "id")
                if id == "__all__":
                    pass
                else:
                    docstring = None
                    docstring_expr = body[body.index(b) + 1]
                    if isinstance(docstring_expr, ast.Expr):
                        if isinstance(docstring_expr.value, ast.Constant):
                            docstring = docstring_expr.value.value
                    module_attributes[submodule].append((id, "float", docstring, []))
            elif isinstance(b, ast.Expr):
                pass
            else:
                print(f"Skipping {submodule} {b} {ast.dump(b)} \n\n")

    # Create Protocols for fft and linalg
    submodules = []
    OPTIONAL_SUBMODULES = ["fft", "linalg"]
    for submodule, attributes in module_attributes.items():
        if submodule not in OPTIONAL_SUBMODULES:
            continue
        cls_def, typevars_, type = _attributes_to_protocol(
            submodule[0].upper() + submodule[1:] + "Namespace", attributes, typevars
        )
        out.body.append(cls_def)
        if submodule in OPTIONAL_SUBMODULES:
            submodules.append((submodule, type, None, []))

    # Create Protocols for the main namespace
    attributes = [
        attribute
        for submodule, attributes in module_attributes.items()
        for attribute in attributes
        if submodule not in OPTIONAL_SUBMODULES
    ] + submodules
    out.body.append(_attributes_to_protocol("ArrayNamespace", attributes, typevars)[0])

    out_path = draft_path / out_name
    out_path.write_text(ast.unparse(out), "utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="python func_to_protocol.py test.py test_out.py",
        description=__doc__,
    )
    parser.add_argument(
        "--out-name",
        type=str,
        help="The name of the output file.",
        default="_namespace.py",
        required=False,
    )
    args = parser.parse_args()
    main(args.out_name)
