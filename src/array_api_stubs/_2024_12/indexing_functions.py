__all__ = ["take", "take_along_axis"]

from ._types import Union, Optional, array


def take(x: array, indices: array, /, *, axis: Optional[int] = None) -> array:
    """
    Returns elements of an array along an axis.

    Parameters
    ----------
    x: array
        input array. Should have one or more dimensions (axes).
    indices: array
        array indices. The array must be one-dimensional and have an integer data type. If an index is negative, the function must determine the element to select along a specified axis (dimension) by counting from the last element (where ``-1`` refers to the last element).
    axis: Optional[int]
        axis over which to select values. If ``axis`` is negative, the function must determine the axis along which to select values by counting from the last dimension (where ``-1`` refers to the last dimension).

        If ``x`` is a one-dimensional array, providing an ``axis`` is optional; however, if ``x`` has more than one dimension, providing an ``axis`` is required.

    Returns
    -------
    out: array
        an array having the same data type as ``x``. The output array must have the same rank (i.e., number of dimensions) as ``x`` and must have the same shape as ``x``, except for the axis specified by ``axis`` whose size must equal the number of elements in ``indices``.

    Notes
    -----

    -   Conceptually, ``take(x, indices, axis=3)`` is equivalent to ``x[:,:,:,indices,...]``; however, explicit indexing via arrays of indices is not currently supported in this specification due to concerns regarding ``__setitem__`` and array mutation semantics.
    -   This specification does not require bounds checking. The behavior for out-of-bounds indices is left unspecified.
    -   When ``x`` is a zero-dimensional array, behavior is unspecified and thus implementation-defined.

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Out-of-bounds behavior is explicitly left unspecified.

    .. versionchanged:: 2024.12
       Behavior when provided a zero-dimensional input array is explicitly left unspecified.

    .. versionchanged:: 2024.12
       Clarified support for negative indices.
    """


def take_along_axis(x: array, indices: array, /, *, axis: int = -1) -> array:
    """
    Returns elements from an array at the one-dimensional indices specified by ``indices`` along a provided ``axis``.

    Parameters
    ----------
    x: array
        input array. Must be compatible with ``indices``, except for the axis (dimension) specified by ``axis`` (see :ref:`broadcasting`).
    indices: array
        array indices. Must have the same rank (i.e., number of dimensions) as ``x``. If an index is negative, the function must determine the element to select along a specified axis (dimension) by counting from the last element (where ``-1`` refers to the last element).
    axis: int
        axis along which to select values. If ``axis`` is negative, the function must determine the axis along which to select values by counting from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.

    Returns
    -------
    out: array
        an array having the same data type as ``x``. Must have the same rank (i.e., number of dimensions) as ``x`` and must have a shape determined according to :ref:`broadcasting`, except for the axis (dimension) specified by ``axis`` whose size must equal the size of the corresponding axis (dimension) in ``indices``.

    Notes
    -----

    -   This specification does not require bounds checking. The behavior for out-of-bounds indices is left unspecified.

    .. versionadded:: 2024.12
    """
