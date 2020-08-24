# Sorting Functions

> Array API specification for sorting functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="argsort" href="#argsort">#</a> argsort(x, /, *, axis=-1)

Returns the indices that sort an array `x` in ascending order along a specified axis.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to sort. If set to `-1`, the function sorts along the last axis. Default: `-1`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array of indices having the same shape as `x`.

### <a name="sort" href="#sort">#</a> sort(x, /, *, axis=-1)

Returns a sorted (in ascending order) copy of an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to sort. If set to `-1`, the function sorts along the last axis. Default: `-1`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a sorted array having the same data type and shape as `x`.
