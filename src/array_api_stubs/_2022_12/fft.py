__all__ = [
    "fft",
    "ifft",
    "fftn",
    "ifftn",
    "rfft",
    "irfft",
    "rfftn",
    "irfftn",
    "hfft",
    "ihfft",
    "fftfreq",
    "rfftfreq",
    "fftshift",
    "ifftshift",
]

from ._types import Tuple, Union, Sequence, array, Optional, Literal, device


def fft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional discrete Fourier transform.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (length, axis, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array axis, the input array axis is trimmed to length ``n``.
        - ``n`` is not provided, the full the length of the input array axis must be used. The length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have the same data type as ``x``. The length along the transformed axis is ``n``, if given, or the length of the input along the axis specified by ``axis`` otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def ifft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same (length, axis, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array axis, the input array axis is trimmed to length ``n``.
        - ``n`` is not provided, the full the length of the input array axis must be used. The length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have the same data type as ``x``. The length along the transformed axis is ``n``, if given, or the length of the input along the axis specified by ``axis`` otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def fftn(
    x: array,
    /,
    *,
    s: Optional[Sequence[int]] = None,
    axes: Optional[Sequence[int]] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (sizes, axes, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    s: Optional[Sequence[int]]
        length of each transformed axis of the output. If

        - ``s[i]`` is greater than the length of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to length ``s[i]``.
        - ``s[i]`` is less than the length of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to length ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the length of each transformed axis (dimension) in the output array must equal the length of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the length along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the Fourier transform. If ``None``, all axes must be transformed.

        If ``s`` is specified, the corresponding ``axes`` to be transformed must be explicitly specified too.

        Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n = prod(s)`` is the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have the same data type as ``x``. The length along each transformed axis ``i`` is ``s[i]``, if ``s`` is given and ``s[i]`` is not ``-1``, or the length of the corresponding axis of the input array otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def ifftn(
    x: array,
    /,
    *,
    s: Optional[Sequence[int]] = None,
    axes: Optional[Sequence[int]] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional inverse discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (sizes, axes, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    s: Optional[Sequence[int]]
        length of each transformed axis of the output. If

        - ``s[i]`` is greater than the length of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to length ``s[i]``.
        - ``s[i]`` is less than the length of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to length ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the length of each transformed axis (dimension) in the output array must equal the length of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the length along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the Fourier transform. If ``None``, all axes must be transformed.

        If ``s`` is specified, the corresponding ``axes`` to be transformed must be explicitly specified too.

        Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n = prod(s)`` is the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have the same data type as ``x``. The length along each transformed axis ``i`` is ``s[i]``, if ``s`` is given and ``s[i]`` is not ``-1``, or the length of the corresponding axis of the input array otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def rfft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional discrete Fourier transform for real-valued input.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axis and normalization mode) and consistent length.

    Parameters
    ----------
    x: array
        input array. Must have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **input**. If

        - ``n`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array axis, the input array axis is trimmed to length ``n``.
        - ``n`` is not provided, the full the length of the input array axis must be used.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). If ``n`` is even, the length of the transformed axis is ``(n/2)+1``. If ``n`` is odd, the length is ``(n+1)/2``. If ``n`` is ``None``, it defaults to ``x.shape[axis]``.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def irfft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional inverse of ``rfft`` for complex-valued input.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axis and normalization mode) and consistent length.

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    n: int
        length of the transformed axis of the **output**. If

        - ``n//2+1`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n//2+1``.
        - ``n//2+1`` is less than the length of the input array, the input array axis is trimmed to length ``n//2+1``.
        - ``n`` is not provided, the full the length of the input array axis must be used. The length of the transformed axis of the output must equal ``2*(x.shape[axis]-1)``.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The length along the transformed axis is ``n``, if given, or ``2*(x.shape[axis]-1)`` otherwise. Therefore, to get an odd number of output points along ``axis``, ``n`` must be specified.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def rfftn(
    x: array,
    /,
    *,
    s: Optional[Sequence[int]] = None,
    axes: Optional[Sequence[int]] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional discrete Fourier transform for real-valued input.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfftn(rfftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axes and normalization mode) and consistent sizes.

    Parameters
    ----------
    x: array
        input array. Must have a real-valued floating-point data type.
    s: Optional[Sequence[int]]
        length of each transformed axis of the **input**. If

        - ``s[i]`` is greater than the length of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to length ``s[i]``.
        - ``s[i]`` is less than the length of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to length ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the length of each transformed axis (dimension) in the output array must equal the length of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the length along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the Fourier transform. If ``None``, all axes must be transformed.

        If ``s`` is specified, the corresponding ``axes`` to be transformed must be explicitly specified too.

        Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n = prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). The length along the last transformed axis must be equal to ``s[-1]//2+1`` and the length along the remaining transformed axes ``i``  must be equal to ``s[i]``, where ``s`` defaults to ``x.shape`` if the parameter ``s`` is ``None`` and ``s[i]`` defaults to ``x.shape[i]`` if ``s[i]`` is ``-1``.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def irfftn(
    x: array,
    /,
    *,
    s: Optional[Sequence[int]] = None,
    axes: Optional[Sequence[int]] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional inverse of ``rfftn`` for complex-valued input.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfftn(rfftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axes and normalization mode) and consistent sizes.

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    s: Optional[Sequence[int]]
        length of each transformed axis of the **output**. ``n=s[i]`` is also the number of input points used along the axis (dimension) ``i``, except for the last axis, where ``n=s[-1]//2+1`` points of the input are used. If

        - ``n`` is greater than the length of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to length ``n``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the length of each transformed axis (dimension) in the output array must equal the length of the corresponding axis in the input array, except for the last axis which is trimmed to ``2*(m-1)``, where ``m`` is the length of the input along the axis.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the length along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the Fourier transform. If ``None``, all axes must be transformed.

        If ``s`` is specified, the corresponding ``axes`` to be transformed must be explicitly specified too.

        Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n = prod(s)`` is the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The length along the last transformed axis is ``s[-1]`` if given, or ``2*(m - 1)`` otherwise, and all other axes ``s[i]``. Therefore, to get an odd number of output points along the last axis, ``s`` must be specified.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def hfft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    x: array
        input array. Should have a complex-valued floating-point data type.
    n: int
        length of the transformed axis of the **output**. If

        - ``n//2+1`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n//2+1``.
        - ``n//2+1`` is less than the length of the input array axis, the input array axis is trimmed to length ``n//2+1``.
        - ``n`` is not provided, the full the length of the input array axis must be used. The length of the transformed axis of the output must equal ``2*(m-1)``, where ``m`` is the length of the input along the axis specified by ``axis``.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The length along the transformed axis is ``n``, if given or ``2*(m-1)`` otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def ihfft(
    x: array,
    /,
    *,
    n: Optional[int] = None,
    axis: int = -1,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    x: array
        input array. Must have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **input**. If

        - ``n`` is greater than the length of the input array axis, the input array axis is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array axis, the input array axis is trimmed to length ``n``.
        - ``n`` is not provided, the full the length of the input array axis must be used. The length of the transformed axis must equal ``m//2 + 1``, where ``m`` is the length of the input along the axis specified by ``axis``.

        Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If not set, the last axis (dimension) is used.

        Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). The length along the transformed axis is ``m//2 + 1``, where ``m` is ``n` if ``n`` is given, or the length of the input along the axis specified by ``axis`` otherwise.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def fftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Computes the discrete Fourier transform sample frequencies.

    For a Fourier transform of length ``n`` and length unit of ``d`` the frequencies are described as:

    .. code-block::

      f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n)        # if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)  # if n is odd

    Parameters
    ----------
    n: int
        window length.
    d: float
        sample spacing between individual samples of the Fourier transform input. Default: ``1.0``.
    device: Optional[device]
        device on which to place the created array. Default: ``None``.

    Returns
    -------
    out: array
        an array of shape ``(n,)`` containing the sample frequencies. The returned array must have the default real-valued floating-point data type.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def rfftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Computes the discrete Fourier transform sample frequencies (for ``rfft`` and ``irfft``).

    For a Fourier transform of length ``n`` and length unit of ``d`` the frequencies are described as:

    .. code-block::

      f = [0, 1, ...,     n/2-1,     n/2] / (d*n)  # if n is even
      f = [0, 1, ..., (n-1)/2-1, (n-1)/2] / (d*n)  # if n is odd

    The Nyquist frequency component is considered to be positive.

    Parameters
    ----------
    n: int
        window length.
    d: float
        sample spacing between individual samples of the Fourier transform input. Default: ``1.0``.
    device: Optional[device]
        device on which to place the created array. Default: ``None``.

    Returns
    -------
    out: array
        an array of shape ``(n//2+1,)`` containing the sample frequencies. The returned array must have the default real-valued floating-point data type.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def fftshift(x: array, /, *, axes: Optional[Union[int, Sequence[int]]] = None) -> array:
    """
    Shift the zero-frequency component to the center of the spectrum.

    This function swaps half-spaces for all axes (dimensions) specified by ``axes``.

    .. note::
       ``out[0]`` is the Nyquist component only if the length of the input is even.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Optional[Union[int, Sequence[int]]]
        axes over which to shift. If ``None``, the function must shift all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type as ``x``. The returned array must have the same shape as the input array ``x``.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def ifftshift(x: array, /, *, axes: Optional[Union[int, Sequence[int]]] = None) -> array:
    """
    Inverse of ``fftshift``.

    .. note::
       Although identical for even-length ``x``, ``fftshift`` and ``ifftshift`` differ by one sample for odd-length ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Optional[Union[int, Sequence[int]]]
        axes over which to perform the inverse shift. If ``None``, the function must shift all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type as ``x``. The returned array must have the same shape as the input array ``x``.

    Notes
    -----

    .. versionadded:: 2022.12
    """
