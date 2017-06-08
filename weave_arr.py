import numpy as np

def weave_arr(a, b):
    """
    weave two ndarrays 'a' and 'b' together
    """
    ashape = a.shape
    bshape = b.shape
    if len(ashape) == 1:
        cshape = (ashape[0] + bshape[0],)
    else:
        cshape = (ashape[0]+bshape[0], ashape[1])
    c = np.empty(cshape,dtype=a.dtype)
    c[0::2] = a
    c[1::2] = b
    return c

