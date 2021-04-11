# Creation Functions

> Array API specification for creating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-arange)=
### arange(start, /, *, stop=None, step=1, dtype=None, device=None)

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

    -   the distance between two adjacent elements (`out[i+1] - out[i]`). Default: `1`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values. The length of the output array must be `ceil((stop-start)/step)`.


(function-asarray)=
### asarray(obj, /, *, dtype=None, device=None, copy=None)

Convert the input to an array.

#### Parameters

-   **obj**: _Union\[ float, NestedSequence\[ bool | int | float ], SupportsDLPack, SupportsBufferProtocol ]_

    -   Object to be converted to an array. Can be a Python scalar, a (possibly nested) sequence of Python scalars, or an object supporting DLPack or the Python buffer protocol.

    :::{tip}
    An object supporting DLPack has `__dlpack__` and `__dlpack_device__` methods.
    An object supporting the buffer protocol can be turned into a memoryview through `memoryview(obj)`.
    :::

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from the data type(s) in `obj`. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

-   **copy**: _Optional\[ bool ]_

    -   Whether or not to make a copy of the input. If `True`, always copies. If `False`, never copies for input which supports DLPack or the buffer protocol, and raises `ValueError` in case that would be necessary. If `None`, reuses existing memory buffer if possible, copies otherwise. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array containing the data from `obj`.


(function-empty)=
### empty(shape, /, *, dtype=None, device=None)

Returns an uninitialized array having a specified `shape`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

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

    -   device to place the created array on, if given. If `device` is `None`, the default device must be used, not `x.device`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and containing uninitialized data.

(function-eye)=
### eye(N, /, *, M=None, k=0, dtype=None, device=None)

Returns a two-dimensional array with ones on the `k`th diagonal and zeros elsewhere.

#### Parameters

-   **N**: _int_

    -   number of rows in the output array.

-   **M**: _Optional\[ int ]_

    -   number of columns in the output array. If `None`, the default number of columns in the output array is `N`. Default: `None`.

-   **k**: _Optional\[ int ]_

    -   index of the diagonal. A positive value refers to an upper diagonal, a negative value to a lower diagonal, and `0` to the main diagonal. Default: `0`.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

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
### full(shape, fill_value, /, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with `fill_value`.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **fill_value**: _Union\[ int, float ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array where every element is equal to `fill_value`.

(function-full_like)=
### full_like(x, fill_value, /, *, dtype=None, device=None)

Returns a new array filled with `fill_value` and having the same `shape` as an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array from which to derive the output array shape.

-   **fill_value**: _Union\[ int, float ]_

    -   fill value.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be inferred from `x`. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. If `device` is `None`, the default device must be used, not `x.device`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and where every element is equal to `fill_value`.

(function-linspace)=
### linspace(start, stop, num, /, *, dtype=None, device=None, endpoint=True)

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

    -   device to place the created array on, if given. Default: `None`.

-   **endpoint**: _bool_

    -   boolean indicating whether to include `stop` in the interval. Default: `True`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a one-dimensional array containing evenly spaced values.

(function-ones)=
### ones(shape, /, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with ones.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

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

    -   device to place the created array on, if given. If `device` is `None`, the default device must be used, not `x.device`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with ones.

(function-zeros)=
### zeros(shape, /, *, dtype=None, device=None)

Returns a new array having a specified `shape` and filled with zeros.

#### Parameters

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   output array shape.

-   **dtype**: _Optional\[ &lt;dtype&gt; ]_

    -   output array data type. If `dtype` is `None`, the output array data type must be the default floating-point data type. Default: `None`.

-   **device**: _Optional\[ &lt;device&gt; ]_

    -   device to place the created array on, if given. Default: `None`.

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

    -   device to place the created array on, if given. If `device` is `None`, the default device must be used, not `x.device`. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having the same shape as `x` and filled with zeros.
