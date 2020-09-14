# Manipulation Functions

> Array API specification for manipulating arrays.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.

<!-- NOTE: please keep the functions in alphabetical order -->

### <a name="concat" href="#concat">#</a> concat(arrays, /, *, axis=0)

Joins a sequence of arrays along an existing axis.

#### Parameters

-   **arrays**: _Sequence\[ &lt;array&gt; ]_

    -   input arrays to join. The arrays must have the same shape, except in the dimension specified by `axis`.

-   **axis**: _Optional\[ int ]_ 

    -   axis along which the arrays will be joined. If `axis` is `None`, arrays are flattened before concatenation. If `axis` is negative, the function must count from last dimension. Default: `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array containing the concatenated values.

### <a name="flip" href="#flip">#</a> flip(x, /, *, axis=None)

Reverses the order of elements in an array along the given axis. The shape of the array must be preserved.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array.

-   **axis**: _Optional\[ Union\[ int, Tuple\[ int, ... ] ] ]_ 

    -   axis (or axes) along which to flip. If `axis` is `None`, the function must flip all input array axes. If `axis` is negative, the function must count from the last dimension. If provided more than one axis, the function must flip only the specified axes. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type as `x` and whose axes, relative to `x`, are flipped.

### <a name="reshape" href="#reshape">#</a> reshape(x, shape, /)

Reshapes an array without changing its data.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array to reshape.

-   **shape**: _Union\[ int, Tuple\[ int, ... ] ]_ 

    -   a new shape compatible with the original shape. If `shape` is an integer, then the result must be a one-dimensional array of that length. One shape dimension is allowed to be `-1`. When a shape dimension is `-1`, the corresponding output array shape dimension must be inferred from the length of the array and the remaining dimensions.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an output array having the same data type, elements, and underlying element order as `x`.