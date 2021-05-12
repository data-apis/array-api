# Linear Algebra Functions

> Array API specification for linear algebra functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-linalg-cholesky)=
### linalg.cholesky(x, /, *, upper=False)

Returns the Cholesky decomposition of a symmetric positive-definite matrix (or a stack of symmetric positive-definite matrices) `x`.

<!-- NOTE: once complex numbers are supported, each square matrix must be Hermitian. -->

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

-   **upper**: _bool_

    -   If `True`, the result must be the upper-triangular Cholesky factor. If `False`, the result must be the lower-triangular Cholesky factor. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the Cholesky factors for each square matrix. The returned array must have a floating-point data type determined by {ref}`type-promotion` and shape as `x`.

(function-cross)=
### cross(x1, x2, /, *, axis=-1)

Returns the cross product of 3-element vectors. If `x1` and `x2` are multi-dimensional arrays (i.e., both have a rank greater than `1`), then the cross-product of each pair of corresponding 3-element vectors is independently computed.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array. Should have a numeric data type.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must have the same shape as `x1`.  Should have a numeric data type.

-   **axis**: _int_

    -   the axis (dimension) of `x1` and `x2` containing the vectors for which to compute the cross product. If set to `-1`, the function computes the cross product for vectors defined by the last axis (dimension). Default: `-1`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the cross products. The returned array must have a data type determined by {ref}`type-promotion`.

(function-det)=
### det(x, /)

Returns the determinant of a square matrix (or stack of square matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `x` is a two-dimensional array, a zero-dimensional array containing the determinant; otherwise, a non-zero dimensional array containing the determinant for each square matrix. The returned array must have the same data type as `x`.

(function-diagonal)=
### diagonal(x, /, *, axis1=0, axis2=1, offset=0)

Returns the specified diagonals. If `x` has more than two dimensions, then the axes (dimensions) specified by `axis1` and `axis2` are used to determine the two-dimensional sub-arrays from which to return diagonals.

#### Parameters

-   **x**: _&lt;array&gt;_

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

    -   if `x` is a two-dimensional array, a one-dimensional array containing the diagonal; otherwise, a multi-dimensional array containing the diagonals and whose shape is determined by removing `axis1` and `axis2` and appending a dimension equal to the size of the resulting diagonals. The returned array must have the same data type as `x`.

(function-eig)=
### eig()

TODO

(function-eigvalsh)=
### eigvalsh()

TODO

(function-einsum)=
### einsum()

TODO

(function-inv)=
### inv(x, /)

Computes the multiplicative inverse of a square matrix (or a stack of square matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the multiplicative inverses. The returned array must have a floating-point data type determined by {ref}`type-promotion` and must have the same shape as `x`.

(function-linalg-lstsq)=
### linalg.lstsq(x1, x2, /, *, rtol=None)

Returns the least-squares solution to a linear matrix equation `Ax = b`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   coefficient array `A` having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a floating-point data type.

-   **x2**: _&lt;array&gt;_

    -   ordinate (or "dependent variable") array `b`. If `x2` has shape `(..., M)`, `x2` is equivalent to an array having shape `(..., M, 1)`, and `shape(x2)` must be compatible with `shape(x1)[:-1]` (see {ref}`broadcasting`). If `x2` has shape `(..., M, K)`, each column `k` defines a set of ordinate values for which to compute a solution, and `shape(x2)[:-1]` must be compatible with `shape(x1)[:-1]` (see {ref}`broadcasting`). Should have a floating-point data type.

-   **rtol**: _Optional\[ Union\[ float, &lt;array&gt; ] ]_

    -   relative tolerance for small singular values. Singular values less than or equal to `rtol * largest_singular_value` are set to zero. If a `float`, the value is equivalent to a zero-dimensional array having a data type determined by {ref}`type-promotion` (as applied to `x1` and `x2`) and must be broadcast against each matrix. If an `array`, must have a floating-point data type and must be compatible with `shape(x1)[:-2]` (see {ref}`broadcasting`). If `None`, the default value is `max(M, N) * eps`, where `eps` must be the machine epsilon associated with the floating-point data type determined by {ref}`type-promotion` (as applied to `x1` and `x2`). Default: `None`.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt;, &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple `(x, residuals, rank, s)` whose
    
        -   first element must have the field name `x` and must be an array containing the least-squares solution for each `MxN` matrix in `x1`. The array containing the solutions must have shape `(N, K)` and must have a floating-point data type determined by {ref}`type-promotion`.
        -   second element must have the field name `residuals` and must be an array containing the sum of squares residuals (i.e., the squared Euclidean 2-norm for each column in `b - Ax`). The array containing the residuals must have shape `(K,)` and must have a floating-point data type determined by {ref}`type-promotion`.
        -   third element must have the field name `rank` and must be an array containing the effective rank of each `MxN` matrix. The array containing the ranks must have shape `shape(x1)[:-2]` and must have an integer data type.
        -   fourth element must have the field name `s` and must be an array containing the singular values for each `MxN` matrix in `x1`. The array containing the singular values must have shape `(..., min(M, N))` and must have a floating-point data type determined by {ref}`type-promotion`.

(function-matmul)=
### matmul()

TODO

(function-matrix_power)=
### matrix_power()

TODO

(function-matrix_rank)=
### matrix_rank()

TODO

(function-norm)=
### norm(x, /, *, axis=None, keepdims=False, ord=None)

Computes the matrix or vector norm of `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. Should have a floating-point data type.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, int ] ] ]_

    -   If an integer, `axis` specifies the axis (dimension) along which to compute vector norms.

        If a 2-tuple, `axis` specifies the axes (dimensions) defining two-dimensional matrices for which to compute matrix norms.

        If `None`,

        -   if `x` is one-dimensional, the function must compute the vector norm.
        -   if `x` is two-dimensional, the function must compute the matrix norm.
        -   if `x` has more than two dimensions, the function must compute the vector norm over all array values (i.e., equivalent to computing the vector norm of a flattened array).

        Negative indices must be supported. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the axes (dimensions) specified by `axis` must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the axes (dimensions) specified by `axis` must not be included in the result. Default: `False`.

-   **ord**: _Optional\[ Union\[  int, float, Literal\[ inf, -inf, 'fro', 'nuc' ] ] ]_

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

        -   if matrix (or matrices), the function must compute the Frobenius norm.
        -   if vector (or vectors), the function must compute the L2-norm (Euclidean norm).

        Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the norms. If `axis` is `None`, the returned array must be a zero-dimensional array containing a vector norm. If `axis` is a scalar value (`int` or `float`), the returned array must have a rank which is one less than the rank of `x`. If `axis` is a 2-tuple, the returned array must have a rank which is two less than the rank of `x`. The returned array must have a floating-point data type determined by {ref}`type-promotion`.

(function-outer)=
### outer(x1, x2, /)

Computes the outer product of two vectors `x1` and `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first one-dimensional input array of size `N`. Should have a numeric data type.

-   **x2**: _&lt;array&gt;_

    -   second one-dimensional input array of size `M`. Should have a numeric data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a two-dimensional array containing the outer product and whose shape is `(N, M)`. The returned array must have a data type determined by {ref}`type-promotion`.

(function-linalg-pinv)=
### linalg.pinv(x, /, *, rtol=None)

Computes the (Moore-Penrose) pseudo-inverse of a matrix (or a stack of square matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a floating-point data type.

-   **rtol**: _Optional\[ Union\[ float, &lt;array&gt; ] ]_
    
    -   relative tolerance for small singular values. Singular values less than or equal to `rtol * largest_singular_value` are set to zero. If a `float`, the value is equivalent to a zero-dimensional array having a floating-point data type determined by {ref}`type-promotion` (as applied to `x`) and must be broadcast against each matrix. If an `array`, must have a floating-point data type and must be compatible with `shape(x)[:-2]` (see {ref}`broadcasting`). If `None`, the default value is `max(M, N) * eps`, where `eps` must be the machine epsilon associated with the floating-point data type determined by {ref}`type-promotion` (as applied to `x`). Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the pseudo-inverses. The returned array must have a floating-point data type determined by {ref}`type-promotion` and must have shape `(..., N, M)` (i.e., must have the same shape as `x`, except the innermost two dimensions must be transposed).

(function-qr)=
### qr()

TODO

(function-linalg-slogdet)=
### linalg.slogdet(x, /)

Returns the sign and the natural logarithm of the absolute value of the determinant of a square matrix (or a stack of square matrices) `x`.

```{note}

The purpose of this function is to calculate the determinant more accurately when the determinant is either very small or very large, as calling `det` may overflow or underflow.
```

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple (`sign`, `logabsdet`) whose
    
        -   first element must be an array containing a number representing the sign of the determinant for each square matrix.
        -   second element must be an array containing the determinant for each square matrix.
    
        For a real matrix, the sign of the determinant must be either `1`, `0`, or `-1`. If a determinant is zero, then the corresponding `sign` must be `0` and `logabsdet` must be `-infinity`. In all cases, the determinant must be equal to `sign * exp(logsabsdet)`.

        Each returned array must have shape `shape(x)[:-2]` and a floating-point data type determined by {ref}`type-promotion`.

(function-linalg-solve)=
### linalg.solve(x1, x2, /)

Returns the solution to the system of linear equations represented by the well-determined (i.e., full rank) linear matrix equation `AX = B`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   coefficient array `A` having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Must be of full rank (i.e., all rows or, equivalently, columns must be linearly independent). Should have a floating-point data type.

-   **x2**: _&lt;array&gt;_

    -   ordinate (or "dependent variable") array `B`. If `x2` has shape `(..., M)`, `x2` is equivalent to an array having shape `(..., M, 1)`, and `shape(x2)` must be compatible with `shape(x1)[:-1]` (see {ref}`broadcasting`). If `x2` has shape `(..., M, K)`, each column `k` defines a set of ordinate values for which to compute a solution, and `shape(x2)[:-1]` must be compatible with `shape(x1)[:-1]` (see {ref}`broadcasting`). Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the solution to the system `AX = B` for each square matrix. The returned array must have the same shape as `x2` (i.e., the array corresponding to `B`) and must have a floating-point data type determined by {ref}`type-promotion`.

(function-linalg-svd)=
### linalg.svd(x, /, *, full_matrices=True)

Computes the singular value decomposition `A = USV` of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.

-   **full_matrices**: _bool_

    -   If `True`, compute full-sized `u` and `v`, such that `u` has shape `(..., M, M)` and `v` has shape `(..., N, N)`. If `False`, compute on the leading `K` singular vectors, such that `u` has shape `(..., M, K)` and `v` has shape `(..., K, N)` and where `K = min(M, N)`. Default: `True`.

#### Returns

-   **out**: _Union\[ &lt;array&gt;, Tuple\[ &lt;array&gt;, ... ] ]_

    -   a namedtuple `(u, s, v)` whose
    
        -   first element must be an array whose shape depends on the value of `full_matrices` and contain unitary array(s) (i.e., the left singular vectors). The left singular vectors must be stored as columns. If `full_matrices` is `True`, the array must have shape `(..., M, M)`. If `full_matrices` is `False`, the array must have shape `(..., M, K)`, where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.
        -   second element must be an array with shape `(..., K)` that contains the vector(s) of singular values of length `K`. For each vector, the singular values must be sorted in descending order by magnitude, such that `s[..., 0]` is the largest value, `s[..., 1]` is the second largest value, et cetera. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.
        -   third element must be an array whose shape depends on the value of `full_matrices` and contain unitary array(s) (i.e., the right singular vectors). The right singular vectors must be stored as rows (i.e., the array is the adjoint). If `full_matrices` is `True`, the array must have shape `(..., N, N)`. If `full_matrices` is `False`, the array must have shape `(..., K, N)` where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.

        Each returned array must have the same floating-point data type as `x`.

(function-tensordot)=
### tensordot(x1, x2, /, *, axes=2)

Returns a tensor contraction of `x1` and `x2` over specific axes.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array. Should have a numeric data type.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see {ref}`broadcasting`). Should have a numeric data type.

-   **axes**: _Union\[ int, Tuple\[ Sequence\[ int ], Sequence\[ int ] ] ]_

    -   number of axes (dimensions) to contract or explicit sequences of axes (dimensions) for `x1` and `x2`, respectively.
       
        If `axes` is an `int` equal to `N`, then contraction must be performed over the last `N` axes of `x1` and the first `N` axes of `x2` in order. The size of each corresponding axis (dimension) must match. Must be nonnegative.

        -   If `N` equals `0`, the result is the tensor (outer) product.
        -   If `N` equals `1`, the result is the tensor dot product.
        -   If `N` equals `2`, the result is the tensor double contraction (default).
       
        If `axes` is a tuple of two sequences `(x1_axes, x2_axes)`, the first sequence must apply to `x` and the second sequence to `x2`. Both sequences must have the same length. Each axis (dimension) `x1_axes[i]` for `x1` must have the same size as the respective axis (dimension) `x2_axes[i]` for `x2`. Each sequence must consist of unique (nonnegative) integers that specify valid axes for each respective array.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the tensor contraction whose shape consists of the non-contracted axes (dimensions) of the first array `x1`, followed by the non-contracted axes (dimensions) of the second array `x2`. The returned array must have a data type determined by {ref}`type-promotion`.

(function-trace)=
### trace(x, /, *, axis1=0, axis2=1, offset=0)

Returns the sum along the specified diagonals. If `x` has more than two dimensions, then the axes (dimensions) specified by `axis1` and `axis2` are used to determine the two-dimensional sub-arrays for which to compute the trace.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. Must have at least `2` dimensions. Should have a numeric data type.

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

    -   if `x` is a two-dimensional array, the returned array must be a zero-dimensional array containing the trace; otherwise, the returned array must be a multi-dimensional array containing the traces.

        The shape of a multi-dimensional output array is determined by removing `axis1` and `axis2` and storing the traces in the last array dimension. For example, if `x` has rank `k` and shape `(I, J, K, ..., L, M, N)` and `axis1=-2` and `axis1=-1`, then a multi-dimensional output array has rank `k-2` and shape `(I, J, K, ..., L)` where

        ```text
        out[i, j, k, ..., l] = trace(a[i, j, k, ..., l, :, :])
        ```

        The returned array must have the same data type as `x`.

(function-transpose)=
### transpose(x, /, *, axes=None)

Transposes (or permutes the axes (dimensions)) of an array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axes**: _Optional\[ Tuple\[ int, ... ] ]_

    -   tuple containing a permutation of `(0, 1, ..., N-1)` where `N` is the number of axes (dimensions) of `x`. If `None`, the axes (dimensions) must be permuted in reverse order (i.e., equivalent to setting `axes=(N-1, ..., 1, 0)`). Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the transpose. The returned array must have the same data type as `x`.

(function-vecdot)=
### vecdot(x1, x2, /, *, axis=None)

Computes the (vector) dot product of two arrays.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array. Should have a numeric data type.

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `x1` (see {ref}`broadcasting`). Should have a numeric data type.

-   **axis**: _Optional\[ int ]_

    -   axis over which to compute the dot product. Must be an integer on the interval `[-N, N)`, where `N` is the rank (number of dimensions) of the shape determined according to {ref}`broadcasting`. If specified as a negative integer, the function must determine the axis along which to compute the dot product by counting backward from the last dimension (where `-1` refers to the last dimension). If `None`, the function must compute the dot product over the last axis. Default: `None`.

#### Returns

-   **out**: _&lt;array;&gt;_

    -   if `x1` and `x2` are both one-dimensional arrays, a zero-dimensional containing the dot product; otherwise, a non-zero-dimensional array containing the dot products and having rank `N-1`, where `N` is the rank (number of dimensions) of the shape determined according to {ref}`broadcasting`. The returned array must have a data type determined by {ref}`type-promotion`.

#### Raises

-   if provided an invalid `axis`.
-   if the size of the axis over which to compute the dot product is not the same for both `x1` and `x2`.
