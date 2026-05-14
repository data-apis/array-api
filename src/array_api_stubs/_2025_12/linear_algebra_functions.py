__all__ = ["matmul", "matrix_transpose", "tensordot", "vecdot"]


from ._types import Tuple, Union, Sequence, array


def matmul(x1: array, x2: array, /) -> array:
    """
    Computes the matrix product.

    Parameters
    ----------
    x1: array
        first input array. **Should** have a numeric data type. **Must** have at least one dimension.

        -   If ``x1`` is a one-dimensional array having shape ``(M,)`` and ``x2`` has more than one dimension, ``x1`` **must** be promoted to a two-dimensional array by prepending ``1`` to its dimensions (i.e., **must** have shape ``(1, M)``). After matrix multiplication, the prepended dimensions in the returned array **must** be removed.
        -   If ``x1`` has more than one dimension (including after vector-to-matrix promotion), ``shape(x1)[:-2]`` **must** be compatible with ``shape(x2)[:-2]`` (after vector-to-matrix promotion) (see :ref:`broadcasting`).
        -   If ``x1`` has shape ``(..., M, K)``, the innermost two dimensions form matrices on which to perform matrix multiplication.

    x2: array
        second input array. **Should** have a numeric data type. **Must** have at least one dimension.

        -   If ``x2`` is one-dimensional array having shape ``(N,)`` and ``x1`` has more than one dimension, ``x2`` **must** be promoted to a two-dimensional array by appending ``1`` to its dimensions (i.e., **must** have shape ``(N, 1)``). After matrix multiplication, the appended dimensions in the returned array **must** be removed.
        -   If ``x2`` has more than one dimension (including after vector-to-matrix promotion), ``shape(x2)[:-2]`` **must** be compatible with ``shape(x1)[:-2]`` (after vector-to-matrix promotion) (see :ref:`broadcasting`).
        -   If ``x2`` has shape ``(..., K, N)``, the innermost two dimensions form matrices on which to perform matrix multiplication.

    Returns
    -------
    out: array
        output array.

        -   If both ``x1`` and ``x2`` are one-dimensional arrays having shape ``(N,)``, the returned array **must** be a zero-dimensional array and **must** contain the inner product as its only element.
        -   If ``x1`` is a two-dimensional array having shape ``(M, K)`` and ``x2`` is a two-dimensional array having shape ``(K, N)``, the returned array **must** be a two-dimensional array and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ and having shape ``(M, N)``.
        -   If ``x1`` is a one-dimensional array having shape ``(K,)`` and ``x2`` is an array having shape ``(..., K, N)``, the returned array **must** be an array having shape ``(..., N)`` (i.e., prepended dimensions during vector-to-matrix promotion **must** be removed) and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_.
        -   If ``x1`` is an array having shape ``(..., M, K)`` and ``x2`` is a one-dimensional array having shape ``(K,)``, the returned array **must** be an array having shape ``(..., M)`` (i.e., appended dimensions during vector-to-matrix promotion **must** be removed) and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_.
        -   If ``x1`` is a two-dimensional array having shape ``(M, K)`` and ``x2`` is an array having shape ``(..., K, N)``, the returned array **must** be an array having shape ``(..., M, N)`` and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for each stacked matrix.
        -   If ``x1`` is an array having shape ``(..., M, K)`` and ``x2`` is a two-dimensional array having shape ``(K, N)``, the returned array **must** be an array having shape ``(..., M, N)`` and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for each stacked matrix.
        -   If either ``x1`` or ``x2`` has more than two dimensions, the returned array **must** be an array having a shape determined by :ref:`broadcasting` ``shape(x1)[:-2]`` against ``shape(x2)[:-2]`` and **must** contain the `conventional matrix product <https://en.wikipedia.org/wiki/Matrix_multiplication>`_ for each stacked matrix.

        The returned array **must** have a data type determined by :ref:`type-promotion`.

    Raises
    ------
    Exception
        an exception **should** be raised in the following circumstances:

        -   if either ``x1`` or ``x2`` is a zero-dimensional array.
        -   if ``x1`` is a one-dimensional array having shape ``(K,)``, ``x2`` is a one-dimensional array having shape ``(L,)``, and ``K != L``.
        -   if ``x1`` is a one-dimensional array having shape ``(K,)``, ``x2`` is an array having shape ``(..., L, N)``, and ``K != L``.
        -   if ``x1`` is an array having shape ``(..., M, K)``, ``x2`` is a one-dimensional array having shape ``(L,)``, and ``K != L``.
        -   if ``x1`` is an array having shape ``(..., M, K)``, ``x2`` is an array having shape ``(..., L, N)``, and ``K != L``.

    Notes
    -----

    -   The ``matmul`` function **must** implement the same semantics as the built-in ``@`` operator (see `PEP 465 <https://www.python.org/dev/peps/pep-0465>`_).

    -   If either ``x1`` or ``x2`` has a complex floating-point data type, the function **must not** complex-conjugate or transpose either argument. If conjugation and/or transposition is desired, a user can explicitly perform these operations prior to computing the matrix product.

    .. versionchanged:: 2022.12
       Added complex data type support.
    """


def matrix_transpose(x: array, /) -> array:
    """
    Transposes a matrix (or a stack of matrices) ``x``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices.

    Returns
    -------
    out: array
        an array containing the transpose for each matrix. The returned array **must** have shape ``(..., N, M)``. The returned array **must** have the same data type as ``x``.
    """


def tensordot(
    x1: array,
    x2: array,
    /,
    *,
    axes: Union[int, Tuple[Sequence[int], Sequence[int]]] = 2,
) -> array:
    """
    Returns a tensor contraction of ``x1`` and ``x2`` over specific axes.

    Parameters
    ----------
    x1: array
        first input array. **Should** have a numeric data type.
    x2: array
        second input array. **Should** have a numeric data type. Corresponding contracted axes of ``x1`` and ``x2`` **must** be equal.

    axes: Union[int, Tuple[Sequence[int], Sequence[int]]]
        number of axes to contract or explicit sequences of axis indices for ``x1`` and ``x2``, respectively.

        If ``axes`` is an ``int`` equal to ``N``, then contraction **must** be performed over the last ``N`` axes of ``x1`` and the first ``N`` axes of ``x2`` in order. The size of each corresponding axis **must** match. An integer ``axes`` value **must** be nonnegative.

        -   If ``N`` equals ``0``, the result **must** be the tensor (outer) product.
        -   If ``N`` equals ``1``, the result **must** be the tensor dot product.
        -   If ``N`` equals ``2``, the result **must** be the tensor double contraction (default).

        If ``axes`` is a tuple of two sequences ``(x1_axes, x2_axes)``, the first sequence **must** apply to ``x1`` and the second sequence **must** apply to ``x2``. Both sequences **must** have the same length. Each axis ``x1_axes[i]`` for ``x1`` **must** have the same size as the respective axis ``x2_axes[i]`` for ``x2``. Each index referred to in a sequence **must** be unique. A valid axis **must** be an integer on the interval ``[-S, S)``, where ``S`` is the number of axes in respective array. Hence, if ``x1`` has ``N`` axes, a valid ``x1`` axes **must** be an integer on the interval ``[-N, N)``. If ``x2`` has ``M`` axes, a valid ``x2`` axes **must** be an integer on the interval ``[-M, M)``. If an axis is specified as a negative integer, the function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). If provided an invalid axis, the function **must** raise an exception.


    Returns
    -------
    out: array
        an array containing the tensor contraction. The returned array **must** have a shape which consists of the non-contracted axes of the first array ``x1``, followed by the non-contracted axes of the second array ``x2``. The returned array **must** have a data type determined by :ref:`type-promotion`.

    Notes
    -----

    -   The ``tensordot`` function corresponds to the generalized matrix product.
    -   Contracted axes **must** not be broadcasted.
    -   If either ``x1`` or ``x2`` has a complex floating-point data type, the function **must not** complex-conjugate or transpose either argument. If conjugation and/or transposition is desired, a user can explicitly perform these operations prior to computing the generalized matrix product.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Allow negative axes.
    """


def vecdot(x1: array, x2: array, /, *, axis: int = -1) -> array:
    r"""
    Computes the (vector) dot product of two arrays.

    Let :math:`\mathbf{a}` be a vector in ``x1`` and :math:`\mathbf{b}` be a corresponding vector in ``x2``. The dot product is defined as

    .. math::
       \mathbf{a} \cdot \mathbf{b} = \sum_{i=0}^{n-1} \overline{a_i}b_i

    over the axis specified by ``axis`` and where :math:`n` is the axis size and :math:`\overline{a_i}` denotes the complex conjugate if :math:`a_i` is complex and the identity if :math:`a_i` is real-valued.

    Parameters
    ----------
    x1: array
        first input array. **Should** have a floating-point data type.
    x2: array
        second input array. **Must** be compatible with ``x1`` for all non-contracted axes (see :ref:`broadcasting`). The size of the axis over which to compute the dot product **must** be the same size as the respective axis in ``x1``. **Should** have a floating-point data type.
    axis: int
        axis of ``x1`` and ``x2`` containing the vectors for which to compute the dot product. **Should** be an integer on the interval ``[-N, -1]``, where ``N`` is ``min(x1.ndim, x2.ndim)``. The function **must** determine the axis along which to perform the operation by counting backward from the last axis (where ``-1`` refers to the last axis). By default, the function **must** compute the dot product over the last axis. Default: ``-1``.

    Returns
    -------
    out: array
        if ``x1`` and ``x2`` are both one-dimensional arrays, a zero-dimensional containing the dot product; otherwise, a non-zero-dimensional array containing the dot products and having ``N-1`` axes, where ``N`` is number of axes in the shape determined according to :ref:`broadcasting` along the non-contracted axes. The returned array **must** have a data type determined by :ref:`type-promotion`.

    Raises
    ------
    Exception
        an exception **should** be raised in the following circumstances:

        -   if the size of the axis over which to compute the dot product is not the same (before broadcasting) for both ``x1`` and ``x2``.

    Notes
    -----

    -   The contracted axis **must** not be broadcasted.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Restricted ``axis`` to only negative integers.
    """
