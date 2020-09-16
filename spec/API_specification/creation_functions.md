# Creation Functions

> Array API specification for creating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="arange" href="#arange">#</a> arange(start, /, *, stop=None, step=1, dtype=None)

Returns evenly spaced values within the half-open interval `[start, stop)` as a one-dimensional array.

#### Parameters

-   **start**: _Union\[ int, float ]_

    -   if `stop` is specified, the start of interval (inclusive); otherwise, the end of the interval (exclusive). If `stop` is not specified, the default starting value is `0`.

-   **stop**: _Optional\[ Union\[ int, float ] ]_

    -   the end of the interval. Default: `None`.

.. note::

    This function cannot guarantee that the interval does not include the `stop` value in those cases where `step` is not an integer and floating-point rounding errors affect the length of the output array.

-   **step**: _Union\[ int, float ]_

    -   the distance between two adjacent elements (`out[i+1] - out[i]`). Default: `1`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values. The length of the output array must be `ceil((stop-start)/step)`.

### <a name="empty" href="#empty">#</a> empty(shape, /, *, dtype=None)

Returns an uninitialized array having a specified `shape`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing uninitialized data.

### <a name="empty_like" href="#empty_like">#</a> empty_like(x, /, *, dtype=None)

Returns an uninitialized array with the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and containing uninitialized data.

### <a name="eye" href="#eye">#</a> eye(N, /, *, M=None, k=0, dtype=None)

Returns a two-dimensional array with ones on the `k`th diagonal and zeros elsewhere.

#### Parameters

-   **N**: _int_

    -   number of rows in the output array.

-   **M**: _Optional\[ int ]_

    -   number of columns in the output array. If `None`, the default number of columns in the output array is `N`. Default: `None`.

-   **k**: _Optional\[ int ]_

    -   index of the diagonal. A positive value refers to an upper diagonal, a negative value to a lower diagonal, and `0` to the main diagonal. Default: `0`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array where all elements are equal to zero, except for the `k`th diagonal, whose values are equal to one.

### <a name="full" href="#full">#</a> full(shape, fill_value, /, *, dtype=None)

Returns a new array having a specified `shape` and filled with `fill_value`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **fill_value**: _Union\[ int, float ] ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array where every element is equal to `fill_value`.

### <a name="full_like" href="#full_like">#</a> full_like(x, fill_value, /, *, dtype=None)

Returns a new array filled with `fill_value` and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **fill_value**: _Union\[ int, float ] ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and where every element is equal to `fill_value`.

### <a name="linspace" href="#linspace">#</a> linspace(start, stop, num, /, *, dtype=None, endpoint=True)

Returns evenly spaced numbers over a specified interval.

#### Parameters

-   **start**: _Union\[ int, float ]_

    -   the start of the interval.

-   **stop**: _Union\[ int, float ]_

    -   the end of the interval. If `endpoint` is `False`, the function must generate a sequence of `num+1` evenly spaced numbers starting with `start` and ending with `stop` and exclude the `stop` from the returned array such that the returned array consists of evenly spaced numbers over the half-open interval `[start, stop)`. If `endpoint` is `True`, the output array must consist of evenly spaced numbers over the closed interval `[start, stop]`. Default: `True`.
       
        _Note: that the step size changes when `endpoint` is `False`._

-   **num**: _int_

    -   number of samples. Must be a non-negative integer value; otherwise, the function must raise an exception.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

-   **endpoint**: _Optional\[ bool ]_

    -   boolean indicating whether to include `stop` in the interval. Default: `True`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values.

### <a name="ones" href="#ones">#</a> ones(shape, /, *, dtype=None)

Returns a new array having a specified `shape` and filled with ones.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing ones.

### <a name="ones_like" href="#ones_like">#</a> ones_like(x, /, *, dtype=None)

Returns a new array filled with ones and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with ones.

### <a name="zeros" href="#zeros">#</a> zeros(shape, /, *, dtype=None)

Returns a new array having a specified `shape` and filled with zeros.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing zeros.

### <a name="zeros_like" href="#zeros_like">#</a> zeros_like(x, /, *, dtype=None)

Returns a new array filled with zeros and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_ 

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with zeros.
