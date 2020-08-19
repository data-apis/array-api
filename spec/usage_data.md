# Data on existing API design & usage

## Summary

Since the goal of this API is to move existing array APIs closer toward one
another, its design is informed primarily from these existing libraries and
their usage, not from abstract theory or first principles. We can understand our
process as pulled in two directions, driven by downstream usage of array
libraries toward a larger surface area and driven by array implementers toward a
smaller one. We are trying to thread a needle between these two stakeholders,
trying to find the pieces that are implemented by most of the array libraries
and that are used by many applications. To do this, we have collected data on:

- Array API producers: What functionality different array libraries implement
  (NumPy, Tensorflow, etc.)
- Array API consumers: What functionality is commonly used by downstream
  libraries (scikit-learn, pandas, etc.)

## Methods

To collect data on array API producers, we scraped the docs of the many common
array libraries to pull out the signatures for their various functions. For
consumers, we looked at a number of popular downstream data science libraries
that used an array library and ran their test suites, recording every call to an
array API. Using those traces, we have data on how the different APIs are used,
including what functions are called and what type of arguments they take.

We used this data to inform which APIs were most commonly used, to understand
what to include in the specification. We were also able to see which keyword
arguments were used and the types of the arguments. This data helped inform our
choices on what to standardize.

## Tooling

To understand how a downstream consumer calls an API library led us to build a
general purpose library for tracing Python API calls. Running their test suites
using this library, lets us reconstruct the "view" of the API from the
perspective of different downstream users. To do this, we run the test suites
under a special mode that lets us record every call they make to the NumPy and
Pandas APIs. Given this list of calls we can then understand what functionality
these downstream libraries are using the APIs.

Once we have all these records of function calls, we combine them to create a
single view of the downstream API. To do this, we create an inferred function
signature, given a number of records of its usage. If the function in question
support the `inspect.signature` function, this is relatively straightforward,
since we know the type of all the arguments, i.e. whether they are positional,
or keyword, and whether they are optional. However, many functions implemented
in C do not support this type of introspection, so for them we only have a
record of the positional and keyword arguments passed in. From those, we have to
make a guess at which arguments are required, which are optional, and which are
keyword only. Also, when different types are passed to the same argument, we
take the type union of them.

In order to present the results in a human-readable form, we generate a type
definition like file for each of the modules we trace, which lists which
downstream library access each function and how many times they do.

There are a number of limitations with this approach. The primary one is it
being relatively resource intense, since adding this tracing slows down
execution by quiet a lot. Also, it requires creating a custom environment for
each downstream library that is capable of running its test suite.

However, compared to existing static analysis approaches it has the advantage of
letting us extract however much information from the run time as we want,
including string literals, so we can capture arguments that take constants.

## Detailed results and raw data

The tooling for collecting traces from executing library exists in the
[`python-record-api` library](https://github.com/data-apis/python-record-api)
and is published on PyPi. The `data` folder in that repository contains all of
the generated typings, from different downstream users.

The [`array-api-comparison`](https://github.com/data-apis/array-api-comparison)
repository contains the data that was scraped from array library websites, as
well as some summary analysis using that data and the recorded data.
