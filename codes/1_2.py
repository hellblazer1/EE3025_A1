import soundfile as sf
from scipy import signal
import numpy as np

#read .wav file
input_signal,fs = sf.read('../data/Sound_Noise.wav')

#sampling frequency of input signal
sampl_freq = fs

#order of the filter
order = 4

#cutoff freq 4kHz
cutoff_freq = 4000

#digital frequency
Wn = 2*cutoff_freq/sampl_freq

#b and a are numerator and denominator polynomials respectively
b,a = signal.butter(order,Wn,'low')
print('a:',a)
print('b:',b)

#filter the input signal with butterworth filter 
output_signal = signal.filtfilt(b,a,input_signal)

#write output signal into .wav file
sf.write('../data/Sound_With_ReducedNoise.wav',output_signal,fs)
