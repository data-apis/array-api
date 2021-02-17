# Data type functions

> Array API specification for data type functions.

A conforming implementation of the array API standard must provide and support the following data type functions.

<!-- NOTE: please keep the constants in alphabetical order -->

## Objects in API
(can_cast)=
### can_cast(from_, to)

Determines if a type conversion is allowed under the rules described by {ref}`type-promotion`.

#### Parameters

-   **from_**: _Union\[ &lt;dtype&gt ]_

    -   the data type, scalar or array to cast from.

-   **to**: _&lt;dtype&gt_

    -   the data type to cast to.

#### Returns

-   **out**: _bool_

    -   True if the cast can occur according to the {ref}`type-promotion`.

(finfo)=
### finfo(type)

Defines the machine limits for floating point types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt, instance ]_

    -   the kind of floating point data-type about which to get information

#### Returns

-   **out**: _&lt;class&gt;_

    -   a class with that encapsules the following attributes:

        -   **bits**: _int_
            -   The number of bits occupied by the type
        -   **eps**: _float_
            -   The difference between 1.0 and the next smallest representable float larger than 1.0 following the IEEE 754 standard.
        -   **max**: _float_
            -   The largest representable number.
        -   **min**: _float_
            -   The smallest representable number.
        -   **tiny**: _float_
            -   The smallest positive representable number.

(iinfo)=
### iinfo(type)

Defines the machine limits for integer types.

#### Parameters

-   **type**: _Union\[ &lt;dtype&gt, instance ]_

    -   the kind of integer data-type about which to get information

#### Returns

-   **out**: _&lt;class&gt;_

    -   a class with that encapsules the following attributes:

        -   **bits**: _int_
            -   The number of bits occupied by the type
        -   **max**: _int_
            -   The largest representable number.
        -   **min**: _int_
            -   The smallest representable number.

(function-result_type)=
### result_type(*arrays_and_dtypes)

Returns the dtype that results from applying the type promotion rules
(see {ref}`type-promotion`) to the arguments.

```{note}
If mixed dtypes (e.g. integer and floating-point) are used, the output of
`result_type` will be implementation-specific.
```

#### Parameters

-   **arrays_and_dtypes**: _Sequence\[Union\[&lt;array&gt;, &lt;dtype&gt;\]\];_

    -   input arrays and dtypes.

#### Returns

-   **out**: _&lt;dtype&gt;_

    -   the dtype resulting from an operation involving the input arrays and dtypes.
