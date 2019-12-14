def uencode(u,n):
    # output range
    val = pow(2,n) - 1
    # map input to output
    ret = (u+1)*(val+1)/2
    # truncate to integer
    ret = np.floor(ret)
    # handle u~1
    ret[u > (1-1e-12)] = val
	return ret
def udecode(u,n):
	pass
	# return ret