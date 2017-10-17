# matplotlib
try:
    import matplotlib
    import matplotlib.pyplot as plt
except:
    print('could not import matplotlib')

# numpy
import numpy as np

# astropy
try:
    import astropy.io.fits as fits
    from astropy.time import Time
    import astropy.stats as astats
except:
    print('could not import astropy')

# scipy
try:
    import scipy.stats as stats
    import scipy.optimize as optimize
    import scipy.signal as signal
except:
    print('could not import scipy')

# pyuvdata
try:
    from pyuvdata import UVCal, UVData, UVFITS, UVBeam
except:
    print('could not import pyuvdata')

# uvt
try:
    import uvtools as uvt
except:
    print('could not import uvtools')

# heracal
try:
    import hera_cal as hc
except:
    print('could not import hera_cal')

# hera qm
try:
    import hera_qm as hq
except:
    print('could not import hera_qm')

# aipy
try:
    import aipy
except:
    print('could not import aipy')

# other
import glob
import fnmatch
import os
import sys
import subprocess
import multiprocessing
import cPickle as pkl
import json
import datetime
import copy
from collections import OrderedDict
import shutil






