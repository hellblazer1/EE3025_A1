import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

def tocomplex(field):
	field = str(field)[2:]
	field = field[0 : len(field) - 1]
	return complex(field.replace('+-', '-').replace('i', 'j'))

X_k = np.loadtxt('../data/x_fft.dat', converters={0: tocomplex}, dtype = np.complex128, delimiter = '\n')
H_k = np.loadtxt('../data/h_fft.dat', converters={0: tocomplex}, dtype = np.complex128, delimiter = '\n')

X_k = np.fft.fftshift(X_k)
H_k = np.fft.fftshift(H_k)

n = len(X_k)
w = np.linspace(-np.pi,np.pi,n)
fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(w,abs(X_k))
ax[0].set_xlabel("$\omega$")
ax[0].set_ylabel("|X(k)|")
ax[0].set_title("FFT of x[n]")

ax[1].plot(w,abs(H_k))
ax[1].set_xlabel("$\omega$")
ax[1].set_ylabel("|H(k)|")
ax[1].set_title("FFT of h[n]")
fig.tight_layout()

#if using termux
plt.savefig('../figs/5_1.eps')
plt.savefig('../figs/5_1.pdf')
