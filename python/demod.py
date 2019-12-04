import numpy as np
import matplotlib.pyplot as plt
import pdb
from mplcursors import cursor as cs
from scipy.io.wavfile import read
pi = np.pi
nb = 100  #şimdilik bildiğimi varsayıyorum
""" ********************* Transmitted signal x ****************************** """
Fs,y = read(r'C:\Users\Emre\Desktop\14.08.09_the_mechanic\ders\430\proje\430-project\python\test.wav')
time = np.arange(0,len(y))/Fs
plt.plot(time,y)
# ylim([-0.2 1.2])
plt.figure()
Tb_re = 1/Fs
""" ********************* Channel model h and w ***************************** """
# h=1 # Fading 
# w=0 # Noise
""" ********************* Received signal y ********************************* """
# y=h.*y+w
""" ********************* Define BPSK Demodulation ************************** """
y_dem = np.empty(0)
t = np.arange(0,Tb_re,Tb_re/nb)
t = t[:-1]
for n in np.arange(0,len(y),len(t)):
    c = np.cos(2*pi*fc*t) # carrier signal 
    y_dem0 = c * y[n : n+len(t)]
#    t4 = np.arange(0,Tb_re,Tb_re/nb)
    z = np.trapz(y_dem0,t) # integration 
    A_dem = np.round((2*z/Tb_re))                                     
    if A_dem>Ac/2: # logic level = Ac/2
        A=1
    else:
        A=0
    y_dem=[y_dem A]
end
x_out=y_dem # output signal
""" *************** Represent output signal as digital signal *************** """
xx_bit=[]
for n=1:length(x_out)
    if x_out(n)==1
       xx_bitt=ones(1,nb)
    else x_out(n)
        xx_bitt=zeros(1,nb)
    end
     xx_bit=[xx_bit xx_bitt]
end
t4=Tb_re/nb:Tb_re/nb:nb*length(x_out)*(Tb_re/nb)
# subplot(3,1,3)
plot(t4,xx_bit,'LineWidth',2)
plt.grid()
axis([ 0 Tb_re*length(x_out) -0.5 1.5])
ylabel('Amplitude(volt)')
xlabel(' Time(sec)')
title('Output signal as digital signal')
""" **************************** end of program ***************************** """