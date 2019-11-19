% ********************* Transmitted signal x ******************************
% x=x_mod;
[y,Fs] = audioread('Ses002.amr');
time=(1:length(y))/Fs;
x=y;
plot(time,y);

figure;
nb=1/Fs;
% Tb = ;
% ********************* Channel model h and w *****************************
% h=1; % Fading 
% w=0; % Noise
% ********************* Received signal y *********************************
% y=h.*x+w;
% ********************* Define BPSK Demodulation **************************
y_dem=[];
for n=t2L:t2L:length(y)
  t=Tb/nb:Tb/nb:Tb;
  c=cos(2*pi*fc*t); % carrier siignal 
  y_dem0=c.*y((n-(t2L-1)):n);
  t4=Tb/nb:Tb/nb:Tb;
  z=trapz(t4,y_dem0); % intregation 
  A_dem=round((2*z/Tb));                                     
  if(A_dem>Ac/2) % logic level = Ac/2
    A=1;
  else
    A=0;
  end
  y_dem=[y_dem A];
end
x_out=y_dem; % output signal;
% *************** Represent output signal as digital signal ***************
xx_bit=[];
for n=1:length(x_out);
    if x_out(n)==1;
       xx_bitt=ones(1,nb);
    else x_out(n)==0;
        xx_bitt=zeros(1,nb);
    end
     xx_bit=[xx_bit xx_bitt];
end
t4=Tb/nb:Tb/nb:nb*length(x_out)*(Tb/nb);
subplot(3,1,3)
plot(t4,xx_bit,'LineWidth',2);grid on;
axis([ 0 Tb*length(x_out) -0.5 1.5]);
ylabel('Amplitude(volt)');
xlabel(' Time(sec)');
title('Output signal as digital signal');
% **************************** end of program *****************************