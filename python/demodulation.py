# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:04:58 2019

@author: Emre
"""
# As we all know, the toolbox of signal processing in matlab is very powerful, 
# but because of some real-time requirements for deep learning, bloggers have to go to python    ?????????
import numpy as np
from math import pi
from den import filter,freq_resp
from scipy.io.wavfile import read,write

quantization_level = 16
Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\bpsk_de.wav')
y_bpsk_de = np.fromfile(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\bpsk_de.wav',
                   dtype = "uint8")
y_bpsk_de_bytes = np.unpackbits(y_bpsk_de)
#print(Fs)
#time = np.arange(0,len(y))/Fs
#plt.plot(time,y)
ts = np.arange(0, len(y) / Fs, 1 / Fs)
ts_by = np.arange(0, len(y_bpsk_de_bytes) / Fs, 1 / Fs)
fc = 4000
coherent_carrier = np.cos(2 * pi * fc * ts)
coherent_carrier_by = np.cos(2 * pi * fc * ts_by)
multiplied = y * coherent_carrier * 2
multiplied_by = y_bpsk_de_bytes * coherent_carrier_by * 2
filtered_out = filter(multiplied,high=150,typ='lowpass')
#filtered_out = filter(multiplied,high=150,typ='lowpass')



# lowpass_out = np.int16(lowpass_out)             # etkisi var mı bilmiyorum
detection_bpsk = np.where(multiplied > 0,1,0)
packed_detection_bpsk = np.packbits(detection_bpsk)
#bunu_yaz = np.int16(detection_bpsk/np.max(np.abs(detection_bpsk)) * 2**(quantization_level-1))
packed_detection_bpsk.tofile('dbpsk.wav')
dbpsk1 = np.fromfile(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\dbpsk.wav',dtype = "int16")
write('dbpsk1.wav',Fs,dbpsk1)