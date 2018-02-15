"""
lin_trans.py
-----------

functions for linear transformations
of matrices

- rotation in 2d and 3d
- stretch in 2d and 3d

Nick Kern
July, 2017
"""
import numpy as np

def rot2d(phi):
    """
    rotate counter clockwise by phi
    """
    return np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])

def stretch2d(sx=1, sy=1):
    """
    stretch in 2d
    """
    return np.array([[sx, 0], [0, sy]])

def trans2d(phi=0, sx=1, sy=1):
    """
    linear rotation and stretch in 2d
    """
    R = rot2d(phi)
    S = stretch2d(sx=sx, sy=sy)
    return np.dot(R, S)

def rot3d(phi_x=0, phi_y=0, phi_z=0):
    Rx = np.array([[1, 0, 0], [0, np.cos(phi_x), -np.sin(phi_x)], [0, np.sin(phi_x), np.cos(phi_x)]])
    Ry = np.array([[np.cos(phi_y), 0, np.sin(phi_y)], [0, 1, 0], [-np.sin(phi_y), 0, np.cos(phi_y)]])
    Rz = np.array([[np.cos(phi_z), -np.sin(phi_z), 0], [np.sin(phi_z), np.cos(phi_z), 0], [0, 0, 0]])
    return np.dot(Rx, np.dot(Ry, Rz))

def stretch3d(sx=1, sy=1, sz=1):
    """
    linear stretch in 3d
    """
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, sz]])

def trans3d(sx=1, sy=1, sz=1, phi_x=0, phi_y=0, phi_z=0):
    """
    linear rotation and stretch in 3d
    """
    R = rot3d(phi_x=phi_x, phi_y=phi_y, phi_z=phi_z)
    S = stretched(sx=sx, sy=sy, sz=sz)
    return np.dot(R, S)

