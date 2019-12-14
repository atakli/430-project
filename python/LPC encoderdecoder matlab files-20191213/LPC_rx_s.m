function synth_speech_agr=LPC_rx_s(data_frame)

data_frame=uint16(data_frame);
fs=8000; % Sound sampling rate (not the sampling rate of the receiver, sampling rate of the recorded sound as a source file).
fsize = 60e-3;    %frame size
frame_length = round(fs .* fsize); 


kk=0;
synth_speech_agr=[];
data_frame_agr=[];

while(kk==0)
    clearvars -except kk synth_speech_agr fs data_frame frame_length

%Decoding
if isempty(data_frame)
    break
end
length_in_sec_bin_rec=data_frame(1:10);
length_in_sec_rec=double(bi2de(length_in_sec_bin_rec.'))/100;
if length_in_sec_rec<1
    kk=1;
end
length_x=length_in_sec_rec*fs;
data_frame(1:10)=[];
length_voiced_elements=round(length_in_sec_rec*fs/frame_length);

max_parcor_bin_rec=data_frame(1:7);
max_parcor_dec=double(bi2de(max_parcor_bin_rec.'))/100;
data_frame(1:7)=[];

gain_elements_max_bin_rec=data_frame(1:7);
gain_elements_max_dec=double(bi2de(gain_elements_max_bin_rec.'))/100;
data_frame(1:7)=[];

pitch_unique_length_bin=data_frame(1:10);
pitch_unique_length=bi2de(pitch_unique_length_bin.');
data_frame(1:10)=[];

%
pitch_unique_bin=data_frame(1:pitch_unique_length);
pitch_unique_binary_reshpd=reshape(pitch_unique_bin,10,pitch_unique_length/10);
pitch_unique_decoded=bi2de(pitch_unique_binary_reshpd.').';
data_frame(1:pitch_unique_length)=[];

voiced=data_frame(1:length_voiced_elements);
voiced=repelem(voiced,frame_length);
data_frame(1:length_voiced_elements)=[];

binary_pitch_plot_single_dec=data_frame(1:length_voiced_elements*10);
data_frame(1:length_voiced_elements*10)=[];

gain_elements_encoded_bit_single=data_frame(1:length_voiced_elements*12);
data_frame(1:length_voiced_elements*12)=[];

a_coeff_norm_1_encoded_bit_single=data_frame(1:length_voiced_elements*5);
data_frame(1:length_voiced_elements*5)=[];

a_coeff_norm_2_encoded_bit_single=data_frame(1:length_voiced_elements*5);
data_frame(1:length_voiced_elements*5)=[];

a_coeff_norm_3_encoded_bit_single=data_frame(1:length_voiced_elements*5);
data_frame(1:length_voiced_elements*5)=[];

a_coeff_norm_4_encoded_bit_single=data_frame(1:length_voiced_elements*5);
data_frame(1:length_voiced_elements*5)=[];

a_coeff_norm_5_encoded_bit_single=data_frame(1:length_voiced_elements*4);
data_frame(1:length_voiced_elements*4)=[];

a_coeff_norm_6_encoded_bit_single=data_frame(1:length_voiced_elements*4);
data_frame(1:length_voiced_elements*4)=[];

a_coeff_norm_7_encoded_bit_single=data_frame(1:length_voiced_elements*4);
data_frame(1:length_voiced_elements*4)=[];

a_coeff_norm_8_encoded_bit_single=data_frame(1:length_voiced_elements*4);
data_frame(1:length_voiced_elements*4)=[];

a_coeff_norm_9_encoded_bit_single=data_frame(1:length_voiced_elements*3);
data_frame(1:length_voiced_elements*3)=[];

a_coeff_norm_10_encoded_bit_single=data_frame(1:length_voiced_elements*2);
data_frame(1:length_voiced_elements*2)=[];

a_coeff_norm_1_encoded_bit_single_reshaped=reshape(a_coeff_norm_1_encoded_bit_single,5,length_voiced_elements);
a_coeff_norm_1_encoded=bi2de(a_coeff_norm_1_encoded_bit_single_reshaped.').';

a_coeff_norm_2_encoded_bit_single_reshaped=reshape(a_coeff_norm_2_encoded_bit_single,5,length_voiced_elements);
a_coeff_norm_2_encoded=bi2de(a_coeff_norm_2_encoded_bit_single_reshaped.').';

a_coeff_norm_3_encoded_bit_single_reshaped=reshape(a_coeff_norm_3_encoded_bit_single,5,length_voiced_elements);
a_coeff_norm_3_encoded=bi2de(a_coeff_norm_3_encoded_bit_single_reshaped.').';

a_coeff_norm_4_encoded_bit_single_reshaped=reshape(a_coeff_norm_4_encoded_bit_single,5,length_voiced_elements);
a_coeff_norm_4_encoded=bi2de(a_coeff_norm_4_encoded_bit_single_reshaped.').';

a_coeff_norm_5_encoded_bit_single_reshaped=reshape(a_coeff_norm_5_encoded_bit_single,4,length_voiced_elements);
a_coeff_norm_5_encoded=bi2de(a_coeff_norm_5_encoded_bit_single_reshaped.').';

a_coeff_norm_6_encoded_bit_single_reshaped=reshape(a_coeff_norm_6_encoded_bit_single,4,length_voiced_elements);
a_coeff_norm_6_encoded=bi2de(a_coeff_norm_6_encoded_bit_single_reshaped.').';

a_coeff_norm_7_encoded_bit_single_reshaped=reshape(a_coeff_norm_7_encoded_bit_single,4,length_voiced_elements);
a_coeff_norm_7_encoded=bi2de(a_coeff_norm_7_encoded_bit_single_reshaped.').';

a_coeff_norm_8_encoded_bit_single_reshaped=reshape(a_coeff_norm_8_encoded_bit_single,4,length_voiced_elements);
a_coeff_norm_8_encoded=bi2de(a_coeff_norm_8_encoded_bit_single_reshaped.').';

a_coeff_norm_9_encoded_bit_single_reshaped=reshape(a_coeff_norm_9_encoded_bit_single,3,length_voiced_elements);
a_coeff_norm_9_encoded=bi2de(a_coeff_norm_9_encoded_bit_single_reshaped.').';

a_coeff_norm_10_encoded_bit_single_reshaped=reshape(a_coeff_norm_10_encoded_bit_single,2,length_voiced_elements);
a_coeff_norm_10_encoded=bi2de(a_coeff_norm_10_encoded_bit_single_reshaped.').';


a_coeff_norm_1_decoded=udecode(a_coeff_norm_1_encoded,5)*max_parcor_dec;
a_coeff_norm_2_decoded=udecode(a_coeff_norm_2_encoded,5)*max_parcor_dec;
a_coeff_norm_3_decoded=udecode(a_coeff_norm_3_encoded,5)*max_parcor_dec;
a_coeff_norm_4_decoded=udecode(a_coeff_norm_4_encoded,5)*max_parcor_dec;
a_coeff_norm_5_decoded=udecode(a_coeff_norm_5_encoded,4)*max_parcor_dec;
a_coeff_norm_6_decoded=udecode(a_coeff_norm_6_encoded,4)*max_parcor_dec;
a_coeff_norm_7_decoded=udecode(a_coeff_norm_7_encoded,4)*max_parcor_dec;
a_coeff_norm_8_decoded=udecode(a_coeff_norm_8_encoded,4)*max_parcor_dec;
a_coeff_norm_9_decoded=udecode(a_coeff_norm_9_encoded,3)*max_parcor_dec;
a_coeff_norm_10_decoded=udecode(a_coeff_norm_10_encoded,2)*max_parcor_dec;



vec_len=size([zeros(1, length(a_coeff_norm_1_decoded)); a_coeff_norm_1_decoded;a_coeff_norm_2_decoded;a_coeff_norm_3_decoded;a_coeff_norm_4_decoded ...
                             ;a_coeff_norm_5_decoded;a_coeff_norm_6_decoded;a_coeff_norm_7_decoded;a_coeff_norm_8_decoded...
                             ;a_coeff_norm_9_decoded;a_coeff_norm_10_decoded],2);
                         
a_coeff_all_decoded=zeros(frame_length,vec_len);


a_coeff_all_decoded(1:11,:)=[zeros(1, length(a_coeff_norm_1_decoded)); a_coeff_norm_1_decoded;a_coeff_norm_2_decoded;a_coeff_norm_3_decoded;a_coeff_norm_4_decoded ...
                             ;a_coeff_norm_5_decoded;a_coeff_norm_6_decoded;a_coeff_norm_7_decoded;a_coeff_norm_8_decoded...
                             ;a_coeff_norm_9_decoded;a_coeff_norm_10_decoded];

parcor_all_decoded_vec=reshape(a_coeff_all_decoded,[1, size(a_coeff_all_decoded,1)*size(a_coeff_all_decoded,2)]);

N= frame_length - 1;
for b=1 : floor(length_x/frame_length)
%     y1=x(b:b+N);     %"b+N" denotes the end point of current frame.
%                 %"y" denotes an array of the data points of the current 
%                 %frame
%     y = filter([1 -.9378], 1, y1);  %pre-emphasis filtering
% 
%     %aCoeff [LEVINSON-DURBIN METHOD];

    [a,tcount_of_aCoeff] = func_a_coeff_from_parcor (parcor_all_decoded_vec(1+(b-1)*frame_length:(b-1)*frame_length+11)); %e=error signal from lev-durb proc
    aCoeff_quant(1+(b-1)*frame_length:(b-1)*frame_length+11) = a;  %aCoeff is array of "a" for whole "x"
%     %GAIN;
%         pitch_plot_b = pitch_plot(b); %pitch period
%         voiced_b = voiced(b);
%     gain(b) = f_GAIN (e, voiced_b, pitch_plot_b);
end



gain_elements_decoded=zeros(1,frame_length*ceil(length_x/frame_length));


gain_elements_encoded_reshaped=reshape(gain_elements_encoded_bit_single,12,length_voiced_elements).';
gain_elements_encoded_rec=bi2de(gain_elements_encoded_reshaped);

if length(gain_elements_decoded)/frame_length>length(gain_elements_encoded_rec)
gain_elements_decoded(1:frame_length:end-frame_length)=udecode(gain_elements_encoded_rec,6)*gain_elements_max_dec;
else
gain_elements_decoded(1:frame_length:end)=udecode(gain_elements_encoded_rec,12)*gain_elements_max_dec;
end



binary_pitch_plot_reshaped=reshape(binary_pitch_plot_single_dec,10,length_voiced_elements).';

binary_pitch_plot_decoded=bi2de(binary_pitch_plot_reshaped);

pitch_unique_dec_dbl=double(pitch_unique_decoded);
binary_pitch_plot_decoded_mapped=pitch_unique_dec_dbl(binary_pitch_plot_decoded);

binary_pitch_plot_decoded_mapped_rep=repelem(binary_pitch_plot_decoded_mapped,frame_length);



synth_speech = f_DECODER (aCoeff_quant, binary_pitch_plot_decoded_mapped_rep, voiced, gain_elements_decoded);


%RESULTS,
% de2beep

% disp('Press a key to play the original sound!');
% pause;
% soundsc(x, fs);
% 
% disp('Press a key to play the LPC compressed sound!');
% pause;
synth_speech_agr=[synth_speech_agr synth_speech]; 

end
end