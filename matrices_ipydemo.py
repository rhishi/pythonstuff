""" IPython demo to illustrate the use of numpy matrices.

To run, if you have ipydemo.py, do

import ipydemo; ipydemo.rundemo('matrices_ipydemo.py')

"""
import math
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

def printTypeAndValue(x):
  print type(x), "\n", x

N = 8
I = np.matrix(np.identity(N))

printTypeAndValue(I)
printTypeAndValue(I[0])
printTypeAndValue(np.asarray(I[0]))
printTypeAndValue(np.squeeze(np.asarray(I[0])))
printTypeAndValue(np.asarray(I[0])[0])
printTypeAndValue(np.asarray(I[0]).reshape(-1))
printTypeAndValue(np.reshape(np.asarray(I[0]), -1))

# <demo> --- stop ---
# <demo> --- stop ---

for r in I:
  a = np.squeeze(np.asarray(r))
  print "row", r, "row", a, "fft", fft.fft(a)

DFTMatrix = np.matrix([ fft.fft(np.squeeze(np.asarray(r))) for r in I ])

printTypeAndValue(DFTMatrix)

# <demo> --- stop ---
# <demo> --- stop ---

printTypeAndValue(DFTMatrix.T == DFTMatrix)
printTypeAndValue((DFTMatrix.T == DFTMatrix).all())

print "Is DFT Matrix exactly equal to its transpose?", ("Yes!" if (DFTMatrix.T == DFTMatrix).all() else "No!") 

printTypeAndValue(DFTMatrix.T - DFTMatrix)
printTypeAndValue(np.around(DFTMatrix.T - DFTMatrix, 10))

print "Is DFT Matrix nearly equal to its transpose?", ("Yes!" if (abs(DFTMatrix.T - DFTMatrix) < 1e-10).all() else "No!") 

# <demo> --- stop ---
# <demo> --- stop ---

A = np.matrix("1, 2; 3 4")
print A
print A.T
print A.I
print A * A.I

# <demo> --- stop ---

print "A * A = ", A * A
print "A**2 = ", A**2

# <demo> --- stop ---

print "np.multiply(A, A) = ", np.multiply(A, A)

# <demo> --- stop ---
# <demo> --- stop ---

x = np.array([1, 2])
xm = np.matrix(x).T
print x, xm, xm.shape
print A * xm

# <demo> --- stop ---


