#function of "voicingDetector_zero_crossing_detector__hamza"

def func_vd_zc(y):
	ZC = 0
	for n in range(len(y)):
		if n+2 > length(y):
			break
		ZC += (1./2) .* abs(sign(y[n+1])-sign(y[n]))	# şu nokta meselesi ne ya
	return ZC

ZC;													# bu ne olum

# çok mühim olmamakla beraber if yapacağına for n in range(len(y)-1) denebilir belki, incele