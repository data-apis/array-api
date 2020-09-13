.. _type-promotion:

# Type Promotion Rules

> Array API specification for type promotion rules.

A conforming implementation of the array API standard must implement the following type promotion rules governing the common result type for two **array** operands during an arithmetic operation.

A conforming implementation of the array API standard may support additional type promotion rules beyond those described in this specification.

.. note::

    Type codes are used here to keep tables readable, they are not part of the standard.
    In code, use the dtype objects specified in :ref:`data-types` (e.g., `int16` rather than `'i2'`).

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

    -   **i1**: 8-bit signed integer (i.e., `int8`)
    -   **i2**: 16-bit signed integer (i.e., `int16`)
    -   **i4**: 32-bit signed integer (i.e., `int32`)
    -   **i8**: 64-bit signed integer (i.e., `int64`)

-   unsigned integer type promotion table:

    |        | u1 | u2 | u4 | u8 |
    | ------ | -- | -- | -- | -- |
    | **u1** | u1 | u2 | u4 | u8 |
    | **u2** | u2 | u2 | u4 | u8 |
    | **u4** | u4 | u4 | u4 | u8 |
    | **u8** | u8 | u8 | u8 | u8 |

    where

    -   **u1**: 8-bit unsigned integer (i.e., `uint8`)
    -   **u2**: 16-bit unsigned integer (i.e., `uint16`)
    -   **u4**: 32-bit unsigned integer (i.e., `uint32`)
    -   **u8**: 64-bit unsigned integer (i.e., `uint64`)

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

    -   **f4**: single-precision (32-bit) floating-point number (i.e., `float32`)
    -   **f8**: double-precision (64-bit) floating-point number (i.e., `float64`)

## Notes

-   Type promotion rules **strictly** apply when determining the common result type for two **array** operands during an arithmetic operation, regardless of array dimension. Accordingly, zero-dimensional arrays are subject to the same type promotion rules as dimensional arrays.
-   Non-array ("scalar") operands are **not** permitted to participate in type promotion.


.. note::

    Mixed integer and floating-point type promotion rules are not specified
    because behaviour varies between implementations.