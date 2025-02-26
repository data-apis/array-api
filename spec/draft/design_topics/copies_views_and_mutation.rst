.. _copyview-mutability:

Copy-view behavior and mutability
==================================

.. admonition:: Mutating views
   :class: important

   Array API consumers are *strongly* advised to avoid *any* mutating operations when an array object may either be a "view" (i.e., an array whose data refers to memory that belongs to another array) or own memory of which one or more other array objects may be views. This admonition may become more strict in the future (e.g., this specification may require that view mutation be prohibited and trigger an exception). Accordingly, only perform mutation operations (e.g., in-place assignment) when absolutely confident that array data belongs to one, and only one, array object.

Strided array implementations (e.g. NumPy, PyTorch, CuPy, MXNet) typically
have the concept of a "view", meaning an array containing data in memory that
belongs to another array (i.e., a different "view" on the original data).
Views are useful for performance reasons—not copying data to a new location
saves memory and is faster than copying—but can also affect the semantics
of code. This happens when views are combined with *mutating* operations.
The following example is illustrative:

.. code-block:: python

   x = ones(1)
   y = x[:]  # `y` *may* be a view on the data of `x`
   y -= 1  # if `y` is a view, this modifies `x`

Code similar to the above example will not be portable between array
libraries. For example, for NumPy, PyTorch, and CuPy, ``x`` will contain the value ``0``,
while, for TensorFlow, JAX, and Dask, ``x`` will contain the value ``1``. In
this case, the combination of views and mutability is fundamentally problematic
if the goal is to be able to write code with unambiguous semantics.

Views are necessary for getting good performance out of the current strided
array libraries. It is not always clear, however, when a library will return a
view and when it will return a copy. This standard does not attempt to
specify this—libraries may do either.

There are several types of operations that may perform in-place mutation of
array data. These include:

1. In-place operators (e.g. ``*=``)
2. Item assignment (e.g. ``x[0] = 1``)
3. Slice assignment (e.g., ``x[:2, :] = 3``)
4. The `out=` keyword present in some strided array libraries (e.g. ``sin(x, out=y)``)

Libraries such as TensorFlow and JAX tend to support in-place operators by providing
alternative syntax for item and slice assignment (e.g. an ``update_index``
function or ``x.at[idx].set(y)``) and have no need for ``out=``.

A potential solution could be to make views read-only or implement copy-on-write
semantics. Both are hard to implement and would present significant backward
compatibility issues for current strided array libraries. Read-only
views would also not be a full solution due to the fact that mutating the original
(base) array will also result in ambiguous semantics. Accordingly, this standard
does not attempt to pursue this solution.

Both in-place operators and item/slice assignment can be mapped onto
equivalent functional expressions (e.g. ``x[idx] = val`` maps to
``x.at[idx].set(val)``), and, given that both in-place operators and item/slice
assignment are very widely used in both library and end user code, this
standard chooses to include them.

The situation with ``out=`` is slightly different—it's less heavily used, and
easier to avoid. It's also not an optimal API because it mixes an
"efficiency of implementation" consideration ("you're allowed to do this
in-place") with the semantics of a function ("the output _must_ be placed into
this array"). There are libraries that do some form of tracing or abstract
interpretation over a vocabulary that does not support mutation (to make
analysis easier). In those cases implementing ``out=`` with correct handling of
views may even be impossible to do.

There are alternatives. For example, the concept of donated arguments in JAX or
working buffers in LAPACK which allow the user to express "you _may_ overwrite
this data; do whatever is fastest". Given that those alternatives aren't widely
used in array libraries today, this standard chooses to (a) leave out ``out=``,
and (b) not specify another method of reusing arrays that are no longer needed
as buffers.

This leaves the problem of the initial example—despite the best efforts of this
standard, it remains possible to write code that will not work the same for all
array libraries. This is something that the users are advised to best keep in
mind and to reason carefully about the potential ambiguity of implemented code.

Copy keyword argument behavior
------------------------------

Several APIs in this standard support a ``copy`` keyword argument (e.g.,
``asarray``, ``astype``, ``reshape``, and ``__dlpack__``). Typically, when a
user sets ``copy=True``, the user does so in order to ensure that they are free
to mutate the returned array without side-effects—namely, without mutating other
views on the original (base) array. Accordingly, when ``copy=True``, unless an
array library can guarantee that an array can be mutated without side-effects,
conforming libraries are recommended to always perform a physical copy of the
underlying array data.

.. note::
   Typically, in order to provide such a guarantee, libraries must perform
   whole-program analysis.

Conversely, consumers of this standard should expect that, if they set
``copy=True``, they are free to use in-place operations on a returned array.
