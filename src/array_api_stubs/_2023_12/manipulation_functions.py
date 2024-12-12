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


def broadcast_arrays(*arrays: array) -> List[array]:
    """
    Broadcasts one or more arrays against one another.

    Parameters
    ----------
    arrays: array
        an arbitrary number of to-be broadcasted arrays.

    Returns
    -------
    out: List[array]
        a list of broadcasted arrays. Each array must have the same shape. Each array must have the same dtype as its corresponding input array.
    """


def broadcast_to(x: array, /, shape: Tuple[int, ...]) -> array:
    """
    Broadcasts an array to a specified shape.

    Parameters
    ----------
    x: array
        array to broadcast.
    shape: Tuple[int, ...]
        array shape. Must be compatible with ``x`` (see :ref:`broadcasting`). If the array is incompatible with the specified shape, the function should raise an exception.

    Returns
    -------
    out: array
        an array having a specified shape. Must have the same data type as ``x``.
    """


def concat(
    arrays: Union[Tuple[array, ...], List[array]], /, *, axis: Optional[int] = 0
) -> array:
    """
    Joins a sequence of arrays along an existing axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. The arrays must have the same shape, except in the dimension specified by ``axis``.
    axis: Optional[int]
        axis along which the arrays will be joined. If ``axis`` is ``None``, arrays must be flattened before concatenation. If ``axis`` is negative, the function must determine the axis along which to join by counting from the last dimension. Default: ``0``.

    Returns
    -------
    out: array
        an output array containing the concatenated values. If the input arrays have different data types, normal :ref:`type-promotion` must apply. If the input arrays have the same data type, the output array must have the same data type as the input arrays.

        .. note::
           This specification leaves type promotion between data type families (i.e., ``intxx`` and ``floatxx``) unspecified.
    """


def expand_dims(x: array, /, *, axis: int = 0) -> array:
    """
    Expands the shape of an array by inserting a new axis (dimension) of size one at the position specified by ``axis``.

    Parameters
    ----------
    x: array
        input array.
    axis: int
        axis position (zero-based). If ``x`` has rank (i.e, number of dimensions) ``N``, a valid ``axis`` must reside on the closed-interval ``[-N-1, N]``. If provided a negative ``axis``, the axis position at which to insert a singleton dimension must be computed as ``N + axis + 1``. Hence, if provided ``-1``, the resolved axis position must be ``N`` (i.e., a singleton dimension must be appended to the input array ``x``). If provided ``-N-1``, the resolved axis position must be ``0`` (i.e., a singleton dimension must be prepended to the input array ``x``).

    Returns
    -------
    out: array
        an expanded output array having the same data type as ``x``.

    Raises
    ------
    IndexError
        If provided an invalid ``axis`` position, an ``IndexError`` should be raised.
    """


def flip(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> array:
    """
    Reverses the order of elements in an array along the given axis. The shape of the array must be preserved.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis (or axes) along which to flip. If ``axis`` is ``None``, the function must flip all input array axes. If ``axis`` is negative, the function must count from the last dimension. If provided more than one axis, the function must flip only the specified axes. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type and shape as ``x`` and whose elements, relative to ``x``, are reordered.
    """


def moveaxis(
    x: array,
    source: Union[int, Tuple[int, ...]],
    destination: Union[int, Tuple[int, ...]],
    /,
) -> array:
    """
    Moves array axes (dimensions) to new positions, while leaving other axes in their original positions.

    Parameters
    ----------
    x: array
        input array.
    source: Union[int, Tuple[int, ...]]
        Axes to move. Provided axes must be unique. If ``x`` has rank (i.e, number of dimensions) ``N``, a valid axis must reside on the half-open interval ``[-N, N)``.
    destination: Union[int, Tuple[int, ...]]
        indices defining the desired positions for each respective ``source`` axis index. Provided indices must be unique. If ``x`` has rank (i.e, number of dimensions) ``N``, a valid axis must reside on the half-open interval ``[-N, N)``.

    Returns
    -------
    out: array
        an array containing reordered axes. The returned array must have the same data type as ``x``.

    Notes
    -----

    .. versionadded:: 2023.12
    """


def permute_dims(x: array, /, axes: Tuple[int, ...]) -> array:
    """
    Permutes the axes (dimensions) of an array ``x``.

    Parameters
    ----------
    x: array
        input array.
    axes: Tuple[int, ...]
        tuple containing a permutation of ``(0, 1, ..., N-1)`` where ``N`` is the number of axes (dimensions) of ``x``.

    Returns
    -------
    out: array
        an array containing the axes permutation. The returned array must have the same data type as ``x``.
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

        When ``repeats`` is an array, the shape of the output array for this function depends on the data values in the ``repeats`` array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing the values in ``repeats``. Accordingly, such libraries may choose to omit support for ``repeats`` arrays; however, conforming implementations must support providing a literal ``int``. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array containing elements to repeat.
    repeats: Union[int, array]
        the number of repetitions for each element.

        If ``axis`` is ``None``, let ``N = prod(x.shape)`` and

        -   if ``repeats`` is an array, ``repeats`` must be broadcast compatible with the shape ``(N,)`` (i.e., be a one-dimensional array having shape ``(1,)`` or ``(N,)``).
        -   if ``repeats`` is an integer, ``repeats`` must be broadcasted to the shape `(N,)`.

        If ``axis`` is not ``None``, let ``M = x.shape[axis]`` and

        -   if ``repeats`` is an array, ``repeats`` must be broadcast compatible with the shape ``(M,)`` (i.e., be a one-dimensional array having shape ``(1,)`` or ``(M,)``).
        -   if ``repeats`` is an integer, ``repeats`` must be broadcasted to the shape ``(M,)``.

        If ``repeats`` is an array, the array must have an integer data type.

        .. note::
           For specification-conforming array libraries supporting hardware acceleration, providing an array for ``repeats`` may cause device synchronization due to an unknown output shape. For those array libraries where synchronization concerns are applicable, conforming array libraries are advised to include a warning in their documentation regarding potential performance degradation when ``repeats`` is an array.

    axis: Optional[int]
        the axis (dimension) along which to repeat elements. If ``axis`` is `None`, the function must flatten the input array ``x`` and then repeat elements of the flattened input array and return the result as a one-dimensional output array. A flattened input array must be flattened in row-major, C-style order. Default: ``None``.

    Returns
    -------
    out: array
        an output array containing repeated elements. The returned array must have the same data type as ``x``. If ``axis`` is ``None``, the returned array must be a one-dimensional array; otherwise, the returned array must have the same shape as ``x``, except for the axis (dimension) along which elements were repeated.

    Notes
    -----

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
        a new shape compatible with the original shape. One shape dimension is allowed to be ``-1``. When a shape dimension is ``-1``, the corresponding output array shape dimension must be inferred from the length of the array and the remaining dimensions.
    copy: Optional[bool]
        whether or not to copy the input array. If ``True``, the function must always copy. If ``False``, the function must never copy. If ``None``, the function must avoid copying, if possible, and may copy otherwise. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type and elements as ``x``.

    Raises
    ------
    ValueError
        If ``copy=False`` and a copy would be necessary, a ``ValueError``
        should be raised.
    """


def roll(
    x: array,
    /,
    shift: Union[int, Tuple[int, ...]],
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
) -> array:
    """
    Rolls array elements along a specified axis. Array elements that roll beyond the last position are re-introduced at the first position. Array elements that roll beyond the first position are re-introduced at the last position.

    Parameters
    ----------
    x: array
        input array.
    shift: Union[int, Tuple[int, ...]]
        number of places by which the elements are shifted. If ``shift`` is a tuple, then ``axis`` must be a tuple of the same size, and each of the given axes must be shifted by the corresponding element in ``shift``. If ``shift`` is an ``int`` and ``axis`` a tuple, then the same ``shift`` must be used for all specified axes. If a shift is positive, then array elements must be shifted positively (toward larger indices) along the dimension of ``axis``. If a shift is negative, then array elements must be shifted negatively (toward smaller indices) along the dimension of ``axis``.
    axis: Optional[Union[int, Tuple[int, ...]]]
        axis (or axes) along which elements to shift. If ``axis`` is ``None``, the array must be flattened, shifted, and then restored to its original shape. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type as ``x`` and whose elements, relative to ``x``, are shifted.
    """


def squeeze(x: array, /, axis: Union[int, Tuple[int, ...]]) -> array:
    """
    Removes singleton dimensions (axes) from ``x``.

    Parameters
    ----------
    x: array
        input array.
    axis: Union[int, Tuple[int, ...]]
        axis (or axes) to squeeze.

    Returns
    -------
    out: array
        an output array having the same data type and elements as ``x``.

    Raises
    ------
    ValueError
        If a specified axis has a size greater than one (i.e., it is not a
        singleton dimension), a ``ValueError`` should be raised.
    """


def stack(arrays: Union[Tuple[array, ...], List[array]], /, *, axis: int = 0) -> array:
    """
    Joins a sequence of arrays along a new axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. Each array must have the same shape.
    axis: int
        axis along which the arrays will be joined. Providing an ``axis`` specifies the index of the new axis in the dimensions of the result. For example, if ``axis`` is ``0``, the new axis will be the first dimension and the output array will have shape ``(N, A, B, C)``; if ``axis`` is ``1``, the new axis will be the second dimension and the output array will have shape ``(A, N, B, C)``; and, if ``axis`` is ``-1``, the new axis will be the last dimension and the output array will have shape ``(A, B, C, N)``. A valid ``axis`` must be on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If provided an ``axis`` outside of the required interval, the function must raise an exception. Default: ``0``.

    Returns
    -------
    out: array
        an output array having rank ``N+1``, where ``N`` is the rank (number of dimensions) of ``x``. If the input arrays have different data types, normal :ref:`type-promotion` must apply. If the input arrays have the same data type, the output array must have the same data type as the input arrays.

        .. note::
           This specification leaves type promotion between data type families (i.e., ``intxx`` and ``floatxx``) unspecified.
    """


def tile(x: array, repetitions: Tuple[int, ...], /) -> array:
    """
    Constructs an array by tiling an input array.

    Parameters
    ----------
    x: array
        input array.
    repetitions: Tuple[int, ...]
        number of repetitions along each axis (dimension).

        Let ``N = len(x.shape)`` and ``M = len(repetitions)``.

        If ``N > M``, the function must prepend ones until all axes (dimensions) are specified (e.g., if ``x`` has shape ``(8,6,4,2)`` and ``repetitions`` is the tuple ``(3,3)``, then ``repetitions`` must be treated as ``(1,1,3,3)``).

        If ``N < M``, the function must prepend singleton axes (dimensions) to ``x`` until ``x`` has as many axes (dimensions) as ``repetitions`` specifies (e.g., if ``x`` has shape ``(4,2)`` and ``repetitions`` is the tuple ``(3,3,3,3)``, then ``x`` must be treated as if it has shape ``(1,1,4,2)``).

    Returns
    -------
    out: array
        a tiled output array. The returned array must have the same data type as ``x`` and must have a rank (i.e., number of dimensions) equal to ``max(N, M)``. If ``S`` is the shape of the tiled array after prepending singleton dimensions (if necessary) and ``r`` is the tuple of repetitions after prepending ones (if necessary), then the number of elements along each axis (dimension) must satisfy ``S[i]*r[i]``, where ``i`` refers to the ``i`` th axis (dimension).

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
        axis along which the array will be split. A valid ``axis`` must be on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If provided an ``axis`` outside of the required interval, the function must raise an exception. Default: ``0``.

    Returns
    -------
    out: Tuple[array, ...]
        tuple of slices along the given dimension. All the arrays have the same shape.

    Notes
    -----

    .. versionadded:: 2023.12
    """
