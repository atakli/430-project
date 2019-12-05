# from IPython import get_ipython
# get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt
from mplcursors import cursor as cs
from scipy.io.wavfile import read
#import pdb
pi = np.pi
N = 120
nb = 100  #şimdilik bildiğimi varsayıyorum
""" ********************* Transmitted signal x ****************************** """
Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\test.wav')
time = np.arange(0,len(y))/Fs
plt.plot(time,y)
#plt.show(block=False)
# ylim([-0.2 1.2])
Tb_re = 1/Fs
fc = 4 * (1/Tb_re)	# carrier frequency for bit 1
""" ********************* Channel model h and w ***************************** """
# h=1 # Fading 
# w=0 # Noise
""" ********************* Received signal y ********************************* """
# y=h.*y+w
""" ********************* Define BPSK Demodulation ************************** """
y_dem = np.empty(0)
t = np.arange(0,Tb_re,Tb_re/nb)
t = t[:-1]
c = np.cos(2*pi*fc*t) # carrier signal 
for n in np.arange(0,len(y),len(t)):
    y_dem0 = c * y[n : n+len(t)]
#    t4 = np.arange(0,Tb_re,Tb_re/nb) # lan zaten aynısı niye bi daha tanımlıyosun
    z = np.trapz(y_dem0,t) # integration 
    A_dem = np.round(2*z/Tb_re)                                  
    if A_dem > 0: # logic level = Ac/2
        y_dem = np.append(y_dem,1)
    else:
        y_dem = np.append(y_dem,0)
t = np.arange(0, size, sampling_t) (0,10,0.01)
ts = np.arange(0, (nb * N) / Fs, 1 / Fs)
css = np.cos(2*pi*fc*ts) # carrier signal 
dene = css * y * 2
#plt.plot(dene)
t = 
detection_bpsk = np.zeros(len(t), dtype=np.float32)
flag = np.zeros(N, dtype=np.float32)

for i in range(10):
    tempF = 0
    for j in range(nb):
        tempF = tempF + dene[i * nb + j]
    if tempF > 0:
        flag[i] = 1
    else:
        flag[i] = 0
for i in range(N):
    if flag[i] == 0:
        for j in range(nb):
            detection_bpsk[i * nb + j] = 0
    else:
        for j in range(nb):
            detection_bpsk[i * nb + j] = 1
""" *************** Represent output signal as digital signal *************** """
xx_bit = np.empty(0)
for n in range(len(y_dem)):
    if y_dem[n] == 1:
       xx_bitt = np.ones((1,nb))
    else:
       xx_bitt = np.zeros((1,nb))
    xx_bit = np.append(xx_bit,xx_bitt)
# t4 = np.arange(0,nb,Tb_re/nb) * float('%e'%(len(y_dem) * (Tb_re/nb)))
t4 = np.arange(0,N * Tb_re,Tb_re/nb)
# subplot(3,1,3)
#pdb.set_trace()
plt.figure()
plt.plot(t4,xx_bit,lineWidth=2)
#plt.plot(t4[:12000],xx_bit)#,'LineWidth',2)
cs()
plt.grid()
#plt.axis([ 0 Tb_re*length(y_dem) -0.5 1.5])
#plt.xlim(0,Tb_re * len(y_dem))
#plt.ylim(-0.5,1.5)
plt.ylabel('Amplitude(volt)')
plt.xlabel(' Time(sec)')
plt.title('Output signal as digital signal')
plt.show()
""" **************************** end of program ***************************** """




