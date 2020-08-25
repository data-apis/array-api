# Purpose and scope

## Introduction



## History



## Scope (includes out-of-scope / non-goals)



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

A conforming implementation of the array API standard must provide and support all the functions, arguments, data types, syntax, and semantics described in this specification.

A conforming implementation of the array API standard may provide additional values, objects, properties, data types, and functions beyond those described in this specification.

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
