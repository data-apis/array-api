(data-dependent-output-shapes)=

# Data-dependent output shapes

Array libraries which build array computation graphs commonly employ static memory allocation techniques for performance optimization. In order to efficiently perform static memory allocation, such libraries must be able to infer array sizes during ahead-of-time (AOT) compilation. Functions and operations which are value-dependent present difficulties for such libraries, as array sizes cannot be inferred AOT without also knowing the contents of the respective arrays.

While value-dependent functions and operations are not impossible for array computation graph libraries to implement, this specification does not want to impose an undue burden on such libraries and permits omission of value-dependent operations. All other array libraries are expected, however, to implement the value-dependent operations included in this specification in order to be array specification compliant.

Value-dependent operations are demarcated in this specification using an admonition similar to the following:

:::{admonition} Data-dependent output shape
:class: important

The shape of the output array for this function/operation depends on the data values in the input array; hence, libraries that build array computation graphs (e.g., JAX, Dask, etc.) may find this function/operation difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See {ref}`data-dependent-output-shapes` section for more details.
:::