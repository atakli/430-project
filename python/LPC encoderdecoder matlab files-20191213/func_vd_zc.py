#function of "voicingDetector_zero_crossing_detector__hamza"
import numpy as np
def sign(a):
	y = np.sign(a)
	if complex(a).imag != 0:
		return a / abs(a)
	return y
def func_vd_zc(y):
	ZC = 0
	for n in range(len(y)):
		if n+2 > len(y):
			break
		ZC += (1/2) * abs( sign( y[n+1] ) - sign( y[n] ) )
	return ZC

# print('ZC from func_vd_zc: ',ZC)													# bu ne olum. gerek yok

# çok mühim olmamakla beraber if yapacağına for n in range(len(y)-1) denebilir belki, incele