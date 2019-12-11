import numpy as np
from math import pi
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fftpack import fft,fftfreq

Fs = 44100
def freq_resp(sig,plot=True,label=None):
    datafft = fft(sig)
    fftabs = abs(datafft)
    samples = sig.shape[0]
    freqs = fftfreq(samples,1/Fs)
#    print(freqs[np.where(fftabs == np.max(fftabs))][0])
    if plot == True:
        plt.plot(freqs,fftabs)
        plt.title('Frequency Response')
def filter(sig,order=5,low=50,high=200,plot=False,typ='lowpass'):
# Filter out-of-band noise by bandpass filter
# bandpass_out = signal.filtfilt(b11, a11, y)
# Coherent demodulation, multiplied by coherent carrier in phase with the same frequency
# coherent_demod = bandpass_out * (coherent_carrier * 2)
    if typ == 'lowpass':
        [b,a] = signal.ellip(order, 0.5, 60, (high * 2 / Fs), btype = 'lowpass', analog = False, output = 'ba')
    elif typ == 'highpass':
        [b,a] = signal.ellip(order, 0.5, 60, (low * 2 / Fs), btype = 'highpass', analog = False, output = 'ba') 
    else:
        [b,a] = signal.ellip(order, 0.5, 60, [low * 2 / Fs, high * 2 / Fs], btype = 'bandpass', analog = False, output = 'ba') 
    result = signal.filtfilt(b, a, sig)
    if plot == True:
        plt.plot(result)    
    return result