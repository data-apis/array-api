# Data type functions

> Array API specification for data type functions.

A conforming implementation of the array API standard must provide and support the following data type functions.

<!-- NOTE: please keep the constants in alphabetical order -->

## Objects in API

(finfo)=
### finfo(type, /)

Machine limits for floating-point data types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt, &lt;array&gt; ]_

    -   the kind of floating-point data-type about which to get information.

#### Returns

-   **out**: _&lt;class&gt;_

    -   an object having the following attributes:

        -   **bits**: _int_
            -   number of bits occupied by the floating-point data type.
        -   **eps**: _float_
            -   difference between 1.0 and the next smallest representable floating-point number larger than 1.0 according to the IEEE-754 standard.
        -   **max**: _float_
            -   largest representable number.
        -   **min**: _float_
            -   smallest representable number.

(iinfo)=
### iinfo(type, /)

Machine limits for integer data types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt, &lt;array&gt; ]_

    -   the kind of integer data-type about which to get information.

#### Returns

-   **out**: _&lt;class&gt;_

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

-   **arrays_and_dtypes**: _Sequence\[ Union\[ &lt;array&gt;, &lt;dtype&gt; \] \];_

    -   input arrays and dtypes.

#### Returns

-   **out**: _&lt;dtype&gt;_

    -   the dtype resulting from an operation involving the input arrays and dtypes.
