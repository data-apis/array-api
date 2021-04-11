# Utility Functions

> Array API specification for utility functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-all)=
### all(x, /, *, axis=None, keepdims=False)

Tests whether all input array elements evaluate to `True` along a specified axis.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which to perform a logical AND reduction. By default, a logical AND reduction must be performed over the entire array. If a tuple of integers, logical AND reductions must be performed over multiple axes. A valid `axis` must be an integer on the interval `[-N, N)`, where `N` is the rank (number of dimensions) of `x`. If an `axis` is specified as a negative integer, the function must determine the axis along which to perform a reduction by counting backward from the last dimension (where `-1` refers to the last dimension). If provided an invalid `axis`, the function must raise an exception. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if a logical AND reduction was performed over the entire array, the returned array must be a zero-dimensional array containing the test result; otherwise, the returned array must be a non-zero-dimensional array containing the test results. The returned array must have a data type of `bool`.

(function-any)=
### any(x, /, *, axis=None, keepdims=False)

Tests whether any input array element evaluates to `True` along a specified axis.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which to perform a logical OR reduction. By default, a logical OR reduction must be performed over the entire array. If a tuple of integers, logical OR reductions must be performed over multiple axes. A valid `axis` must be an integer on the interval `[-N, N)`, where `N` is the rank (number of dimensions) of `x`. If an `axis` is specified as a negative integer, the function must determine the axis along which to perform a reduction by counting backward from the last dimension (where `-1` refers to the last dimension). If provided an invalid `axis`, the function must raise an exception. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if a logical OR reduction was performed over the entire array, the returned array must be a zero-dimensional array containing the test result; otherwise, the returned array must be a non-zero-dimensional array containing the test results. The returned array must have a data type of `bool`.
