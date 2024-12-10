.. _exceptions:

Exceptions
==========

This standard specifies expected syntax and semantics for a set of APIs. When
inputs to an API do not match what is expected, libraries may emit warnings,
raise exceptions, or misbehave in unexpected ways. In general, it is not
possible to foresee or specify all the ways in which unexpected or invalid
inputs are provided. Therefore, this standard does not attempt to specify
exception or warning types to the extent needed in order to do exception
handling in a portable manner. In general, it is expected that array library
implementers follow `the guidance given by the documentation of the Python
language <https://docs.python.org/3/library/exceptions.html>`__, and either use
builtin exception or warning types that are appropriate for the
situation or use custom exceptions or warnings that derive from those builtin
ones.

In specific cases, it may be useful to provide guidance to array library
authors regarding what an appropriate exception is. That guidance will be
phrased as **should** rather than **must** (typically in a *Raises* section),
because (a) there may be reasons for an implementer to deviate, and (b) more
often than not, existing array library implementation already differ in their
choices, and it may not be worth them breaking backward compatibility in order
to comply with a "*must*" in this standard.

In other cases, this standard will only specify that an exception *should* or
must be raised, but not mention what type of exception that is.
