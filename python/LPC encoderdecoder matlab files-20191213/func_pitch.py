# min_freq = 80;
# max_freq = 300;
# 
# period_max = round(fs / min_freq);
# period_min = round(fs / max_freq);
def func_pitch(y,fs):
	period_min = round (fs * 2e-3)  	# total data points in 2ms of "x", as min period of a female voice frame = 2ms
	period_max = round (fs * 20e-3)   	# as max period of a male voice frame : 20ms
# BODY OF PROGRAM
	R = np.correlate(y,y,mode='full')
	[R_max , R_mid] = max(enumerate(R),key=operator.itemgetter(0))	
	# R_max is the peak of "R", R_mid=(index of R_max) : the midpoint of "R"
	pitch_per_range = R[R_mid + period_min - 1 : R_mid + period_max]
	[R_max, R_mid] = max(enumerate(pitch_per_range),key=operator.itemgetter(0))
	pitch_period = R_mid + period_min
	return pitch_period