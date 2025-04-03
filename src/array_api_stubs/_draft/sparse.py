from __future__ import annotations

from ._types import array

__all__ = ["from_binsparse"]


def from_binsparse(arrays: dict[str, array], descriptor: dict, /) -> array:
    """
    Returns a new array containing the data from another (array) object with a ``__binsparse__`` method.

    Parameters
    ----------
    arrays: dict[str, array]
        input constituent arrays.
    descriptor: dict
        The parsed binsparse descriptor of the array.

    Returns
    -------
    out: array
        an array containing the data in `arrays` with a format specified by `descriptor`.

        .. admonition:: Note
           :class: note

           The returned array may be either a copy or a view. See :ref:`data-interchange` for details.
    """
