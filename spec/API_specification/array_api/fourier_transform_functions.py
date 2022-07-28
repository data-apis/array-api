from ._types import Tuple, Union, Sequence, array, Optional


def fft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform. The expected behavior includes a round-trip transform using the inverse function, ``ifft(fft(a)) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to the length ``n`` before computing the Fourier transform. Otherwise, the length of the input along the axis given by the ``axis`` keyword. Default: ``None``.
    axis: int
        axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: No normalization.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``.
        - ``'forward'``: Normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a complex-valued array transformed along the axis indicated by the ``axis`` keyword. The length along the transformed axis is ``n//2+1``.


    **Raises**

    - If ``axis`` is not a valid axis of ``a``.
    """


def ifft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform. The expected behavior includes a round-trip transform using the inverse function, ``ifft(fft(a)) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to the length ``n`` before computing the inverse Fourier transform. Otherwise, the length of the input along the axis given by the ``axis`` keyword. Default: ``None``.
    axis: int
        axis used to compute the inverse Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: Normalize by ``1/n``.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``
        - ``'forward'``: No normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a complex-valued array transformed along the axis indicated by the ``axis`` keyword. The length along the transformed axis is ``n//2+1``.


    **Raises**

    -   If ``axis`` is not a valid axis of ``a``.
    """


def fftn(a: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: str = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform. The expected behavior includes a round-trip transform using the inverse function, ``ifftn(fftn(a)) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If given, each axis ``i`` will be either zero-padded or trimmed to the length ``s[i]`` before computing the Fourier transform. Otherwise, the shape of the input along the axes given by the ``axes`` keyword. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: No normalization.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``.
        - ``'forward'``: Normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes indicated by the ``axes`` keyword.


    **Raises**

    - If ``s`` and ``axes`` have different lengths.
    - If ``axes`` contains any invalid axis of ``a``.
    """


def ifftn(a: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: str = 'backward') -> array:
    """
    Computes the n-dimensional inverse discrete Fourier transform. The expected behavior includes a round-trip transform using the inverse function, ``ifftn(fftn(a)) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If given, each axis will be either zero-padded or trimmed to the length ``s[i]`` before computing the inverse Fourier transform. Otherwise, the length of the input along the axis given by the ``axes`` keyword. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the inverse Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: Normalize by ``1/n``.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``
        - ``'forward'``: No normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axes indicated by the `axes` keyword.


    **Raises**

    - If ``s`` and ``axes`` have different lengths.
    - If ``axes`` contains any invalid axis of ``a``.
    """


def rfft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform for real-valued input. The expected behavior includes a round-trip transform using the inverse function, ``irfft(rfft(a), n=a.shape[axis]) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the **input**. If given, the input will be either zero-padded or trimmed to this length before computing the real Fourier transform. Otherwise, the length of the input along the axis specified by the ``axis`` keyword is used. Default: ``None``.
    axis: int
        axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: No normalization.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``.
        - ``'forward'``: Normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a complex-valued array transformed along the axis indicated by the ``axis`` keyword. The length along the transformed axis is ``n//2+1``.


    **Raises**

    - If ``axis`` is not a valid axis of ``a``.
    """


def irfft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional inverse of ``rfft``. The expected behavior includes a round-trip transform using the inverse function, ``irfft(rfft(a), n=a.shape[axis]) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the **output**. If given, the input will be either zero-padded or trimmed to ``n//2+1`` before computing the inverse of ``rfft``. Otherwise, it will default to ``2 * (m - 1)`` where ``m`` is the length of the input along the axis given by the ``axis`` keyword. Default: ``None``.
    axis: int
        axis used to compute the real Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: Normalize by ``1/n``.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``
        - ``'forward'``: No normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a real-valued array transformed along the axis indicated by the ``axis`` keyword. The length along the transformed axis is ``n`` (if given) or ``2 * (m - 1)``.


    **Raises**

    -   If ``axis`` is not a valid axis of ``a``.
    """


def rfftn(a: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: str = 'backward') -> array:
    """
    Computes the n-dimensional discrete Fourier transform for real-valued input. The expected behavior includes a round-trip transform using the inverse function, ``irfftn(rfftn(a), s=a.shape) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the output. If given, each axis ``i`` will be either zero-padded or trimmed to the length ``s[i]`` before computing the real Fourier transform. Otherwise, the shape of the input along the axes given by the `axes` keyword. The last element ``s[-1]`` is for computing ``rfft(a[axes[-1]], n=s[-1])`` whereas other elements for ``fft(a[axes[i]], n=s[i])``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the Fourier transform. If not specified, the last ``len(s)`` axes are used, or all axes if ``s`` is not specified either. Default: ``None``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: No normalization.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``.
        - ``'forward'``: Normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a complex-valued array transformed along the axes indicated by the ``axes`` keyword. The length along the last transformed axis is ``s[-1]//2+1`` and along other axes ``s[i]``.


    **Raises**

    - If ``s`` and ``axes`` have different lengths.
    - If ``axes`` contains any invalid axis of ``a``.
    """


def irfftn(a: array, /, *, s: Union[Sequence[int], Tuple[int, ...]] = None, axes: Union[Sequence[int], Tuple[int, ...]] = None, norm: str = 'backward') -> array:
    """
    Computes the n-dimensional inverse of ``rfftn``. The expected behavior includes a round-trip transform using the inverse function, ``irfftn(rfftn(a), s=a.shape) == a`` within numerical accuracy.

    Parameters
    ----------
    a: array
        input array
    s: Union[Sequence[int], Tuple[int, ...]]
        size of each transformed axis of the **output**. If given, the last axis will be either zero-padded or trimmed to ``s[-1]//2+1``, whereas all other axes ``i`` are either zero-padded or trimmed to the length ``s[i]``, before computing the inverse of ``rfftn``. Otherwise, the last axis is either zero-padded or trimmed to ``2 * (m - 1)``, where `m` is the length of the input along the axis, and all other axes use the input shape. The last element ``s[-1]`` is for computing ``irfft(a[axes[-1]], n=s[-1])`` whereas other elements for ``ifft(a[axes[i]], n=s[i])``. Default: ``None``.
    axes: Union[Sequence[int], Tuple[int, ...]]
        axes over which to compute the inverse Fourier transform. If it is not specified, the last ``len(s)`` axes are used or all axes if ``s`` is also not specified. Default: ``None``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: Normalize by ``1/n``.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``
        - ``'forward'``: No normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a real-valued array transformed along the axes indicated by the ``axes`` keyword. The length along the last transformed axis is ``s[-1]`` (if given) or ``2 * (m - 1)``, and all other axes ``s[i]``.


    **Raises**

    - If ``s`` and ``axes`` have different lengths.
    - If ``axes`` contains any invalid axis of ``a``.
    """


def hfft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to this length before computing the Hermitian Fourier transform. Otherwise, it will default to ``2 * (m - 1)`` where ``m`` is the length of the input along the axis given by the ``axis`` keyword. Default: ``None``.
    axis: int
        axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: No normalization.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``.
        - ``'forward'``: Normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a transformed array.


    **Raises**

    - If ``axis`` is not a valid axis of ``a``.
    """


def ihfft(a: array, /, *, n: Optional[int] = None, axis: int = -1, norm: str = 'backward') -> array:
    """
    Computes the one-dimensional inverse discrete Fourier transform of a signal with Hermitian symmetry.

    Parameters
    ----------
    a: array
        input array
    n: int
        length of the transformed axis of the output. If given, the input will be either zero-padded or trimmed to this length before computing the Hermitian Fourier transform. Otherwise, it will default to ``2 * (m - 1)`` where ``m`` is the length of the input along the axis given by the ``axis`` keyword. Default: ``None``.
    axis: int
        axis used to compute the Fourier transform. If it is not specified, the last axis is used. Default: ``-1``.
    norm: str
        specify the normalization mode. Should be one of the following modes:

        - ``'backward'``: Normalize by ``1/n``.
        - ``'ortho'``: Normalize by ``1/sqrt(n)``
        - ``'forward'``: No normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        a transformed array.


    **Raises**

    -   If ``axis`` is not a valid axis of ``a``.
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
        input array.
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
        input array.
    axes: Union[int, Sequence[int], Tuple[int, ...]]
        axes over which to calculate. If not specified, it shifts all axes. Default: ``None``.

    Returns
    -------
    out: array
        the shifted array.
    """


__all__ = ['fft','ifft','fftn','ifftn','rfft','irfft','rfftn','irfftn','hfft','ihfft','fftfreq','rfftfreq','fftshift','ifftshift']
