import numpy as np
from matplotlib.markers import MarkerStyle
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import patches

#if using termux
import subprocess
import shlex

#co-efficients of numerator and denominator
input_signal,fs = sf.read('../data/Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000
Wn = 2*cutoff_freq/sampl_freq
b,a = signal.butter(order,Wn,'low')

#calculating zeros
zeros=np.poly1d(b).r
print("Zeros: ",zeros)
real_z = np.real(zeros)
imag_z = np.imag(zeros)

#calculating poles
poles=np.poly1d(a).r
print("Poles: ", poles)
real_p = np.real(poles)
imag_p = np.imag(poles)

x = np.linspace(-3,3,1000)
y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='#539ecd')

ax = plt.subplot(111)
#unit circle    
unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed',label = 'unit circle')
ax.add_patch(unit_circle)

#circle passing through max abs(poles) and zero axes    
req_circle = patches.Circle((0,0), radius = np.max(np.abs(poles)),fill=True, color='white', ls='solid')
ax.add_patch(req_circle)

#boundary to highlight region with |z| > 0.811
boundary = patches.Circle((0,0), radius=np.max(np.abs(poles)), fill=False, color='black', ls='solid')
ax.add_patch(boundary)

plt.plot(real_z,imag_z,'o',color='black',markersize=5,label = 'zeros')
plt.plot(real_p,imag_p,'x',color='black',markersize=5,label = 'poles')
plt.text(-0.1,0,"z=0")
plt.text(0,0.86,"ROC",fontsize='x-small')
plt.title('pole zero plot in z plane with ROC |z| > 0.811')
plt.xlabel('real')
plt.ylabel('imaginary')
plt.axis('scaled')
plt.axis([-2,2,-2,2])
plt.legend()
#If using termux
#plt.savefig('../figs/4_2.pdf')
#plt.savefig('../figs/4_2.eps')
plt.show()
