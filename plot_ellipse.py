'''
Personal Script to Plot an Ellipse using matplotlib.pyplot
matplotlib.patches.Ellipse is not sufficient for desired purposes

Nicholas Kern
February, 2016
'''
import numpy as np
import pylab as mp

def plot_ellipse(semimaj=1,semimin=1,phi=0,x_cent=0,y_cent=0,theta_num=1e3,ax=None,plot_kwargs=None,fill=False,fill_kwargs=None):
	'''
		- create an ellipse in polar coordinates then transform to cartesian
		- if given an axes, plot an ellipse with plot_kwargs
		- if not given an axes, create a basic figure and axes and plot
		major keywords are:
		semimaj : length of semimajor axis (always taken to be some phi from positive x-axis!)
		semimin : length of semiminor axis
		phi : angle in radians semimajor axis is above positive x axis
		x_cent : x center
		y_cent : y center
		theta_num : number of points to sample from 0 to 2pi
	'''
	# Generate data for ellipse structure
	theta = np.linspace(0,2*np.pi,theta_num)
	r = 1 / np.sqrt((np.cos(theta))**2 + (np.sin(theta))**2)
	x = r*np.cos(theta)
	y = r*np.sin(theta)
	data = np.array([x,y])
	S = np.array([[semimaj,0],[0,semimin]])
	R = np.array([[np.cos(phi),-np.sin(phi)],[np.sin(phi),np.cos(phi)]])
	T = np.dot(R,S)
	data = np.dot(T,data)
	data[0] += x_cent
	data[1] += y_cent

	# Plot!
	if ax == None:
		fig,ax = mp.subplots()

	if plot_kwargs == None:
		ax.plot(data[0],data[1],color='b',linestyle='-')	
	else:
		ax.plot(data[0],data[1],**plot_kwargs)


	if fill == True:
		ax.fill(data[0],data[1],**fill_kwargs)


