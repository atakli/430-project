from udecode_uencode import udecode
from func_a_coeff_from_parcor import func_a_coeff_from_parcor
from math import ceil,floor
from f_DECODER import f_DECODER
import numpy as np
def LPC_rx_s(data_frame):
# len ve size vs'leri kontrol et 
	data_frame = np.uint16(data_frame)	# 65536'den büyük bi eleman varsa ne olacak?
	fs = 8000		# Sound sampling rate (not the sampling rate of the receiver, sampling rate of the recorded sound as a source file).
	fsize = 60e-3	# frame size	# BU NE?
	frame_length = round(fs * fsize)

	kk = 0
	synth_speech_agr = np.zeros(0)
	data_frame_agr = []

	variables = dir()[7:]							# esnek olmayabilir her zaman çalışmayabilir şüpheliyim

	while kk == 0:
		clearvars -except kk synth_speech_agr fs data_frame frame_length		# bence buna gerek yok 
																				# ama detaylı incelemedim

		# Decoding
		if data_frame.size > 0:
			break
		length_in_sec_bin_rec = data_frame[:10]
		length_in_sec_rec = np.double(bi2de(length_in_sec_bin_rec.T)) / 100
		if length_in_sec_rec < 1:
			kk = 1
		length_x = length_in_sec_rec * fs
		data_frame = np.delete(data_frame,np.arange(10))
		length_voiced_elements = round(length_in_sec_rec * fs / frame_length)

		max_parcor_bin_rec = data_frame[:7]
		max_parcor_dec = np.double(bi2de(max_parcor_bin_rec.T)) / 100
		data_frame = np.delete(data_frame,np.arange(7))

		gain_elements_max_bin_rec = data_frame[:7]
		gain_elements_max_dec = np.double(bi2de(gain_elements_max_bin_rec.T)) / 100
		data_frame = np.delete(data_frame,np.arange(7))

		pitch_unique_length_bin = data_frame[:10]
		pitch_unique_length = bi2de(pitch_unique_length_bin.T)
		data_frame = np.delete(data_frame,np.arange(10))

		pitch_unique_bin = data_frame[:pitch_unique_length]
		pitch_unique_binary_reshpd = pitch_unique_bin.reshape(10,pitch_unique_length/10)
		pitch_unique_decoded = bi2de(pitch_unique_binary_reshpd.T).T
		data_frame = np.delete(data_frame,np.arange(pitch_unique_length))	# arange'in içindeki float olmasa iyi olur
																			# though, hata vermiyor, kullanmasan iyi olur diyor
		voiced = data_frame[:length_voiced_elements]
		voiced = repelem(voiced,frame_length)
		data_frame[:length_voiced_elements] = np.delete(data_frame,np.arange(length_voiced_elements))

		binary_pitch_plot_single_dec = data_frame[:length_voiced_elements * 10]
		data_frame = np.delete(data_frame,np.arange(length_voiced_elements * 10))

		gain_elements_encoded_bit_single = data_frame[:length_voiced_elements * 12]
		data_frame = np.delete(data_frame,np.arange(length_voiced_elements * 12))

		acn = 'a_coeff_norm_'
		ebs = '_encoded_bit_single'
		for i,s in zip(range(1,11,1),[5,5,5,5,4,4,4,4,3,2]):
			globals()[acn+str(i)+ebs] = data_frame[:length_voiced_elements * s]
			data_frame = np.delete(data_frame,np.arange(length_voiced_elements * s))				#bu ne arkadaş ya, saçma değil mi

		for i,s in zip(range(1,11,1),[5,5,5,5,4,4,4,4,3,2]):
			globals()[acn+str(i)+ebs+'_reshaped'] = globals()[acn+str(i)+ebs].reshape(s,length_voiced_elements)
			globals()[acn+str(i)+'_encoded'] = bi2de(globals()[acn+str(i)+'_encoded_bit_single_reshaped'].T).T			#bi2de
			
		for i,s in zip(range(1,11,1),[5,5,5,5,4,4,4,4,3,2]):	
			globals()[acn+str(i)+'_decoded'] = udecode(globals()[acn+str(i)+'_encoded'],s) * max_parcor_dec	# udecode: not implemented yet

		son = np.zeros((1,len(a_coeff_norm_1_decoded)))
		for i in range(1,11,1):
			iki = [globals()[acn+str(i)+'_decoded']
			son = np.concatenate(son,iki)					# doğru axis olacak mı bilmiyorum, cmd'de 1,4lük matrixlerle denedim doğru oldu
		vec_len = son.shape[1]								
								 
		a_coeff_all_decoded = np.zeros((frame_length,vec_len))

		son = np.zeros((1,len(a_coeff_norm_1_decoded)))
		for i in range(1,11,1):
			iki = [globals()[acn+str(i)+'_decoded']
			son = np.concatenate(son,iki)					# doğru axis olacak mı bilmiyorum, cmd'de 1,4lük matrixlerle denedim doğru oldu
		a_coeff_all_decoded = son[0:11,:]					# son[1:11] de aynı şey python'da, ama matlabda farklı

		parcor_all_decoded_vec = a_coeff_all_decoded.reshape(1, a_coeff_all_decoded.shape[0] * a_coeff_all_decoded.shape[1])

		N = frame_length - 1
		for b in range(floor(length_x/frame_length)):
		#     y1=x(b:b+N);     %"b+N" denotes the end point of current frame.
		#                 %"y" denotes an array of the data points of the current 
		#                 %frame
		#     y = filter([1 -.9378], 1, y1);  %pre-emphasis filtering
		# 
		#     %aCoeff [LEVINSON-DURBIN METHOD];

			[a,tcount_of_aCoeff] = func_a_coeff_from_parcor(parcor_all_decoded_vec[b * frame_length : b * frame_length + 10])
			# e=error signal from lev-durb proc
			aCoeff_quant[b * frame_length : b * frame_length + 10] = a
			# aCoeff is array of "a" for whole "x"
		#     # GAIN;
		#         pitch_plot_b = pitch_plot(b); %pitch period
		#         voiced_b = voiced(b);
		#     gain(b) = f_GAIN (e, voiced_b, pitch_plot_b);

		gain_elements_decoded = np.zeros((1,frame_length * ceil(length_x/frame_length)))

		gain_elements_encoded_reshaped = gain_elements_encoded_bit_single.reshape(12,length_voiced_elements).T
		gain_elements_encoded_rec = bi2de(gain_elements_encoded_reshaped)
		if gain_elements_decoded.size / frame_length > gain_elements_encoded_rec.size:		
			gain_elements_decoded[:-frame_length:frame_length] = udecode(gain_elements_encoded_rec,6) * gain_elements_max_dec
		else:
			gain_elements_decoded[::frame_length] = udecode(gain_elements_encoded_rec,12) * gain_elements_max_dec

		binary_pitch_plot_reshaped = binary_pitch_plot_single_dec.reshape(10,length_voiced_elements).T

		binary_pitch_plot_decoded = bi2de(binary_pitch_plot_reshaped);

		pitch_unique_dec_dbl = np.double(pitch_unique_decoded)				# double np.double'a mı denk, kontrol et
		binary_pitch_plot_decoded_mapped = pitch_unique_dec_dbl(binary_pitch_plot_decoded);

		binary_pitch_plot_decoded_mapped_rep = repelem(binary_pitch_plot_decoded_mapped,frame_length);

		synth_speech = f_DECODER (aCoeff_quant, binary_pitch_plot_decoded_mapped_rep, voiced, gain_elements_decoded);

		#RESULTS,
		# de2beep
		#
		# disp('Press a key to play the original sound!');
		# pause;
		# soundsc(x, fs);
		# 
		# disp('Press a key to play the LPC compressed sound!');
		# pause;
		synth_speech_agr = np.append(synth_speech_agr,synth_speech)
	
	return synth_speech_agr