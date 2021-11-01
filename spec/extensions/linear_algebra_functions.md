(linear-algebra-extension)=
# Linear Algebra Extension

> Array API specification for linear algebra functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

## Design Principles

A principal goal of this specification is to standardize commonly implemented interfaces among array libraries. While this specification endeavors to avoid straying too far from common practice, this specification does, with due restraint, seek to address design decisions arising more from historical accident than first principles. This is especially true for linear algebra APIs, which have arisen and evolved organically over time and have often been tied to particular underlying implementations (e.g., to BLAS and LAPACK).

Accordingly, the standardization process affords the opportunity to reduce interface complexity among linear algebra APIs by inferring and subsequently codifying common design themes, thus allowing more consistent APIs. What follows is the set of design principles governing the APIs which follow:

1.  **Batching**: if an operation is explicitly defined in terms of matrices (i.e., two-dimensional arrays), then the associated interface should support "batching" (i.e., the ability to perform the operation over a "stack" of matrices). Example operations include:

    -   `inv`: computing the multiplicative inverse of a square matrix.
    -   `cholesky`: performing Cholesky decomposition.
    -   `matmul`: performing matrix multiplication.

2.  **Data types**: if an operation requires decimal operations and {ref}`type-promotion` semantics are undefined (e.g., as is the case for mixed-kind promotions), then the associated interface should be specified as being restricted to floating-point data types. While the specification uses the term "SHOULD" rather than "MUST", a conforming implementation of the array API standard should only ignore the restriction provided overly compelling reasons for doing so. Example operations which should be limited to floating-point data types include:

    -   `inv`: computing the multiplicative inverse.
    -   `slogdet`: computing the natural logarithm of the absolute value of the determinant.
    -   `norm`: computing the matrix or vector norm.

    Certain operations are solely comprised of multiplications and additions. Accordingly, associated interfaces need not be restricted to floating-point data types. However, careful consideration should be given to overflow, and use of floating-point data types may be more prudent in practice. Example operations include:

    -   `matmul`: performing matrix multiplication.
    -   `trace`: computing the sum along the diagonal.
    -   `cross`: computing the vector cross product.

    Lastly, certain operations may be performed independent of data type, and, thus, the associated interfaces should support all data types specified in this standard. Example operations include:

    -   `matrix_transpose`: computing the transpose.
    -   `diagonal`: returning the diagonal.

3.  **Return values**: if an interface has more than one return value, the interface should return a namedtuple consisting of each value.

    In general, interfaces should avoid polymorphic return values (e.g., returning an array **or** a namedtuple, dependent on, e.g., an optional keyword argument). Dedicated interfaces for each return value type are preferred, as dedicated interfaces are easier to reason about at both the implementation level and user level. Example interfaces which could be combined into a single overloaded interface, but are not, include:

    -   `eig`: computing both eigenvalues and eignvectors.
    -   `eigvals`: computing only eigenvalues.

4.  **Implementation agnosticism**: a standardized interface should eschew parameterization (including keyword arguments) biased toward particular implementations.

    Historically, at a time when all array computing happened on CPUs, BLAS and LAPACK underpinned most numerical computing libraries and environments. Naturally, language and library abstractions catered to the parameterization of those libraries, often exposing low-level implementation details verbatim in their higher-level interfaces, even if such choices would be considered poor or ill-advised by today's standards (e.g., NumPy's use of `UPLO` in `eigh`). However, the present day is considerably different. While still important, BLAS and LAPACK no longer hold a monopoly over linear algebra operations, especially given the proliferation of devices and hardware on which such operations must be performed. Accordingly, interfaces must be conservative in the parameterization they support in order to best ensure universality. Such conservatism applies even to performance optimization parameters afforded by certain hardware.

5.  **Orthogonality**: an interface should have clearly defined and delineated functionality which, ideally, has no overlap with the functionality of other interfaces in the specification. Providing multiple interfaces which can all perform the same operation creates unnecessary confusion regarding interface applicability (i.e., which interface is best at which time) and decreases readability of both library and user code. Where overlap is possible, the specification must be parsimonious in the number of interfaces, ensuring that each interface provides a unique and compelling abstraction. Examples of related interfaces which provide distinct levels of abstraction (and generality) include:

    -   `vecdot`: computing the dot product of two vectors.
    -   `matmul`: performing matrix multiplication (including between two vectors and thus the dot product).
    -   `tensordot`: computing tensor contractions (generalized sum-products).
    -   `einsum`: expressing operations in terms of Einstein summation convention, including dot products and tensor contractions.

    The above can be contrasted with, e.g., NumPy, which provides the following interfaces for computing the dot product or related operations:

    -   `dot`: dot product, matrix multiplication, and tensor contraction.
    -   `inner`: dot product.
    -   `vdot`: dot product with flattening and complex conjugation.
    -   `multi_dot`: chained dot product.
    -   `tensordot`: tensor contraction.
    -   `matmul`: matrix multiplication (dot product for two vectors).
    -   `einsum`: Einstein summation convention.

    where `dot` is overloaded based on input array dimensionality and `vdot` and `inner` exhibit a high degree of overlap with other interfaces. By consolidating interfaces and more clearly delineating behavior, this specification aims to ensure that each interface has a unique purpose and defined use case.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-linalg-cholesky)=
### linalg.cholesky(x, /, *, upper=False)

Returns the lower (upper) Cholesky decomposition x = LLᵀ (x = UᵀU) of a symmetric positive-definite matrix (or a stack of matrices) `x`, where `L` is a lower-triangular matrix or a stack of matrices (`U` is an upper-triangular matrix or a stack of matrices).

<!-- NOTE: once complex numbers are supported, each square matrix must be Hermitian. -->

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

-   **upper**: _bool_

    -   If `True`, the result must be the upper-triangular Cholesky factor `U`. If `False`, the result must be the lower-triangular Cholesky factor `L`. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the Cholesky factors for each square matrix. If `upper` is `False`, the array must contain lower-triangular matrices. Otherwise, it must contain upper-triangular matrices. The returned array must have a floating-point data type determined by {ref}`type-promotion` and shape as `x`.

(function-linalg-cross)=
### linalg.cross(x1, x2, /, *, axis=-1)

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

(function-linalg-det)=
### linalg.det(x, /)

Returns the determinant of a square matrix (or a stack of square matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `x` is a two-dimensional array, a zero-dimensional array containing the determinant; otherwise, a non-zero dimensional array containing the determinant for each square matrix. The returned array must have the same data type as `x`.

(function-linalg-diagonal)=
### linalg.diagonal(x, /, *, offset=0)

Returns the specified diagonals of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices.

-   **offset**: _int_

    -   offset specifying the off-diagonal relative to the main diagonal.

        -   `offset = 0`: the main diagonal.
        -   `offset > 0`: off-diagonal above the main diagonal.
        -   `offset < 0`: off-diagonal below the main diagonal.

        Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the diagonals and whose shape is determined by removing the last two dimensions and appending a dimension equal to the size of the resulting diagonals. The returned array must have the same data type as `x`.

(function-linalg-eigh)=
### linalg.eigh(x, /)

Returns the eigenvalues and eigenvectors x = QLQᵀ of a symmetric matrix (or a stack of matrices) `x`, where `Q` is an orthogonal matrix (or a stack of matrices) and `L` is a vector (or a stack of vectors).

<!-- NOTE: once complex number support, each matrix must be Hermitian and the returned Q unitary.
           We might also want to make the dtype of `eigenvalues` unconditionally real -->

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Must have a floating-point data type.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt; ]_

    -   a namedtuple (`eigenvalues`, `eigenvectors`) whose

        -   first element must have the field name `eigenvalues` (corresponding to `L` above) and must be an array consisting of computed eigenvalues. The array containing the eigenvalues must have shape `(..., M)`.
        -   second element have have the field name `eigenvectors` (corresponding to `Q` above) and must be an array where the columns of the inner most matrices contain the computed eigenvectors. These matrices must be orthogonal. The array containing the eigenvectors must have shape `(..., M, M)`.

        Each returned array must have the same floating-point data type as `x`.

```{note}

Eigenvalue sort order is left unspecified.
```

```{note}
The function `eig` will be added in a future version of the specification,
as it requires complex number support.
```

(function-linalg-eigvalsh)=
### linalg.eigvalsh(x, /)

Returns the eigenvalues of a symmetric matrix (or a stack of matrices) `x`.

<!-- NOTE: once complex number support, each matrix must be Hermitian -->

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Must have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the computed eigenvalues. The returned array must have shape `(..., M)` and have the same data type as `x`.

```{note}

Eigenvalue sort order is left unspecified.
```

```{note}
The function `eigvals` will be added in a future version of the specification,
as it requires complex number support.
```

(function-linalg-inv)=
### linalg.inv(x, /)

Returns the multiplicative inverse of a square matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the multiplicative inverses. The returned array must have a floating-point data type determined by {ref}`type-promotion` and must have the same shape as `x`.

(function-linalg-matmul)=
### linalg.matmul(x1, x2, /)

Alias for {ref}`function-matmul`.

(function-linalg-matrix-norm)=
### linalg.matrix_norm(x, /, *, axis=(-2, -1), keepdims=False, ord='fro')

Computes the matrix norm of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. Must have at least `2` dimensions. Should have a floating-point data type.

-   **axis**: _Tuple\[ int, int ]_

    -   a 2-tuple which specifies the axes (dimensions) defining two-dimensional matrices for which to compute matrix norms. Negative indices must be supported. Default: `(-2, -1)` (i.e., the last two-dimensions).

-   **keepdims**: _bool_

    -   If `True`, the axes (dimensions) specified by `axis` must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the axes (dimensions) specified by `axis` must not be included in the result. Default: `False`.

-   **ord**: _Optional\[ Union\[  int, float, Literal\[ inf, -inf, 'fro', 'nuc' ] ] ]_

    -   order of the norm. The following mathematical norms must be supported:
        | ord              | description                     |
        | ---------------- | ------------------------------- |
        | 'fro'            | Frobenius norm                  |
        | 'nuc'            | nuclear norm                    |
        | 1                | max(sum(abs(x), axis=0))        |
        | 2                | largest singular value          |
        | inf              | max(sum(abs(x), axis=1))        |

        The following non-mathematical "norms" must be supported:
        | ord              | description                     |
        | ---------------- | ------------------------------- |
        | -1               | min(sum(abs(x), axis=0))        |
        | -2               | smallest singular value         |
        | -inf             | min(sum(abs(x), axis=1))        |

        If `ord=1`, the norm corresponds to the induced matrix norm where `p=1` (i.e., the maximum absolute value column sum).

        If `ord=2`, the norm corresponds to the induced matrix norm where `p=inf` (i.e., the maximum absolute value row sum).

        If `ord=inf`, the norm corresponds to the induced matrix norm where `p=2` (i.e., the largest singular value).

        Default: `'fro'`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the norms. If `keepdims` is `False`, the returned array must have a rank which is two less than the rank of `x`. The returned array must have a floating-point data type determined by {ref}`type-promotion`.

(function-linalg-matrix_power)=
### linalg.matrix_power(x, n, /)

Raises a square matrix (or a stack of matrices) `x` to an integer power `n`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

-   **n**: _int_

    -   integer exponent.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `n` is equal to zero, an array containing the identity matrix for each square matrix. If `n` is less than zero, an array containing the inverse of each square matrix raised to the absolute value of `n`, provided that each square matrix is invertible. If `n` is greater than zero, an array containing the result of raising each square matrix to the power `n`. The returned array must have the same shape as `x` and a floating-point data type determined by {ref}`type-promotion`.

(function-linalg-matrix_rank)=
### linalg.matrix_rank(x, /, *, rtol=None)

Returns the rank (i.e., number of non-zero singular values) of a matrix (or a stack of matrices).

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a floating-point data type.

-   **rtol**: _Optional\[ Union\[ float, &lt;array&gt; ] ]_

    -   relative tolerance for small singular values. Singular values less than or equal to `rtol * largest_singular_value` are set to zero. If a `float`, the value is equivalent to a zero-dimensional array having a floating-point data type determined by {ref}`type-promotion` (as applied to `x`) and must be broadcast against each matrix. If an `array`, must have a floating-point data type and must be compatible with `shape(x)[:-2]` (see {ref}`broadcasting`). If `None`, the default value is `max(M, N) * eps`, where `eps` must be the machine epsilon associated with the floating-point data type determined by {ref}`type-promotion` (as applied to `x`). Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the ranks. The returned array must have a floating-point data type determined by {ref}`type-promotion` and must have shape `(...)` (i.e., must have a shape equal to `shape(x)[:-2]`).

(function-linalg-matrix-transpose)=
### linalg.matrix_transpose(x, /)

Alias for {ref}`function-matrix-transpose`.

(function-linalg-outer)=
### linalg.outer(x1, x2, /)

Returns the outer product of two vectors `x1` and `x2`.

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

Returns the (Moore-Penrose) pseudo-inverse of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a floating-point data type.

-   **rtol**: _Optional\[ Union\[ float, &lt;array&gt; ] ]_

    -   relative tolerance for small singular values. Singular values less than or equal to `rtol * largest_singular_value` are set to zero. If a `float`, the value is equivalent to a zero-dimensional array having a floating-point data type determined by {ref}`type-promotion` (as applied to `x`) and must be broadcast against each matrix. If an `array`, must have a floating-point data type and must be compatible with `shape(x)[:-2]` (see {ref}`broadcasting`). If `None`, the default value is `max(M, N) * eps`, where `eps` must be the machine epsilon associated with the floating-point data type determined by {ref}`type-promotion` (as applied to `x`). Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the pseudo-inverses. The returned array must have a floating-point data type determined by {ref}`type-promotion` and must have shape `(..., N, M)` (i.e., must have the same shape as `x`, except the innermost two dimensions must be transposed).

(function-linalg-qr)=
### linalg.qr(x, /, *, mode='reduced')

Returns the qr decomposition x = QR of a matrix (or a stack of matrices) `x`, where `Q` is an orthonormal matrix (or a stack of matrices) and `R` is an upper-triangular matrix (or a stack of matrices).

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a floating-point data type.

-   **mode**: _Literal\[ 'reduced', 'complete' ]_

    -   decomposition mode. Should be one of the following modes:

        -   `'reduced'`: compute only the leading `K` columns of `q`, such that `q` and `r` have dimensions `(..., M, K)` and `(..., K, N)`, respectively, and where `K = min(M, N)`.
        -   `'complete'`: compute `q` and `r` with dimensions `(..., M, M)` and `(..., M, N)`, respectively.

        Default: `'reduced'`.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple `(q, r)` whose

        -   first element must have the field name `q` and must be an array whose shape depends on the value of `mode` and contain matrices with orthonormal columns. If `mode` is `'complete'`, the array must have shape `(..., M, M)`. If `mode` is `'reduced'`, the array must have shape `(..., M, K)`, where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same size as those of the input `x`.
        -   second element must have the field name `r` and must be an array whose shape depends on the value of `mode` and contain upper-triangular matrices. If `mode` is `'complete'`, the array must have shape `(..., M, M)`. If `mode` is `'reduced'`, the array must have shape `(..., K, N)`, where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same size as those of the input `x`.

        Each returned array must have a floating-point data type determined by {ref}`type-promotion`.

(function-linalg-slogdet)=
### linalg.slogdet(x, /)

Returns the sign and the natural logarithm of the absolute value of the determinant of a square matrix (or a stack of matrices) `x`.

```{note}

The purpose of this function is to calculate the determinant more accurately when the determinant is either very small or very large, as calling `det` may overflow or underflow.
```

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, M)` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple (`sign`, `logabsdet`) whose

        -   first element must have the field name `sign` and must be an array containing a number representing the sign of the determinant for each square matrix.
        -   second element must have the field name `logabsdet` and must be an array containing the determinant for each square matrix.

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

Returns the singular value decomposition A = USVh of a matrix (or a stack of matrices) `x` where `U` is a matrix (or a stack of matrices) with orthonormal columns, `S` is a vector of non-negative numbers (or stack of vectors), and `Vh` is a matrix (or a stack of matrices) with orthonormal rows.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.

-   **full_matrices**: _bool_

    -   If `True`, compute full-sized `U` and `Vh`, such that `U` has shape `(..., M, M)` and `Vh` has shape `(..., N, N)`. If `False`, compute on the leading `K` singular vectors, such that `U` has shape `(..., M, K)` and `Vh` has shape `(..., K, N)` and where `K = min(M, N)`. Default: `True`.

#### Returns

<!-- NOTE: once complex number support, each U, Vh must be unitary and we might want to make the returned dtype of `S` unconditionally real -->

-   **out**: _Union\[ &lt;array&gt;, Tuple\[ &lt;array&gt;, ... ] ]_

    -   a namedtuple `(u, s, vh)` whose

        -   first element must have the field name `u` and must be an array whose shape depends on the value of `full_matrices` and contain matrices with orthonormal columns (i.e., the columns are left singular vectors). If `full_matrices` is `True`, the array must have shape `(..., M, M)`. If `full_matrices` is `False`, the array must have shape `(..., M, K)`, where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.
        -   second element must have the field name `s` and must be an array with shape `(..., K)` that contains the vector(s) of singular values of length `K`. For each vector, the singular values must be sorted in descending order by magnitude, such that `s[..., 0]` is the largest value, `s[..., 1]` is the second largest value, et cetera. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.
        -   third element must have the field name `vh` and must be an array whose shape depends on the value of `full_matrices` and contain orthonormal rows (i.e., the rows are the right singular vectors and the array is the adjoint). If `full_matrices` is `True`, the array must have shape `(..., N, N)`. If `full_matrices` is `False`, the array must have shape `(..., K, N)` where `K = min(M, N)`. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`.

        Each returned array must have the same floating-point data type as `x`.

(function-linalg-svdvals)=
### linalg.svdvals(x, /)

Returns the singular values of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array with shape `(..., K)` that contains the vector(s) of singular values of length `K`. For each vector, the singular values must be sorted in descending order by magnitude, such that `s[..., 0]` is the largest value, `s[..., 1]` is the second largest value, et cetera. The first `x.ndim-2` dimensions must have the same shape as those of the input `x`. The returned array must have the same floating-point data type as `x`.

(function-linalg-tensordot)=
### linalg.tensordot(x1, x2, /, *, axes=2)

Alias for {ref}`function-tensordot`.

(function-linalg-trace)=
### linalg.trace(x, /, *, offset=0)

Returns the sum along the specified diagonals of a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices. Should have a numeric data type.

-   **offset**: _int_

    -   offset specifying the off-diagonal relative to the main diagonal.

        -   `offset = 0`: the main diagonal.
        -   `offset > 0`: off-diagonal above the main diagonal.
        -   `offset < 0`: off-diagonal below the main diagonal.

        Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the traces and whose shape is determined by removing the last two dimensions and storing the traces in the last array dimension. For example, if `x` has rank `k` and shape `(I, J, K, ..., L, M, N)`, then an output array has rank `k-2` and shape `(I, J, K, ..., L)` where

        ```text
        out[i, j, k, ..., l] = trace(a[i, j, k, ..., l, :, :])
        ```

        The returned array must have the same data type as `x`.

(function-linalg-vecdot)=
### linalg.vecdot(x1, x2, /, *, axis=None)

Alias for {ref}`function-vecdot`.

(function-linalg-vector-norm)=
### linalg.vector_norm(x, /, *, axis=None, keepdims=False, ord=2)

Computes the vector norm of a vector (or batch of vectors) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. Should have a floating-point data type.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   If an integer, `axis` specifies the axis (dimension) along which to compute vector norms. If an n-tuple, `axis` specifies the axes (dimensions) along which to compute batched vector norms. If `None`, the vector norm must be computed over all array values (i.e., equivalent to computing the vector norm of a flattened array). Negative indices must be supported. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the axes (dimensions) specified by `axis` must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the axes (dimensions) specified by `axis` must not be included in the result. Default: `False`.

-   **ord**: _Union\[  int, float, Literal\[ inf, -inf ] ]_

    -   order of the norm. The following mathematical norms must be supported:
        | ord              | description                |
        | ---------------- | -------------------------- |
        | 1                | L1-norm (Manhattan)        |
        | 2                | L2-norm (Euclidean)        |
        | inf              | infinity norm              |
        | (int,float >= 1) | p-norm                     |

        The following non-mathematical "norms" must be supported:
        | ord              | description                    |
        | ---------------- | ------------------------------ |
        | 0                | sum(a != 0)                    |
        | -1               | 1./sum(1./abs(a))              |
        | -2               | 1./sqrt(sum(1./abs(a)\*\*2))   |
        | -inf             | min(abs(a))                    |
        | (int,float < 1)  | sum(abs(a)\*\*ord)\*\*(1./ord) |

        Default: `2`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the vector norms. If `axis` is `None`, the returned array must be a zero-dimensional array containing a vector norm. If `axis` is a scalar value (`int` or `float`), the returned array must have a rank which is one less than the rank of `x`. If `axis` is a `n`-tuple, the returned array must have a rank which is `n` less than the rank of `x`. The returned array must have a floating-point data type determined by {ref}`type-promotion`.
