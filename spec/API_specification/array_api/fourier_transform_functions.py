from ._types import Tuple, Union, Sequence, array, Optional, Literal


def fft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array, the input array must be zero-padded such that the input array has length ``n``.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        If not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def ifft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array, the input array must be zero-padded such that the input array has length ``n``.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        If not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def fftn(x: array, /, *, s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the output. If

        - ``s[i]`` is greater than the size of the input array along a corresponding axis (dimension) ``i``, the corresponding axis of the input array must be zero-padded such that the axis has size ``s[i]``.
        - ``s[i]`` is less than the size of the input array along a corresponding axis (dimension) ``i``, the corresponding axis of the input array must be trimmed such that the axis has size ``s[i]``.


        If ``axes`` is not ``None``, size ``s[i]`` corresponds to the size of axis ``axes[j]`` where ``i == j``.

        If not provided, the size of each transformed axis (dimension) in the output array must equal the size of the corresponding axis in the input array.

        Default: ``None``.
    axes: Sequence[int]
        axes (dimension) over which to compute the Fourier transform. If ``None`` and ``s`` is not specified, all axes must be transformed. If ``s`` is specified, the corresponding ``axes`` to be transformed must be explicitly specified too. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determine by :ref:`type-promotion`.
    """


def ifftn(x: array, /, *, s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional inverse discrete Fourier transform.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifftn(fftn(x)) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the output. If

        - ``s[i]`` is greater than the size of the input array along a corresponding axis (dimension) ``j``, the corresponding axis of the input array must be zero-padded such that the axis has size ``s[i]``.
        - ``s[i]`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``.

        If not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Sequence[int]
        axes over which to compute the inverse Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determine by :ref:`type-promotion`.
    """


def rfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform for real-valued input.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x), n=x.shape[axis]) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **input**. If

        - ``n`` is greater than the length of the input array, the input array must be zero-padded such that the input array has length ``n``.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        If not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def irfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional inverse of ``rfft``.

    .. note::
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x), n=x.shape[axis]) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    n: int
        length of the transformed axis of the **output**. If

        - ``n//2+1`` is greater than the length of the input array, the input array must be zero-padded.
        - ``n//2+1`` is less than the length of the input array, the input array must be trimmed.

        If not provided, the length of the transformed axis of the output must equal the length ``2 * (m - 1)`` where ``m`` is the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real floating-point data type determined by :ref:`type-promotion`. The length along the transformed axis is ``n`` (if given) or ``2 * (m - 1)``.
    """


def rfftn(x: array, /, *, s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform for real-valued input.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfftn(rfftn(x), n=x.shape[axis]) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the output. If

        - ``s[i]`` is greater than the size of the input array along a corresponding axis (dimension) ``j``, the corresponding axis of the input array must be zero-padded such that the axis has size ``s[i]``.
        - ``s[i]`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``.

        If not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Sequence[int]
        axes over which to compute the Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def irfftn(x: array, /, *, s: Sequence[int] = None, axes: Sequence[int] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional inverse of ``rfftn``.

    .. note::
       Applying the n-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfftn(rfftn(x), n=x.shape[axis]) == x``), provided that the transform and inverse transform are performed with the same normalization mode.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    s: Sequence[int]
        size of each transformed axis of the **output**. If

        - ``s[i]`` is greater than the size of the input array along a corresponding axis (dimension) ``j``, the corresponding axis of the input array must be zero-padded such that the axis has size ``s[i]``.
        - ``s[i]`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``. Except for the last axis is trimmed to ``2 * (m - 1)``, where `m` is the length of the input along the axis.

        If not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Sequence[int]
        axes over which to compute the inverse Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. The length along the last transformed axis is ``s[-1]`` (if given) or ``2 * (m - 1)``, and all other axes ``s[i]``.
    """


def hfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is greater than the length of the input array, the input array must be zero-padded such that the input array has length ``n``.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        If not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
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


def ihfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **input**. If

        - ``n`` is greater than the length of the input array, the input array must be zero-padded such that the input array has length ``n``.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        If not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        where ``n`` equals ``prod(s)``, the logical FFT size.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex-valued floating-point data type determined by :ref:`type-promotion`.
    """


def fftfreq(n: int, /, *, d: float = 1.0):
    """
    Returns the discrete Fourier transform sample frequencies.

    For a Fourier transform of length ``n`` and length unit of ``d`` the frequencies are described as:

    .. code-block::

      f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n)       # if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n) # if n is odd

    Parameters
    ----------
    n: int
        window length.
    d: float
        sample spacing between individual samples of the Fourier transform input. Default: ``1.0``.

    Returns
    -------
    out: array
        an array of length ``n`` containing the sample frequencies. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """


def rfftfreq(n: int, /, *, d: float = 1.0):
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

    Returns
    -------
    out: array
        an array of length ``n//2+1`` containing the sample frequencies. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """


def fftshift(x: array, /, *, axes: Union[int, Sequence[int]] = None):
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


def ifftshift(x: array, /, *, axes: Union[int, Sequence[int]] = None):
    """
    Inverse of ``fftshift``.

    .. note::
       Although identical for even-length ``x``, ``fftshift`` and ``ifftshift`` differ by one sample for odd-length ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Union[int, Sequence[int]]
        axes over which to perform the inverse. If ``None``, the function must shift all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type as ``x``.
    """


__all__ = ['fft','ifft','fftn','ifftn','rfft','irfft','rfftn','irfftn','hfft','ihfft','fftfreq','rfftfreq','fftshift','ifftshift']
