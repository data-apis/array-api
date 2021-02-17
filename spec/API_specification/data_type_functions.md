# Data type functions

> Array API specification for data type functions.

A conforming implementation of the array API standard must provide and support the following data type functions.

<!-- NOTE: please keep the constants in alphabetical order -->

## Objects in API

(finfo)=
### finfo(type)

Defines the machine limits for floating point types.

#### Parameters

-   **type**: _Union\[ float, &lt;dtype&gt, instance ]_

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
        -   **resolution**: _float_
            -   The approximate decimal resolution of this type.

(iinfo)=
### iinfo(type)

Defines the machine limits for integer types.

#### Parameters

-   **type**: _Union\[ integer, &lt;dtype&gt, instance ]_

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
