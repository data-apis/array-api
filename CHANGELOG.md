# Changelog

> Specification changelog.

## v2022.12

### Updates

#### APIs

- `__bool__`: add support for non-boolean data types ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `__abs__`: add complex number support ([gh-546](https://github.com/data-apis/array-api/pull/546))
- `__add__`: add complex number support ([gh-525](https://github.com/data-apis/array-api/pull/525))
- `__dlpack__`: raise `BufferError` when data cannot be exported as DLPack ([gh-498](https://github.com/data-apis/array-api/pull/498))
- `__eq__`: add complex number support ([gh-528](https://github.com/data-apis/array-api/pull/528))
- `__float__`: add support for non-floating-point data types ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `__int__`: add support for non-integer data types ([gh-497](https://github.com/data-apis/array-api/pull/497))
- `__matmul__`: add complex number support ([gh-557](https://github.com/data-apis/array-api/pull/557))
- `__mul__`: add complex number support ([gh-551](https://github.com/data-apis/array-api/pull/551))
- `__ne__`: add complex number support ([gh-529](https://github.com/data-apis/array-api/pull/529))
- `__neg__`: add complex number support ([gh-448](https://github.com/data-apis/array-api/pull/448))
- `__pos__`: add complex number support ([gh-447](https://github.com/data-apis/array-api/pull/447))
- `__pow__`: add complex number support ([gh-537](https://github.com/data-apis/array-api/pull/537))
- `__sub__`: add complex number support ([gh-526](https://github.com/data-apis/array-api/pull/526))
- `__truediv__`: add complex number support ([gh-554](https://github.com/data-apis/array-api/pull/554))
- `abs`: add complex number support ([gh-546](https://github.com/data-apis/array-api/pull/546))
- `acos`: add complex number support ([gh-517](https://github.com/data-apis/array-api/pull/517))
- `acosh`: add complex number support ([gh-520](https://github.com/data-apis/array-api/pull/520))
- `add`: add complex number support ([gh-525](https://github.com/data-apis/array-api/pull/525))
- `asin`: add complex number support ([gh-521](https://github.com/data-apis/array-api/pull/521))
- `asinh`: add complex number support ([gh-522](https://github.com/data-apis/array-api/pull/522))
- `atan`: add complex number support ([gh-523](https://github.com/data-apis/array-api/pull/523))
- `atanh`: add complex number support ([gh-524](https://github.com/data-apis/array-api/pull/524))
- `all`: add complex number support ([gh-442](https://github.com/data-apis/array-api/pull/442))
- `any`: add complex number support ([gh-442](https://github.com/data-apis/array-api/pull/442))
- `asarray`: add complex number support ([gh-434](https://github.com/data-apis/array-api/pull/434))
- `astype`: add complex number support ([gh-445](https://github.com/data-apis/array-api/pull/445))
- `cos`: add complex number support ([gh-454](https://github.com/data-apis/array-api/pull/454))
- `cosh`: add complex number support ([gh-453](https://github.com/data-apis/array-api/pull/453))
- `divide`: add complex number support ([gh-554](https://github.com/data-apis/array-api/pull/554))
- `equal`: add complex number support ([gh-528](https://github.com/data-apis/array-api/pull/528))
- `eye`: add complex number support ([gh-436](https://github.com/data-apis/array-api/pull/436))
- `exp`: add complex number support ([gh-451](https://github.com/data-apis/array-api/pull/451))
- `expm1`: add complex number support ([gh-452](https://github.com/data-apis/array-api/pull/452))
- `finfo`: add complex number support ([gh-484](https://github.com/data-apis/array-api/pull/484))
- `full`: add complex number support ([gh-435](https://github.com/data-apis/array-api/pull/435))
- `full_like`: add complex number support ([gh-435](https://github.com/data-apis/array-api/pull/435))
- `isfinite`: add complex number support ([gh-531](https://github.com/data-apis/array-api/pull/531))
- `isinf`: add complex number support ([gh-530](https://github.com/data-apis/array-api/pull/530))
- `isnan`: add complex number support ([gh-532](https://github.com/data-apis/array-api/pull/532))
- `linspace`: add complex number support ([gh-568](https://github.com/data-apis/array-api/pull/568))
- `log`: add complex number support ([gh-514](https://github.com/data-apis/array-api/pull/514))
- `log1p`: add complex number support ([gh-534](https://github.com/data-apis/array-api/pull/534))
- `log10`: add complex number support ([gh-536](https://github.com/data-apis/array-api/pull/536))
- `log2`: add complex number support ([gh-535](https://github.com/data-apis/array-api/pull/535))
- `matmul`: add complex number support ([gh-557](https://github.com/data-apis/array-api/pull/557))
- `meshgrid`: add complex number support ([gh-437](https://github.com/data-apis/array-api/pull/437))
- `multiply`: add complex number support ([gh-551](https://github.com/data-apis/array-api/pull/551))
- `negative`: add complex number support ([gh-448](https://github.com/data-apis/array-api/pull/448))
- `nonzero`: add complex number support ([gh-441](https://github.com/data-apis/array-api/pull/441))
- `not_equal`: add complex number support ([gh-529](https://github.com/data-apis/array-api/pull/529))
- `ones`: add complex number support ([gh-438](https://github.com/data-apis/array-api/pull/438))
- `ones_like`: add complex number support ([gh-438](https://github.com/data-apis/array-api/pull/438))
- `positive`: add complex number support ([gh-447](https://github.com/data-apis/array-api/pull/447))
- `pow`: add complex number support ([gh-537](https://github.com/data-apis/array-api/pull/537))
- `prod`: add complex number support ([gh-553](https://github.com/data-apis/array-api/pull/553))
- `round`: add complex number support ([gh-440](https://github.com/data-apis/array-api/pull/440))
- `sign`: add complex number support ([gh-556](https://github.com/data-apis/array-api/pull/556))
- `sin`: add complex number support ([gh-457](https://github.com/data-apis/array-api/pull/457))
- `sinh`: add complex number support ([gh-456](https://github.com/data-apis/array-api/pull/456))
- `square`: add complex number support ([gh-552](https://github.com/data-apis/array-api/pull/552))
- `sqrt`: add complex number support ([gh-461](https://github.com/data-apis/array-api/pull/461))
- `subtract`: add complex number support ([gh-526](https://github.com/data-apis/array-api/pull/526))
- `sum`: add complex number support ([gh-538](https://github.com/data-apis/array-api/pull/538))
- `tan`: add complex number support ([gh-459](https://github.com/data-apis/array-api/pull/459))
- `tanh`: add complex number support ([gh-458](https://github.com/data-apis/array-api/pull/458))
- `tensordot`: add complex number support ([gh-558](https://github.com/data-apis/array-api/pull/558))
- `unique_all`: add complex number support ([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_counts`: add complex number support ([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_inverse`: add complex number support ([gh-540](https://github.com/data-apis/array-api/pull/540))
- `unique_values`: add complex number support ([gh-540](https://github.com/data-apis/array-api/pull/540))
- `vecdot`: add complex number support ([gh-512](https://github.com/data-apis/array-api/pull/512))

#### Extensions

- Mechanism by which to access extension APIs ([gh-470](https://github.com/data-apis/array-api/pull/470))
- `linalg.cholesky`: add complex number support ([gh-443](https://github.com/data-apis/array-api/pull/443))
- `linalg.cross`: add support for broadcasting ([gh-417](https://github.com/data-apis/array-api/pull/417))
- `linalg.cross`: add complex number support ([gh-559](https://github.com/data-apis/array-api/pull/559))
- `linalg.det`: add complex number support ([gh-542](https://github.com/data-apis/array-api/pull/542))
- `linalg.eigh`: add complex number support ([gh-543](https://github.com/data-apis/array-api/pull/543))
- `linalg.eigvalsh`: add complex number support ([gh-543](https://github.com/data-apis/array-api/pull/543))
- `linalg.inv`: add complex number support ([gh-547](https://github.com/data-apis/array-api/pull/547))
- `linalg.matrix_norm`: add complex number support ([gh-565](https://github.com/data-apis/array-api/pull/565))
- `linalg.matrix_power`: add complex number support ([gh-549](https://github.com/data-apis/array-api/pull/549))
- `linalg.matrix_rank`: add complex number support ([gh-563](https://github.com/data-apis/array-api/pull/563))
- `linalg.outer`: add complex number support ([gh-560](https://github.com/data-apis/array-api/pull/560))
- `linalg.pinv`: add complex number support ([gh-564](https://github.com/data-apis/array-api/pull/564))
- `linalg.qr`: add complex number support ([gh-548](https://github.com/data-apis/array-api/pull/548))
- `linalg.slogdet`: add complex number support ([gh-567](https://github.com/data-apis/array-api/pull/567))
- `linalg.solve`: add complex number support ([gh-566](https://github.com/data-apis/array-api/pull/566))
- `linalg.svd`: add complex number support ([gh-561](https://github.com/data-apis/array-api/pull/561))
- `linalg.svdvals`: add complex number support ([gh-562](https://github.com/data-apis/array-api/pull/562))
- `linalg.trace`: add support for specifying output array data type ([gh-502](https://github.com/data-apis/array-api/pull/502))
- `linalg.trace`: add complex number support ([gh-541](https://github.com/data-apis/array-api/pull/541))
- `linalg.vector_norm`: add complex number support ([gh-550](https://github.com/data-apis/array-api/pull/550))

* * *

### Additions

#### Data Types

- `complex64`: single-precision complex floating-point numbers ([gh-418](https://github.com/data-apis/array-api/pull/418))
- `complex128`: double-precision complex floating-point numbers ([gh-418](https://github.com/data-apis/array-api/pull/418))
- Type promotion rules: real-complex and complex-complex data type promotion guidance ([gh-491](https://github.com/data-apis/array-api/pull/491))
- Guidance for mixing arrays and Python `complex` scalars ([gh-513](https://github.com/data-apis/array-api/pull/513))
- Guidance for data type variability across devices ([gh-515](https://github.com/data-apis/array-api/pull/515))
- Guidance for complex number ordering ([gh-527](https://github.com/data-apis/array-api/pull/527))
- Guidance for complex number equality ([gh-528](https://github.com/data-apis/array-api/pull/528))

**note**: conforming implementations must define a default complex floating-point data type.

#### APIs

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