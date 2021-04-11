# Set Functions

> Array API specification for creating and operating on sets.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-unique)=
### unique(x, /, *, return_counts=False, return_index=False, return_inverse=False)

Returns the unique elements of an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. If `x` has more than one dimension, the function must flatten `x` and return the unique elements of the flattened array.

-   **return_counts**: _bool_

    -   If `True`, the function must also return the number of times each unique element occurs in `x`. Default: `False`.

-   **return_index**: _bool_

    -   If `True`, the function must also return the indices (first occurrences) of `x` that result in the unique array. Default: `False`.

-   **return_inverse**: _bool_

    -   If `True`, the function must also return the indices of the unique array that reconstruct `x`. Default: `False`.

#### Returns

-   **out**: _Union\[ &lt;array&gt;, Tuple\[ &lt;array&gt;, ... ] ]_

    -   if `return_counts`, `return_index`, and `return_inverse` are all `False`, an array containing the set of unique elements in `x`; otherwise, a tuple containing two or more of the following arrays (in order):

        -   **unique**: _&lt;array&gt;_

            -   an array containing the set of unique elements in `x`. The returned array must have the same data type as `x`.

            ```{note}
            The order of elements is not specified, and may vary between implementations.
            ```

        -   **indices**: _&lt;array&gt;_

            -   an array containing the indices (first occurrences) of `x` that result in `unique`. The returned array must have the default array index data type.

        -   **inverse**: _&lt;array&gt;_

            -   an array containing the indices of `unique` that reconstruct `x`. The returned array must have the default array index data type.

        -   **counts**: _&lt;array&gt;_

            -   an array containing the number of times each unique element occurs in `x`.

                _TODO: should this be `int64`? This probably makes sense for most hardware; however, may be undesirable for older hardware and/or embedded systems._
