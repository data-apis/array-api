__all__ = [
    "__array_namespace_info__",
    "capabilities",
    "default_device",
    "default_dtypes",
    "devices",
    "dtypes",
]

from ._types import (
    Optional,
    Union,
    Tuple,
    List,
    device,
    dtype,
    DefaultDataTypes,
    DataTypes,
    Capabilities,
    Info,
)


def __array_namespace_info__() -> Info:
    """
    Returns a namespace with Array API namespace inspection utilities.

    See :ref:`inspection` for a list of inspection APIs.

    Returns
    -------
    out: Info
        An object containing Array API namespace inspection utilities.

    Notes
    -----

    The returned object may be either a namespace or a class, so long as an Array API user can access inspection utilities as follows:

    ::

      info = xp.__array_namespace_info__()
      info.capabilities()
      info.devices()
      info.dtypes()
      info.default_dtypes()
      # ...

    .. versionadded: 2023.12
    """


def capabilities() -> Capabilities:
    """
    Returns a dictionary of array library capabilities.

    The dictionary must contain the following keys:

    -   `"boolean indexing"`: boolean indicating whether an array library supports boolean indexing. If a conforming implementation fully supports boolean indexing in compliance with this specification (see :ref:`indexing`), the corresponding dictionary value must be ``True``; otherwise, the value must be ``False``.
    -   `"data-dependent shapes"`: boolean indicating whether an array library supports data-dependent output shapes. If a conforming implementation fully supports all APIs included in this specification (excluding boolean indexing) which have data-dependent output shapes, as explicitly demarcated throughout the specification, the corresponding dictionary value must be ``True``; otherwise, the value must be ``False``.

    Returns
    -------
    out: Capabilities
        a dictionary of array library capabilities.

    Notes
    -----

    .. versionadded: 2023.12
    """


def default_device() -> device:
    """
    Returns the default device.

    Returns
    -------
    out: device
        an object corresponding to the default device.

    Notes
    -----

    .. versionadded: 2023.12
    """


def default_dtypes(
    *,
    device: Optional[device] = None,
) -> DefaultDataTypes:
    """
    Returns a dictionary containing default data types.

    The dictionary must have the following keys:

    -   `"real floating"`: default real floating-point data type.
    -   `"complex floating"`: default complex floating-point data type.
    -   `"integral"`: default integral data type.
    -   `"indexing"`: default array index data type.

    Dictionary values must be the corresponding data type object.

    Parameters
    ----------
    device: Optional[device]
        device for which to return default data types. If ``device`` is ``None``, the returned data types must be the default data types for the current device; otherwise, the returned data types must be default data types specific to the specified device. Default: ``None``.

        .. note::
           Some array libraries have the concept of a device context manager, allowing library consumers to manage the current device context. When ``device`` is ``None``, libraries supporting a device context should return the default data types for the current device. For libraries without a context manager or supporting only a single device, those libraries should return the default data types for the default device.

    Returns
    -------
    out: DefaultDataTypes
        a dictionary containing the default data type for respective data type kinds.

    Notes
    -----

    .. versionadded: 2023.12
    """


def dtypes(
    *,
    device: Optional[device] = None,
    kind: Optional[Union[str, Tuple[str, ...]]] = None,
) -> DataTypes:
    """
    Returns a dictionary of supported *Array API* data types.

    .. note::
       While specification-conforming array libraries may support additional data types which are not present in this specification, data types which are not present in this specification should not be included in the returned dictionary.

    .. note::
       Specification-conforming array libraries must only return supported data types having expected properties as described in :ref:`data-types`. For example, if a library decides to alias ``float32`` as ``float64``, that library must not include ``float64`` in the dictionary of supported data types.

    Parameters
    ----------
    kind: Optional[Union[str, Tuple[str, ...]]]
        data type kind.

        -   If ``kind`` is ``None``, the function must return a dictionary containing all supported Array API data types.

        -   If ``kind`` is a string, the function must return a dictionary containing the data types belonging to the specified data type kind. The following data type kinds must be supported:

            -   ``'bool'``: boolean data types (e.g., ``bool``).
            -   ``'signed integer'``: signed integer data types (e.g., ``int8``, ``int16``, ``int32``, ``int64``).
            -   ``'unsigned integer'``: unsigned integer data types (e.g., ``uint8``, ``uint16``, ``uint32``, ``uint64``).
            -   ``'integral'``: integer data types. Shorthand for ``('signed integer', 'unsigned integer')``.
            -   ``'real floating'``: real-valued floating-point data types (e.g., ``float32``, ``float64``).
            -   ``'complex floating'``: complex floating-point data types (e.g., ``complex64``, ``complex128``).
            -   ``'numeric'``: numeric data types. Shorthand for ``('integral', 'real floating', 'complex floating')``.

        -   If ``kind`` is a tuple, the tuple specifies a union of data type kinds, and the function must return a dictionary containing the data types belonging to at least one of the specified data type kinds.

        Default: ``None``.
    device: Optional[device]
        device for which to return supported data types. If ``device`` is ``None``, the returned data types must be the supported data types for the current device; otherwise, the returned data types must be supported data types specific to the specified device. Default: ``None``.

        .. note::
           Some array libraries have the concept of a device context manager, allowing library consumers to manage the current device context. When ``device`` is ``None``, libraries supporting a device context should return the supported data types for the current device. For libraries without a context manager or supporting only a single device, those libraries should return the supported data types for the default device.

    Returns
    -------
    out: DataTypes
        a dictionary containing supported data types.

        .. note::
           Dictionary keys must only consist of canonical names as defined in :ref:`data-types`.

    Notes
    -----

    .. versionadded: 2023.12
    """


def devices() -> List[device]:
    """
    Returns a list of supported devices which are available at runtime.

    Returns
    -------
    out: List[device]
        a list of supported devices.

    Notes
    -----

    Each device object (see :ref:`device-support`) in the list of returned devices must be an object which can be provided as a valid keyword-argument to array creation functions.

    Notes
    -----

    .. versionadded: 2023.12
    """
