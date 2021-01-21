# Manipulation Functions

> Array API specification for manipulating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-concat)=
### concat(arrays, /, *, axis=0)

Joins a sequence of arrays along an existing axis.

#### Parameters

-   **arrays**: _Tuple\[ &lt;array&gt; ]_

    -   input arrays to join. The arrays must have the same shape, except in the dimension specified by `axis`.

-   **axis**: _Optional\[ int ]_

    -   axis along which the arrays will be joined. If `axis` is `None`, arrays must be flattened before concatenation. If `axis` is negative, the function must determine the axis along which to join by counting from the last dimension. Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array containing the concatenated values. If the input arrays have different data types, normal [type promotion rules](type_promotion.md) must apply. If the input arrays have the same data type, the output array must have the same data type as the input arrays.

        ```{note}

        This specification leaves type promotion between data type families (i.e., `intxx` and `floatxx`) unspecified.
        ```

(function-expand_dims)=
### expand_dims(x, axis, /)

Expands the shape of an array by inserting a new axis (dimension) of size one at the position specified by `axis`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _int_

    -   axis position. Must follow Python's indexing rules: zero-based and negative indices must be counted backward from the last dimension. If `x` has rank `N`, a valid `axis` must reside on the interval `[-N-1, N+1]`. An `IndexError` exception must be raised if provided an invalid `axis` position.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an expanded output array having the same data type and shape as `x`.

(function-flip)=
### flip(x, /, *, axis=None)

Reverses the order of elements in an array along the given axis. The shape of the array must be preserved.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis (or axes) along which to flip. If `axis` is `None`, the function must flip all input array axes. If `axis` is negative, the function must count from the last dimension. If provided more than one axis, the function must flip only the specified axes. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type and shape as `x` and whose elements, relative to `x`, are reordered.

(function-reshape)=
### reshape(x, shape, /)

Reshapes an array without changing its data.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array to reshape.

-   **shape**: _Tuple\[ int, ... ]_

    -   a new shape compatible with the original shape. One shape dimension is allowed to be `-1`. When a shape dimension is `-1`, the corresponding output array shape dimension must be inferred from the length of the array and the remaining dimensions.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type, elements, and underlying element order as `x`.

(function-roll)=
### roll(x, shift, /, *, axis=None)

Rolls array elements along a specified axis. Array elements that roll beyond the last position are re-introduced at the first position. Array elements that roll beyond the first position are re-introduced at the last position.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **shift**: _Union\[ int, Tuple\[ int, ... ] ]_

    -   number of places by which the elements are shifted. If `shift` is a tuple, then `axis` must be a tuple of the same size, and each of the given axes must be shifted by the corresponding element in `shift`. If `shift` is an `int` and `axis` a tuple, then the same `shift` must be used for all specified axes. If a shift is positive, then array elements must be shifted positively (toward larger indices) along the dimension of `axis`. If a shift is negative, then array elements must be shifted negatively (toward smaller indices) along the dimension of `axis`.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis (or axes) along which elements to shift. If `axis` is `None`, the array must be flattened, shifted, and then restored to its original shape. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type as `x` and whose elements, relative to `x`, are shifted.

(function-squeeze)=
### squeeze(x, /, *, axis=None)

Removes singleton dimensions (axes) from `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_

    -   axis (or axes) to squeeze. If provided, only the specified axes must be squeezed. If `axis` is `None`, all singleton dimensions (axes) must be removed. If a specified axis has a size greater than one, the specified axis must be left unchanged. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type and elements as `x`.

(function-stack)=
### stack(arrays, /, *, axis=0)

Joins a sequence of arrays along a new axis.

#### Parameters

-   **arrays**: _Tuple\[ &lt;array&gt; ]_

    -   input arrays to join. Each array must have the same shape.

-   **axis**: _int_

    -   axis along which the arrays will be joined. Providing an `axis` specifies the index of the new axis in the dimensions of the result. For example, if `axis` is `0`, the new axis will be the first dimension and the output array will have shape `(N, A, B, C)`; if `axis` is `1`, the new axis will be the second dimension and the output array will have shape `(A, N, B, C)`; and, if `axis` is `-1`, the new axis will be the last dimension and the output array will have shape `(A, B, C, N)`. A valid `axis` must be on the interval `[-N, N)`, where `N` is the rank (number of dimensions) of `x`. If provided an `axis` outside of the required interval, the function must raise an exception. Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having rank `N+1`, where `N` is the rank (number of dimensions) of `x`. If the input arrays have different data types, normal [type promotion rules](type_promotion.md) must apply. If the input arrays have the same data type, the output array must have the same data type as the input arrays.

        ```{note}

        This specification leaves type promotion between data type families (i.e., `intxx` and `floatxx`) unspecified.
        ```
