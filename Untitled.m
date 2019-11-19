% ********************* Define transmitted signal *************************
N=10; % Number of bits , size of transmitted signal x_inp=[x_1 x_2 ... x_N] 
x_inp= randi([0,1],1,N)%(1,N);  % binary signal 0 or 1 % message to be transmitted 
% x_inp = [x_inp  preamble];
Tb=0.0001; % bit period (second)   
% ********************* Represent input signal as digital signal ****
x_bit=[]; 
L = 100;
nb=100; % bbit/bit
for n=1:1:N   % 
    if x_inp(n)==1;  % 
       x_bitt=ones(1,nb);
    else x_inp(n)==0;
        x_bitt=zeros(1,nb);
    end
     x_bit=[x_bit x_bitt];		% her loop'tan sonra üstüne ekliyo
end
% x_bit = upsample(x_inp,L);
t1=Tb/nb:Tb/nb:nb*N*(Tb/nb); % time of the signal 
f1 = figure(1);
set(f1,'color',[1 1 1]);
subplot(3,1,1);
plot(t1,x_bit,'lineWidth',2);grid on;
axis([ 0 Tb*N -0.5 1.5]);
ylabel('Tmplitude(volt)');
xlabel(' Time(sec)');
title('Input signal as digital signal');

% ********************* Define BFSK Modulation ****************************
Ac=5;  % Amplitude of carrier signal
mc=4;  % fc>>fs fc=mc*fs fs=1/Tb
fc=mc*(1/Tb); % carrier frequency for bit 1
fi1=0; % carrier phase for bit 1
fi2=pi; % carrier phase for bit 0
t2=Tb/nb:Tb/nb:Tb;                 
t2L=length(t2);
x_mod=[];
for (i=1:1:N)
    if (x_inp(i)==1)
        x_mod0=Ac*cos(2*pi*fc*t2+fi1);%modulation signal with carrier signal 1
    else
        x_mod0=Ac*cos(2*pi*fc*t2+fi2);%modulation signal with carrier signal 2
    end
    x_mod=[x_mod x_mod0];
end
t3=Tb/nb:Tb/nb:Tb*N;
subplot(3,1,2);
plot(t3,x_mod);
xlabel('Time(sec)');
ylabel('Amplitude(volt)');
title('Signal of  BASK modulation ');