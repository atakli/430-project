# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:33 2019

@author: Emre
"""
#import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft,fftfreq
import numpy as np
samplerate, data = wavfile.read("Mono-1k_10k_44k_16bit.wav")
datafft = fft(data)
fftabs = abs(datafft)
samples = data.shape[0]
freqs = fftfreq(samples,1/samplerate)
freqs[np.where(fftabs == np.max(fftabs))][0]
