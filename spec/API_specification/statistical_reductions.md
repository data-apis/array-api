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

### <a name="mean" href="#mean">#</a> mean(x, /, *, axis=None, keepdims=False, out=None)

Calculates the arithmetic mean of the input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis or axes along which the mean must be computed. By default, the mean must be computed over the entire array. If a tuple of integers, the mean must be computed over multiple axes.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array. Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

-   **out**: _Optional\[ &lt;array&gt; ]_

    -   output array. If provided, the output array must have the expected output shape. If not provided or is `None`, an uninitialized return array must be created and then filled with the result of each computation. Default: `None`.

#### Returns

-   **out**: _Union\[ float, &lt;array&gt; ]_

    -   if the arithmetic mean was computed over the entire array, the arithmetic mean; otherwise, an array containing the arithmetic means.