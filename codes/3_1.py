import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

def imp_res(z,num_coeffs,den_coeffs):
    Num = np.polyval(num_coeffs,pow(z,-1))
    Den = np.polyval(den_coeffs,pow(z,-1))
    return Num/Den

#parameters of butterworth filter 
x,fs = sf.read('../data/Sound_Noise.wav') 
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

#Calculating coefficients of numerator and denominator for butterworth filter
b,a = signal.butter(order,Wn,'low')
w = np.linspace(-np.pi,np.pi,len(x))
z = np.exp(1j * w)

H = imp_res(z,b,a)

#plotting the magnitude of frequency domain impulse response of the filter
plt.plot(w,abs(H))
plt.title('Magnitude of frequency domain Impulse Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(j\omega)|$')
#If using termux
plt.savefig('../figs/3_1.pdf')
plt.savefig('../figs/3_1.eps')
