"""IPython demo to illustrate plotting Gaussian distributions using MATPLOTLIB.

To run it, start IPython in Pylab mode and execute the following commands:

from ipydemo import *
rundemo('gaussian-distribution-ipythondemo.py')

"""

import math
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, variance):
  return 1.0/math.sqrt(2 * math.pi * variance) * np.exp(- 0.5 * (x - mean)**2 / variance)

x = np.arange(-5.0, 5.0, 0.05)

# <demo> --- stop ---

plt.subplot(211)
plt.xlim(-5.0, 5.0)
plt.ylim(0.0, 1.4)
plt.xticks(np.arange(-5.0, 5.0, 1.0))
plt.grid(True)
plt.hold(True)

# <demo> --- stop ---

y = gaussian(x, 0, 0.1)
plt.plot(x, y, 'b')

# <demo> --- stop ---

y = gaussian(x, 0, 1)
plt.plot(x, y, 'r')

# <demo> --- stop ---

y = gaussian(x, 0, 5)
plt.plot(x, y, 'y')

# <demo> --- stop ---

y = gaussian(x, -2, 0.5)
plt.plot(x, y, 'g')

# <demo> --- stop ---

def integrate(y, x):
    n = len(x)
    r = np.zeros(n)
    for i in range(1, n):
        delta = x[i] - x[i-1]
        r[i] = r[i-1] + 0.5 * (y[i] + y[i-1]) * delta 
    return r

plt.subplot(212)
plt.xlim(-5.0, 5.0)
plt.ylim(0.0, 1.0)
plt.xticks(np.arange(-5.0, 5.0, 1.0))
plt.grid(True)
plt.hold(True)

# <demo> --- stop ---

y = integrate(gaussian(x, 0, 0.1), x)
plt.plot(x, y, 'b')

# <demo> --- stop ---

y = integrate(gaussian(x, 0, 1), x)
plt.plot(x, y, 'r')

# <demo> --- stop ---

y = integrate(gaussian(x, 0, 5), x)
plt.plot(x, y, 'y')

# <demo> --- stop ---

y = integrate(gaussian(x, -2, 0.5), x)
plt.plot(x, y, 'g')

# <demo> --- stop ---

if not plt.isinteractive(): plt.show()
