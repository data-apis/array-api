# Data on existing API design & usage

## Summary

Since the goal of this API is to move existing array APIs closer toward one another, its design is informed primarily from these existing libraries and their usage, not from abstract theory or first principles. We can understand our process as pulled in two directions, driven by downstream usage of array libraries toward a larger surface area and driven by array implementors toward a smaller one. We are effectively trying to thread a needle between these two stakeholders, trying to find the pieces that are implemented by most of the array libraries and that are used by many applications. To do this, we have collected data on both what functionality different array libraries implement as well as what functionality is commonly used.



## Methods

To collect data on array API producers, we scraped the docs of the many common array libraries to pull out the signatures for their various functions. For consumers, we looked at a number of popular downstream data science libraries that used an array library and ran their test suites, recording every call to an array API. Using those traces, we have data on how the different APIs are used, including what functions are called and what type of arguments they take.



## Tooling

To understand how a downstream consumer calls an API library led us to build a general purpose library for tracing Python API calls. Running their test suites using this library, lets us reconstruct the "view" of the API from the perspective of different downstream users. To do this, we use Python's `sys.settrace` functionality to trigger a breakpoint after every bytecode execution. In that breakpoint, we inspect what bytecode is being execute, and if it involves a function call we look at the Python stack to understand what object is being called and what it's arguments are. If that function is part of the library we are tracing, we save a log of the types of the arguments. We also record any bytecode calls that are not techincally function calls, but can be overriden by libraries, through the implementation of custom "dunder" methods, like `__iter__`, `__add__`, or `__getitem__`. This is important, so that we can understand how operations like indexing are used, by looking at the types of objects provides to these methods.

Once we have all these records of function calls, we combine them to create a single view of the downstream API. To do this, we create an inferred function signature, given a number of records of its usage. If the function in question support the `inspect.signature` function, this is relatively straightforward, since we know the type of all the arguments, i.e. whether they are positional, or keyword, and whether they are optional. However, many functions implemented in C do not support this type of instrospection, so for them we only have a record of the positional and keyword arguments passed in. From those, we have to make a best guess at which args are required, which are optional, and which are keyword only. Also, when different types are passed to the same argument, we take the type union of them.

In order to present the results in a human readbable form, we generate a type definition like file for each of the modules we trace, which lists which downstream library access each function and how many times they do.
 

The most similar existing tool, is probably the [MonkeyType](https://github.com/Instagram/MonkeyType) library, created by Instagram, to generate type definitions from usage of Python code. However, they do not stop at every bytecode execution, instead only tracing function calls, leaving out some of the "dunder" methods. It would likely be useful to explore at some point how the functionality we needed could be added to that existing library.

There are a number of limitations with this approach. The primary one is it being relatively resource intense, since adding this tracing slows down execution by quiet a lot. This has led us to create an automated runner for these tasks using Kubernetes. Also, it requires creating a custom environment for each downstream library that is capable of running its test suite.

However, compared to existing static analysis approaches it has the advantage of letting us extract however much information from the run time as we want, including string literals so we can capture arguments that take constants.


## Detailed results and raw data


The tooling for collecting traces from executing library exists in the [`python-record-api` library](https://github.com/data-apis/python-record-api) and is published on PyPi. The `data` folder in that repository contains all of the generated typings, from different downstream users.

The [`array-api-comparison`](https://github.com/data-apis/array-api-comparison) repository contains the data that was scraped from array library websites, as well as some summary analysis using that data and the recorded data.
