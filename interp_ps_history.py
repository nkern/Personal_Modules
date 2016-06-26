"""
Interpolate power spectra evolution

Nicholas Kern
2016
"""

import numpy as np
import numpy.linalg as la
import itertools
import operator
import functools

def poly_design_mat(Xrange,dim=2,degree=6):
	"""
	- Create polynomial design matrix given discrete values for dependent variables
	- dim : number of dependent variables 
	- degree : degree of polynomial to fit
	- Xrange is a list with dim # of arrays, with each array containing
		discrete values of the dependent variables that have been unraveled for dim > 1
	- Xrange has shape dim x Ndata, where Ndata is the # of discrete data points
	- A : Ndata x M design matrix, where M = (dim+degree)!/(dim! * degree!)
	- Example of A for dim = 2, degree = 2, Ndata = 3:
		A = [   [ 1  x  y  x^2  y^2  xy ]
				[ 1  x  y  x^2  y^2  xy ]
				[ 1  x  y  x^2  y^2  xy ]   ]
	"""

	# Generate all permutations
	perms = itertools.product(range(degree+1),repeat=dim)
	perms = np.array(map(list,perms))

	# Take the sum of the powers, sort, and eliminate sums > degree
	sums = np.array(map(lambda x: reduce(operator.add,x),perms))
	argsort = np.argsort(sums)
	sums = sums[argsort]
	keep = np.where(sums <= degree)[0]
	perms = perms[argsort][keep]

	# Create design matrix
	to_the_power = lambda x,y: np.array(map(lambda z: x**z,y))
	dims = []
	for i in range(dim):
		dims.append(to_the_power(Xrange[i],perms.T[i]).T)
	dims = np.array(dims)

	A = np.array(map(lambda y: map(lambda x: functools.reduce(operator.mul,x),y),dims.T)).T

	return A

def chi_square_min(y,A,N):
	'''
	- perform chi square minimization
	- A is data model
	- N are weights of each y_i for fit
	- y are dataset
	'''
	# Solve for coefficients xhat
	xhat = np.dot( la.inv( np.dot( np.dot(A.T,la.inv(N)), A)), np.dot( np.dot(A.T,la.inv(N)), y) )

	return xhat

def get_nearest(x,xarr,x_id,n=3):
	"""
	Get n nearest points in xarr to point x, and return their IDs in increasing order
	"""
	dist = np.abs(xarr-x)
	nn_id = x_id[np.argsort(dist)][:n]
	return nn_id[np.argsort(nn_id)]

def ps_interp(z_array, z_data, y_data, n=3, degree=2):
	""" 
	ps_interp(z_array, z_data, y_data, n=3, degree=2)
	- Interpolate power spectra histories output by 21cmFAST onto different redshifts
	- Fit a quadratic to nearest 3-points
	z_array : row vector ndarray of desired redshifts at which we want the power spectra
	z_data : row vector ndarray of 21cmFAST output redshifts
	y_data : matrix ndarray with shape (z_num, k_num) of 21cmFAST output power spectra (DelDel [mK^2])
	"""
	# Order data by redshift
	sort = np.argsort(z_array)
	z_array = z_array[sort]
	sort = np.argsort(z_data)
	z_data = z_data[sort]
	y_data = y_data[sort]

	# Get redshift and kbin numbers
	z_num = len(z_data)
	try: k_num = y_data.shape[1]
	except IndexError: k_num = 1

	# Assign each z_data point an identification number
	z_id = np.arange(z_num)

	# Iterate over desired points to interpolate
	y_interp = []
	for i in range(len(z_array)):
		# Fit flag
		fit = True

		# Assign z point
		z = z_array[i]

		# Get nearest neighbors
		if i != 0:
			# If nearest neighbors haven't changed, do redo fit!
			nn_id_new = get_nearest(z,z_data,z_id,n=n)
			if np.abs(sum(nn_id - nn_id_new)) < 0.1:
				fit = False
			else:
				# If they have, get new nearest neighbors
				nn_id = nn_id_new
		else:
			nn_id = get_nearest(z,z_data,z_id,n=n)

		# Fit for polynomial
		if fit == True:
			A = poly_design_mat([z_data[nn_id]],dim=1,degree=degree)
			N = np.eye(n)
			xhat = chi_square_min(y_data[nn_id],A,N)

		# Make prediction
		A = poly_design_mat([[z]],dim=1,degree=degree)
		y_pred = np.dot(A,xhat)

		y_interp.append(y_pred.ravel())

	return np.array(y_interp)





