.. _out-keyword:

# out

> Array API specification for the `out` keyword argument.

A conforming implementation of the array API standard must adhere to the following conventions.

-   Functions and methods which support providing one or more output arrays must do so via a single `out` keyword argument whose default value is `None`.
-   If a function or method returns a single output array, the `out` keyword argument must be either `None` or an array.
-   If a function or method returns multiple output arrays, the `out` keyword argument must be a tuple with one entry (either `None` or an array) per output. Providing a single output array when a function or method returns multiple output arrays is **not** permitted.
-   If `out` is not provided or is `None`, an uninitialized return array must be created for each output for which an output array has not been provided.
-   Functions and methods which support the `out` keyword argument are **not** permitted to change the shape of provided output arrays.