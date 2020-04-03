# a function of f_DEOCDER
import numpy as np
from scipy.signal import lfilter

def f_SYN_UV(aCoeff, gain, frame_length, b):
	wn = np.random.randn(1, frame_length)
	syn_y2 = lfilter(1, np.array([1,aCoeff[b+1:b+1+9]]), wn)
	syn_y1 = syn_y2 * gain[b]
	return syn_y1