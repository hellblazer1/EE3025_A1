import soundfile as sf
from scipy import signal
import numpy as np
#If using termux
import subprocess
import shlex
#read .wav file
input_signal,fs = sf.read('../data/Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000

n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))

#writing data into a dat file
np.savetxt('../data/x.dat', input_signal[0:n])
