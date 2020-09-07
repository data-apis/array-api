# Creation Functions

> Array API specification for creating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="arange" href="#arange">#</a> arange(start, /, *, stop=None, step=1, dtype=None)

Returns evenly spaced values within the half-open interval `[start, stop)` as a one-dimensional array.

#### Parameters

-   **start**: _Union\[ int, float ]_

    -   if `stop` is specified, the start of interval (inclusive); otherwise, the end of the interval (exclusive). If `stop` is not specified, the default starting value is `0`.

-   **stop**: _Optional\[ Union\[ int, float ] ]_

    -   the end of the interval. Default: `None`.

        _Note: this function cannot guarantee that the interval does not include the `stop` value in those cases where `step` is not an integer and floating-point rounding errors affect the length of the output array._

-   **step**: _Union\[ int, float ]_

    -   the distance between two adjacent elements (`out[i+1] - out[i]`). Default: `1`.

-   **dtype**: _Optional\[ TODO ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values. The length of the output array must be `ceil((stop-start)/step)`.

### <a name="empty" href="#empty">#</a> empty(shape, /, *, dtype=None)

Returns an uninitialized array of given `shape` and data type.

#### Parameters

-   **shape**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ TODO ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing uninitialized data.

### <a name="empty_like" href="#empty_like">#</a> empty_like(x, /, *, dtype=None)

Returns an uninitialized array with the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape. If `dtype` is not provided, the output array data type must be inferred from `x`.

-   **dtype**: _Optional\[ TODO ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and containing uninitialized data.
