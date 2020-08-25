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

    -   the axis (dimension) of `a` and `b` containing the vectors for which to compute the cross product. If set to `-1`, the function computes the cross product for vectors defined by the last axis (dimension). Default: `-1`.

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

### <a name="diagonal" href="#diagonal">#</a> diagonal(a, /, *, axis1=0, axis2=1, offset=0)

Returns the specified diagonals. If `a` has more than two dimensions, then the axes (dimensions) specified by `axis1` and `axis2` are used to determine the two-dimensional sub-arrays from which to return diagonals. 

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array. Must have at least `2` dimensions.

-   **axis1**: _int_

    -   first axis (dimension) with respect to which to take diagonal. Default: `0`.

-   **axis2**: _int_

    -   second axis (dimension) with respect to which to take diagonal. Default: `1`.

-   **offset**: _int_

    -   offset specifying the off-diagonal relative to the main diagonal.

        -   `offset = 0`: the main diagonal.
        -   `offset > 0`: off-diagonal above the main diagonal.
        -   `offset < 0`: off-diagonal below the main diagonal.

        Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `a` is a two-dimensional array, a one-dimensional array containing the diagonal; otherwise, a multi-dimensional array containing the diagonals and whose shape is determined by removing `axis1` and `axis2` and appending a dimension equal to the size of the resulting diagonals. Must have the same data type as `a`.

### <a name="inv" href="#inv">#</a> inv(a, /)

Computes the multiplicative inverse of a square matrix (or stack of square matrices) `a`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the multiplicative inverses. Must have the same data type and shape as `a`.

### <a name="norm" href="#norm">#</a> norm(a, /, *, axis=None, keepdims=False, ord=None)

Computes the matrix or vector norm of `a`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, int ] ] ]_

    -   If an integer, `axis` specifies the axis (dimension) along which to compute vector norms.
    
        If a 2-tuple, `axis` specifies the axes (dimensions) defining two-dimensional matrices for which to compute matrix norms.
    
        If `None`,
    
        -   if `a` is one-dimensional, the function computes the vector norm.
        -   if `a` is two-dimensional, the function computes the matrix norm.
        -   if `a` has more than two dimensions, the function computes the vector norm over all array values (i.e., equivalent to computing the vector norm of a flattened array).

        Negative indices must be supported. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the axes (dimensions) specified by `axis` must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the axes (dimensions) specified by `axis` must not be included in the result. Default: `False`.

-   **ord**: _Optional\[ int, float, Literal\[ inf, -inf, 'fro', 'nuc' ] ]_

    -   order of the norm. The following mathematical norms must be supported:

        | ord              | matrix                          | vector                     |
        | ---------------- | ------------------------------- | -------------------------- |
        | 'fro'            | 'fro'                           | -                          |
        | 'nuc'            | 'nuc'                           | -                          |
        | 1                | max(sum(abs(x), axis=0))        | L1-norm (Manhattan)        |
        | 2                | largest singular value          | L2-norm (Euclidean)        |
        | inf              | max(sum(abs(x), axis=1))        | infinity norm              |
        | (int,float >= 1) | -                               | p-norm                     |

        The following non-mathematical "norms" must be supported:

        | ord              | matrix                          | vector                         |
        | ---------------- | ------------------------------- | ------------------------------ |
        | 0                | -                               | sum(a != 0)                    |
        | -1               | min(sum(abs(x), axis=0))        | 1./sum(1./abs(a))              |
        | -2               | smallest singular value         | 1./sqrt(sum(1./abs(a)\*\*2))   |
        | -inf             | min(sum(abs(x), axis=1))        | min(abs(a))                    |
        | (int,float < 1)  | -                               | sum(abs(a)\*\*ord)\*\*(1./ord) |

        When `ord` is `None`, the following norms must be the default norms:

        | ord              | matrix                          | vector                     |
        | ---------------- | ------------------------------- | -------------------------- |
        | None             | 'fro'                           | L2-norm (Euclidean)        |
        
        where `fro` corresponds to the **Frobenius norm**, `nuc` corresponds to the **nuclear norm**, and `-` indicates that the norm is **not** supported.

        For matrices,

        -   if `ord=1`, the norm corresponds to the induced matrix norm where `p=1` (i.e., the maximum absolute value column sum).
        -   if `ord=2`, the norm corresponds to the induced matrix norm where `p=inf` (i.e., the maximum absolute value row sum).
        -   if `ord=inf`, the norm corresponds to the induced matrix norm where `p=2` (i.e., the largest singular value).

        If `None`,

        -   if matrix (or matrices), the function computes the Frobenius norm.
        -   if vector (or vectors), the function computes the L2-norm (Euclidean norm).
        
        Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the norms. Must have the same data type as `a`. If `axis` is `None`, the output array is a zero-dimensional array containing a vector norm. If `axis` is a scalar value (`int` or `float`), the output array has a rank which is one less than the rank of `a`. If `axis` is a 2-tuple, the output array has a rank which is two less than the rank of `a`.

### <a name="outer" href="#outer">#</a> outer(a, b, /)

Computes the outer product of two vectors `a` and `b`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   first one-dimensional input array of size `N`.

-   **b**: _&lt;array&gt;_

    -   second one-dimensional input array of size `M`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a two-dimensional array containing the outer product and whose shape is `NxM`.

### <a name="trace" href="#trace">#</a> trace(a, /, *, axis1=0, axis2=1, offset=0)

Returns the sum along the specified diagonals. If `a` has more than two dimensions, then the axes (dimensions) specified by `axis1` and `axis2` are used to determine the two-dimensional sub-arrays for which to compute the trace. 

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array. Must have at least `2` dimensions.

-   **axis1**: _int_

    -   first axis (dimension) with respect to which to compute the trace. Default: `0`.

-   **axis2**: _int_

    -   second axis (dimension) with respect to which to compute the trace. Default: `1`.

-   **offset**: _int_

    -   offset specifying the off-diagonal relative to the main diagonal.

        -   `offset = 0`: the main diagonal.
        -   `offset > 0`: off-diagonal above the main diagonal.
        -   `offset < 0`: off-diagonal below the main diagonal.

        Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `a` is a two-dimensional array, a zero-dimensional array containing the trace; otherwise, a multi-dimensional array containing the traces.
    
        The shape of a multi-dimensional output array is determined by removing `axis1` and `axis2` and storing the traces in the last array dimension. For example, if `a` has rank `k` and shape `(I, J, K, ..., L, M, N)` and `axis1=-2` and `axis1=-1`, then a multi-dimensional output array has rank `k-2` and shape `(I, J, K, ..., L)` where
    
        ```text
        out[i, j, k, ..., l] = trace(a[i, j, k, ..., l, :, :])
        ```

### <a name="transpose" href="#transpose">#</a> transpose(a, /, *, axes=None)

Transposes (or permutes the axes (dimensions)) of an array `a`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   input array.

-   **axes**: _Optional\[ Tuple\[ int, ... ] ]_

    -   tuple containing a permutation of `(0, 1, ..., N-1)` where `N` is the number of axes (dimensions) of `a`. If `None`, the axes (dimensions) are permuted in reverse order (i.e., equivalent to setting `axes=(N-1, ..., 1, 0)`). Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the transpose. Must have the same data type as `a`.