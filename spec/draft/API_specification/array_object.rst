.. _array-object:

Array object
============

    Array API specification for array object attributes and methods.

A conforming implementation of the array API standard must provide and support an array object having the following attributes and methods.

Furthermore, a conforming implementation of the array API standard must support, at minimum, array objects of rank (i.e., number of dimensions) ``0``, ``1``, ``2``, ``3``, and ``4`` and must explicitly document their maximum supported rank ``N``.

.. note::
    Conforming implementations must support zero-dimensional arrays.

    Apart from array object attributes, such as ``ndim``, ``device``, and ``dtype``, all operations in this standard return arrays (or tuples of arrays), including those operations, such as ``mean``, ``var``, and ``std``, from which some common array libraries (e.g., NumPy) return scalar values.

    *Rationale: always returning arrays is necessary to (1) support accelerator libraries where non-array return values could force device synchronization and (2) support delayed execution models where an array represents a future value.*

-------------------------------------------------

.. _operators:

Operators
---------

A conforming implementation of the array API standard must provide and support an array object supporting the following Python operators.

Arithmetic Operators
~~~~~~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following Python arithmetic operators.

-   ``+x``: :meth:`.Array.__pos__`

    -   `operator.pos(x) <https://docs.python.org/3/library/operator.html#operator.pos>`_
    -   `operator.__pos__(x) <https://docs.python.org/3/library/operator.html#operator.__pos__>`_

-   `-x`: :meth:`.Array.__neg__`

    -   `operator.neg(x) <https://docs.python.org/3/library/operator.html#operator.neg>`_
    -   `operator.__neg__(x) <https://docs.python.org/3/library/operator.html#operator.__neg__>`_

-   `x1 + x2`: :meth:`.Array.__add__`

    -   `operator.add(x1, x2) <https://docs.python.org/3/library/operator.html#operator.add>`_
    -   `operator.__add__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__add__>`_

-   `x1 - x2`: :meth:`.Array.__sub__`

    -   `operator.sub(x1, x2) <https://docs.python.org/3/library/operator.html#operator.sub>`_
    -   `operator.__sub__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__sub__>`_

-   `x1 * x2`: :meth:`.Array.__mul__`

    -   `operator.mul(x1, x2) <https://docs.python.org/3/library/operator.html#operator.mul>`_
    -   `operator.__mul__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__mul__>`_

-   `x1 / x2`: :meth:`.Array.__truediv__`

    -   `operator.truediv(x1,x2) <https://docs.python.org/3/library/operator.html#operator.truediv>`_
    -   `operator.__truediv__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__truediv__>`_

-   `x1 // x2`: :meth:`.Array.__floordiv__`

    -   `operator.floordiv(x1, x2) <https://docs.python.org/3/library/operator.html#operator.floordiv>`_
    -   `operator.__floordiv__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__floordiv__>`_

-   `x1 % x2`: :meth:`.Array.__mod__`

    -   `operator.mod(x1, x2) <https://docs.python.org/3/library/operator.html#operator.mod>`_
    -   `operator.__mod__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__mod__>`_

-   `x1 ** x2`: :meth:`.Array.__pow__`

    -   `operator.pow(x1, x2) <https://docs.python.org/3/library/operator.html#operator.pow>`_
    -   `operator.__pow__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__pow__>`_

Arithmetic operators should be defined for arrays having real-valued data types.

Array Operators
~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following Python array operators.

-   `x1 @ x2`: :meth:`.Array.__matmul__`

    -   `operator.matmul(x1, x2) <https://docs.python.org/3/library/operator.html#operator.matmul>`_
    -   `operator.__matmul__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__matmul__>`_

The matmul ``@`` operator should be defined for arrays having real-valued data types.

Bitwise Operators
~~~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following Python bitwise operators.

-   `~x`: :meth:`.Array.__invert__`

    -   `operator.inv(x) <https://docs.python.org/3/library/operator.html#operator.inv>`_
    -   `operator.invert(x) <https://docs.python.org/3/library/operator.html#operator.invert>`_
    -   `operator.__inv__(x) <https://docs.python.org/3/library/operator.html#operator.__inv__>`_
    -   `operator.__invert__(x) <https://docs.python.org/3/library/operator.html#operator.__invert__>`_

-   `x1 & x2`: :meth:`.Array.__and__`

    -   `operator.and(x1, x2) <https://docs.python.org/3/library/operator.html#operator.and>`_
    -   `operator.__and__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__and__>`_

-   `x1 | x2`: :meth:`.Array.__or__`

    -   `operator.or(x1, x2) <https://docs.python.org/3/library/operator.html#operator.or>`_
    -   `operator.__or__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__or__>`_

-   `x1 ^ x2`: :meth:`.Array.__xor__`

    -   `operator.xor(x1, x2) <https://docs.python.org/3/library/operator.html#operator.xor>`_
    -   `operator.__xor__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__xor__>`_

-   `x1 << x2`: :meth:`.Array.__lshift__`

    -   `operator.lshift(x1, x2) <https://docs.python.org/3/library/operator.html#operator.lshift>`_
    -   `operator.__lshift__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__lshift__>`_

-   `x1 >> x2`: :meth:`.Array.__rshift__`

    -   `operator.rshift(x1, x2) <https://docs.python.org/3/library/operator.html#operator.rshift>`_
    -   `operator.__rshift__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__rshift__>`_

Bitwise operators should be defined for arrays having integer and boolean data types.

Comparison Operators
~~~~~~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following Python comparison operators.

-   `x1 < x2`: :meth:`.Array.__lt__`

    -   `operator.lt(x1, x2) <https://docs.python.org/3/library/operator.html#operator.lt>`_
    -   `operator.__lt__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__lt__>`_

-   `x1 <= x2`: :meth:`.Array.__le__`

    -   `operator.le(x1, x2) <https://docs.python.org/3/library/operator.html#operator.le>`_
    -   `operator.__le__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__le__>`_

-   `x1 > x2`: :meth:`.Array.__gt__`

    -   `operator.gt(x1, x2) <https://docs.python.org/3/library/operator.html#operator.gt>`_
    -   `operator.__gt__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__gt__>`_

-   `x1 >= x2`: :meth:`.Array.__ge__`

    -   `operator.ge(x1, x2) <https://docs.python.org/3/library/operator.html#operator.ge>`_
    -   `operator.__ge__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__ge__>`_

-   `x1 == x2`: :meth:`.Array.__eq__`

    -   `operator.eq(x1, x2) <https://docs.python.org/3/library/operator.html#operator.eq>`_
    -   `operator.__eq__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__eq__>`_

-   `x1 != x2`: :meth:`.Array.__ne__`

    -   `operator.ne(x1, x2) <https://docs.python.org/3/library/operator.html#operator.ne>`_
    -   `operator.__ne__(x1, x2) <https://docs.python.org/3/library/operator.html#operator.__ne__>`_

:meth:`.Array.__lt__`, :meth:`.Array.__le__`, :meth:`.Array.__gt__`, :meth:`.Array.__ge__` are only defined for arrays having real-valued data types. Other comparison operators should be defined for arrays having any data type.
For backward compatibility, conforming implementations may support complex numbers; however, inequality comparison of complex numbers is unspecified and thus implementation-dependent (see :ref:`complex-number-ordering`).

In-place Operators
~~~~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following in-place Python operators.

An in-place operation must not change the data type or shape of the in-place array as a result of :ref:`type-promotion` or :ref:`broadcasting`.

An in-place operation must have the same behavior (including special cases) as its respective binary (i.e., two operand, non-assignment) operation. For example, after in-place addition ``x1 += x2``, the modified array ``x1`` must always equal the result of the equivalent binary arithmetic operation ``x1 = x1 + x2``.

.. note::
    In-place operators must be supported as discussed in :ref:`copyview-mutability`.

Arithmetic Operators
""""""""""""""""""""

-   ``+=``. May be implemented via ``__iadd__``.
-   ``-=``. May be implemented via ``__isub__``.
-   ``*=``. May be implemented via ``__imul__``.
-   ``/=``. May be implemented via ``__itruediv__``.
-   ``//=``. May be implemented via ``__ifloordiv__``.
-   ``**=``. May be implemented via ``__ipow__``.
-   ``%=``. May be implemented via ``__imod__``.

Array Operators
"""""""""""""""

-   ``@=``. May be implemented via ``__imatmul__``.

Bitwise Operators
"""""""""""""""""

-   ``&=``. May be implemented via ``__iand__``.
-   ``|=``. May be implemented via ``__ior__``.
-   ``^=``. May be implemented via ``__ixor__``.
-   ``<<=``. May be implemented via ``__ilshift__``.
-   ``>>=``. May be implemented via ``__irshift__``.

Reflected Operators
~~~~~~~~~~~~~~~~~~~

A conforming implementation of the array API standard must provide and support an array object supporting the following reflected operators.

The results of applying reflected operators must match their non-reflected equivalents.

.. note::
    All operators for which ``array <op> scalar`` is implemented must have an equivalent reflected operator implementation.

Arithmetic Operators
""""""""""""""""""""

-   ``__radd__``
-   ``__rsub__``
-   ``__rmul__``
-   ``__rtruediv__``
-   ``__rfloordiv__``
-   ``__rpow__``
-   ``__rmod__``

Array Operators
"""""""""""""""

-   ``__rmatmul__``

Bitwise Operators
"""""""""""""""""

-   ``__rand__``
-   ``__ror__``
-   ``__rxor__``
-   ``__rlshift__``
-   ``__rrshift__``

-------------------------------------------------

.. currentmodule:: array_api

Attributes
----------
..
  NOTE: please keep the attributes in alphabetical order


.. autosummary::
   :toctree: generated
   :template: property.rst

   Array.dtype
   Array.device
   Array.mT
   Array.ndim
   Array.shape
   Array.size
   Array.T

-------------------------------------------------

Methods
-------
..
  NOTE: please keep the methods in alphabetical order


.. autosummary::
   :toctree: generated
   :template: property.rst

   Array.__abs__
   Array.__add__
   Array.__and__
   Array.__array_namespace__
   Array.__bool__
   Array.__complex__
   Array.__dlpack__
   Array.__dlpack_device__
   Array.__eq__
   Array.__float__
   Array.__floordiv__
   Array.__ge__
   Array.__getitem__
   Array.__gt__
   Array.__index__
   Array.__int__
   Array.__invert__
   Array.__le__
   Array.__lshift__
   Array.__lt__
   Array.__matmul__
   Array.__mod__
   Array.__mul__
   Array.__ne__
   Array.__neg__
   Array.__or__
   Array.__pos__
   Array.__pow__
   Array.__rshift__
   Array.__setitem__
   Array.__sub__
   Array.__truediv__
   Array.__xor__
   Array.to_device
