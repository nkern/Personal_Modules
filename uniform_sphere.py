"""
uniform distribution on a circle or sphere or hyper-sphere
"""
import numpy as np
import scipy.linalg as la
import scipy.stats as stats

def multivar_uniform_sph(loc,cov,size=1,seed=None):
	"""
	generate uniform data within a circle, sphere or hyper-sphere
	use cholesky to make mapping from unit sphere to desired covariance
	"""
	if seed != None:
		np.random.seed(seed)

	# Generate vanilla data w extra size
	dims = cov.shape[0]
	data = []
	for i in range(dims):
		data.append(stats.uniform.rvs(-1,2,size*5))
	data = np.array(data)

	# Get distance vector
	R = np.array(map(lambda x: np.sqrt(sum(x**2)), data.T))

	# Get points that are inside R=1
	inside = R <= 1
	len_in = len(np.where(inside==True)[0])

	if len_in >= size:
		rando = np.random.choice(np.arange(len_in),size=size,replace=False)
		data = data.T[inside][rando].T

	else:
		# Isolate good data
		data = data.T[inside].T
		while True:
			# Make new random data
			new_data = []
			for i in range(dims):
				new_data.append(stats.uniform.rvs(-1,2,size*5))
			new_data = np.array(new_data)
			# Get distance vector and those inside unit vector
			R = np.array(map(lambda x: np.sqrt(sum(x**2)), new_data.T))
			inside = R <= 1
			# Add good data to previous data
			data = np.vstack([data.T,new_data.T[inside]]).T
			len_in = data.shape[1]
			if len_in >= size:
				rando = np.random.choice(np.arange(len_in),size=size,replace=False)
				data = data.T[rando].T
				break
			else:
				continue

	# Perform cholesky to map data into covariance
	L = la.cholesky(cov)
	data_prime = np.dot(L,data)	
	return data_prime
	
	




