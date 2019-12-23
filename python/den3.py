from cv2 import matchTemplate as cv2m

def search_sequence_cv2(arr,seq):
    """ Find sequence in an array using cv2.
    """

    # Run a template match with input sequence as the template across
    # the entire length of the input array and get scores.
    S = cv2m(arr.astype('uint8'),seq.astype('uint8'),cv2.TM_SQDIFF)

    # Now, with floating point array cases, the matching scores might not be 
    # exactly zeros, but would be very small numbers as compared to others.
    # So, for that use a very small to be used to threshold the scorees 
    # against and decide for matches.
    thresh = 1e-5 # Would depend on elements in seq. So, be careful setting this.

    # Find the matching indices
    idx = np.where(S.ravel() < thresh)[0]

    # Get the range of those indices as final output
    if len(idx)>0:
        return np.unique((idx[:,None] + np.arange(seq.size)).ravel())
    else:
        return []         # No match found