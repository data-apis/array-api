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

### <a name="det" href="#det">#</a> det(a, /)

Returns the determinant of a square matrix (or stack of square matrices) `a`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `a` is a two-dimensional array, a zero-dimensional array containing the determinant; otherwise, a non-zero dimensional array containing the determinant for each square matrix.

### <a name="diagonal" href="#diagonal">#</a> diagonal(a, /, *, offset=0, axis1=0, axis2=1)

Returns the specified diagonals. If `a` has more than two dimensions, then the axes specified by `axis1` and `axis2` are used to determine the two-dimensional sub-arrays from which to return diagonals. 

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array. Must have at least `2` dimensions.

-   **offset**: _int_

    -   offset specifying the off-diagonal relative to the main diagonal.

        -   `offset = 0`: the main diagonal.
        -   `offset > 0`: off-diagonal above the main diagonal.
        -   `offset < 0`: off-diagonal below the main diagonal.

    Default: `0`.

-   **axis1**: _int_

    -   first axis with respect to which to take diagonal. Default: `0`.

-   **axis2**: _int_

    -   second axis with respect to which to take diagonal. Default: `1`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `a` is a two-dimensional array, a one-dimensional array containing the diagonal; otherwise, a multi-dimensional array containing the diagonals and whose shape is determined by removing `axis1` and `axis2` and appending a dimension equal to the size of the resulting diagonals. The returned array must have the same type as `a`.
