.. array-object:

# Array object

> Array API specification for array object attributes and methods.

A conforming implementation of the array API standard must provide and support an array object having the following attributes and methods adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a method accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in :ref:`broadcasting`.
-   Unless stated otherwise, methods must support the data types defined in :ref:`data-types`.
-   Unless stated otherwise, methods must adhere to the type promotion rules defined in :ref:`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

* * *

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

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where the number of dimensions may be dynamic._

### <a name="shape" href="#shape">#</a> shape

Array dimensions.

#### Returns

-   **out**: _Union\[ Tuple\[ int, ...], &lt;shape&gt; ]_

    -   array dimensions as either a tuple or a custom shape object. If a shape object, the object must be immutable and must support indexing for dimension retrieval.

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where a shape may be dynamic._

### <a name="size" href="#size">#</a> size

Number of elements in an array. This should equal the product of the array's dimensions.

#### Returns

-   **out**: _int_

    -   number of elements in an array.

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where the number of elements may be dynamic._

### <a name="T" href="#T">#</a> T

Transpose of the array.

#### Returns

-   **out**: _&lt;array&gt;_

    -   array whose dimensions (axes) are permuted in reverse order relative to original array. Must have the same data type as the original array.

* * *

## Methods

<!-- NOTE: please keep the methods in alphabetical order -->

### <a name="__abs__" href="#__abs__">#</a> \_\_abs\_\_(x, /)

Calculates the absolute value for each element `x_i` of an array instance `x` (i.e., the element-wise result has the same magnitude as the respective element in `x` but has positive sign).

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `-0`, the result is `+0`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise absolute value. Must have the same data type as `x`.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `abs`.

### <a name="__add__" href="#__add__">#</a> \_\_add\_\_(x1, x2, /)

Calculates the sum for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `-infinity`, the result is `NaN`.
-   If `x1_i` is `-infinity` and `x2_i` is `+infinity`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is finite, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is finite, the result is `-infinity`.
-   If `x1_i` is finite and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is finite and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `-0` and `x2_i` is `-0`, the result is `-0`.
-   If `x1_i` is `-0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `-0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is `+0` or `-0` and `x2_i` is a nonzero finite number, the result is `x2_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is `+0` or `-0`, the result is `x1_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is `-x1_i`, the result is `+0`.
-   In the remaining cases, when neither an `infinity`, `+0`, `-0`, nor a `NaN` is involved, and the operands have the same sign or have different magnitudes, the sum must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported round mode. If the magnitude is too large to represent, the operation overflows and the result is an `infinity` of appropriate sign.

.. note::

    Floating-point addition is a commutative operation, but not always associative.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance (augend array).

-   **x2**: _&lt;array&gt;_

    -   addend array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise sums.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `add`.

### <a name="__and__" href="#__and__">#</a> \_\_and\_\_(x1, x2, /)

Evaluates `x1_i & x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart

### <a name="__eq__" href="#__eq__">#</a> \_\_eq\_\_(x1, x2, /)

Computes the truth value of `x1_i == x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `equal`.

### <a name="__floordiv__" href="#__floordiv__">#</a> \_\_floordiv\_\_(x1, x2, /)

Evaluates `x1_i // x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: an element-wise counterpart API

### <a name="__ge__" href="#__ge__">#</a> \_\_ge\_\_(x1, x2, /)

Computes the truth value of `x1_i >= x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `greater_equal`.

### <a name="__getitem__" href="#__getitem__">#</a> \_\_getitem\_\_(x, key, /)

TODO

### <a name="__gt__" href="#__gt__">#</a> \_\_gt\_\_(x1, x2, /)

Computes the truth value of `x1_i > x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `greater`.

### <a name="__invert__" href="#__invert__">#</a> \_\_invert\_\_(x, /)

Evaluates `~x_i` for each element `x_i` of an array instance `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart (bitwise_not)

### <a name="__le__" href="#__le__">#</a> \_\_le\_\_(x1, x2, /)

Computes the truth value of `x1_i <= x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `less_equal`.

### <a name="__len__" href="#__len__">#</a> \_\_len\_\_(x, /)

TODO

### <a name="__lshift__" href="#__lshift__">#</a> \_\_lshift\_\_(x1, x2, /)

Evaluates `x1_i << x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart?

### <a name="__lt__" href="#__lt__">#</a> \_\_lt\_\_(x1, x2, /)

Computes the truth value of `x1_i < x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `less`.

### <a name="__mod__" href="#__mod__">#</a> \_\_mod\_\_(x1, x2, /)

Evaluates `x1_i % x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: an element-wise counterpart API

### <a name="__mul__" href="#__mul__">#</a> \_\_mul\_\_(x1, x2, /)

Calculates the product for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If both `x1_i` and `x2_i` have the same sign, the result is positive.
-   If `x1_i` and `x2_i` have different signs, the result is negative.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is either `+infinity` and `-infinity` with the sign determined by the rule already stated above.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is a finite nonzero value, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x1_i` is a finite nonzero value and `x2_i` is either `+infinity` or `-infinity`, the result is a signed infinity with the sign determined by the rule already stated above.
-   In the remaining cases, where neither an `infinity` nor `NaN` is involved, the product must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to represent, the result is an `infinity` of appropriate sign. If the magnitude is too small to represent, the result is a zero of appropriate sign.

.. note::

    Floating-point multiplication is not always associative due to finite precision.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise products.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `multiply`.

### <a name="__ne__" href="#__ne__">#</a> \_\_ne\_\_(x1, x2, /)

Computes the truth value of `x1_i != x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `not_equal`.

### <a name="__neg__" href="#__neg__">#</a> \_\_neg\_\_(x, /)

Evaluates `-x_i` for each element `x_i` of an array instance `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (numpy.negative)

### <a name="__or__" href="#__or__">#</a> \_\_or\_\_(x1, x2, /)

Evaluates `x1_i | x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (bitwise_or)

### <a name="__pos__" href="#__pos__">#</a> \_\_pos\_\_(x, /)

Evaluates `+x_i` for each element `x_i` of an array instance `x`.

#### Parameters

-   **x**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (numpy.positive)

### <a name="__pow__" href="#__pow__">#</a> \_\_pow\_\_(x1, x2, /)

Calculates an implementation-dependent approximation of exponentiation by raising each element `x1_i` (the base) of an array instance `x1` to the power of `x2_i` (the exponent), where `x2_i` is the corresponding element of the array `x2`.

-   If `x1_i` is not equal to `1` and `x2_i` is `NaN`, the result is `NaN`.
-   If `x2_i` is `+0`, the result is `1`, even if `x1_i` is `NaN`.
-   If `x2_i` is `-0`, the result is `1`, even if `x1_i` is `NaN`.
-   If `x1_i` is `NaN` and `x2_i` is nonzero, the result is `NaN`.
-   If `abs(x1_i)` is greater than `1` and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `abs(x1_i)` is greater than `1` and `x2_i` is `-infinity`, the result is `+0`.
-   If `abs(x1_i)` is `1` and `x2_i` is `+infinity`, the result is `1`.
-   If `abs(x1_i)` is `1` and `x2_i` is `-infinity`, the result is `1`.
-   If `x1_i` is `1` and `x2_i` is not `NaN`, the result is `1`.
-   If `abs(x1_i)` is less than `1` and `x2_i` is `+infinity`, the result is `+0`.
-   If `abs(x1_i)` is less than `1` and `x2_i` is `-infinity`, the result is `+infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is greater than `0`, the result is `+infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is less than `0`, the result is `+0`.
-   If `x1_i` is `-infinity` and `x2_i` is greater than `0`, the result is `-infinity`.
-   If `x1_i` is `-infinity`, `x2_i` is greater than `0`, and `x2_i` is not an odd integer value, the result is `+infinity`.
-   If `x1_i` is `-infinity`, `x2_i` is less than `0`, and `x2_i` is an odd integer value, the result is `-0`.
-   If `x1_i` is `-infinity`, `x2_i` is less than `0`, and `x2_i` is not an odd integer value, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is greater than `0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is less than `0`, the result is `+infinity`.
-   If `x1_i` is `-0`, `x2_i` is greater than `0`, and `x2_i` is an odd integer value, the result is `-0`.
-   If `x1_i` is `-0`, `x2_i` is greater than `0`, and `x2_i` is not an odd integer value, the result is `+0`.
-   If `x1_i` is `-0`, `x2_i` is less than `0`, and `x2_i` is an odd integer value, the result is `-infinity`.
-   If `x1_i` is `-0`, `x2_i` is less than `0`, and `x2_i` is not an odd integer value, the result is `+infinity`.
-   If `x1_i` is less than `0`, `x1_i` is finite, `x2_i` is finite, and `x2_i` is not an integer value, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance whose elements correspond to the exponentiation base.

-   **x2**: _&lt;array&gt;_

    -   other array whose elements correspond to the exponentiation exponent. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `pow`.

### <a name="__radd__" href="#__radd__">#</a> \_\_radd\_\_(x1, x2, /)

Calculates the sum for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `-infinity`, the result is `NaN`.
-   If `x1_i` is `-infinity` and `x2_i` is `+infinity`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is finite, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is finite, the result is `-infinity`.
-   If `x1_i` is finite and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is finite and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `-0` and `x2_i` is `-0`, the result is `-0`.
-   If `x1_i` is `-0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `-0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is `+0` or `-0` and `x2_i` is a nonzero finite number, the result is `x2_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is `+0` or `-0`, the result is `x1_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is `-x1_i`, the result is `+0`.
-   In the remaining cases, when neither an `infinity`, `+0`, `-0`, nor a `NaN` is involved, and the operands have the same sign or have different magnitudes, the sum must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported round mode. If the magnitude is too large to represent, the operation overflows and the result is an `infinity` of appropriate sign.

.. note::

    Floating-point addition is a commutative operation, but not always associative.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance (addend array).

-   **x2**: _&lt;array&gt;_

    -   augend array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise sums.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `add`.

### <a name="__rand__" href="#__rand__">#</a> \_\_rand\_\_(x1, x2, /)

Evaluates `x2_i & x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: link to functional equivalent

### <a name="__rfloordiv__" href="#__rfloordiv__">#</a> \_\_rfloordiv\_\_(x1, x2, /)

Evaluates `x2_i // x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: an element-wise counterpart API

### <a name="__rlshift__" href="#__rlshift__">#</a> \_\_rlshift\_\_(x1, x2, /)

Evaluates `x2_i << x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart?

### <a name="__rmod__" href="#__rmod__">#</a> \_\_rmod\_\_(x1, x2, /)

Evaluates `x2_i % x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: an element-wise counterpart API

### <a name="__rmul__" href="#__rmul__">#</a> \_\_rmul\_\_(x1, x2, /)

Calculates the product for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If both `x1_i` and `x2_i` have the same sign, the result is positive.
-   If `x1_i` and `x2_i` have different signs, the result is negative.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is either `+infinity` and `-infinity` with the sign determined by the rule already stated above.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is a finite nonzero value, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x1_i` is a finite nonzero value and `x2_i` is either `+infinity` or `-infinity`, the result is a signed infinity with the sign determined by the rule already stated above.
-   In the remaining cases, where neither an `infinity` nor `NaN` is involved, the product must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to represent, the result is an `infinity` of appropriate sign. If the magnitude is too small to represent, the result is a zero of appropriate sign.

.. note::

    Floating-point multiplication is not always associative due to finite precision.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise products.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `multiply`.

### <a name="__ror__" href="#__ror__">#</a> \_\_ror\_\_(x1, x2, /)

Evaluates `x2_i | x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (bitwise_or)

### <a name="__rpow__" href="#__rpow__">#</a> \_\_rpow\_\_(x1, x2, /)

Calculates an implementation-dependent approximation of exponentiation by raising each element `x2_i` (the base) of an array `x2` to the power of `x1_i` (the exponent), where `x1_i` is the corresponding element of the array instance `x1`.

-   If `x2_i` is not equal to `1` and `x1_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is `+0`, the result is `1`, even if `x2_i` is `NaN`.
-   If `x1_i` is `-0`, the result is `1`, even if `x2_i` is `NaN`.
-   If `x2_i` is `NaN` and `x1_i` is nonzero, the result is `NaN`.
-   If `abs(x2_i)` is greater than `1` and `x1_i` is `+infinity`, the result is `+infinity`.
-   If `abs(x2_i)` is greater than `1` and `x1_i` is `-infinity`, the result is `+0`.
-   If `abs(x2_i)` is `1` and `x1_i` is `+infinity`, the result is `1`.
-   If `abs(x2_i)` is `1` and `x1_i` is `-infinity`, the result is `1`.
-   If `x2_i` is `1` and `x1_i` is not `NaN`, the result is `1`.
-   If `abs(x2_i)` is less than `1` and `x1_i` is `+infinity`, the result is `+0`.
-   If `abs(x2_i)` is less than `1` and `x1_i` is `-infinity`, the result is `+infinity`.
-   If `x2_i` is `+infinity` and `x1_i` is greater than `0`, the result is `+infinity`.
-   If `x2_i` is `+infinity` and `x1_i` is less than `0`, the result is `+0`.
-   If `x2_i` is `-infinity` and `x1_i` is greater than `0`, the result is `-infinity`.
-   If `x2_i` is `-infinity`, `x1_i` is greater than `0`, and `x1_i` is not an odd integer value, the result is `+infinity`.
-   If `x2_i` is `-infinity`, `x1_i` is less than `0`, and `x1_i` is an odd integer value, the result is `-0`.
-   If `x2_i` is `-infinity`, `x1_i` is less than `0`, and `x1_i` is not an odd integer value, the result is `+0`.
-   If `x2_i` is `+0` and `x1_i` is greater than `0`, the result is `+0`.
-   If `x2_i` is `+0` and `x1_i` is less than `0`, the result is `+infinity`.
-   If `x2_i` is `-0`, `x1_i` is greater than `0`, and `x1_i` is an odd integer value, the result is `-0`.
-   If `x2_i` is `-0`, `x1_i` is greater than `0`, and `x1_i` is not an odd integer value, the result is `+0`.
-   If `x2_i` is `-0`, `x1_i` is less than `0`, and `x1_i` is an odd integer value, the result is `-infinity`.
-   If `x2_i` is `-0`, `x1_i` is less than `0`, and `x1_i` is not an odd integer value, the result is `+infinity`.
-   If `x2_i` is less than `0`, `x2_i` is finite, `x1_i` is finite, and `x1_i` is not an integer value, the result is `NaN`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance whose elements correspond to the exponentiation exponent.

-   **x2**: _&lt;array&gt;_

    -   other array whose elements correspond to the exponentiation base. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `pow`.

### <a name="__rrshift__" href="#__rrshift__">#</a> \_\_rrshift\_\_(x1, x2, /)

Evaluates `x2_i >> x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart?

### <a name="__rshift__" href="#__rshift__">#</a> \_\_rshift\_\_(x1, x2, /)

Evaluates `x1_i >> x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart?

### <a name="__rsub__" href="#__rsub__">#</a> \_\_rsub\_\_(x1, x2, /)

Calculates the difference for each element `x2_i` of an array `x2` with the respective element `x1_i` of the array instance `x1`. The result of `x2_i - x1_i` **must** be the same as `x2_i + (-x1_i)` and is thus governed by the same floating-point rules as addition (see [`__radd__`][#__radd__]).

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance (subtrahend array).

-   **x2**: _&lt;array&gt;_

    -   minuend array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise differences.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `subtract`.

### <a name="__rtruediv__" href="#__rtruediv__">#</a> \_\_rtruediv\_\_(x1, x2, /)

Evaluates `x2_i / x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If both `x1_i` and `x2_i` has the same sign, the result is positive.
-   If `x1_i` and `x2_i` has different signs, the result is negative.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x2_i` is either `+infinity` or `-infinity` and `x1_i` is either `+0` or `-0`, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x2_i` is either `+infinity` or `-infinity` and `x1_i` is a finite nonzero value, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x2_i` is a finite value and `x1_i` is either `+infinity` or `-infinity`, the result is a signed zero with the sign determined by the rule already stated above.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x2_i` is either `+0` or `-0` and `x1_i` is a finite nonzero value, the result is a signed zero with the sign determined by the rule already stated above.
-   If `x2_i` is a nonzero finite value and `x1_i` is either `+0` or `-0`, the result is a signed infinity with the sign determined by the rule already stated above.
-   In the remaining cases, where neither an `-infinity`, `+0`, `-0`, or `NaN` is involved, the quotient must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too larger to represent, the operation overflows and the result is an `infinity` of appropriate sign. If the magnitude is too small to represent, the operation underflows and the result is a zero of appropriate sign.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance (divisor).

-   **x2**: _&lt;array&gt;_

    -   dividend array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `divide`.

### <a name="__rxor__" href="#__rxor__">#</a> \_\_rxor\_\_(x1, x2, /)

Evaluates `x2_i ^ x1_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (bitwise_or)

### <a name="__setitem__" href="#__setitem__">#</a> \_\_setitem\_\_(x, key, value, /)

TODO

### <a name="__sizeof__" href="#__sizeof__">#</a> \_\_sizeof\_\_(x, /)

TODO

### <a name="__sub__" href="#__sub__">#</a> \_\_sub\_\_(x1, x2, /)

Calculates the difference for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. The result of `x1_i - x2_i` **must** be the same as `x1_i + (-x2_i)` and is thus governed by the same floating-point rules as addition (see [`__add__`][#__add__]).

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance (minuend array).

-   **x2**: _&lt;array&gt;_

    -   subtrahend array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise differences.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `subtract`.

### <a name="__truediv__" href="#__truediv__">#</a> \_\_truediv\_\_(x1, x2, /)

Evaluates `x1_i / x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`. For floating-point arithmetic,

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If both `x1_i` and `x2_i` has the same sign, the result is positive.
-   If `x1_i` and `x2_i` has different signs, the result is negative.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+0` or `-0`, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is a finite nonzero value, the result is a signed infinity with the sign determined by the rule already stated above.
-   If `x1_i` is a finite value and `x2_i` is either `+infinity` or `-infinity`, the result is a signed zero with the sign determined by the rule already stated above.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is a finite nonzero value, the result is a signed zero with the sign determined by the rule already stated above.
-   If `x1_i` is a nonzero finite value and `x2_i` is either `+0` or `-0`, the result is a signed infinity with the sign determined by the rule already stated above.
-   In the remaining cases, where neither an `-infinity`, `+0`, `-0`, or `NaN` is involved, the quotient must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too larger to represent, the operation overflows and the result is an `infinity` of appropriate sign. If the magnitude is too small to represent, the operation underflows and the result is a zero of appropriate sign.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

.. note::

    Element-wise results should equal those of the equivalent element-wise function. TODO: link to function specification: `divide`.

### <a name="__xor__" href="#__xor__">#</a> \_\_xor\_\_(x1, x2, /)

Evaluates `x1_i ^ x2_i` for each element `x1_i` of an array instance `x1` with the respective element `x2_i` of the array `x2`.

#### Parameters

-   **x1**: _&lt;array&gt;_

    -   array instance.

-   **x2**: _&lt;array&gt;_

    -   other array. Must be compatible with `x1` (see :ref:`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results.

TODO: functional counterpart? (bitwise_xor)