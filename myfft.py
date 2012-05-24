from types import *
import math
import cmath

def twiddles(n):
    """Returns an array of n twiddle factors."""
    return [cmath.rect(1, -2 * math.pi * k / n) for k in range(0, n)]

def dft(x):
    N = len(x)
    return [ sum( [ x[n] * cmath.rect(1, -2 * math.pi * n * k / N) for n in range(0, N)], 0) for k in range(0, N) ]
    
def fft(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    eve = fft(x[0::2])
    odd = fft(x[1::2])
    twiddles = [cmath.rect(1, -2 * math.pi * k / N) for k in range(0, N/2)]
    twohalves = zip(*[(e + t * o, e - t * o) for (e, o, t) in zip(eve, odd, twiddles)])
    res = [elm for half in twohalves for elm in half]
    return res

        