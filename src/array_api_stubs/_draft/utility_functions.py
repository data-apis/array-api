__all__ = ["all", "any", "diff"]


from ._types import Optional, Tuple, Union, array


def all(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Tests whether all input array elements evaluate to ``True`` along a specified axis.

    .. note::
       Positive infinity, negative infinity, and NaN must evaluate to ``True``.

    .. note::
       If ``x`` has a complex floating-point data type, elements having a non-zero component (real or imaginary) must evaluate to ``True``.

    .. note::
       If ``x`` is an empty array or the size of the axis (dimension) along which to evaluate elements is zero, the test result must be ``True``.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to perform a logical AND reduction. By default, a logical AND reduction must be performed over the entire array. If a tuple of integers, logical AND reductions must be performed over multiple axes. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to perform a reduction by counting backward from the last dimension (where ``-1`` refers to the last dimension). If provided an invalid ``axis``, the function must raise an exception. Default: ``None``.
    keepdims: bool
        If ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if a logical AND reduction was performed over the entire array, the returned array must be a zero-dimensional array containing the test result; otherwise, the returned array must be a non-zero-dimensional array containing the test results. The returned array must have a data type of ``bool``.

    Notes
    -----

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def any(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Tests whether any input array element evaluates to ``True`` along a specified axis.

    .. note::
       Positive infinity, negative infinity, and NaN must evaluate to ``True``.

    .. note::
       If ``x`` has a complex floating-point data type, elements having a non-zero component (real or imaginary) must evaluate to ``True``.

    .. note::
       If ``x`` is an empty array or the size of the axis (dimension) along which to evaluate elements is zero, the test result must be ``False``.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to perform a logical OR reduction. By default, a logical OR reduction must be performed over the entire array. If a tuple of integers, logical OR reductions must be performed over multiple axes. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to perform a reduction by counting backward from the last dimension (where ``-1`` refers to the last dimension). If provided an invalid ``axis``, the function must raise an exception. Default: ``None``.
    keepdims: bool
        If ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if a logical OR reduction was performed over the entire array, the returned array must be a zero-dimensional array containing the test result; otherwise, the returned array must be a non-zero-dimensional array containing the test results. The returned array must have a data type of ``bool``.

    Notes
    -----

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def diff(
    x: array,
    /,
    *,
    axis: int = -1,
    n: int = 1,
    prepend: Optional[array] = None,
    append: Optional[array] = None,
) -> array:
    """
    Calculates the n-th discrete forward difference along a specified axis.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.
    axis: int
        axis along which to compute differences. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute differences by counting backward from the last dimension (where ``-1`` refers to the last dimension). If provided an invalid ``axis``, the function must raise an exception. Default: ``-1``.
    n: int
        number of times to recursively compute differences. Default: ``1``.
    prepend: Optional[array]
        values to prepend to a specified axis prior to computing differences. Must have the same shape as ``x``, except for the axis specified by ``axis`` which may have any size. Should have the same data type as ``x``. Default: ``None``.
    append: Optional[array]
        values to append to a specified axis prior to computing differences. Must have the same shape as ``x``, except for the axis specified by ``axis`` which may have any size. Should have the same data type as ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array containing the n-th differences. Should have the same data type as ``x``. Must have the same shape as ``x``, except for the axis specified by ``axis`` which must have a size determined as follows:

        -   Let ``M`` be the number of elements along an axis specified by ``axis``.
        -   Let ``N1`` be the number of prepended values along an axis specified by ``axis``.
        -   Let ``N2`` be the number of appended values along an axis specified by ``axis``.
        -   The final size of the axis specified by ``axis`` must be ``M + N1 + N2 - n``.

    Notes
    -----

    -   The first-order differences are given by ``out[i] = x[i+1] - x[i]`` along a specified axis. Higher-order differences must be calculated recursively (e.g., by calling ``diff(out, axis=axis, n=n-1)``).
    -   If a conforming implementation chooses to support ``prepend`` and ``append`` arrays which have a different data type than ``x``, the ``prepend`` and ``append`` arrays should promote to the same data type as ``x`` (see :ref:`type-promotion`). If ``prepend`` and ``append`` do not promote to the same data type as ``x`` or are of a different data type "kind" (integer, real-valued floating-point, or complex floating-point), behavior is unspecified and thus implementation-defined.
    """
