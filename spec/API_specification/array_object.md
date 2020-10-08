# Array object

> Array API specification for array object attributes and methods.

A conforming implementation of the array API standard must provide and support an array object having the following attributes and methods adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a method accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, methods must support the data types defined in :ref:`data-types`.
-   Unless stated otherwise, methods must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

## Attributes

<!-- NOTE: please keep the attributes in alphabetical order -->

### <a name="dtype" href="#dtype">#</a> dtype

Data type of the array elements.

#### Returns

-   **out**: _&lt;dtype&gt;_

    -   array data type.

### <a name="ndim" href="#ndim">#</a> ndim

Number of array dimensions (axes).

#### Returns

-   **out**: _int_

    -   number of array dimensions (axes).

### <a name="shape" href="#shape">#</a> shape

Array dimensions.

#### Returns

-   **out**: _Union\[ Tuple\[ int, ...], &lt;shape&gt; ]_

    -   array dimensions as either a tuple or a custom shape object. If a shape object, the object must be immutable and must support indexing for dimension retrieval.

### <a name="size" href="#size">#</a> size

Number of elements in an array. This should equal the product of the array's dimensions.

#### Returns

-   **out**: _int_

    -   number of elements in an array.

### <a name="T" href="#T">#</a> T

Transpose of the array.

#### Returns

-   **out**: _&lt;array&gt;_

    -   array whose dimensions (axes) are permuted in reverse order relative to original array. Must have the same data type as the original array.

## Methods

<!-- NOTE: please keep the methods in alphabetical order -->
