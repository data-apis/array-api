# Broadcasting

> Array API specification for broadcasting semantics.

## Overview

**Broadcasting** refers to the automatic (implicit) expansion of array dimensions to be of equal sizes without copying array data.

## Algorithm

Given an element-wise arithmetic operation involving two compatible arrays, an array having a singleton dimension (i.e., a dimension whose size is one) is broadcast (i.e., virtually repeated) across an array having a corresponding non-singleton dimension.

The results of the element-wise arithmetic operation must be stored in an array having a shape determined by the following algorithm.

1.  Let `x1` and `x2` both be arrays.

1.  Let `shape1` be a tuple describing the shape of array `x1`.

1.  Let `shape2` be a tuple describing the shape of array `x2`.

1.  Let `N1` be the number of dimensions of array `x1` (i.e., the result of `len(shape1)`).

1.  Let `N2` be the number of dimensions of array `x2` (i.e., the result of `len(shape2)`).

1.  Let `N` be the maximum value of `N1` and `N2` (i.e., the result of `max(N1, N2)`).

1.  Let `shape` be a temporary list of length `N` for storing the shape of the result array.

1.  Let `i` be `N-1`.

1.  Repeat, while `i >= 0`

	a.  If `N1 > i`, let `d1` be the size of dimension `n` for array `x1` (i.e., the result of `shape1[i]`); else, let `d1` be `1`.

	a.  If `N2 > i`, let `d2` be the size of dimension `n` for array `x2` (i.e., the result of `shape2[i]`); else, let `d2` be `1`.

	a.  If `d1 == 1`, then
		
		-   set `shape[i]` to `d2`.

	a.  Else, if `d2 == 1`, then

		-   set `shape[i]` to `d1`.

	a.  Else, if `d1 == d2`, then

		-   set `shape[i]` to `d1`.

	a.  Else, throw an exception.

	a.  Set `i` to `i-1`.

1.  Let `tuple(shape)` be the shape of the result array.

### Examples

The following examples demonstrate the application of the broadcasting algorithm for two compatible arrays.

```text
A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
---------------------------------
Result (4d array):  8 x 7 x 6 x 5

A      (2d array):  5 x 4
B      (1d array):      1
-------------------------
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
-------------------------
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
------------------------------
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
------------------------------
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 1
------------------------------
Result (3d array):  15 x 3 x 5
```

The following examples demonstrate array shapes which do **not** broadcast.

```text
A      (1d array):  3
B      (1d array):  4 # dimension does not match

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second dimension does not match
```