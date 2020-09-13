# Purpose and scope

## Introduction



## History



## Scope (includes out-of-scope / non-goals)



## Stakeholders




## High-level API overview




## How to read this document

For guidance on how to read and understand the type annotations included in this specification, consult the Python [documentation](https://docs.python.org/3/library/typing.html).


## How to adopt this API

Most (all) existing array libraries will find something in this API standard
that is incompatible with a current implementation, and that they cannot
change due to backwards compatibility concerns. Therefore we expect that each
of those libraries will want to offer a standard-compliant API in a _new
namespace_. The question then becomes: how does a user access this namespace?

The simplest method is: document the import to use to directly access the
namespace (e.g. `import package_name.array_api`). This has two issues though:

1. Array-consuming libraries that want to support multiple array libraries
   then have to explicitly import each library.
2. It is difficult to _version_ the array API standard implementation (see
   :ref:`api-versioning`).

To address both issues, a uniform method must be provided by a conforming
implementation to access the API namespace, namely a function:

```
xp = x.__array_namespace__()
```

The function must take one keyword, `api_version=None`, to make it possible to
request a specific API version:

```
xp = x.__array_namespace__(api_version='2020.10')
```

.. note::

    This is inspired by [NEP 37](https://numpy.org/neps/nep-0037-array-module.html#how-to-use-get-array-module),
    however it avoids adding a dependency on NumPy or having to provide a
    separate package just to do `get_array_module(x)`

    NEP 37 is still in flux (it was just accepted by JAX and TensorFlow on an
    experimental basis), and it's possible that that should be accepted instead.

    TBD: a decision must be made on this topic before a first version of the
    standard can become final. We prefer to delay this decision, to see how
    NEP 37 adoption will work out.

The `xp` namespace must contain the array object and all functionality
specified in :ref:`api-specification`. It may contain other functionality,
however it is recommended not to add other functions or objects, because that
may make it harder for users to write code that will work with multiple array
libraries.


* * *

## Conformance

A conforming implementation of the array API standard must provide and support all the functions, arguments, data types, syntax, and semantics described in this specification.

A conforming implementation of the array API standard may provide additional values, objects, properties, data types, and functions beyond those described in this specification.

* * *

## Terms and Definitions

For the purposes of this specification, the following terms and definitions apply.

<!-- NOTE: please keep terms in alphabetical order -->

### array

a (usually fixed-size) multidimensional container of items of the same type and size.

### axis

an array dimension.

### broadcast

automatic (implicit) expansion of array dimensions to be of equal sizes without copying array data for the purpose of making arrays with different shapes have compatible shapes for element-wise operations.

### compatible

two arrays whose dimensions are compatible (i.e., where the size of each dimension in one array is either equal to one or to the size of the corresponding dimension in a second array).

### element-wise

an operation performed element-by-element, in which individual array elements are considered in isolation and independently of other elements within the same array.

### matrix

a two-dimensional array.

### rank

number of array dimensions (not to be confused with the number of linearly independent columns of a matrix).

### shape

a tuple of `N` non-negative integers that specify the sizes of each dimension and where `N` corresponds to the number of dimensions.

### singleton dimension

a dimension whose size is one.

### vector

a one-dimensional array.

* * *

## Normative References

The following referenced documents are indispensable for the application of this specification.

-   __IEEE 754-2019: IEEE Standard for Floating-Point Arithmetic.__ Institute of Electrical and Electronic Engineers, New York (2019).