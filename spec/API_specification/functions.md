# Functions

> Array API function specification.

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

* * *

## Functions

A conforming implementation of the array API standard must provide and support the following functions.

<!-- NOTE: please keep the functions in alphabetical order -->

### abs(x, *, out=None)

Calculates the absolute value for each element `x_i` of the input array `x` (i.e., the element-wise result has the same magnitude as the respective element in `x` but has positive sign).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `-0`, the result is `+0`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the absolute value of each element in `x`.

### acos(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse cosine for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians and ranges from `+0` to `+π`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is exactly `1`, the result is `+0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse cosine of each element in `x`.

### acosh(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic cosine for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `1`, the result is `NaN`.
-   If `x_i` is `1`, the result is `+0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic cosine of each element in `x`.

### asin(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse sine for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians and ranges from `-π/2` to `+π/2`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse sine of each element in `x`.

### asinh(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic sine for each element `x_i` in the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic sine of each element in `x`.

### atan(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse tangent for each element `x_i` of the input array `x`. Each element-wise result is expressed in radians and ranges from `-π/2` to `+π/2`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is an implementation-dependent approximation to `+π/2` (rounded).
-   If `x_i` is `-infinity`, the result is an implementation-dependent approximation to `-π/2` (rounded).

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse tangent of each element in `x`.

### atanh(x, *, out=None)

Calculates an implementation-dependent approximation to the inverse hyperbolic tangent for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `-1`, the result is `NaN`.
-   If `x_i` is greater than `1`, the result is `NaN`.
-   If `x_i` is `-1`, the result is `-infinity`.
-   If `x_i` is `+1`, the result is `+infinity`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the inverse hyperbolic tangent of each element in `x`.

### ceil(x, *, out=None)

Rounds each element `x_i` of the input array `x` to the smallest (i.e., closest to `-infinity`) integer-valued number that is not less than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### cos(x, *, out=None)

Calculates an implementation-dependent approximation to the cosine for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `NaN`.
-   If `x_i` is `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the cosine of each element in `x`.

### cosh(x, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic cosine for each element `x_i` in the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic cosine of each element in `x`.

### exp(x, *, out=None)

Calculates an implementation-dependent approximation to the exponential function for each element `x_i` of the input array `x` (`e` raised to the power of `x_i`, where `e` is the base of the natural logarithm).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `1`.
-   If `x_i` is `-0`, the result is `1`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `+0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the evaluated exponential function result for each element in `x`.

### floor(x, *, out=None)

Rounds each element `x_i` of the input array `x` to the greatest (i.e., closest to `+infinity`) integer-valued number that is not greater than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### log(x, *, out=None)

Calculates an implementation-dependent approximation to the natural logarithm for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `0`, the result is `NaN`.
-   If `x_i` is `+0` or `-0`, the result is `-infinity`.
-   If `x_i` is `1`, the result is `+0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the evaluated natural logarithm for each element in `x`.

### round(x, *, out=None)

Rounds each element `x_i` of the input array `x` to the nearest integer-valued number.

-   If `x_i` is already integer-valued, the result is `x_i`.
-   If two integers are equally close to `x_i`, the result is whichever integer is farthest from `0`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

### sin(x, *, out=None)

Calculates an implementation-dependent approximation to the sine for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the sine of each element in `x`.

### sinh(x, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic sine for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.
-   If `x_i` is `-infinity`, the result is `-infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic sine of each element in `x`.

### sqrt(x, *, out=None)

Calculates an implementation-dependent approximation to the square root for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `0`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the square root of each element in `x`.

### tan(x, *, out=None)

Calculates an implementation-dependent approximation to the tangent for each element `x_i` of the input array `x`. Each element `x_i` is assumed to be expressed in radians.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity` or `-infinity`, the result is `NaN`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the tangent of each element in `x`.

### tanh(x, *, out=None)

Calculates an implementation-dependent approximation to the hyperbolic tangent for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+1`.
-   If `x_i` is `-infinity`, the result is `-1`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the hyperbolic tangent of each element in `x`.

### trunc(x, *, out=None)

Rounds each element `x_i` of the input array `x` to the integer-valued number that is closest to but no greater than `x_i`.

-   If `x_i` is already integer-valued, the result is `x_i`.

#### Parameters

-   **x**: input array.
-   **out**: output array. If provided, must be a tuple consisting of a single value: the output array. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each element-wise computation. Default: `None`.

#### Returns

-   **out**: an array containing the rounded result for each element in `x`.

* * *

## Addendum

-   Optional arguments must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   The `out` keyword argument must be a tuple with one entry per output.
-   If `out` is not provided or is `None` (the default), an uninitialized return array must be created for each output.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.