
import numpy as np

def vol1(r):
	return 2.*r

def vol2(r):
	return np.pi*r**2

def vol3(r):
	return 4./3.*np.pi*r**3

def vol4(r):
	return np.pi**2/2.*r**4

def vol5(r):
	return 8*np.pi**2/15.*r**5

def vol6(r):
	return np.pi**3/6.*r**6

def vol7(r):
	return 16.*np.pi**3/105.*r**7

def vol8(r):
	return np.pi**4/24. * r**8

def vol9(r):
	return 32.*np.pi**4/945. * r**9

def vol10(r):
	return np.pi**5/120.*r**10

def vol_high_n(r,n):
	return 1/np.sqrt(n*np.pi) * (2*np.pi*np.e/n)**(n/2.)*r**n

def discrete_vol(r,n):
	mesh = np.meshgrid(*[np.linspace(-1,1,r*2) for i in range(n)])
	mesh = np.vstack([mesh[i].ravel() for i in range(n)]).T
	mesh_R = np.sqrt(np.array(map(sum,mesh**2)))
	sel = mesh_R <= 1
	return np.where(sel==True)[0].size

