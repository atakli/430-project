import numpy as np
def uencode(inp,n):
	"""# output range
	val = pow(2,n) - 1
	# map input to output
	ret = (u+1)*(val+1)/2
	# truncate to integer
	ret = np.floor(ret)
	# handle u~1
	ret[u > (1-1e-12)] = val
	return ret"""

	if not np.array_equal(n,np.int64(n)):
		raise ValueError("uencode: N must be an integer in the range [2, 32]")
	out = np.zeros(inp.shape)

	width = 2 / pow(2,n)

	out[inp >= 1] = pow(2,n) - 1
	idx = (inp > -1) & (inp < 1)
	out[idx] = np.floor((inp[idx] + 1) / width)
	return out
def udecode(inp,n):	

	if not np.array_equal(inp,np.int64(inp)):
		raise ValueError("udecode: inp must be matrix of integers")

	if not np.array_equal(n,np.int64(n)):
		raise ValueError("udecode: N must be an integer in the range [2, 32]")

	if np.all (inp >= 0):
		signed = "unsigned"
		lowerlevel = 0
		upperlevel = pow(2,n) - 1
	else:
		signed = "signed"
		lowerlevel = - pow(2,n - 1)
		upperlevel = pow(2,n - 1) - 1

	if signed == "unsigned":
		inp[inp > upperlevel] = upperlevel
	elif signed == "signed":
		inp[inp < lowerlevel] = lowerlevel
		inp[inp > upperlevel] = upperlevel

	width = 2 / pow(2,n)

	out = np.double(inp) * width			# double doğru mu?
	if signed == "unsigned":
		out = out - 1
	return out