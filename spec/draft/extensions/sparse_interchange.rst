.. _sparse_interchange:

Sparse interchange
==================

    Array API specification for sparse interchange functions.

Extension name and usage
------------------------

If implemented, this extension must be retrievable via::

    >>> if hasattr(x, 'sparse'):
    >>>     # Use the extension

.. currentmodule:: array_api

Objects in API
--------------

A conforming implementation of this extension must provide and support the following
functions/methods. In addition, the ``asarray`` method must also be able to convert
objects with supported formats which implement the protocol.

..
  NOTE: please keep the functions and their inverse together

.. currentmodule:: array_api.sparse

.. autosummary::
   :toctree: generated
   :template: method.rst

   from_binsparse

.. currentmodule:: array_api

.. autosummary::
   :toctree: generated
   :template: property.rst

   array.__binsparse__
   array.__binsparse_descriptor__
