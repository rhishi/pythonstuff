import numpy as np

a = np.arange(10)
print type(a), a

def vecadd_python(a, b):
    c = [0] * len(a)
    for i in range(N):
        c[i] = a[i] + b[i]

def vecadd_numpy(a, b, N):
    return a + b

N = 5000000
a = range(N)
b = range(N)
