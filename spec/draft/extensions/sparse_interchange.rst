.. _sparse_interchange:

Sparse interchange
==================

    Array API specification for sparse interchange functions using `binsparse <https://graphblas.org/binsparse-specification/>`_.

Extension name and usage
------------------------

If implemented, this extension must be retrievable via::

    >>> xp = x.__array_namespace__()
    >>> if hasattr(xp, 'sparse'):
    >>>     # Use the extension

To convert an object from another library supporting also supporting the sparse interchange extension::

    >>> xp1 = xp1.sparse.from_binsparse(xp2_array)  # Convert with the same formats
    >>> xp1 = xp1.sparse.from_binsparse(xp2_array, descriptor=binsparse_descriptor)

.. _binsparse_descriptor_examples:

Examples of binsparse descriptors
---------------------------------

While the `binsparse specification <https://graphblas.org/binsparse-specification/>`_ uses JSON for its descriptor,
we will work with equivalent Python objects instead. Here are some examples of binsparse descriptors::

    >>> coo_2d_descriptor = {
        "binsparse": {
          "version": "0.1",
          "format": "COOR",
          "shape": [10, 12],
          "number_of_stored_values": 20,
          "data_types": {
            "indices_0": "uint64",
            "indices_1": "uint64",
            "values": "float32",
          },
        },
        "original_source": f"{library_name!s}, version {library_version!s}",
    }
    >>> csr_2d_descriptor = {
        "binsparse": {
          "version": "0.1",
          "format": "CSR",
          "shape": [20, 24],
          "number_of_stored_values": 20,
          "data_types": {
            "pointers_to_1": "uint64",
            "indices_1": "uint64",
            "values": "float32",
          },
        },
        "original_source": f"{library_name!s}, version {library_version!s}",
    }
    >>> compressed_vector_descriptor = {
        "binsparse": {
          "version": "0.1",
          "format": "CVEC",
          "shape": [30],
          "number_of_stored_values": 3,
          "data_types": {
            "indices_0": "uint64",
            "values": "float32",
          },
        },
        "original_source": f"{library_name!s}, version {library_version!s}",
    }

Objects in API
--------------

.. currentmodule:: array_api

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
