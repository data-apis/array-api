(data-interchange)=

# Data interchange mechanisms

This section discusses the mechanism to convert one type of array into another.
As discussed in the {ref}`assumptions-dependencies <Assumptions>` section,
_functions_ provided by an array library are not expected to operate on
_array types_ implemented by another library. Instead, the array can be
converted to a "native" array type.

The interchange mechanism must offer the following:

1. Data access via a protocol that describes the memory layout of the array
   in an implementation-independent manner.
   _Rationale: any number of libraries must be able to exchange data, and no
   particular package must be needed to do so._
2. Support for all dtypes in this API standard (see {ref}`data-types`).
3. Device support. It must be possible to determine on what device the array
   that is to be converted lives.
   _Rationale: there are CPU-only, GPU-only, and multi-device array types;
   it's best to support these with a single protocol (with separate
   per-device protocols it's hard to figure out unambiguous rules for which
   protocol gets used, and the situation will get more complex over time
   as TPU's and other accelerators become more widely available)._
4. Zero-copy semantics where possible, making a copy only if needed (e.g.
   when data is not contiguous in memory).
   _Rationale: performance._
5. A Python-side and a C-side interface, the latter with a stable C ABI.
   _Rationale: all prominent existing array libraries are implemented in
   C/C++, and are released independently from each other. Hence a stable C
   ABI is required for packages to work well together._

The best candidate for this protocol is DLPack. See the
[RFC to adopt DLPack](https://github.com/data-apis/consortium-feedback/issues/1)
for details.

```{note}

The main alternatives to DLPack are device-specific methods:

- The [buffer protocol](https://docs.python.org/dev/c-api/buffer.html) on CPU
- `__cuda_array_interface__` for CUDA, specified in the Numba documentation
  [here](https://numba.pydata.org/numba-doc/0.43.0/cuda/cuda_array_interface.html)
  (Python-side only at the moment)

An issue with device-specific protocols are: if two libraries both
support multiple device types, in which order should the protocols be
tried? A growth in the number of protocols to support each time a new
device gets supported by array libraries (e.g. TPUs, AMD GPUs, emerging
hardware accelerators) also seems undesirable.

In addition to the above argument, it is also clear from adoption
patterns that DLPack has the widest support. The buffer protocol, despite
being a lot older and standardized as part of Python itself via PEP 3118,
hardly has any support from array libraries. CPU interoperability is
mostly dealt with via the NumPy-specific `__array__` (which, when called,
means the object it is attached to must return a `numpy.ndarray`
containing the data the object holds).
```

TODO: design an appropriate Python API for DLPACK (`to_dlpack` followed by `from_dlpack` is a little clunky, we'd like it to work more like the buffer protocol does on CPU, with a single constructor function).

TODO: specify the expected behaviour with copy/view/move/shared-memory semantics in detail.


```{note}

If an array that is accessed via the interchange protocol lives on a
device that the requesting library does not support, one of two things
must happen: moving data to another device, or raising an exception.
Device transfers are typically expensive, hence doing that silently can
lead to hard to detect performance issues. Hence it is recommended to
raise an exception, and let the user explicitly enable device transfers
via, e.g., a `force=False` keyword that they can set to `True`.
```
