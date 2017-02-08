"""
round_to_n.py
-------------
Adapted from:
http://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python

Nicholas Kern
2016
"""
import numpy as np

def round_to_n(x,n=1):
    try:
        return np.round(x, -int(np.floor(np.log10(x))) + (n - 1))
    except:
        shape = x.shape
    return np.array(map(lambda z: np.round(z, -int(np.floor(np.log10(np.abs(z)))) + (n - 1)), x.ravel())).reshape(shape)
