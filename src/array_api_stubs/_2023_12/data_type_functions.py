__all__ = ["astype", "can_cast", "finfo", "iinfo", "isdtype", "result_type"]

from ._types import (
    Union,
    Tuple,
    array,
    dtype,
    finfo_object,
    iinfo_object,
    device,
    Optional,
)


def astype(
    x: array, dtype: dtype, /, *, copy: bool = True, device: Optional[device] = None
) -> array:
    """
    Copies an array to a specified data type irrespective of :ref:`type-promotion` rules.

    .. note::
       Casting floating-point ``NaN`` and ``infinity`` values to integral data types is not specified and is implementation-dependent.

    .. note::
       Casting a complex floating-point array to a real-valued data type should not be permitted.

       Historically, when casting a complex floating-point array to a real-valued data type, libraries such as NumPy have discarded imaginary components such that, for a complex floating-point array ``x``, ``astype(x)`` equals ``astype(real(x))``). This behavior is considered problematic as the choice to discard the imaginary component is arbitrary and introduces more than one way to achieve the same outcome (i.e., for a complex floating-point array ``x``, ``astype(x)`` and ``astype(real(x))`` versus only ``astype(imag(x))``). Instead, in order to avoid ambiguity and to promote clarity, this specification requires that array API consumers explicitly express which component should be cast to a specified real-valued data type.

    .. note::
       When casting a boolean input array to a real-valued data type, a value of ``True`` must cast to a real-valued number equal to ``1``, and a value of ``False`` must cast to a real-valued number equal to ``0``.

       When casting a boolean input array to a complex floating-point data type, a value of ``True`` must cast to a complex number equal to ``1 + 0j``, and a value of ``False`` must cast to a complex number equal to ``0 + 0j``.

    .. note::
       When casting a real-valued input array to ``bool``, a value of ``0`` must cast to ``False``, and a non-zero value must cast to ``True``.

       When casting a complex floating-point array to ``bool``, a value of ``0 + 0j`` must cast to ``False``, and all other values must cast to ``True``.

    Parameters
    ----------
    x: array
        array to cast.
    dtype: dtype
        desired data type.
    copy: bool
        specifies whether to copy an array when the specified ``dtype`` matches the data type of the input array ``x``. If ``True``, a newly allocated array must always be returned. If ``False`` and the specified ``dtype`` matches the data type of the input array, the input array must be returned; otherwise, a newly allocated array must be returned. Default: ``True``.
    device: Optional[device]
        device on which to place the returned array. If ``device`` is ``None``, the output array device must be inferred from ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array having the specified data type. The returned array must have the same shape as ``x``.

    Notes
    -----

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Added device keyword argument support.
    """


def can_cast(from_: Union[dtype, array], to: dtype, /) -> bool:
    """
    Determines if one data type can be cast to another data type according :ref:`type-promotion` rules.

    Parameters
    ----------
    from_: Union[dtype, array]
        input data type or array from which to cast.
    to: dtype
        desired data type.

    Returns
    -------
    out: bool
        ``True`` if the cast can occur according to :ref:`type-promotion` rules; otherwise, ``False``.
    """


def finfo(type: Union[dtype, array], /) -> finfo_object:
    """
    Machine limits for floating-point data types.

    Parameters
    ----------
    type: Union[dtype, array]
        the kind of floating-point data-type about which to get information. If complex, the information is about its component data type.

        .. note::
           Complex floating-point data types are specified to always use the same precision for both its real and imaginary components, so the information should be true for either component.

    Returns
    -------
    out: finfo object
        an object having the following attributes:

        - **bits**: *int*

          number of bits occupied by the real-valued floating-point data type.

        - **eps**: *float*

          difference between 1.0 and the next smallest representable real-valued floating-point number larger than 1.0 according to the IEEE-754 standard.

        - **max**: *float*

          largest representable real-valued number.

        - **min**: *float*

          smallest representable real-valued number.

        - **smallest_normal**: *float*

          smallest positive real-valued floating-point number with full precision.

        - **dtype**: dtype

          real-valued floating-point data type.

          .. versionadded:: 2022.12

    Notes
    -----

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def iinfo(type: Union[dtype, array], /) -> iinfo_object:
    """
    Machine limits for integer data types.

    Parameters
    ----------
    type: Union[dtype, array]
        the kind of integer data-type about which to get information.

    Returns
    -------
    out: iinfo object
        an object having the following attributes:

        - **bits**: *int*

          number of bits occupied by the type.

        - **max**: *int*

          largest representable number.

        - **min**: *int*

          smallest representable number.

        - **dtype**: dtype

          integer data type.

          .. versionadded:: 2022.12
    """


def isdtype(
    dtype: dtype, kind: Union[dtype, str, Tuple[Union[dtype, str], ...]]
) -> bool:
    """
    Returns a boolean indicating whether a provided dtype is of a specified data type "kind".

    Parameters
    ----------
    dtype: dtype
        the input dtype.
    kind: Union[str, dtype, Tuple[Union[str, dtype], ...]]
        data type kind.

        -   If ``kind`` is a dtype, the function must return a boolean indicating whether the input ``dtype`` is equal to the dtype specified by ``kind``.
        -   If ``kind`` is a string, the function must return a boolean indicating whether the input ``dtype`` is of a specified data type kind. The following dtype kinds must be supported:

            -   ``'bool'``: boolean data types (e.g., ``bool``).
            -   ``'signed integer'``: signed integer data types (e.g., ``int8``, ``int16``, ``int32``, ``int64``).
            -   ``'unsigned integer'``: unsigned integer data types (e.g., ``uint8``, ``uint16``, ``uint32``, ``uint64``).
            -   ``'integral'``: integer data types. Shorthand for ``('signed integer', 'unsigned integer')``.
            -   ``'real floating'``: real-valued floating-point data types (e.g., ``float32``, ``float64``).
            -   ``'complex floating'``: complex floating-point data types (e.g., ``complex64``, ``complex128``).
            -   ``'numeric'``: numeric data types. Shorthand for ``('integral', 'real floating', 'complex floating')``.

        -   If ``kind`` is a tuple, the tuple specifies a union of dtypes and/or kinds, and the function must return a boolean indicating whether the input ``dtype`` is either equal to a specified dtype or belongs to at least one specified data type kind.

        .. note::
           A conforming implementation of the array API standard is **not** limited to only including the dtypes described in this specification in the required data type kinds. For example, implementations supporting ``float16`` and ``bfloat16`` can include ``float16`` and ``bfloat16`` in the ``real floating`` data type kind. Similarly, implementations supporting ``int128`` can include ``int128`` in the ``signed integer`` data type kind.

           In short, conforming implementations may extend data type kinds; however, data type kinds must remain consistent (e.g., only integer dtypes may belong to integer data type kinds and only floating-point dtypes may belong to floating-point data type kinds), and extensions must be clearly documented as such in library documentation.

    Returns
    -------
    out: bool
        boolean indicating whether a provided dtype is of a specified data type kind.

    Notes
    -----

    .. versionadded:: 2022.12
    """


def result_type(*arrays_and_dtypes: Union[array, dtype]) -> dtype:
    """
    Returns the dtype that results from applying the type promotion rules (see :ref:`type-promotion`) to the arguments.

    .. note::
       If provided mixed dtypes (e.g., integer and floating-point), the returned dtype will be implementation-specific.

    Parameters
    ----------
    arrays_and_dtypes: Union[array, dtype]
        an arbitrary number of input arrays and/or dtypes.

    Returns
    -------
    out: dtype
        the dtype resulting from an operation involving the input arrays and dtypes.
    """
