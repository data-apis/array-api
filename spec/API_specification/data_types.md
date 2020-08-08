.. _data-types:

# Data Types

> Array API specification for supported data types.

A conforming implementation of the array API standard must provide and support the following data types.

A conforming implementation of the array API standard may provide and support additional data types beyond those described in this specification.

## bool

Boolean (`True` or `False`) stored as a byte.

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

IEEE 754 single-precision binary floating-point number (see IEEE 754-2019).

## float64

IEEE 754 double-precision binary floating-point number (see IEEE 754-2019).