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

N = 8
I = np.matrix(np.identity(N))

printTypeAndValue(I)
printTypeAndValue(I[0])
printTypeAndValue(np.asarray(I[0]))
printTypeAndValue(np.squeeze(np.asarray(I[0])))
printTypeAndValue(np.asarray(I[0])[0])
printTypeAndValue(np.asarray(I[0]).reshape(-1))
printTypeAndValue(np.reshape(np.asarray(I[0]), -1))

for r in I:
  a = np.squeeze(np.asarray(r))
  print "row", r, "row", a, "fft", fft.fft(a)

DFTMatrix = np.matrix([ fft.fft(np.squeeze(np.asarray(r))) for r in I ])

printTypeAndValue(DFTMatrix)

printTypeAndValue(DFTMatrix.T == DFTMatrix)
printTypeAndValue((DFTMatrix.T == DFTMatrix).all())

print "Is DFT Matrix exactly equal to its transpose?", ("Yes!" if (DFTMatrix.T == DFTMatrix).all() else "No!") 

printTypeAndValue(DFTMatrix.T - DFTMatrix)
printTypeAndValue(np.around(DFTMatrix.T - DFTMatrix, 10))

print "Is DFT Matrix nearly equal to its transpose?", ("Yes!" if (abs(DFTMatrix.T - DFTMatrix) < 1e-10).all() else "No!") 
