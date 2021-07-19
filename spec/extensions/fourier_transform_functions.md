# Fourier transform Functions

> Array API specification for Fourier transform functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in {ref}`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

## Objects in API

<!-- NOTE: please keep the functions and their inverse together -->
(function-fft)=
### fft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional discrete Fourier transform. The expected behavior includes a round-trip transform using the inverse function, `fft(ifft(a)) == a`.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to the length `n` before computing the Fourier transform. Otherwise, the length of the input along the axis given by the `axis` keyword. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: No normalization.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: Normalize by `1/n`.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axis indicated by the `axis` keyword.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-ifft)=
### ifft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional inverse discrete Fourier transform.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to the length `n` before computing the inverse Fourier transform. Otherwise, the length of the input along the axis given by the `axis` keyword. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the inverse Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: Normalize by `1/n`.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: No normalization.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axis indicated by the `axis` keyword.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-fftn)=
### fftn(a, /, *, s=None, axes=None, norm='backward')

Computes the n-dimensional discrete Fourier transform.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **s**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Size of each transformed axis of the output. If given, each axis will be either zero-padded or trimmed to the length `s[i]` before computing the Fourier transform. Otherwise, the length of the input along the axis given by the `axes` keyword. Default: `None`.

-   **axes**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -  Axes over which to compute the Fourier transform. If not specified, the last `len(s)` axes are used, or all axes if `s` is not specified either. Default: `None`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: No normalization.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: Normalize by `1/n`.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axes indicated by the `axes` keyword.

#### Raises

-   If `s` and `axes` have different lengths.
-   If an element of `axes` is larger than the number of axes of `a`.

(function-ifftn)=
### ifftn(a, /, *, s=None, axes=None, norm='backward')

Computes the n-dimensional inverse discrete Fourier transform.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **s**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Size of each transformed axis of the output. If given, each axis will be either zero-padded or trimmed to the length `s[i]` before computing the inverse Fourier transform. Otherwise, the length of the input along the axis given by the `axes` keyword. Default: `None`.

-   **axes**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -  Axes over which to compute the inverse Fourier transform. If not specified, the last `len(s)` axes are used, or all axes if `s` is not specified either. Default: `None`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: Normalize by `1/n`.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: No normalization.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axes indicated by the `axes` keyword.

#### Raises

-   If `s` and `axes` have different lengths.
-   If an element of `axes` is larger than the number of axes of `a`.

(function-rfft)=
### rfft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional discrete Fourier transform for real-valued input.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the input array. If given, the input will be either zero-padded or trimmed to this length before computing the real Fourier transform. Otherwise, the length of the input along the axis specified by the `axis` keyword is used. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the real Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: No normalization.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: Normalize by `1/n`.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axis indicated by the `axis` keyword.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-irfft)=
### irfft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional inverse discrete Fourier transform for real-valued input.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to this length before computing the real Fourier transform. Otherwise, it will default to `2 * (m - 1)` where `m` is the length of the input along the axis given by the `axis` keyword. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the real Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: Normalize by `1/n`.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: No normalization.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axis indicated by the `axis` keyword.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-rfftn)=
### rfftn(a, /, *, s=None, axes=None, norm='backward')

Computes the n-dimensional discrete Fourier transform for real-valued input.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **s**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Size of each transformed axis of the output. If given, each axis will be either zero-padded or trimmed to the length `s[i]` before computing the real Fourier transform. Otherwise, no padding will be performed in each dimension. Default: `None`.

-   **axes**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -  Axes over which to compute the Fourier transform. If not specified, the last `len(s)` axes are used, or all axes if `s` is not specified either. Default: `None`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: No normalization.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: Normalize by `1/n`.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axes indicated by the `axes` keyword.

#### Raises

-   If `s` and `axes` have different lengths.
-   If an element of `axes` is larger than the number of axes of `a`.

(function-irfftn)=
### irfftn(a, /, *, s=None, axes=None, norm='backward')

Computes the n-dimensional inverse discrete Fourier transform for real-valued input.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **s**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Size of each transformed axis of the output. If given, each axis will be either zero-padded or trimmed to the length `s[i]` before computing the Fourier transform. Otherwise, no padding will be performed in each dimension. Default: `None`.

-   **axes**: _Union\[ Sequence\[ int ], Tuple\[ int, ... ] ]_

    -  Axes over which to compute the inverse Fourier transform. If it is not specified, the last `len(s)` axes are used or all axes if `s` is also not specified. Default: `None`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: Normalize by `1/n`.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: No normalization.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array transformed along the axes indicated by the `axes` keyword.

#### Raises

-   If `s` and `axes` have different lengths.
-   If an element of `axes` is larger than the number of axes of `a`.

(function-hfft)=
### hfft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional discrete Fourier transform of a signal with Hermitian symmetry.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to this length before computing the Hermitian Fourier transform. Otherwise, it will default to `2 * (m - 1)` where `m` is the length of the input along the axis given by the `axis` keyword. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: No normalization.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: Normalize by `1/n`.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   A transformed array.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-ihfft)=
### ihfft(a, /, *, n=None, axis=-1, norm='backward')

Computes the one-dimensional inverse discrete Fourier transform of a signal with Hermitian symmetry.

#### Parameters

-   **a**: _&lt;array&gt;_

    -   Input array.

-   **n**: _int_

    -   Length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to this length before computing the Hermitian Fourier transform. Otherwise, it will default to `2 * (m - 1)` where `m` is the length of the input along the axis given by the `axis` keyword. Default: `None`.

-   **axis**: _int_

    -  Axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: `-1`.

-   **norm**: _str_

    -   Specify the normalization mode. Should be one of the following modes:

        - `'backward'`: Normalize by `1/n`.
        - `'ortho'`: Normalize by `1/sqrt(n)`
        - `'forward'`: No normalization.

        Default: `'backward'`

#### Returns

-   **out**: _&lt;array&gt;_

    -   A transformed array.

#### Raises

-   If `axis` is not a valid axis of `a`.

(function-fftfreq)=
### fftfreq(n, /, *, d=1.0)

Returns the discrete Fourier transform sample frequencies. For a Fourier transform of length `n` and length unit of `d` the frequencies are described as:

```
f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n) if n is even
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n) if n is odd
```

#### Parameters

-   **n**: _int_

    -   Window length.

-   **d**: _float_

    -   Sample spacing between individual samples of the Fourier transform input. Default: `1.0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array of length `n` containing the sample frequencies.

(function-rfftfreq)=
### rfftfreq(n, /, *, d=1.0)

Returns the discrete Fourier transform sample frequencies. For a Fourier transform of length `n` and length unit of `d` the frequencies are described as:

```
f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n) if n is even
f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n) if n is odd
```

The Nyquist frequency component is considered to be positive.

#### Parameters

-   **n**: _int_

    -   Window length.

-   **d**: _float_

    -   Sample spacing between individual samples of the Fourier transform input. Default: `1.0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   An array of length `n` containing the sample frequencies.

(function-fftshift)=
### fftshift(x, /, *, axes=None)

Reorders n-dimensional FTT data to have negative frequency terms first. In this way, the zero-frequency component shifts to the center of the spectrum. Note that `out[0]` is the Nyquist component only if the length of the input is even.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   Input array.

-   **axes**: _Union\[ int, Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Axes over which to shift. If not specified, it shifts all axes. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   The shifted array.

(function-ifftshift)=
### ifftshift(x, /, *, axes=None)

Inverse of `fftshift`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   Input array.

-   **axes**: _Union\[ int, Sequence\[ int ], Tuple\[ int, ... ] ]_

    -   Axes over which to calculate. If not specified, it shifts all axes. Default: `None`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   The shifted array.
