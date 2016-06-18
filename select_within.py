"""
select points within a hyper-ellipsoid given covariance of ellipsoid
"""
import numpy as np, numpy.linalg as la

def select_within(Xarr,cov,Rmax=1.0):
	"""
	Xarr 	: ndarray [Nsamples,Ndimensions]
	cov		: Covariance of hyper ellipsoid
	"""
	# Solve for cholesky decomposition
	L 		= la.cholesky(cov)
	invL 	= la.inv(L)

	# Whiten the Xarr and covariance
	Xarr_W = np.dot(invL,Xarr.T).T
	cov_W = np.dot(invL,cov)

	# Find Radius vector, with distances scaled by covariance along each dimension
	rad = np.sqrt(np.array(map(sum,(Xarr_W/cov_W.diagonal())**2)))

	# Select points within Rmax
	sel = rad <= Rmax

	return sel