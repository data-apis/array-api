__all__ = ["isin", "unique_all", "unique_counts", "unique_inverse", "unique_values"]


from ._types import Tuple, Union, array


def isin(
    x1: Union[array, int, float, complex, bool],
    x2: Union[array, int, float, complex, bool],
    /,
    *,
    invert: bool = False,
) -> array:
    """
    Tests whether each element in ``x1`` is in ``x2``.

    Parameters
    ----------
    x1: Union[array, int, float, complex, bool]
        first input array. **May** have any data type.
    x2: Union[array, int, float, complex, bool]
        second input array. **May** have any data type.
    invert: bool
        boolean indicating whether to invert the test criterion. If ``True``, the function **must** test whether each element in ``x1`` is *not* in ``x2``. If ``False``, the function **must** test whether each element in ``x1`` is in ``x2``. Default: ``False``.

    Returns
    -------
    out: array
        an array containing element-wise test results. The returned array **must** have the same shape as ``x1`` and **must** have a boolean data type.

    Notes
    -----

    -   At least one of ``x1`` or ``x2`` **must** be an array.

    -   If an element in ``x1`` is in ``x2``, the corresponding element in the output array **must** be ``True``; otherwise, the corresponding element in the output array **must** be ``False``.

    -   Testing whether an element in ``x1`` corresponds to an element in ``x2`` **should** be determined based on value equality (see :func:`~array_api.equal`). For input arrays having floating-point data types, value-based equality implies the following behavior. When ``invert`` is ``False``,

        -   As ``nan`` values compare as ``False``, if an element in ``x1`` is ``nan``, the corresponding element in the returned array **should** be ``False``.
        -   As complex floating-point values having at least one ``nan`` component compare as ``False``, if an element in ``x1`` is a complex floating-point value having one or more ``nan`` components, the corresponding element in the returned array **should** be ``False``.
        -   As ``-0`` and ``+0`` compare as ``True``, if an element in ``x1`` is ``±0`` and ``x2`` contains at least one element which is ``±0``, the corresponding element in the returned array **should** be ``True``.

        When ``invert`` is ``True``, the returned array must contain the same results as if the operation is implemented as ``logical_not(isin(x1, x2))``.

    -   Comparison of arrays without a corresponding promotable data type (see :ref:`type-promotion`) is unspecified and thus implementation-defined.
    """


def unique_all(x: array, /) -> Tuple[array, array, array, array]:
    """
    Returns the unique elements of an input array ``x``, the first occurring indices for each unique element in ``x``, the indices from the set of unique elements that reconstruct ``x``, and the corresponding counts for each unique element in ``x``.

    .. admonition:: Data-dependent output shape
        :class: important

        The shapes of two of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, et cetera) can find this function difficult to implement without knowing array values. Accordingly, such libraries **may** choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. If ``x`` has more than one dimension, the function **must** flatten ``x`` and return the unique elements of the flattened array.

    Returns
    -------
    out: Tuple[array, array, array, array]
        a namedtuple ``(values, indices, inverse_indices, counts)`` whose

        -   first element **must** have the field name ``values`` and **must** be a one-dimensional array containing the unique elements of ``x``. The array **must** have the same data type as ``x``.
        -   second element **must** have the field name ``indices`` and **must** be an array containing the indices (first occurrences) of a flattened ``x`` that result in ``values``. The array **must** have the same shape as ``values`` and **must** have the default array index data type.
        -   third element **must** have the field name ``inverse_indices`` and **must** be an array containing the indices of ``values`` that reconstruct ``x``. The array **must** have the same shape as ``x`` and **must** have the default array index data type.
        -   fourth element **must** have the field name ``counts`` and **must** be an array containing the number of times each unique element occurs in ``x``. The order of the returned counts **must** match the order of ``values``, such that a specific element in ``counts`` corresponds to the respective unique element in ``values``. The returned array **must** have same shape as ``values`` and **must** have the default array index data type.

    Notes
    -----

    -   The order of unique elements returned by this function is unspecified and thus implementation-defined. As a consequence, element order **may** vary between implementations.

    -   Uniqueness **should** be determined based on value equality (see :func:`~array_api.equal`). For input arrays having floating-point data types, value-based equality implies the following behavior.

        -   As ``nan`` values compare as ``False``, ``nan`` values **should** be considered distinct.
        -   As complex floating-point values having at least one ``nan`` component compare as ``False``, complex floating-point values having ``nan`` components **should** be considered distinct.
        -   As ``-0`` and ``+0`` compare as ``True``, signed zeros **should not** be considered distinct, and the corresponding unique element **may** be implementation-defined (e.g., an implementation **may** choose to return ``-0`` if ``-0`` occurs before ``+0``).

        As signed zeros are not distinct, using ``inverse_indices`` to reconstruct the input array is not guaranteed to return an array having the exact same values.

        Each ``nan`` value and each complex floating-point value having a ``nan`` component **should** have a count of one, while the counts for signed zeros **should** be aggregated as a single count.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Clarified flattening behavior and required the order of ``counts`` match the order of ``values``.
    """


def unique_counts(x: array, /) -> Tuple[array, array]:
    """
    Returns the unique elements of an input array ``x`` and the corresponding counts for each unique element in ``x``.

    .. admonition:: Data-dependent output shape
        :class: important

        The shapes of two of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) can find this function difficult to implement without knowing array values. Accordingly, such libraries **may** choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. If ``x`` has more than one dimension, the function **must** flatten ``x`` and return the unique elements of the flattened array.

    Returns
    -------
    out: Tuple[array, array]
        a namedtuple `(values, counts)` whose

        -   first element **must** have the field name ``values`` and **must** be a one-dimensional array containing the unique elements of ``x``. The array **must** have the same data type as ``x``.
        -   second element **must** have the field name `counts` and **must** be an array containing the number of times each unique element occurs in ``x``. The order of the returned counts **must** match the order of ``values``, such that a specific element in ``counts`` corresponds to the respective unique element in ``values``. The returned array **must** have same shape as ``values`` and **must** have the default array index data type.

    Notes
    -----

    -   The order of unique elements returned by this function is unspecified and thus implementation-defined. As a consequence, element order **may** vary between implementations.

    -   Uniqueness **should** be determined based on value equality (see :func:`~array_api.equal`). For input arrays having floating-point data types, value-based equality implies the following behavior.

        -   As ``nan`` values compare as ``False``, ``nan`` values **should** be considered distinct.
        -   As complex floating-point values having at least one ``nan`` component compare as ``False``, complex floating-point values having ``nan`` components **should** be considered distinct.
        -   As ``-0`` and ``+0`` compare as ``True``, signed zeros **should not** be considered distinct, and the corresponding unique element **may** be implementation-defined (e.g., an implementation **may** choose to return ``-0`` if ``-0`` occurs before ``+0``).

        Each ``nan`` value and each complex floating-point value having a ``nan`` component **should** have a count of one, while the counts for signed zeros **should** be aggregated as a single count.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Clarified flattening behavior and required the order of ``counts`` match the order of ``values``.
    """


def unique_inverse(x: array, /) -> Tuple[array, array]:
    """
    Returns the unique elements of an input array ``x`` and the indices from the set of unique elements that reconstruct ``x``.

    .. admonition:: Data-dependent output shape
        :class: important

        The shapes of two of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) can find this function difficult to implement without knowing array values. Accordingly, such libraries **may** choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. If ``x`` has more than one dimension, the function **must** flatten ``x`` and return the unique elements of the flattened array.

    Returns
    -------
    out: Tuple[array, array]
        a namedtuple ``(values, inverse_indices)`` whose

        -   first element **must** have the field name ``values`` and **must** be a one-dimensional array containing the unique elements of ``x``. The array **must** have the same data type as ``x``.
        -   second element **must** have the field name ``inverse_indices`` and **must** be an array containing the indices of ``values`` that reconstruct ``x``. The array **must** have the same shape as ``x`` and have the default array index data type.

    Notes
    -----

    -   The order of unique elements returned by this function is unspecified and thus implementation-defined. As a consequence, element order **may** vary between implementations.

    -   Uniqueness **should** be determined based on value equality (see :func:`~array_api.equal`). For input arrays having floating-point data types, value-based equality implies the following behavior.

        -   As ``nan`` values compare as ``False``, ``nan`` values **should** be considered distinct.
        -   As complex floating-point values having at least one ``nan`` component compare as ``False``, complex floating-point values having ``nan`` components **should** be considered distinct.
        -   As ``-0`` and ``+0`` compare as ``True``, signed zeros **should not** be considered distinct, and the corresponding unique element **may** be implementation-defined (e.g., an implementation **may** choose to return ``-0`` if ``-0`` occurs before ``+0``).

        As signed zeros are not distinct, using ``inverse_indices`` to reconstruct the input array is not guaranteed to return an array having the exact same values.

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Clarified flattening behavior.
    """


def unique_values(x: array, /) -> array:
    """
    Returns the unique elements of an input array ``x``.

    .. admonition:: Data-dependent output shape
        :class: important

        The shapes of two of the output arrays for this function depend on the data values in the input array; hence, array libraries which build computation graphs (e.g., JAX, Dask, etc.) can find this function difficult to implement without knowing array values. Accordingly, such libraries **may** choose to omit this function. See :ref:`data-dependent-output-shapes` section for more details.

    Parameters
    ----------
    x: array
        input array. If ``x`` has more than one dimension, the function **must** flatten ``x`` and return the unique elements of the flattened array.

    Returns
    -------
    out: array
        a one-dimensional array containing the set of unique elements in ``x``. The returned array **must** have the same data type as ``x``.

    Notes
    -----

    -   The order of unique elements returned by this function is unspecified and thus implementation-defined. As a consequence, element order **may** vary between implementations.

    -   Uniqueness **should** be determined based on value equality (see :func:`~array_api.equal`). For input arrays having floating-point data types, value-based equality implies the following behavior.

        -   As ``nan`` values compare as ``False``, ``nan`` values **should** be considered distinct.
        -   As complex floating-point values having at least one ``nan`` component compare as ``False``, complex floating-point values having ``nan`` components **should** be considered distinct.
        -   As ``-0`` and ``+0`` compare as ``True``, signed zeros **should not** be considered distinct, and the corresponding unique element **may** be implementation-defined (e.g., an implementation **may** choose to return ``-0`` if ``-0`` occurs before ``+0``).

    .. versionchanged:: 2022.12
       Added complex data type support.

    .. versionchanged:: 2023.12
       Required that the output array must be one-dimensional.
    """
