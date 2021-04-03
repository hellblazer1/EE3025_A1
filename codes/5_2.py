import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex


yn= np.loadtxt('../data/y_ifft.dat')

n = len(yn)
plt.plot(yn)
plt.xlabel("n")
plt.ylabel("y(n)")
plt.title("y(n) obtained through performing ifft(fft(Y))")

#if using termux
plt.savefig('../figs/5_2.eps')
plt.savefig('../figs/5_2.pdf')

