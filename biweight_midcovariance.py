import numpy as np
import astropy.stats as astats

def biweight_midcovariance(a, c=9.0, M=None, transpose=False):
    r"""
    Compute the biweight midcovariance.
    This is a robust and resistant estimator of the covariance matrix.

    Parameters
    ----------
    a : array-like
        A 2D numpy.ndarray of shape (N_variables, N_observations)
        Each row of a represents a variable, and each column
        a single observation of all variables (same as numpy.cov convention)

    c : float, optional, default=9.0
        Tuning constant.

    M : array-like, optional, shape=(N_dims,)
        Initial guess for biweight location

    transpose : bool, optional, default=False
        Transpose the input array

    Returns
    -------
    biweight_covariance : `~numpy.ndarray`
        Estimate of the covariance matrix of <a, a.T>

    Examples
    --------
    Generate multivariate Gaussian with outliers and compute
    numpy covariance and the biweight_covariance

    >>> import numpy as np
    >>> from astropy.stats import biweight_midcovariance
    >>> # Generate 2D normal sampling of points
    >>> rng = np.random.RandomState(1)
    >>> d = np.array([rng.normal(0, 1, 200), rng.normal(0, 3, 200)])
    >>> # Introduce an obvious outlier
    >>> d[0,0] = 30.0
    >>> # Calculate biweight covariances
    >>> bw_cov = biweight_midcovariance(d)
    >>> # Print out recovered standard deviations
    >>> print(np.around(np.sqrt(bw_cov.diagonal()), 1))
    [ 0.9  3.1]

    See Also
    --------
    biweight_midvariance, biweight_location

    References
    ----------
    http://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/biwmidc.htm

    """
    # Ensure a is array-like
    a = np.asanyarray(a)

    # Ensure a is 2D
    if a.ndim != 2:
        if a.ndim == 1:
            a = a[np.newaxis,:]
        else:
            raise ValueError("a.ndim should equal 2")

    # Transpose
    if transpose == True and a.ndim == 2:
        a = a.T

    # Estimate location if not given
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
    usub1 = (1 - u ** 2)
    usub5 = (1 - 5 * u ** 2)
    usub1[~mask] = 0.0

    # now compute numerator and denominator
    numerator = d * usub1 ** 2
    denominator = (usub1 * usub5).sum(axis=1)[:, np.newaxis]

    # return estimate of the covariance
    numerator_matrix = np.dot(numerator, numerator.T)
    denominator_matrix = np.dot(denominator, denominator.T)
    nsqrt = np.sqrt(n.reshape(1,-1))
    return nsqrt * (numerator_matrix / denominator_matrix) * nsqrt.T

