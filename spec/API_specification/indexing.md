.. _indexing:

# Indexing

> Array API specification for indexing arrays.

A conforming implementation of the array API standard must adhere to the following conventions.

## Single-Axis Indexing

To index a single array axis, an array must support standard Python indexing rules.

1.  Indices must start at `0` (i.e., zero-based indexing). Valid positive indices must reside on the interval `[0, n)`, where `n` is the axis (dimension) size.

2.  Negative indices must count backward from the last array index, starting from `-1` (where `-1` refers to the last index). Valid negative indices must reside on the interval `[-n, -1]`, where `n` is the axis (dimension) size. To convert a negative index `j` to a zero-based positive index `i`, evaluate `i = n+j`.

3.  Colons `:` must be used for slices: `start:stop:step`, where `start` is inclusive and `stop` is exclusive.

### Slice Syntax

The basic slice syntax is `i:j:k` where `i` is the starting index, `j` is the stopping index, and `k` is the step (`k != 0`).

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

    The starting index `i` is **always** included, while the stopping index `j` is **always** excluded. This preserves `x[:i]+x[i:]` always being equal to `x`.

Slice syntax must have the following defaults. Let `n` be the axis (dimension) size.

1.  If `k` is not provided (e.g., `0:10`), `k` must equal `1`.
2.  If `k > 0` and `i` is not provided (e.g., `:10:2`), `i` must equal `0`.
3.  If `k > 0` and `j` is not provided (e.g., `0::2`), `j` must equal `n`.
4.  If `k < 0` and `i` is not provided (e.g., `:10:-2`), `i` must equal `n-1`.
5.  If `k < 0` and `j` is not provided (e.g., `0::-2`), `j` must equal `-n-1`.

Indexing via `:` and `::` must be equivalent and have defaults derived from the rules above. Both `:` and `::` indicate to select all elements along a single axis (dimension).

## Multi-Axis Indexing

Multi-dimensional arrays must extend the concept of single-axis indexing to multiple axes by applying single-axis indexing rules along each axis (dimension) and supporting the following additional rules. Let `N` be the number of dimensions of a multi-dimensional array `A`.

1.  Each axis may be independently indexed via single-axis indexing by providing a comma-separated sequence (selection tuple) of single-axis indexing expressions (e.g., `A[:, 2:10, :]`).

.. note::

    In Python, `x[(exp1, exp2, ..., expN)]` is equivalent to `x[exp1, exp2, ..., expN]`; the latter is just syntactic sugar for the former.

2.  Providing a single integer as a single-axis index must index the same elements as the slice `i:i+1`.

3.  Providing a single integer as a single-axis index must reduce the number of array dimensions by `1` (i.e., the array rank should decrease by one; if `A` has rank `2`, `rank(A)-1 == rank(A[0, :])`). In particular, a selection tuple with the `m`th element an integer (and all other entries `:`) indexes the corresponding sub-array with rank `N-1`.

4.  Providing a slice must retain array dimensions (i.e., the array rank must remain the same; `rank(A) == rank(A[:])`).

5.  If the number of provided single-axis indexing expressions is less than `N`, then `:` must be assumed for the remaining dimensions (e.g., if `A` has rank `2`, `A[2:10] == A[2:10, :]`).

6.  Providing ellipsis must apply `:` to each dimension necessary to index all dimensions (e.g., if `A` has rank `4`, `A[1:, ..., 2:5] == A[1:, :, :, 2:5]`). Only a single ellipsis must be allowed. An exception must be raised if more than one ellipsis is provided. 
