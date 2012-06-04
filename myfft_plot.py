import myfft
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

N = 1024
nseries = range(0, 1024)

x = range(0, 1024)
X = myfft.fft(x)
absX = [ abs(v) for v in X ]

#plt.plot(nseries, x, nseries, absX)
#plt.savefig('myfftplot01.png', format='png')


x = [ 1 if i == 100 else 0 for i in range(0, 1024) ]
X = myfft.fft(x)
absX = [ abs(v) for v in X ]

plt.plot(nseries, x, nseries, absX)
plt.savefig('myfftplot02.png', format='png')
