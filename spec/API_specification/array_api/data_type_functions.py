from ._types import Union, array, dtype, finfo_object, iinfo_object

def astype(x: array, dtype: dtype, /, *, copy: bool = True) -> array:
    """
    Copies an array to a specified data type irrespective of :ref:`type-promotion` rules.

    .. note::
       Casting floating-point ``NaN`` and ``infinity`` values to integral data types is not specified and is implementation-dependent.

    .. note::
       When casting a boolean input array to a real-valued data type, a value of ``True`` must cast to a numeric value equal to ``1``, and a value of ``False`` must cast to a numeric value equal to ``0``.

       When casting a real-valued input array to ``bool``, a value of ``0`` must cast to ``False``, and a non-zero value must cast to ``True``.

    Parameters
    ----------
    x: array
        array to cast.
    dtype: dtype
        desired data type.
    copy: bool
        specifies whether to copy an array when the specified ``dtype`` matches the data type of the input array ``x``. If ``True``, a newly allocated array must always be returned. If ``False`` and the specified ``dtype`` matches the data type of the input array, the input array must be returned; otherwise, a newly allocated must be returned. Default: ``True``.

    Returns
    -------
    out: array
        an array having the specified data type. The returned array must have the same shape as ``x``.
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

__all__ = ['astype', 'can_cast', 'finfo', 'iinfo', 'result_type']
