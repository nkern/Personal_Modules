"""
multivariable logistic distribution
"""
import scipy.stats as stats
import numpy as np, numpy.linalg as la


def multi_logistic(loc,cov,rvs=True,size=1):
	"""
	loc is a numpy ndarray row vector of shape [n_dimensions]
	cov is a numpy ndarray matrix of shape [n_dimensions, n_dimensions]
	"""

	# Get dimensions
	dim = cov.shape[0]

	# Get linear transform
	vec,val,vecinv = la.svd(cov)
	val = np.eye(dim)*np.sqrt(val)
	T = np.dot(vec,val)

	# Generate white data
	data = []
	for i in range(dim):
		data.append(stats.logistic.rvs(loc=0,scale=1,size=size))
	data = np.array(data)

	# Transform
	data = np.dot(T,data)

	return data

