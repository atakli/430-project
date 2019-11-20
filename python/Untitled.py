# % ********************* Define transmitted signal *************************
N=100# % Number of bits , size of transmitted signal x_inp=[x_1 x_2 ... x_N] 
x_inp = randi([0,1],1,N)#%(1,N)#  % binary signal 0 or 1 % message to be transmitted
preamble_N = 20#
% preamble = randi([0,1],1,preamble_N)
preamble = [0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0]#
N = preamble_N + N#     % toplam number of bits becomes 120
x_inp = [x_inp preamble]#
% x_inp = [x_inp  preamble]#
Tb=0.0001# % bit period (second)  
# ********************* Represent input signal as digital signal ****
x_bit=[]
# L = 100
nb=100# % bbit/bit      # heralde samples/bit ya. Total number of samples becomes N * nb = 12000
                        # total duration of signal becomes 12000 * Tb = 1.2 sec as the real case.
for n in np.range(1,N+1,1):  
    if x_inp(n)==1:
       x_bitt = np.ones((1,nb))
    else:
        x_bitt = zeros((1,nb))
    x_bit += x_bitt		# her loop'tan sonra ustune ekliyo

# x_bit = upsample(x_inp,L);
t1=Tb/nb:Tb/nb:nb*N*(Tb/nb); % time of the signal 
f1 = figure(1);
set(f1,'color',[1 1 1]);
subplot(3,1,1);
plot(t1,x_bit,'lineWidth',2);grid on;
axis([ 0 Tb*N -0.5 1.5]);
ylabel('Tmplitude(volt)');
xlabel(' Time(sec)');
title('Input signal as digital signal');