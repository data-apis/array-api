# Data type functions

> Array API specification for data type functions.

A conforming implementation of the array API standard must provide and support the following data type functions.

<!-- NOTE: please keep the constants in alphabetical order -->

## Objects in API
(function-broadcast_arrays)=
### broadcast_arrays(*arrays)

Broadcasts one or more arrays against one another.

#### Parameters

-   **arrays**: _Sequence\[ &lt;array&gt; ]_

    -   arrays to broadcast.

#### Returns

-   **out**: _List\[ &lt;array&gt; ]_

    -   a list of broadcasted arrays. Each array must have the same shape. Each array must have the same dtype as its corresponding input array.

(function-broadcast_to)=
### broadcast_to(x, /, shape)

Broadcasts an array to a specified shape.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   array to broadcast.

-   **shape**: _Tuple\[int, ...]_

    -   array shape. Must be compatible with `x` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array having a specified shape. Must have the same data type as `x`.

#### Raises

-   if the array is incompatible with the specified shape (see {ref}`broadcasting`).

(function-can_cast)=
### can_cast(from_, to, /)

Determines if one data type can be cast to another data type according {ref}`type-promotion` rules.

#### Parameters

-   **from_**: _Union\[ &lt;dtype&gt;, &lt;array&gt;]_

    -   input data type or array from which to cast.

-   **to**: _&lt;dtype&gt;_

    -   desired data type.

#### Returns

-   **out**: _bool_

    -   `True` if the cast can occur according to {ref}`type-promotion` rules; otherwise, `False`.

(function-finfo)=
### finfo(type, /)

Machine limits for floating-point data types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt;, &lt;array&gt; ]_

    -   the kind of floating-point data-type about which to get information.

#### Returns

-   **out**: _&lt;finfo object&gt;_

    -   an object having the following attributes:

        -   **bits**: _int_
            -   number of bits occupied by the floating-point data type.
        -   **eps**: _float_
            -   difference between 1.0 and the next smallest representable floating-point number larger than 1.0 according to the IEEE-754 standard.
        -   **max**: _float_
            -   largest representable number.
        -   **min**: _float_
            -   smallest representable number.
        -   **smallest_normal**: _float_
            -   smallest positive floating-point number with full precision.

(function-iinfo)=
### iinfo(type, /)

Machine limits for integer data types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt;, &lt;array&gt; ]_

    -   the kind of integer data-type about which to get information.

#### Returns

-   **out**: _&lt;iinfo object&gt;_

    -   a class with that encapsules the following attributes:

        -   **bits**: _int_
            -   number of bits occupied by the type
        -   **max**: _int_
            -   largest representable number.
        -   **min**: _int_
            -   smallest representable number.

(function-result_type)=
### result_type(*arrays_and_dtypes)

Returns the dtype that results from applying the type promotion rules
(see {ref}`type-promotion`) to the arguments.

```{note}
If provided mixed dtypes (e.g., integer and floating-point), the returned dtype will be implementation-specific.
```

#### Parameters

-   **arrays_and_dtypes**: _Sequence\[ Union\[ &lt;array&gt;, &lt;dtype&gt; \] \]_

    -   input arrays and dtypes.

#### Returns

-   **out**: _&lt;dtype&gt;_

    -   the dtype resulting from an operation involving the input arrays and dtypes.
