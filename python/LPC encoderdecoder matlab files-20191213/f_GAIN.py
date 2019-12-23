# function for calc gain per frame
from numpy import floor         
def f_GAIN(e, voiced_b, pitch_plot_b):              # gain of 1 (current) frame is returned
													# pitch_plot_b = pitch period of frame starting at data point "b"
	# GAIN
	if voiced_b == 0:    							# if frame starting at data point "b" is unvoiced
		denom = e.size
		power_b = sum( np.square(e[:denom]) ) / denom
		gain_b = np.sqrt( power_b )
	else:      # if frame starting at data point "b" is voiced
		denom = floor(e.size / pitch_plot_b ) * pitch_plot_b 	# see page 270 of main book
		power_b = sum( np.square(e[:denom]) ) / denom
		gain_b = np.sqrt( pitch_plot_b * power_b )
		
	# print('power_b from f_GAIN: ',power_b)	# bence gerek yok bunları yazdırmaya
	# print('gain_b from f_GAIN: ',gain_b)	# ihtiyaç olursa yazdırırız
	return gain_b, power_b