(tutorial-api)=

# Array API Tutorial - Migrating API

The purpose of this tutorial is to show common patterns for migrating your APIs to
the standard-compatible version in the least disruptive manner for the users.
The patterns discussed in the document cover renaming functions and changing their
signatures, with deprecation periods.

## Renaming a function

First common migration that might occur is the need to rename a function to
the one that is present (or is semantically close enough) in the array API standard.

Let's assume our API has a `transpose` function - the one that is not in the standard
under this name. Instead, `permute_dims` is present for permuting the axes of an
array, so we can assume this is the one we want to migrate users to. The original
function is as follows:

```py
def transpose(a, axes=None):
    ...
```

The first stage is to implement `permute_dims` and deprecate the old one with an
informative migration guide on what should be used instead:

```py
def permute_dims(x, /, axes):
    ...

def transpose(a, axes=None):
    warnings.warn("`transpose` function is deprecated, use `permute_dims` instead.", DeprecationWarning)
    ...
```

After a deprecation cycle, when you are ready to remove the deprecated function,
you should still leave hints for users in case they skipped deprecated versions.
One option is to track deprecated & removed functions' names in `__getattr__` and
still inform users what has happened and what to do about it:

```py
# in your `__init__.py`

def __getattr__(attr):
    ...
    if attr == "transpose":
        raise AttributeError(
            f"`transpose` was removed in the ... release. use `permute_dims` instead."
        )
```

## Changing a function's signature

Another common pattern during migration to the array API standard is to modify
the signature of a function. The most troublesome parameters are keyword arguments
as it requires users to use the new name.

For this scenario we are about to change `reshape` signature to the one in
the standard:

```py
def reshape(a, newshape):
    ...
```

We need to rename `newshape` parameter to `shape`, add `copy` parameter, and enforce
new positional/keyword calling format.

After researching how users call our `reshape`, we decided to: make `a` positional
only without an extra deprecation message apart from changelog entry, make `shape`
positional or keyword parameter, and make `newshape` and `copy` keyword only:

```py
def reshape(a, /, shape=None, *, newshape=None, copy=None):
    ...
```

This way users calling `reshape(arr, (ax1, ax2, ax3))` will not notice any change
in the behavior of the function. Now we need to iron out other scenarios.
Users calling the function with a `newshape=...` need to receive a warning with
a proper recommendation, and the extreme case of both `shape` and `newshape` passed
needs to result in an exception:

```py
import warnings

def reshape(a, /, shape=None, *, newshape=None, copy=None):
    if newshape is not None:
        warnings.warn(
            "`newshape` keyword argument is deprecated, use `shape=...` or pass shape positionally instead.", DeprecationWarning,
        )
        if shape is not None:
            raise TypeError("You cannot specify `newshape` and `shape` arguments at the same time.")
        shape = newshape
    # proceed with `shape` argument
    ...
```

Once a deprecation period has passed, we replace the deprecation warning with
a to a `TypeError`, with the same migration message as before:

```py
def reshape(a, /, shape=None, *, newshape=None, copy=None):
    if newshape is not None:
        raise TypeError(
            "`newshape` keyword argument is not supported anymore, use `shape=...` "
            "or pass shape positionally instead."
        )
    ...
```

In case your original parameter supported `None` as an actual shape as well, you
should consider introducing a custom `_NoValue` instance for tracking whether
the parameter was set or not:

```py
class _NoValueType:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

_NoValue = _NoValueType()
# Use `newshape=_NoValue` in the signature
```

The final step is to remove deprecated and already unsupported parameters, which
leaves us with a final and standard compatible version for the next release:

```py
def reshape(a, /, shape, *, copy=None):
    ...
```
