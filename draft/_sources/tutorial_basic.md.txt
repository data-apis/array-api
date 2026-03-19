(tutorial-basic)=

# Array API Tutorial

In this tutorial, we're going to demonstrate how to migrate to the Array API from the array consumer's
point of view for a simple graph algorithm.

The example presented here comes from the [`graphblas-algorithms`](https://github.com/python-graphblas/graphblas-algorithms).
library. In particular, we'll be migrating [the HITS algorithm](https://github.com/python-graphblas/graphblas-algorithms/blob/35dbc90e808c6bf51b63d51d8a63f59238c02975/graphblas_algorithms/algorithms/link_analysis/hits_alg.py#L9), which is
used for the link analysis for estimating prominence in sparse networks, to be Array API compliant.

The inlined and slightly simplified (without "authority" feature)
implementation looks similar to the following:

```python
def hits(G, max_iter=100, tol=1.0e-8, normalized=True):
    N = len(G)
    h = Vector(float, N, name="h")
    a = Vector(float, N, name="a")
    h << 1.0 / N
    # Power iteration: make up to max_iter iterations
    A = G._A
    hprev = Vector(float, N, name="h_prev")
    for _i in range(max_iter):
        hprev, h = h, hprev
        a << hprev @ A
        h << A @ a
        h *= 1.0 / h.reduce(monoid.max).get(0)
        if is_converged(hprev, h, tol):
            break
    else:
        raise ConvergenceFailure(max_iter)
    if normalized:
        h *= 1.0 / h.reduce().get(0)
        a *= 1.0 / a.reduce().get(0)
    return h, a

def is_converged(xprev, x, tol):
    xprev << binary.minus(xprev | x)
    xprev << unary.abs(xprev)
    return xprev.reduce().get(0) < xprev.size * tol
```

We can see that the API is specific to the GraphBLAS array object.
There is a `Vector` constructor, overloaded `<<` for assigning new values,
and `reduce`/`get` for reductions. We need to replace them, and, by convention,
we will use `xp` namespace for calling respective functions.

First, we want to make sure we construct arrays in an agnostic way:

```python
h = xp.full(N, 1.0 / N)
A = xp.asarray(G.A)
```

Then, instead of `reduce` calls, we will use appropriate reduction
functions from the Array API:

```python
h = h / xp.max(h)
# ...
h = h / xp.sum(xp.abs(h))
a = a / xp.sum(xp.abs(a))
# ...
err = xp.sum(xp.abs(...))
```

We replace the custom binary operation with the Array API counterpart:

```python
...(x - xprev)
```

And finally, let's ensure that the result of the convergence
condition is a scalar coming from our API:

```python
err < xp.asarray(N * tol)
```

The rewrite is complete now, we can assemble all constituent parts into
a full implementation:

```python
def hits(G, max_iter=100, tol=1.0e-8, normalized=True):
    N = len(G)
    h = xp.full(N, 1.0 / N)
    A = xp.asarray(G.A)
    # Power iteration: make up to max_iter iterations
    for _i in range(max_iter):
        hprev = h
        a = hprev @ A
        h = A @ a
        h = h / xp.max(h)
        if is_converged(hprev, h, N, tol):
            break
    else:
        raise Exception("Didn't converge")
    if normalized:
        h = h / xp.sum(xp.abs(h))
        a = a / xp.sum(xp.abs(a))
    return h, a

def is_converged(xprev, x, N, tol):
    err = xp.sum(xp.abs(x - xprev))
    return err < xp.asarray(N * tol)
```

At this point, the actual execution depends only on `xp` namespace,
and replacing that one variable will allow us to switch from, e.g., NumPy arrays on the CPU
to JAX arrays for running on a GPU. This lets us be more flexible, and, for example,
use lazy evaluation and JIT compile a loop body with JAX's JIT compilation:

```python
import jax
import jax.numpy as jnp

xp = jnp

def hits(G, max_iter=100, tol=1.0e-8, normalized=True):
    N = len(G)
    h = xp.full((N, 1), 1.0 / N)
    A = xp.asarray(G.A)
    # Power iteration: make up to max_iter iterations
    for _i in range(max_iter):
        h, a, conv = loop_body(h, A, N, tol)
        if conv:
            break
    else:
        raise Exception("Didn't converge")
    if normalized:
        h = h / xp.sum(xp.abs(h))
        a = a / xp.sum(xp.abs(a))
    return h, a

@jax.jit
def loop_body(hprev, A, N, tol):
    a = hprev.mT @ A
    h = A @ a.mT
    h = h / xp.max(h)
    conv = is_converged(hprev, h, N, tol)
    return h, a, conv

def is_converged(xprev, x, N, tol):
    err = xp.sum(xp.abs(x - xprev))
    return err < xp.asarray(N * tol)

if __name__ == "__main__":

    class Graph():
        def __init__(self):
            self.A = xp.ones((10, 10))
        def __len__(self):
            return len(self.A)

    G = Graph()
    h, a = hits(G)
```
