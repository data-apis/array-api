.. _branch-cuts:

Branch Cuts
===========

In the mathematical field of complex analysis, a **branch cut** is a curve in the complex plane across which an analytic multi-valued function is discontinuous. Branch cuts are often taken as lines or line segments, and the choice of any particular branch cut is a matter of convention.

For example, consider the function :math:`z^2` which maps a complex number :math:`z` to a well-defined number :math:`z^2`. The function's inverse function :math:`\sqrt{z}` does not, however, map to a single value. For example, for :math:`z = 1`, :math:`\sqrt{1} = \pm 1`. While one can choose a unique principal value for this and similar functions (e.g., in this case, the principal square root is :math:`+1`), choices cannot be made continuous over the whole complex plane, as lines of discontinuity must occur. To handle discontinuities, one commonly adopts branch cuts, which are not, in general, unique. Instead, one chooses a branch cut as a matter of convention in order to give simple analytic properties.

Branch cuts do not arise for single-valued trigonometric, hyperbolic, integer power, or exponential functions; however, branch cuts do arise for their multi-valued inverses.

In contrast to real-valued floating-point numbers which have well-defined behavior as specified in IEEE 754, complex-valued floating-point numbers have no equivalent specification. Accordingly, this specification chooses to follow C99 conventions for special cases and branch cuts for those functions supporting complex numbers. For those functions which do not have C99 equivalents (e.g., linear algebra APIs), the specification relies on dominant conventions among existing array libraries.

.. warning::
   All branch cuts documented in this specification are considered **provisional**. While conforming implementations of the array API standard should adopt the branch cuts described in this standard, consumers of array API standard implementations should **not** assume that branch cuts are consistent between implementations. 

   Provided no issues arise due to the choice of branch cut, the provisional status is likely to be removed in a future revision of this standard.