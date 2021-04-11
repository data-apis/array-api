(searching-functions)=

# Searching Functions

> Array API specification for functions for searching arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-argmax)=
### argmax(x, /, *, axis=None, keepdims=False)

Returns the indices of the maximum values along a specified axis. When the maximum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to search. If `None`, the function must return the index of the maximum value of the flattened array. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `axis` is `None`, a zero-dimensional array containing the index of the first occurrence of the maximum value; otherwise, a non-zero-dimensional array containing the indices of the maximum values. The returned array must have be the default array index data type.

(function-argmin)=
### argmin(x, /, *, axis=None, keepdims=False)

Returns the indices of the minimum values along a specified axis. When the minimum value occurs multiple times, only the indices corresponding to the first occurrence are returned.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to search. If `None`, the function must return the index of the minimum value of the flattened array. Default: `None`.

-   **keepdims**: _bool_

    -   If `True`, the reduced axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see {ref}`broadcasting`). Otherwise, if `False`, the reduced axes (dimensions) must not be included in the result. Default: `False`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   if `axis` is `None`, a zero-dimensional array containing the index of the first occurrence of the minimum value; otherwise, a non-zero-dimensional array containing the indices of the minimum values. The returned array must have the default array index data type.

(function-nonzero)=
### nonzero(x, /)

Returns the indices of the array elements which are non-zero.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. Must have a positive rank. If `x` is zero-dimensional, the function must raise an exception.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, ... ]_

    -   a tuple of `k` arrays, one for each dimension of `x` and each of size `n` (where `n` is the total number of non-zero elements), containing the indices of the non-zero elements in that dimension. The indices must be returned in row-major, C-style order. The returned array must have the default array index data type.

(function-where)=
### where(condition, x1, x2, /)

Returns elements chosen from `x1` or `x2` depending on `condition`.

#### Parameters

-   **condition**: _&lt;array&gt;_

    -   when `True`, yield `x1_i`; otherwise, yield `x2_i`. Must be compatible with `x1` and `x2` (see {ref}`broadcasting`).

-   **x1**: _&lt;array&gt;_

    -   first input array. Must be compatible with `condition` and `x2` (see {ref}`broadcasting`).

-   **x2**: _&lt;array&gt;_

    -   second input array. Must be compatible with `condition` and `x1` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array with elements from `x1` where `condition` is `True`, and elements from `x2` elsewhere. The returned array must have a data type determined by {ref}`type-promotion` rules.
