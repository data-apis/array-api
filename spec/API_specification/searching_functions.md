# Searching Functions

> Array API specification for sorting functions.
A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="argmax" href="#argmax">#</a> argmax(x, /, *, axis=None, keepdims=False)

Returns the indices of the maximum values along a specified axis. When the maximum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to search. If `None`, the function must return the index of the maximum value of the flattened array. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `axis` is `None`, a zero-dimensional array containing the index of the first occurrence of the maximum value; otherwise, a non-zero-dimensional array containing the indices of the maximum values.

### <a name="argmin" href="#argmin">#</a> argmin(x, /, *, axis=None, keepdims=False)

Returns the indices of the minimum values along a specified axis. When the minimum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to search. If `None`, the function must return the index of the minimum value of the flattened array. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `axis` is `None`, a zero-dimensional array containing the index of the first occurrence of the minimum value; otherwise, a non-zero-dimensional array containing the indices of the minimum values.

### <a name="nonzero" href="#nonzero">#</a> nonzero(x, /)

Return the indices of the array elements which are non-zero.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, ... ]_

    -   a tuple of arrays, one for each dimension of `x`, containing the indices of the non-zero elements in that dimension. The indices must be returned in row-major, C-style order.