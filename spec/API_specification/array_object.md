(array-object)=

# Array object

> Array API specification for array object attributes and methods.

A conforming implementation of the array API standard must provide and support an array object having the following attributes and methods adhering to the following conventions.

-   Positional parameters must be [positional-only](https://www.python.org/dev/peps/pep-0570/) parameters. Positional-only parameters have no externally-usable name. When a method accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
-   Optional parameters must be [keyword-only](https://www.python.org/dev/peps/pep-3102/) arguments.
-   Broadcasting semantics must follow the semantics defined in {ref}`broadcasting`.
-   Unless stated otherwise, methods must support the data types defined in {ref}`data-types`.
-   Unless stated otherwise, methods must adhere to the type promotion rules defined in {ref}`type-promotion`.
-   Unless stated otherwise, floating-point operations must adhere to IEEE 754-2019.

* * *

(operators)=

## Operators

A conforming implementation of the array API standard must provide and support an array object supporting the following Python operators:

-   `x1 < x2`: [`__lt__(x1, x2)`](#__lt__self-other-)

    -   [`operator.lt(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.lt)
    -   [`operator.__lt__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__lt__)

-   `x1 <= x2`: [`__le__(x1, x2)`](#__le__self-other-)

    -   [`operator.le(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.le)
    -   [`operator.__le__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__le__)

-   `x1 > x2`: [`__gt__(x1, x2)`](#__gt__self-other-)

    -   [`operator.gt(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.gt)
    -   [`operator.__gt__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__gt__)

-   `x1 >= x2`: [`__ge__(x1, x2)`](#__ge__self-other-)

    -   [`operator.ge(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.ge)
    -   [`operator.__ge__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__ge__)

-   `x1 == x2`: [`__eq__(x1, x2)`](#__eq__self-other-)

    -   [`operator.eq(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.eq)
    -   [`operator.__eq__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__eq__)

-   `x1 != x2`: [`__ne__(x1, x2)`](#__ne__self-other-)

    -   [`operator.ne(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.ne)
    -   [`operator.__ne__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__ne__)

-   `+x`: [`__pos__(x)`](#__pos__self-)

    -   [`operator.pos(x)`](https://docs.python.org/3/library/operator.html#operator.pos)
    -   [`operator.__pos__(x)`](https://docs.python.org/3/library/operator.html#operator.__pos__)

-   `-x`: [`__neg__(x)`](#__neg__self-)

    -   [`operator.neg(x)`](https://docs.python.org/3/library/operator.html#operator.neg)
    -   [`operator.__neg__(x)`](https://docs.python.org/3/library/operator.html#operator.__neg__)

-   `x1 + x2`: [`__add__(x1, x2)`](#__add__self-other-)

    -   [`operator.add(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.add)
    -   [`operator.__add__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__add__)

-   `x1 - x2`: [`__sub__(x1, x2)`](#__sub__self-other-)

    -   [`operator.sub(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.sub)
    -   [`operator.__sub__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__sub__)

-   `x1 * x2`: [`__mul__(x1, x2)`](#__mul__self-other-)

    -   [`operator.mul(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.mul)
    -   [`operator.__mul__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__mul__)

-   `x1 / x2`: [`__truediv__(x1, x2)`](#__truediv__self-other-)

    -   [`operator.truediv(x1,x2)`](https://docs.python.org/3/library/operator.html#operator.truediv)
    -   [`operator.__truediv__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__truediv__)

-   `x1 // x2`: [`__floordiv__(x1, x2)`](#__floordiv__self-other-)

    -   [`operator.floordiv(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.floordiv)
    -   [`operator.__floordiv__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__floordiv__)

-   `x1 % x2`: [`__mod__(x1, x2)`](#__mod__self-other-)

    -   [`operator.mod(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.mod)
    -   [`operator.__mod__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__mod__)

-   `x1 ** x2`: [`__pow__(x1, x2)`](#__pow__self-other-)

    -   [`operator.pow(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.pow)
    -   [`operator.__pow__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__pow__)

-   `x1 @ x2`: [`__matmul__(x1, x2)`](#__matmul__self-other-)

    -   [`operator.matmul(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.matmul)
    -   [`operator.__matmul__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__matmul__)

-   `~x`: [`__invert__(x)`](#__invert__self-)

    -   [`operator.inv(x)`](https://docs.python.org/3/library/operator.html#operator.inv)
    -   [`operator.invert(x)`](https://docs.python.org/3/library/operator.html#operator.invert)
    -   [`operator.__inv__(x)`](https://docs.python.org/3/library/operator.html#operator.__inv__)
    -   [`operator.__invert__(x)`](https://docs.python.org/3/library/operator.html#operator.__invert__)

-   `x1 & x2`: [`__and__(x1, x2)`](#__and__self-other-)

    -   [`operator.and(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.and)
    -   [`operator.__and__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__and__)

-   `x1 | x2`: [`__or__(x1, x2)`](#__or__self-other-)

    -   [`operator.or(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.or)
    -   [`operator.__or__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__or__)

-   `x1 ^ x2`: [`__xor__(x1, x2)`](#__xor__self-other-)

    -   [`operator.xor(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.xor)
    -   [`operator.__xor__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__xor__)

-   `x1 << x2`: [`__lshift__(x1, x2)`](#__lshift__self-other-)

    -   [`operator.lshift(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.lshift)
    -   [`operator.__lshift__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__lshift__)

-   `x1 >> x2`: [`__rshift__(x1, x2)`](#__rshift__self-other-)

    -   [`operator.rshift(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.rshift)
    -   [`operator.__rshift__(x1, x2)`](https://docs.python.org/3/library/operator.html#operator.__rshift__)


### In-place Operators

A conforming implementation of the array API standard must provide and support
an array object supporting the following in-place Python operators:

- `+=`. May be implemented via `__iadd__`.
- `-=`. May be implemented via `__isub__`.
- `*=`. May be implemented via `__imul__`.
- `/=`. May be implemented via `__itruediv__`.
- `//=`. May be implemented via `__ifloordiv__`.
- `**=`. May be implemented via `__ipow__`.
- `@=`. May be implemented via `__imatmul__`.
- `%=`. May be implemented via `__imod__`.
- `&=`. May be implemented via `__iand__`.
- `|=`. May be implemented via `__ior__`.
- `^=`. May be implemented via `__ixor__`.
- `<<=`. May be implemented via `__ilshift__`.
- `>>=`. May be implemented via `__irshift__`.

An in-place operation must not change the dtype or shape of the in-place array
as a result of {ref}`type-promotion` or {ref}`broadcasting`.

```{note}

In-place operators must be supported as discussed in {ref}`copyview-mutability`.
```

### Reflected Operators

A conforming implementation of the array API standard must provide and support
an array object supporting the following reflected operators:

- `__radd__`
- `__rsub__`
- `__rmul__`
- `__rtruediv__`
- `__rfloordiv__`
- `__rpow__`
- `__rmatmul__`
- `__rmod__`
- `__rand__`
- `__ror__`
- `__rxor__`
- `__rlshift__`
- `__rrshift__`

The results of applying reflected operators must match their non-reflected equivalents.

```{note}

All operators for which `array <op> scalar` is implemented must have an equivalent reflected operator implementation.
```

* * *

## Attributes

<!-- NOTE: please keep the attributes in alphabetical order -->

(attribute-dtype)=
### dtype

Data type of the array elements.

#### Returns

-   **out**: _&lt;dtype&gt;_

    -   array data type.

(attribute-device)=
### device

Hardware device the array data resides on.

#### Returns

-   **out**: _&lt;device&gt;_

    -   a `device` object (see {ref}`device-support`).

(attribute-ndim)=
### ndim

Number of array dimensions (axes).

#### Returns

-   **out**: _int_

    -   number of array dimensions (axes).

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where the number of dimensions may be dynamic._

(attribute-shape)=
### shape

Array dimensions.

#### Returns

-   **out**: _Union\[ Tuple\[ int, ...], &lt;shape&gt; ]_

    -   array dimensions as either a tuple or a custom shape object. If a shape object, the object must be immutable and must support indexing for dimension retrieval.

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where a shape may be dynamic._

(attribute-size)=
### size

Number of elements in an array. This must equal the product of the array's dimensions.

#### Returns

-   **out**: _int_

    -   number of elements in an array.

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where the number of elements may be dynamic._

(attribute-T)=
### T

Transpose of the array.

#### Returns

-   **out**: _&lt;array&gt;_

    -   array whose dimensions (axes) are permuted in reverse order relative to original array. The returned array must have the same data type as the original array.

* * *

## Methods

<!-- NOTE: please keep the methods in alphabetical order -->

(method-__abs__)=
### \_\_abs\_\_(self, /)

Calculates the absolute value for each element of an array instance (i.e., the element-wise result has the same magnitude as the respective element but has positive sign).

#### Special Cases

For floating-point operands, let `self` equal `x`.

-   If `x_i` is `NaN`, the result is `NaN`.
-   If `x_i` is `-0`, the result is `+0`.
-   If `x_i` is `-infinity`, the result is `+infinity`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise absolute value. The returned array must have the same data type as `self`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`abs(x)`](elementwise_functions.md#absx-).
```

(method-__add__)=
### \_\_add\_\_(self, other, /)

Calculates the sum for each element of an array instance with the respective element of the array `other`.

#### Special Cases

For floating-point operands, let `self` equal `x1` and `other` equal `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `-infinity`, the result is `NaN`.
-   If `x1_i` is `-infinity` and `x2_i` is `+infinity`, the result is `NaN`.
-   If `x1_i` is `+infinity` and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is a finite number, the result is `+infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is a finite number, the result is `-infinity`.
-   If `x1_i` is a finite number and `x2_i` is `+infinity`, the result is `+infinity`.
-   If `x1_i` is a finite number and `x2_i` is `-infinity`, the result is `-infinity`.
-   If `x1_i` is `-0` and `x2_i` is `-0`, the result is `-0`.
-   If `x1_i` is `-0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `-0`, the result is `+0`.
-   If `x1_i` is `+0` and `x2_i` is `+0`, the result is `+0`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is a nonzero finite number, the result is `x2_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is either `+0` or `-0`, the result is `x1_i`.
-   If `x1_i` is a nonzero finite number and `x2_i` is `-x1_i`, the result is `+0`.
-   In the remaining cases, when neither `infinity`, `+0`, `-0`, nor a `NaN` is involved, and the operands have the same mathematical sign or have different magnitudes, the sum must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported round mode. If the magnitude is too large to represent, the operation overflows and the result is an `infinity` of appropriate mathematical sign.

```{note}

Floating-point addition is a commutative operation, but not always associative.
```

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance (augend array).

-   **other**: _&lt;array&gt;_

    -   addend array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise sums. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`add(x1, x2)`](elementwise_functions.md#addx1-x2-).
```

(method-__and__)=
### \_\_and\_\_(self, other, /)

Evaluates `self_i & other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer or boolean data type.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`). Must have an integer or boolean data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`bitwise_and(x1, x2)`](elementwise_functions.md#logical_andx1-x2-).
```


(method-__array_namespace__)=
### \_\_array_namespace\_\_(self, /, *, api_version=None)

Returns an object that has all the array API functions on it.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **api_version**: _&lt;Optional\[str\]&gt;_

    -   string representing the version of the array API specification to be returned, in `'YYYY.MM'` form, for example, `'2020.10'`. If it is `None`, it should return the namespace corresponding to latest version of the array API specification.  If the given version is invalid or not implemented for the given module, an error should be raised. Default: `None`.

#### Returns

-   **out**: _&lt;object&gt;_

    -   an object representing the array API namespace. It should have every top-level function defined in the specification as an attribute. It may contain other public names as well, but it is recommended to only include those names that are part of the specification.


(method-__bool__)=
### \_\_bool\_\_(self, /)

Converts a zero-dimensional boolean array to a Python `bool` object.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   zero-dimensional array instance. Must have a boolean data type.

#### Returns

-   **out**: _&lt;bool&gt;_

    -   a Python `bool` object representing the single element of the array.


(method-__dlpack__)=
### \_\_dlpack\_\_(self, /, *, stream=None)

Exports the array for consumption by {ref}`function-from_dlpack` as a DLPack capsule.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **stream**: _Optional\[ int ]_

    -   a Python integer representing a pointer to a stream. `stream` is provided by the consumer to the producer to instruct the producer to ensure that operations can safely be performed on the array. The pointer must be a positive integer or `-1`. If `stream` is `-1`, the value may be used by the consumer to signal "producer must not perform any synchronization". Device-specific notes:

        :::{admonition} CUDA
        -   `None`: producer must assume the legacy default stream (default).
        -   `1`: the legacy default stream.
        -   `2`: the per-thread default stream.
        -   `> 2`: stream number represented as a Python integer.

        `0` is disallowed due to its ambiguity: `0` could mean either `None`, `1`, or `2`.
        :::

        :::{admonition} ROCm
        -   `None`: producer must assume the legacy default stream (default).
        -   `0`: the default stream.
        -   `> 2`: stream number represented as a Python integer.

        Using `1` and `2` is not supported.
        :::

        ```{tip}
        It is recommended that implementers explicitly handle streams. If
        they use the legacy default stream, specifying `1` (CUDA) or `0`
        (ROCm) is preferred. `None` is a safe default for developers who do
        not want to think about stream handling at all, potentially at the
        cost of more synchronization than necessary.
        ```

#### Returns

-   **capsule**: _&lt;PyCapsule&gt;_

    -   a DLPack capsule for the array. See {ref}`data-interchange` for details.


(method-__dlpack_device__)=
### \_\_dlpack\_device\_\_(self, /)

Returns device type and device ID in DLPack format. Meant for use within {ref}`function-from_dlpack`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **device**: _Tuple\[enum.IntEnum, int\]_

    -   a tuple `(device_type, device_id)` in DLPack format. Valid device type enum members are:

        ```
        CPU = 1
        CUDA = 2
        CPU_PINNED = 3
        OPENCL = 4
        VULKAN = 7
        METAL = 8
        VPI = 9
        ROCM = 10
        ```

(method-__eq__)=
### \_\_eq\_\_(self, other, /)

Computes the truth value of `self_i == other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`equal(x1, x2)`](elementwise_functions.md#equalx1-x2-).
```

(method-__float__)=
### \_\_float\_\_(self, /)

Converts a zero-dimensional floating-point array to a Python `float` object.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   zero-dimensional array instance. Must have a floating-point data type.

#### Returns

-   **out**: _&lt;float&gt;_

    -   a Python `float` object representing the single element of the array instance.

(method-__floordiv__)=
### \_\_floordiv\_\_(self, other, /)

Evaluates `self_i // other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`floor_divide(x1, x2)`](elementwise_functions.md#floor_dividex1-x2-).
```

(method-__ge__)=
### \_\_ge\_\_(self, other, /)

Computes the truth value of `self_i >= other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`greater_equal(x1, x2)`](elementwise_functions.md#greater_equalx1-x2-).
```

(method-__getitem__)=
### \_\_getitem\_\_(self, key, /)

Returns `self[key]`.

#### Parameters

-   **self**: _&lt;array;&gt;_

    -   array instance.

-   **key**: _Union\[ int, slice, ellipsis, Tuple\[ Union\[ int, slice, ellipsis ], ... ], &lt;array&gt; ]_

    -   index key.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the accessed value(s). The returned array must have the same data type as `self`.

(method-__gt__)=
### \_\_gt\_\_(self, other, /)

Computes the truth value of `self_i > other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`greater(x1, x2)`](elementwise_functions.md#greaterx1-x2-).
```

(method-__int__)=
### \_\_int\_\_(self, /)

Converts a zero-dimensional integer array to a Python `int` object.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   zero-dimensional array instance. Must have an integer data type.

#### Returns

-   **out**: _&lt;int&gt;_

    -   a Python `int` object representing the single element of the array instance.

(method-__invert__)=
### \_\_invert\_\_(self, /)

Evaluates `~self_i` for each element of an array instance.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer or boolean data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have the same data type as `self`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`bitwise_invert(x)`](elementwise_functions.md#bitwise_invertx-).
```

(method-__le__)=
### \_\_le\_\_(self, other, /)

Computes the truth value of `self_i <= other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`less_equal(x1, x2)`](elementwise_functions.md#less_equalx1-x2-).
```

(method-__len__)=
### \_\_len\_\_(self, /)

_TODO: need to more carefully consider this in order to accommodate, e.g., graph tensors where a shape may be dynamic. Furthermore, not clear whether this should be implemented, as, e.g., NumPy's behavior of returning the size of the first dimension is not necessarily intuitive, as opposed to, say, the total number of elements._

(method-__lshift__)=
### \_\_lshift\_\_(self, other, /)

Evaluates `self_i << other_i` for each element of an array instance with the respective element  of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer data type.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`). Must have an integer data type. Each element must be greater than or equal to `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have the same data type as `self`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`less_equal(x1, x2)`](elementwise_functions.md#bitwise_left_shiftx1-x2-).
```

(method-__lt__)=
### \_\_lt\_\_(self, other, /)

Computes the truth value of `self_i < other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`less(x1, x2)`](elementwise_functions.md#lessx1-x2-).
```

(method-__matmul__)=
### \_\_matmul\_\_(self, other, /)

_TODO: awaiting `matmul` functional equivalent._

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   _TODO_

(method-__mod__)=
### \_\_mod\_\_(self, other, /)

Evaluates `self_i % other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. Each element-wise result must have the same sign as the respective element `other_i`. The returned array must have a floating-point data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`remainder(x1, x2)`](elementwise_functions.md#remainderx1-x2-).
```

(method-__mul__)=
### \_\_mul\_\_(self, other, /)

Calculates the product for each element of an array instance with the respective element of the array `other`.

#### Special Cases

For floating-point operands, let `self` equal `x1` and `other` equal `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x1_i` and `x2_i` have the same mathematical sign, the result has a positive mathematical sign, unless the result is `NaN`. If the result is `NaN`, the "sign" of `NaN` is implementation-defined.
-   If `x1_i` and `x2_i` have different mathematical signs, the result has a negative mathematical sign, unless the result is `NaN`. If the result is `NaN`, the "sign" of `NaN` is implementation-defined.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is a nonzero finite number, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
-   If `x1_i` is a nonzero finite number and `x2_i` is either `+infinity` or `-infinity`, the result is a signed infinity with the mathematical sign determined by the rule already stated above.
-   In the remaining cases, where neither `infinity` nor `NaN` is involved, the product must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too large to represent, the result is an `infinity` of appropriate mathematical sign. If the magnitude is too small to represent, the result is a zero of appropriate mathematical sign.

```{note}

Floating-point multiplication is not always associative due to finite precision.
```

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise products. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`multiply(x1, x2)`](elementwise_functions.md#multiplyx1-x2-).
```

(method-__ne__)=
### \_\_ne\_\_(self, other, /)

Computes the truth value of `self_i != other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type of `bool` (i.e., must be a boolean array).

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`not_equal(x1, x2)`](elementwise_functions.md#not_equalx1-x2-).
```

(method-__neg__)=
### \_\_neg\_\_(self, /)

Evaluates `-self_i` for each element of an array instance.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the evaluated result for each element in `self`. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`negative(x)`](elementwise_functions.md#negativex-).
```

(method-__or__)=
### \_\_or\_\_(self, other, /)

Evaluates `self_i | other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer or boolean data type.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`). Must have an integer or boolean data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`positive(x1, x2)`](elementwise_functions.md#bitwise_orx1-x2-).
```

(method-__pos__)=
### \_\_pos\_\_(self, /)

Evaluates `+self_i` for each element of an array instance.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the evaluated result for each element. The returned array must have the same data type as `self`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`positive(x)`](elementwise_functions.md#positivex-).
```

(method-__pow__)=
### \_\_pow\_\_(self, other, /)

Calculates an implementation-dependent approximation of exponentiation by raising each element (the base) of an array instance to the power of `other_i` (the exponent), where `other_i` is the corresponding element of the array `other`.

#### Special Cases

For floating-point operands, let `self` equal `x1` and `other` equal `x2`.

-   If `x1_i` is not equal to `1` and `x2_i` is `NaN`, the result is `NaN`.
-   If `x2_i` is `+0`, the result is `1`, even if `x1_i` is `NaN`.
-   If `x2_i` is `-0`, the result is `1`, even if `x1_i` is `NaN`.
-   If `x1_i` is `NaN` and `x2_i` is not equal to `0`, the result is `NaN`.
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
-   If `x1_i` is less than `0`, `x1_i` is a finite number, `x2_i` is a finite number, and `x2_i` is not an integer value, the result is `NaN`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance whose elements correspond to the exponentiation base.

-   **other**: _&lt;array&gt;_

    -   other array whose elements correspond to the exponentiation exponent. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`pow(x1, x2)`](elementwise_functions.md#powx1-x2-).
```

(method-__rshift__)=
### \_\_rshift\_\_(self, other, /)

Evaluates `self_i >> other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer data type.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`). Must have an integer data type. Each element must be greater than or equal to `0`.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have the same data type as `self`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`bitwise_right_shift(x1, x2)`](elementwise_functions.md#bitwise_right_shiftx1-x2-).
```

(method-__setitem__)=
### \_\_setitem\_\_(self, key, value, /)

_TODO: dependent on the indexing specification._

(method-__sub__)=
### \_\_sub\_\_(self, other, /)

Calculates the difference for each element of an array instance with the respective element of the array `other`. The result of `self_i - other_i` must be the same as `self_i + (-other_i)` and must be governed by the same floating-point rules as addition (see [`__add__()`](#__add__self-other-)).

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance (minuend array).

-   **other**: _&lt;array&gt;_

    -   subtrahend array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise differences. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`subtract(x1, x2)`](elementwise_functions.md#subtractx1-x2-).
```

(method-__truediv__)=
### \_\_truediv\_\_(self, other, /)

Evaluates `self_i / other_i` for each element of an array instance with the respective element of the array `other`.

#### Special Cases

For floating-point operands, let `self` equal `x1` and `other` equal `x2`.

-   If either `x1_i` or `x2_i` is `NaN`, the result is `NaN`.
-   If `x1_i` is either `+infinity` or `-infinity` and `x2_i` is either `+infinity` or `-infinity`, the result is `NaN`.
-   If `x1_i` is either `+0` or `-0` and `x2_i` is either `+0` or `-0`, the result is `NaN`.
-   If `x1_i` is `+0` and `x2_i` is greater than `0`, the result is `+0`.
-   If `x1_i` is `-0` and `x2_i` is greater than `0`, the result `-0`.
-   If `x1_i` is `+0` and `x2_i` is less than `0`, the result is `-0`.
-   If `x1_i` is `-0` and `x2_i` is less than `0`, the result is `+0`.
-   If `x1_i` is greater than `0` and `x2_i` is `+0`, the result is `+infinity`.
-   If `x1_i` is greater than `0` and `x2_i` is `-0`, the result is `-infinity`.
-   If `x1_i` is less than `0` and `x2_i` is `+0`, the result is `-infinity`.
-   If `x1_i` is less than `0` and `x2_i` is `-0`, the result is `+infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is a positive (i.e., greater than `0`) finite number, the result is `+infinity`.
-   If `x1_i` is `+infinity` and `x2_i` is a negative (i.e., less than `0`) finite number, the result is `-infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is a positive (i.e., greater than `0`) finite number, the result is `-infinity`.
-   If `x1_i` is `-infinity` and `x2_i` is a negative (i.e., less than `0`) finite number, the result is `+infinity`.
-   If `x1_i` is a positive (i.e., greater than `0`) finite number and `x2_i` is `+infinity`, the result is `+0`.
-   If `x1_i` is a positive (i.e., greater than `0`) finite number and `x2_i` is `-infinity`, the result is `-0`.
-   If `x1_i` is a negative (i.e., less than `0`) finite number and `x2_i` is `+infinity`, the result is `-0`.
-   If `x1_i` is a negative (i.e., less than `0`) finite number and `x2_i` is `-infinity`, the result is `+0`.
-   If `x1_i` and `x2_i` have the same mathematical sign and are both nonzero finite numbers, the result has a positive mathematical sign.
-   If `x1_i` and `x2_i` have different mathematical signs and are both nonzero finite numbers, the result has a negative mathematical sign.
-   In the remaining cases, where neither `-infinity`, `+0`, `-0`, nor `NaN` is involved, the quotient must be computed and rounded to the nearest representable value according to IEEE 754-2019 and a supported rounding mode. If the magnitude is too larger to represent, the operation overflows and the result is an `infinity` of appropriate mathematical sign. If the magnitude is too small to represent, the operation underflows and the result is a zero of appropriate mathematical sign.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`divide(x1, x2)`](elementwise_functions.md#dividex1-x2-).
```

(method-__xor__)=
### \_\_xor\_\_(self, other, /)

Evaluates `self_i ^ other_i` for each element of an array instance with the respective element of the array `other`.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance. Must have an integer or boolean data type.

-   **other**: _&lt;array&gt;_

    -   other array. Must be compatible with `self` (see {ref}`broadcasting`). Must have an integer or boolean data type.

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array containing the element-wise results. The returned array must have a data type determined by {ref}`type-promotion`.

```{note}

Element-wise results must equal the results returned by the equivalent element-wise function [`bitwise_xor(x1, x2)`](elementwise_functions.md#bitwise_xorx1-x2-).
```

(method-to_device)=
### to\_device(self, device, /)

Move the array to the given device.

#### Parameters

-   **self**: _&lt;array&gt;_

    -   array instance.

-   **device**: _&lt;device&gt;_

    -   a `device` object (see {ref}`device-support`).

#### Returns

-   **out**: _&lt;array&gt;_

    -   an array with the same data and dtype, located on the specified device.
