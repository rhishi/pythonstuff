"""
IPython demo to illustrate the use of numpy.

To run, if you have ipydemo.py, do

    import ipydemo; ipydemo.rundemo('numpy')
"""

# import numpy, and a few other things.
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

# <demo> --- stop ---
# numpy provides multidimensional, homogeneous arrays.  np.array constructs
# an ndarray from an array-like object, e.g. a list of lists.

a = np.array([[1,2,3], [4,5,6]])

print "a =\n", a
print "      Type of a : type(a) =", type(a)
print "Dimension count : a.ndim  =", a.ndim, " also called rank"
print "  Element count : a.size  =", a.size
print "          Shape : a.shape =", a.shape

# <demo> --- stop ---
# In general, you shouldn't really think in terms of "rows" or "columns" of
# ndarrays, but seeing how 'a' was printed, for a 2D ndarray, you can think
# of the first dimension being the rows, and the second being the columns.
# Looking at its shape, you can say it has 2 rows and 3 columns.

# <demo> --- stop ---
# Operations on ndarrays are element-wise. Vector/matrix product is np.dot.

v = np.array([1.245, -3.592, 2.8734])
print "          v * 3 =", v * 3
print "          v * v =", v * v
print "       a[0] * v =", a[0] * v, " its sum =", sum(a[0] * v)
print "np.dot(a[0], v) =", np.dot(a[0], v)

# <demo> --- stop ---
# a[0] above was a shortcut for a[0,:] to get the first row of a. a[i,j] gives
# the element of a at ith row and jth column.  Slicings are possible in all
# dimensions independently.

# the middle column of a
print "    a[:,1] = ", a[:,1],    "  ndim =", a[:,1].ndim, "shape =", a[:,1].shape 

# the last two columns of the first row.
print "a[0  ,1:3] = ", a[0,1:3],  "  ndim =", a[0,1:3].ndim,   "shape =", a[0,1:3].shape
print "a[0:1,1:3] =", a[0:1,1:3], " ndim =", a[0:1,1:3].ndim, "shape =", a[0:1,1:3].shape
