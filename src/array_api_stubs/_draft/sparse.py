from __future__ import annotations

from typing import Optional
from ._types import array, device

__all__ = ["from_binsparse"]


def from_binsparse(
    x: object,
    /,
    *,
    descriptor: Optional[dict] = None,
    device: Optional[device] = None,
    copy: Optional[bool] = None,
) -> array:
    """
    Returns a new array containing the data from another (array) object with a ``__binsparse__`` method,
    assuming the format specified in `descriptor` is supported in this library.

    Parameters
    ----------
    x: object
        input (array) object.
    descriptor: Optional[dict]
        If ``descriptor`` is ``None``, the array must be returned in the format in which it is stored or materializable to.
        Otherwise, it must be converted to the format specified by ``descriptor``.

        If ``copy`` is ``False``, no conversion should be performed, and only stored data should be returned.

        If the format specified by ``descriptor`` is unsupported by the library, a ``TypeError`` must be raised.
    device: Optional[device]
        device on which to place the created array. If ``device`` is ``None`` and ``x`` supports binsparse, the output array
        must be on the same device as ``x``. Default: ``None``.

        The v2023.12 standard only mandates that a compliant library should offer a way for ``from_binsparse`` to return an array
        whose underlying memory is accessible to the Python interpreter, when the corresponding ``device`` is provided. If the
        array library does not support such cases at all, the function must raise ``BufferError``. If a copy must be made to
        enable this support but ``copy`` is set to ``False``, the function must raise ``ValueError``.

        Other device kinds will be considered for standardization in a future version of this API standard.
    copy: Optional[bool]
        boolean indicating whether or not to copy the input. If ``True``, the function must always copy. If ``False``, the function must never copy, and raise ``BufferError`` in case a copy is deemed necessary (e.g.  if a cross-device data movement is requested, and it is not possible without a copy). If ``None``, the function must reuse the existing memory buffer if possible and copy otherwise. Default: ``None``.


    Returns
    -------
    out: array
        an array containing the data in `arrays` with a format specified by `descriptor`.

        .. admonition:: Note
           :class: note

           The returned array may be either a copy or a view. See :ref:`data-interchange` for details.

    Raises
    ------
    BufferError
        The ``__binsparse__``, ``__binsparse_descriptor__``, ``__dlpack__`` or ``__dlpack_device__``
        methods on the input array or constituent arrays may raise ``BufferError`` when the data
        cannot be exported as a binsparse-compatible array. (e.g., incompatible dtype, strides, or
        device). It may also raise other errors when export fails for other reasons (e.g., not
        enough memory available to materialize the data). ``from_dlpack`` must propagate such
        exceptions.
    AttributeError
        If the ``__binsparse__`` and ``__binsparse_descriptor__`` methods are not present
        on the input array. This may happen for libraries that are never able
        to export their data with binsparse.
    ValueError
        If data exchange is possible via an explicit copy but ``copy`` is set to ``False``.
    TypeError
        If ``descriptor`` is ``None``, the data received from the source library is not guaranteed to
        be in a format that the target array library supports. In this case, a ``TypeError`` must be raised.
        Additionally, if ``descriptor`` is not ``None``, it must be passed along to ``__binsparse__``, which
        may raise a ``TypeError`` if the conversion is unsupported by the source library, which
        ``from_binsparse`` must propagate.
    """
