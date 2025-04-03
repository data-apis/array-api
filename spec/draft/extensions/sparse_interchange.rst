.. _sparse_interchange:

Sparse interchange
==================

    Array API specification for sparse interchange functions.

Extension name and usage
------------------------

If implemented, this extension must be retrievable via::

    >>> if hasattr(x, 'sparse'):
    >>>     # Use the extension

Objects in API
--------------

A conforming implementation of this extension must provide and support the following
functions/methods.

.. currentmodule:: array_api

..
  NOTE: please keep the functions and their inverse together

.. autosummary::
   :toctree: generated
   :template: method.rst

   sparse.from_binsparse


.. autosummary::
   :toctree: generated
   :template: property.rst

   array.__binsparse__
   array.__binsparse_descriptor__
