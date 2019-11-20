import numpy as np
import matplotlib.pyplot as plt
import pdb
from mplcursors import cursor as cs
pi = np.pi
""" Define transmitted signal """
N=100# % Number of bits , size of transmitted signal x_inp=[x_1 x_2 ... x_N] 
x_inp = np.random.randint(0,2,(1,N))#%(1,N)#  % binary signal 0 or 1 % message to be transmitted
preamble = np.array([0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0])
preamble_N = len(preamble)
N = preamble_N + N#		% toplam number of bits becomes 120
x_inp = np.append(x_inp,preamble)
Tb=0.0001# % bit period (second)  
""" Represent input signal as digital signal """
x_bit=np.empty(0)
# L = 100
nb=100# % bbit/bit		# heralde samples/bit ya. Total number of samples becomes N * nb = 12000
						# total duration of signal becomes 12000 * Tb = 1.2 sec as the real case.
for n in np.arange(0,N,1):	
	if x_inp[n]==1:
	   x_bit0 = np.ones((1,nb))
	else:
	   x_bit0 = np.zeros((1,nb))
	x_bit = np.append(x_bit,x_bit0)		# her loop'tan sonra ustune ekliyo

# x_bit = upsample(x_inp,L);
t1 = np.arange(0,nb*N*(Tb/nb),Tb/nb)		# time of the signal 
# pdb.set_trace()
# f1 = figure(1);
# set(f1,'color',[1 1 1]);
# plt.subplots(3,1,1); 
plt.plot(t1,x_bit,lineWidth=2)
plt.grid()
cs()
# axis([ 0 Tb*N -0.5 1.5]);
plt.ylabel('Amplitude(volt)');
plt.xlabel(' Time(sec)');
plt.title('Input signal as digital signal')
plt.show()

""" Define BFSK Modulation """
Ac = 5	# Amplitude of carrier signal
mc = 4	# fc>>fs fc=mc*fs fs=1/Tb
fc = mc*(1/Tb)	# carrier frequency for bit 1
fi1 = 0	   # carrier phase for bit 1
fi2 = pi	# carrier phase for bit 0
t2 = np.arange(0,Tb,Tb/nb)
len_t2 = len(t2)
x_mod=np.empty(0);
for i in np.arange(0,N,1):					# bu for'u np.where ve np.cos ile yapabilirim tahmin ediyorum
	if x_inp[i] == 1:
		x_mod0 = Ac*np.cos(2*pi*fc*t2+fi1)	# modulation signal with carrier signal 1
	else:
		x_mod0 = Ac*np.cos(2*pi*fc*t2+fi2)	# modulation signal with carrier signal 2
	x_mod = np.append(x_mod,x_mod0)

t3 = np.arange(0,Tb*N,Tb/nb)
# subplot(3,1,2);
# pdb.set_trace()
plt.plot(x_mod,lineWidth=2);
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude(volt)')
plt.title('Signal of BPSK modulation ')
plt.show()

# sound(x_mod)

