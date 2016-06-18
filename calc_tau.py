"""
Calculate tau given ionization history
"""

from __future__ import division
import numpy as np
from astropy.cosmology import FlatLambdaCDM
from scipy.integrate import quad
from sklearn.gaussian_process import GaussianProcess

sig_T           = 6.6524e-25            # cm2
c               = 2.9979e10             # cm s-1

gp_kwargs = {	'corr': 'squared_exponential',
		'random_start': 1,
		'regr': 'linear',
		'theta0': 1.0,
		'thetaL': None,
		'thetaU': None,
		'verbose': False,
		'nugget':1e-5
		}

cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

def t0(z):
	a = 1./(1+z)
	return quad(lambda a: a/cosmo.H(a).value*3.086e19,0,a)[0]
	
def nh(z):
	return 1.6e-6*(1+z)**3

def dtau(z, xh, nh):
	return xh(z)*nh(z)*sig_T*c

def tau(z,zre=9,zre_width=0.85,nh=nh):
	tend = cosmo.age(0).value * 3.15576e7
	tstart = cosmo.age(z).value * 3.15576e7
	zarr = np.linspace(z,0,1e3)
	ages = cosmo.age(zarr).value* 3.15576e7
	dages = np.concatenate([[ages[1]-ages[0]],ages[1:] - ages[:-1]])

	z_array = np.linspace(0,z,1e4)
	xe_array = np.tanh( (z_array-zre)*zre_width )/2. + 0.5
	GP = GaussianProcess(**gp_kwargs).fit(z_array[:,np.newaxis],xe_array)
	def xh(z):
		return GP.predict(z)

	y = np.array(map(lambda x: dtau(x,xh,nh), zarr)).ravel()
	integral = np.trapz(y=y,x=ages,dx=dages)
	return integral














