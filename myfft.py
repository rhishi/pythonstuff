from types import *
import math
import cmath

def twiddles(n):
    """Returns an array of n twiddle factors."""
    return [cmath.rect(1, -2 * math.pi * k / n) for k in range(0, n)]

def dft(x):
    N = len(x)
    return [ sum( [ x[n] * cmath.rect(1, -2 * math.pi * n * k / N) for n in range(0, N)], 0) for k in range(0, N) ]
    
def fft_r2(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 2 != 0: return x
    eve = fft_r2(x[0::2])
    odd = fft_r2(x[1::2])
    twiddles = [cmath.rect(1, -2 * math.pi * k / N) for k in range(0, N/2)]
    twohalves = zip(*[(e + t * o, e - t * o) for (e, o, t) in zip(eve, odd, twiddles)])
    res = [elm for half in twohalves for elm in half]
    return res

def fft_r4(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 4 != 0: return fft_r2(x)
    f = [fft_r4(x[i::4]) for i in range(0, 4)]
    twiddles = [cmath.rect(1, -2 * math.pi * k / N) for k in range(0, N/4)]
    s = [ [ f[i][k] * (twiddles[k]**i) for k in range(0, N/4) ] for i in range(0, 4)]
    dft4 = [[1,   1,  1,  1],
            [1, -1j, -1, 1j],
            [1,  -1,  1, -1],
            [1,  1j, -1, -1j]]
    res = [ [dft4[i][0] * s[0][k] +
             dft4[i][1] * s[1][k] +
             dft4[i][2] * s[2][k] +
             dft4[i][3] * s[3][k] for k in range(0, N/4) ] for i in range(0, 4) ]
    return res[0] + res[1] + res[2] + res[3]

        