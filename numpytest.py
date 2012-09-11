import numpy as np
import numpy.fft as fft

def printTypeAndValue(x):
  print type(x), "\n", x

a = np.arange(10)
printTypeAndValue(a)

def vecadd_python(a, b):
    c = [0] * len(a)
    for i in range(N):
        c[i] = a[i] + b[i]

def vecadd_numpy(a, b, N):
    return a + b

N = 5000000
a = range(N)
b = range(N)

