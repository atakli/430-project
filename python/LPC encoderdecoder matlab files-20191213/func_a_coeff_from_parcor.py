#function of levinsonDurbin__Hamza

def func_a_coeff_from_parcor (k_coeff):

	#M=how much, how much order?
	# if (nargin<2): M = 10   	#prediction order=10; 
	M = 10  # bunu ben ekledim sonradan çünkü nargin denen şeyle uğraşmak istemedim ve zaten nargin hep 1 bu proje için
	#lan ne hep'i zaten sadece bi yerde çağrılıyo bu fonksiyon

	sk = 0       #initializing summartion term "sk"
	a = np.concatenate((np.zeros((M+1,M+1)),np.zeros((M+1,M+1))))	 #defining a matrix of zeros for "a" for init.

	#MAIN BODY OF THIS PROGRAM STARTS FROM HERE>>>>>>>>>>>>>>
	# z=xcorr(y);

	#finding array of R[l]
	# R=z( ( (length(z)+1) ./2 ) : length(z)); #R=array of "R[l]", where l=0,1,2,
											 #...(b+N)-1
											 #R(1)=R[lag=0], R(2)=R[lag=1], 
											 #R(3)=R[lag=2]... etc 

	#GETTING OTHER PARAMETERS OF PREDICTOR OF ORDER "0":
	s = 1				        # s=step no.
	# J(1)=R(1);          	# J=array of "Jl", where l=0,1,2...(b+N)-1
						#J(1)=J0, J(2)=J1, J(3)=J2 etc

	#GETTING OTHER PARAMETERS OF PREDICTOR OF ORDER "(s-1)":
	for s in range(1,M+1):
	#     sk=0;               #clearing "sk" for each iteration
	#     for i=2:(s-1),
	#         sk=sk + a(i,(s-1)).*R(s-i+1);
	#     end                 #now we know value of "sk", the summation term
	#                         #of formula of calculating "k(l)"
	#     k(s)=(R(s) + sk)./J(s-1);
	#     J(s)=J(s-1).*(1-(k(s)).^2);
		a[s,s] = - k_coeff[s]
		a[1,s] = 1
		for i in range(1,s-1):
			a[i,s] = a[i,s-1] - k_coeff(s) * a[s-i+1,s-1]
	#increment "b" and do same for next frame until end of frame when 
	#combining this code with other parts of LPC algo


	#PREDICTION ERROR; FOR TESTING THE ABOVE PREDICTOR
	aCoeff = a[0:s,s-1].T.conj()        # array of "a(i,s)", where, s=M+1
	# parcor=k;
	tcount_of_aCoeff = len(aCoeff)

	# est_y = lfilter([0 -aCoeff(2:end)],1,y);    # = s^(n) with a cap on page 92 of the book
	# e = y - est_y;      #supposed to be a white noise
	return aCoeff,tcount_of_aCoeff