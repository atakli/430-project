# This m file is for locating a good enough "M". For a good value of "M",
# "PG" will be high. But it also adds computational load as we increase "M".
# Run this for different frames of "x" and see for yourself. Define the 
# starting values of frames by defining a value to "b" at line 25.
# 
# Here,  array of "k"=Reflection C-oefficients
#        array of "a"=LPCs
#        array of "R"=autocorrelation co-efficients
# every notation is according to page 112 [chapter4] of Speech Coding
# Algorithms by W. C. Chu.
# 
# the indexes in this code is "+1" from the indexes in the book in some
# cases because there is no index "0" in matlab
from scipy.signal import lfilter
from scipy.io.wavfile import write,read
# clear all

for M in range(2:100):
    
	# INITIALIZATION:
	inpfilenm = 's1ofwb.wav'
	fs, x = read(inpfilenm)						# "t_16k_2s.wav" is the file I used. Change accordingly.
	# length(x)
	b = 3841        							# index no. of starting data point of current frame
	fsize = 30e-3	    						# frame size
	frame_length = round(fs * fsize)  			# number of data points in each framesize of "x"
	N = frame_length - 1        				# N+1 = frame length = number of data points in each frame
	sk = 0       								# initializing summartion term "sk"
	a = np.concatenate((np.zeros((M+1,M+1)),np.zeros((M+1,M+1)))) 				# defining a matrix of zeros for "a" for init.
	# a'yı niye böyle amelece tanımlamış? Bi hikmeti vardır heralde. Ama matlabcılara güven olmaz
	# FRAME SEGMENTATION:
	y1 = x[b-1:b+N]	    						# "b+N" denotes the end point of current frame.
												# "y" denotes an array of the data points of the current frame
	y = lfilter([1 -.9378], 1, y1)  			# pre-emphasis filtering

	# MAIN BODY OF THIS PROGRAM STARTS FROM HERE>>>>>>>>>>>>>>
	z = np.correlate(y,y,mode='full')

	# finding array of R[l]
	R = z[ (len(z)+1) / 2 - 1 : len(z)] 		# R=array of "R[l]", where l=0,1,2,
												# ...(b+N)-1
												# R(1)=R[lag=0], R(2)=R[lag=1], 
												# R(3)=R[lag=2]... etc 

	# GETTING OTHER PARAMETERS OF PREDICTOR OF ORDER "0":
	s = 1        								# step no
	J = np.zeros(M+1)							# initializion is required in python
	J[0] = R[0]          						# J=array of "Jl", where l=0,1,2...(b+N)-1
												# J(1)=J0, J(2)=J1, J(3)=J2 etc

	# GETTING OTHER PARAMETERS OF PREDICTOR OF ORDER "(s-1)":
	for s in range(1,M+1):
		sk = 0               # clearing "sk" for each iteration
		for i in range(1,s-1):
			sk = sk + a[i,s-1] * R[s-i+1]
							# now we know value of "sk", the summation term
							# of formula of calculating "k(l)"
		k[s] = (R[s] + sk) / J[s-1]
		J(s) = J[s-1] * (1 - np.square(k(s),2) )
		
		a[s,s] = -k[s]
		a[1,s] = 1
		for i in range(1,s-1):
			a[i,s] = a[i,s-1] - k(s) * a[s-i+1,s-1]

	s += 1 # for a simple matlab python difference
	a_final = a[0:s,s-1].T.conj()
	est_y = lfilter(np.concatenate((np.zeros(1),a_final.T.flatten()[1:])),1,y)    #  = s^(n) with a cap on page 92 of the book
	e = y - est_y	      						# supposed to be a white noise

	pg[M] = 10 * np.log10( sum(np.square(y,2)) / sum(np.square(e,2)) )      # prediction gain

plt.figure()
plt.subplot(2,1,1)
plt.plot(x)
plt.title('original speech file ' + inpfilenm)
plt.subplot(2,1,2)
plt.plot(pg)
plt.title('Prediction Gain (PG) vs Prediction Order (M) for frame starting at data point "b"')
plt.xlabel('M')
plt.ylabel('PG')
plt.tight_layout()

print("This m file is simply 'func_lev_durb.m' with a little modification. If you run this for many frames, \
you will see that PG is good enough for M = a value around '10' for most of the frames")
