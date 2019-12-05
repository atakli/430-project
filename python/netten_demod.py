# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:04:58 2019

@author: Emre
"""
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
#import math
from scipy.io.wavfile import read

zhfont1 = matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\noised.wav')

#time = np.arange(0,len(y))/Fs
#plt.plot(time,y)
ts = np.arange(0, len (y) / Fs, 1 / Fs)
fc = 4000
coherent_carrier = np.cos(2 * pi * fc * ts)
 # ,passband is [2000,6000]
[b11,a11] = signal.ellip(5, 0.5, 60, [2000 * 2 / 80000, 6000 * 2 / 80000], btype = 'bandpass', analog = False, output = 'ba')
 # Low pass filter design, passband cutoff frequency is 2000Hz 
[b12,a12] = signal.ellip(5, 0.5, 60, (2000 * 2 / 80000), btype = 'lowpass', analog = False, output = 'ba')
 # Filter out-of-band noise by bandpass filter
bandpass_out = signal.filtfilt(b11, a11, y)
 #Coherent demodulation, multiplied by coherent carrier in phase with the same frequency
coherent_demod = bandpass_out * (coherent_carrier * 2)
 # Pass low pass filter
lowpass_out = signal.filtfilt(b12, a12, coherent_demod)

fig2 = plt.figure()
#fig.subplots_adjust(hspace=1)
bx1 = fig2.add_subplot(2, 1, 1)
bx1.set_title('local carrier downconversion, after low pass filter', fontproperties = zhfont1, fontsize=20)
#plt.axis([0, size, -1.5, 1.5])
plt.plot(lowpass_out, 'r')

 #sample judgment
#detection_bpsk = np.zeros(len(y), dtype=np.float32)
#flag = np.zeros(size, dtype=np.float32)
#
#for i in range(size):
#    tempF = 0
#    for j in range(nb):
#        tempF = tempF + lowpass_out[i * nb + j]
#    if tempF > 0:
#        flag[i] = 1
#    else:
#        flag[i] = 0
#for i in range(size):
#    if flag[i] == 0:
#        for j in range(nb):
#            detection_bpsk[i * nb + j] = 0
#    else:
#        for j in range(nb):
#            detection_bpsk[i * nb + j] = 1
detection_bpsk = np.where(lowpass_out > 0,1,0)
bx2 = fig2.add_subplot(2, 1, 2)
bx2.set_title('signal after BPSK signal sampling decision', fontproperties = zhfont1, fontsize=20)
#plt.axis([0, size, -0.5, 1.5])
plt.plot(detection_bpsk, 'r')
plt.tight_layout()
plt.show()