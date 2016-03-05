"""
Linear Least Squares
Functions and Tools used to do LLS in Python

Nicholas Kern
March, 2016
"""

import itertools
import operator
import numpy as np
import functools
from DictEZ import create as ezcreate


class LLS(object):

    def __init__(self,object):
        self.__dict__.update(object)

    def poly_design_mat(self,Xrange,dim=2,degree=6):
        """
        - Create design matrix given discrete values for dependent variables
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

        # Update Class Namespace
        names = ['A','perms']
        self.__dict__.update(ezcreate(names,locals()))

        return A














