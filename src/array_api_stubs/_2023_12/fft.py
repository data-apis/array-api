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
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (number of elements, axis, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    n: Optional[int]
        number of elements over which to compute the transform along the axis (dimension) specified by ``axis``. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``M``.

        -   If ``n`` is greater than ``M``, the axis specified by ``axis`` must be zero-padded to size ``n``.
        -   If ``n`` is less than ``M``, the axis specified by ``axis`` must be trimmed to size ``n``.
        -   If ``n`` equals ``M``, all elements along the axis specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have the same data type as ``x`` and must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the input array have a complex floating-point data type and required that the output array have the same data type as the input array.
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
       Applying the one-dimensional inverse discrete Fourier transform to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``ifft(fft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (number of elements, axis, and normalization mode).

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    n: Optional[int]
        number of elements over which to compute the transform along the axis (dimension) specified by ``axis``. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``M``.

        -   If ``n`` is greater than ``M``, the axis specified by ``axis`` must be zero-padded to size ``n``.
        -   If ``n`` is less than ``M``, the axis specified by ``axis`` must be trimmed to size ``n``.
        -   If ``n`` equals ``M``, all elements along the axis specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have the same data type as ``x`` and must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the input array have a complex floating-point data type and required that the output array have the same data type as the input array.
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
        input array. Should have a complex floating-point data type.
    s: Optional[Sequence[int]]
        number of elements over which to compute the transform along the axes (dimensions) specified by ``axes``. Let ``i`` be the index of the ``n``-th axis specified by ``axes`` (i.e., ``i = axes[n]``) and ``M[i]`` be the size of the input array along axis ``i``. When ``s`` is ``None``, the function must set ``s`` equal to a sequence of integers such that ``s[i]`` equals ``M[i]`` for all ``i``.

        -   If ``s[i]`` is greater than ``M[i]``, axis ``i`` must be zero-padded to size ``s[i]``.
        -   If ``s[i]`` is less than ``M[i]``, axis ``i`` must be trimmed to size ``s[i]``.
        -   If ``s[i]`` equals ``M[i]`` or ``-1``, all elements along axis ``i`` must be used when computing the transform.

        If ``s`` is not ``None``, ``axes`` must not be ``None``. Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the transform. A valid axis in ``axes`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an axis is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension).

        If ``s`` is provided, the corresponding ``axes`` to be transformed must also be provided. If ``axes`` is ``None``, the function must compute the transform over all axes. Default: ``None``.

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.
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
        an array transformed along the axes (dimensions) specified by ``axes``. The returned array must have the same data type as ``x`` and must have the same shape as ``x``, except for the axes specified by ``axes`` which must have size ``s[i]``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the input array have a complex floating-point data type and required that the output array have the same data type as the input array.
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
        input array. Should have a complex floating-point data type.
    s: Optional[Sequence[int]]
        number of elements over which to compute the transform along the axes (dimensions) specified by ``axes``. Let ``i`` be the index of the ``n``-th axis specified by ``axes`` (i.e., ``i = axes[n]``) and ``M[i]`` be the size of the input array along axis ``i``. When ``s`` is ``None``, the function must set ``s`` equal to a sequence of integers such that ``s[i]`` equals ``M[i]`` for all ``i``.

        -   If ``s[i]`` is greater than ``M[i]``, axis ``i`` must be zero-padded to size ``s[i]``.
        -   If ``s[i]`` is less than ``M[i]``, axis ``i`` must be trimmed to size ``s[i]``.
        -   If ``s[i]`` equals ``M[i]`` or ``-1``, all elements along axis ``i`` must be used when computing the transform.

        If ``s`` is not ``None``, ``axes`` must not be ``None``. Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the transform. A valid axis in ``axes`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an axis is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension).

        If ``s`` is provided, the corresponding ``axes`` to be transformed must also be provided. If ``axes`` is ``None``, the function must compute the transform over all axes. Default: ``None``.

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.
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
        an array transformed along the axes (dimensions) specified by ``axes``. The returned array must have the same data type as ``x`` and must have the same shape as ``x``, except for the axes specified by ``axes`` which must have size ``s[i]``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the input array have a complex floating-point data type and required that the output array have the same data type as the input array.
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
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axis and normalization mode) and consistent values for the number of elements over which to compute the transforms.

    Parameters
    ----------
    x: array
        input array. Must have a real-valued floating-point data type.
    n: Optional[int]
        number of elements over which to compute the transform along the axis (dimension) specified by ``axis``. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``M``.

        -   If ``n`` is greater than ``M``, the axis specified by ``axis`` must be zero-padded to size ``n``.
        -   If ``n`` is less than ``M``, the axis specified by ``axis`` must be trimmed to size ``n``.
        -   If ``n`` equals ``M``, all elements along the axis specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). The returned array must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n//2 + 1``.

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
       Applying the one-dimensional inverse discrete Fourier transform for real-valued input to the output of this function must return the original (i.e., non-transformed) input array within numerical accuracy (i.e., ``irfft(rfft(x)) == x``), provided that the transform and inverse transform are performed with the same arguments (axis and normalization mode) and consistent values for the number of elements over which to compute the transforms.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.
    n: Optional[int]
        number of elements along the transformed axis (dimension) specified by ``axis`` in the **output array**. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``2*(M-1)``.

        -   If ``n//2+1`` is greater than ``M``, the axis of the input array specified by ``axis`` must be zero-padded to size ``n//2+1``.
        -   If ``n//2+1`` is less than ``M``, the axis of the input array specified by ``axis`` must be trimmed to size ``n//2+1``.
        -   If ``n//2+1`` equals ``M``, all elements along the axis of the input array specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The returned array must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n``.

    Notes
    -----

    -   In order to return an array having an odd number of elements along the transformed axis, the function must be provided an odd integer for ``n``.

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the output array have a real-valued floating-point data type having the same precision as the input array.
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
        number of elements over which to compute the transform along axes (dimensions) specified by ``axes``. Let ``i`` be the index of the ``n``-th axis specified by ``axes`` (i.e., ``i = axes[n]``) and ``M[i]`` be the size of the input array along axis ``i``. When ``s`` is ``None``, the function must set ``s`` equal to a sequence of integers such that ``s[i]`` equals ``M[i]`` for all ``i``.

        -   If ``s[i]`` is greater than ``M[i]``, axis ``i`` must be zero-padded to size ``s[i]``.
        -   If ``s[i]`` is less than ``M[i]``, axis ``i`` must be trimmed to size ``s[i]``.
        -   If ``s[i]`` equals ``M[i]`` or ``-1``, all elements along axis ``i`` must be used when computing the transform.

        If ``s`` is not ``None``, ``axes`` must not be ``None``. Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the transform. A valid axis in ``axes`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an axis is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension).

        If ``s`` is provided, the corresponding ``axes`` to be transformed must also be provided. If ``axes`` is ``None``, the function must compute the transform over all axes. Default: ``None``.

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.
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
        an array transformed along the axes (dimension) specified by ``axes``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). The returned array must have the same shape as ``x``, except for the last transformed axis which must have size ``s[-1]//2 + 1`` and the remaining transformed axes which must have size ``s[i]``.

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
        input array. Should have a complex floating-point data type.
    s: Optional[Sequence[int]]
        number of elements along the transformed axes (dimensions) specified by ``axes`` in the **output array**. Let ``i`` be the index of the ``n``-th axis specified by ``axes`` (i.e., ``i = axes[n]``) and ``M[i]`` be the size of the input array along axis ``i``. When ``s`` is ``None``, the function must set ``s`` equal to a sequence of integers such that ``s[i]`` equals ``M[i]`` for all ``i``, except for the last transformed axis in which ``s[i]`` equals ``2*(M[i]-1)``. For each ``i``, let ``n`` equal ``s[i]``, except for the last transformed axis in which ``n`` equals ``s[i]//2+1``.

        -   If ``n`` is greater than ``M[i]``, axis ``i`` of the input array must be zero-padded to size ``n``.
        -   If ``n`` is less than ``M[i]``, axis ``i`` of the input array must be trimmed to size ``n``.
        -   If ``n`` equals ``M[i]`` or ``-1``, all elements along axis ``i`` of the input array must be used when computing the transform.

        If ``s`` is not ``None``, ``axes`` must not be ``None``. Default: ``None``.
    axes: Optional[Sequence[int]]
        axes (dimensions) over which to compute the transform. A valid axis in ``axes`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an axis is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension).

        If ``s`` is provided, the corresponding ``axes`` to be transformed must also be provided. If ``axes`` is ``None``, the function must compute the transform over all axes. Default: ``None``.

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.
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
        an array transformed along the axes (dimension) specified by ``axes``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The returned array must have the same shape as ``x``, except for the transformed axes which must have size ``s[i]``.

    Notes
    -----

    -   In order to return an array having an odd number of elements along the last transformed axis, the function must be provided an odd integer for ``s[-1]``.

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the output array have a real-valued floating-point data type having the same precision as the input array.
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
        input array. Should have a complex floating-point data type.
    n: Optional[int]
        number of elements along the transformed axis (dimension) specified by ``axis`` in the **output array**. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``2*(M-1)``.

        -   If ``n//2+1`` is greater than ``M``, the axis of the input array specified by ``axis`` must be zero-padded to length ``n//2+1``.
        -   If ``n//2+1`` is less than ``M``, the axis of the input array specified by ``axis`` must be trimmed to size ``n//2+1``.
        -   If ``n//2+1`` equals ``M``, all elements along the axis of the input array specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: no normalization.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: normalize by ``1/n``.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type). The returned array must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n``.

    Notes
    -----

    .. versionadded:: 2022.12

    .. versionchanged:: 2023.12
       Required the input array to have a complex floating-point data type and required that the output array have a real-valued data type having the same precision as the input array.
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
    n: Optional[int]
        number of elements over which to compute the transform along the axis (dimension) specified by ``axis``. Let ``M`` be the size of the input array along the axis specified by ``axis``. When ``n`` is ``None``, the function must set ``n`` equal to ``M``.

        -   If ``n`` is greater than ``M``, the axis specified by ``axis`` must be zero-padded to size ``n``.
        -   If ``n`` is less than ``M``, the axis specified by ``axis`` must be trimmed to size ``n``.
        -   If ``n`` equals ``M``, all elements along the axis specified by ``axis`` must be used when computing the transform.

        Default: ``None``.
    axis: int
        axis (dimension) of the input array over which to compute the transform. A valid ``axis`` must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis`` is specified as a negative integer, the function must determine the axis along which to compute the transform by counting backward from the last dimension (where ``-1`` refers to the last dimension). Default: ``-1``.
    norm: Literal['backward', 'ortho', 'forward']
        normalization mode. Should be one of the following modes:

        - ``'backward'``: normalize by ``1/n``.
        - ``'ortho'``: normalize by ``1/sqrt(n)`` (i.e., make the FFT orthonormal).
        - ``'forward'``: no normalization.

        Default: ``'backward'``.

    Returns
    -------
    out: array
        an array transformed along the axis (dimension) specified by ``axis``. The returned array must have a complex floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``float64``, then the returned array must have a ``complex128`` data type). The returned array must have the same shape as ``x``, except for the axis specified by ``axis`` which must have size ``n//2 + 1``.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def fftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Computes the discrete Fourier transform sample frequencies.

    For a Fourier transform of length ``n`` and length unit of ``d``, the frequencies are described as:

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

    .. versionchanged:: 2023.12
       Required the output array have the default real-valued floating-point data type.
    """


def rfftfreq(n: int, /, *, d: float = 1.0, device: Optional[device] = None) -> array:
    """
    Computes the discrete Fourier transform sample frequencies (for ``rfft`` and ``irfft``).

    For a Fourier transform of length ``n`` and length unit of ``d``, the frequencies are described as:

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

    .. versionchanged:: 2023.12
       Required the output array have the default real-valued floating-point data type.
    """


def fftshift(x: array, /, *, axes: Optional[Union[int, Sequence[int]]] = None) -> array:
    """
    Shifts the zero-frequency component to the center of the spectrum.

    This function swaps half-spaces for all axes (dimensions) specified by ``axes``.

    .. note::
       ``out[0]`` is the Nyquist component only if the length of the input is even.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axes: Optional[Union[int, Sequence[int]]]
        axes over which to shift. If ``None``, the function must shift all axes. Default: ``None``.

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type and shape as ``x``.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def ifftshift(
    x: array, /, *, axes: Optional[Union[int, Sequence[int]]] = None
) -> array:
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

        If ``axes`` contains two or more entries which resolve to the same axis (i.e., resolved axes are not unique), the behavior is unspecified and thus implementation-defined.

    Returns
    -------
    out: array
        the shifted array. The returned array must have the same data type and shape as ``x``.

    Notes
    -----

    .. versionadded:: 2022.12
    """
