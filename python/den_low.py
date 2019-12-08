import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000  # Sampling frequency
# Generate the time vector properly
t = np.arange(1000) / fs
signala = np.sin(2*np.pi*100*t) # with frequency of 100
# plt.plot(t, signala, label='a')

signalb = np.sin(2*np.pi*20*t) # frequency 20
# plt.plot(t, signalb, label='b')

signalc = signala + signalb
# plt.plot(t, signalc, label='c')

fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b0, a0 = signal.butter(5, w, 'low')
b4, a4 = signal.butter(1, w, 'low')
output0 = signal.filtfilt(b0, a0, signalc)
output4 = signal.filtfilt(b4, a4, signalc)
plt.plot(t, output0, label='filtered0')
plt.plot(t, output4, label='filtered4')
plt.legend()
plt.show()