__all__ = ["DType"]

from typing import Protocol


class DType(Protocol):
    def __eq__(self, other: "DType", /) -> bool:
        """
        Computes the truth value of ``self == other`` in order to test for data type object equality.

        Parameters
        ----------
        self: dtype
            data type instance. May be any supported data type.
        other: dtype
            other data type instance. May be any supported data type.

        Returns
        -------
        out: bool
            a boolean indicating whether the data type objects are equal.
        """
        ...
