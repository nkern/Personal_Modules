import numpy as np

def where_eps(arr,equal,eps=1e-4,boolean=False):
	if boolean == True:
		return (arr < equal+eps)*(arr > equal-eps)
	else:
		return np.where( (arr < equal + eps) & (arr > equal - eps) )[0]



