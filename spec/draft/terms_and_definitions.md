# Terms and Definitions

For the purposes of this specification, the following terms and definitions apply.

## Normative Keywords

This specification aims to follow [RFC 2119](https://tools.ietf.org/html/rfc2119) and using the following keywords to indicate requirement levels:

**must**:
a definition or behavior is an absolute requirement of this specification.

**must not**:
a definition or behavior is an absolute prohibition of this specification.

**should**:
valid reasons may exist to ignore a definition or behavior in particular circumstances; however, the full implications must be understood and carefully weighed before choosing a different course.

**should not**:
valid reasons may exist when a particular discouraged behavior is acceptable or even useful; however, the full implications must be understood and carefully weighed before implementing any behavior described by this keyword.

**may**:
a definition or behavior is truly optional.

## General Terminology

<!-- NOTE: please keep terms in alphabetical order -->

**array**:
a (usually fixed-size) multidimensional container of items of the same type and size.

**axis**:
an array dimension.

**branch cut**:
a curve in the complex plane across which a given complex function fails to be continuous.

**broadcast**:
automatic (implicit) expansion of array dimensions to be of equal sizes without copying array data for the purpose of making arrays with different shapes have compatible shapes for element-wise operations.

**compatible**:
two arrays whose dimensions are compatible (i.e., where the size of each dimension in one array is either equal to one or to the size of the corresponding dimension in a second array).

**element-wise**:
an operation performed element-by-element, in which individual array elements are considered in isolation and independently of other elements within the same array.

**matrix**:
a two-dimensional array.

**rank**:
number of array dimensions (not to be confused with the number of linearly independent columns of a matrix).

**shape**:
a tuple of `N` non-negative integers that specify the sizes of each dimension and where `N` corresponds to the number of dimensions.

**singleton dimension**:
a dimension whose size is one.

**vector**:
a one-dimensional array.
