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

(function-matmul)=
### matmul(x1, x2, /)

Computes the matrix product.

```{note}

The `matmul` function must implement the same semantics as the built-in `@` operator (see [PEP 465](https://www.python.org/dev/peps/pep-0465)).
```

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   first input array. Should have a numeric data type. Must have at least one dimension. If `x1` is one-dimensional having shape `(M)` and `x2` has more than one dimension, `x1` must be promoted to a two-dimensional array by prepending `1` to its dimensions (i.e., must have shape `(1, M)`). After matrix multiplication, the prepended dimensions in the returned array must be removed. If `x1` has more than one dimension (including after vector-to-matrix promotion), `x1` must be compatible with `x2` (see {ref}`broadcasting`). If `x1` has shape `(..., M, K)`, the innermost two dimensions form matrices on which to perform matrix multiplication.

-   **x2**: _&lt;array&gt;_

    -   second input array. Should have a numeric data type. Must have at least one dimension. If `x2` is one-dimensional having shape `(N)` and `x1` has more than one dimension, `x2` must be promoted to a two-dimensional array by appending `1` to its dimensions (i.e., must have shape `(N, 1)`). After matrix multiplication, the appended dimensions in the returned array must be removed. If `x2` has more than one dimension (including after vector-to-matrix promotion), `x2` must be compatible with `x1` (see {ref}`broadcasting`). If `x2` has shape `(..., K, N)`, the innermost two dimensions form matrices on which to perform matrix multiplication.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if both `x1` and `x2` are one-dimensional arrays having shape `(N)`, a zero-dimensional array containing the inner product as its only element.
    -   if `x1` is a two-dimensional array having shape `(M, K)` and `x2` is a two-dimensional array having shape `(K, N)`, a two-dimensional array containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication) and having shape `(M, N)`.
    -   if `x1` is a one-dimensional array having shape `(K)` and `x2` is an array having shape `(..., K, N)`, an array having shape `(..., N)` (i.e., prepended dimensions during vector-to-matrix promotion must be removed) and containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication).
    -   if `x1` is an array having shape `(..., M, K)` and `x2` is a one-dimensional array having shape `(K)`, an array having shape `(..., M)` (i.e., appended dimensions during vector-to-matrix promotion must be removed) and containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication).
    -   if `x1` is a two-dimensional array having shape `(M, K)` and `x2` is an array having shape `(..., K, N)`, an array having shape `(..., M, N)` and containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication) for each stacked matrix.
    -   if `x1` is an array having shape `(..., M, K)` and `x2` is a two-dimensional array having shape `(K, N)`, an array having shape `(..., M, N)` and containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication) for each stacked matrix.
    -   if either `x1` or `x2` has more than two dimensions, an array having a shape determined by {ref}`broadcasting` `x1` against `x2` and containing the [conventional matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication) for each stacked matrix.

    The returned array must have a data type determined by {ref}`type-promotion`.

#### Raises

-   if either `x1` or `x2` is a zero-dimensional array.
-   if `x1` is a one-dimensional array having shape `(N)`, `x2` is a one-dimensional array having shape `(M)`, and `N != M`.
-   if `x1` is an array having shape `(..., M, K)`, `x2` is an array having shape `(..., L, N)`, and `K != L`.

(function-matrix-transpose)=
### matrix_transpose(x, /)

Transposes a matrix (or a stack of matrices) `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the transpose for each matrix and having shape `(..., N, M)`. The returned array must have the same data type as `x`.

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

-   **out**: _&lt;array&gt;_

    -   if `x1` and `x2` are both one-dimensional arrays, a zero-dimensional containing the dot product; otherwise, a non-zero-dimensional array containing the dot products and having rank `N-1`, where `N` is the rank (number of dimensions) of the shape determined according to {ref}`broadcasting`. The returned array must have a data type determined by {ref}`type-promotion`.

#### Raises

-   if provided an invalid `axis`.
-   if the size of the axis over which to compute the dot product is not the same for both `x1` and `x2`.
