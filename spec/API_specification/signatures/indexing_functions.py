from ._types import Union, array

def take(x: array, indices: Union[int, array], /, *, axis: int) -> array:
    """
    Returns elements of an array along an axis.

    .. note::
       Conceptually, the call ``take(x, indices, axis=3)`` is equivalent to ``x[:,:,:,indices,...]``; however, explicit indexing via arrays of indices is not currently supported in this specification due to concerns regarding ``__setitem__`` and array mutation semantics.

    Parameters
    ----------
    x: array
        input array.
    indices: Union[int, array]
        array indices. If ``indices`` is an array, the array must be one-dimensional and have an integer data type. If ``indices`` is an integer, the function must follow single-axis indexing semantics (see :ref:`indexing`).
    axis: int
        axis over which to select values. If ``axis`` is negative, the function must determine the axis along which to select values by counting from the last dimension.

    Returns
    -------
    out: array
        an array having the same data type as ``x``. If ``indices`` is an array, the output array must have the same rank (i.e., number of dimensions) as ``x`` and must have the same shape as ``x``, except for the axis specified by ``axis`` whose size must equal the number of elements in ``indices``. If ``indices`` is an integer, the output array must have one less dimension than ``x`` (i.e., the array rank should decrease by one). In particular, if ``x`` has rank ``N``, when ``indices`` is an integer, this function must be equivalent to a selection tuple (e.g., ``x[:,:,3,:]``, ``x[0,:]``, et cetera) with the ``m``\th element an integer (and all other entries ``:``), thus indexing a sub-array with rank ``N-1``.

        .. note::
           When ``indices`` is an integer and ``x`` is an array of rank ``1``, the returned array must be an array of rank ``0``, not a scalar.
    """

__all__ = ['take']
