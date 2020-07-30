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

-   **out**: an array containing the evaluated exponential function result for each element in `x`.

### sqrt(x, *, out=None)

Calculates an implementation-dependent approximation to the square root for each element `x_i` of the input array `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is less than `0`, the result is `NaN`.
-   If `x_i` is `+0`, the result is `+0`.
-   If `x_i` is `-0`, the result is `-0`.
-   If `x_i` is `+infinity`, the result is `+infinity`.

* * *

## Addendum

-   Optional arguments must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   The `out` keyword argument must be a tuple with one entry per output.
-   If `out` is not provided or is `None` (the default), an uninitialized return array must be created for each output.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.