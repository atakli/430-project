# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:31:31 2019

@author: Emre
"""

# -*- coding:utf-8 -*-

import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib,time,math
import scipy.signal as signal

size = 1000
sampling_t = 0.01
nb = int(1 / sampling_t)
t = np.arange(0, size, sampling_t)

 # Randomly generated signal sequence
a = np.random.randint(0, 2, size)
m = np.zeros(len(t), dtype=np.float32)

for i in range(len(t)):
    m[i] = a[math.floor(t[i])]
fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)

 # set_titleChinese garbled
zhfont1 = matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')

ax1.set_title('Generate random n-bit binary signal', fontproperties = zhfont1, fontsize = 20)
plt.axis([0, size, -0.5, 1.5])
plt.plot(t, m, 'b')

fc = 4000
fs = 20 * fc # sampling frequency
ts = np.arange(0, (100 * size) / fs, 1 / fs)
coherent_carrier = np.cos(np.dot(2 * pi * fc, ts))
bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (m - 1))

 # BPSK modulated signal waveform
ax2 = fig.add_subplot(3, 1, 2)
ax2.set_title('BPSK modulation signal', fontproperties=zhfont1, fontsize=20)
plt.axis([0,size,-1.5, 1.5])
plt.plot(t, bpsk, 'r')

 # Define additive white Gaussian noise
def awgn(y, snr):
    snr = 10 ** (snr / 10.0)
    xpower = np.sum(y ** 2) / len(y)
    npower = xpower / snr
    return np.random.randn(len(y)) * np.sqrt(npower) + y

 # AWGN noise
noise_bpsk = awgn(bpsk, 5)

 # BPSK modulation signal superimposed noise waveform
ax3 = fig.add_subplot(3, 1, 3)
ax3.set_title('BPSK modulated signal superimposed noise waveform', fontproperties = zhfont1, fontsize = 20)
plt.axis([0, size, -1.5, 1.5])
plt.plot(t, noise_bpsk, 'r')
plt.tight_layout()

 # ,passband is [2000,6000]
[b11,a11] = signal.ellip(5, 0.5, 60, [2000 * 2 / 80000, 6000 * 2 / 80000], btype = 'bandpass', analog = False, output = 'ba')

 # Low pass filter design, passband cutoff frequency is 2000Hz
[b12,a12] = signal.ellip(5, 0.5, 60, (2000 * 2 / 80000), btype = 'lowpass', analog = False, output = 'ba')

 # Filter out-of-band noise by bandpass filter
bandpass_out = signal.filtfilt(b11, a11, noise_bpsk)

 #Coherent demodulation, multiplied by coherent carrier in phase with the same frequency
coherent_demod = bandpass_out * (coherent_carrier * 2)

 # Pass low pass filter
lowpass_out = signal.filtfilt(b12, a12, coherent_demod)
fig2 = plt.figure()
bx1 = fig2.add_subplot(3, 1, 1)
bx1.set_title('local carrier downconversion, after low pass filter', fontproperties = zhfont1, fontsize=20)
plt.axis([0, size, -1.5, 1.5])
plt.plot(t, lowpass_out, 'r')

 #sample judgment
detection_bpsk = np.zeros(len(t), dtype=np.float32)
flag = np.zeros(size, dtype=np.float32)

bak1 = time.time()
for i in range(size):
    tempF = 0
    for j in range(100):
        tempF = tempF + lowpass_out[i * 100 + j]
    if tempF > 0:
        flag[i] = 1
    else:
        flag[i] = 0
for i in range(size):
    if flag[i] == 0:
        for j in range(100):
            detection_bpsk[i * 100 + j] = 0
    else:
        for j in range(100):
            detection_bpsk[i * 100 + j] = 1
print('eskisi: ',time.time()-bak1)
detection_bpsk3 = np.zeros(size, dtype=np.float32)
tempF = np.zeros(0, dtype=np.float32)

bak = time.time()
for i in range(size):
    tempF = np.append(tempF,lowpass_out[i*nb:(i+1)*nb].sum())
detection_bpsk3 = np.where(tempF > 0,1,0)
print('yenisi: ',time.time()-bak)
print('aynı mı: ',np.array_equal(detection_bpsk3,a))
detection_bpsk2 = np.where(lowpass_out > 0,1,0)
print('ne kadarı aynı: Yüzde ',len(np.where(detection_bpsk == detection_bpsk2)[0])/len(detection_bpsk)*100)
bx2 = fig2.add_subplot(3, 1, 2)
bx2.set_title('signal after BPSK signal sampling decision', fontproperties = zhfont1, fontsize=20)
plt.axis([0, size, -0.5, 1.5])
plt.plot(t, detection_bpsk, 'r')
plt.tight_layout()

fig3 = plt.figure()
cx1 = fig3.add_subplot(3, 1, 1)
cx1.set_title('new signal', fontproperties = zhfont1, fontsize=20)
plt.plot(detection_bpsk3, 'g')

cx2 = fig3.add_subplot(3, 1, 2)
cx2.set_title('original signal', fontproperties = zhfont1, fontsize=20)
plt.plot(a, 'g')
plt.tight_layout()
plt.show()