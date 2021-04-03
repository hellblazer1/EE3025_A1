import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

h = np.loadtxt('../data/h.dat')
#plotting first 100 time samples of h
plt.plot(np.arange(100),h[:100])
plt.xlabel("n")
plt.ylabel("h(n)")
plt.title("Time domain impulse response from the difference equation")

#if using termux
plt.savefig('../figs/4_1.eps')
plt.savefig('../figs/4_1.pdf')
