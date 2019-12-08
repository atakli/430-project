# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:16:56 2019

@author: Emre
"""
import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt
import matplotlib,time
from scipy.io.wavfile import write,read
from den import filter,freq_resp
hepsi = time.time()
Fs,bpsk = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\bpsk_de2.wav')
fc = 4000
nb = 10
ts = np.arange(0, len(bpsk) / Fs, 1 / Fs)
coherent_carrier = np.cos(np.dot(2 * pi * fc, ts))
#bandpass_out = filter(bpsk,low=2000,high=6000,typ='bandpass')
coherent_demod = bpsk * (coherent_carrier * 2)
#coherent_demod = bandpass_out * (coherent_carrier * 2)
lowpass_out = filter(coherent_demod,high=400)
lowpass_out = filter(lowpass_out,low=200,typ='highpass')
#lowpass_out = coherent_demod
print('filtre bitti')
bas = time.time()

#lowpass_out = lowpass_out.reshape((int(len(lowpass_out)/nb),nb))
lowpass_out = lowpass_out[:6187000].reshape((int(len(lowpass_out[:6187000])/nb),nb))
tempF = np.sum(lowpass_out,axis=1)
detection_bpsk3 = np.where(tempF > 0,1,0)

print('süre: ',time.time()-bas)
#    plt.plot(t, detection_bpsk, 'r')
#    plt.plot(t, m, 'b')
bas = time.time()
packed_detection_bpsk = np.packbits(np.uint8(detection_bpsk3))
#bunu_yaz = np.int16(detection_bpsk/np.max(np.abs(detection_bpsk)) * 2**(quantization_level-1))
packed_detection_bpsk.tofile('dbpsk.wav')
dbpsk1 = np.fromfile(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\dbpsk.wav',dtype = "int16")
write('dbpsk1.wav',Fs,dbpsk1)
print('süre np.byte filan: ',time.time()-bas)
#    Fs_son,y_son = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\dbpsk1.wav')
print('bütün süre: ',time.time()-hepsi)
