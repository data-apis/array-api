__all__ = ["ArrayAPINamespace"]

from typing import Protocol

from .creation_functions import arange as ArangeCallable


class ArrayAPINamespace(Protocol):
    """Protocol for the array API namespace itself."""

    arange: ArangeCallable
