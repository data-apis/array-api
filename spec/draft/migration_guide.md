# Migration Guide

## Introduction

The Array API Standard was based in the common APIs across multiple Python array libraries as a response to the fragmentation of the ecosystem. It was decided for the Array API Standard to be as compact as possible, meaning that it doesn't include all the creation and manipulation functions available in other libraries, but it is equally as powerful. The aim of this guide is to help users get started with the use of the Array API by providing common equivalents with the NumPy API.

Depending on the version of the Array API Standard that you are intended to use, the number of total APIs may vary and this migration guide is using the latest version `v2022.12`.

## Equivalents

| NumPy | Array API |
| ----- | --------- |
| `ravel(x)` | `reshape(x, (-1,))` |
| `flatten(x)` | `reshape(x, (-1,))` |
