(migration-guide)=

# Migration Guide

This page is meant to help migrate your codebase to an Array API compliant
implementation. The guide is divided into two parts and, depending on your
exact use-case, you should look thoroughly into at least one of them.

The first part is dedicated for {ref}`array-producers`. If your library
mimics, for example, NumPy's or Dask's functionality, then you can find in
the first part additional instructions and guidance on how to ensure
downstream users can easily pick your solution as an array provider for
their system/algorithm.

The second part delves into details for Array API compatibility for
{ref}`array-consumers`. This pertains to any software that performs
multidimensional array manipulation in Python, such as may be found in
scikit-learn, SciPy, or statsmodels. If your software relies on a certain
array producing library, such as NumPy or JAX, then you can use the second
part to learn how to make it library agnostic and interchange array
namespaces with significantly less friction.

## Ecosystem

Apart from the documented standard, the Array API ecosystem also provides
a set of tools and packages to help you with the migration process:


(array-api-compat)=

### Array API Compat

GitHub: [array-api-compat](https://github.com/data-apis/array-api-compat)
User group: Array Consumers

Although NumPy, Dask, CuPy, and PyTorch support the Array API Standard, there
are still some corner cases where their behavior diverges from the standard.
`array-api-compat` provides a compatibility layer to cover these cases.
This is also accompanied by a few utility functions for easier introspection
into array objects. As an array consumer, you can still rely on the original
API while having access to the standard compatible one.


(array-api-strict)=

### Array API Strict

GitHub: [array-api-strict](https://github.com/data-apis/array-api-strict)
User group: Array Consumers, Array Producers (for testing)

`array-api-strict` is a library that provides a strict and minimal
implementation of the Array API Standard. For array producers, it is designed
to be used as a reference implementation for testing and development purposes.
You can compare your API calls with `array-api-strict` counterparts and
ensure that your library is fully compliant with the standard and can
serve as a reliable reference for other developers in the ecosystem.
For consumers, you can use `array-api-strict` during the development as an
array provider to ensure your code uses API compliant with the standard.


(array-api-tests)=

### Array API Test

GitHub: [array-api-tests](https://github.com/data-apis/array-api-tests)
User group: Array Producers

`array-api-tests` is a collection of tests that can be used to verify the
compliance of your library with the Array API Standard. It includes tests
for array producers, covering a wide range of functionalities and use cases.
By running these tests, you can ensure that your library adheres to the
standard and can be used with compatible array consumers libraries.


(array-api-extra)=

### Array API Extra

GitHub: [array-api-extra](https://github.com/data-apis/array-api-extra)
User group: Array Consumers

`array-api-extra` is a collection of additional utilities and tools that are
missing from the Array API Standard but can be useful for compliant array
consumers. It includes additional array manipulation and statistical functions.
It is already used by SciPy and scikit-learn.

The sections below mention when and how to use them.


(array-producers)=

## Array Producers

For array producers, the central task during the development/migration process
is ensuring that the user-facing API adheres to the Array API Standard.

The complete API of the standard is documented in the
[API specification](https://data-apis.org/array-api/latest/API_specification/index.html).

There, each function, constant, and object is described with details
on parameters, return values, and special cases.

### Testing against Array API

There are two main ways to test your API for compliance: either using
`array-api-tests` suite or testing your API manually against the
`array-api-strict` reference implementation.

#### Array API Test suite (Recommended)

{ref}`array-api-tests` is a test suite which verifies that your API
adheres to the standard. For each function or method, it confirms
it's importable, verifies the signature, generates multiple test
cases with [hypothesis](https://hypothesis.readthedocs.io/en/latest/)
package, and runs assertions on the outputs.

The setup details are enclosed in the GitHub repository, so here we
cover only the minimal workflow:

1. Install your package, for example in editable mode.
2. Clone `array-api-tests`, and set `ARRAY_API_TESTS_MODULE` environment
   variable to your package import name.
3. Inside the `array-api-tests` directory run `pytest` command. There are
   multiple useful options delivered by the test suite. A few worth mentioning:
   - `--max-examples=1000` - maximal number of test cases to generate by the
     hypothesis. This allows you to balance between execution time of the test
     suite and thoroughness of the testing. It's advised to use as many examples
     as the time buget can fit. Each test case is a random combination of
     possible inputs: the more cases, the higher chance of finding an
     unsupported edge case.
   - With the `--xfails-file` option, you can describe which tests are expected
     to fail. It's impossible to get the whole API perfectly implemented on a
     first try, so tracking what still fails gives you more control over the
     state of your API.
   - `-o xfail_strict=<bool>` is often used with the previous one. If a test
     expected to fail actually passes (`XPASS`), then you can decide whether
     to ignore that fact or raise it as an error.
   - `--skips-file` for skipping tests. At times, some failing tests might stall
     the execution time of the test suite. In that case, the most convenient
     option is to skip these for the time being.

We strongly advise you to embed this setup in your CI as well. This will allow
you to monitor the coverage live, and make sure new changes don't break existing
APIs. For a reference, here's a [NumPy Array API Tests CI setup](https://github.com/numpy/numpy/blob/581d10f43b539a189a2d37856e5130464de9e5f6/.github/workflows/linux.yml#L296).


#### Array API Strict

A simpler, and more manual, way of testing the Array API coverage is to
run your API calls along with the {ref}`array-api-strict` Python implementation.

This way you can ensure the outputs coming from your API match the minimal
reference implementation. Bear in mind, however, that you need to write
the tests cases yourself, so you need to also take into account the edge
cases as well.


(array-consumers)=

## Array Consumers

For array consumers, the main premise is to keep in mind that your **array
manipulation operations should not lock in for a particular array producing
library**. For instance, if you use NumPy for arrays, then your code could
contain:

```python
import numpy as np

# ...
b = np.full(shape, val, dtype=dtype) @ a
c = np.mean(a, axis=0)
return np.dot(c, b)
```

The first step should be as simple as assigning `np` namespace to a dedicated
namespace variable. The convention in the ecosystem is to name it `xp`. Then
making sure that each method and function call is something that Array API
supports is vital. `dot` is present in the NumPy's API but the standard
doesn't support it. For the sake of simplicity let's assume both `c` and `b`
are `ndim=2`, therefore we select `tensordot` instead - both NumPy and the
standard define it:

```python
import numpy as np

xp = np

# ...
b = xp.full(shape, val, dtype=dtype) @ a
c = xp.mean(a, axis=0)
return xp.tensordot(c, b, axes=1)
```

Then replacing one backend with another one should rely on providing a different
namespace, such as: `xp = torch`, e.g. via environment variable. This can be useful
if you're writing a script or in your custom software. The other alternatives are:

- If you are building a library where the backend is determined by input arrays,
  and your function accepts array arguments, then a recommended way is to ask
  your input arrays for a namespace to use: `xp = arr.__array_namespace__()`.
  If the given library doesn't have it, then [`array_api_compat.array_namespace()`](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.array_namespace)
  should be used instead:
  ```python
  def func(array1, scalar1, scalar2):
    xp = array1.__array_namespace__()  # or array_namespace(array1)
    return xp.arange(scalar1, scalar2) @ array1
  ```
- For a function that accepts scalars and returns arrays, use namespace `xp` as
  a parameter in the signature. Then enforcing objects to be of type by the
  provided backend can be achieved with `arg1 = xp.asarray(arg1)` for each input:
  ```python
  def func(s1, s2, xp):
    return xp.arange(s1, s2)
  ```

If you're relying on NumPy, CuPy, PyTorch, Dask, or JAX then
{ref}`array-api-compat` can come in handy for the transition. The compat layer
allows you to still rely on your selection of array producing library, while
making sure you're already using standard compatible API. Additionally, it
offers a set of useful utility functions, such as:

- [array_namespace()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.array_namespace)
  for fetching the namespace based on input arrays.
- [is_array_api_obj()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.is_array_api_obj)
  for the introspection whether a given object is Array API compatible.
- [device()](https://data-apis.org/array-api-compat/helper-functions.html#array_api_compat.device)
  to get a device the array resides on.

For now, the migration from a specific library (e.g., NumPy) to a standard
compatible setup requires a manual intervention for each failing API call,
but, in the future, we plan to provide some automation tools for it.
