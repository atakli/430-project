# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:35:53 2019
@author: Emre
"""
# -*- coding:utf-8 -*-
import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt
import matplotlib,os
from scipy.io.wavfile import write,read
from playsound import playsound

zhfont1 = matplotlib.font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
#def to_bits(quantization_level):
#    bits_list = []
#    for index in range(2 ** quantization_level):
#        bits = [index & (2 ** k) for k in range(quantization_level)]
#        bits_list.append(tuple((1 if b else 0) for b in bits))
#        return dict((i, bits) for i, bits in enumerate(bits_list))

def dosyadan_oku():
    Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den.wav')
    write('den0.wav',Fs,y[:,0])
    y_b = np.fromfile(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den0.wav',
                          dtype = "uint8")
    y_bytes = np.unpackbits(y_b)
    file_stats = os.stat(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den0.wav')
    quantization_level = int(file_stats.st_size * 8 / y.shape[0]) # how many bits used to represent every sample
#    quantization_level = 16 # 16 : 64 kbytes    # olmadı düzelt
    fc = 400
    ts = np.arange(0, len(y_bytes) / Fs, 1 / Fs)
    bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (y_bytes - 1))
    bunu_yaz = np.int16(bpsk/np.max(np.abs(bpsk)) * 2**(quantization_level-1))
#    packed_bpsk = np.packbits(bpsk)
    write('bpsk_de.wav',Fs,bunu_yaz)
#    playsound('bpsk_de.wav')
    fig, ax = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=1)
    plot_input(ax,y[:,0])
    plot_bpsk(ax,bpsk)
    
def random():
    
    size = 100 # 10
    #sampling_t = 1/Fs
    sampling_t = 0.01
    nb = 1 / sampling_t
    quantization_level = 16 # 16 : 64 kbytes
    t = np.arange(0, size, sampling_t)
    
    # Define additive white Gaussian noise
    def awgn(y, snr):
    
        snr = 10 ** (snr / 10.0)
        xpower = np.sum(y ** 2) / len(y)
        npower = xpower / snr
        return np.random.randn(len(y)) * np.sqrt(npower) + y
    
     # Randomly generated signal sequence
    a = np.random.randint(0, 2, size)
    m = np.zeros(int(size * nb), dtype=np.float32)
    for i in range(int(size * nb)):
        m[i] = a[floor(t[i])]
        
    fc = 4000
    Fs = 20 * fc # sampling frequency
    ts = np.arange(0, (nb * size) / Fs, 1 / Fs)
     # BPSK modulated signal waveform
    bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (m - 1))
     # AWGN noise
    noise_bpsk = awgn(bpsk, 5)
    yaz_ve_cal(quantization_level,noise_bpsk,Fs)
    fig, ax = plt.subplots(3, 1)
    fig.subplots_adjust(hspace=1)
    plot_input(ax,m)
    plot_bpsk(ax,bpsk)
    plot_noised(ax,noise_bpsk)
    
def plot_input(ax,input_sound):
    ax[0].set_title('Generated random n-bit binary signal', fontproperties = zhfont1, fontsize = 20)
#    plt.axis([0, size, -0.5, 1.5])
    ax[0].plot(input_sound, 'b')
    
def plot_bpsk(ax,bpsk):
    ax[1].set_title('BPSK modulated signal', fontproperties=zhfont1, fontsize=20) #  width=0.5,
#    ax2.axis([0,size,-1.5, 1.5])
    ax[1].plot(bpsk, 'r')
    
def plot_noised(ax,noise_bpsk):
    ax[2].set_title('BPSK modulated signal superimposed noise waveform', fontproperties = zhfont1, fontsize = 20)
#    ax3.axis([0, size, -1.5, 1.5])
    ax[2].plot(noise_bpsk, 'r')
    
def yaz_ve_cal(quantization_level,noise_bpsk,Fs):
    bunu_yaz = np.int16(noise_bpsk/np.max(np.abs(noise_bpsk)) * 2**(quantization_level-1))
    write('bpsk.wav',Fs,bunu_yaz)
    playsound('bpsk.wav')
dosyadan_oku()