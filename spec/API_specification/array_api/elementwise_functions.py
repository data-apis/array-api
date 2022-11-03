from ._types import array

def abs(x: array, /) -> array:
    """
    Calculates the absolute value for each element ``x_i`` of the input array ``x`` (i.e., the element-wise result has the same magnitude as the respective element in ``x`` but has positive sign).

    .. note::
       For signed integer data types, the absolute value of the minimum representable integer is implementation-dependent.

    **Special Cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``-0``, the result is ``+0``.
    - If ``x_i`` is ``-infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the absolute value of each element in ``x``. The returned array must have the same data type as ``x``.
    """

def acos(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation of the principal value of the inverse cosine, having domain ``[-1, +1]`` and codomain ``[+0, +π]``, for each element ``x_i`` of the input array ``x``. Each element-wise result is expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is greater than ``1``, the result is ``NaN``.
    - If ``x_i`` is less than ``-1``, the result is ``NaN``.
    - If ``x_i`` is ``1``, the result is ``+0``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse cosine of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def acosh(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the inverse hyperbolic cosine, having domain ``[+1, +infinity]`` and codomain ``[+0, +infinity]``, for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``1``, the result is ``NaN``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array whose elements each represent the area of a hyperbolic sector. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse hyperbolic cosine of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def add(x1: array, x2: array, /) -> array:
    """
    Calculates the sum for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a finite number, the result is ``+infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a finite number, the result is ``-infinity``.
    - If ``x1_i`` is a finite number and ``x2_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x1_i`` is a finite number and ``x2_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is a nonzero finite number, the result is ``x2_i``.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is either ``+0`` or ``-0``, the result is ``x1_i``.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is ``-x1_i``, the result is ``+0``.
    - In the remaining cases, when neither ``infinity``, ``+0``, ``-0``, nor a ``NaN`` is involved, and the operands have the same mathematical sign or have different magnitudes, the sum must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported round mode. If the magnitude is too large to represent, the operation overflows and the result is an `infinity` of appropriate mathematical sign.

    .. note::
       Floating-point addition is a commutative operation, but not always associative.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise sums. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def asin(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation of the principal value of the inverse sine, having domain ``[-1, +1]`` and codomain ``[-π/2, +π/2]`` for each element ``x_i`` of the input array ``x``. Each element-wise result is expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is greater than ``1``, the result is ``NaN``.
    - If ``x_i`` is less than ``-1``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse sine of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def asinh(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the inverse hyperbolic sine, having domain ``[-infinity, +infinity]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` in the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.

    Parameters
    ----------
    x: array
        input array whose elements each represent the area of a hyperbolic sector. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse hyperbolic sine of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def atan(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation of the principal value of the inverse tangent, having domain ``[-infinity, +infinity]`` and codomain ``[-π/2, +π/2]``, for each element ``x_i`` of the input array ``x``. Each element-wise result is expressed in radians.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is an implementation-dependent approximation to ``+π/2``.
    - If ``x_i`` is ``-infinity``, the result is an implementation-dependent approximation to ``-π/2``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse tangent of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def atan2(x1: array, x2: array, /) -> array:
    """
    Calculates an implementation-dependent approximation of the inverse tangent of the quotient ``x1/x2``, having domain ``[-infinity, +infinity] x [-infinity, +infinity]`` (where the ``x`` notation denotes the set of ordered pairs of elements ``(x1_i, x2_i)``) and codomain ``[-π, +π]``, for each pair of elements ``(x1_i, x2_i)`` of the input arrays ``x1`` and ``x2``, respectively. Each element-wise result is expressed in radians.

    The mathematical signs of ``x1_i`` and ``x2_i`` determine the quadrant of each element-wise result. The quadrant (i.e., branch) is chosen such that each element-wise result is the signed angle in radians between the ray ending at the origin and passing through the point ``(1,0)`` and the ray ending at the origin and passing through the point ``(x2_i, x1_i)``.

    .. note::
       Note the role reversal: the "y-coordinate" is the first function parameter; the "x-coordinate" is the second function parameter. The parameter order is intentional and traditional for the two-argument inverse tangent function where the y-coordinate argument is first and the x-coordinate argument is second.

    By IEEE 754 convention, the inverse tangent of the quotient ``x1/x2`` is defined for ``x2_i`` equal to positive or negative zero and for either or both of ``x1_i`` and ``x2_i`` equal to positive or negative ``infinity``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is an implementation-dependent approximation to ``+π/2``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is an implementation-dependent approximation to ``+π/2``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``+0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is ``-0``, the result is an implementation-dependent approximation to ``+π``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is an implementation-dependent approximation to ``+π``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``+0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is ``-0``, the result is an implementation-dependent approximation to ``-π``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is an implementation-dependent approximation to ``-π``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is an implementation-dependent approximation to ``-π/2``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is an implementation-dependent approximation to ``-π/2``.
    - If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is ``+infinity``, the result is ``+0``.
    - If ``x1_i`` is greater than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is ``-infinity``, the result is an implementation-dependent approximation to ``+π``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is ``+infinity``, the result is ``-0``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, and ``x2_i`` is ``-infinity``, the result is an implementation-dependent approximation to ``-π``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a finite number, the result is an implementation-dependent approximation to ``+π/2``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a finite number, the result is an implementation-dependent approximation to ``-π/2``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``+infinity``, the result is an implementation-dependent approximation to ``+π/4``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is ``-infinity``, the result is an implementation-dependent approximation to ``+3π/4``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``+infinity``, the result is an implementation-dependent approximation to ``-π/4``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is ``-infinity``, the result is an implementation-dependent approximation to ``-3π/4``.

    Parameters
    ----------
    x1: array
        input array corresponding to the y-coordinates. Should have a real-valued floating-point data type.
    x2: array
        input array corresponding to the x-coordinates. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse tangent of the quotient ``x1/x2``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.

    """

def atanh(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the inverse hyperbolic tangent, having domain ``[-1, +1]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``-1``, the result is ``NaN``.
    - If ``x_i`` is greater than ``1``, the result is ``NaN``.
    - If ``x_i`` is ``-1``, the result is ``-infinity``.
    - If ``x_i`` is ``+1``, the result is ``+infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.

    Parameters
    ----------
    x: array
        input array whose elements each represent the area of a hyperbolic sector. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the inverse hyperbolic tangent of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def bitwise_and(x1: array, x2: array, /) -> array:
    """
    Computes the bitwise AND of the underlying binary representation of each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have an integer or boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have an integer or boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def bitwise_left_shift(x1: array, x2: array, /) -> array:
    """
    Shifts the bits of each element ``x1_i`` of the input array ``x1`` to the left by appending ``x2_i`` (i.e., the respective element in the input array ``x2``) zeros to the right of ``x1_i``.

    Parameters
    ----------
    x1: array
        first input array. Should have an integer data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have an integer data type. Each element must be greater than or equal to ``0``.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def bitwise_invert(x: array, /) -> array:
    """
    Inverts (flips) each bit for each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have an integer or boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have the same data type as ``x``.
    """

def bitwise_or(x1: array, x2: array, /) -> array:
    """
    Computes the bitwise OR of the underlying binary representation of each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have an integer or boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have an integer or boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def bitwise_right_shift(x1: array, x2: array, /) -> array:
    """
    Shifts the bits of each element ``x1_i`` of the input array ``x1`` to the right according to the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       This operation must be an arithmetic shift (i.e., sign-propagating) and thus equivalent to floor division by a power of two.

    Parameters
    ----------
    x1: array
        first input array. Should have an integer data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have an integer data type. Each element must be greater than or equal to ``0``.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def bitwise_xor(x1: array, x2: array, /) -> array:
    """
    Computes the bitwise XOR of the underlying binary representation of each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have an integer or boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have an integer or boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def ceil(x: array, /) -> array:
    """
    Rounds each element ``x_i`` of the input array ``x`` to the smallest (i.e., closest to ``-infinity``) integer-valued number that is not less than ``x_i``.

    **Special cases**

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the rounded result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

def conj(x: array, /) -> array:
    """
    Returns the complex conjugate for each element ``x_i`` of the input array ``x``.

    For complex numbers of the form

    .. math::
       a + bj

    the complex conjugate is defined as

    .. math::
       a - bj

    Hence, the returned complex conjugates must be computed by negating the imaginary component of each element ``x_i``.

    Parameters
    ----------
    x: array
        input array. Should have a complex-floating point data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have the same data type as ``x``.
    """


def cos(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the cosine for each element ``x_i`` of the input array ``x``.

    Each element ``x_i`` is assumed to be expressed in radians.

    **Special cases**

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``NaN``.
    - If ``x_i`` is ``-infinity``, the result is ``NaN``.

    For complex floating-point operands, special cases must be handled as if the operation is implemented as ``cosh(x*1j)``.

    .. note::
       The cosine is an entire function on the complex plane and has no branch cuts.

    .. note::
       For complex arguments, the mathematical definition of cosine is

       .. math::
          \begin{align} \operatorname{cos}(x) &= \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n} \\ &= \frac{e^{jx} + e^{-jx}}{2} \\ &= \operatorname{cosh}(jx) \end{align}

       where :math:`\operatorname{cosh}` is the hyperbolic cosine.

    Parameters
    ----------
    x: array
        input array whose elements are each expressed in radians. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the cosine of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def cosh(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the hyperbolic cosine for each element ``x_i`` in the input array ``x``.

    The mathematical definition of the hyperbolic cosine is

    .. math::
       \operatorname{cosh}(x) = \frac{e^x + e^{-x}}{2}

    **Special cases**

    .. note::
       For all operands, ``cosh(x)`` must equal ``cosh(-x)``.

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``+infinity``.

    For complex floating-point operands, let ``a = real(x_i)``, ``b = imag(x_i)``, and

    .. note::
       For complex floating-point operands, ``cosh(conj(x))`` must equal ``conj(cosh(x))``.

    - If ``a`` is ``+0`` and ``b`` is ``+0``, the result is ``1 + 0j``.
    - If ``a`` is ``+0`` and ``b`` is ``+infinity``, the result is ``NaN + 0j`` (sign of the imaginary component is unspecified).
    - If ``a`` is ``+0`` and ``b`` is ``NaN``, the result is ``NaN + 0j`` (sign of the imaginary component is unspecified).
    - If ``a`` is a nonzero finite number and ``b`` is ``+infinity``, the result is ``NaN + NaN j``.
    - If ``a`` is a nonzero finite number and ``b`` is ``NaN``, the result is ``NaN + NaN j``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+0``, the result is ``+infinity + 0j``.
    - If ``a`` is ``+infinity`` and ``b`` is a nonzero finite number, the result is ``+infinity * cis(b)``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+infinity``, the result is ``+infinity + NaN j`` (sign of the real component is unspecified).
    - If ``a`` is ``+infinity`` and ``b`` is ``NaN``, the result is ``+infinity + NaN j``.
    - If ``a`` is ``NaN`` and ``b`` is either ``+0`` or ``-0``, the result is ``NaN + 0j`` (sign of the imaginary component is unspecified).
    - If ``a`` is ``NaN`` and ``b`` is a nonzero finite number, the result is ``NaN + NaN j``.
    - If ``a`` is ``NaN`` and ``b`` is ``NaN``, the result is ``NaN + NaN j``.

    where ``cis(v)`` is ``cos(v) + sin(v)*1j``.

    .. note::
       The hyperbolic cosine is an entire function in the complex plane and has no branch cuts. The function is periodic, with period :math:`2\pi j`, with respect to the imaginary component.

    Parameters
    ----------
    x: array
        input array whose elements each represent a hyperbolic angle. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the hyperbolic cosine of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def divide(x1: array, x2: array, /) -> array:
    """
    Calculates the division for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       If one or both of the input arrays have integer data types, the result is implementation-dependent, as type promotion between data type "kinds" (e.g., integer versus floating-point) is unspecified.

       Specification-compliant libraries may choose to raise an error or return an array containing the element-wise results. If an array is returned, the array must have a real-valued floating-point data type.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+0`` or ``-0``, the result is ``NaN``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is ``+0``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is ``+infinity``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is ``-infinity``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is ``-infinity``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``-infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``-infinity``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``+infinity``.
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``+0``.
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``-0``.
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``-0``.
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``+0``.
    - If ``x1_i`` and ``x2_i`` have the same mathematical sign and are both nonzero finite numbers, the result has a positive mathematical sign.
    - If ``x1_i`` and ``x2_i`` have different mathematical signs and are both nonzero finite numbers, the result has a negative mathematical sign.
    - In the remaining cases, where neither ``-infinity``, ``+0``, ``-0``, nor ``NaN`` is involved, the quotient must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to represent, the operation overflows and the result is an ``infinity`` of appropriate mathematical sign. If the magnitude is too small to represent, the operation underflows and the result is a zero of appropriate mathematical sign.

    Parameters
    ----------
    x1: array
        dividend input array. Should have a real-valued data type.
    x2: array
        divisor input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def equal(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i == x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. May have any data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). May have any data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def exp(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the exponential function for each element ``x_i`` of the input array ``x`` (``e`` raised to the power of ``x_i``, where ``e`` is the base of the natural logarithm).

    **Special cases**

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``1``.
    - If ``x_i`` is ``-0``, the result is ``1``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``+0``.

    For complex floating-point operands, let ``a = real(x_i)``, ``b = imag(x_i)``, and

    .. note::
       For complex floating-point operands, ``exp(conj(x))`` must equal ``conj(exp(x))``.

    - If ``a`` is either ``+0`` or ``-0`` and ``b`` is ``+0``, the result is ``1 + 0j``.
    - If ``a`` is a finite number and ``b`` is ``+infinity``, the result is ``NaN + NaN j``.
    - If ``a`` is a finite number and ``b`` is ``NaN``, the result is ``NaN + NaN j``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+0``, the result is ``infinity + 0j``.
    - If ``a`` is ``-infinity`` and ``b`` is a finite number, the result is ``+0 * cis(b)``.
    - If ``a`` is ``+infinity`` and ``b`` is a nonzero finite number, the result is ``+infinity * cis(b)``.
    - If ``a`` is ``-infinity`` and ``b`` is ``+infinity``, the result is ``0 + 0j`` (signs of real and imaginary components are unspecified).
    - If ``a`` is ``+infinity`` and ``b`` is ``+infinity``, the result is ``infinity + NaN j`` (sign of real component is unspecified).
    - If ``a`` is ``-infinity`` and ``b`` is ``NaN``, the result is ``0 + 0j`` (signs of real and imaginary components are unspecified).
    - If ``a`` is ``+infinity`` and ``b`` is ``NaN``, the result is ``infinity + NaN j`` (sign of real component is unspecified).
    - If ``a`` is ``NaN`` and ``b`` is ``+0``, the result is ``NaN + 0j``.
    - If ``a`` is ``NaN`` and ``b`` is not equal to ``0``, the result is ``NaN + NaN j``.
    - If ``a`` is ``NaN`` and ``b`` is ``NaN``, the result is ``NaN + NaN j``.

    where ``cis(v)`` is ``cos(v) + sin(v)*1j``.

    .. note::
       The exponential function is an entire function in the complex plane and has no branch cuts.

    Parameters
    ----------
    x: array
        input array. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated exponential function result for each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def expm1(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to ``exp(x)-1``, having domain ``[-infinity, +infinity]`` and codomain ``[-1, +infinity]``, for each element ``x_i`` of the input array ``x``.

    .. note::
       The purpose of this function is to calculate ``exp(x)-1.0`` more accurately when `x` is close to zero. Accordingly, conforming implementations should avoid implementing this function as simply ``exp(x)-1.0``. See FDLIBM, or some other IEEE 754-2019 compliant mathematical library, for a potential reference implementation.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-1``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def floor(x: array, /) -> array:
    """
    Rounds each element ``x_i`` of the input array ``x`` to the greatest (i.e., closest to ``+infinity``) integer-valued number that is not greater than ``x_i``.

    **Special cases**

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the rounded result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

def floor_divide(x1: array, x2: array, /) -> array:
    r"""
    Rounds the result of dividing each element ``x1_i`` of the input array ``x1`` by the respective element ``x2_i`` of the input array ``x2`` to the greatest (i.e., closest to `+infinity`) integer-value number that is not greater than the division result.

    .. note::
       For input arrays which promote to an integer data type, the result of division by zero is unspecified and thus implementation-defined.

    **Special cases**

    .. note::
       Floor division was introduced in Python via `PEP 238 <https://www.python.org/dev/peps/pep-0238/>`_ with the goal to disambiguate "true division" (i.e., computing an approximation to the mathematical operation of division) from "floor division" (i.e., rounding the result of division toward negative infinity). The former was computed when one of the operands was a ``float``, while the latter was computed when both operands were ``int``\s. Overloading the ``/`` operator to support both behaviors led to subtle numerical bugs when integers are possible, but not expected.

       To resolve this ambiguity, ``/`` was designated for true division, and ``//`` was designated for floor division. Semantically, floor division was `defined <https://www.python.org/dev/peps/pep-0238/#semantics-of-floor-division>`_ as equivalent to ``a // b == floor(a/b)``; however, special floating-point cases were left ill-defined.

       Accordingly, floor division is not implemented consistently across array libraries for some of the special cases documented below. Namely, when one of the operands is ``infinity``, libraries may diverge with some choosing to strictly follow ``floor(a/b)`` and others choosing to pair ``//`` with ``%`` according to the relation ``b = a % b + b * (a // b)``. The special cases leading to divergent behavior are documented below.

       This specification prefers floor division to match ``floor(divide(x1, x2))`` in order to avoid surprising and unexpected results; however, array libraries may choose to more strictly follow Python behavior.

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+0`` or ``-0``, the result is ``NaN``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is ``+0``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is ``+infinity``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is ``-infinity``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is ``-infinity``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``+infinity``. (**note**: libraries may return ``NaN`` to match Python behavior.)
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``-infinity``. (**note**: libraries may return ``NaN`` to match Python behavior.)
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``-infinity``. (**note**: libraries may return ``NaN`` to match Python behavior.)
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``+infinity``. (**note**: libraries may return ``NaN`` to match Python behavior.)
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``+0``.
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``-0``. (**note**: libraries may return ``-1.0`` to match Python behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``-0``. (**note**: libraries may return ``-1.0`` to match Python behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``+0``.
    - If ``x1_i`` and ``x2_i`` have the same mathematical sign and are both nonzero finite numbers, the result has a positive mathematical sign.
    - If ``x1_i`` and ``x2_i`` have different mathematical signs and are both nonzero finite numbers, the result has a negative mathematical sign.
    - In the remaining cases, where neither ``-infinity``, ``+0``, ``-0``, nor ``NaN`` is involved, the quotient must be computed and rounded to the greatest (i.e., closest to `+infinity`) representable integer-value number that is not greater than the division result. If the magnitude is too large to represent, the operation overflows and the result is an ``infinity`` of appropriate mathematical sign. If the magnitude is too small to represent, the operation underflows and the result is a zero of appropriate mathematical sign.

    Parameters
    ----------
    x1: array
        dividend input array. Should have a real-valued data type.
    x2: array
        divisor input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def greater(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i > x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def greater_equal(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i >= x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def imag(x: array, /) -> array:
    """
    Returns the imaginary component of a complex number for each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a floating-point data type with the same floating-point precision as ``x`` (e.g., if ``x`` is ``complex64``, the returned array must have the floating-point data type ``float32``). 
    """

def isfinite(x: array, /) -> array:
    """
    Tests each element ``x_i`` of the input array ``x`` to determine if finite (i.e., not ``NaN`` and not equal to positive or negative infinity).

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing test results. An element ``out_i`` is ``True`` if ``x_i`` is finite and ``False`` otherwise. The returned array must have a data type of ``bool``.
    """

def isinf(x: array, /) -> array:
    """
    Tests each element ``x_i`` of the input array ``x`` to determine if equal to positive or negative infinity.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing test results. An element ``out_i`` is ``True`` if ``x_i`` is either positive or negative infinity and ``False`` otherwise. The returned array must have a data type of ``bool``.
    """

def isnan(x: array, /) -> array:
    """
    Tests each element ``x_i`` of the input array ``x`` to determine whether the element is ``NaN``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing test results. An element ``out_i`` is ``True`` if ``x_i`` is ``NaN`` and ``False`` otherwise. The returned array should have a data type of ``bool``.
    """

def less(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i < x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def less_equal(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i <= x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def log(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the natural (base ``e``) logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated natural logarithm for each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def log1p(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to ``log(1+x)``, where ``log`` refers to the natural (base ``e``) logarithm, having domain ``[-1, +infinity]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` of the input array ``x``.

    .. note::
       The purpose of this function is to calculate ``log(1+x)`` more accurately when `x` is close to zero. Accordingly, conforming implementations should avoid implementing this function as simply ``log(1+x)``. See FDLIBM, or some other IEEE 754-2019 compliant mathematical library, for a potential reference implementation.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``-1``, the result is ``NaN``.
    - If ``x_i`` is ``-1``, the result is ``-infinity``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def log2(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the base ``2`` logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated base ``2`` logarithm for each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def log10(x: array, /) -> array:
    """
    Calculates an implementation-dependent approximation to the base ``10`` logarithm, having domain ``[0, +infinity]`` and codomain ``[-infinity, +infinity]``, for each element ``x_i`` of the input array ``x``.

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is either ``+0`` or ``-0``, the result is ``-infinity``.
    - If ``x_i`` is ``1``, the result is ``+0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the evaluated base ``10`` logarithm for each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def logaddexp(x1: array, x2: array, /) -> array:
    """
    Calculates the logarithm of the sum of exponentiations ``log(exp(x1) + exp(x2))`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is not ``NaN``, the result is ``+infinity``.
    - If ``x1_i`` is not ``NaN`` and ``x2_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued floating-point data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def logical_and(x1: array, x2: array, /) -> array:
    """
    Computes the logical AND for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       While this specification recommends that this function only accept input arrays having a boolean data type, specification-compliant array libraries may choose to accept input arrays having real-valued data types. If non-boolean data types are supported, zeros must be considered the equivalent of ``False``, while non-zeros must be considered the equivalent of ``True``.

    Parameters
    ----------
    x1: array
        first input array. Should have a boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of `bool`.
    """

def logical_not(x: array, /) -> array:
    """
    Computes the logical NOT for each element ``x_i`` of the input array ``x``.

    .. note::
       While this specification recommends that this function only accept input arrays having a boolean data type, specification-compliant array libraries may choose to accept input arrays having real-valued data types. If non-boolean data types are supported, zeros must be considered the equivalent of ``False``, while non-zeros must be considered the equivalent of ``True``.

    Parameters
    ----------
    x: array
        input array. Should have a boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def logical_or(x1: array, x2: array, /) -> array:
    """
    Computes the logical OR for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       While this specification recommends that this function only accept input arrays having a boolean data type, specification-compliant array libraries may choose to accept input arrays having real-valued data types. If non-boolean data types are supported, zeros must be considered the equivalent of ``False``, while non-zeros must be considered the equivalent of ``True``.

    Parameters
    ----------
    x1: array
        first input array. Should have a boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def logical_xor(x1: array, x2: array, /) -> array:
    """
    Computes the logical XOR for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       While this specification recommends that this function only accept input arrays having a boolean data type, specification-compliant array libraries may choose to accept input arrays having real-valued data types. If non-boolean data types are supported, zeros must be considered the equivalent of ``False``, while non-zeros must be considered the equivalent of ``True``.

    Parameters
    ----------
    x1: array
        first input array. Should have a boolean data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a boolean data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def multiply(x1: array, x2: array, /) -> array:
    """
    Calculates the product for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    **Special cases**

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+0`` or ``-0``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` and ``x2_i`` have the same mathematical sign, the result has a positive mathematical sign, unless the result is ``NaN``. If the result is ``NaN``, the "sign" of ``NaN`` is implementation-defined.
    - If ``x1_i`` and ``x2_i`` have different mathematical signs, the result has a negative mathematical sign, unless the result is ``NaN``. If the result is ``NaN``, the "sign" of ``NaN`` is implementation-defined.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is a nonzero finite number, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
    - If ``x1_i`` is a nonzero finite number and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
    - In the remaining cases, where neither ``infinity`` nor ``NaN`` is involved, the product must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to represent, the result is an `infinity` of appropriate mathematical sign. If the magnitude is too small to represent, the result is a zero of appropriate mathematical sign.

    .. note::
       Floating-point multiplication is not always associative due to finite precision.

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise products. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def negative(x: array, /) -> array:
    """
    Computes the numerical negative of each element ``x_i`` (i.e., ``y_i = -x_i``) of the input array ``x``.

    .. note::
       For signed integer data types, the numerical negative of the minimum representable integer is implementation-dependent.

    .. note::
       If ``x`` has a complex floating-point data type, both the real and imaginary components for each ``x_i`` must be negated (a result which follows from the rules of complex number multiplication).

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def not_equal(x1: array, x2: array, /) -> array:
    """
    Computes the truth value of ``x1_i != x2_i`` for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``.

    Parameters
    ----------
    x1: array
        first input array. May have any data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`).

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type of ``bool``.
    """

def positive(x: array, /) -> array:
    """
    Computes the numerical positive of each element ``x_i`` (i.e., ``y_i = +x_i``) of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

def pow(x1: array, x2: array, /) -> array:
    """
    Calculates an implementation-dependent approximation of exponentiation by raising each element ``x1_i`` (the base) of the input array ``x1`` to the power of ``x2_i`` (the exponent), where ``x2_i`` is the corresponding element of the input array ``x2``.

    .. note::
       If both ``x1`` and ``x2`` have integer data types, the result of ``pow`` when ``x2_i`` is negative (i.e., less than zero) is unspecified and thus implementation-dependent.

       If ``x1`` has an integer data type and ``x2`` has a real-valued floating-point data type, behavior is implementation-dependent (type promotion between data type "kinds" (integer versus floating-point) is unspecified).

    **Special cases**

    For floating-point operands,

    - If ``x1_i`` is not equal to ``1`` and ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x2_i`` is ``+0``, the result is ``1``, even if ``x1_i`` is ``NaN``.
    - If ``x2_i`` is ``-0``, the result is ``1``, even if ``x1_i`` is ``NaN``.
    - If ``x1_i`` is ``NaN`` and ``x2_i`` is not equal to ``0``, the result is ``NaN``.
    - If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``abs(x1_i)`` is greater than ``1`` and ``x2_i`` is ``-infinity``, the result is ``+0``.
    - If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``+infinity``, the result is ``1``.
    - If ``abs(x1_i)`` is ``1`` and ``x2_i`` is ``-infinity``, the result is ``1``.
    - If ``x1_i`` is ``1`` and ``x2_i`` is not ``NaN``, the result is ``1``.
    - If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``+infinity``, the result is ``+0``.
    - If ``abs(x1_i)`` is less than ``1`` and ``x2_i`` is ``-infinity``, the result is ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is greater than ``0``, the result is ``+infinity``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is less than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and ``x2_i`` is an odd integer value, the result is ``-infinity``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is greater than ``0``, and ``x2_i`` is not an odd integer value, the result is ``+infinity``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and ``x2_i`` is an odd integer value, the result is ``-0``.
    - If ``x1_i`` is ``-infinity``, ``x2_i`` is less than ``0``, and ``x2_i`` is not an odd integer value, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is ``+infinity``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and ``x2_i`` is an odd integer value, the result is ``-0``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is greater than ``0``, and ``x2_i`` is not an odd integer value, the result is ``+0``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i`` is an odd integer value, the result is ``-infinity``.
    - If ``x1_i`` is ``-0``, ``x2_i`` is less than ``0``, and ``x2_i`` is not an odd integer value, the result is ``+infinity``.
    - If ``x1_i`` is less than ``0``, ``x1_i`` is a finite number, ``x2_i`` is a finite number, and ``x2_i`` is not an integer value, the result is ``NaN``.

    Parameters
    ----------
    x1: array
        first input array whose elements correspond to the exponentiation base. Should have a real-valued data type.
    x2: array
        second input array whose elements correspond to the exponentiation exponent. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def real(x: array, /) -> array:
    """
    Returns the real component of a complex number for each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a complex floating-point data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. The returned array must have a floating-point data type with the same floating-point precision as ``x`` (e.g., if ``x`` is ``complex64``, the returned array must have the floating-point data type ``float32``). 
    """

def remainder(x1: array, x2: array, /) -> array:
    """
    Returns the remainder of division for each element ``x1_i`` of the input array ``x1`` and the respective element ``x2_i`` of the input array ``x2``.

    .. note::
       This function is equivalent to the Python modulus operator ``x1_i % x2_i``.

    .. note::
       For input arrays which promote to an integer data type, the result of division by zero is unspecified and thus implementation-defined.

    **Special cases**

    .. note::
       In general, similar to Python's ``%`` operator, this function is **not** recommended for floating-point operands as semantics do not follow IEEE 754. That this function is specified to accept floating-point operands is primarily for reasons of backward compatibility.

    For floating-point operands,

    - If either ``x1_i`` or ``x2_i`` is ``NaN``, the result is ``NaN``.
    - If ``x1_i`` is either ``+infinity`` or ``-infinity`` and ``x2_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.
    - If ``x1_i`` is either ``+0`` or ``-0`` and ``x2_i`` is either ``+0`` or ``-0``, the result is ``NaN``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is greater than ``0``, the result is ``+0``.
    - If ``x1_i`` is ``+0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is ``-0`` and ``x2_i`` is less than ``0``, the result is ``-0``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``+0``, the result is ``NaN``.
    - If ``x1_i`` is greater than ``0`` and ``x2_i`` is ``-0``, the result is ``NaN``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``+0``, the result is ``NaN``.
    - If ``x1_i`` is less than ``0`` and ``x2_i`` is ``-0``, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``NaN``.
    - If ``x1_i`` is ``+infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a positive (i.e., greater than ``0``) finite number, the result is ``NaN``.
    - If ``x1_i`` is ``-infinity`` and ``x2_i`` is a negative (i.e., less than ``0``) finite number, the result is ``NaN``.
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``x1_i``. (**note**: this result matches Python behavior.)
    - If ``x1_i`` is a positive (i.e., greater than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``x2_i``. (**note**: this result matches Python behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``+infinity``, the result is ``x2_i``. (**note**: this results matches Python behavior.)
    - If ``x1_i`` is a negative (i.e., less than ``0``) finite number and ``x2_i`` is ``-infinity``, the result is ``x1_i``. (**note**: this result matches Python behavior.)
    - In the remaining cases, the result must match that of the Python ``%`` operator.

    Parameters
    ----------
    x1: array
        dividend input array. Should have a real-valued data type.
    x2: array
        divisor input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise results. Each element-wise result must have the same sign as the respective element ``x2_i``. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def round(x: array, /) -> array:
    """
    Rounds each element ``x_i`` of the input array ``x`` to the nearest integer-valued number.

    .. note::
       For complex floating-point operands, real and imaginary components must be independently rounded to the nearest integer-valued number.
    
       Rounded real and imaginary components must be equal to their equivalent rounded real-valued floating-point counterparts (i.e., for complex-valued ``x``, ``real(round(x))`` must equal ``round(real(x)))`` and ``imag(round(x))`` must equal ``round(imag(x))``).

    **Special cases**

    .. note::
       For complex floating-point operands, the following special cases apply to real and imaginary components independently (e.g., if ``real(x_i)`` is ``NaN``, the rounded real component is ``NaN``).

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If two integers are equally close to ``x_i``, the result is the even integer closest to ``x_i``.

    Parameters
    ----------
    x: array
        input array. Should have a numeric data type.

    Returns
    -------
    out: array
        an array containing the rounded result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

def sign(x: array, /) -> array:
    """
    Returns an indication of the sign of a number for each element ``x_i`` of the input array ``x``.

    **Special cases**

    - If ``x_i`` is less than ``0``, the result is ``-1``.
    - If ``x_i`` is either ``-0`` or ``+0``, the result is ``0``.
    - If ``x_i`` is greater than ``0``, the result is ``+1``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

def sin(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the sine for each element ``x_i`` of the input array ``x``.

    Each element ``x_i`` is assumed to be expressed in radians.

    **Special cases**

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.

    For complex floating-point operands, special cases must be handled as if the operation is implemented as ``-1j * sinh(x*1j)``.

    .. note::
       The sine is an entire function on the complex plane and has no branch cuts.

    .. note::
       For complex arguments, the mathematical definition of sine is

       .. math::
          \begin{align} \operatorname{sin}(x) &= \frac{e^{jx} - e^{-jx}}{2j} \\ &= \frac{\operatorname{sinh}(jx)}{j} \\ &= \frac{\operatorname{sinh}(jx)}{j} \cdot \frac{j}{j} \\ &= -j \cdot \operatorname{sinh}(jx) \end{align}

       where :math:`\operatorname{sinh}` is the hyperbolic sine.

    Parameters
    ----------
    x: array
        input array whose elements are each expressed in radians. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the sine of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def sinh(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the hyperbolic sine for each element ``x_i`` of the input array ``x``.

    The mathematical definition of the hyperbolic sine is

    .. math::
       \operatorname{sinh}(x) = \frac{e^x - e^{-x}}{2}

    **Special cases**

    .. note::
       For all operands, ``sinh(x)`` must equal ``-sinh(-x)``.

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.

    For complex floating-point operands, let ``a = real(x_i)``, ``b = imag(x_i)``, and

    .. note::
       For complex floating-point operands, ``sinh(conj(x))`` must equal ``conj(sinh(x))``.

    - If ``a`` is ``+0`` and ``b`` is ``+0``, the result is ``+0 + 0j``.
    - If ``a`` is ``+0`` and ``b`` is ``+infinity``, the result is ``0 + NaN j`` (sign of the real component is unspecified).
    - If ``a`` is ``+0`` and ``b`` is ``NaN``, the result is ``0 + NaN j`` (sign of the real component is unspecified).
    - If ``a`` is a positive (i.e., greater than ``0``) finite number and ``b`` is ``+infinity``, the result is ``NaN + NaN j``.
    - If ``a`` is a positive (i.e., greater than ``0``) finite number and ``b`` is ``NaN``, the result is ``NaN + NaN j``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+0``, the result is ``+infinity + 0j``.
    - If ``a`` is ``+infinity`` and ``b`` is a positive finite number, the result is ``+infinity * cis(b)``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+infinity``, the result is ``infinity + NaN j`` (sign of the real component is unspecified).
    - If ``a`` is ``+infinity`` and ``b`` is ``NaN``, the result is ``infinity + NaN j`` (sign of the real component is unspecified).
    - If ``a`` is ``NaN`` and ``b`` is ``+0``, the result is ``NaN + 0j``.
    - If ``a`` is ``NaN`` and ``b`` is a nonzero finite number, the result is ``NaN + NaN j``.
    - If ``a`` is ``NaN`` and ``b`` is ``NaN``, the result is ``NaN + NaN j``.

    where ``cis(v)`` is ``cos(v) + sin(v)*1j``.

    .. note::
       The hyperbolic sine is an entire function in the complex plane and has no branch cuts. The function is periodic, with period :math:`2\pi j`, with respect to the imaginary component.

    Parameters
    ----------
    x: array
        input array whose elements each represent a hyperbolic angle. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the hyperbolic sine of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def square(x: array, /) -> array:
    """
    Squares (``x_i * x_i``) each element ``x_i`` of the input array ``x``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the evaluated result for each element in ``x``. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def sqrt(x: array, /) -> array:
    """
    Calculates the square root, having domain ``[0, +infinity]`` and codomain ``[0, +infinity]``, for each element ``x_i`` of the input array ``x``. After rounding, each result must be indistinguishable from the infinitely precise result (as required by IEEE 754).

    **Special cases**

    For floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is less than ``0``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued floating-point data type.

    Returns
    -------
    out: array
        an array containing the square root of each element in ``x``. The returned array must have a real-valued floating-point data type determined by :ref:`type-promotion`.
    """

def subtract(x1: array, x2: array, /) -> array:
    """
    Calculates the difference for each element ``x1_i`` of the input array ``x1`` with the respective element ``x2_i`` of the input array ``x2``. The result of ``x1_i - x2_i`` must be the same as ``x1_i + (-x2_i)`` and must be governed by the same floating-point rules as addition (see :meth:`add`).

    Parameters
    ----------
    x1: array
        first input array. Should have a real-valued data type.
    x2: array
        second input array. Must be compatible with ``x1`` (see :ref:`broadcasting`). Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the element-wise differences. The returned array must have a data type determined by :ref:`type-promotion`.
    """

def tan(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the tangent for each element ``x_i`` of the input array ``x``.

    Each element ``x_i`` is assumed to be expressed in radians.

    **Special cases**

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is either ``+infinity`` or ``-infinity``, the result is ``NaN``.

    For complex floating-point operands, special cases must be handled as if the operation is implemented as ``-1j * tanh(x*1j)``.

    .. note::
       Tangent is an analytical function on the complex plane and has no branch cuts. The function is periodic, with period :math:`\pi j`, with respect to the real component and has first order poles along the real line at coordinates :math:`(\pi (\frac{1}{2} + n), 0)`. However, IEEE 754 binary floating-point representation cannot represent the value :math:`\pi / 2` exactly, and, thus, no argument value is possible for which a pole error occurs.

    .. note::
       For complex arguments, the mathematical definition of tangent is

       .. math::
          \begin{align} \operatorname{tan}(x) &= \frac{j(e^{-jx} - e^{jx})}{e^{-jx} + e^{jx}} \\ &= (-1) \frac{j(e^{jx} - e^{-jx})}{e^{jx} + e^{-jx}} \\ &= -j \cdot \operatorname{tanh}(jx) \end{align}

       where :math:`\operatorname{tanh}` is the hyperbolic tangent.

    Parameters
    ----------
    x: array
        input array whose elements are expressed in radians. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the tangent of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def tanh(x: array, /) -> array:
    r"""
    Calculates an implementation-dependent approximation to the hyperbolic tangent for each element ``x_i`` of the input array ``x``.

    The mathematical definition of the hyperbolic tangent is

    .. math::
       \begin{align} \operatorname{tanh}(x) &= \frac{\operatorname{sinh}(x)}{\operatorname{cosh}(x)} \\ &= \frac{e^x - e^{-x}}{e^x + e^{-x}} \end{align}

    where :math:`\operatorname{sinh}(x)` is the hyperbolic sine and :math:`\operatorname{cosh}(x)` is the hyperbolic cosine.

    **Special cases**

    .. note::
       For all operands, ``tanh(-x)`` must equal ``-tanh(x)``.

    For real-valued floating-point operands,

    - If ``x_i`` is ``NaN``, the result is ``NaN``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``+infinity``, the result is ``+1``.
    - If ``x_i`` is ``-infinity``, the result is ``-1``.

    For complex floating-point operands, let ``a = real(x_i)``, ``b = imag(x_i)``, and

    .. note::
       For complex floating-point operands, ``tanh(conj(x))`` must equal ``conj(tanh(x))``.

    - If ``a`` is ``+0`` and ``b`` is ``+0``, the result is ``+0 + 0j``.
    - If ``a`` is a nonzero finite number and ``b`` is ``+infinity``, the result is ``NaN + NaN j``.
    - If ``a`` is ``+0`` and ``b`` is ``+infinity``, the result is ``+0 + NaN j``.
    - If ``a`` is a nonzero finite number and ``b`` is ``NaN``, the result is ``NaN + NaN j``.
    - If ``a`` is ``+0`` and ``b`` is ``NaN``, the result is ``+0 + NaN j``.
    - If ``a`` is ``+infinity`` and ``b`` is a positive (i.e., greater than ``0``) finite number, the result is ``1 + 0j``.
    - If ``a`` is ``+infinity`` and ``b`` is ``+infinity``, the result is ``1 + 0j`` (sign of the imaginary component is unspecified).
    - If ``a`` is ``+infinity`` and ``b`` is ``NaN``, the result is ``1 + 0j`` (sign of the imaginary component is unspecified).
    - If ``a`` is ``NaN`` and ``b`` is ``+0``, the result is ``NaN + 0j``.
    - If ``a`` is ``NaN`` and ``b`` is a nonzero number, the result is ``NaN + NaN j``.
    - If ``a`` is ``NaN`` and ``b`` is ``NaN``, the result is ``NaN + NaN j``.

    .. warning::
       For historical reasons stemming from the C standard, array libraries may not return the expected result when ``a`` is ``+0`` and ``b`` is either ``+infinity`` or ``NaN``. The result should be ``+0 + NaN j`` in both cases; however, for libraries compiled against older C versions, the result may be ``NaN + NaN j``.

       Array libraries are not required to patch these older C versions, and, thus, users are advised that results may vary across array library implementations for these special cases.

    .. note::
       The hyperbolic tangent is an analytical function on the complex plane and has no branch cuts. The function is periodic, with period :math:`\pi j`, with respect to the imaginary component and has first order poles along the imaginary line at coordinates :math:`(0, \pi (\frac{1}{2} + n))`. However, IEEE 754 binary floating-point representation cannot represent :math:`\pi / 2` exactly, and, thus, no argument value is possible such that a pole error occurs.

    Parameters
    ----------
    x: array
        input array whose elements each represent a hyperbolic angle. Should have a floating-point data type.

    Returns
    -------
    out: array
        an array containing the hyperbolic tangent of each element in ``x``. The returned array must have a floating-point data type determined by :ref:`type-promotion`.
    """

def trunc(x: array, /) -> array:
    """
    Rounds each element ``x_i`` of the input array ``x`` to the integer-valued number that is closest to but no greater than ``x_i``.

    **Special cases**

    - If ``x_i`` is already integer-valued, the result is ``x_i``.

    For floating-point operands,

    - If ``x_i`` is ``+infinity``, the result is ``+infinity``.
    - If ``x_i`` is ``-infinity``, the result is ``-infinity``.
    - If ``x_i`` is ``+0``, the result is ``+0``.
    - If ``x_i`` is ``-0``, the result is ``-0``.
    - If ``x_i`` is ``NaN``, the result is ``NaN``.

    Parameters
    ----------
    x: array
        input array. Should have a real-valued data type.

    Returns
    -------
    out: array
        an array containing the rounded result for each element in ``x``. The returned array must have the same data type as ``x``.
    """

__all__ = ['abs', 'acos', 'acosh', 'add', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'bitwise_and', 'bitwise_left_shift', 'bitwise_invert', 'bitwise_or', 'bitwise_right_shift', 'bitwise_xor', 'ceil', 'conj', 'cos', 'cosh', 'divide', 'equal', 'exp', 'expm1', 'floor', 'floor_divide', 'greater', 'greater_equal', 'imag', 'isfinite', 'isinf', 'isnan', 'less', 'less_equal', 'log', 'log1p', 'log2', 'log10', 'logaddexp', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'multiply', 'negative', 'not_equal', 'positive', 'pow', 'real', 'remainder', 'round', 'sign', 'sin', 'sinh', 'square', 'sqrt', 'subtract', 'tan', 'tanh', 'trunc']
