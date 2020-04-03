# a function of f_DEOCDER
from scipy.signal import lfilter
from numpy import floor
# clear all;
# frame_length = 480;
# pitch_plot_b = 92;

def f_SYN_V(aCoeff, gain, frame_length, pitch_plot_b, b):
	# creating pulsetrain
	ptrain = np.zeros(frame_length)			# python'da array'e assign etmeden önce define etmen gerekiyo, matlab gibi değil
	for f in range(frame_length):
		if f / pitch_plot_b == floor(f / pitch_plot_b):
			ptrain[f] = 1
		else:
			ptrain[f] = 0

	syn_y2 = lfilter(1, [1,aCoeff[b+1:b+1+9]], ptrain)
	syn_y1 = syn_y2 * gain(b)

	return syn_y1

# ;y/abs(y)