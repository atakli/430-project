# DECODER PORTION
from f_SYN_UV import f_SYN_UV
from f_SYN_V import f_SYN_V
def f_DECODER(aCoeff, pitch_plot, voiced, gain):
	# re-calculating frame_length for this decoder
	frame_length = 1
	for i in range(len(gain)):
		if gain[i] == 0:
			frame_length += 1
		else:
			break
	# decoding starts here
	synth_speech = np.zeros(frame_length-1)
	for b in range(0,min([len(aCoeff),len(voiced),len(gain),len(pitch_plot)]),frame_length): 
	# len(gain) should be very close (i.e less than a frame_length error) to len(x)

		# FRAME IS VOICED OR UNVOICED
		if voiced(b) == 1:   #voiced frame
			pitch_plot_b = pitch_plot[b]
			syn_y1 = f_SYN_V (aCoeff, gain, frame_length, pitch_plot_b, b)
		else:
			syn_y1 = f_SYN_UV (aCoeff, gain, frame_length, b) 	# unvoiced frame
		synth_speech = np.append(synth_speech,np.zeros(b))
		synth_speech[b:b+frame_length-1] = syn_y1
		
	return synth_speech