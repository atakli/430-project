# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:35:53 2019
@author: Emre
"""
# -*- coding:utf-8 -*-
import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt
import matplotlib
from scipy.io.wavfile import write,read
zhfont1 = matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
fig, (ax1,ax2,ax3) = fig.subplots(3, 1, 3)
fig.subplots_adjust(hspace=1)
def dosyadan_oku():
    Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den.wav')
    
def random():
    
    size = 100 # 10
    #sampling_t = 1/Fs
    sampling_t = 0.01
    nb = 1 / sampling_t
    quantization_level = 16
    t = np.arange(0, size, sampling_t)
    
    # Define additive white Gaussian noise
    def awgn(y, snr):
    
        snr = 10 ** (snr / 10.0)
        xpower = np.sum(y ** 2) / len(y)
        npower = xpower / snr
        return np.random.randn(len(y)) * np.sqrt(npower) + y
    
     # Randomly generated signal sequence
    a = np.random.randint(0, 2, size)
    m = np.zeros(size * nb, dtype=np.float32)
    for i in range(size * nb):
        m[i] = a[floor(t[i])]
        
    fc = 4000
    Fs = 20 * fc # sampling frequency
    ts = np.arange(0, (nb * size) / Fs, 1 / Fs)
     # BPSK modulated signal waveform
    bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (m - 1))
     # AWGN noise
    noise_bpsk = awgn(bpsk, 5)
def plot_input(input_sound):
    ax1.set_title('Generate random n-bit binary signal', fontproperties = zhfont1, fontsize = 20)
#    plt.axis([0, size, -0.5, 1.5])
    plt.plot(input_sound, 'b')
    
def plot_bpsk(bpsk):
    ax2.set_title('BPSK modulation signal', fontproperties=zhfont1, fontsize=20) #  width=0.5,
#    ax2.axis([0,size,-1.5, 1.5])
    ax2.plot(bpsk, 'r')
    
def plot_noised(noise_bpsk):
    ax3.set_title('BPSK modulated signal superimposed noise waveform', fontproperties = zhfont1, fontsize = 20)
#    ax3.axis([0, size, -1.5, 1.5])
    ax3.plot(noise_bpsk, 'r')
def yaz(quantization_level,noise_bpsk):
    bunu_yaz = np.int16(noise_bpsk/np.max(np.abs(noise_bpsk)) * 2**(quantization_level-1))
    write('bpsk.wav',Fs,bunu_yaz)