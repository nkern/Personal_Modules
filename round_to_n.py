import numpy as np

def round_to_n(x,n=1):
	try:
		return np.round(x, -int(np.floor(np.log10(x))) + (n - 1))
	except:
		return np.array(map(lambda z: np.round(z, -int(np.floor(np.log10(z))) + (n - 1)), x))
