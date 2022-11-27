.. _complex-number-ordering:

Complex Number Ordering
=======================

Given a set :math:`\{a_1, \ldots, a_n\}`, an order relation must satisfy the following properties:

1. For any :math:`a` in the set, :math:`a \leq a` (i.e., *reflexive*).
2. For any :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b` and :math:`b \leq c`, then :math:`a \leq c` (i.e., *transitive*).
3. For any :math:`a` and :math:`b` in the set, if :math:`a \leq b` and :math:`b \leq a`, then :math:`a = b` (i.e., *antisymmetric*).
4. For any :math:`a` and :math:`b` in the set, either :math:`a \leq b` or :math:`b \leq a` (or both) (i.e., in addition to a *partial order* established by 1-3, satisfies a *total order*).
5. For all :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b`, then :math:`a + c \leq b + c` (i.e., compatible with addition).
6. For all :math:`a`, :math:`b`, and :math:`c` in the set, if :math:`a \leq b` and :math:`0 \leq c`, then :math:`ac \leq bc` (i.e., compatible with multiplication).

Defining an order relation for complex numbers which satisfies all six properties defined above is not possible. Accordingly, this specification does not require that a conforming implementation of the array API standard adopt any specific complex number order relation.

In order to satisfy backward compatibility guarantees, conforming implementations of the array API standard may choose to define an order relation for complex numbers (e.g., lexicographic); however, consumers of the array API standard should **not** assume that complex number ordering is consistent between implementations or even supported.