(data-types)=

# Data Types

> Array API specification for supported data types.

A conforming implementation of the array API standard must provide and support the following data types.

A conforming implementation of the array API standard must define a default floating-point data type (either `float32` or `float64`), as well as a default data type for an array index (either `int32` or `int64`).

```{note}

The default floating-point and array index integer data types should be clearly defined in a conforming library's documentation.
```


## bool

Boolean (`True` or `False`).

## int8

An 8-bit signed integer whose values exist on the interval `[-128, +127]`.

## int16

A 16-bit signed integer whose values exist on the interval `[−32,767, +32,767]`.

## int32

A 32-bit signed integer whose values exist on the interval `[−2,147,483,647, +2,147,483,647]`.

## int64

A 64-bit signed integer whose values exist on the interval `[−9,223,372,036,854,775,807, +9,223,372,036,854,775,807]`.

## uint8

An 8-bit unsigned integer whose values exist on the interval `[0, +255]`.

## uint16

A 16-bit unsigned integer whose values exist on the interval `[0, +65,535]`.

## uint32

A 32-bit unsigned integer whose values exist on the interval `[0, +4,294,967,295]`.

## uint64

A 64-bit unsigned integer whose values exist on the interval `[0, +18,446,744,073,709,551,615]`.

## float32

IEEE 754 single-precision (32-bit) binary floating-point number (see IEEE 754-2019).

## float64

IEEE 754 double-precision (64-bit) binary floating-point number (see IEEE 754-2019).


:::{admonition} Future extension
:class: hint
It is expected that in the next version of this standard, `complex64` and `complex128`
dtypes will be added, with these casting rules (will be added to {ref}`type-promotion`):

![Type promotion diagram for complex dtypes in next version](/_static/images/dtype_promotion_complex.png)

See [array-api/issues/102](https://github.com/data-apis/array-api/issues/102)
for more details.
:::

```{note}
Data types ("dtypes") are objects that can be used as `dtype` specifiers in functions and methods (e.g., `zeros((2, 3), dtype=float32)`). A conforming implementation may add methods or attributes to data type objects; however, these methods and attributes are not included in this specification.

Implementations may provide other ways to specify data types (e.g.,
`zeros((2, 3), dtype='f4')`); however, these are not included in this specification.

A conforming implementation of the array API standard may provide and support additional data types beyond those described in this specification.
```

(data-type-categories)=
## Data Type Categories

For the purposes of this specification, the following data type categories are defined.
Libraries do not need to organize dtypes according to these categories. These
are only for organizing the functions in this specification itself. Future versions of
the specification will include additional categories for complex data types.

### Numeric Data Types

`int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`,
`uint64`, `float32`, and `float64` (i.e., all dtypes except for `bool`).

### Integer Data Types

`int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, and
`uint64`.

### Floating-point Data Types

`float32` and `float64`.

### Boolean Data Types

`bool`.
