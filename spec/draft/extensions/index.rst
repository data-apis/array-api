.. _extensions:

Extensions
==========

Extensions are coherent sets of functionality that are commonly implemented
across array libraries. Each array library supporting this standard may, but is
not required to, implement an extension. If an extension is supported, it
must be accessible inside the main array API supporting namespace as a separate
namespace.

Extension module implementors must aim to provide all functions and other
public objects in an extension. The rationale for this is that downstream usage
can then check whether or not the extension is present (using ``hasattr(xp,
'extension_name')`` should be enough), and can then assume that functions are
implemented. This in turn makes it also easy for array-consuming libraries to
document which array libraries they support - e.g., "all libraries implementing
the array API standard and its linear algebra extension".

The mechanism through which the extension namespace is made available is up to
the implementer, e.g. via a regular submodule that is imported under the
``linalg`` name, or via a module-level ``__getattr__``.

The functions in an extension must adhere to the same conventions as those in
the array API standard. See :ref:`api-specification`.


Extensions
----------

.. toctree::
   :maxdepth: 1

   fourier_transform_functions
   linear_algebra_functions
