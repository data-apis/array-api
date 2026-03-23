(migration-guide)=

# Migration Guide

This page is meant to help migrate your codebase to an array API standard
compliant implementation or become interoperable with compliant
implementations. The guide is divided into three parts.

The first part gives an overview of the {ref}`ecosystem` libraries, that
are helpful in different contexts when working with the array API standard.

The second part is dedicated to {ref}`array-producers`. If your library
mimics, for example, NumPy's or PyTorch's functionality, then you can find in
here additional instructions and guidance on how to ensure downstream users
can easily pick your solution as an array provider for their system/algorithm.

The third part delves into details for array API standard compatibility for
{ref}`array-consumers`. This pertains to any software that performs
multidimensional array manipulation in Python, such as may be found in
scikit-learn, SciPy, or statsmodels. If your software relies on a certain
array producing library, such as NumPy or JAX, then you can use the second
part to learn how to make it library agnostic and, as a result, use array
namespaces interchangeably with significantly less friction.


(ecosystem)=

## Ecosystem

Apart from the documented standard, the array API ecosystem also provides
a set of tools and packages to help you with the migration process:


(array-api-compat)=

### array-api-compat

GitHub: [array-api-compat](https://github.com/data-apis/array-api-compat)

User group: Array Consumers

Although NumPy or CuPy support the array API standard, there are still some
corner cases where their behavior diverges from the standard.
`array-api-compat` provides a compatibility layer to cover an additional subset
of such corner cases for supported libraries. This is also accompanied by a few
utility functions for easier introspection into array objects. As an array
consumer, you can consume standard-compliant namespaces as well as the wrapped
namespaces in `array-api-compat` at the same time.


(array-api-strict)=

### array-api-strict

GitHub: [array-api-strict](https://github.com/data-apis/array-api-strict)

User group: Array Consumers

`array-api-strict` is a library that provides a strict and minimal
implementation of the array API standard. As a consumer, you can use
`array-api-strict` in parametrising tests over the array namespace
to ensure your code uses only APIs compliant which are in the standard.


(array-api-tests)=

### array-api-tests

GitHub: [array-api-tests](https://github.com/data-apis/array-api-tests)

User group: Array Producers

`array-api-tests` is a collection of tests that can be used to verify the
compliance of your library with the array API standard. It includes tests
for array producers, covering a wide range of functionalities and use cases.
By running these tests, you can ensure that your library adheres to the
standard and can be used with compatible array consumer libraries.


(array-api-extra)=

### array-api-extra

GitHub: [array-api-extra](https://github.com/data-apis/array-api-extra)

User group: Array Consumers

`array-api-extra` is a collection of additional utilities and tools that are
not present in the array API standard but can be useful for compliant array
consumers. It includes additional array manipulation and statistical
functions, support for lazy backends, and useful testing utilities. It is
already used by SciPy and scikit-learn.


(array-producers)=

## Array Producers

For array producers, the central task during the development/migration process
is ensuring that the user-facing API adheres to the array API standard.

The complete API of the standard is documented in the
[API specification](https://data-apis.org/array-api/latest/API_specification/index.html).

There, each function, constant, and object is described with details
on parameters, return values, and special cases.

### Testing against array API

There are two main ways to test your API for compliance: either using
`array-api-tests` suite or testing your API manually against the
`array-api-strict` reference implementation.

#### array-api-tests suite (Recommended)

{ref}`array-api-tests` is a test suite which verifies that your API
adheres to the standard. For each function or method, it confirms
it's importable, verifies the signature, generates multiple test
cases with the [hypothesis](https://hypothesis.readthedocs.io/en/latest/)
package, and runs assertions on the outputs.

The setup details are enclosed in the GitHub repository, so here we
cover only the minimal workflow:

1. Install your package (e.g., in editable mode).
2. Clone `array-api-tests`, and set the `ARRAY_API_TESTS_MODULE` environment
   variable to your package import name.
3. Inside the `array-api-tests` directory run the command for running pytest: `pytest`. There are
   multiple useful options delivered by the test suite. A few worth mentioning:
   - `--max-examples=1000` - maximal number of test cases to generate when using
     hypothesis. This allows you to balance between execution time of the test
     suite and thoroughness of the testing. It's advised to use as many examples
     as the time buget can fit. Each test case is a random combination of
     possible inputs: the more cases, the higher chance of finding an
     unsupported edge case.
   - With the `--xfails-file` option, you can describe which tests are expected
     to fail. It's impossible to get the whole API perfectly implemented on a
     first try, so tracking what still fails gives you more control over the
     state of your API.
   - `-o xfail_strict=<bool>` is often used with the previous option. If a test
     expected to fail actually passes (`XPASS`), then you can decide whether
     to ignore that fact or raise it as an error.
   - `--skips-file` for skipping tests. At times, some failing tests might stall
     the execution time of the test suite. In that case, the most convenient
     option is to skip these for the time being.

We strongly advise you to embed this setup in your CI as well. This will allow
you to continuously monitor array API standard coverage, and make sure new
changes don't break existing APIs. As a reference, see
[NumPy's array-api-tests CI setup](https://github.com/numpy/numpy/blob/581d10f43b539a189a2d37856e5130464de9e5f6/.github/workflows/linux.yml#L296)
and [a Pixi workspace setup](https://github.com/mdhaber/mparray/blob/0ef47e008fef92c605f73907436d4c6617419161/pixi.toml#L119-L179).


#### array-api-strict

A simpler, and more manual, way of testing array API standard coverage is to
run your API calls along with the {ref}`array-api-strict` Python implementation.

This way, you can ensure that the outputs coming from your API match the minimal
reference implementation. Bear in mind, however, that you need to write
the tests cases yourself, so you need to also take into account any applicable edge
cases.


(array-consumers)=

## Array Consumers

For array consumers, the main premise is that your **array manipulation operations
should not be specific to one particular array producing library**. For instance,
if your code is specific to NumPy, it might contain:

```python
import numpy as np

# ...
b = np.full(shape, val, dtype=dtype) @ a
c = np.mean(a, axis=0)
return np.dot(c, b)
```

The first step should be as simple as assigning the `np` namespace to a dedicated
namespace variable. The convention used in the ecosystem is to name it `xp`.
Then, it is vital to ensure that each method and function call is something that
the array API standard supports. For example, `dot` is present in the NumPy
API, but the standard doesn't support it. For the sake of simplicity, let's
assume both `c` and `b` are `ndim=2`; therefore, we select `tensordot` instead,
as both NumPy and the standard define it:

```python
import numpy as np

xp = np

# ...
b = xp.full(shape, val, dtype=dtype) @ a
c = xp.mean(a, axis=0)
return xp.tensordot(c, b, axes=1)
```

At this point, replacing one backend with another one should only require
providing a different namespace, such as `xp = torch` (e.g., via an environment
variable). This can be useful if you're writing a script or in your custom
software. The other alternatives are:

- If you are building a library where the backend is determined by input
  arrays, and your function accepts array arguments, then a recommended way to
  fetch the namespace is to use [`array_api_compat.array_namespace()`](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.array_namespace).
  In case you don't want to introduce a new package dependency, you can rely
  on a plain `xp = arr.__array_namespace__()`:
  ```python
  def func(array1, scalar1, scalar2):
    xp = array_namespace(array1)  # or array1.__array_namespace__()
    return xp.arange(scalar1, scalar2) @ array1
  ```
- For a function that accepts scalars and returns arrays, use namespace `xp` as
  a parameter in the signature. Enforcing objects to have the same type as the
  provided backend can then be achieved with `arg1 = xp.asarray(arg1)` for each input:
  ```python
  def func(s1, s2, xp):
    return xp.arange(s1, s2)
  ```

If you're relying on NumPy, CuPy, PyTorch, Dask, or JAX then
{ref}`array-api-compat` can come in handy for the transition. The compat layer
allows you to still rely on your preferred array producing library, while
making sure you're already using standard compatible API. Additionally, it
offers a set of useful utility functions, such as:

- [array_namespace()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.array_namespace)
  for fetching the namespace based on input arrays.
- [is_array_api_obj()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.is_array_api_obj)
  for inspecting whether a given object is array API compatible.
- [device()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.device)
  for retrieving the device on which an array resides.

For now, the migration from a specific library (e.g., NumPy) to a standard
compatible setup requires a manual intervention for each failing API call,
but, in the future, we're hoping to provide tools for automating the migration process.
