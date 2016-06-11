
from numpy import pi, sqrt, e

def vol1(r):
	return 2.*r

def vol2(r):
	return pi*r**2

def vol3(r):
	return 4./3.*pi*r**3

def vol4(r):
	return pi**2/2.*r**4

def vol5(r):
	return 8*pi**2/15.*r**5

def vol6(r):
	return pi**3/6.*r**6

def vol7(r):
	return 16.*pi**3/105.*r**7

def vol8(r):
	return pi**4/24. * r**8

def vol9(r):
	return 32.*pi**4/945. * r**9

def vol10(r):
	return pi**5/120.*r**10

def vol_high_n(r,n):
	return 1/sqrt(n*pi) * (2*pi*e/n)**(n/2.)*r**n




