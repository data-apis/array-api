# Element-wise Functions

> Array API specification for element-wise functions.

## Conformance

A conforming implementation of the array API standard must provide and support all the functions, arguments, syntax, and semantics described in this specification.

A conforming implementation of the array API standard may provide additional values, objects, properties, and functions beyond those described in this specification.

* * *

## Normative References

The following referenced documents are indispensable for the application of this specification.

-   __IEEE 754-2019: IEEE Standard for Floating-Point Arithmetic.__ Institute of Electrical and Electronic Engineers, New York (2019).

* * *

## Terms and Definitions

For the purposes of this specification, the following terms and definitions apply.

### array

a (usually fixed-size) multidimensional container of items of the same type and size.

### shape

a tuple of `N` non-negative integers that specify the sizes of each dimension and where `N` corresponds to the number of dimensions.

### element-wise

an operation performed element-by-element, in which individual array elements are considered in isolation and independently of surrounding array elements.

* * *

## Functions

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   An `out` keyword argument must be a tuple with one entry per output.
-   If `out` is not provided or is `None` (the default), an uninitialized return array must be created for each output.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="abs" href="#abs">#</a> abs(x, /, *, out=None)

Calculates the absolute value for each element <code>x<sub>i</sub></code> of the input array `x` (i.e., the element-wise result has the same magnitude as the respective element in `x` but has positive sign).

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the absolute value of each element in `x`.

### <a name="acos" href="#acos">#</a> acos(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse cosine, having domain `[-1, +1]` and codomain `[+0, +π]`, for each element <code>x<sub>i</sub></code> of the input array `x`. Each element-wise result is expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is greater than `1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `-1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is exactly `1`, the result is `+0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse cosine of each element in `x`.

### <a name="acosh" href="#acosh">#</a> acosh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic cosine, having domain `[+1, +infinity]` and codomain `[+0, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `1`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array whose elements each represent the area of a hyperbolic sector.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic cosine of each element in `x`.

### <a name="add" href="#add">#</a> add(x1, x2, /, *, out=None)

Calculates the sum for each element <code>x1<sub>i</sub></code> of the input array `x1` with the respective element <code>x2<sub>i</sub></code> of the input array `x2`.

-   If either <code>x1<sub>i</sub></code> or <code>x2<sub>i</sub></code> is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: input array.
-   **x2**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the element-wise sums.

### <a name="asin" href="#asin">#</a> asin(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse sine, having domain `[-1, +1]` and codomain `[-π/2, +π/2]` for each element <code>x<sub>i</sub></code> of the input array `x`. Each element-wise result is expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is greater than `1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `-1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse sine of each element in `x`.

### <a name="asinh" href="#asinh">#</a> asinh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic sine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element <code>x<sub>i</sub></code> in the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: input array whose elements each represent the area of a hyperbolic sector.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic sine of each element in `x`.

### <a name="atan" href="#atan">#</a> atan(x, /, *, out=None)

Calculates an implementation-dependent approximation of the principal value of the inverse tangent, having domain `[-infinity, +infinity]` and codomain `[-π/2, +π/2]`, for each element <code>x<sub>i</sub></code> of the input array `x`. Each element-wise result is expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is an implementation-dependent approximation to `+π/2` (rounded).
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is an implementation-dependent approximation to `-π/2` (rounded).

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse tangent of each element in `x`.

### <a name="atanh" href="#atanh">#</a> atanh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic tangent, having domain `[-1, +1]` and codomain `[-infinity, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `-1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is greater than `1`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `-1`, the result is `-infinity`.
-   If <code>x<sub>i</sub></code> is `+1`, the result is `+infinity`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.

#### Parameters

-   **x**: input array whose elements each represent the area of a hyperbolic sector.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic tangent of each element in `x`.

### <a name="ceil" href="#ceil">#</a> ceil(x, /, *, out=None)

Rounds each element <code>x<sub>i</sub></code> of the input array `x` to the smallest (i.e., closest to `-infinity`) integer-valued number that is not less than <code>x<sub>i</sub></code>.

-   If <code>x<sub>i</sub></code> is already integer-valued, the result is <code>x<sub>i</sub></code>.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### <a name="cos" href="#cos">#</a> cos(x, /, *, out=None)

Calculates an implementation-dependent approximation to the cosine, having domain `(-infinity, +infinity)` and codomain `[-1, +1]`, for each element <code>x<sub>i</sub></code> of the input array `x`. Each element <code>x<sub>i</sub></code> is assumed to be expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array whose elements are each expressed in radians.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the cosine of each element in `x`.

### <a name="cosh" href="#cosh">#</a> cosh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic cosine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element <code>x<sub>i</sub></code> in the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array whose elements each represent a hyperbolic angle.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic cosine of each element in `x`.

### <a name="divide" href="#divide">#</a> divide(x1, x2, /, *, out=None)

Calculates the division for each element <code>x1<sub>i</sub></code> of the input array `x1` with the respective element <code>x2<sub>i</sub></code> of the input array `x2`.

-   If either <code>x1<sub>i</sub></code> or <code>x2<sub>i</sub></code> is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: dividend input array.
-   **x2**: divisor input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the element-wise results.

### <a name="exp" href="#exp">#</a> exp(x, /, *, out=None)

Calculates an implementation-dependent approximation to the exponential function, having domain `[-infinity, +infinity]` and codomain `[+0, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x` (`e` raised to the power of <code>x<sub>i</sub></code>, where `e` is the base of the natural logarithm).

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `1`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `+0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the evaluated exponential function result for each element in `x`.

### <a name="floor" href="#floor">#</a> floor(x, /, *, out=None)

Rounds each element <code>x<sub>i</sub></code> of the input array `x` to the greatest (i.e., closest to `+infinity`) integer-valued number that is not greater than <code>x<sub>i</sub></code>.

-   If <code>x<sub>i</sub></code> is already integer-valued, the result is <code>x<sub>i</sub></code>.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### <a name="log" href="#log">#</a> log(x, /, *, out=None)

Calculates an implementation-dependent approximation to the natural (base `e`) logarithm, having domain `[0, +infinity]` and codomain `[-infinity, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `0`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0` or `-0`, the result is `-infinity`.
-   If <code>x<sub>i</sub></code> is `1`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the evaluated natural logarithm for each element in `x`.

### <a name="multiply" href="#multiply">#</a> multiply(x1, x2, /, *, out=None)

Calculates the product for each element <code>x1<sub>i</sub></code> of the input array `x1` with the respective element <code>x2<sub>i</sub></code> of the input array `x2`.

-   If either <code>x1<sub>i</sub></code> or <code>x2<sub>i</sub></code> is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: input array.
-   **x2**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the element-wise products.

### <a name="round" href="#round">#</a> round(x, /, *, out=None)

Rounds each element <code>x<sub>i</sub></code> of the input array `x` to the nearest integer-valued number.

-   If <code>x<sub>i</sub></code> is already integer-valued, the result is <code>x<sub>i</sub></code>.
-   If two integers are equally close to <code>x<sub>i</sub></code>, the result is whichever integer is farthest from `0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### <a name="sin" href="#sin">#</a> sin(x, /, *, out=None)

Calculates an implementation-dependent approximation to the sine, having domain `(-infinity, +infinity)` and codomain `[-1, +1]`, for each element <code>x<sub>i</sub></code> of the input array `x`. Each element <code>x<sub>i</sub></code> is assumed to be expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array whose elements are each expressed in radians.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the sine of each element in `x`.

### <a name="sinh" href="#sinh">#</a> sinh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic sine, having domain `[-infinity, +infinity]` and codomain `[-infinity, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: input array whose elements each represent a hyperbolic angle.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic sine of each element in `x`.

### <a name="sqrt" href="#sqrt">#</a> sqrt(x, /, *, out=None)

Calculates the square root, having domain `[0, +infinity]` and codomain `[0, +infinity]`, for each element <code>x<sub>i</sub></code> of the input array `x`. After rounding, each result should be indistinguishable from the infinitely precise result (as required by IEEE 754).

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is less than `0`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the square root of each element in `x`.

### <a name="subtract" href="#subtract">#</a> subtract(x1, x2, /, *, out=None)

Calculates the difference for each element <code>x1<sub>i</sub></code> of the input array `x1` with the respective element <code>x2<sub>i</sub></code> of the input array `x2`.

-   If either <code>x1<sub>i</sub></code> or <code>x2<sub>i</sub></code> is `NaN`, the result is `NaN`.

#### Parameters

-   **x1**: input array.
-   **x2**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the element-wise differences.

### <a name="tan" href="#tan">#</a> tan(x, /, *, out=None)

Calculates an implementation-dependent approximation to the tangent, having domain `(-infinity, +infinity)` and codomain `(-infinity, +infinity)`, for each element <code>x<sub>i</sub></code> of the input array `x`. Each element <code>x<sub>i</sub></code> is assumed to be expressed in radians.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array whose elements are each expressed in radians.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the tangent of each element in `x`.

### <a name="tanh" href="#tanh">#</a> tanh(x, /, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic tangent, having domain `[-infinity, +infinity]` and codomain `[-1, +1]`, for each element <code>x<sub>i</sub></code> of the input array `x`.

-   If <code>x<sub>i</sub></code> is `NaN`, the result is `NaN`.
-   If <code>x<sub>i</sub></code> is `+0`, the result is `+0`.
-   If <code>x<sub>i</sub></code> is `-0`, the result is `-0`.
-   If <code>x<sub>i</sub></code> is `+infinity`, the result is `+1`.
-   If <code>x<sub>i</sub></code> is `-infinity`, the result is `-1`.

#### Parameters

-   **x**: input array whose elements each represent a hyperbolic angle.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic tangent of each element in `x`.

### <a name="trunc" href="#trunc">#</a> trunc(x, /, *, out=None)

Rounds each element <code>x<sub>i</sub></code> of the input array `x` to the integer-valued number that is closest to but no greater than <code>x<sub>i</sub></code>.

-   If <code>x<sub>i</sub></code> is already integer-valued, the result is <code>x<sub>i</sub></code>.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.
