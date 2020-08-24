# Linear Algebra Functions

> Array API specification for linear algebra functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="cross" href="#cross">#</a> cross(a, b, /, *, axis=-1)

Returns the cross product of 3-element vectors. If `a` and `b` are multi-dimensional arrays (i.e., both have a rank greater than `1`), then the cross-product of each pair of corresponding 3-element vectors is independently computed.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   first input array.

-   **b**: _&lt;array&gt;_

    -   second input array. Must have the same shape as `a`. 

-   **axis**: _int_

    -   the axis of `a` and `b` containing the vectors for which to compute the cross product. If set to `-1`, the function computes the cross product for vectors defined by the last axis. Default: `-1`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the cross products.