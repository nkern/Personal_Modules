import numpy as np
import astropy.stats as astats

def biweight_midcovariance(a, c=9.0, M=None):
    r"""
    Compute the biweight midcovariance.

    This is a robust and resistant estimator of the covariance matrix.

    For more details, see:
    `<http://www.itl.nist.gov/div898/software/
    dataplot/refman2/auxillar/biwmidc.htm>_.`

    Parameters
    ----------
    a : array-like, shape=(N_dims, N_samples)
    Input array

    c : float, optional
    Tuning constant. Default is 9.0

    M : array-like, optional, shape=(N_dims,)
    Initial guess for biweight location

    Returns
    -------
    biweight_covariance : `~numpy.ndarray`

    Examples
    --------
    Generate multivariate Gaussian with outliers and compute
    numpy covariance and the biweight_covariance

    >>> import numpy as np
    >>> import scipy.stats as stats
    >>> from astropy.stats import biweight_midcovariance
    >>> d = np.array([stats.norm.rvs(0,1,1000),stats.norm.rvs(0,3,1000)])
    >>> d[0,0] = 30
    >>> np_cov = np.cov(d)
    >>> bw_cov = biweight_midcovariance(d)
    >>> print(np.sqrt(np_cov.diagonal()), np.sqrt(bw_cov.diagonal()))
    (array([ 1.38868655,  2.97004256]), array([ 1.0232835 ,  3.02582728]))

    See Also
    --------
    biweight_midvariance, biweight_location
    """

    a = np.asanyarray(a)

    if M is None:
        M = np.median(a, axis=1)

    # set up the differences
    d = (a.T - M).T

    # set up the weighting
    mad = astats.median_absolute_deviation(a, axis=1)
    u = (d.T / (c * mad)).T

    # now remove the outlier points
    mask = np.abs(u) < 1
    n = mask.sum(axis=1)
    usub1 = (1-u**2)
    usub5 = (1-5*u**2)
    usub1[~mask] = 0.0

    # now compute numerator and denominators
    numerator = d * usub1 ** 2
    denominator = (usub1 * usub5).sum(axis=1)[:, np.newaxis]

    return n * np.dot(numerator, numerator.T) / np.dot(denominator, denominator.T)
