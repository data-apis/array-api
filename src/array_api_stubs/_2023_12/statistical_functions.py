__all__ = ["cumulative_sum", "max", "mean", "min", "prod", "std", "sum", "var"]


from ._types import Optional, Tuple, Union, array, dtype


def cumulative_sum(
    x: array,
    /,
    *,
    axis: Optional[int] = None,
    dtype: Optional[dtype] = None,
    include_initial: bool = False,
) -> array:
    """
    Calculates the cumulative sum of elements in the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.
    axis: Optional[int]
        axis along which a cumulative sum must be computed. If ``axis`` is negative, the function must determine the axis along which to compute a cumulative sum by counting from the last dimension.

        If ``x`` is a one-dimensional array, providing an ``axis`` is optional; however, if ``x`` has more than one dimension, providing an ``axis`` is required.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array must have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array must have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array must have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array must have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array should be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    include_initial: bool
        boolean indicating whether to include the initial value as the first value in the output. By convention, the initial value must be the additive identity (i.e., zero). Default: ``False``.

    Returns
    -------
    out: array
        an array containing the cumulative sums. The returned array must have a data type as described by the ``dtype`` parameter above.

        Let ``N`` be the size of the axis along which to compute the cumulative sum. The returned array must have a shape determined according to the following rules:

        -   if ``include_initial`` is ``True``, the returned array must have the same shape as ``x``, except the size of the axis along which to compute the cumulative sum must be ``N+1``.
        -   if ``include_initial`` is ``False``, the returned array must have the same shape as ``x``.

    Notes
    -----

    **Special Cases**

    For both real-valued and complex floating-point operands, special cases must be handled as if the operation is implemented by successive application of :func:`~array_api.add`.

    .. versionadded:: 2023.12
    """


def max(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Calculates the maximum value of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which maximum values must be computed. By default, the maximum value must be computed over the entire array. If a tuple of integers, maximum values must be computed over multiple axes. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the maximum value was computed over the entire array, a zero-dimensional array containing the maximum value; otherwise, a non-zero-dimensional array containing the maximum values. The returned array must have the same data type as ``x``.

    Notes
    -----

    When the number of elements over which to compute the maximum value is zero, the maximum value is implementation-defined. Specification-compliant libraries may choose to raise an error, return a sentinel value (e.g., if ``x`` is a floating-point input array, return ``NaN``), or return the minimum possible value for the input array ``x`` data type (e.g., if ``x`` is a floating-point array, return ``-infinity``).

    The order of signed zeros is unspecified and thus implementation-defined. When choosing between ``-0`` or ``+0`` as a maximum value, specification-compliant libraries may choose to return either value.

    For backward compatibility, conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-defined (see :ref:`complex-number-ordering`).

    **Special Cases**

    For floating-point operands,

    -   If ``x_i`` is ``NaN``, the maximum value is ``NaN`` (i.e., ``NaN`` values propagate).

    .. versionchanged:: 2023.12
       Clarified that the order of signed zeros is implementation-defined.
    """


def mean(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Calculates the arithmetic mean of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which arithmetic means must be computed. By default, the mean must be computed over the entire array. If a tuple of integers, arithmetic means must be computed over multiple axes. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the arithmetic mean was computed over the entire array, a zero-dimensional array containing the arithmetic mean; otherwise, a non-zero-dimensional array containing the arithmetic means. The returned array must have the same data type as ``x``.

        .. note::
           While this specification recommends that this function only accept input arrays having a real-valued floating-point data type, specification-compliant array libraries may choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array must have the default real-valued floating-point data type.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the arithmetic mean.

    -   If ``N`` is ``0``, the arithmetic mean is ``NaN``.
    -   If ``x_i`` is ``NaN``, the arithmetic mean is ``NaN`` (i.e., ``NaN`` values propagate).
    """


def min(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
) -> array:
    """
    Calculates the minimum value of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which minimum values must be computed. By default, the minimum value must be computed over the entire array. If a tuple of integers, minimum values must be computed over multiple axes. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the minimum value was computed over the entire array, a zero-dimensional array containing the minimum value; otherwise, a non-zero-dimensional array containing the minimum values. The returned array must have the same data type as ``x``.

    Notes
    -----

    When the number of elements over which to compute the minimum value is zero, the minimum value is implementation-defined. Specification-compliant libraries may choose to raise an error, return a sentinel value (e.g., if ``x`` is a floating-point input array, return ``NaN``), or return the maximum possible value for the input array ``x`` data type (e.g., if ``x`` is a floating-point array, return ``+infinity``).

    The order of signed zeros is unspecified and thus implementation-defined. When choosing between ``-0`` or ``+0`` as a minimum value, specification-compliant libraries may choose to return either value.

    For backward compatibility, conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-defined (see :ref:`complex-number-ordering`).

    **Special Cases**

    For floating-point operands,

    -   If ``x_i`` is ``NaN``, the minimum value is ``NaN`` (i.e., ``NaN`` values propagate).

    .. versionchanged:: 2023.12
       Clarified that the order of signed zeros is implementation-defined.
    """


def prod(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    dtype: Optional[dtype] = None,
    keepdims: bool = False,
) -> array:
    """
    Calculates the product of input array ``x`` elements.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which products must be computed. By default, the product must be computed over the entire array. If a tuple of integers, products must be computed over multiple axes. Default: ``None``.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array must have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array must have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array must have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array must have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array should be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the product was computed over the entire array, a zero-dimensional array containing the product; otherwise, a non-zero-dimensional array containing the products. The returned array must have a data type as described by the ``dtype`` parameter above.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the product.

    -   If ``N`` is ``0``, the product is `1` (i.e., the empty product).

    For both real-valued and complex floating-point operands, special cases must be handled as if the operation is implemented by successive application of :func:`~array_api.multiply`.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Required the function to return a floating-point array having the same data type as the input array when provided a floating-point array.
    """


def std(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    correction: Union[int, float] = 0.0,
    keepdims: bool = False,
) -> array:
    """
    Calculates the standard deviation of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which standard deviations must be computed. By default, the standard deviation must be computed over the entire array. If a tuple of integers, standard deviations must be computed over multiple axes. Default: ``None``.
    correction: Union[int, float]
        degrees of freedom adjustment. Setting this parameter to a value other than ``0`` has the effect of adjusting the divisor during the calculation of the standard deviation according to ``N-c`` where ``N`` corresponds to the total number of elements over which the standard deviation is computed and ``c`` corresponds to the provided degrees of freedom adjustment. When computing the standard deviation of a population, setting this parameter to ``0`` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the corrected sample standard deviation, setting this parameter to ``1`` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: ``0``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the standard deviation was computed over the entire array, a zero-dimensional array containing the standard deviation; otherwise, a non-zero-dimensional array containing the standard deviations. The returned array must have the same data type as ``x``.

        .. note::
           While this specification recommends that this function only accept input arrays having a real-valued floating-point data type, specification-compliant array libraries may choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array must have the default real-valued floating-point data type.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the standard deviation.

    -   If ``N - correction`` is less than or equal to ``0``, the standard deviation is ``NaN``.
    -   If ``x_i`` is ``NaN``, the standard deviation is ``NaN`` (i.e., ``NaN`` values propagate).
    """


def sum(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    dtype: Optional[dtype] = None,
    keepdims: bool = False,
) -> array:
    """
    Calculates the sum of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which sums must be computed. By default, the sum must be computed over the entire array. If a tuple of integers, sums must be computed over multiple axes. Default: ``None``.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array must have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array must have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array must have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array must have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array should be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the sum was computed over the entire array, a zero-dimensional array containing the sum; otherwise, an array containing the sums. The returned array must have a data type as described by the ``dtype`` parameter above.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the sum.

    -   If ``N`` is ``0``, the sum is ``0`` (i.e., the empty sum).

    For both real-valued and complex floating-point operands, special cases must be handled as if the operation is implemented by successive application of :func:`~array_api.add`.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Required the function to return a floating-point array having the same data type as the input array when provided a floating-point array.
    """


def var(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    correction: Union[int, float] = 0.0,
    keepdims: bool = False,
) -> array:
    """
    Calculates the variance of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which variances must be computed. By default, the variance must be computed over the entire array. If a tuple of integers, variances must be computed over multiple axes. Default: ``None``.
    correction: Union[int, float]
        degrees of freedom adjustment. Setting this parameter to a value other than ``0`` has the effect of adjusting the divisor during the calculation of the variance according to ``N-c`` where ``N`` corresponds to the total number of elements over which the variance is computed and ``c`` corresponds to the provided degrees of freedom adjustment. When computing the variance of a population, setting this parameter to ``0`` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the unbiased sample variance, setting this parameter to ``1`` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: ``0``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) must not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the variance was computed over the entire array, a zero-dimensional array containing the variance; otherwise, a non-zero-dimensional array containing the variances. The returned array must have the same data type as ``x``.


    .. note::
       While this specification recommends that this function only accept input arrays having a real-valued floating-point data type, specification-compliant array libraries may choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array must have the default real-valued floating-point data type.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the variance.

    -   If ``N - correction`` is less than or equal to ``0``, the variance is ``NaN``.
    -   If ``x_i`` is ``NaN``, the variance is ``NaN`` (i.e., ``NaN`` values propagate).
    """
