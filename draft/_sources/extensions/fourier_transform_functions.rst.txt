Fourier transform Functions
===========================

    Array API specification for Fourier transform functions.

Extension name and usage
------------------------

The name of the namespace providing the extension must be: ``fft``.

If implemented, this ``fft`` extension must be retrievable via::

    >>> xp = x.__array_namespace__()
    >>> if hasattr(xp, 'fft'):
    >>>    # Use `xp.fft`


Objects in API
--------------

A conforming implementation of this ``fft`` extension must provide and support the following functions.

.. currentmodule:: array_api.fft

..
  NOTE: please keep the functions and their inverse together

.. autosummary::
   :toctree: generated
   :template: method.rst

   fft
   ifft
   fftn
   ifftn
   rfft
   irfft
   rfftn
   irfftn
   hfft
   ihfft
   fftfreq
   rfftfreq
   fftshift
   ifftshift
