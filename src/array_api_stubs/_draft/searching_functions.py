__all__ = [
    "argmax",
    "argmin",
    "nonzero",
    "top_k",
    "top_k_values",
    "top_k_indices",
    "where",
]


from ._types import Optional, Literal, Tuple, array


def argmax(x: array, /, *, axis: Optional[int] = None, keepdims: bool = False) -> array:
    """
    Returns the indices of the maximum values along a specified axis.

    When the maximum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

    .. note::
       For backward compatibility, conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    axis: Optional[int]
        axis along which to search. If ``None``, the function must return the index of the maximum value of the flattened array. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if ``axis`` is ``None``, a zero-dimensional array containing the index of the first occurrence of the maximum value; otherwise, a non-zero-dimensional array containing the indices of the maximum values. The returned array must have be the default array index data type.
    """


def argmin(x: array, /, *, axis: Optional[int] = None, keepdims: bool = False) -> array:
    """
    Returns the indices of the minimum values along a specified axis.

    When the minimum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

    .. note::
       For backward compatibility, conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    axis: Optional[int]
        axis along which to search. If ``None``, the function must return the index of the minimum value of the flattened array. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if ``axis`` is ``None``, a zero-dimensional array containing the index of the first occurrence of the minimum value; otherwise, a non-zero-dimensional array containing the indices of the minimum values. The returned array must have the default array index data type.
    """


def nonzero(x: array, /) -> Tuple[array, ...]:
    """
    Returns the indices of the array elements which are non-zero.

    .. note::
       If ``x`` has a complex floating-point data type, non-zero elements are those elements having at least one component (real or imaginary) which is non-zero.

    .. note::
       If ``x`` has a boolean data type, non-zero elements are those elements which are equal to ``True``.

    .. admonition:: Data-dependent output shape
       :class: admonition important

       The shape of the output array for this function depends on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. Must have a positive rank. If ``x`` is zero-dimensional, the function must raise an exception.

    Returns
    -------
    out: Typle[array, ...]
        a tuple of ``k`` arrays, one for each dimension of ``x`` and each of size ``n`` (where ``n`` is the total number of non-zero elements), containing the indices of the non-zero elements in that dimension. The indices must be returned in row-major, C-style order. The returned array must have the default array index data type.

    Notes
    -----

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def top_k(
    x: array,
    k: int,
    /,
    *,
    axis: Optional[int] = None,
    mode: Literal["largest", "smallest"] = "largest",
) -> Tuple[array, array]:
    """
    Returns the ``k`` largest (or smallest) elements of an input array ``x`` along a specified dimension.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    k: int
        number of elements to find. Must be a positive integer value.
    axis: Optional[int]
        axis along which to search. If ``None``, the function must search the flattened array. Default: ``None``.
    mode: Literal['largest', 'smallest']
        search mode. Must be one of the following modes:

        -  ``'largest'``: return the ``k`` largest elements.
        -  ``'smallest'``: return the ``k`` smallest elements.

    Returns
    -------
    out: Tuple[array, array]
        a namedtuple ``(values, indices)`` whose

        - first element must have the field name ``values`` and must be an array containing the ``k`` largest (or smallest) elements of ``x``. The array must have the same data type as ``x``. If ``axis`` is ``None``, the array must be a one-dimensional array having shape ``(k,)``; otherwise, if ``axis`` is an integer value, the array must have the same rank (number of dimensions) and shape as ``x``, except for the axis specified by ``axis`` which must have size ``k``.
        - second element must have the field name ``indices`` and must be an array containing indices of ``x`` that result in ``values``. The array must have the same shape as ``values`` and must have the default array index data type. If ``axis`` is ``None``, ``indices`` must be the indices of a flattened ``x``.

    Notes
    -----

    -   If ``k`` exceeds the number of elements in ``x`` or along the axis specified by ``axis``, behavior is left unspecified and thus implementation-dependent. Conforming implementations may choose, e.g., to raise an exception or return all elements.
    -   The order of the returned values and indices is left unspecified and thus implementation-dependent. Conforming implementations may return sorted or unsorted values.
    -   Conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).
    """


def top_k_indices(
    x: array,
    k: int,
    /,
    *,
    axis: Optional[int] = None,
    mode: Literal["largest", "smallest"] = "largest",
) -> array:
    """
    Returns the indices of the ``k`` largest (or smallest) elements of an input array ``x`` along a specified dimension.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    k: int
        number of elements to find. Must be a positive integer value.
    axis: Optional[int]
        axis along which to search. If ``None``, the function must search the flattened array. Default: ``None``.
    mode: Literal['largest', 'smallest']
        search mode. Must be one of the following modes:

        -  ``'largest'``: return the indices of the ``k`` largest elements.
        -  ``'smallest'``: return the indices of the ``k`` smallest elements.

    Returns
    -------
    out: array
        an array containing indices corresponding to the ``k`` largest (or smallest) elements of ``x``. The array must have the default array index data type.  If ``axis`` is ``None``, the array must be a one-dimensional array having shape ``(k,)`` and contain the indices of a flattened ``x``; otherwise, if ``axis`` is an integer value, the array must have the same rank (number of dimensions) and shape as ``x``, except for the axis specified by ``axis`` which must have size ``k``.

    Notes
    -----

    -   If ``k`` exceeds the number of elements in ``x`` or along the axis specified by ``axis``, behavior is left unspecified and thus implementation-dependent. Conforming implementations may choose, e.g., to raise an exception or return all indices.
    -   The order of the returned indices is left unspecified and thus implementation-dependent. Conforming implementations may return indices corresponding to sorted or unsorted values.
    -   Conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).
    """


def top_k_values(
    x: array,
    k: int,
    /,
    *,
    axis: Optional[int] = None,
    mode: Literal["largest", "smallest"] = "largest",
) -> array:
    """
    Returns the ``k`` largest (or smallest) elements of an input array ``x`` along a specified dimension.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    k: int
        number of elements to find. Must be a positive integer value.
    axis: Optional[int]
        axis along which to search. If ``None``, the function must search the flattened array. Default: ``None``.
    mode: Literal['largest', 'smallest']
        search mode. Must be one of the following modes:

        -  ``'largest'``: return the indices of the ``k`` largest elements.
        -  ``'smallest'``: return the indices of the ``k`` smallest elements.

    Returns
    -------
    out: array
        an array containing the ``k`` largest (or smallest) elements of ``x``. The array must have the same data type as ``x``.  If ``axis`` is ``None``, the array must be a one-dimensional array having shape ``(k,)``; otherwise, if ``axis`` is an integer value, the array must have the same rank (number of dimensions) and shape as ``x``, except for the axis specified by ``axis`` which must have size ``k``.

    Notes
    -----

    -   If ``k`` exceeds the number of elements in ``x`` or along the axis specified by ``axis``, behavior is left unspecified and thus implementation-dependent. Conforming implementations may choose, e.g., to raise an exception or return all indices.
    -   The order of the returned values is left unspecified and thus implementation-dependent. Conforming implementations may return sorted or unsorted values.
    -   Conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).
    """


def where(condition: array, x1: array, x2: array, /) -> array:
    """
    Returns elements chosen from ``x1`` or ``x2`` depending on ``condition``.

    Parameters
    ----------
    condition: array
        when ``True``, yield ``x1_i``; otherwise, yield ``x2_i``. Must be compatible with ``x1`` and ``x2`` (see :ref:`broadcasting`).
    x1: array
        first input array. Must be compatible with ``condition`` and ``x2`` (see :ref:`broadcasting`).
    x2: array
        second input array. Must be compatible with ``condition`` and ``x1`` (see :ref:`broadcasting`).

    Returns
    -------
    out: array
        an array with elements from ``x1`` where ``condition`` is ``True``, and elements from ``x2`` elsewhere. The returned array must have a data type determined by :ref:`type-promotion` rules with the arrays ``x1`` and ``x2``.
    """
