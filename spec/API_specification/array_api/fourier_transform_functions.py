from ._types import Tuple, Union, Sequence, array, Optional, Literal

def fft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform.


    .. note::
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy: ``ifft(fft(x)) == x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)``.
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def ifft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)``
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def fftn(x: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform.


    .. note::
       Applying the n-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy: ``ifftn(fftn(x)) == x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If

        - ``s`` is larger than the length of the input array, each axis ``i`` of the input array must be zero-padded.
        - ``s`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``.

        if not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes (dimension) over which to compute the Fourier transform. If set to ``None``, the last ``len(s)`` axes are used, or all axes if ``s`` is set to ``-1``. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)``.
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determine by :ref:`type-promotion`.
    """


def ifftn(x: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional inverse discrete Fourier transform.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If

        - ``s`` is larger than the length of the input array, each axis ``i`` of the input array must be zero-padded.
        - ``s`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``.

        if not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the inverse Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)``
        - ``'forward'``: no normalization.

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
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy: ``irfft(rfft(x), n=x.shape[axis]) == x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **input**. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)``.
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def irfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional inverse of ``rfft``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    n: int
        length of the transformed axis of the **output**. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n//2+1``.

        if not provided, the length of the transformed axis of the output must equal the length ``2 * (m - 1)`` where ``m`` is the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the inverse Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)``
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a real floating-point data type determined by :ref:`type-promotion`. The length along the transformed axis is ``n`` (if given) or ``2 * (m - 1)``.
    """


def rfftn(x: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform for real-valued input.


    .. note::
       Applying the n-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy: ``irfftn(rfftn(x), n=x.shape[axis]) == x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If

        - ``s`` is larger than the length of the input array, each axis ``i`` of the input array must be zero-padded.
        - ``s`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``.

        if not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)``.
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def irfftn(x: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the n-dimensional inverse of ``rfftn``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the **output**. If

        - ``s`` is larger than the length of the input array, each axis ``i`` of the input array must be zero-padded.
        - ``s`` is less than the length of the input array, each axis ``i`` of the input array must be trimmed to the length ``s[i]``. Except for the last axis is trimmed to ``2 * (m - 1)``, where `m` is the length of the input along the axis.

        if not provided, the length of the transformed axes of the output must equal the length of the input along the axes specified by ``axes``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the inverse Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)``
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes (dimension) indicated by ``axes``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`. The length along the last transformed axis is ``s[-1]`` (if given) or ``2 * (m - 1)``, and all other axes ``s[i]``.
    """


def hfft(x: array, /, *, n: Optional[int] = None, axis: int = -1, norm: Literal['backward', 'ortho', 'forward'] = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)``.
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
        input array. Should have a floating-point data type.
    n: int
        length of the transformed axis of the output. If

        - ``n`` is larger than the length of the input array, the input array must be zero-padded.
        - ``n`` is less than the length of the input array, the input array must be trimmed to length ``n``.

        if not provided, the length of the transformed axis of the output must equal the length of the input along the axis specified by ``axis``. Default: ``None``.
    axis: int
        axis (dimension) over which to compute the Fourier transform. If set to ``-1``, the function must compute the Fourier transform over the last axis (dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)``
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) indicated by ``axis``. The returned array must have a complex floating-point data type determined by :ref:`type-promotion`.
    """


def fftfreq(n: int, /, *, d: float = 1.0):
    """
    Returns the discrete Fourier transform sample frequencies. For a Fourier transform of length ``n`` and length unit of ``d`` the frequencies are described as:


    .. code-block::

      f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n) if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n) if n is odd

    Parameters
    ----------
    n: int
        window length.
    d: float
        sample spacing between individual samples of the Fourier transform input. Default: ``1.0``.

    Returns
    -------
    out: array
        an array of length ``n`` containing the sample frequencies.
    """


def rfftfreq(n: int, /, *, d: float = 1.0):
    """
    Returns the discrete Fourier transform sample frequencies. For a Fourier transform of length ``n`` and length unit of ``d`` the frequencies are described as:


    .. code-block::

      f = [0, 1, ..., n/2-1, -n/2, ..., -1] / (d*n) if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n) if n is odd

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
        an array of length ``n`` containing the sample frequencies.
    """


def fftshift(x: array, /, *, axes: Union[int, Sequence[int], Tuple[int, ...]] = None):
    """
    Reorders n-dimensional FTT data to have negative frequency terms first. In this way, the zero-frequency component shifts to the center of the spectrum. Note that ``out[0]`` is the Nyquist component only if the length of the input is even.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Union[int, Sequence[int], Tuple[int, ...]]
        axes over which to shift. If not specified, it shifts all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array.
    """


def ifftshift(x: array, /, *, axes: Union[int, Sequence[int], Tuple[int, ...]] = None):
    """
    Inverse of ``fftshift``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Union[int, Sequence[int], Tuple[int, ...]]
        axes over which to calculate. If not specified, it shifts all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array.
    """


__all__ = ['fft','ifft','fftn','ifftn','rfft','irfft','rfftn','irfftn','hfft','ihfft','fftfreq','rfftfreq','fftshift','ifftshift']
