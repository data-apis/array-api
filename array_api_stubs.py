import sys
from importlib import import_module
from importlib.util import find_spec
from inspect import getmembers, isfunction, signature
from pathlib import Path
from types import FunctionType, ModuleType, SimpleNamespace
from typing import Dict, List, Optional
from unittest import TestCase

__all__ = ["make_stubs_namespace"]

API_VERSIONS = {"2012.12"}  # TODO: infer released versions dynamically


def make_stubs_namespace(api_version: Optional[str] = None) -> SimpleNamespace:
    """
    Returns a ``SimpleNamespace`` where

    * ``functions`` (``dict[str, FunctionType]``) maps names of top-level
      functions to their respective stubs.
    * ``array_methods`` (``dict[str, FunctionType]``) maps names of array
      methods to their respective stubs.
    * ``dtype_methods`` (``dict[str, FunctionType]``) maps names of dtype object
      methods to their respective stubs.
    * ``category_to_functions`` (``dict[str, dict[str, FunctionType]]``) maps
      names of categories to their respective function mappings.
    * ``extension_to_functions`` (``dict[str, dict[str, FunctionType]]``) maps
      names of extensions to their respective function mappings.

    Examples
    --------

    Make a stubs namespace.

        >>> from array_api_stubs import make_stubs_namespace
        >>> stubs = make_stubs_namespace()

    Access the ``array_api.square()`` stub.

        >>> stubs.functions["square"]
        <function array_api.square(x: ~array, /) -> ~array>

    Find names of all set functions.

        >>> stubs.category_to_functions["set"].keys()
        dict_keys(['unique_all', 'unique_counts', 'unique_inverse', 'unique_values'])

    Access the array object's ``__add__`` stub.

        >>> stubs.array_methods["__add__"]
        <function array_api._Array.__add__(self: 'array', other: 'Union[int, float, array]', /) -> 'array'>

    Access the ``array_api.linalg.cross()`` stub.

        >>> stubs.extension_to_functions["linalg"]["cross"]
        <function array_api.linalg.cross(x1: ~array, x2: ~array, /, *, axis: int = -1) -> ~array>

    """
    if api_version is None:
        api_version = "draft"
    if api_version in API_VERSIONS or api_version == "latest":
        raise NotImplementedError("{api_version=} not yet supported")
    elif api_version != "draft":
        raise ValueError(
            f"{api_version=} not 'draft', 'latest', "
            f"or a released version ({API_VERSIONS})"
        )

    spec_dir = Path(__file__).parent / "spec" / "API_specification"
    signatures_dir = spec_dir / "array_api"
    assert signatures_dir.exists()  # sanity check
    spec_abs_path: str = str(spec_dir.resolve())
    sys.path.append(spec_abs_path)
    assert find_spec("array_api") is not None  # sanity check

    name_to_mod: Dict[str, ModuleType] = {}
    for path in signatures_dir.glob("*.py"):
        name = path.name.replace(".py", "")
        name_to_mod[name] = import_module(f"array_api.{name}")

    array = name_to_mod["array_object"].array
    array_methods: Dict[str, FunctionType] = {}
    for name, func in getmembers(array, predicate=isfunction):
        func.__module__ = "array_api"
        assert "Alias" not in func.__doc__  # sanity check
        func.__qualname__ = f"_Array.{func.__name__}"
        array_methods[name] = func

    dtype_eq = name_to_mod["data_types"].__eq__
    assert isinstance(dtype_eq, FunctionType)  # for mypy
    dtype_eq.__module__ = "array_api"
    dtype_eq.__qualname__ = "_DataType.__eq__"
    dtype_methods: Dict[str, FunctionType] = {"__eq__": dtype_eq}

    functions: Dict[str, FunctionType] = {}
    category_to_functions: Dict[str, Dict[str, FunctionType]] = {}
    for name, mod in name_to_mod.items():
        if name.endswith("_functions"):
            category = name.replace("_functions", "")
            name_to_func = {}
            for name in mod.__all__:
                func = getattr(mod, name)
                assert isinstance(func, FunctionType)  # sanity check
                func.__module__ = "array_api"
                name_to_func[name] = func
            functions.update(name_to_func)
            category_to_functions[category] = name_to_func

    extensions: List[str] = ["linalg"]  # TODO: infer on runtime
    extension_to_functions: Dict[str, Dict[str, FunctionType]] = {}
    for ext in extensions:
        mod = name_to_mod[ext]
        name_to_func = {name: getattr(mod, name) for name in mod.__all__}
        name_to_func = {}
        for name in mod.__all__:
            func = getattr(mod, name)
            assert isinstance(func, FunctionType)  # sanity check
            assert func.__doc__ is not None  # for mypy
            if "Alias" in func.__doc__:
                func.__doc__ = functions[name].__doc__
            func.__module__ = f"array_api.{ext}"
            name_to_func[name] = func
        extension_to_functions[ext] = name_to_func

    return SimpleNamespace(
        functions=functions,
        array_methods=array_methods,
        dtype_methods=dtype_methods,
        category_to_functions=category_to_functions,
        extension_to_functions=extension_to_functions,
    )


class TestMakeStubsNamespace(TestCase):
    def setUp(self):
        self.stubs = make_stubs_namespace()

    def test_attributes(self):
        assert isinstance(self.stubs, SimpleNamespace)
        for attr in ["functions", "array_methods", "dtype_methods"]:
            mapping = getattr(self.stubs, attr)
            assert isinstance(mapping, dict)
            assert all(isinstance(k, str) for k in mapping.keys())
            assert all(isinstance(v, FunctionType) for v in mapping.values())
        for attr in ["category_to_functions", "extension_to_functions"]:
            mapping = getattr(self.stubs, attr)
            assert isinstance(mapping, dict)
            assert all(isinstance(k, str) for k in mapping.keys())
            for sub_mapping in mapping.values():
                assert isinstance(sub_mapping, dict)
                assert all(isinstance(k, str) for k in sub_mapping.keys())
                assert all(isinstance(v, FunctionType) for v in sub_mapping.values())

    def test_function_meta(self):
        toplevel_stub = self.stubs.functions["matmul"]
        assert toplevel_stub.__module__ == "array_api"
        extension_stub = self.stubs.extension_to_functions["linalg"]["matmul"]
        assert extension_stub.__module__ == "array_api.linalg"
        assert extension_stub.__doc__ == toplevel_stub.__doc__

    def test_array_method_meta(self):
        stub = self.stubs.array_methods["__add__"]
        assert stub.__module__ == "array_api"
        assert stub.__qualname__ == "_Array.__add__"
        first_arg = next(iter(signature(stub).parameters.values()))
        assert first_arg.name == "self"

    def test_dtype_method_meta(self):
        stub = self.stubs.dtype_methods["__eq__"]
        assert stub.__module__ == "array_api"
        assert stub.__qualname__ == "_DataType.__eq__"
        first_arg = next(iter(signature(stub).parameters.values()))
        assert first_arg.name == "self"
