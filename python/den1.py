import numpy as np
def search_sequence_numpy(arr,seq):
	Na, Nseq = arr.size, seq.size

	r_seq = np.arange(Nseq)

	# Create a 2D array of sliding indices across the entire length of input array.
	# Match up with the input sequence & get the matching starting indices.
	M = (arr[np.arange(Na-Nseq+1)[:,None] + r_seq] == seq).all(1)
	a = (arr[np.arange(Na-Nseq+1)[:,None] + r_seq] == seq)
	# breakpoint()
	# Get the range of those indices as final output
	if M.any() > 0:
		return np.where(np.convolve(M,np.ones((Nseq),dtype=int))>0)[0]
	else:
		return []		  # No match found
