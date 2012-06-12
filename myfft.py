from types import *
import math
import cmath
import itertools
import operator

def twiddles(n):
    """Returns an array of n twiddle factors."""
    return [cmath.rect(1, -2 * math.pi * k / n) for k in range(0, n)]

def dft(x):
    N = len(x)
    return [ sum( [ x[n] * cmath.rect(1, -2 * math.pi * n * k / N) for n in range(0, N)], 0) for k in range(0, N) ]

def fft_r2(x):
    return fft_r2_cryptic(x)
    
def fft_r2_cryptic(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 2 != 0: return x
    eve = fft_r2_cryptic(x[0::2])
    odd = fft_r2_cryptic(x[1::2])
    twiddles = [cmath.rect(1, -2 * math.pi * k / N) for k in range(0, N/2)]
    twohalves = zip(*[(e + t * o, e - t * o) for (e, o, t) in zip(eve, odd, twiddles)])
    res = [elm for half in twohalves for elm in half]
    return res

def fft_r4(x):
    return fft_r4_cryptic(x)

def fft_r4_cryptic(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 4 != 0: return fft_r2(x)
    f = [fft_r4_cryptic(x[i::4]) for i in range(0, 4)]
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

# Now let's write it nicely, being as understandable as the textbook formulas.

def W_(N):
    return cmath.rect(1, -2 * math.pi / N)

def dotproduct(vector1, vector2):
    return sum(itertools.imap(operator.mul, vector1, vector2))

def matrixtimesvector(matrix, vector):
    return [ dotproduct(row, vector) for row in matrix ]

def dft2(x):
    return [x[0] + x[1], x[0] - x[1]]

def dft4(x):
    if len(x) != 4: raise ValueError
    dft4 = [[1,   1,  1,  1],
            [1, -1j, -1, 1j],
            [1,  -1,  1, -1],
            [1,  1j, -1, -1j]]
    return matrixtimesvector(dft4, x)

def fft_r2_simple(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 2 != 0: return x
    eve = fft_r2_simple(x[0::2])
    odd = fft_r2_simple(x[1::2])
    twiddles = [ W_(N) ** k for k in range(N/2)]
    X = [0] * N
    for k in range(N/2):
        pair = [eve[k], twiddles[k] * odd[k]]
        X[k], X[k + N/2] = dft2(pair)
    return X

def fft_r4_simple(x):
    N = len(x)
    if N <= 1: return x # trivial size-1 base case
    if N % 4 != 0: return fft_r2(x)
    f = [fft_r4_simple(x[i::4]) for i in range(0, 4)]
    twiddles = [ W_(N) ** k for k in range(N/4)]
    X = [0] * N
    for k in range(N/4):
        quartet = [ (twiddles[k] ** i) * f[i][k] for i in range(4)]
        X[k], X[k + N/4], X[k + N/2], X[k + 3*N/4] = dft4(quartet)
    return X

