"""IPython demo to illustrate plotting binomial distributions using MATPLOTLIB.

To run it, start IPython in Pylab mode (ipython --pylab) and execute the
following commands:

import ipydemo; ipydemo.rundemo('binomial_ipydemo.py')

"""

import math
import numpy as np
import matplotlib.pyplot as plt

# TODO: follow up on ways of calculating nCr discussed in
# http://stackoverflow.com/questions/3025162/statistics-combinations-in-python

def choose1(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def choose2(n,r):
    """Computes n! / (r! (n-r)!) exactly. Returns a python long int."""
    assert n >= 0
    assert 0 <= r <= n

    c = 1L
    denom = 1
    for (num,denom) in zip(xrange(n,n-r,-1), xrange(1,r+1,1)):
        c = (c * num) // denom
    return c

def choose2_simple(n,r):
    """Computes n! / (r! (n-r)!) exactly. Returns a python long int."""
    assert n >= 0
    assert 0 <= r <= n

    c = 1L
    num = n
    den = 1
    for i in xrange(r):
        c = (c * num) // den
        num -= 1
        den += 1
    return c

def choose(n,r):
    return choose2_simple(n,r)

for n in range(17):
    print ' '.join('%5d' % choose(n,k) for k in range(n+1)).center(100)

def binomial(n, p):
    b = [ choose(n, k) * p**k * (1-p)**(n-k) for k in range(0, n) ]
    return b

print binomial(10, 0.5)
print binomial(20, 0.1)

plt.hold(True)
plt.plot(binomial(20, 0.5))
plt.plot(binomial(20, 0.7))
plt.plot(binomial(20, 0.3))
plt.plot(binomial(20, 0.9))
plt.plot(binomial(20, 0.1))

if not plt.isinteractive(): plt.show()
