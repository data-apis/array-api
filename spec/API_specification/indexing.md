.. _indexing:

# Indexing

> Array API specification for indexing arrays.

A conforming implementation of the array API standard must adhere to the following conventions.

## Single-axis Indexing

To index a single array axis, an array must support standard Python indexing rules. Let `n` be the axis (dimension) size.

-   An integer index must be an object satisfying [`operator.index`](https://www.python.org/dev/peps/pep-0357/) (e.g., `int`).

-   Nonnegative indices must start at `0` (i.e., zero-based indexing).

-   **Valid** nonnegative indices must reside on the half-open interval `[0, n)`.

    .. note::

        This specification does not explicitly require bounds checking. The behavior for out-of-bounds integer indices is left unspecified.

-   Negative indices must count backward from the last array index, starting from `-1` (i.e., negative-one-based indexing, where `-1` refers to the last array index).

    .. note::

        A negative index `j` is equivalent to `n-j`; the former is syntactic sugar for the latter, providing a shorthand for indexing elements that would otherwise need to be specified in terms of the axis (dimension) size.

-   **Valid** negative indices must reside on the closed interval `[-n, -1]`.

    .. note::

        This specification does not explicitly require bounds checking. The behavior for out-of-bounds integer indices is left unspecified.

-   A negative index `j` is related to a zero-based nonnegative index `i` via `i = n+j`.

-   Colons `:` must be used for [slices](https://docs.python.org/3/library/functions.html?highlight=slice#slice): `start:stop:step`, where `start` is inclusive and `stop` is exclusive.

### Slice Syntax

The basic slice syntax is `i:j:k` where `i` is the starting index, `j` is the stopping index, and `k` is the step (`k != 0`). A slice may contain either one or two colons, with either an integer value or nothing on either side of each colon. The following are valid slices.

```text
A[:]
A[i:]
A[:j]
A[i:k]
A[::]
A[i::]
A[:j:]
A[::k]
A[i:j:]
A[i::k]
A[:j:k]
A[i::k]
A[i:j:k]
```

.. note::

    Slice syntax can be equivalently achieved using the Python built-in [`slice()`](https://docs.python.org/3/library/functions.html?highlight=slice#slice) API. From the perspective from `A`, the behavior of `A[i:j:k]` and `A[slice(i, j, k)]` are indistinguishable (i.e., both retrieve the same set of items from `__getitem__`).

Using a slice to index a single array axis must select `m` elements with index values

```text
i, i+k, i+2k, i+3k, ..., i+(m-1)k
```

where

```text
m = q + r
```

and `q` and `r` (`r != 0`) are the quotient and remainder obtained by dividing `j-i` by `k`

```text
j - i = qk + r
```

such that

```text
j > i + (m-1)k
```

.. note::

    For `i < j`, **valid** integer index `i`, and positive step `k`, a starting index `i` is **always** included, while the stopping index `j` is **always** excluded. This preserves `x[:i]+x[i:]` always being equal to `x`.

.. note::

    Using a slice to index into a single array axis should select the same elements as using a slice to index a Python list of the same size.

Slice syntax must have the following defaults. Let `n` be the axis (dimension) size.

-   If `k` is not provided (e.g., `0:10`), `k` must equal `1`.
-   If `k > 0` and `i` is not provided (e.g., `:10:2`), `i` must equal `0`.
-   If `k > 0` and `j` is not provided (e.g., `0::2`), `j` must equal `n`.
-   If `k < 0` and `i` is not provided (e.g., `:10:-2`), `i` must equal `n-1`.
-   If `k < 0` and `j` is not provided (e.g., `0::-2`), `j` must equal `-n-1`.

Indexing via `:` and `::` must be equivalent and have defaults derived from the rules above. Both `:` and `::` indicate to select all elements along a single axis (dimension).

## Multi-axis Indexing

Multi-dimensional arrays must extend the concept of single-axis indexing to multiple axes by applying single-axis indexing rules along each axis (dimension) and supporting the following additional rules. Let `N` be the number of dimensions ("rank") of a multi-dimensional array `A`.

-   Each axis may be independently indexed via single-axis indexing by providing a comma-separated sequence ("selection tuple") of single-axis indexing expressions (e.g., `A[:, 2:10, :, 5]`).

    .. note::

        In Python, `x[(exp1, exp2, ..., expN)]` is equivalent to `x[exp1, exp2, ..., expN]`; the latter is syntactic sugar for the former.

-   Providing a single integer as a single-axis index must index the same elements as the slice `i:i+1`.

-   Providing a single integer as a single-axis index must reduce the number of array dimensions by `1` (i.e., the array rank should decrease by one; if `A` has rank `2`, `rank(A)-1 == rank(A[0, :])`). In particular, a selection tuple with the `m`th element an integer (and all other entries `:`) indexes a sub-array with rank `N-1`.

-   Providing a slice must retain array dimensions (i.e., the array rank must remain the same; `rank(A) == rank(A[:])`).

-   If the number of provided single-axis indexing expressions is less than `N`, then `:` must be assumed for the remaining dimensions (e.g., if `A` has rank `2`, `A[2:10] == A[2:10, :]`).

-   Providing [ellipsis](https://docs.python.org/3/library/constants.html#Ellipsis) must apply `:` to each dimension necessary to index all dimensions (e.g., if `A` has rank `4`, `A[1:, ..., 2:5] == A[1:, :, :, 2:5]`). Only a single ellipsis must be allowed. An exception must be raised if more than one ellipsis is provided. 

## Boolean Array Indexing

