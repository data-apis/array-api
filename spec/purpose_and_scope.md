# Purpose and scope

## Introduction



## History



## Scope (includes out-of-scope / non-goals)



## Stakeholders




## High-level API overview




## How to read this document




## How to adopt this API


* * *

## Conformance

A conforming implementation of the array API standard must provide and support all the functions, arguments, syntax, and semantics described in this specification.

A conforming implementation of the array API standard may provide additional values, objects, properties, and functions beyond those described in this specification.

* * *

## Terms and Definitions

For the purposes of this specification, the following terms and definitions apply.

<!-- NOTE: please keep terms in alphabetical order -->

### array

a (usually fixed-size) multidimensional container of items of the same type and size.

### broadcast

automatic (implicit) expansion of array dimensions to be of equal sizes without copying array data for the purpose of making arrays with different shapes have compatible shapes for element-wise operations.

### compatible

two arrays whose dimensions are compatible (i.e., where the size of each dimension in one array is either equal to one or to the size of the corresponding dimension in a second array).

### element-wise

an operation performed element-by-element, in which individual array elements are considered in isolation and independently of other elements within the same array.

### rank

number of array dimensions (not to be confused with the number of linearly independent columns of a matrix).

### shape

a tuple of `N` non-negative integers that specify the sizes of each dimension and where `N` corresponds to the number of dimensions.

### singleton dimension

a dimension whose size is one.

* * *

## Normative References

The following referenced documents are indispensable for the application of this specification.

-   __IEEE 754-2019: IEEE Standard for Floating-Point Arithmetic.__ Institute of Electrical and Electronic Engineers, New York (2019).