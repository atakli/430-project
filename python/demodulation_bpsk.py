import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt
from scipy.io.wavfile import write,read
from auxiliary_module import filter,freq_resp

preamble = np.array([0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1,
0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],dtype=np.uint8)
# bpsk = LPC_rx_s('bpsk_de2.wav')
Fs,bpsk = read('bpsk_de2.wav')
fc = 4000
nb = 10
bpsk = bpsk[:(len(bpsk) - (len(bpsk) % nb))]
ts = np.arange(0, len(bpsk) / Fs, 1 / Fs)
coherent_carrier = np.cos(np.dot(2 * pi * fc, ts))
coherent_demod = bpsk * (coherent_carrier * 2)
def main(high=400,low=200):
	lowpass_out = filter(coherent_demod,high=high)
	filter_out = filter(lowpass_out,low=low,typ='highpass')

	filter_out = filter_out.reshape((int(len(filter_out)/nb),nb))
	tempF = np.sum(filter_out,axis=1)
	detection_bpsk3 = np.where(tempF > 0,1,0)
	
	packed_detection_bpsk = np.packbits(np.uint8(detection_bpsk3))
	#bunu_yaz = np.int16(detection_bpsk/np.max(np.abs(detection_bpsk)) * 2**(quantization_level-1))
	packed_detection_bpsk.tofile('dbpsk.wav')
	dbpsk1 = np.fromfile('dbpsk.wav',dtype = "int16")
	write('dbpsk1.wav',Fs,dbpsk1)
if __name__ == '__main__':
	main()