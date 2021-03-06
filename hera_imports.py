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
    import scipy.integrate as integrate
    import scipy.interpolate as interp
except:
    print('could not import scipy')

# pyuvdata
try:
    from pyuvdata import UVCal, UVData, UVFITS, UVBeam
    from pyuvdata import utils as uvutils
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

# hera_pspec
try:
    import hera_pspec as hp
except:
    print("could not import hera_pspec")

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

# healpy
try:
    import healpy as hlp
except:
    print('could not import healpy')

# hera_sandbox
try:
    import JD2LST
except:
    print('could not import hera_sandbox scripts')

# linesolve
try:
    import linsolve
except:
    print('could not import linsolve')

# h5py
try:
    import h5py
except:
    print('could not import h5py')


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
from collections import OrderedDict as odict
import shutil
import itertools
import operator





