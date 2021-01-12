(device-support)=

# Device support

For libraries that support execution on more than a single hardware device - e.g. CPU and GPU, or multiple GPUs - it is important to be able to control on which device newly created arrays get placed and where execution happens. Attempting to be fully implicit doesn't always scale well to situations with multiple GPUs.

Existing libraries employ one or more of these three methods to exert such control:
1. A global default device, which may be fixed or user-switchable.
2. A context manager to control device assignment within its scope.
3. Local control via explicit keywords and a method to transfer arrays to another device.

This standard chooses to add support for method 3 (local control), because it's the most explicit and granular, with its only downside being verbosity. A context manager may be added in the future - see {ref}`device-out-of-scope` for details.


## Intended usage

The intended usage for the device support in the current version of the
standard is _device handling in library code_. The assumed pattern is that
users create arrays (for which they can use all the relevant device syntax
that the library they use provides), and that they then pass those arrays
into library code which may have to do the following:

- Create new arrays on the same device as an array that's passed in.
- Determine whether two input arrays are present on the same device or not.
- Move an array from one device to another.
- Create output arrays on the same device as the input arrays.
- Pass on a specified device to other library code.

```{note}
Given that there is not much that's currently common in terms of
device-related syntax between different array libraries, the syntax included
in the standard is kept as minimal as possible while enabling the
above-listed use cases.
```

## Syntax for device assignment

The array API will offer the following syntax for device assignment and
cross-device data transfer:

1. A `.device` property on the array object, which returns a `Device` object
  representing the device the data in the array is stored on, and supports
  comparing devices for equality with `==` and `!=` within the same library
  (e.g., by implementing `__eq__`); comparing device objects from different
  libraries is out of scope).
2. A `device=None` keyword for array creation functions, which takes an
   instance of a `Device` object.
3. A `.to_device(device)` method on the array object, with `device` again being
   a `Device` object, to move an array to a different device.

```{note}
The only way to obtain a `Device` object is from the `.device` property on
the array object, hence there is no `Device` object in the array API itself
that can be instantiated to point to a specific physical or logical device.
```


## Semantics

Handling devices is complex, and some frameworks have elaborate policies for
handling device placement. Therefore this section only gives recommendations,
rather than hard requirements:

- Respect explicit device assignment (i.e. if the input to the `device=` keyword
  is not `None`, guarantee that the array is created on the given device, and
  raise an exception otherwise).
- Preserve device assignment as much as possible (e.g. output arrays from a
  function are expected to be on the same device as input arrays to the
  function).
- Raise an exception if an operation involves arrays on different devices
  (i.e. avoid implicit data transfer between devices).
- Use a default for `device=None` which is consistent between functions
  within the same library.
- If a library has multiple ways of controlling device placement, the most
  explicit method should have the highest priority. For example:
    1. If `device=` keyword is specified, that always takes precedence
    2. If `device=None`, then use the setting from a context manager, if set.
    3. If no context manager was used, then use the global default device/strategy


(device-out-of-scope)=

## Out of scope for device support

Individual libraries may offers APIs for one or more of the following topics,
however those are out of scope for this standard:

- Identifying a specific physical or logical device across libraries
- Setting a default device globally
- Stream/queue control
- Distributed allocation
- Memory pinning
- A context manager for device control

```{note}
A context manager for controlling the default device is present in most existing array
libraries (NumPy being the exception). There are concerns with using a
context manager however. A context manager can be tricky to use at a high
level, since it may affect library code below function calls (non-local
effects). See, e.g., [this PyTorch issue](https://github.com/pytorch/pytorch/issues/27878)
for a discussion on a good context manager API.

Adding a context manager may be considered in a future version of this API standard.
```
