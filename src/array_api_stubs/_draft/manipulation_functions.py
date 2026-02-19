__all__ = [
    "broadcast_arrays",
    "broadcast_to",
    "concat",
    "expand_dims",
    "flip",
    "moveaxis",
    "permute_dims",
    "repeat",
    "reshape",
    "roll",
    "squeeze",
    "stack",
    "tile",
    "unstack",
]


from ._types import List, Optional, Tuple, Union, array


def broadcast_arrays(*arrays: array) -> Tuple[array, ...]:
    """
    Broadcasts one or more arrays against one another.

    Parameters
    ----------
    arrays: array
        an arbitrary number of to-be broadcasted arrays.

    Returns
    -------
    out: Tuple[array, ...]
        tuple of broadcasted arrays. Each array **must** have the same shape. Each array **must** have the same dtype as its corresponding input array.
    """


def broadcast_to(x: array, /, shape: Tuple[int, ...]) -> array:
    """
    Broadcasts an array to a specified shape.

    Parameters
    ----------
    x: array
        array to broadcast. **Must** be capable of being broadcast to the specified ``shape`` (see :ref:`broadcasting`). If the array is incompatible with the specified shape, the function **must** raise an exception.
    shape: Tuple[int, ...]
        array shape.

    Returns
    -------
    out: array
        an array having the specified shape. **Must** have the same data type as ``x``.

    .. versionchanged:: 2024.12
       Clarified broadcast behavior.
    """


def concat(
    arrays: Union[Tuple[array, ...], List[array]], /, *, axis: Optional[int] = 0
) -> array:
    """
    Joins a sequence of arrays along an existing axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. The arrays **must** have the same shape, except in the dimension specified by ``axis``.
    axis: Optional[int]
        axis along which to join the arrays. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in each array. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. If ``axis`` is ``None``, arrays **must** be flattened before concatenation. Default: ``0``.

    Returns
    -------
    out: array
        an output array containing the concatenated values. If the input arrays have different data types, normal :ref:`type-promotion` **must** apply. If the input arrays have the same data type, the output array **must** have the same data type as the input arrays.

        .. note::
           This specification leaves type promotion between data type families (i.e., ``intxx`` and ``floatxx``) unspecified and thus implementation-defined.
    """


def expand_dims(x: array, /, axis: Union[int, Tuple[int, ...]]) -> array:
    """
    Expands the shape of an array by inserting a new axis of size one at the position (or positions) specified by ``axis``.

    Parameters
    ----------
    x: array
        input array.
    axis: Union[int, Tuple[int, ...]]
        axis position(s) (zero-based). If ``axis`` is an integer, ``axis`` **must** be equivalent to the tuple ``(axis,)``. If ``axis`` is a tuple,

        -   a valid axis position **must** reside on the half-open interval ``[-M, M)``, where ``M = N + len(axis)`` and ``N`` is the number of dimensions in ``x``.
        -   if the i-th entry is a negative integer, the axis position of the inserted singleton dimension in the output array **must** be computed as ``M + axis[i]``.
        -   each entry of ``axis`` must resolve to a unique positive axis position.
        -   for each entry of ``axis``, the corresponding dimension in the expanded output array **must** be a singleton dimension.
        -   for the remaining dimensions of the expanded output array, the output array dimensions **must** correspond to the dimensions of ``x`` in order.
        -   if provided an invalid axis position, the function **must** raise an exception.

    Returns
    -------
    out: array
        an expanded output array. **Must** have the same data type as ``x``. If ``axis`` is an integer, the output array must have ``N + 1`` dimensions. If ``axis`` is a tuple, the output array must have ``N + len(axis)`` dimensions.

    Raises
    ------
    IndexError
        If provided an invalid ``axis``, an ``IndexError`` **should** be raised.

    Notes
    -----

    -   Calling this function with a tuple of axis positions **must** be semantically equivalent to calling this function repeatedly with a single axis position only when the following three conditions are met:

        -   each entry of the tuple is normalized to positive axis positions according to the number of dimensions in the expanded output array.
        -   the normalized positive axis positions are sorted in ascending order.
        -   the normalized positive axis positions are unique.
    """


def flip(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> array:
    """
    Reverses the order of elements in an array along the given axis.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis (or axes) along which to reverse elements. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. If ``axis`` is ``None``, the function **must** flip all input array axes. If provided more than one axis, the function **must** flip only the specified axes. Default: ``None``.

    Returns
    -------
    out: array
        an output array. The returned array **must** have the same data type and shape as ``x``. The returned array must have the same elements as ``x``, but which are reordered relative to ``x``.
    """


def moveaxis(
    x: array,
    source: Union[int, Tuple[int, ...]],
    destination: Union[int, Tuple[int, ...]],
    /,
) -> array:
    """
    Moves array axes to new positions, while leaving other axes in their original positions.

    Parameters
    ----------
    x: array
        input array.
    source: Union[int, Tuple[int, ...]]
        axis (or axes) to move. Provided source axes **must** be unique. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.
    destination: Union[int, Tuple[int, ...]]
        axis (or axes) defining the desired position(s) for each respective ``source`` axis index. Provided destination axes **must** be unique. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.

    Returns
    -------
    out: array
        an array containing reordered axes. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    .. versionadded:: 2023.12
    """


def permute_dims(x: array, /, axes: Tuple[int, ...]) -> array:
    """
    Permutes the axes of an array ``x``.

    Parameters
    ----------
    x: array
        input array.
    axes: Tuple[int, ...]
        tuple containing a permutation of axes. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the respective axis index by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.

    Returns
    -------
    out: array
        an array containing the axes permutation. The returned array **must** have the same data type as ``x``.
    """


def repeat(
    x: array,
    repeats: Union[int, array],
    /,
    *,
    axis: Optional[int] = None,
) -> array:
    """
    Repeats each element of an array a specified number of times on a per-element basis.

    .. admonition:: Data-dependent output shape
        :class: important

        When ``repeats`` is an array, the shape of the output array for this function depends on the data values in the ``repeats`` array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) can find this function difficult to implement without knowing the values in ``repeats``. Accordingly, such libraries **may** choose to omit support for ``repeats`` arrays; however, conforming implementations **must** support providing a literal ``int``. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array containing elements to repeat.
    repeats: Union[int, array]
        the number of repetitions for each element.

        If ``axis`` is ``None``, let ``M = prod(x.shape)`` and

        -   if ``repeats`` is an array, ``repeats`` **must** be broadcast compatible with the shape ``(M,)`` (i.e., be a one-dimensional array having shape ``(1,)`` or ``(M,)``).
        -   if ``repeats`` is an integer, ``repeats`` **must** be broadcasted to the shape `(M,)`.

        If ``axis`` is not ``None``, let ``S = x.shape[axis]`` and

        -   if ``repeats`` is an array, ``repeats`` **must** be broadcast compatible with the shape ``(S,)`` (i.e., be a one-dimensional array having shape ``(1,)`` or ``(S,)``).
        -   if ``repeats`` is an integer, ``repeats`` **must** be broadcasted to the shape ``(S,)``.

        If ``repeats`` is an array, the array **must** have an integer data type.

    axis: Optional[int]
        the axis along which to repeat elements. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. If ``axis`` is `None`, the function **must** flatten the input array ``x`` and then repeat elements of the flattened input array and return the result as a one-dimensional output array. A flattened input array **must** be flattened in row-major, C-style order. Default: ``None``.

    Returns
    -------
    out: array
        an output array containing repeated elements. The returned array **must** have the same data type as ``x``. If ``axis`` is ``None``, the returned array **must** be a one-dimensional array; otherwise, the returned array **must** have the same shape as ``x``, except for the axis along which elements were repeated.

    Notes
    -----

    -   For specification-conforming array libraries supporting hardware acceleration, providing an array for ``repeats`` can cause device synchronization due to an unknown output shape. For those array libraries where synchronization concerns are applicable, conforming array libraries **should** include a warning in their documentation regarding potential performance degradation when ``repeats`` is an array.

    .. versionadded:: 2023.12
    """


def reshape(
    x: array, /, shape: Tuple[int, ...], *, copy: Optional[bool] = None
) -> array:
    """
    Reshapes an array without changing its data.

    Parameters
    ----------
    x: array
        input array to reshape.
    shape: Tuple[int, ...]
        a new shape compatible with the original shape. Only one shape dimension **must** be allowed to be ``-1``. When a shape dimension is ``-1``, the corresponding output array shape dimension **must** be inferred from the length of the array and the remaining dimensions.
    copy: Optional[bool]
        whether or not to copy the input array. If ``True``, the function **must** always copy (see :ref:`copy-keyword-argument`). If ``False``, the function **must** never copy. If ``None``, the function **must** avoid copying, if possible, and **may** copy otherwise. Default: ``None``.

    Returns
    -------
    out: array
        an output array. The returned array **must** have the same data type and the same elements as ``x``.

    Raises
    ------
    ValueError
        If ``copy=False`` and a copy would be necessary, a ``ValueError`` **should** be raised.
    """


def roll(
    x: array,
    /,
    shift: Union[int, Tuple[int, ...]],
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
) -> array:
    """
    Rolls array elements along a specified axis.

    Array elements that roll beyond the last position are re-introduced at the first position.

    Array elements that roll beyond the first position are re-introduced at the last position.

    Parameters
    ----------
    x: array
        input array.
    shift: Union[int, Tuple[int, ...]]
        number of places by which the elements are shifted. If ``shift`` is a tuple, then ``axis`` **must** be a tuple of the same size, and each of the given axes **must** be shifted by the corresponding element in ``shift``. If ``shift`` is an ``int`` and ``axis`` a tuple, then the same ``shift`` **must** be used for all specified axes. If a shift is positive, then array elements **must** be shifted positively (toward larger indices) along the dimension of ``axis``. If a shift is negative, then array elements **must** be shifted negatively (toward smaller indices) along the dimension of ``axis``.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis (or axes) along which elements to shift. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. If ``axis`` is ``None``, the array **must** be flattened, shifted, and then restored to its original shape. Default: ``None``.

    Returns
    -------
    out: array
        an output array. The returned array **must** have the same data type as ``x``. The returned array **must** have the same elements as ``x``, but which are shifted relative to ``x``.
    """


def squeeze(x: array, /, axis: Union[int, Tuple[int, ...]]) -> array:
    """
    Removes singleton axes from ``x``.

    Parameters
    ----------
    x: array
        input array.
    axis: Union[int, Tuple[int, ...]]
        axis (or axes) to squeeze. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.

    Returns
    -------
    out: array
        an output array. The returned array **must** have the same data type and the same elements as ``x``.

    Raises
    ------
    ValueError
        If a specified axis has a size greater than one (i.e., it is not a singleton axis), a ``ValueError`` **should** be raised.
    """


def stack(arrays: Union[Tuple[array, ...], List[array]], /, *, axis: int = 0) -> array:
    """
    Joins a sequence of arrays along a new axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. Each array **must** have the same shape.
    axis: int
        axis along which to join the arrays. Providing an ``axis`` specifies the index of the new axis in the shape of the result. For example, if ``axis`` is ``0``, the new axis **must** be the first dimension and the output array **must** have shape ``(N, A, B, C)``; if ``axis`` is ``1``, the new axis will be the second dimension and the output array will have shape ``(A, N, B, C)``; and, if ``axis`` is ``-1``, the new axis will be the last dimension and the output array will have shape ``(A, B, C, N)``. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``0``.

    Returns
    -------
    out: array
        an output array. The returned array **must** have ``N+1`` axes, where ``N`` is the number of axes in ``x``. If the input arrays have different data types, normal :ref:`type-promotion` **must** apply. If the input arrays have the same data type, the output array **must** have the same data type as the input arrays.

    Notes
    -----

    -   This specification leaves type promotion between data type families (i.e., ``intxx`` and ``floatxx``) unspecified and thus implementation-defined.
    """


def tile(x: array, repetitions: Tuple[int, ...], /) -> array:
    """
    Constructs an array by tiling an input array.

    Parameters
    ----------
    x: array
        input array.
    repetitions: Tuple[int, ...]
        number of repetitions along each axis.

        Let ``N = len(x.shape)`` and ``M = len(repetitions)``.

        If ``N > M``, the function **must** prepend ones until all axes are specified (e.g., if ``x`` has shape ``(8,6,4,2)`` and ``repetitions`` is the tuple ``(3,3)``, then ``repetitions`` **must** be treated as ``(1,1,3,3)``).

        If ``N < M``, the function **must** prepend singleton axes to ``x`` until ``x`` has as many axes as ``repetitions`` specifies (e.g., if ``x`` has shape ``(4,2)`` and ``repetitions`` is the tuple ``(3,3,3,3)``, then ``x`` **must** be treated as if it has shape ``(1,1,4,2)``).

    Returns
    -------
    out: array
        a tiled output array. The returned array **must** have the same data type as ``x`` and **must** have a number of axes equal to ``max(N, M)``. If ``S`` is the shape of the tiled array after prepending singleton dimensions (if necessary) and ``r`` is the tuple of repetitions after prepending ones (if necessary), then the number of elements along each axis **must** satisfy ``S[i]*r[i]``, where ``i`` refers to the ``i`` th axis.

    Notes
    -----

    .. versionadded:: 2023.12
    """


def unstack(x: array, /, *, axis: int = 0) -> Tuple[array, ...]:
    """
    Splits an array into a sequence of arrays along the given axis.

    Parameters
    ----------
    x: array
        input array.
    axis: int
        axis along which to split an array. A valid axis **must** be an integer on the interval ``[-N, N)``, where ``N`` is the number of axes in ``x``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception. Default: ``0``.

    Returns
    -------
    out: Tuple[array, ...]
        tuple of slices along the given dimension. Each returned array **must** have the same shape.

    Notes
    -----

    .. versionadded:: 2023.12
    """
