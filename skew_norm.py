"""
Skew Normal Distribution
"""
from __future__ import division
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

def owens_t(h,a,dx=1e-3):
	x = np.arange(0,a,dx)
	y = np.exp(-0.5*h**2*(1+x**2))/(1+x**2)	
	y_int = np.trapz(y=y,x=x,dx=dx)
	return y_int/(2*np.pi)

def pdf(x,loc=0,scale=1,a=0):
	z = (x-loc)/scale
	return 2*norm.pdf(z)*norm.cdf(x*a)

def cdf(x,loc=0,scale=1,a=0):
	z = (x-loc)/scale
	return norm.cdf(z)-2*np.array(map(lambda x: owens_t(x,a),z))

def rvs(size=1,loc=0,scale=1,a=0,x_rang=[-5,5],dx=0.01):
	xarr = np.arange(x_rang[0],x_rang[1],dx)
	cdfunc = cdf(xarr,loc=loc,scale=scale,a=a)
	y_rando = np.random.rand(size)	
	x_samples = np.array( map(lambda x: xarr[np.argsort(np.abs(cdfunc-x))][0],y_rando))
	return x_samples
