Sorting Functions
=================

  Array API specification for sorting functions.

A conforming implementation of the array API standard must provide and support the following functions.


.. note::

  For floating-point input arrays, the sort order of NaNs and signed zeros is unspecified and thus implementation-dependent.

  Implementations may choose to sort signed zeros (``-0 < +0``) or may choose to rely solely on value equality (``==``).

  Implementations may choose to sort NaNs (e.g., to the end or to the beginning of a returned array) or leave them in-place. Should an implementation sort NaNs, the sorting convention should be clearly documented in the conforming implementation's documentation.

  While defining a sort order for IEEE 754 floating-point numbers is recommended in order to facilitate reproducible and consistent sort results, doing so is not currently required by this specification.

.. currentmodule:: array_api

Objects in API
--------------
..
  NOTE: please keep the functions in alphabetical order

.. autosummary::
   :toctree: generated
   :template: method.rst

   argsort
   sort
