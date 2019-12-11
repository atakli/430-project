import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt
import matplotlib,time
from scipy.io.wavfile import write,read
from auxiliary_module import filter,freq_resp

def main():
	Fs,y_den = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den.wav')
	y_den = y_den[:,0]
	#result = filter(y_den,low=50,high=150,typ='bandpass')
	write('den0.wav',Fs,y_den)
	y_b = np.fromfile(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\den0.wav',
						  dtype = "uint8")
	y_bytes = np.unpackbits(y_b)
	sampling_t = 0.1
	nb = int(1/sampling_t)
	t = np.arange(0, len(y_bytes), sampling_t)
	t_floor = np.int64(np.floor(t))
	m = y_bytes[t_floor]
	quantization_level = 16
	fc = 4000
	ts = np.arange(0, 1 / sampling_t * len(y_bytes) / Fs, 1 / Fs)
	bpsk = np.cos(np.dot(2 * pi * fc, ts) + pi * (m - 1))
	bunu_yaz = np.int16(bpsk/np.max(np.abs(bpsk)) * 2**(quantization_level-1))
	write('bpsk_de.wav',Fs,bunu_yaz)
	
def random():
	
	size = 10
	#sampling_t = 1/Fs
	sampling_t = 0.1
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
	return m
if __name__ == '__main__':
	main()