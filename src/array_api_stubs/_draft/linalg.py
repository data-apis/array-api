from ._types import Literal, Optional, Tuple, Union, Sequence, array, dtype
from .constants import inf


def cholesky(x: array, /, *, upper: bool = False) -> array:
    r"""
    Returns the lower (upper) Cholesky decomposition of a complex Hermitian or real symmetric positive-definite matrix ``x``.

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers $\mathbb{R}$, and, if ``x`` is complex-valued, let $\mathbb{K}$ be the set of complex numbers $\mathbb{C}$.

    The lower **Cholesky decomposition** of a complex Hermitian or real symmetric positive-definite matrix :math:`x \in\ \mathbb{K}^{n \times n}` is defined as

    .. math::
       x = LL^{H} \qquad \text{L $\in\ \mathbb{K}^{n \times n}$}

    where :math:`L` is a lower triangular matrix and :math:`L^{H}` is the conjugate transpose when :math:`L` is complex-valued and the transpose when :math:`L` is real-valued.

    The upper Cholesky decomposition is defined similarly

    .. math::
       x = UU^{H} \qquad \text{U $\in\ \mathbb{K}^{n \times n}$}

    where :math:`U` is an upper triangular matrix.

    When ``x`` is a stack of matrices, the function must compute the Cholesky decomposition for each matrix in the stack.

    .. note::
       Whether an array library explicitly checks whether an input array is Hermitian or a symmetric positive-definite matrix (or a stack of matrices) is implementation-defined.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square complex Hermitian or real symmetric positive-definite matrices. Should have a floating-point data type.
    upper: bool
        If ``True``, the result must be the upper-triangular Cholesky factor :math:`U`. If ``False``, the result must be the lower-triangular Cholesky factor :math:`L`. Default: ``False``.

    Returns
    -------
    out: array
        an array containing the Cholesky factors for each square matrix. If ``upper`` is ``False``, the returned array must contain lower-triangular matrices; otherwise, the returned array must contain upper-triangular matrices. The returned array must have a floating-point data type determined by :ref:`type-promotion` and must have the same shape as ``x``.
    """


def cross(x1: array, x2: array, /, *, axis: int = -1) -> array:
    """
    Returns the cross product of 3-element vectors.

    If ``x1`` and/or ``x2`` are multi-dimensional arrays (i.e., the broadcasted result has a rank greater than ``1``), then the cross-product of each pair of corresponding 3-element vectors is independently computed.

    Parameters
    ----------
    x1: array
        first input array. Must have a numeric data type.
    x2: array
        second input array. Must be compatible with ``x1`` for all non-compute axes (see :ref:`broadcasting`). The size of the axis over which to compute the cross product must be the same size as the respective axis in ``x1``. Must have a numeric data type.

        .. note::
           The compute axis (dimension) must not be broadcasted.

    axis: int
        the axis (dimension) of ``x1`` and ``x2`` containing the vectors for which to compute the cross product. Must be an integer on the interval ``[-N, N)``, where ``N`` is the rank (number of dimensions) of the shape determined according to :ref:`broadcasting`. If specified as a negative integer, the function must determine the axis along which to compute the cross product by counting backward from the last dimension (where ``-1`` refers to the last dimension). By default, the function must compute the cross product over the last axis. Default: ``-1``.

    Returns
    -------
    out: array
        an array containing the cross products. The returned array must have a data type determined by :ref:`type-promotion`.


    **Raises**

    -   if provided an invalid ``axis``.
    -   if the size of the axis over which to compute the cross product is not equal to ``3``.
    -   if the size of the axis over which to compute the cross product is not the same (before broadcasting) for both ``x1`` and ``x2``.
    """


def det(x: array, /) -> array:
    """
    Returns the determinant of a square matrix (or a stack of square matrices) ``x``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

    Returns
    -------
    out: array
        if ``x`` is a two-dimensional array, a zero-dimensional array containing the determinant; otherwise, a non-zero dimensional array containing the determinant for each square matrix. The returned array must have the same data type as ``x``.
    """


def diagonal(x: array, /, *, offset: int = 0) -> array:
    """
    Returns the specified diagonals of a matrix (or a stack of matrices) ``x``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices.
    offset: int
        offset specifying the off-diagonal relative to the main diagonal.

        - ``offset = 0``: the main diagonal.
        - ``offset > 0``: off-diagonal above the main diagonal.
        - ``offset < 0``: off-diagonal below the main diagonal.

        Default: `0`.

    Returns
    -------
    out: array
        an array containing the diagonals and whose shape is determined by removing the last two dimensions and appending a dimension equal to the size of the resulting diagonals. The returned array must have the same data type as ``x``.
    """


def eigh(x: array, /) -> Tuple[array]:
    r"""
    Returns an eigenvalue decomposition of a complex Hermitian or real symmetric matrix (or a stack of matrices) ``x``.

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if ``x`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    The **eigenvalue decomposition** of a complex Hermitian or real symmetric matrix :math:`x \in\ \mathbb{K}^{n \times n}` is defined as

    .. math::
       x = Q \Lambda Q^H

    with :math:`Q \in \mathbb{K}^{n \times n}` and :math:`\Lambda \in \mathbb{R}^n` and where :math:`Q^H` is the conjugate transpose when :math:`Q` is complex and the transpose when :math:`Q` is real-valued and :math:`\Lambda` is a diagonal matrix whose diagonal elements are the corresponding eigenvalues. When ``x`` is real-valued, :math:`Q` is orthogonal, and, when ``x`` is complex, :math:`Q` is unitary.

    .. note::
       The eigenvalues of a complex Hermitian or real symmetric matrix are always real.

    .. warning::
       The eigenvectors of a symmetric matrix are not unique and are not continuous with respect to ``x``. Because eigenvectors are not unique, different hardware and software may compute different eigenvectors.

       Non-uniqueness stems from the fact that multiplying an eigenvector by :math:`-1` when ``x`` is real-valued and by :math:`e^{\phi j}` (:math:`\phi \in \mathbb{R}`) when ``x`` is complex produces another set of valid eigenvectors.

    .. note::
       Whether an array library explicitly checks whether an input array is Hermitian or a symmetric matrix (or a stack of matrices) is implementation-defined.

    .. note::
       The function ``eig`` will be added in a future version of the specification.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

    Returns
    -------
    out: Tuple[array]
        a namedtuple (``eigenvalues``, ``eigenvectors``) whose

        -   first element must have the field name ``eigenvalues`` (corresponding to :math:`\operatorname{diag}\Lambda` above) and must be an array consisting of computed eigenvalues. The array containing the eigenvalues must have shape ``(..., M)`` and must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then ``eigenvalues`` must be ``float64``).
        -   second element have have the field name ``eigenvectors`` (corresponding to :math:`Q` above) and must be an array where the columns of the inner most matrices contain the computed eigenvectors. These matrices must be orthogonal. The array containing the eigenvectors must have shape ``(..., M, M)`` and must have the same data type as ``x``.


    .. note::
       Eigenvalue sort order is left unspecified and is thus implementation-dependent.
    """


def eigvalsh(x: array, /) -> array:
    r"""
    Returns the eigenvalues of a complex Hermitian or real symmetric matrix (or a stack of matrices) ``x``.

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if ``x`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    The **eigenvalues** of a complex Hermitian or real symmetric matrix :math:`x \in\ \mathbb{K}^{n \times n}` are defined as the roots (counted with multiplicity) of the polynomial :math:`p` of degree :math:`n` given by

    .. math::
       p(\lambda) = \operatorname{det}(x - \lambda I_n)

    where :math:`\lambda \in \mathbb{R}` and where :math:`I_n` is the *n*-dimensional identity matrix.

    .. note:;
       The eigenvalues of a complex Hermitian or real symmetric matrix are always real.

    .. note::
       Whether an array library explicitly checks whether an input array is Hermitian or a symmetric matrix (or a stack of matrices) is implementation-defined.

    .. note::
       The function ``eigvals`` will be added in a future version of the specification.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the computed eigenvalues. The returned array must have shape ``(..., M)`` and have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then must have a ``float64`` data type).


    .. note::
       Eigenvalue sort order is left unspecified and is thus implementation-dependent.
    """


def inv(x: array, /) -> array:
    r"""
    Returns the multiplicative inverse of a square matrix (or a stack of square matrices) ``x``.

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if ``x`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    The **inverse matrix** :math:`x^{-1} \in\ \mathbb{K}^{n \times n}` of a square matrix :math:`x \in\ \mathbb{K}^{n \times n}` is defined as

    .. math::
       x^{-1}x = xx^{-1} = I_n

    where :math:`I_n` is the *n*-dimensional identity matrix.

    The inverse matrix exists if and only if ``x`` is invertible. When ``x`` is invertible, the inverse is unique.

    When ``x`` is a stack of matrices, the function must compute the inverse for each matrix in the stack.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the multiplicative inverses. The returned array must have a floating-point data type determined by :ref:`type-promotion` and must have the same shape as ``x``.
    """


def matmul(x1: array, x2: array, /) -> array:
    """Alias for :func:`~array_api.matmul`."""


def matrix_norm(
    x: array,
    /,
    *,
    keepdims: bool = False,
    ord: Optional[Union[int, float, Literal[inf, -inf, "fro", "nuc"]]] = "fro",
) -> array:
    """
    Computes the matrix norm of a matrix (or a stack of matrices) ``x``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices. Should have a floating-point data type.
    keepdims: bool
        If ``True``, the last two axes (dimensions) must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the last two axes (dimensions) must not be included in the result. Default: ``False``.
    ord: Optional[Union[int, float, Literal[inf, -inf, 'fro', 'nuc']]]
        order of the norm. The following mathematical norms must be supported:

        +------------------+---------------------------------+
        | ord              | description                     |
        +==================+=================================+
        | 'fro'            | Frobenius norm                  |
        +------------------+---------------------------------+
        | 'nuc'            | nuclear norm                    |
        +------------------+---------------------------------+
        | 1                | max(sum(abs(x), axis=0))        |
        +------------------+---------------------------------+
        | 2                | largest singular value          |
        +------------------+---------------------------------+
        | inf              | max(sum(abs(x), axis=1))        |
        +------------------+---------------------------------+

        The following non-mathematical "norms" must be supported:

        +------------------+---------------------------------+
        | ord              | description                     |
        +==================+=================================+
        | -1               | min(sum(abs(x), axis=0))        |
        +------------------+---------------------------------+
        | -2               | smallest singular value         |
        +------------------+---------------------------------+
        | -inf             | min(sum(abs(x), axis=1))        |
        +------------------+---------------------------------+

        If ``ord=1``, the norm corresponds to the induced matrix norm where ``p=1`` (i.e., the maximum absolute value column sum).

        If ``ord=2``, the norm corresponds to the induced matrix norm where ``p=inf`` (i.e., the maximum absolute value row sum).

        If ``ord=inf``, the norm corresponds to the induced matrix norm where ``p=2`` (i.e., the largest singular value).

        Default: ``'fro'``.

    Returns
    -------
    out: array
        an array containing the norms for each ``MxN`` matrix. If ``keepdims`` is ``False``, the returned array must have a rank which is two less than the rank of ``x``. If ``x`` has a real-valued data type, the returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. If ``x`` has a complex-valued data type, the returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type).
    """


def matrix_power(x: array, n: int, /) -> array:
    """
    Raises a square matrix (or a stack of square matrices) ``x`` to an integer power ``n``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.
    n: int
        integer exponent.

    Returns
    -------
    out: array
        if ``n`` is equal to zero, an array containing the identity matrix for each square matrix. If ``n`` is less than zero, an array containing the inverse of each square matrix raised to the absolute value of ``n``, provided that each square matrix is invertible. If ``n`` is greater than zero, an array containing the result of raising each square matrix to the power ``n``. The returned array must have the same shape as ``x`` and a floating-point data type determined by :ref:`type-promotion`.
    """


def matrix_rank(x: array, /, *, rtol: Optional[Union[float, array]] = None) -> array:
    """
    Returns the rank (i.e., number of non-zero singular values) of a matrix (or a stack of matrices).

    When ``x`` is a stack of matrices, the function must compute the number of non-zero singular values for each matrix in the stack.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices. Should have a floating-point data type.
    rtol: Optional[Union[float, array]]
        relative tolerance for small singular values. Singular values approximately less than or equal to ``rtol * largest_singular_value`` are set to zero. If a ``float``, the value is equivalent to a zero-dimensional array having a real-valued floating-point data type determined by :ref:`type-promotion` (as applied to ``x``) and must be broadcast against each matrix. If an ``array``, must have a real-valued floating-point data type and must be compatible with ``shape(x)[:-2]`` (see :ref:`broadcasting`). If ``None``, the default value is ``max(M, N) * eps``, where ``eps`` must be the machine epsilon associated with the real-valued floating-point data type determined by :ref:`type-promotion` (as applied to ``x``). Default: ``None``.

    Returns
    -------
    out: array
        an array containing the ranks. The returned array must have the default integer data type and must have shape ``(...)`` (i.e., must have a shape equal to ``shape(x)[:-2]``).
    """


def matrix_transpose(x: array, /) -> array:
    """Alias for :func:`~array_api.matrix_transpose`."""


def outer(x1: array, x2: array, /) -> array:
    """
    Returns the outer product of two vectors ``x1`` and ``x2``.

    Parameters
    ----------
    x1: array
        first one-dimensional input array of size ``N``. Must have a numeric data type.
    x2: array
        second one-dimensional input array of size ``M``. Must have a numeric data type.

    Returns
    -------
    out: array
        a two-dimensional array containing the outer product and whose shape is ``(N, M)``. The returned array must have a data type determined by :ref:`type-promotion`.
    """


def pinv(x: array, /, *, rtol: Optional[Union[float, array]] = None) -> array:
    r"""
    Returns the (Moore-Penrose) pseudo-inverse of a matrix (or a stack of matrices) ``x``.

    The pseudo-inverse of a matrix :math:`A`, denoted :math:`A^{+}`, is defined as the matrix that "solves" the least-squares problem :math:`Ax = b` (i.e., if :math:`\overline{x}` is a solution, then :math:`A^{+}` is the matrix such that :math:`\overline{x} = A^{+}b`).

    While the pseudo-inverse can be defined algebraically, one can understand the pseudo-inverse via singular value decomposition (SVD). Namely, if

    .. math::
       A = U \Sigma V^H

    is a singular decomposition of :math:`A`, then

    .. math::
       A^{+} = U \Sigma^{+} V^H

    where :math:`U` and :math:`V^H` are orthogonal matrices, :math:`\Sigma` is a diagonal matrix consisting of :math:`A`'s singular values, and :math:`\Sigma^{+}` is then a diagonal matrix consisting of the reciprocals of :math:`A`'s singular values, leaving zeros in place. During numerical computation, only elements larger than a small tolerance are considered nonzero, and all others replaced by zeros.

    When ``x`` is a stack of matrices, the function must compute the pseudo-inverse for each matrix in the stack.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices. Should have a floating-point data type.
    rtol: Optional[Union[float, array]]
        relative tolerance for small singular values. Singular values approximately less than or equal to ``rtol * largest_singular_value`` are set to zero. If a ``float``, the value is equivalent to a zero-dimensional array having a real-valued floating-point data type determined by :ref:`type-promotion` (as applied to ``x``) and must be broadcast against each matrix. If an ``array``, must have a real-valued floating-point data type and must be compatible with ``shape(x)[:-2]`` (see :ref:`broadcasting`). If ``None``, the default value is ``max(M, N) * eps``, where ``eps`` must be the machine epsilon associated with the real-valued floating-point data type determined by :ref:`type-promotion` (as applied to ``x``). Default: ``None``.

    Returns
    -------
    out: array
        an array containing the pseudo-inverse(s). The returned array must have a floating-point data type determined by :ref:`type-promotion` and must have shape ``(..., N, M)`` (i.e., must have the same shape as ``x``, except the innermost two dimensions must be transposed).
    """


def qr(
    x: array, /, *, mode: Literal["reduced", "complete"] = "reduced"
) -> Tuple[array, array]:
    r"""
    Returns the QR decomposition of a full column rank matrix (or a stack of matrices).

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if ``x`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    The **complete QR decomposition** of a matrix :math:`x \in\ \mathbb{K}^{n \times n}` is defined as

    .. math::
       x = QR

    where :math:`Q \in\ \mathbb{K}^{m \times m}` is orthogonal when ``x`` is real-valued and unitary when ``x`` is complex-valued and where :math:`R \in\ \mathbb{K}^{m \times n}` is an upper triangular matrix with real diagonal (even when ``x`` is complex-valued).

    When :math:`m \gt n` (tall matrix), as :math:`R` is upper triangular, the last :math:`m - n` rows are zero. In this case, the last :math:`m - n` columns of :math:`Q` can be dropped to form the **reduced QR decomposition**.

    .. math::
       x = QR

    where :math:`Q \in\ \mathbb{K}^{m \times n}` and :math:`R \in\ \mathbb{K}^{n \times n}`.

    The reduced QR decomposition equals with the complete QR decomposition when :math:`n \qeq m` (wide matrix).

    When ``x`` is a stack of matrices, the function must compute the QR decomposition for each matrix in the stack.

    .. note::
       Whether an array library explicitly checks whether an input array is a full column rank matrix (or a stack of full column rank matrices) is implementation-defined.

    .. warning::
       The elements in the diagonal of :math:`R` are not necessarily positive. Accordingly, the returned QR decomposition is only unique up to the sign of the diagonal of :math:`R`, and different libraries or inputs on different devices may produce different valid decompositions.

    .. warning::
       The QR decomposition is only well-defined if the first ``k = min(m,n)`` columns of every matrix in ``x`` are linearly independent.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices of rank ``N``. Should have a floating-point data type.
    mode: Literal['reduced', 'complete']
        decomposition mode. Should be one of the following modes:

        -   ``'reduced'``: compute only the leading ``K`` columns of ``q``, such that ``q`` and ``r`` have dimensions ``(..., M, K)`` and ``(..., K, N)``, respectively, and where ``K = min(M, N)``.
        -   ``'complete'``: compute ``q`` and ``r`` with dimensions ``(..., M, M)`` and ``(..., M, N)``, respectively.

        Default: ``'reduced'``.

    Returns
    -------
    out: Tuple[array, array]
        a namedtuple ``(Q, R)`` whose

        -   first element must have the field name ``Q`` and must be an array whose shape depends on the value of ``mode`` and contain matrices with orthonormal columns. If ``mode`` is ``'complete'``, the array must have shape ``(..., M, M)``. If ``mode`` is ``'reduced'``, the array must have shape ``(..., M, K)``, where ``K = min(M, N)``. The first ``x.ndim-2`` dimensions must have the same size as those of the input array ``x``.
        -   second element must have the field name ``R`` and must be an array whose shape depends on the value of ``mode`` and contain upper-triangular matrices. If ``mode`` is ``'complete'``, the array must have shape ``(..., M, N)``. If ``mode`` is ``'reduced'``, the array must have shape ``(..., K, N)``, where ``K = min(M, N)``. The first ``x.ndim-2`` dimensions must have the same size as those of the input ``x``.

        Each returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """


def slogdet(x: array, /) -> Tuple[array, array]:
    r"""
    Returns the sign and the natural logarithm of the absolute value of the determinant of a square matrix (or a stack of square matrices) ``x``.

    .. note::
       The purpose of this function is to calculate the determinant more accurately when the determinant is either very small or very large, as calling ``det`` may overflow or underflow.

    The sign of the determinant is given by

    .. math::
       \operatorname{sign}(\det x) = \begin{cases}
       0 & \textrm{if } \det x = 0 \\
       \frac{\det x}{|\det x|} & \textrm{otherwise}
       \end{cases}

    where :math:`|\det x|` is the absolute value of the determinant of ``x``.

    When ``x`` is a stack of matrices, the function must compute the sign and natural logarithm of the absolute value of the determinant for each matrix in the stack.

    **Special Cases**

    For real-valued floating-point operands,

    - If the determinant is zero, the ``sign`` should be ``0`` and ``logabsdet`` should be ``-infinity``.

    For complex floating-point operands,

    - If the determinant is ``0 + 0j``, the ``sign`` should be ``0 + 0j`` and ``logabsdet`` should be ``-infinity + 0j``.

    .. note::
       Depending on the underlying algorithm, when the determinant is zero, the returned result may differ from ``-infinity`` (or ``-infinity + 0j``). In all cases, the determinant should be equal to ``sign * exp(logabsdet)`` (although, again, the result may be subject to numerical precision errors).

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Should have a floating-point data type.

    Returns
    -------
    out: Tuple[array, array]
        a namedtuple (``sign``, ``logabsdet``) whose

        -   first element must have the field name ``sign`` and must be an array containing a number representing the sign of the determinant for each square matrix. Must have the same data type as ``x``.
        -   second element must have the field name ``logabsdet`` and must be an array containing the natural logarithm of the absolute value of the determinant for each square matrix. If ``x`` is real-valued, the returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. If ``x`` is complex, the returned array must have a real-valued floating-point data type having the same precision as ``x`` (e.g., if ``x`` is ``complex64``, ``logabsdet`` must have a ``float32`` data type).

        Each returned array must have shape ``shape(x)[:-2]``.
    """


def solve(x1: array, x2: array, /) -> array:
    r"""
    Returns the solution of a square system of linear equations with a unique solution.

    Let ``x1`` equal :math:`A` and ``x2`` equal :math:`B`. If the promoted data type of ``x1`` and ``x2`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if the promoted data type of ``x1`` and ``x2`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    This function computes the solution :math:`X \in\ \mathbb{K}^{m \times k}` of the **linear system** associated to :math:`A \in\ \mathbb{K}^{m \times m}` and :math:`B \in\ \mathbb{K}^{m \times k}` and is defined as

    .. math::
       AX = B

    This system of linear equations has a unique solution if and only if :math:`A` is invertible.

    .. note::
       Whether an array library explicitly checks whether ``x1`` is invertible is implementation-defined.

    When ``x1`` and/or ``x2`` is a stack of matrices, the function must compute a solution for each matrix in the stack.

    Parameters
    ----------
    x1: array
        coefficient array ``A`` having shape ``(..., M, M)`` and whose innermost two dimensions form square matrices. Must be of full rank (i.e., all rows or, equivalently, columns must be linearly independent). Should have a floating-point data type.
    x2: array
        ordinate (or "dependent variable") array ``B``. If ``x2`` has shape ``(M,)``, ``x2`` is equivalent to an array having shape ``(..., M, 1)``. If ``x2`` has shape ``(..., M, K)``, each column ``k`` defines a set of ordinate values for which to compute a solution, and ``shape(x2)[:-1]`` must be compatible with ``shape(x1)[:-1]`` (see :ref:`broadcasting`). Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the solution to the system ``AX = B`` for each square matrix. The returned array must have the same shape as ``x2`` (i.e., the array corresponding to ``B``) and must have a floating-point data type determined by :ref:`type-promotion`.
    """


def svd(x: array, /, *, full_matrices: bool = True) -> Union[array, Tuple[array, ...]]:
    r"""
    Returns a singular value decomposition (SVD) of a matrix (or a stack of matrices) ``x``.

    If ``x`` is real-valued, let :math:`\mathbb{K}` be the set of real numbers :math:`\mathbb{R}`, and, if ``x`` is complex-valued, let :math:`\mathbb{K}` be the set of complex numbers :math:`\mathbb{C}`.

    The full **singular value decomposition** of an :math:`m \times n` matrix :math:`x \in\ \mathbb{K}^{m \times n}` is a factorization of the form

    .. math::
       x = U \Sigma V^H

    where :math:`U \in\ \mathbb{K}^{m \times m}`, :math:`\Sigma \in\ \mathbb{K}^{m \times\ n}`, :math:`\operatorname{diag}(\Sigma) \in\ \mathbb{R}^{k}` with :math:`k = \operatorname{min}(m, n)`, :math:`V^H \in\ \mathbb{K}^{n \times n}`, and where :math:`V^H` is the conjugate transpose when :math:`V` is complex and the transpose when :math:`V` is real-valued. When ``x`` is real-valued, :math:`U`, :math:`V` (and thus :math:`V^H`) are orthogonal, and, when ``x`` is complex, :math:`U`, :math:`V` (and thus :math:`V^H`) are unitary.

    When :math:`m \gt n` (tall matrix), we can drop the last :math:`m - n` columns of :math:`U` to form the reduced SVD

    .. math::
       x = U \Sigma V^H

    where :math:`U \in\ \mathbb{K}^{m \times k}`, :math:`\Sigma \in\ \mathbb{K}^{k \times\ k}`, :math:`\operatorname{diag}(\Sigma) \in\ \mathbb{R}^{k}`, and :math:`V^H \in\ \mathbb{K}^{k \times n}`. In this case, :math:`U` and :math:`V` have orthonormal columns.

    Similarly, when :math:`n \gt m` (wide matrix), we can drop the last :math:`n - m` columns of :math:`V` to also form a reduced SVD.

    This function returns the decomposition :math:`U`, :math:`S`, and :math:`V^H`, where :math:`S = \operatorname{diag}(\Sigma)`.

    When ``x`` is a stack of matrices, the function must compute the singular value decomposition for each matrix in the stack.

    .. warning::
       The returned arrays :math:`U` and :math:`V` are neither unique nor continuous with respect to ``x``. Because :math:`U` and :math:`V` are not unique, different hardware and software may compute different singular vectors.

       Non-uniqueness stems from the fact that multiplying any pair of singular vectors :math:`u_k`, :math:`v_k` by :math:`-1` when ``x`` is real-valued and by :math:`e^{\phi j}` (:math:`\phi \in \mathbb{R}`) when ``x`` is complex produces another two valid singular vectors of the matrix.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.
    full_matrices: bool
        If ``True``, compute full-sized ``U`` and ``Vh``, such that ``U`` has shape ``(..., M, M)`` and ``Vh`` has shape ``(..., N, N)``. If ``False``, compute on the leading ``K`` singular vectors, such that ``U`` has shape ``(..., M, K)`` and ``Vh`` has shape ``(..., K, N)`` and where ``K = min(M, N)``. Default: ``True``.

    Returns
    -------
    out: Union[array, Tuple[array, ...]]
        a namedtuple ``(U, S, Vh)`` whose

        -   first element must have the field name ``U`` and must be an array whose shape depends on the value of ``full_matrices`` and contain matrices with orthonormal columns (i.e., the columns are left singular vectors). If ``full_matrices`` is ``True``, the array must have shape ``(..., M, M)``. If ``full_matrices`` is ``False``, the array must have shape ``(..., M, K)``, where ``K = min(M, N)``. The first ``x.ndim-2`` dimensions must have the same shape as those of the input ``x``. Must have the same data type as ``x``.
        -   second element must have the field name ``S`` and must be an array with shape ``(..., K)`` that contains the vector(s) of singular values of length ``K``, where ``K = min(M, N)``. For each vector, the singular values must be sorted in descending order by magnitude, such that ``s[..., 0]`` is the largest value, ``s[..., 1]`` is the second largest value, et cetera. The first ``x.ndim-2`` dimensions must have the same shape as those of the input ``x``. Must have a real-valued floating-point data type having the same precision as ``x`` (e.g., if ``x`` is ``complex64``, ``S`` must have a ``float32`` data type).
        -   third element must have the field name ``Vh`` and must be an array whose shape depends on the value of ``full_matrices`` and contain orthonormal rows (i.e., the rows are the right singular vectors and the array is the adjoint). If ``full_matrices`` is ``True``, the array must have shape ``(..., N, N)``. If ``full_matrices`` is ``False``, the array must have shape ``(..., K, N)`` where ``K = min(M, N)``. The first ``x.ndim-2`` dimensions must have the same shape as those of the input ``x``. Must have the same data type as ``x``.
    """


def svdvals(x: array, /) -> array:
    """
    Returns the singular values of a matrix (or a stack of matrices) ``x``.

    When ``x`` is a stack of matrices, the function must compute the singular values for each matrix in the stack.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form matrices on which to perform singular value decomposition. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array with shape ``(..., K)`` that contains the vector(s) of singular values of length ``K``, where ``K = min(M, N)``. For each vector, the singular values must be sorted in descending order by magnitude, such that ``s[..., 0]`` is the largest value, ``s[..., 1]`` is the second largest value, et cetera. The first ``x.ndim-2`` dimensions must have the same shape as those of the input ``x``. The returned array must have a real-valued floating-point data type having the same precision as ``x`` (e.g., if ``x`` is ``complex64``, the returned array must have a ``float32`` data type).
    """


def tensordot(
    x1: array,
    x2: array,
    /,
    *,
    axes: Union[int, Tuple[Sequence[int], Sequence[int]]] = 2,
) -> array:
    """Alias for :func:`~array_api.tensordot`."""


def trace(x: array, /, *, offset: int = 0, dtype: Optional[dtype] = None) -> array:
    """
    Returns the sum along the specified diagonals of a matrix (or a stack of matrices) ``x``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two dimensions form ``MxN`` matrices. Should have a numeric data type.
    offset: int
        offset specifying the off-diagonal relative to the main diagonal.

        -   ``offset = 0``: the main diagonal.
        -   ``offset > 0``: off-diagonal above the main diagonal.
        -   ``offset < 0``: off-diagonal below the main diagonal.

        Default: ``0``.
    dtype: Optional[dtype]
        data type of the returned array. If ``None``,

        -   if the default data type corresponding to the data type "kind" (integer, real-valued floating-point, or complex floating-point) of ``x`` has a smaller range of values than the data type of ``x`` (e.g., ``x`` has data type ``int64`` and the default data type is ``int32``, or ``x`` has data type ``uint64`` and the default data type is ``int64``), the returned array must have the same data type as ``x``.
        -   if ``x`` has a real-valued floating-point data type, the returned array must have the default real-valued floating-point data type.
        -   if ``x`` has a complex floating-point data type, the returned array must have the default complex floating-point data type.
        -   if ``x`` has a signed integer data type (e.g., ``int16``), the returned array must have the default integer data type.
        -   if ``x`` has an unsigned integer data type (e.g., ``uint16``), the returned array must have an unsigned integer data type having the same number of bits as the default integer data type (e.g., if the default integer data type is ``int32``, the returned array must have a ``uint32`` data type).

        If the data type (either specified or resolved) differs from the data type of ``x``, the input array should be cast to the specified data type before computing the sum. Default: ``None``.

        .. note::
           keyword argument is intended to help prevent data type overflows.

    Returns
    -------
    out: array
        an array containing the traces and whose shape is determined by removing the last two dimensions and storing the traces in the last array dimension. For example, if ``x`` has rank ``k`` and shape ``(I, J, K, ..., L, M, N)``, then an output array has rank ``k-2`` and shape ``(I, J, K, ..., L)`` where

        ::

          out[i, j, k, ..., l] = trace(a[i, j, k, ..., l, :, :])

        The returned array must have a data type as described by the ``dtype`` parameter above.

    Notes
    -----

    **Special Cases**

    Let ``N`` equal the number of elements over which to compute the sum.

    -   If ``N`` is ``0``, the sum is ``0`` (i.e., the empty sum).

    For both real-valued and complex floating-point operands, special cases must be handled as if the operation is implemented by successive application of :func:`~array_api.add`.
    """


def vecdot(x1: array, x2: array, /, *, axis: int = None) -> array:
    """Alias for :func:`~array_api.vecdot`."""


def vector_norm(
    x: array,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: bool = False,
    ord: Union[int, float, Literal[inf, -inf]] = 2,
) -> array:
    r"""
    Computes the vector norm of a vector (or batch of vectors) ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.
    axis: Optional[Union[int, Tuple[int, ...]]]
        If an integer, ``axis`` specifies the axis (dimension) along which to compute vector norms. If an n-tuple, ``axis`` specifies the axes (dimensions) along which to compute batched vector norms. If ``None``, the vector norm must be computed over all array values (i.e., equivalent to computing the vector norm of a flattened array). Negative indices must be supported. Default: ``None``.
    keepdims: bool
        If ``True``, the axes (dimensions) specified by ``axis`` must be included in the result as singleton dimensions, and, accordingly, the result must be compatible with the input array (see :ref:`broadcasting`). Otherwise, if ``False``, the axes (dimensions) specified by ``axis`` must not be included in the result. Default: ``False``.
    ord: Union[int, float, Literal[inf, -inf]]
        order of the norm. The following mathematical norms must be supported:

        +------------------+----------------------------+
        | ord              | description                |
        +==================+============================+
        | 1                | L1-norm (Manhattan)        |
        +------------------+----------------------------+
        | 2                | L2-norm (Euclidean)        |
        +------------------+----------------------------+
        | inf              | infinity norm              |
        +------------------+----------------------------+
        | (int,float >= 1) | p-norm                     |
        +------------------+----------------------------+

        The following non-mathematical "norms" must be supported:

        +------------------+--------------------------------+
        | ord              | description                    |
        +==================+================================+
        | 0                | sum(a != 0)                    |
        +------------------+--------------------------------+
        | -1               | 1./sum(1./abs(a))              |
        +------------------+--------------------------------+
        | -2               | 1./sqrt(sum(1./abs(a)\*\*2))   |
        +------------------+--------------------------------+
        | -inf             | min(abs(a))                    |
        +------------------+--------------------------------+
        | (int,float < 1)  | sum(abs(a)\*\*ord)\*\*(1./ord) |
        +------------------+--------------------------------+

        Default: ``2``.

    Returns
    -------
    out: array
        an array containing the vector norms. If ``axis`` is ``None``, the returned array must be a zero-dimensional array containing a vector norm. If ``axis`` is a scalar value (``int`` or ``float``), the returned array must have a rank which is one less than the rank of ``x``. If ``axis`` is a ``n``-tuple, the returned array must have a rank which is ``n`` less than the rank of ``x``. If ``x`` has a real-valued data type, the returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`. If ``x`` has a complex-valued data type, the returned array must have a real-valued floating-point data type whose precision matches the precision of ``x`` (e.g., if ``x`` is ``complex128``, then the returned array must have a ``float64`` data type).
    """


__all__ = [
    "cholesky",
    "cross",
    "det",
    "diagonal",
    "eigh",
    "eigvalsh",
    "inv",
    "matmul",
    "matrix_norm",
    "matrix_power",
    "matrix_rank",
    "matrix_transpose",
    "outer",
    "pinv",
    "qr",
    "slogdet",
    "solve",
    "svd",
    "svdvals",
    "tensordot",
    "trace",
    "vecdot",
    "vector_norm",
]
