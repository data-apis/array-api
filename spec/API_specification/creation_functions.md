# Creation Functions

> Array API specification for creating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-arange)=
### arange(start, /, stop=None, step=1, *, dtype=None, device=None)

Returns evenly spaced values within the half-open interval `[start, stop)` as a one-dimensional array.

#### Parameters

-   **start**: _Union\[ int, float ]_

    -   if `stop` is specified, the start of interval (inclusive); otherwise, the end of the interval (exclusive). If `stop` is not specified, the default starting value is `0`.

-   **stop**: _Optional\[ Union\[ int, float ] ]_

    -   the end of the interval. Default: `None`.

```{note}

This function cannot guarantee that the interval does not include the `stop` value in those cases where `step` is not an integer and floating-point rounding errors affect the length of the output array.
```

-   **step**: _Union\[ int, float ]_

    -   the distance between two adjacent elements (`out[i+1] - out[i]`). Must not be `0`; may be negative, this results in an empty array if `stop >= start`. Default: `1`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `start`, `stop` and `step`. If those are all integers, the output array dtype must be the default integer dtype; if one or more have type `float`, then the output array dtype must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values. The length of the output array must be `ceil((stop-start)/step)` if `stop - start` and `step` have the same sign, and length 0 otherwise.


(function-asarray)=
### asarray(obj, /, *, dtype=None, device=None, copy=None)

Convert the input to an array.

#### Parameters

-   **obj**: _Union\[ &lt;array&gt;, bool, int, float, NestedSequence\[ bool | int | float ], SupportsDLPack, SupportsBufferProtocol ]_

    -   object to be converted to an array. May be a Python scalar, a (possibly nested) sequence of Python scalars, or an object supporting DLPack or the Python buffer protocol.

    :::{tip}
    An object supporting DLPack has `__dlpack__` and `__dlpack_device__` methods.
    An object supporting the buffer protocol can be turned into a memoryview through `memoryview(obj)`.
    :::

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from the data type(s) in `obj`. If all input values are Python scalars, then

        -   if all values are of type `bool`, the output data type must be `bool`.
        -   if the values are a mixture of `bool`s and `int`, the output data type must be the default integer data type.
        -   if one or more values are `float`s, the output data type must be the default floating-point data type.

        Default: `None`.

        ```{note}
        If `dtype` is not `None`, then array conversions should obey {ref}`type-promotion` rules. Conversions not specified according to {ref}`type-promotion` rules may or may not be permitted by a conforming array library.

        To perform an explicit cast, use {ref}`function-astype`.
        ```

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. If `device` is `None` and `x` is either an array or an object supporting DLPack, the output array device must be inferred from `x`. Default: `None`.

-   **copy**: _Optional\[ bool ]_

    -   boolean indicating whether or not to copy the input. If `True`, the function must always copy. If `False`, the function must never copy for input which supports DLPack or the buffer protocol and must raise a `ValueError` in case a copy would be necessary. If `None`, the function must reuse existing memory buffer if possible and copy otherwise. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the data from `obj`.


(function-empty)=
### empty(shape, *, dtype=None, device=None)

Returns an uninitialized array having a specified `shape`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing uninitialized data.

(function-empty_like)=
### empty_like(x, /, *, dtype=None, device=None)

Returns an uninitialized array with the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. If `device` is `None`, the output array device must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and containing uninitialized data.

(function-eye)=
### eye(n_rows, n_cols=None, /, *, k=0, dtype=None, device=None)

Returns a two-dimensional array with ones on the `k`th diagonal and zeros elsewhere.

#### Parameters

-   **n_rows**: _int_

    -   number of rows in the output array.

-   **n_cols**: _Optional\[ int ]_

    -   number of columns in the output array. If `None`, the default number of columns in the output array is equal to `n_rows`. Default: `None`.

-   **k**: _int_

    -   index of the diagonal. A positive value refers to an upper diagonal, a negative value to a lower diagonal, and `0` to the main diagonal. Default: `0`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array where all elements are equal to zero, except for the `k`th diagonal, whose values are equal to one.

(function-from_dlpack)=
### from_dlpack(x, /)

Returns a new array containing the data from another (array) object with a `__dlpack__` method.

#### Parameters

-   **x**: _object_

    -   input (array) object.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the data in `x`.

        ```{note}
        The returned array may be either a copy or a view. See {ref}`data-interchange` for details.
        ```

(function-full)=
### full(shape, fill_value, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with `fill_value`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **fill_value**: _Union\[ int, float ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `fill_value`. If the fill value is an `int`, the output array data type must be the default integer data type. If the fill value is a `float`, the output array data type must be the default floating-point data type. If the fill value is a `bool`, the output array must have boolean data type. Default: `None`.

        ```{note}
        If `dtype` is `None` and the `fill_value` exceeds the precision of the resolved default output array data type, behavior is left unspecified and, thus, implementation-defined.
        ```

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array where every element is equal to `fill_value`.

(function-full_like)=
### full_like(x, /, fill_value, *, dtype=None, device=None)

Returns a new array filled with `fill_value` and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **fill_value**: _Union\[ int, float ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

        ```{note}
        If `dtype` is `None` and the `fill_value` exceeds the precision of the resolved output array data type, behavior is unspecified and, thus, implementation-defined.
        ```

        ```{note}
        If `dtype` is `None` and the `fill_value` has a data type (`int` or `float`) which is not of the same data type kind as the resolved output array data type (see {ref}`type-promotion`), behavior is unspecified and, thus, implementation-defined.
        ```

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. If `device` is `None`, the output array device must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and where every element is equal to `fill_value`.

(function-linspace)=
### linspace(start, stop, /, num, *, dtype=None, device=None, endpoint=True)

Returns evenly spaced numbers over a specified interval.

#### Parameters

-   **start**: _Union\[ int, float ]_

    -   the start of the interval.

-   **stop**: _Union\[ int, float ]_

    -   the end of the interval. If `endpoint` is `False`, the function must generate a sequence of `num+1` evenly spaced numbers starting with `start` and ending with `stop` and exclude the `stop` from the returned array such that the returned array consists of evenly spaced numbers over the half-open interval `[start, stop)`. If `endpoint` is `True`, the output array must consist of evenly spaced numbers over the closed interval `[start, stop]`. Default: `True`.

        ```{note}

        The step size changes when `endpoint` is `False`.
        ```

-   **num**: _int_

    -   number of samples. Must be a non-negative integer value; otherwise, the function must raise an exception.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

-   **endpoint**: _bool_

    -   boolean indicating whether to include `stop` in the interval. Default: `True`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values.

(function-meshgrid)=
### meshgrid(*arrays, indexing='xy')

Returns coordinate matrices from coordinate vectors.

#### Parameters

-    **arrays**: _&lt;array&gt;_

     -   an arbitrary number of one-dimensional arrays representing grid coordinates. Each array should have the same numeric data type.

-    **indexing**: _str_

     -   Cartesian 'xy' or matrix 'ij' indexing of output. If provided zero or one one-dimensional vector(s) (i.e., the zero- and one-dimensional cases, respectively), the `indexing` keyword has no effect and should be ignored. Default: `'xy'`.

#### Returns

-    **out**: _List\[ &lt;array&gt;, ... ]_

     -   list of N arrays, where `N` is the number of provided one-dimensional input arrays. Each returned array must have rank `N`. For `N` one-dimensional arrays having lengths `Ni = len(xi)`,

         -   if matrix indexing `ij`, then each returned array must have the shape `(N1, N2, N3, ..., Nn)`.

         -   if Cartesian indexing `xy`, then each returned array must have shape `(N2, N1, N3, ..., Nn)`.

         Accordingly, for the two-dimensional case with input one-dimensional arrays of length `M` and `N`, if matrix indexing `ij`, then each returned array must have shape `(M, N)`, and, if Cartesian indexing `xy`, then each returned array must have shape `(N, M)`.

         Similarly, for the three-dimensional case with input one-dimensional arrays of length `M`, `N`, and `P`, if matrix indexing `ij`, then each returned array must have shape `(M, N, P)`, and, if Cartesian indexing `xy`, then each returned array must have shape `(N, M, P)`.

         Each returned array should have the same data type as the input arrays.

(function-ones)=
### ones(shape, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with ones.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing ones.

(function-ones_like)=
### ones_like(x, /, *, dtype=None, device=None)

Returns a new array filled with ones and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. If `device` is `None`, the output array device must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with ones.

(function-tril)=
### tril(x, /, *, k=0)

Returns the lower triangular part of a matrix (or a stack of matrices) `x`.

```{note}
The lower triangular part of the matrix is defined as the elements on and below the specified diagonal `k`.
```

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices.

-   **k**: _int_

    -   diagonal above which to zero elements. If `k = 0`, the diagonal is the main diagonal. If `k < 0`, the diagonal is below the main diagonal. If `k > 0`, the diagonal is above the main diagonal. Default: `0`.

        ```{note}
        The main diagonal is defined as the set of indices `{(i, i)}` for `i` on the interval `[0, min(M, N) - 1]`.
        ```

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the lower triangular part(s). The returned array must have the same shape and data type as `x`. All elements above the specified diagonal `k` must be zeroed. The returned array should be allocated on the same device as `x`.

(function-triu)=
### triu(x, /, *, k=0)

Returns the upper triangular part of a matrix (or a stack of matrices) `x`.

```{note}
The upper triangular part of the matrix is defined as the elements on and above the specified diagonal `k`.
```

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array having shape `(..., M, N)` and whose innermost two dimensions form `MxN` matrices.

-   **k**: _int_

    -   diagonal below which to zero elements. If `k = 0`, the diagonal is the main diagonal. If `k < 0`, the diagonal is below the main diagonal. If `k > 0`, the diagonal is above the main diagonal. Default: `0`.

        ```{note}
        The main diagonal is defined as the set of indices `{(i, i)}` for `i` on the interval `[0, min(M, N) - 1]`.
        ```

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the upper triangular part(s). The returned array must have the same shape and data type as `x`. All elements below the specified diagonal `k` must be zeroed. The returned array should be allocated on the same device as `x`.

(function-zeros)=
### zeros(shape, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with zeros.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing zeros.

(function-zeros_like)=
### zeros_like(x, /, *, dtype=None, device=None)

Returns a new array filled with zeros and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device on which to place the created array. If `device` is `None`, the output array device must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with zeros.
