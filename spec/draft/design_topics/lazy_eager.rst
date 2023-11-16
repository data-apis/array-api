.. _lazy-eager:

Lazy vs. eager execution
========================

While the execution model for implementations is out of scope of this standard, there are a few aspects of lazy (or graph-based) execution as contrasted to eager execution that may have an impact on the prescribed semantics of individual APIs, and will therefore show up in the API specification.

One important difference is data-dependent or value-dependent behavior, as described in :ref:`data-dependent-output-shapes`. Because such behavior is hard to implement, implementers may choose to omit such APIs from their library.

Another difference is when the Python language itself prescribes that a specific type *must* be returned. For those cases, it is not possible to return a lazy/delayed kind of object to avoid computing a value. This is the case for five dunder methods: `__bool__`, `__int__`, `__float__`, `__complex__` and `__index__`. Each implementation has only two choices when one of these methods is called:

1. Compute a value of the required type (a Python scalar of type `bool`, `int`, `float` or `complex`), or
2. Raise an exception.

When an implementation is 100% lazy, for example when it serializes a computation graph, computing the value is not possible and hence such an implementation has no choice but to raise an exception. For a "mostly lazy" implementation, it may make sense to trigger execution instead - but it is not required to, both choices are valid.

A common code construct where this happens is conditional logic, e.g.::

    vals = compute_something()
    if all(vals):
        # The if-statement will make Python call the __bool__ method
        # on the result of `all(vals)`.
        do_something_else()

Note that the API does not contain control flow constructs that would allow avoiding the implicit `__bool__` call in the example above. The only control flow-like function is `where`, but there's no function like `cond` to replace an `if`-statement.
