__all__ = ["argmax", "argmin", "count_nonzero", "nonzero", "searchsorted", "where"]


from ._types import Optional, Tuple, Literal, Union, array


def argmax(x: array, /, *, axis: Optional[int] = None, keepdims: bool = False) -> array:
    """
    Returns the indices of the maximum values along a specified axis.

    When the maximum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

    Parameters
    ----------
    x: array
        input array. **Should** have a real-valued data type.
    axis: Optional[int]
        axis along which to search. If ``None``, the function **must** return the index of the maximum value of the flattened array. If not ``None``, a valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be broadcast-compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes **must not** be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if ``axis`` is ``None``, a zero-dimensional array containing the index of the first occurrence of the maximum value; otherwise, a non-zero-dimensional array containing the indices of the maximum values. The returned array **must** have be the default array index data type.

    Notes
    -----

    -   For backward compatibility, conforming implementations **may** support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).
    """


def argmin(x: array, /, *, axis: Optional[int] = None, keepdims: bool = False) -> array:
    """
    Returns the indices of the minimum values along a specified axis.

    When the minimum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

    Parameters
    ----------
    x: array
        input array. **Should** have a real-valued data type.
    axis: Optional[int]
        axis along which to search. If ``None``, the function **must** return the index of the minimum value of the flattened array. If not ``None``, a valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be broadcast-compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes **must not** be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if ``axis`` is ``None``, a zero-dimensional array containing the index of the first occurrence of the minimum value; otherwise, a non-zero-dimensional array containing the indices of the minimum values. The returned array **must** have the default array index data type.

    Notes
    -----

    -   For backward compatibility, conforming implementations **may** support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).
    """


def count_nonzero(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Counts the number of array elements which are non-zero.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to count non-zero values. By default, the number of non-zero values must be computed over the entire array. If a tuple of integers, the number of non-zero values must be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be broadcast-compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes **must not** be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the number of non-zeros values was computed over the entire array, a zero-dimensional array containing the total number of non-zero values; otherwise, a non-zero-dimensional array containing the counts along the specified axes. The returned array **must** have the default array index data type.

    Notes
    -----

    -   If ``x`` has a complex floating-point data type, non-zero elements are those elements having at least one component (real or imaginary) which is non-zero.
    -   If ``x`` has a boolean data type, non-zero elements are those elements which are equal to ``True``.

    .. versionadded:: 2024.12
    """


def nonzero(x: array, /) -> Tuple[array, ...]:
    """
    Returns the indices of the array elements which are non-zero.

    .. admonition:: Data-dependent output shape
       :class: admonition important

       The shape of the output array for this function depends on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. **Must** have one or more dimensions. If ``x`` is zero-dimensional, the function **must** raise an exception.

    Returns
    -------
    out: Tuple[array, ...]
        a tuple of ``k`` arrays, one for each dimension of ``x`` and each of size ``n`` (where ``n`` is the total number of non-zero elements), containing the indices of the non-zero elements in that dimension. The indices **must** be returned in row-major, C-style order. The returned array **must** have the default array index data type.

    Notes
    -----

    -   If ``x`` has a complex floating-point data type, non-zero elements are those elements having at least one component (real or imaginary) which is non-zero.
    -   If ``x`` has a boolean data type, non-zero elements are those elements which are equal to ``True``.

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def searchsorted(
    x1: array,
    x2: Union[array, int, float],
    /,
    *,
    side: Literal["left", "right"] = "left",
    sorter: Optional[array] = None,
) -> array:
    """
    Finds the indices into ``x1`` such that, if the corresponding elements in ``x2`` were inserted before the indices, the order of ``x1``, when sorted in ascending order, would be preserved.

    Parameters
    ----------
    x1: array
        input array. **Must** be a one-dimensional array. **Should** have a real-valued data type. If ``sorter`` is ``None``, **must** be sorted in ascending order; otherwise, ``sorter`` **must** be an array of indices that sort ``x1`` in ascending order.
    x2: Union[array, int, float]
        array containing search values. **Should** have a real-valued data type.
    side: Literal['left', 'right']
        argument controlling which index is returned if a value lands exactly on an edge.

        Let ``v`` be an element of ``x2`` given by ``v = x2[j]``, where ``j`` refers to a valid index (see :ref:`indexing`).

        - If ``v`` is less than all elements in ``x1``, then ``out[j]`` **must** be ``0``.
        - If ``v`` is greater than all elements in ``x1``, then ``out[j]`` **must** be ``M``, where ``M`` is the number of elements in ``x1``.
        - Otherwise, each returned index ``i = out[j]`` **must** satisfy an index condition:

          - If ``side == 'left'``, then ``x1[i-1] < v <= x1[i]``.
          - If ``side == 'right'``, then ``x1[i-1] <= v < x1[i]``.

        Default: ``'left'``.
    sorter: Optional[array]
        array of indices that sort ``x1`` in ascending order. The array **must** have the same shape as ``x1`` and have an integer data type. Default: ``None``.

    Returns
    -------
    out: array
        an array of indices with the same shape as ``x2``. The returned array **must** have the default array index data type.

    Notes
    -----

    -   If ``x2`` is a scalar value, ``x2`` should be treated as equivalent to a zero-dimensional array having a data type determined according to :ref:`mixing-scalars-and-arrays`.
    -   For real-valued floating-point arrays, the sort order of NaNs and signed zeros is unspecified and thus implementation-dependent. Accordingly, when a real-valued floating-point array contains NaNs and signed zeros, what constitutes ascending order **may** vary among specification-conforming array libraries.
    -   While behavior for arrays containing NaNs and signed zeros is implementation-dependent, specification-conforming libraries **should**, however, ensure consistency with ``sort`` and ``argsort`` (i.e., if a value in ``x2`` is inserted into ``x1`` according to the corresponding index in the output array and ``sort`` is invoked on the resultant array, the sorted result **should** be an array in the same order).

    .. versionadded:: 2023.12

    .. versionchanged:: 2024.12
       Fixed incorrect boundary conditions.
    """


def where(
    condition: array,
    x1: Union[array, int, float, complex, bool],
    x2: Union[array, int, float, complex, bool],
    /,
) -> array:
    """
    Returns elements chosen from ``x1`` or ``x2`` depending on ``condition``.

    Parameters
    ----------
    condition: array
        when ``True``, yield ``x1_i``; otherwise, yield ``x2_i``. **Should** have a boolean data type. **Must** be broadcast-compatible with ``x1`` and ``x2`` (see :ref:`broadcasting`).
    x1: Union[array, int, float, complex, bool]
        first input array. **Must** be broadcast-compatible with ``condition`` and ``x2`` (see :ref:`broadcasting`).
    x2: Union[array, int, float, complex, bool]
        second input array. **Must** be broadcast-compatible with ``condition`` and ``x1`` (see :ref:`broadcasting`).

    Returns
    -------
    out: array
        an array with elements from ``x1`` where ``condition`` is ``True``, and elements from ``x2`` elsewhere. The returned array **must** have a data type determined by :ref:`type-promotion` rules with the arrays ``x1`` and ``x2``.

    Notes
    -----

    -   At least one of  ``x1`` and ``x2`` **must** be an array.
    -   If either ``x1`` or ``x2`` is a scalar value, the returned array **must** have a data type determined according to :ref:`mixing-scalars-and-arrays`.

    .. versionchanged:: 2024.12
       Added scalar argument support.

    .. versionchanged:: 2024.12
       Clarified that the ``condition`` argument should have a boolean data type.
    """
