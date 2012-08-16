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

if not plt.isinteractive(): plt.show()
