__all__ = ["take"]

from ._types import Union, Optional, array


def take(x: array, indices: array, /, *, axis: Optional[int] = None) -> array:
    """
    Returns elements of an array along an axis.

    .. note::
       Conceptually, ``take(x, indices, axis=3)`` is equivalent to ``x[:,:,:,indices,...]``; however, explicit indexing via arrays of indices is not currently supported in this specification due to concerns regarding ``__setitem__`` and array mutation semantics.

    Parameters
    ----------
    x: array
        input array.
    indices: array
        array indices. The array must be one-dimensional and have an integer data type.

        .. note::
           This specification does not require bounds checking. The behavior for out-of-bounds indices is left unspecified.

    axis: Optional[int]
        axis over which to select values. If ``axis`` is negative, the function must determine the axis along which to select values by counting from the last dimension.

        If ``x`` is a one-dimensional array, providing an ``axis`` is optional; however, if ``x`` has more than one dimension, providing an ``axis`` is required.

    Returns
    -------
    out: array
        an array having the same data type as ``x``. The output array must have the same rank (i.e., number of dimensions) as ``x`` and must have the same shape as ``x``, except for the axis specified by ``axis`` whose size must equal the number of elements in ``indices``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Out-of-bounds behavior is explicitly left unspecified.
    """
