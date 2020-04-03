# function of levinsonDurbin__Hamza
import numpy as np
def func_lev_durb(y,M):
	# M=how much, how much order?
	# if nargin < 2: M = 10    					# prediction order=10 
	# bunu ben commentledim sonradan çünkü nargin denen şeyle uğraşmak istemedim: zaten nargin hep 2 bu proje için
	# aslında func definiton'da M=10 desem olurdu

	sk = 0       								# initializing summartion term "sk"
	a = np.concatenate((np.zeros((M+1,M+1)),np.zeros((M+1,M+1)))) 				# defining a matrix of zeros for "a" for init.

	# MAIN BODY OF THIS PROGRAM STARTS FROM HERE>>>>>>>>>>>>>>
	z = np.correlate(y,y,mode='full') 

	# finding array of R[l]
	R = z[ (len(z)+1) / 2 - 1 : len(z) ] 		# R=array of "R[l]", where l=0,1,2,...(b+N)-1
												# R(1)=R[lag=0], R(2)=R[lag=1], 
												# R(3)=R[lag=2]... etc 

	# GETTING OTHER PARAMETERS OF PREDICTOR OF ORDER "0":
	s = 1        								# step no.
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
		J[s] = J[s-1] * (1 - np.square(k[s]) )
		
		a[s,s] = -k[s]
		a[1,s] = 1
		for i in range(1,s-1):
			a[i,s] = a[i,s-1] - k(s) * a[s-i+1,s-1]
	#increment "b" and do same for next frame until end of frame when 
	#combining this code with other parts of LPC algo

	s += 1 # for a simple matlab python difference
	#PREDICTION ERROR; FOR TESTING THE ABOVE PREDICTOR
	aCoeff = a[0:s,s-1].T.conj()       						# array of "a(i,s)", where, s=M+1
	parcor = k
	tcount_of_aCoeff = len(aCoeff)

	est_y = lfilter(np.concatenate((np.zeros(1),aCoeff.T.flatten()[1:])),1,y)    #  = s^(n) with a cap on page 92 of the book
	e = y - est_y      										# supposed to be a white noise
	return parcor, aCoeff, tcount_of_aCoeff, e