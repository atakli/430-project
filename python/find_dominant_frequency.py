# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:33 2019

@author: Emre
"""
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq
#import numpy as np
samplerate, data = wavfile.read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\bpsk_de.wav')
print('samplerate: ',samplerate)
datafft = fft(data)
fftabs = abs(datafft)
samples = data.shape[0]
freqs = fftfreq(samples,1/samplerate)
# print(freqs[np.where(fftabs == np.max(fftabs))][0])
plt.plot(freqs,fftabs)
plt.show()
