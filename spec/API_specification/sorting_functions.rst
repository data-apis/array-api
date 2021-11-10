Sorting Functions
=================

  Array API specification for sorting functions.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

* Positional parameters must be `positional-only <https://www.python.org/dev/peps/pep-0570/>`_ parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
* Optional parameters must be `keyword-only <https://www.python.org/dev/peps/pep-3102/>`_ arguments.
* Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.

.. note::

  For floating-point input arrays, the sort order of NaNs and signed zeros is unspecified and thus implementation-dependent.

  Implementations may choose to sort signed zeros (``-0 < +0``) or may choose to rely solely on value equality (``==``).

  Implementations may choose to sort NaNs (e.g., to the end or to the beginning of a returned array) or leave them in-place. Should an implementation sort NaNs, the sorting convention should be clearly documented in the conforming implementation's documentation.

  While defining a sort order for IEEE 754 floating-point numbers is recommended in order to facilitate reproducible and consistent sort results, doing so is not currently required by this specification.

Objects in API
--------------

..
  NOTE: please keep the functions in alphabetical order

.. _function-argsort:

argsort(x, /, *, axis=-1, descending=False, stable=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the indices that sort an array ``x`` along a specified axis.

**Parameters**

* **x**: *<array>*
   * input array.

* **axis**: *int*
   * axis along which to sort. If set to ``-1``, the function must sort along the last axis. Default: ``-1``.

* **descending**: *bool*
   * sort order. If ``True``, the returned indices sort ``x`` in descending order (by value). If ``False``, the returned indices sort ``x`` in ascending order (by value). Default: ``False``.

* **stable**: *bool*
   * sort stability. If ``True``, the returned indices must maintain the relative order of ``x`` values which compare as equal. If ``False``, the returned indices may or may not maintain the relative order of ``x`` values which compare as equal (i.e., the relative order of ``x`` values which compare as equal is implementation-dependent). Default: ``True``.

**Returns**

* **out**: *<array>*
   * an array of indices. The returned array must have the same shape as ``x``. The returned array must have the default array index data type.

.. _function-sort:

sort(x, /, *, axis=-1, descending=False, stable=True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a sorted copy of an input array ``x``.

**Parameters**

* **x**: *<array>*
   * input array.

* **axis**: *int*
   * axis along which to sort. If set to ``-1``, the function must sort along the last axis. Default: ``-1``.

* **descending**: *bool*
   * sort order. If ``True``, the array must be sorted in descending order (by value). If ``False``, the array must be sorted in ascending order (by value). Default: ``False``.

* **stable**: *bool*
   * sort stability. If ``True``, the returned array must maintain the relative order of ``x`` values which compare as equal. If ``False``, the returned array may or may not maintain the relative order of ``x`` values which compare as equal (i.e., the relative order of ``x`` values which compare as equal is implementation-dependent). Default: ``True``.

**Returns**

* **out**: *<array>*
   * a sorted array. The returned array must have the same data type and shape as ``x``.
