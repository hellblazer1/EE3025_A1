import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

#If using termux
import subprocess
import shlex

input_signal, fs = sf.read('../data/Sound_Noise.wav')
sampl_freq = fs
order = 4
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))


xdata = np.loadtxt('../data/x.dat')
ydata = np.loadtxt('../data/y.dat')

t = np.arange(0,n)

fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(t,xdata)
ax[0].set_title("Input to the difference equation")
ax[0].set_xlabel("n")
ax[0].set_ylabel("x(n)")

ax[1].plot(t,ydata)
ax[1].set_xlabel("n")
ax[1].set_title("Output from the difference equation")
ax[1].set_ylabel("y(n)")
fig.tight_layout()

plt.savefig('../figs/2_2.eps')
plt.savefig('../figs/2_2.pdf')


