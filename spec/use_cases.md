# Use cases

Use cases inform the requirements for, and design choices made in, this array
API standard. This section first discusses what types of use cases are
considered, and then works out a few concrete use cases in more detail.

## Types of use cases

- Packages that depend on a specific array library currently, and would like
  to support multiple of them (e.g. for GPU or distributed array support, for
  improved performance, or for reaching a wider user base).
- Writing new libraries/tools that wrap multiple array libraries.
- Projects that implement new types of arrays with, e.g., hardware-specific
  optimizations or auto-parallelization behavior, and need an API to put on
  top that is familiar to end users.
- End users that want to switch from one library to another without learning
  about all the small differences between those libraries.


## Concrete use cases

### Use case 1: add GPU and distributed support to SciPy

When surveying a representative set of advanced users and research software
engineers in 2019 (for [this NSF proposal](https://figshare.com/articles/Mid-Scale_Research_Infrastructure_-_The_Scientific_Python_Ecosystem/8009441)),
the single most common pain point brought up about SciPy was performance.

SciPy heavily relies on NumPy (its only non-optional runtime dependency).
NumPy provides an array implementation that's in-memory, CPU-only and
single-threaded. Common performance-related wishes users have are:

- parallel algorithms (can be multi-threaded or multiprocessing based)
- support for distributed arrays (with Dask in particular)
- support for GPUs

Some parallelism can be supported in SciPy, it has a `workers` keyword
(similar to scikit-learn's `n_jobs` keyword) that allows specifying to use
parallelism in some algorithms. However SciPy itself will not directly start
depending on a GPU or distributed array implementation, or contain (e.g.)
CUDA code - that's not maintainable given the resources for development.
_However_, there is a way to provide distributed or GPU support. Part of the
solution is provided by NumPy's "array protocols" (see gh-1), that allow
dispatching to other array implementations. The main problem then becomes how
to know whether this will work with a particular distributed or GPU array
implementation - given that there are zero other array implementations that
are even close to providing full NumPy compatibility - without adding that
array implementation as a dependency.

It's clear that SciPy functionality that relies on compiled extensions (C,
C++, Cython, Fortran) directly can't easily be run on another array library
than NumPy (see :ref:`C-api` for more details about this topic). Pure Python
code can work though. There's two main possibilities:

1. Testing with another package, manually or in CI, and simply provide a list
   of functionality that is found to work. Then make ad-hoc fixes to expand
   the set that works.
2. Start relying on a well-defined subset of the NumPy API (or a new
   NumPy-like API), for which compatibility is guaranteed.

Option (2) seems strongly preferable, and that "well-defined subset" is _what
an API standard should provide_. Testing will still be needed, to ensure there
are no critical corner cases or bugs between array implementations, however
that's then a very tractable task.

As a concrete example, consider the spectral analysis functions in `scipy.signal`.
All of those functions (e.g., `periodogram`, `spectrogram`, `csd`, `welch`, `stft`,
`istft`) are pure Python - with the exception of `lombscargle` which is ~40
lines of Cython - and uses NumPy function calls, array attributes and
indexing. The beginning of each function could be changed to retrieve the
module that implements the array API standard for the given input array type,
and then functions from that module could be used instead of NumPy functions.

If the user has another array type, say a CuPy or PyTorch array `x` on their
GPU, doing:
```
from scipy import signal

signal.welch(x)
```
will result in:
```
# For CuPy
ValueError: object __array__ method not producing an array

# For PyTorch
TypeError: can't convert cuda:0 device type tensor to numpy.
```
and therefore the user will have to explicitly convert to and from a
`numpy.ndarray` (which is quite inefficient):
```
# For CuPy
x_np = cupy.asnumpy(x)
freq, Pxx = (cupy.asarray(res) for res in signal.welch(x_np))

# For PyTorch
x_np = x.cpu().numpy()
# Note: ends up with tensors on CPU, may still have to move them back
freq, Pxx = (torch.tensor(res) for res in signal.welch(x_np))
```
This code will look a little different for each array library. The end goal
here is to be able to write this instead as:
```
freq, Pxx = signal.welch(x)
```
and have `freq`, `Pxx` be arrays of the same type and on the same device as `x`.

.. note::

    This type of use case applies to many other libraries, from scikit-learn
    and scikit-image to domain-specific libraries like AstroPy and
    scikit-bio, to code written for a single purpose or user.
