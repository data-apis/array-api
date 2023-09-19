# Changelog

> Specification changelog.

This changelog is organized by specification version and notes all changes with respect to the previous version. Within the section for a specific version (e.g., v2022.12), separate sections are used for (a) changes to existing APIs and requirements, (b) new APIs and new requirements, and (c) errata.

## v2022.12

### Updates

> Updates to existing APIs and requirements.

#### APIs

- `__bool__`: add support for non-boolean data types ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `__dlpack__`: raise `BufferError` when data cannot be exported as DLPack ([gh-498](https://github.com/data-apis/array-api/pull/498))
- `__float__`: add support for non-floating-point data types ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `__int__`: add support for non-integer data types ([gh-497](https://github.com/data-apis/array-api/pull/497))

##### Complex Number Support

The following APIs were updated to support arrays having complex floating-point data types:

- `__abs__`([gh-546](https://github.com/data-apis/array-api/pull/546))
- `__add__`([gh-525](https://github.com/data-apis/array-api/pull/525))
- `__eq__`([gh-528](https://github.com/data-apis/array-api/pull/528))
- `__matmul__`([gh-557](https://github.com/data-apis/array-api/pull/557))
- `__mul__`([gh-551](https://github.com/data-apis/array-api/pull/551))
- `__ne__`([gh-529](https://github.com/data-apis/array-api/pull/529))
- `__neg__`([gh-448](https://github.com/data-apis/array-api/pull/448))
- `__pos__`([gh-447](https://github.com/data-apis/array-api/pull/447))
- `__pow__`([gh-537](https://github.com/data-apis/array-api/pull/537))
- `__sub__`([gh-526](https://github.com/data-apis/array-api/pull/526))
- `__truediv__`([gh-554](https://github.com/data-apis/array-api/pull/554))
- `abs`([gh-546](https://github.com/data-apis/array-api/pull/546))
- `acos`([gh-517](https://github.com/data-apis/array-api/pull/517))
- `acosh`([gh-520](https://github.com/data-apis/array-api/pull/520))
- `add`([gh-525](https://github.com/data-apis/array-api/pull/525))
- `asin`([gh-521](https://github.com/data-apis/array-api/pull/521))
- `asinh`([gh-522](https://github.com/data-apis/array-api/pull/522))
- `atan`([gh-523](https://github.com/data-apis/array-api/pull/523))
- `atanh`([gh-524](https://github.com/data-apis/array-api/pull/524))
- `all`([gh-442](https://github.com/data-apis/array-api/pull/442))
- `any`([gh-442](https://github.com/data-apis/array-api/pull/442))
- `asarray`([gh-434](https://github.com/data-apis/array-api/pull/434))
- `astype`([gh-445](https://github.com/data-apis/array-api/pull/445))
- `cos`([gh-454](https://github.com/data-apis/array-api/pull/454))
- `cosh`([gh-453](https://github.com/data-apis/array-api/pull/453))
- `divide`([gh-554](https://github.com/data-apis/array-api/pull/554))
- `equal`([gh-528](https://github.com/data-apis/array-api/pull/528))
- `eye`([gh-436](https://github.com/data-apis/array-api/pull/436))
- `exp`([gh-451](https://github.com/data-apis/array-api/pull/451))
- `expm1`([gh-452](https://github.com/data-apis/array-api/pull/452))
- `finfo`([gh-484](https://github.com/data-apis/array-api/pull/484))
- `full`([gh-435](https://github.com/data-apis/array-api/pull/435))
- `full_like`([gh-435](https://github.com/data-apis/array-api/pull/435))
- `isfinite`([gh-531](https://github.com/data-apis/array-api/pull/531))
- `isinf`([gh-530](https://github.com/data-apis/array-api/pull/530))
- `isnan`([gh-532](https://github.com/data-apis/array-api/pull/532))
- `linspace`([gh-568](https://github.com/data-apis/array-api/pull/568))
- `log`([gh-514](https://github.com/data-apis/array-api/pull/514))
- `log1p`([gh-534](https://github.com/data-apis/array-api/pull/534))
- `log10`([gh-536](https://github.com/data-apis/array-api/pull/536))
- `log2`([gh-535](https://github.com/data-apis/array-api/pull/535))
- `matmul`([gh-557](https://github.com/data-apis/array-api/pull/557))
- `meshgrid`([gh-437](https://github.com/data-apis/array-api/pull/437))
- `multiply`([gh-551](https://github.com/data-apis/array-api/pull/551))
- `negative`([gh-448](https://github.com/data-apis/array-api/pull/448))
- `nonzero`([gh-441](https://github.com/data-apis/array-api/pull/441))
- `not_equal`([gh-529](https://github.com/data-apis/array-api/pull/529))
- `ones`([gh-438](https://github.com/data-apis/array-api/pull/438))
- `ones_like`([gh-438](https://github.com/data-apis/array-api/pull/438))
- `positive`([gh-447](https://github.com/data-apis/array-api/pull/447))
- `pow`([gh-537](https://github.com/data-apis/array-api/pull/537))
- `prod`([gh-553](https://github.com/data-apis/array-api/pull/553))
- `round`([gh-440](https://github.com/data-apis/array-api/pull/440))
- `sign`([gh-556](https://github.com/data-apis/array-api/pull/556))
- `sin`([gh-457](https://github.com/data-apis/array-api/pull/457))
- `sinh`([gh-456](https://github.com/data-apis/array-api/pull/456))
- `square`([gh-552](https://github.com/data-apis/array-api/pull/552))
- `sqrt`([gh-461](https://github.com/data-apis/array-api/pull/461))
- `subtract`([gh-526](https://github.com/data-apis/array-api/pull/526))
- `sum`([gh-538](https://github.com/data-apis/array-api/pull/538))
- `tan`([gh-459](https://github.com/data-apis/array-api/pull/459))
- `tanh`([gh-458](https://github.com/data-apis/array-api/pull/458))
- `tensordot`([gh-558](https://github.com/data-apis/array-api/pull/558))
- `unique_all`([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_counts`([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_inverse`([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_values`([gh-540](https://github.com/data-apis/array-api/pull/540))
- `vecdot`([gh-512](https://github.com/data-apis/array-api/pull/512))

#### Extensions

> Updates to APIs and requirements included as part of specification extensions.

- Mechanism by which to access extension APIs ([gh-470](https://github.com/data-apis/array-api/pull/470))
- `linalg.cross`: add support for broadcasting ([gh-417](https://github.com/data-apis/array-api/pull/417))
- `linalg.trace`: add support for specifying output array data type ([gh-502](https://github.com/data-apis/array-api/pull/502))

##### Complex Number Support

The following APIs were updated to support arrays having complex floating-point data types:

- `linalg.cholesky`([gh-443](https://github.com/data-apis/array-api/pull/443))
- `linalg.cross`([gh-559](https://github.com/data-apis/array-api/pull/559))
- `linalg.det`([gh-542](https://github.com/data-apis/array-api/pull/542))
- `linalg.eigh`([gh-543](https://github.com/data-apis/array-api/pull/543))
- `linalg.eigvalsh`([gh-543](https://github.com/data-apis/array-api/pull/543))
- `linalg.inv`([gh-547](https://github.com/data-apis/array-api/pull/547))
- `linalg.matrix_norm`([gh-565](https://github.com/data-apis/array-api/pull/565))
- `linalg.matrix_power`([gh-549](https://github.com/data-apis/array-api/pull/549))
- `linalg.matrix_rank`([gh-563](https://github.com/data-apis/array-api/pull/563))
- `linalg.outer`([gh-560](https://github.com/data-apis/array-api/pull/560))
- `linalg.pinv`([gh-564](https://github.com/data-apis/array-api/pull/564))
- `linalg.qr`([gh-548](https://github.com/data-apis/array-api/pull/548))
- `linalg.slogdet`([gh-567](https://github.com/data-apis/array-api/pull/567))
- `linalg.solve`([gh-566](https://github.com/data-apis/array-api/pull/566))
- `linalg.svd`([gh-561](https://github.com/data-apis/array-api/pull/561))
- `linalg.svdvals`([gh-562](https://github.com/data-apis/array-api/pull/562))
- `linalg.trace`([gh-541](https://github.com/data-apis/array-api/pull/541))
- `linalg.vector_norm`([gh-550](https://github.com/data-apis/array-api/pull/550))

* * *

### Additions

> New APIs and requirements added to the specification.

#### Data Types

The following data types were added to the specification:

- `complex64`: single-precision complex floating-point numbers ([gh-418](https://github.com/data-apis/array-api/pull/418))
- `complex128`: double-precision complex floating-point numbers ([gh-418](https://github.com/data-apis/array-api/pull/418))

To support complex floating-point numbers, the following requirements were added to the specification:

- Type promotion rules: real-complex and complex-complex data type promotion guidance ([gh-491](https://github.com/data-apis/array-api/pull/491))
- Guidance for mixing arrays and Python `complex` scalars ([gh-513](https://github.com/data-apis/array-api/pull/513))
- Guidance for data type variability across devices ([gh-515](https://github.com/data-apis/array-api/pull/515))
- Guidance for complex number ordering ([gh-527](https://github.com/data-apis/array-api/pull/527))
- Guidance for complex number equality ([gh-528](https://github.com/data-apis/array-api/pull/528))
- Guidance for value-based promotion when results are outside of their real domain ([gh-573](https://github.com/data-apis/array-api/pull/573))

**note**: conforming implementations must define a default complex floating-point data type.

#### APIs

The following APIs were added to the specification:

- `__array_api_version__`: string representing the version of the array API specification ([gh-480](https://github.com/data-apis/array-api/pull/480))
- `__complex__`: convert a zero-dimensional array to a Python `complex` object ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `conj`: return the complex conjugate of a complex number ([gh-446](https://github.com/data-apis/array-api/pull/446))
- `finfo.dtype`: floating-point data type ([gh-485](https://github.com/data-apis/array-api/pull/485))
- `iinfo.dtype`: integer data type ([gh-485](https://github.com/data-apis/array-api/pull/485))
- `imag`: return the imaginary component of a complex number ([gh-496](https://github.com/data-apis/array-api/pull/496))
- `isdtype`: test whether a provided `dtype` is of a specified data type kind ([gh-503](https://github.com/data-apis/array-api/pull/503))
- `real`: return the real component of a complex number ([gh-427](https://github.com/data-apis/array-api/pull/427))
- `take`: return elements of an array along a specified axis ([gh-416](https://github.com/data-apis/array-api/pull/416))

#### Extensions

The following optional extensions were added to the specification:

- `fft`: Fast Fourier Transforms (FFT) ([gh-189](https://github.com/data-apis/array-api/pull/189))

	- `fft`
	- `ifft`
	- `fftn`
	- `ifftn`
	- `rfft`
	- `rfftn`
	- `irfft`
	- `irfttn`
	- `fftfreq`
	- `rfftfreq`
	- `fftshift`
	- `ifftshift`

* * *

### Errata

The following is a list of fixes and points of clarification with regard to the previous version of the specification:

- Missing `self` parameter for array object properties ([gh-464](https://github.com/data-apis/array-api/pull/464))
- `__setitem__`: clarify that in-place element-wise operations must not change the shape of the in-place array as a result of broadcasting ([gh-429](https://github.com/data-apis/array-api/pull/429))
- `full`: missing type annotation for `bool` fill values ([gh-435](https://github.com/data-apis/array-api/pull/435))
- `full_like`: missing type annotation for `bool` fill values ([gh-435](https://github.com/data-apis/array-api/pull/435))
- `iinfo`: fix typo in description ([gh-439](https://github.com/data-apis/array-api/pull/439))
- `linalg.eigh`: fix input data type to allow non-floating-point data types for backward compat in alignment with other `linalg` APIs ([gh-572](https://github.com/data-apis/array-api/pull/572))
- `linalg.eigvalsh`: fix input data type to allow non-floating-point data types for backward compat in alignment with other `linalg` APIs ([gh-572](https://github.com/data-apis/array-api/pull/572))
- `linalg.matrix_rank`: fix return data type ([gh-510](https://github.com/data-apis/array-api/pull/510))
- `linalg.trace`: clarify special cases for floating-point operands and the empty sum ([gh-502](https://github.com/data-apis/array-api/pull/502))
- `linspace`: conversion of `start` and `stop` should follow type promotion rules ([gh-568](https://github.com/data-apis/array-api/pull/568))
- `nonzero`: clarify that, for arrays having a boolean data type, non-zero elements are those elements which equal `True` ([gh-441](https://github.com/data-apis/array-api/pull/441))
- `trunc`: fix description ([gh-511](https://github.com/data-apis/array-api/pull/511))
- `vecdot`: clarify broadcasting behavior ([gh-417](https://github.com/data-apis/array-api/pull/417) and [gh-473](https://github.com/data-apis/array-api/pull/473))
