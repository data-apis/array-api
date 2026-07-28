__all__ = [
    "bincount",
    "cumulative_sum",
    "cumulative_prod",
    "max",
    "mean",
    "min",
    "prod",
    "std",
    "sum",
    "var",
]


from ._types import Optional, Tuple, Union, array, dtype


def bincount(
    x: array, /, weights: Optional[array] = None, *, minlength: int = 0
) -> array:
    """
    Counts the number of occurrences of each element in ``x``.

    .. admonition:: Data-dependent output shape
        :class: important

        The shape of the output array for this function depends on the data values in ``x``; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) can find this function difficult to implement without knowing the values in ``x``. Accordingly, such libraries **may** choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. **Should** be a one-dimensional array. **Must** have an integer data type.
    weights: Optional[array]
        an array of weights for each element in ``x``. **Must** have the same shape as ``x``. **Must** have a numeric data type. If not provided, each bin in the returned array **must** give the number of occurrences of its index value in ``x``. If provided, each bin in the returned array **must** be a sum of the weights corresponding to the respective index values in ``x`` (i.e., if value ``n`` is found at index ``i`` in ``x``, then ``out[n] += weights[i]``, instead of ``out[n] += 1``). Default: ``None``.
    minlength: int
        minimum number of bins. **Must** be a nonnegative integer. Default: ``0``.

    Returns
    -------
    out: array
        an array containing the number of occurrences. Let ``N`` equal ``max(xp.max(x)+1, minlength)``. The returned array **should** have shape ``(N,)``.

        If ``weights`` is not ``None``, the returned array **must** have the same data type as ``weights``.

        If ``weights`` is ``None``, the returned array **must** have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array **must** have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array **must** have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array **must** have a ``uint32`` data type).

    Notes
    -----

    -   If ``x`` contains negative values, behavior is unspecified and thus implementation-defined.
    """


def cumulative_prod(
    x: array,
    /,
    *,
    axis: Optional[int] = None,
    dtype: Optional[dtype] = None,
    include_initial: bool = False,
) -> array:
    """
    Calculates the cumulative product of elements in the input array ``x``.

    Parameters
    ----------
    x: array
        input array. **Should** have one or more dimensions (axes). **Should** have a numeric data type.
    axis: Optional[int]
        axis along which to compute the cumulative product. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.

        If ``x`` is a one-dimensional array, providing an ``axis`` **must** be optional; however, if ``x`` has more than one dimension, providing an ``axis`` **must** be required.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array **must** have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array **must** have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array **must** have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array **must** have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array **should** be cast to the specified data type before computing the product (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    include_initial: bool
        boolean indicating whether to include the initial value as the first value in the output. By convention, the initial value **must** be the multiplicative identity (i.e., one). Default: ``False``.

    Returns
    -------
    out: array
        an array containing the cumulative products. The returned array **must** have a data type as described by the ``dtype`` parameter above.

        Let ``M`` be the size of the axis along which to compute the cumulative product. The returned array **must** have a shape determined according to the following rules:

        -   if ``include_initial`` is ``True``, the returned array **must** have the same shape as ``x``, except the size of the axis along which to compute the cumulative product **must** be ``M+1``.
        -   if ``include_initial`` is ``False``, the returned array **must** have the same shape as ``x``.

    Notes
    -----

    -   When ``x`` is a zero-dimensional array, behavior is unspecified and thus implementation-defined.

    **Special Cases**

    For both real-valued and complex floating-point operands, special cases **must** be handled as if the operation is implemented by successive application of :func:`~array_api.multiply`.

    .. versionadded:: 2024.12
    """


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
        input array. **Should** have one or more dimensions (axes). **Should** have a numeric data type.
    axis: Optional[int]
        axis along which to compute the cumulative sum. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.

        If ``x`` is a one-dimensional array, providing an ``axis`` **must** be optional; however, if ``x`` has more than one dimension, providing an ``axis`` **must** be required.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array **must** have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array **must** have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array **must** have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array **must** have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array **should** be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    include_initial: bool
        boolean indicating whether to include the initial value as the first value in the output. By convention, the initial value **must** be the additive identity (i.e., zero). Default: ``False``.

    Returns
    -------
    out: array
        an array containing the cumulative sums. The returned array **must** have a data type as described by the ``dtype`` parameter above.

        Let ``M`` be the size of the axis along which to compute the cumulative sum. The returned array **must** have a shape determined according to the following rules:

        -   if ``include_initial`` is ``True``, the returned array **must** have the same shape as ``x``, except the size of the axis along which to compute the cumulative sum **must** be ``M+1``.
        -   if ``include_initial`` is ``False``, the returned array **must** have the same shape as ``x``.

    Notes
    -----

    -   When ``x`` is a zero-dimensional array, behavior is unspecified and thus implementation-defined.

    **Special Cases**

    For both real-valued and complex floating-point operands, special cases **must** be handled as if the operation is implemented by successive application of :func:`~array_api.add`.

    .. versionadded:: 2023.12

    .. versionchanged:: 2024.12
       Behavior when providing a zero-dimensional array is explicitly left unspecified.
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
        input array. **Should** have a real-valued data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to compute maximum values. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. By default, the maximum value **must** be computed over the entire array. If a tuple of integers, maximum values **must** be computed over multiple axes. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the maximum value is computed over the entire array, a zero-dimensional array containing the maximum value; otherwise, a non-zero-dimensional array containing the maximum values. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   When the number of elements over which to compute the maximum value is zero, the maximum value is implementation-defined. Specification-compliant libraries **may** choose to raise an error, return a sentinel value (e.g., if ``x`` is a floating-point input array, return ``NaN``), or return the minimum possible value for the input array ``x`` data type (e.g., if ``x`` is a floating-point array, return ``-infinity``).

    -   The order of signed zeros is unspecified and thus implementation-defined. When choosing between ``-0`` or ``+0`` as a maximum value, specification-compliant libraries **may** choose to return either value.

    -   For backward compatibility, conforming implementations **may** support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-defined (see :ref:`complex-number-ordering`).

    **Special Cases**

    For floating-point operands,

    -   If ``x_i`` is ``NaN``, the maximum value **must** be ``NaN`` (i.e., ``NaN`` values propagate).

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
        input array. **Should** have a floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to compute arithmetic means. By default, the mean **must** be computed over the entire array. If a tuple of integers, arithmetic means **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the arithmetic mean is computed over the entire array, a zero-dimensional array containing the arithmetic mean; otherwise, a non-zero-dimensional array containing the arithmetic means. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   While this specification recommends that this function only accept input arrays having a floating-point data type, specification-compliant array libraries **may** choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array **must** have the default real-valued floating-point data type.

    **Special Cases**

    Let ``M`` equal the number of elements over which to compute the arithmetic mean. For real-valued operands,

    -   If ``M`` is ``0``, the arithmetic mean **must** be ``NaN``.
    -   If ``x_i`` is ``NaN``, the arithmetic mean **must** be ``NaN`` (i.e., ``NaN`` values propagate).

    For complex floating-point operands, real-valued floating-point special cases **should** independently apply to the real and imaginary component operations involving real numbers. For example, let ``a = real(x_i)`` and ``b = imag(x_i)``, and

    -   If ``M`` is ``0``, the arithmetic mean **must** be ``NaN + NaN j``.
    -   If ``a`` is ``NaN``, the real component of the result **must** be ``NaN``.
    -   Similarly, if ``b`` is ``NaN``, the imaginary component of the result **must** be ``NaN``.

    .. note::
       Array libraries, such as NumPy, PyTorch, and JAX, currently deviate from this specification in their handling of components which are ``NaN`` when computing the arithmetic mean. In general, consumers of array libraries implementing this specification are recommended to use :func:`~array_api.isnan` to test whether the result of computing the arithmetic mean over an array have a complex floating-point data type is ``NaN``, rather than relying on ``NaN`` propagation of individual components.

    .. versionchanged:: 2024.12
       Added complex data type support.
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
        input array. **Should** have a real-valued data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to compute minimum values. By default, the minimum value **must** be computed over the entire array. If a tuple of integers, minimum values **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the minimum value is computed over the entire array, a zero-dimensional array containing the minimum value; otherwise, a non-zero-dimensional array containing the minimum values. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   When the number of elements over which to compute the minimum value is zero, the minimum value is implementation-defined. Specification-compliant libraries **may** choose to raise an error, return a sentinel value (e.g., if ``x`` is a floating-point input array, return ``NaN``), or return the maximum possible value for the input array ``x`` data type (e.g., if ``x`` is a floating-point array, return ``+infinity``).

    -   The order of signed zeros is unspecified and thus implementation-defined. When choosing between ``-0`` or ``+0`` as a minimum value, specification-compliant libraries **may** choose to return either value.

    -   For backward compatibility, conforming implementations **may** support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-defined (see :ref:`complex-number-ordering`).

    **Special Cases**

    For floating-point operands,

    -   If ``x_i`` is ``NaN``, the minimum value **must** be ``NaN`` (i.e., ``NaN`` values propagate).

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
        input array. **Should** have a numeric data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to compute products. By default, the product **must** be computed over the entire array. If a tuple of integers, products **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array **must** have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array **must** have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array **must** have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array **must** have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array **should** be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the product is computed over the entire array, a zero-dimensional array containing the product; otherwise, a non-zero-dimensional array containing the products. The returned array **must** have a data type as described by the ``dtype`` parameter above.

    Notes
    -----

    **Special Cases**

    Let ``M`` equal the number of elements over which to compute the product.

    -   If ``M`` is ``0``, the product **must** be `1` (i.e., the empty product).

    For both real-valued and complex floating-point operands, special cases **must** be handled as if the operation is implemented by successive application of :func:`~array_api.multiply`.

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
        input array. **Should** have a real-valued floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which to compute standard deviations. By default, the standard deviation **must** be computed over the entire array. If a tuple of integers, standard deviations **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    correction: Union[int, float]
        degrees of freedom adjustment. Setting this parameter to a value other than ``0`` has the effect of adjusting the divisor during the calculation of the standard deviation according to ``M-c`` where ``M`` corresponds to the total number of elements over which the standard deviation is computed and ``c`` corresponds to the provided degrees of freedom adjustment. When computing the standard deviation of a population, setting this parameter to ``0`` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the corrected sample standard deviation, setting this parameter to ``1`` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: ``0``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the standard deviation is computed over the entire array, a zero-dimensional array containing the standard deviation; otherwise, a non-zero-dimensional array containing the standard deviations. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   While this specification recommends that this function only accept input arrays having a real-valued floating-point data type, specification-compliant array libraries **may** choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array **must** have the default real-valued floating-point data type.

    **Special Cases**

    Let ``M`` equal the number of elements over which to compute the standard deviation.

    -   If ``M - correction`` is less than or equal to ``0``, the standard deviation **must** be ``NaN``.
    -   If ``x_i`` is ``NaN``, the standard deviation **must** be ``NaN`` (i.e., ``NaN`` values propagate).
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
        input array. **Should** have a numeric data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which sums **must** be computed. By default, the sum **must** be computed over the entire array. If a tuple of integers, sums **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.

    dtype: Optional[dtype]
        data type of the returned array. If ``None``, the returned array **must** have the same data type as ``x``, unless ``x`` has an integer data type supporting a smaller range of values than the default integer data type (e.g., ``x`` has an ``int16`` or ``uint32`` data type and the default integer data type is ``int64``). In those latter cases:

        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array **must** have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array **must** have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array **must** have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array **should** be cast to the specified data type before computing the sum (rationale: the ``dtype`` keyword argument is intended to help prevent overflows). Default: ``None``.

    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the sum is computed over the entire array, a zero-dimensional array containing the sum; otherwise, an array containing the sums. The returned array **must** have a data type as described by the ``dtype`` parameter above.

    Notes
    -----

    **Special Cases**

    Let ``M`` equal the number of elements over which to compute the sum.

    -   If ``M`` is ``0``, the sum **must** be ``0`` (i.e., the empty sum).

    For both real-valued and complex floating-point operands, special cases **must** be handled as if the operation is implemented by successive application of :func:`~array_api.add`.

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
        input array. **Should** have a real-valued floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis or axes along which variances **must** be computed. By default, the variance **must** be computed over the entire array. If a tuple of integers, variances **must** be computed over multiple axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``None``.
    correction: Union[int, float]
        degrees of freedom adjustment. Setting this parameter to a value other than ``0`` has the effect of adjusting the divisor during the calculation of the variance according to ``M-c`` where ``M`` corresponds to the total number of elements over which the variance is computed and ``c`` corresponds to the provided degrees of freedom adjustment. When computing the variance of a population, setting this parameter to ``0`` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the unbiased sample variance, setting this parameter to ``1`` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: ``0``.
    keepdims: bool
        if ``True``, the reduced axes (dimensions) **must** be included in the result as singleton dimensions, and, accordingly, the result **must** be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the reduced axes (dimensions) **must** not be included in the result. Default: ``False``.

    Returns
    -------
    out: array
        if the variance is computed over the entire array, a zero-dimensional array containing the variance; otherwise, a non-zero-dimensional array containing the variances. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   While this specification recommends that this function only accept input arrays having a real-valued floating-point data type, specification-compliant array libraries **may** choose to accept input arrays having an integer data type. While mixed data type promotion is implementation-defined, if the input array ``x`` has an integer data type, the returned array **must** have the default real-valued floating-point data type.

    **Special Cases**

    Let ``M`` equal the number of elements over which to compute the variance.

    -   If ``M - correction`` is less than or equal to ``0``, the variance **must** be ``NaN``.
    -   If ``x_i`` is ``NaN``, the variance **must** be ``NaN`` (i.e., ``NaN`` values propagate).
    """
