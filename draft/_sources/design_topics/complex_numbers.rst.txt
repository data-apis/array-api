.. _complex-numbers:

Complex Numbers
===============

The Complex Plane
-----------------

Mathematically, equality comparison between complex numbers depends on the choice of topology. For example, the complex plane has a continuum of infinities; however, when the complex plane is projected onto the surface of a sphere (a stereographic projection commonly referred to as the *Riemann sphere*), infinities coalesce into a single *point at infinity*, thus modeling the extended complex plane. For the former, the value :math:`\infty + 3j` is distinct from (i.e., does not equal) :math:`\infty + 4j`, while, for the latter, :math:`\infty + 3j` does equal :math:`\infty + 4j`.

Modeling complex numbers as a Riemann sphere conveys certain mathematical niceties (e.g., well-behaved division by zero and preservation of the identity :math:`\frac{1}{\frac{1}{z}} = z`); however, translating the model to IEEE 754 floating-point operations can lead to some unexpected results. For example, according to IEEE 754, :math:`+\infty` and :math:`-\infty` are distinct values; hence, for equality comparison, if :math:`x = +\infty` and :math:`y = -\infty`, then :math:`x \neq y`. In contrast, if we convert :math:`x` and :math:`y` to their complex number equivalents :math:`x = +\infty + 0j` and :math:`y = -\infty + 0j` and then interpret within the context of the extended complex plane, we arrive at the opposite result; namely, :math:`x = y`.

In short, given the constraints of floating-point arithmetic and the subtleties of signed zeros, infinities, NaNs, and their interaction, crafting a specification which always yields intuitive results and satisfies all use cases involving complex numbers is not possible. Instead, this specification attempts to follow precedent (e.g., C99, Python, Julia, NumPy, and elsewhere), while also minimizing surprise. The result is an imperfect balance in which certain APIs may appear to embrace the one-infinity model found in C/C++ for algebraic operations involving complex numbers (e.g., considering :math:`\infty + \operatorname{NaN}\ j` to be infinite, irrespective of the imaginary component's value, including NaN), while other APIs may rely on the complex plane with its multiplicity of infinities (e.g., in transcendental functions). Accordingly, consumers of this specification should expect that certain results involving complex numbers for one operation may not be wholly consistent with results involving complex numbers for another operation.


.. _branch-cuts:

Branch Cuts
-----------

In the mathematical field of complex analysis, a **branch cut** is a curve in the complex plane across which an analytic multi-valued function is discontinuous. Branch cuts are often taken as lines or line segments, and the choice of any particular branch cut is a matter of convention.

For example, consider the function :math:`z^2` which maps a complex number :math:`z` to a well-defined number :math:`z^2`. The function's inverse function :math:`\sqrt{z}` does not, however, map to a single value. For example, for :math:`z = 1`, :math:`\sqrt{1} = \pm 1`. While one can choose a unique principal value for this and similar functions (e.g., in this case, the principal square root is :math:`+1`), choices cannot be made continuous over the whole complex plane, as lines of discontinuity must occur. To handle discontinuities, one commonly adopts branch cuts, which are not, in general, unique. Instead, one chooses a branch cut as a matter of convention in order to give simple analytic properties.

Branch cuts do not arise for single-valued trigonometric, hyperbolic, integer power, or exponential functions; however, branch cuts do arise for their multi-valued inverses.

In contrast to real-valued floating-point numbers which have well-defined behavior as specified in IEEE 754, complex-valued floating-point numbers have no equivalent specification. Accordingly, this specification chooses to follow C99 conventions for special cases and branch cuts for those functions supporting complex numbers. For those functions which do not have C99 equivalents (e.g., linear algebra APIs), the specification relies on dominant conventions among existing array libraries.

.. warning::
   All branch cuts documented in this specification are considered **provisional**. While conforming implementations of the array API standard should adopt the branch cuts described in this standard, consumers of array API standard implementations should **not** assume that branch cuts are consistent between implementations. 

   Provided no issues arise due to the choice of branch cut, the provisional status is likely to be removed in a future revision of this standard.


.. _complex-number-ordering:

Complex Number Ordering
-----------------------

Given a set :math:`\{a_1, \ldots, a_n\}`, an order relation must satisfy the following properties:

1. **Reflexive**: for any :math:`a` in the set, :math:`a \leq a`.
2. **Transitive**: for any :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b` and :math:`b \leq c`, then :math:`a \leq c`.
3. **Antisymmetric**: for any :math:`a` and :math:`b` in the set, if :math:`a \leq b` and :math:`b \leq a`, then :math:`a = b`.
4. **Total Order**: in addition to the *partial order* established by 1-3, for any :math:`a` and :math:`b` in the set, either :math:`a \leq b` or :math:`b \leq a` (or both).
5. **Compatible with Addition**: for all :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b`, then :math:`a + c \leq b + c`.
6. **Compatible with Multiplication**: for all :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b` and :math:`0 \leq c`, then :math:`ac \leq bc`.

Defining an order relation for complex numbers which satisfies all six properties defined above is not possible. Accordingly, this specification does not require that a conforming implementation of the array API standard adopt any specific complex number order relation.

In order to satisfy backward compatibility guarantees, conforming implementations of the array API standard may choose to define an ordering for complex numbers (e.g., lexicographic); however, consumers of the array API standard should **not** assume that complex number ordering is consistent between implementations or even supported.

If a conforming implementation chooses to define an ordering for complex numbers, the ordering must be clearly documented.


Valued-based Promotion
----------------------

According to the type promotion rules described in this specification (see :ref:`type-promotion`), only the data types of the input arrays participating in an operation matter, not their values. The same principle applies to situations in which one or more results of operations on real-valued arrays are mathematically defined in the complex domain, but not in their real domain.

By convention, the principal square root of :math:`-1` is :math:`j`, where :math:`j` is the imaginary unit. Despite this convention, for those operations supporting type promotion, conforming implementations must only consider input array data types when determining the data type of the output array. For example, if a real-valued input array is provided to :func:`~array_api.sqrt`, the output array must also be real-valued, even if the input array contains negative values. Accordingly, if a consumer of a conforming implementation of this specification desires for an operation's results to include the complex domain, the consumer should first cast the input array(s) to an appropriate complex floating-point data type before performing the operation.