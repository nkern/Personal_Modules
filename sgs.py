"""
sgs.py : Stochastic Grid Sampling

Sample from a multi-dimensional grid but add small amounts of stochasticity
"""
import numpy as np

def sgs_sample(Ndim=2,grid_shape=[4,4],grid_cent=[0,0],grid_width=[10,10],damp=1.):
	x = []
	cell_size = []
	for i in range(Ndim):
		x.append(np.linspace(-grid_width[i]/2.+grid_cent[i],grid_width[i]/2.+grid_cent[i],grid_shape[i]))
		cell_size.append(float(grid_width[i]) / float(grid_shape[i]-1))
	mesh = np.array(np.meshgrid(*x))
	cell_size = np.array(cell_size)

	stochastic = []
	for i in range(Ndim):
		stochastic.append((np.random.rand(*mesh[i].shape)*2-1)*cell_size[i])

	stochastic = np.array(stochastic)
	return mesh + stochastic/damp




