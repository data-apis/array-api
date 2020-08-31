.. _accuracy:

# Accuracy

## Arithmetic Operations

The results of element-wise arithmetic operations

-   `+`
-   `-`
-   `*`
-   `/`
-   `%`

including the corresponding element-wise array APIs defined in this standard

-   add
-   subtract
-   multiply
-   divide

for floating-point operands must return the nearest representable value according to IEEE 754-2019 and a supported rounding mode. By default, the rounding mode should be `roundTiesToEven` (i.e., ties rounded toward the nearest value with an even least significant bit).

## Mathematical Functions

This specification does **not** precisely define the behavior of the following functions

-   acos
-   acosh
-   asin
-   asinh
-   atan
-   atanh
-   cos
-   cosh
-   exp
-   log
-   sin
-   sinh
-   sqrt
-   tan
-   tanh
   
except to require specific results for certain argument values that represent boundary cases of interest.

For other argument values, these functions should compute approximations to the results of respective mathematical functions; however, this specification recognizes that array libraries may be constrained by underlying hardware and/or seek to optimize performance over absolute accuracy and, thus, allows some latitude in the choice of approximation algorithms.

Although the specification leaves the choice of algorithms to the implementation, this specification recommends (but does not specify) that implementations use the approximation algorithms for IEEE 754-2019 arithmetic contained in [fdlibm](http://www.netlib.org/fdlibm), the freely distributable mathematical library from Sun Microsystems, or some other comparable IEEE 754-2019 compliant mathematical library.

## Statistical Functions

(TODO)

## Linear Algebra

(TODO)