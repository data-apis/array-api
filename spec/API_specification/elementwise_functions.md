# Element-wise Functions

> Array API specification for element-wise functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   The `out` keyword argument must follow the conventions defined in :ref:`out-keyword`.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="abs" href="#abs">#</a> abs(x, /, *, out=None)

Calculates the absolute value for each element `x_i` of the input array `x` (i.e., the element-wise result has the same magnitude as the respective element in `x` but has positive sign).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `-0`, the result is `+0`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the absolute value of each element in `x`.

### <a name="acos" href="#acos">#</a> acos(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse cosine, having domain `[-1, +1]` and codomain `[+0, +π]`, for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is exactly `1`, the result is `+0`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse cosine of each element in `x`.

### <a name="acosh" href="#acosh">#</a> acosh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic cosine, having domain `[+1, +infinity]` and codomain `[+0, +infinity]`, for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `1`, the result is `NaN`.
-   If `x_i` is `1`, the result is `+0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent the area of a hyperbolic sector.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse hyperbolic cosine of each element in `x`.

### <a name="add" href="#add">#</a> add(x1, x2, /, *, out=None)

Calculates the sum for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise sums.

### <a name="asin" href="#asin">#</a> asin(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse sine, having domain `[-1, +1]` and codomain `[-π/2, +π/2]` for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse sine of each element in `x`.

### <a name="asinh" href="#asinh">#</a> asinh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic sine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element `x_i` in the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent the area of a hyperbolic sector.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse hyperbolic sine of each element in `x`.

### <a name="atan" href="#atan">#</a> atan(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse tangent, having domain `[-infinity, +infinity]` and codomain `[-π/2, +π/2]`, for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is an implementation-dependent approximation to `+π/2` (rounded).
-   If `x_i` is `-infinity`, the result is an implementation-dependent approximation to `-π/2` (rounded).

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse tangent of each element in `x`.

### <a name="atanh" href="#atanh">#</a> atanh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic tangent, having domain `[-1, +1]` and codomain `[-infinity, +infinity]`, for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is `-1`, the result is `-infinity`.
-   If `x_i` is `+1`, the result is `+infinity`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent the area of a hyperbolic sector.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the inverse hyperbolic tangent of each element in `x`.

### <a name="ceil" href="#ceil">#</a> ceil(x, /, *, out=None)

Rounds each element `x_i` of the input array `x` to the smallest (i.e., closest to `-infinity`) integer-valued number that is not less than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the rounded result for each element in `x`.

### <a name="cos" href="#cos">#</a> cos(x, /, *, out=None)

Calculates an implementation-dependent approximation to the cosine, having domain `(-infinity, +infinity)` and codomain `[-1, +1]`, for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `NaN`.
-   If `x_i` is `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements are each expressed in radians.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the cosine of each element in `x`.

### <a name="cosh" href="#cosh">#</a> cosh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic cosine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element `x_i` in the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent a hyperbolic angle.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the hyperbolic cosine of each element in `x`.

### <a name="divide" href="#divide">#</a> divide(x1, x2, /, *, out=None)

Calculates the division for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   dividend input array.

-   **x2**: _&lt;array&gt;_

    -   divisor input array. Must be compatible with `x1` (see :ref:`broadcasting`).

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="equal" href="#equal">#</a> equal(x1, x2, /, *, out=None)

Computes the truth value of `x1_i == x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="exp" href="#exp">#</a> exp(x, /, *, out=None)

Calculates an implementation-dependent approximation to the exponential function, having domain `[-infinity, +infinity]` and codomain `[+0, +infinity]`, for each element `x_i` of the input array `x` (`e` raised to the power of `x_i`, where `e` is the base of the natural logarithm).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `+0`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the evaluated exponential function result for each element in `x`.

### <a name="floor" href="#floor">#</a> floor(x, /, *, out=None)

Rounds each element `x_i` of the input array `x` to the greatest (i.e., closest to `+infinity`) integer-valued number that is not greater than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the rounded result for each element in `x`.

### <a name="greater" href="#greater">#</a> greater(x1, x2, /, *, out=None)

Computes the truth value of `x1_i > x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="greater_equal" href="#greater_equal">#</a> greater_equal(x1, x2, /, *, out=None)

Computes the truth value of `x1_i >= x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="less" href="#less">#</a> less(x1, x2, /, *, out=None)

Computes the truth value of `x1_i < x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="less_equal" href="#less_equal">#</a> less_equal(x1, x2, /, *, out=None)

Computes the truth value of `x1_i <= x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="log" href="#log">#</a> log(x, /, *, out=None)

Calculates an implementation-dependent approximation to the natural (base `e`) logarithm, having domain `[0, +infinity]` and codomain `[-infinity, +infinity]`, for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `0`, the result is `NaN`.
-   If `x_i` is `+0` or `-0`, the result is `-infinity`.
-   If `x_i` is `1`, the result is `+0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the evaluated natural logarithm for each element in `x`.

### <a name="logical_and" href="#logical_and">#</a> logical_and(x1, x2, /, *, out=None)

Computes the logical AND for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`. Zeros should be considered the equivalent of `False`, while non-zeros should be considered the equivalent of `True`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="logical_not" href="#logical_not">#</a> logical_not(x, /, *, out=None)

Computes the logical NOT for each element `x_i` of the input array `x`. Zeros should be considered the equivalent of `False`, while non-zeros should be considered the equivalent of `True`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array `x` (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="logical_or" href="#logical_or">#</a> logical_or(x1, x2, /, *, out=None)

Computes the logical OR for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`. Zeros should be considered the equivalent of `False`, while non-zeros should be considered the equivalent of `True`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="logical_xor" href="#logical_xor">#</a> logical_xor(x1, x2, /, *, out=None)

Computes the logical XOR for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`. Zeros must should be considered the equivalent of `False`, while non-zeros must should be considered the equivalent of `True`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="multiply" href="#multiply">#</a> multiply(x1, x2, /, *, out=None)

Calculates the product for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`).

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise products.

### <a name="not_equal" href="#not_equal">#</a> not_equal(x1, x2, /, *, out=None)

Computes the truth value of `x1_i != x2_i` for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`). 

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array, whose underlying data type is `bool`, must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

### <a name="round" href="#round">#</a> round(x, /, *, out=None)

Rounds each element `x_i` of the input array `x` to the nearest integer-valued number.

-   If `x_i` is already integer-valued, the result is `x_i`.
-   If two integers are equally close to `x_i`, the result is whichever integer is farthest from `0`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the rounded result for each element in `x`.

### <a name="sin" href="#sin">#</a> sin(x, /, *, out=None)

Calculates an implementation-dependent approximation to the sine, having domain `(-infinity, +infinity)` and codomain `[-1, +1]`, for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements are each expressed in radians.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the sine of each element in `x`.

### <a name="sinh" href="#sinh">#</a> sinh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic sine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent a hyperbolic angle.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the hyperbolic sine of each element in `x`.

### <a name="sqrt" href="#sqrt">#</a> sqrt(x, /, *, out=None)

Calculates the square root, having domain `[0, +infinity]` and codomain `[0, +infinity]`, for each element `x_i` of the input array `x`. After rounding, each result should be indistinguishable from the infinitely precise result (as required by IEEE 754).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `0`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the square root of each element in `x`.

### <a name="subtract" href="#subtract">#</a> subtract(x1, x2, /, *, out=None)

Calculates the difference for each element `x1_i` of the input array `x1` with the respective element `x2_i` of the input array `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see :ref:`broadcasting`).

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input arrays (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise differences.

### <a name="tan" href="#tan">#</a> tan(x, /, *, out=None)

Calculates an implementation-dependent approximation to the tangent, having domain `(-infinity, +infinity)` and codomain `(-infinity, +infinity)`, for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements are each expressed in radians.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the tangent of each element in `x`.

### <a name="tanh" href="#tanh">#</a> tanh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic tangent, having domain `[-infinity, +infinity]` and codomain `[-1, +1]`, for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+1`.
-   If `x_i` is `-infinity`, the result is `-1`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array whose elements each represent a hyperbolic angle.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the hyperbolic tangent of each element in `x`.

### <a name="trunc" href="#trunc">#</a> trunc(x, /, *, out=None)

Rounds each element `x_i` of the input array `x` to the integer-valued number that is closest to but no greater than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **out**:  _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must be compatible with the provided input array (see :ref:`broadcasting`). If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the rounded result for each element in `x`.
