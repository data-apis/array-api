# Set Functions

> Array API specification for creating and operating on sets.

A conforming implementation of the array API standard must provide and support the following functions adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Unless stated otherwise, functions must support the data types defined in {ref}`data-types`.

## Objects in API

<!-- NOTE: please keep the functions in alphabetical order -->

(function-unique)=
### unique(x, /)

:::{admonition} Data-dependent output shape
:class: important

The shapes of one of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See {ref}`data-dependent-output-shapes` section for more details.
:::

Returns the unique elements of an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. If `x` has more than one dimension, the function must flatten `x` and return the unique elements of the flattened array.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt;, &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple `(values, indices, inverse_indices, counts)` whose

        -   first element must have the field name `values` and must be an array containing the unique elements of `x`.
        -   second element must have the field name `indices` and must be an array containing the indices (first occurrences) of `x` that result in `values`. The array must have the same shape as `values` and must have the default integer data type.
        -   third element must have the field name `inverse_indices` and must be an array containing the indices of `values` that reconstruct `x`. The array must have the same shape as `x` and must have the default integer data type.
        -   fourth element must have the field name `counts` and must be an array containing the number of times each unique element occurs in `x`. The returned array must have same shape as `x` and must have the default integer data type.

(function-unique-inverse)=
### unique_inverse(x, /)

Returns the unique elements of an input array `x` and the indices from the set of unique elements that reconstruct `x`.

:::{admonition} Data-dependent output shape
:class: important

The shape of one of the output arrays for this function depends on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See {ref}`data-dependent-output-shapes` section for more details.
:::

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. If `x` has more than one dimension, the function must flatten `x` and return the unique elements of the flattened array.

#### Returns

-   **out**: _Tuple\[ &lt;array&gt;, &lt;array&gt; ]_

    -   a namedtuple `(values, inverse_indices)` whose

        -   first element must have the field name `values` and must be an array containing the unique elements of `x`.
        -   second element must have the field name `inverse_indices` and must be an array containing the indices of `values` that reconstruct `x`. The array must have the same shape as `x` and have the default integer data type.

(function-unique-values)=
### unique_values(x, /)

:::{admonition} Data-dependent output shape
:class: important

The shape of the output array for this function depends on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) may find this function difficult to implement without knowing array values. Accordingly, such libraries may choose to omit this function. See {ref}`data-dependent-output-shapes` section for more details.
:::

Returns the unique elements of an input array `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   input array. If `x` has more than one dimension, the function must flatten `x` and return the unique elements of the flattened array.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the set of unique elements in `x`. The returned array must have the same data type as `x`.

        ```{note}
        The order of elements is not specified and may vary between implementations.
        ```