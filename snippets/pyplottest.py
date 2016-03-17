import matplotlib.pyplot as plt
import matplotlib.pylab as pl
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.savefig('pyplot01.png', format='png')

plt.hist(pl.randn(100000), 50)
plt.savefig('pyplot_randn_hist.png', format='png')


