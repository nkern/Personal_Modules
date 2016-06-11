"""
CMB parameter mappings

"""
from __future__ import division
import numpy as np
from scipy.integrate import quad

def grhoPrefac(h):
	return (3.3379*10**(-7))*h**2

def grhoPhotons(T):
	return 1.4952*10**(-13)*T**4

def grhoNeutrinos(T,nuDegen):
	return nuDegen*(7./8.) * (4./11.)**(4./3.) * grhoPhotons(T)

def grhoa2(h, Obh2, Och2, T, a, nuDegen):
	return grhoPrefac(1.0) * (Obh2 + Och2) * (a - a**4) + (grhoPhotons(T) + grhoNeutrinos(T, nuDegen)) * (1 - a**4) + grhoPrefac(h) * a**4

def dtauda(a, h, Obh2, Och2, T, nuDegen):
	return np.sqrt(3./grhoa2(h, Obh2, Och2, T, a, nuDegen))

def R(a, Obh2):
	return (3.*10.**4) * Obh2 * a

def rs(aend, h, Obh2, Och2, T, nuDegen):
	def func(a, h, Obh2, Och2, T, nuDegen):
		return dtauda(a, h, Obh2, Och2, T, nuDegen)*1./np.sqrt(3*(1 + R(a, Obh2)))
	integral = quad(func,0,aend,args=(h, Obh2, Och2, T, nuDegen))
	return integral[0]

def ComovingLOSDist(astart, h, Obh2, Och2, T, nuDegen):
	integral = quad(dtauda, astart, 1, args=(h, Obh2, Och2, T, nuDegen))
	return integral[0]

def zstar(Obh2, Och2): 
	 return 1048*(1 + 0.00124*Obh2**(-0.738))*(1 + ((0.0783*Obh2**(-0.238))/(1 + 39.5*Obh2**(0.763)))*(Och2 + Obh2)**(0.560/(1 + 21.1*Obh2**(1.81))))

def ztoa(z):
	return 1./(1 + z);

def Theta_MC(h, Obh2, Och2, T=2.726, nuDegen=3.04):
	arec = ztoa(zstar(Obh2,Och2))
	return rs(arec, h, Obh2, Och2, T, nuDegen)/ComovingLOSDist(arec, h, Obh2, Och2, T, nuDegen)


