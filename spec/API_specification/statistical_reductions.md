# Statistical Reductions

> Array API specification for statistical reductions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   The `out` keyword argument must follow the conventions defined in :ref:`out-keyword`.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="max" href="#max">#</a> max(x, /, *, axis=None, keepdims=False, out=None)

Calculates the maximum value of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which maximum values must be computed. By default, the maximum value must be computed over the entire array. If a tuple of integers, maximum values must be computed over multiple axes. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ int, float, &lt;array&gt; ]_

    -   if the maximum value was computed over the entire array, the maximum value; otherwise, an array containing the maximum values.

### <a name="mean" href="#mean">#</a> mean(x, /, *, axis=None, keepdims=False, out=None)

Calculates the arithmetic mean of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which arithmetic means must be computed. By default, the mean must be computed over the entire array. If a tuple of integers, arithmetic means must be computed over multiple axes. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ float, &lt;array&gt; ]_

    -   if the arithmetic mean was computed over the entire array, the arithmetic mean; otherwise, an array containing the arithmetic means.

### <a name="min" href="#min">#</a> min(x, /, *, axis=None, keepdims=False, out=None)

Calculates the minimum value of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which minimum values must be computed. By default, the minimum value must be computed over the entire array. If a tuple of integers, minimum values must be computed over multiple axes. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ int, float, &lt;array&gt; ]_

    -   if the minimum value was computed over the entire array, the minimum value; otherwise, an array containing the minimum values.

### <a name="prod" href="#prod">#</a> prod(x, /, *, axis=None, keepdims=False, out=None)

Calculates the product of input array `x` elements.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which products must be computed. By default, the product must be computed over the entire array. If a tuple of integers, products must be computed over multiple axes. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ int, float, &lt;array&gt; ]_

    -   if the product was computed over the entire array, the product; otherwise, an array containing the products.

### <a name="std" href="#std">#</a> std(x, /, *, axis=None, correction=0.0, keepdims=False, out=None)

Calculates the standard deviation of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which standard deviations must be computed. By default, the standard deviation must be computed over the entire array. If a tuple of integers, standard deviations must be computed over multiple axes. Default: `None`.

-   **correction**: _float_

    -   degrees of freedom adjustment. Setting this parameter to a value other than `0.0` has the effect of adjusting the divisor during the calculation of the standard deviation according to `N-c` where `N` corresponds to the total number of elements over which the standard deviation is computed and `c` corresponds to the provided degrees of freedom adjustment. When computing the standard deviation of a population, setting this parameter to `0.0` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the corrected sample standard deviation, setting this parameter to `1.0` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: `0.0`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ float, &lt;array&gt; ]_

    -   if the standard deviation was computed over the entire array, the standard deviation; otherwise, an array containing the standard deviations.

### <a name="sum" href="#sum">#</a> sum(x, /, *, axis=None, keepdims=False, out=None)

Calculates the sum of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which sums must be computed. By default, the sum must be computed over the entire array. If a tuple of integers, sums must be computed over multiple axes. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ int, float, &lt;array&gt; ]_

    -   if the sum was computed over the entire array, the sum; otherwise, an array containing the sums.

### <a name="var" href="#var">#</a> var(x, /, *, axis=None, correction=0.0, keepdims=False, out=None)

Calculates the variance of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which variances must be computed. By default, the variance must be computed over the entire array. If a tuple of integers, variances must be computed over multiple axes. Default: `None`.

-   **correction**: _float_

    -   degrees of freedom adjustment. Setting this parameter to a value other than `0.0` has the effect of adjusting the divisor during the calculation of the variance according to `N-c` where `N` corresponds to the total number of elements over which the variance is computed and `c` corresponds to the provided degrees of freedom adjustment. When computing the variance of a population, setting this parameter to `0.0` is the standard choice (i.e., the provided array contains data constituting an entire population). When computing the unbiased sample variance, setting this parameter to `1.0` is the standard choice (i.e., the provided array contains data sampled from a larger population; this is commonly referred to as Bessel's correction). Default: `0.0`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ float, &lt;array&gt; ]_

    -   if the variance was computed over the entire array, the variance; otherwise, an array containing the variances.