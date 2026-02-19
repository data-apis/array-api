.. _inspection:

Inspection
==========

    Array API specification for namespace inspection utilities.

A conforming implementation of the array API standard must provide and support the following functions and associated inspection APIs.


Objects in API
--------------

.. currentmodule:: array_api.info

..
  NOTE: please keep the functions in alphabetical order

.. autosummary::
   :toctree: generated
   :template: method.rst

   __array_namespace_info__


Inspection APIs
---------------

In the namespace (or class) returned by ``__array_namespace_info__``, a conforming implementation of the array API standard must provide and support the following functions (or methods) for programmatically querying data type and device support, capabilities, and other specification-defined implementation-specific behavior, as documented in the functions described below.

..
  NOTE: please keep the functions in alphabetical order

.. autosummary::
   :toctree: generated
   :template: method.rst

   capabilities
   default_device
   default_dtypes
   devices
   dtypes
