"""
Types for type annotations used in the array API standard.

The type variables should be replaced with the actual types for a given
library, e.g., for NumPy TypeVar('array') would be replaced with ndarray.
"""
from __future__ import annotations

__all__ = [
    "Any",
    "List",
    "Literal",
    "NestedSequence",
    "Optional",
    "PyCapsule",
    "SupportsBufferProtocol",
    "SupportsDLPack",
    "Tuple",
    "Union",
    "Sequence",
    "array",
    "device",
    "dtype",
    "ellipsis",
    "finfo_object",
    "iinfo_object",
    "Enum",
    "DefaultDataTypes",
    "DataTypes",
    "Capabilities",
    "Info",
]

from dataclasses import dataclass
from typing import (
    Any,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    TypedDict,
    TypeVar,
    Union,
    Protocol,
)
from enum import Enum

array = TypeVar("array")
device = TypeVar("device")
dtype = TypeVar("dtype")
SupportsDLPack = TypeVar("SupportsDLPack")
SupportsBufferProtocol = TypeVar("SupportsBufferProtocol")
PyCapsule = TypeVar("PyCapsule")
# ellipsis cannot actually be imported from anywhere, so include a dummy here
# to keep pyflakes happy. https://github.com/python/typeshed/issues/3556
ellipsis = TypeVar("ellipsis")

DefaultDataTypes = TypedDict(
    "DefaultDataTypes",
    {
        "real floating": dtype,
        "complex floating": dtype,
        "integral": dtype,
        "indexing": dtype,
    },
)
DataTypes = TypedDict(
    "DataTypes",
    {
        "bool": dtype,
        "float32": dtype,
        "float64": dtype,
        "complex64": dtype,
        "complex128": dtype,
        "int8": dtype,
        "int16": dtype,
        "int32": dtype,
        "int64": dtype,
        "uint8": dtype,
        "uint16": dtype,
        "uint32": dtype,
        "uint64": dtype,
    },
    total=False,
)
Capabilities = TypedDict(
    "Capabilities", {"boolean_indexing": bool, "data_dependent_shapes": bool}
)


@dataclass
class Info:
    """Namespace returned by `__array_namespace_info__`."""

    @staticmethod
    def capabilities() -> Capabilities:
        ...

    @staticmethod
    def default_device() -> device:
        ...

    @staticmethod
    def default_dtypes(*, device: Optional[device]) -> DefaultDataTypes:
        ...

    @staticmethod
    def devices() -> List[device]:
        ...

    @staticmethod
    def dtypes(
        *, device: Optional[device], kind: Optional[Union[str, Tuple[str, ...]]]
    ) -> DataTypes:
        ...


@dataclass
class finfo_object:
    """Dataclass returned by `finfo`."""

    bits: int
    eps: float
    max: float
    min: float
    smallest_normal: float
    dtype: dtype


@dataclass
class iinfo_object:
    """Dataclass returned by `iinfo`."""

    bits: int
    max: int
    min: int
    dtype: dtype


_T_co = TypeVar("_T_co", covariant=True)


class NestedSequence(Protocol[_T_co]):
    def __getitem__(self, key: int, /) -> Union[_T_co, NestedSequence[_T_co]]:
        ...

    def __len__(self, /) -> int:
        ...
