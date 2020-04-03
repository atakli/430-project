from udecode_uencode import uencode
from math import ceil,floor
from f_ENCODER import f_ENCODER
import numpy as np
def LPC_tx_s(x):
	
	fs = 8000
	kk = 0
	all_sig = x
	synth_speech_agr = []
	data_frame_agr = []

	while kk * fs < len(all_sig):
		# clearvars -except kk all_sig synth_speech_agr fs data_frame_agr
		x = all_sig[kk * fs : min((kk+1) * fs,len(all_sig))]
		if len(x) < fs / 10:
			break
		# LENGTH (IN SEC) OF INPUT WAVEFILE,
		t = len(x) / fs
		# sprintf('Processing the wavefile "%s"', inpfilenm)
		# sprintf('The wavefile is  %3.2f   seconds long', t)

		# THE ALGORITHM STARTS HERE
		M = 10  # prediction order
		[parcor, aCoeff, pitch_plot, voiced, gain] = f_ENCODER(x, fs, M)  # pitch_plot is pitch periods

		fsize = 60e-3    # frame size
		frame_length = round(fs * fsize)
		pitch_plot_elements = pitch_plot[::frame_length]
		voiced_elements = voiced[::frame_length]
		gain_elements = gain[::frame_length]
		gain_elements_max = max(gain_elements)
		gain_elements_normalized = gain_elements / gain_elements_max
		a_coeff_norm = parcor / max(abs(parcor))

		max_parcor = round(max(abs(parcor))*100)
		max_parcor_bin = de2bi(max_parcor,7)
		gain_elements_max_scaled = round(gain_elements_max*100)
		gain_elements_max_bin = de2bi(gain_elements_max_scaled,7)
		length_in_sec_scaled_binary = de2bi(round(t*100),10)

		pitch_unique = np.unique(pitch_plot_elements)
		[gec,idx] = np.in1d(pitch_plot_elements,pitch_unique)
		binary_pitch_plot = de2bi(idx,10).T
		binary_pitch_plot_single = binary_pitch_plot.copy()
		pitch_unique_binary = de2bi(pitch_unique,10).T
		pitch_unique_binary_vec = pitch_unique_binary.copy()
		pitch_unique_binary_vec_length = len(pitch_unique_binary_vec)
		pitch_unique_binary_vec_length_binary = de2bi(pitch_unique_binary_vec_length,10).T

		# Gain quantization
		# gain_elements_mapped=round((gain_elements_normalized) * 2^5);
		# gain_elements_mapped(gain_elements_mapped==2^5)=2^5-1;
		# 
		# gain_elements_quantized=dec2bin(gain_elements_mapped, 5) - '0';

		# All Quantizations
		no_of_bits = 12
		gain_elements_encoded = uencode(gain_elements_normalized,no_of_bits)

		gain_elements_encoded_bit = de2bi(gain_elements_encoded).T
		gain_elements_encoded_bit_single = gain_elements_encoded_bit.copy()

		# k_1, k_2 quantization
		acn = 'a_coeff_norm_'
		for i in range(1,11):
			globals()[acn+str(i)] = a_coeff_norm[(s+1)::frame_length]

		for i,no_of_bits in zip(range(1,11),[5,5,5,5,4,4,4,4,3,2]):
			globals()[acn+str(i)+'_encoded'] = uencode(globals()[acn+str(i)],no_of_bits)
			
		for i,no_of_bits in zip(range(1,11),[5,5,5,5,4,4,4,4,3,2]):
			globals()[acn+str(i)+'_encoded_bit'] = de2bi(globals()[acn+str(i)+'_encoded'],no_of_bits).T
			globals()[acn+str(i)+'_encoded_bit_single'] = globals()[acn+str(i)+'_encoded_bit'].copy()

		# Construct data frame 
		data_frame = np.concatenate(length_in_sec_scaled_binary.T,max_parcor_bin.T,gain_elements_max_bin.T, \
		pitch_unique_binary_vec_length_binary, pitch_unique_binary_vec, voiced_elements.T, \
		binary_pitch_plot_single, gain_elements_encoded_bit_single)
		for i in range(1,11,1):
			iki = globals()[acn+str(i)+'_encoded_bit_single']
			data_frame = np.concatenate(son,iki)		# doğru axis olacak mı bilmiyorum, cmd'de 1,4lük matrixlerle denedim doğru oldu		

		data_frame_agr = np.append(data_frame_agr,data_frame)
		kk = kk + 1
	return data_frame_agr