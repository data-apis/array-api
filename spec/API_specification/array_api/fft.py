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
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array, the input array is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array, the input array is trimmed to length ``n``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
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
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array, the input array is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array, the input array is trimmed to length ``n``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def fftn(
    x: array,
    /,
    *,
    s: Sequence[int] = None,
    axes: Sequence[int] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (sizes, axes, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the output. If

        - ``s[i]`` is greater than the size of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to size ``s[i]``.
        - ``s[i]`` is less than the size of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to size ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the size of each transformed axis (dimension) in the output array must equal the size of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the size along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Sequence[int]
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
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def ifftn(
    x: array,
    /,
    *,
    s: Sequence[int] = None,
    axes: Sequence[int] = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
) -> array:
    """
    Computes the n-dimensional inverse discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (sizes, axes, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the output. If

        - ``s[i]`` is greater than the size of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to size ``s[i]``.
        - ``s[i]`` is less than the size of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to size ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the size of each transformed axis (dimension) in the output array must equal the size of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the size along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Sequence[int]
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
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
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

        - ``n`` is greater than the length of the input array, the input array is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array, the input array is trimmed to length ``n``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex-valued floating-point data type determined by :ref:`type-promotion`.
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

        - ``n//2+1`` is greater than the length of the input array, the input array is zero-padded to length ``n//2+1``.
        - ``n//2+1`` is less than the length of the input array, the input array is trimmed to length ``n//2+1``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length ``2*(m-1)``, where ``m`` is the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. The length along the transformed axis is ``n`` (if given) or ``2*(m-1)`` (otherwise).
    """


def rfftn(
    x: array,
    /,
    *,
    s: Sequence[int] = None,
    axes: Sequence[int] = None,
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
    s: Sequence[int]
        size of each transformed axis of the **input**. If

        - ``s[i]`` is greater than the size of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to size ``s[i]``.
        - ``s[i]`` is less than the size of the input array along a corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to size ``s[i]``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the size of each transformed axis (dimension) in the output array must equal the size of the corresponding axis in the input array.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the size along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Sequence[int]
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
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex-valued floating-point data type determined by :ref:`type-promotion`.
    """


def irfftn(
    x: array,
    /,
    *,
    s: Sequence[int] = None,
    axes: Sequence[int] = None,
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
    s: Sequence[int]
        size of each transformed axis of the **output**. ``n=s[i]`` is also the number of input points used along the axis (dimension) ``i``, except for the last axis, where ``n=s[-1]//2+1`` points of the input are used. If

        - ``n`` is greater than the size of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is zero-padded to size ``n``.
        - ``n`` is less than the size of the input array along the corresponding axis (dimension) ``i``, the input array along the axis ``i`` is trimmed to size ``n``.
        - ``s[i]`` is ``-1``, the whole input array along the axis ``i`` is used (no padding/trimming).
        - ``s`` is not provided, the size of each transformed axis (dimension) in the output array must equal the size of the corresponding axis in the input array, except for the last axis which is trimmed to ``2*(m-1)``, where ``m`` is the length of the input along the axis.

        If ``s`` is not ``None``, ``axes`` must not be ``None`` either, and ``s[i]`` corresponds to the size along the transformed axis specified by ``axes[i]``.

        Default: ``None``.
    axes: Sequence[int]
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
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. The length along the last transformed axis is ``s[-1]`` (if given) or ``2*(m - 1)`` (otherwise), and all other axes ``s[i]``.
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
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the **output**. If

        - ``n//2+1`` is greater than the length of the input array, the input array is zero-padded to length ``n//2+1``.
        - ``n//2+1`` is less than the length of the input array, the input array is trimmed to length ``n//2+1``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length ``2*(m-1)``, where ``m`` is the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
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

        - ``n`` is greater than the length of the input array, the input array is zero-padded to length ``n``.
        - ``n`` is less than the length of the input array, the input array is trimmed to length ``n``.
        - ``n`` is not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``.

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
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex-valued floating-point data type determined by :ref:`type-promotion`.
    """


def fftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Returns the discrete Fourier transform sample frequencies.

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
        an array of length ``n`` containing the sample frequencies. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """


def rfftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Returns the discrete Fourier transform sample frequencies (for ``rfft`` and ``irfft``).

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
        an array of length ``n//2+1`` containing the sample frequencies. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """


def fftshift(x: array, /, *, axes: Union[int, Sequence[int]] = None) -> array:
    """
    Shift the zero-frequency component to the center of the spectrum.

    This function swaps half-spaces for all axes (dimensions) specified by ``axes``.

    .. note::
       ``out[0]`` is the Nyquist component only if the length of the input is even.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Union[int, Sequence[int]]
        axes over which to shift. If ``None``, the function must shift all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type as ``x``.
    """


def ifftshift(x: array, /, *, axes: Union[int, Sequence[int]] = None) -> array:
    """
    Inverse of ``fftshift``.

    .. note::
       Although identical for even-length ``x``, ``fftshift`` and ``ifftshift`` differ by one sample for odd-length ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Union[int, Sequence[int]]
        axes over which to perform the inverse shift. If ``None``, the function must shift all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type as ``x``.
    """


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
