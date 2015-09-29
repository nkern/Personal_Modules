#Takes an apparent magnitude (in any filter) with a given redshift as distance away from observer, and gives the absolute magnitude of object in same filter. 

# M(apparent magnitude, redshift)
# >>>Absolute Magnitude
# Requires SciPy

from __future__ import division
from math import *
from scipy.integrate import quad

def M(m,z):
	H=71
	c = 2.9999E5
	Om = .27
	Ov = 1-Om
	Dh = c/H
	integral = quad(lambda x: 1/((Om*(1+1.0*x)**3 + Ov)**(.5)), 0, z)
	Dc = Dh * integral[0]
	Dm=Dc	
	Dl = Dm*(1+1.0*z)
	print 'Absolute Mag:'

	return m-5*log10(Dl*10**6)+5	
