import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from scipy import array, zeros, signal
from scipy.fftpack import fft, ifft, convolve

#If using termux
import subprocess
import shlex



x,fs = sf.read('../data/Sound_Noise.wav')
y = np.zeros(len(x))
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

h = np.zeros(len(x))
h[0] = (b[0]/a[0])
h[1] = (1/a[0]) * (b[1]-a[1]*h[0])
h[2] = (1/a[0]) * (b[2]-a[2]*h[0]-a[1]*h[1])
h[3] = (1/a[0]) * (b[3]-a[1]*h[2]-a[3]*h[0]-a[2]*h[1])
h[4] = (1/a[0]) * (b[4]-a[1]*h[3]-a[2]*h[2]-a[4]*h[0]-a[3]*h[1])
for i in range(5,len(x)):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-a[4]*h[i-4])


#circular convolution in freq domain
def conv(x, h):
  X = fft(x)
  H = fft(h)
  #computing convolution in frequency domain
  Y = X * H
  #calculating time domain representation of Y
  y = ifft(Y)
  return y
  
  			
y = conv(x,h)
plt.plot(np.real(y))
plt.title('Output signal through convolution')
plt.xlabel('n')
plt.ylabel('y(n)')

#If using termux
plt.savefig('../figs/4_3.pdf')
plt.savefig('../figs/4_3.eps')
subprocess.run(shlex.split("termux-open ../figs/4_3.pdf"))
