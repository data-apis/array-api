(device-support)=

# Device support

For libraries that support execution on more than a single hardware device - e.g. CPU and GPU, or multiple GPUs - it is important to be able to control on which device newly created arrays get placed and where execution happens. Attempting to be fully implicit doesn't scale to situation with multiple GPUs.

Existing libraries employ one or more of these three methods to exert such control:
1. A global default device, which may be fixed or user-switchable.
2. A context manager to control device assignment within its scope.
3. Local control via explicit keywords and a method to transfer arrays to another device.

This standard chooses to add support for method 3 (local control), because it's the most explicit and granular, with its only downside being verbosity. A context manager may be added in the future - see {ref}`device-out-of-scope` for details.

## Syntax for device assignment

The array API will offer the following syntax for device assignment and cross-device data transfer:

1. A string representation to identify a device: `'device_type:index'`, with
   `:index'` optional (e.g. doesn't apply to `'cpu'`). All lower-case, with type
   strings `'cpu'`, `'gpu'`, `'tpu'`.
2. A `device` object, whose constructor takes the string representation, with properties:
   - `str`: the string representation.
   - `type`: the device type part of the string representation.
   - `index`: the device index, as an integer (with the first device of a given type having index `0`).
3. A `device=None` keyword for array creation functions, which takes either the string representation or an instance of a `device` object.
4. A `.to(device)` method on the array object, with `device` again being
   either a string or a device instance, to move arrays to a different device.
5. A `.device` property on the array object, which returns a `device` object instance


## Semantics

- Operations involving one or more arrays on the same device must return arrays on that same device
- Operations involving arrays on different devices must raise an exception
- `device` object instances are only meant to be consumed by the library that produced them - the string attribute can be used for portability between libraries.
- If a library encounters a device specification for an unknown or
  unsupported device, it must raise a `ValueError`.
- There must be a default device, meaning all usages of `device=None` will produce arrays on the same device.

```{note}
The default device will typically be either `'cpu'` or `'gpu:0'`, however this
is _not_ a requirement. Also note that the default device can vary based on
available devices, e.g. `'gpu:0'` if available, `'cpu'` otherwise. Users should be
aware of this, and consider using explicit device control if the default may
not be right for them.
```


(device-out-of-scope)=

## Out of scope for device support

Individual libraries may offers APIs for one or more of the following topics,
however those are out of scope for this standard:

- Setting a default device globally
- Stream/queue control
- Distributed allocation
- Memory pinning
- A context manager for device control

```{note}
A context manager for controlling the default device is present in most existing array
libraries (NumPy being the exception). There are concerns with using a
context manager however:

- TensorFlow has an issue where its `.shape` attribute is also a tensor, and
  that interacts badly with its context manager approach to specifying
  devices - because metadata like shape typically should live on the host,
  not on an accelerator.
- A context manager can be tricky to use at a high level, since it may affect
  library code below function calls (non-local effects). See, e.g., [this
  PyTorch issue](https://github.com/pytorch/pytorch/issues/27878) for a
  discussion on a good context manager API.

Adding a context manager may be considered in a future version of this API standard.
```