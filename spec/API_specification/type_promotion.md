.. _type-promotion:

# Type Promotion Rules

> Array API specification for type promotion rules.

A conforming implementation of the array API standard must implement the following type promotion rules governing the common result type for two **array** operands during an arithmetic operation.

A conforming implementation of the array API standard may support additional type promotion rules beyond those described in this specification.

## Rules

<!-- Note: please keep table columns aligned -->

-   signed integer type promotion table:

    |        | i1 | i2 | i4 | i8 |
    | ------ | -- | -- | -- | -- |
    | **i1** | i1 | i2 | i4 | i8 |
    | **i2** | i2 | i2 | i4 | i8 |
    | **i4** | i4 | i4 | i4 | i8 |
    | **i8** | i8 | i8 | i8 | i8 |

    where

    -   **i1**: 8-bit signed integer
    -   **i2**: 16-bit signed integer
    -   **i4**: 32-bit signed integer
    -   **i8**: 64-bit signed integer

-   unsigned integer type promotion table:

    |        | u1 | u2 | u4 | u8 |
    | ------ | -- | -- | -- | -- |
    | **u1** | u1 | u2 | u4 | u8 |
    | **u2** | u2 | u2 | u4 | u8 |
    | **u4** | u4 | u4 | u4 | u8 |
    | **u8** | u8 | u8 | u8 | u8 |

    where

    -   **u1**: 8-bit unsigned integer
    -   **u2**: 16-bit unsigned integer
    -   **u4**: 32-bit unsigned integer
    -   **u8**: 64-bit unsigned integer

-   mixed unsigned and signed integer type promotion table:

    |        | u1 | u2 | u4 |
    | ------ | -- | -- | -- |
    | **i1** | i2 | i4 | i8 |
    | **i2** | i2 | i4 | i8 |
    | **i4** | i4 | i4 | i8 |

-   floating-point type promotion table:

    |        | f4 | f8 |
    | ------ | -- | -- |
    | **f4** | f4 | f8 |
    | **f8** | f8 | f8 |

    where

    -   **f4**: single-precision (32-bit) floating-point number
    -   **f8**: double-precision (64-bit) floating-point number

## Notes

-   Type promotion rules **strictly** apply when determining the common result type for two **array** operands during an arithmetic operation, regardless of array dimension. Accordingly, zero-dimensional arrays are subject to the same type promotion rules as dimensional arrays.
-   Non-array ("scalar") operands are **not** permitted to participate in type promotion.