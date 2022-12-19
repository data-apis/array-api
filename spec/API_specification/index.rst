.. _api-specification:

API specification
=================

A conforming implementation of the array API standard must provide and support the APIs and behavior detailed in this specification while adhering to the following conventions.

-   When a function signature includes a `/`, positional parameters must be `positional-only <https://www.python.org/dev/peps/pep-0570/>`_ parameters. See :ref:`function-and-method-signatures`.
-   When a function signature includes a `*`, optional parameters must be `keyword-only <https://www.python.org/dev/peps/pep-3102/>`_ arguments. See :ref:`function-and-method-signatures`.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, functions must support the data types defined in :ref:`data-types`.
-   Functions may only be required for a subset of input data types. Libraries may choose to implement functions for additional data types, but that behavior is not required by the specification. See :ref:`data-type-categories`.
-   Unless stated otherwise, functions must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.
-   Unless stated otherwise, element-wise mathematical functions must satisfy the minimum accuracy requirements defined in :ref:`accuracy`.


.. toctree::
   :caption: API specification
   :maxdepth: 3

   array_object
   broadcasting
   constants
   creation_functions
   data_type_functions
   data_types
   elementwise_functions
   function_and_method_signatures
   indexing
   indexing_functions
   linear_algebra_functions
   manipulation_functions
   searching_functions
   set_functions
   sorting_functions
   statistical_functions
   type_promotion
   utility_functions
   version
