# Purpose and scope

## Introduction


### This API standard


## History



## Scope (includes out-of-scope / non-goals)

This section outlines what is in scope and out of scope for this API standard.

### In scope

The scope of the array API standard includes:

- Functionality which needs to be included in an array library for it to adhere
  to this standard.
- Names of functions, methods, classes and other objects.
- Function signatures, including type annotations.
- Semantics of functions and methods. I.e. expected outputs including precision
  for and dtypes of numerical results.
- Semantics in the presence of `nan`'s, `inf`'s, empty arrays (i.e. arrays
  including one or more dimensions of size `0`).
- Casting rules, broadcasting, indexing
- Data interchange. I.e. protocols to convert one type of array into another
  type, potentially sharing memory.
- Device support.

Furthermore, meta-topics included in this standard include:

- Use cases for the API standard and assumptions made in it
- API standard adoption
- API standard versioning
- Future API standard evolution
- Array library and API standard versioning
- Verification of API standard conformance

The concrete set of functionality that is in scope for this version of the
standard is shown in this diagram (_TODO: update after deciding on how optional
extensions are dealt with_):

![Scope of array API](_static/images/scope_of_array_API.png)


**Goals** for the API standard include:

- Make it possible for array-consuming libraries to start using multiple types
  of arrays as inputs.
- Enable more sharing and reuse of code built on top of the core functionality
  in the API standard.
- For authors of new array libraries, provide a concrete API that can be
  adopted as is, rather than each author having to decide what to borrow from
  where and where to deviate.
- Make the learning curve for users less steep when they switch from one array
  library to another one.


### Out of scope

1. Implementations of the standard are out of scope.

   _Rationale: the standard will consist of a document and an accompanying test
   suite with which the conformance of an implementation can be verified. Actual
   implementations will live in array libraries; no reference implementation is
   planned._

2. Execution semantics are out of scope. This includes single-threaded vs.
   parallel execution, task scheduling and synchronization, eager vs. delayed
   evaluation, performance characteristics of a particular implementation of the
   standard, and other such topics.

   _Rationale: execution is the domain of implementations. Attempting to specify
   execution behavior in a standard is likely to require much more fine-grained
   coordination between developers of implementations, and hence is likely to
   become an obstable to adoption._

3. Non-Python API standardization (e.g., Cython or NumPy C APIs)

   _Rationale: this is an important topic for some array-consuming libraries,
   but there is no widely shared C/Cython API and hence it doesn't make sense at
   this point in time to standardize anything. See
   [the C API section](design_topics/C_API.md) for more details._

4. Standardization of these dtypes is out of scope: bfloat16, complex, extended
   precision floating point, datetime, string, object and void dtypes.

   _Rationale: these dtypes aren't uniformly supported, and their inclusion at
   this point in time could put a significant implementation burden on
   libraries. It is expected that some of these dtypes - in particular
   `bfloat16`, `complex64`, and `complex128` - will be included in a future
   version of the standard._

5. The following topics are out of scope: I/O, polynomials, error handling,
   testing routines, building and packaging related functionality, methods of
   binding compiled code (e.g., `cffi`, `ctypes`), subclassing of an array
   class, masked arrays, and missing data.

   _Rationale: these topics are not core functionality for an array library,
   and/or are too tied to implementation details._

6. NumPy (generalized) universal functions, i.e. ufuncs and gufuncs.

   _Rationale: these are NumPy-specific concepts, and are mostly just a
   particular way of building regular functions with a few extra
   methods/properties._


**Non-goals** for the API standard include:

- Making array libraries identical so they can be merged.

  _Each library will keep having its own particular strength, whether it's
  offering functionality beyond what's in the standard, performance advantages
  for a given use case, specific hardware or software environment support, or
  more._

- Implement a backend or runtime switching system to be able to switch from one
  array library to another with a single setting or line of code.

  _This may be feasible, however it's assumed that when an array-consuming
  library switches from one array type to another, some testing and possibly
  code adjustment for performance or other reasons may be needed._


### TBD whether or not in scope, or for a later version

- Random number generation, Fourier transforms, and miscellaneous functionality
  like a padding function.

  _This will be decided later, depending on whether "optional extensions" will
  be added to the standard._


### Implications of in/out of scope

If something is out of scope and therefore will not be part of (the current
version of) the API standard, that means that there are no guarantees that that
functionality works the same way, or even exists at all, across the set of
array libraries that conform to the standard. It does _not_ imply that this
functionality is less important or should not be used.


## Stakeholders

Arrays are fundamental to scientific computing, data science, and machine
learning and deep learning. Hence there are many stakeholders for an array API
standard. The _direct_ stakeholders of this standard are **authors/maintainers of
Python array libraries**. There are many more types of _indirect_ stakeholders
though, including:

- maintainers of libraries and other programs which depend on array libraries
  (called "array-consuming libraries" in the rest of this document)
- authors of non-Python array libraries
- developers of compilers and runtimes with array-specific functionality
- end users

Libraries that are being actively considered - in terms of current behaviour and
API surface - during the creation of the first version of this standard
include:

- [NumPy](https://numpy.org)
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)
- [MXNet](https://numpy.mxnet.io/)
- [JAX](https://github.com/google/jax)
- [Dask](https://dask.org/)
- [CuPy](https://cupy.chainer.org/)

Other Python array libraries that are currently under active development and
could adopt this API standard include:

- [xarray](https://xarray.pydata.org/)
- [PyData/Sparse](https://sparse.pydata.org)
- [Weld](https://github.com/weld-project/weld)
- [Bohrium](https://bohrium.readthedocs.io/)
- [Arkouda](https://github.com/mhmerrill/arkouda)
- [Legate](https://research.nvidia.com/publication/2019-11_Legate-NumPy%3A-Accelerated)

There are a huge amount of array-consuming libraries; some of the most
prominent ones that are being taken into account - in terms of current array
API usage or impact of design decisions on them - include (this list is likely
to grow it over time):

- [Pandas](https://pandas.pydata.org/)
- [SciPy](https://github.com/scipy/scipy)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [scikit-image](https://scikit-image.org/)
- [NetworkX](https://networkx.github.io/)

Array libraries in other languages, some of which may grow a Python API in the
future or have taken inspiration from NumPy or other array libraries, include:

- [Xtensor](https://xtensor.readthedocs.io) (C++, cross-language)
- [XND](https://xnd.io/) (C, cross-language)
- [stdlib](https://stdlib.io/) (JavaScript)
- [rust-ndarray](https://github.com/rust-ndarray/ndarray) (Rust)
- [rray](https://github.com/r-lib/rray) (R)
- [ND4J](https://github.com/deeplearning4j/nd4j) (JVM)
- [NumSharp](https://github.com/SciSharp/NumSharp) (C#)

Compilers, runtimes, and dispatching layers for which this API standard may be
relevant:

- [Cython](https://cython.org/)
- [Numba](http://numba.pydata.org/)
- [Pythran](https://pythran.readthedocs.io/en/latest/)
- [Transonic](https://transonic.readthedocs.io)
- [ONNX](https://onnx.ai/)
- [Apache TVM](https://tvm.apache.org/)
- [MLIR](https://mlir.llvm.org/)
- [TACO](https://github.com/tensor-compiler/taco)
- [unumpy](https://github.com/Quansight-Labs/unumpy)
- [einops](https://github.com/arogozhnikov/einops)
- [Apache Arrow](https://arrow.apache.org/)


## High-level API overview




## How to read this document

For guidance on how to read and understand the type annotations included in this specification, consult the Python [documentation](https://docs.python.org/3/library/typing.html).


## How to adopt this API


* * *

## Conformance

A conforming implementation of the array API standard must provide and support
all the functions, arguments, data types, syntax, and semantics described in
this specification.

A conforming implementation of the array API standard may provide additional
values, objects, properties, data types, and functions beyond those described
in this specification.

Libraries which aim to provide a conforming implementation but haven't yet
completed such an implementation may, and are encouraged to, provide details on
the level of (non-)conformance. For details on how to do this, see
[Verification - measuring conformance](verification_test_suite.md).


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
