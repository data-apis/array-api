# Data interchange mechanisms

This section discusses the mechanism to convert one type of array into another.
As discussed in the :ref:`assumptions-dependencies <Assumptions>` section,
_functions_ provided by an array library are not expected to operate on
_array types_ implemented by another library. Instead, the array can be
converted to a "native" array type.

The interchange mechanism must offer the following:

1. Data access via a protocol that describes the memory layout of the array
   in an implementation-independent manner.
   _Rationale: any number of libraries must be able to exchange data, and no
   particular package must be needed to do so._
2. Support for all dtypes in this API standard (see :ref:`data-types`).
3. Device support. It must be possible to determine on what device the array
   that is to be converted lives.
   _Rationale: there are CPU-only, GPU-only, and multi-device array types;
   it's best to support these with a single protocol (with separate
   per-device protocols it's hard to figure out unambiguous rules for which
   protocol gets used, and the situation will get more complex over time
   as TPU's and other accelerators become more widely available)._
4. Moving data from one device to another must raise by default, and be
   explicitly enabled by the user.
   _Rationale: data transfer is typically very expensive, and hence must not
   happen silently._
5. Zero-copy semantics where possible, making a copy only if needed (e.g.
   when data is not contiguous in memory).
   _Rationale: performance._
6. A stable C ABI.
   _Rationale: all prominent existing array libraries are implemented in
   C/C++, and are released independently from each other. Hence a stable C
   ABI is required for packages to work well together._

The best candidate for this protocol is DLPack. See the
[RFC to adopt DLPack](https://github.com/data-apis/consortium-feedback/issues/1)
for details.

TODO: design an appropriate Python API for DLPACK (`to_dlpack` followed by `from_dlpack` is a little clunky, we'd like it to work more like the buffer protocol does on CPU, with a single constructor function).

TODO: specify the expected behaviour with copy/view/move/shared-memory semantics in detail.
