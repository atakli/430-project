function data_frame_agr=LPC_tx_s(x)

fs=8000;
kk=0;
all_sig=x;
synth_speech_agr=[];
data_frame_agr=[];

while(kk*fs<length(all_sig))
    clearvars -except kk all_sig synth_speech_agr fs data_frame_agr
    x=all_sig(kk*fs+1:min((kk+1)*fs,length(all_sig)));
    if (length(x)<fs/10)
        break
    end
%LENGTH (IN SEC) OF INPUT WAVEFILE,
t=length(x)./fs;
% sprintf('Processing the wavefile "%s"', inpfilenm)
% sprintf('The wavefile is  %3.2f   seconds long', t)


%THE ALGORITHM STARTS HERE,
M=10 ;  %prediction order
[parcor, aCoeff, pitch_plot, voiced, gain] = f_ENCODER(x, fs, M);  %pitch_plot is pitch periods


fsize = 60e-3;    %frame size
frame_length = round(fs .* fsize); 
pitch_plot_elements=pitch_plot(1:frame_length:end);
voiced_elements=voiced(1:frame_length:end);
gain_elements=gain(1:frame_length:end);
gain_elements_max=max(gain_elements);
gain_elements_normalized=gain_elements./gain_elements_max;
a_coeff_norm=parcor./max(abs(parcor));

max_parcor=round(max(abs(parcor))*100);
max_parcor_bin=de2bi(max_parcor,7);
gain_elements_max_scaled=round(gain_elements_max*100);
gain_elements_max_bin=de2bi(gain_elements_max_scaled,7);
length_in_sec_scaled_binary=de2bi(round(t*100),10);

pitch_unique=unique(pitch_plot_elements);
[~,idx] = ismember(pitch_plot_elements,pitch_unique);
binary_pitch_plot=de2bi(idx,10).';
binary_pitch_plot_single=binary_pitch_plot(:);
pitch_unique_binary=de2bi(pitch_unique,10).';
pitch_unique_binary_vec=pitch_unique_binary(:);
pitch_unique_binary_vec_length=length(pitch_unique_binary_vec);
pitch_unique_binary_vec_length_binary=de2bi(pitch_unique_binary_vec_length,10).';




% Gain quantization
% gain_elements_mapped=round((gain_elements_normalized) * 2^5);
% gain_elements_mapped(gain_elements_mapped==2^5)=2^5-1;
% 
% gain_elements_quantized=dec2bin(gain_elements_mapped, 5) - '0';

%All Quantizations
no_of_bits=12;
gain_elements_encoded=uencode(gain_elements_normalized,no_of_bits);

gain_elements_encoded_bit=de2bi(gain_elements_encoded).';
gain_elements_encoded_bit_single=gain_elements_encoded_bit(:);

% k_1, k_2 quantization
no_of_bits=5;
a_coeff_norm_1=a_coeff_norm(2:frame_length:end);
a_coeff_norm_2=a_coeff_norm(3:frame_length:end);
a_coeff_norm_3=a_coeff_norm(4:frame_length:end);
a_coeff_norm_4=a_coeff_norm(5:frame_length:end);

a_coeff_norm_1_encoded=uencode(a_coeff_norm_1,no_of_bits);
a_coeff_norm_2_encoded=uencode(a_coeff_norm_2,no_of_bits);
a_coeff_norm_3_encoded=uencode(a_coeff_norm_3,no_of_bits);
a_coeff_norm_4_encoded=uencode(a_coeff_norm_4,no_of_bits);

a_coeff_norm_1_encoded_bit=de2bi(a_coeff_norm_1_encoded,no_of_bits).';
a_coeff_norm_1_encoded_bit_single=a_coeff_norm_1_encoded_bit(:);
a_coeff_norm_2_encoded_bit=de2bi(a_coeff_norm_2_encoded,no_of_bits).';
a_coeff_norm_2_encoded_bit_single=a_coeff_norm_2_encoded_bit(:);
a_coeff_norm_3_encoded_bit=de2bi(a_coeff_norm_3_encoded,no_of_bits).';
a_coeff_norm_3_encoded_bit_single=a_coeff_norm_3_encoded_bit(:);
a_coeff_norm_4_encoded_bit=de2bi(a_coeff_norm_4_encoded,no_of_bits).';
a_coeff_norm_4_encoded_bit_single=a_coeff_norm_4_encoded_bit(:);

no_of_bits=4;
a_coeff_norm_5=a_coeff_norm(6:frame_length:end);
a_coeff_norm_6=a_coeff_norm(7:frame_length:end);
a_coeff_norm_7=a_coeff_norm(8:frame_length:end);
a_coeff_norm_8=a_coeff_norm(9:frame_length:end);

a_coeff_norm_5_encoded=uencode(a_coeff_norm_5,no_of_bits);
a_coeff_norm_6_encoded=uencode(a_coeff_norm_6,no_of_bits);
a_coeff_norm_7_encoded=uencode(a_coeff_norm_7,no_of_bits);
a_coeff_norm_8_encoded=uencode(a_coeff_norm_8,no_of_bits);

a_coeff_norm_5_encoded_bit=de2bi(a_coeff_norm_5_encoded,no_of_bits).';
a_coeff_norm_5_encoded_bit_single=a_coeff_norm_5_encoded_bit(:);
a_coeff_norm_6_encoded_bit=de2bi(a_coeff_norm_6_encoded,no_of_bits).';
a_coeff_norm_6_encoded_bit_single=a_coeff_norm_6_encoded_bit(:);
a_coeff_norm_7_encoded_bit=de2bi(a_coeff_norm_7_encoded,no_of_bits).';
a_coeff_norm_7_encoded_bit_single=a_coeff_norm_7_encoded_bit(:);
a_coeff_norm_8_encoded_bit=de2bi(a_coeff_norm_8_encoded,no_of_bits).';
a_coeff_norm_8_encoded_bit_single=a_coeff_norm_8_encoded_bit(:);

no_of_bits=3;
a_coeff_norm_9=a_coeff_norm(10:frame_length:end);

a_coeff_norm_9_encoded=uencode(a_coeff_norm_9,no_of_bits);

a_coeff_norm_9_encoded_bit=de2bi(a_coeff_norm_9_encoded,no_of_bits).';
a_coeff_norm_9_encoded_bit_single=a_coeff_norm_9_encoded_bit(:);

no_of_bits=2;
a_coeff_norm_10=a_coeff_norm(11:frame_length:end);

a_coeff_norm_10_encoded=uencode(a_coeff_norm_10,no_of_bits);

a_coeff_norm_10_encoded_bit=de2bi(a_coeff_norm_10_encoded,no_of_bits).';
a_coeff_norm_10_encoded_bit_single=a_coeff_norm_10_encoded_bit(:);

% Construct data frame 
data_frame=[length_in_sec_scaled_binary.'; max_parcor_bin.'; gain_elements_max_bin.'; pitch_unique_binary_vec_length_binary; pitch_unique_binary_vec; voiced_elements.'; binary_pitch_plot_single; gain_elements_encoded_bit_single; a_coeff_norm_1_encoded_bit_single; a_coeff_norm_2_encoded_bit_single; a_coeff_norm_3_encoded_bit_single;...
    a_coeff_norm_4_encoded_bit_single; a_coeff_norm_5_encoded_bit_single; a_coeff_norm_6_encoded_bit_single; a_coeff_norm_7_encoded_bit_single; a_coeff_norm_8_encoded_bit_single;....
    a_coeff_norm_9_encoded_bit_single; a_coeff_norm_10_encoded_bit_single];

data_frame_agr=[data_frame_agr; data_frame];
kk=kk+1;
end

end