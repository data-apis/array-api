# Sorting Functions

> Array API specification for sorting functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="argsort" href="#argsort">#</a> argsort(x, /, *, axis=-1, descending=False, stable=True)

Returns the indices that sort an array `x` along a specified axis.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to sort. If set to `-1`, the function sorts along the last axis. Default: `-1`.

-   **descending**: _bool_

    -   sort order. If `True`, the returned indices sort `x` in descending order (by value). If `False`, the returned indices sort `x` in ascending order (by value). Default: `False`.

-   **stable**: _bool_

    -   sort stability. If `True`, the returned indices must maintain the relative order of `x` values which compare as equal. If `False`, the returned indices may or may not maintain the relative order of `x` values which compare as equal (i.e., the relative order of `x` values which compare as equal is implementation-dependent). Default: `True`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array of indices. The returned array must have the same shape as `x`. The returned array must have the default array index data type.

### <a name="sort" href="#sort">#</a> sort(x, /, *, axis=-1, descending=False, stable=True)

Returns a sorted copy of an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis along which to sort. If set to `-1`, the function sorts along the last axis. Default: `-1`.

-   **descending**: _bool_

    -   sort order. If `True`, the array is sorted in descending order (by value). If `False`, the array is sorted in ascending order (by value). Default: `False`.

-   **stable**: _bool_

    -   sort stability. If `True`, the returned array must maintain the relative order of `x` values which compare as equal. If `False`, the returned array may or may not maintain the relative order of `x` values which compare as equal (i.e., the relative order of `x` values which compare as equal is implementation-dependent). Default: `True`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   a sorted array. The returned array must have the same data type and shape as `x`.
