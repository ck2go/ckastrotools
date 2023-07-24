"""Test the distances module."""
import numpy as np
from ckastrotools.milkyway.coordinates import getRgalFromVlsr, getVlsrFromRgal


def test_getRgalFromVlsr(mocker):
    # Define parameters for the test
    vlsr = np.array([25., 50., 75., 100.])
    glon = np.array([270.])
    glat = 0.
    R_0 = 8.34
    t_0 = 240.
    precision = 0.001
    expected_min = np.array([8.34, 8.34, 8.34, 8.34])

    # Call the function
    result = getRgalFromVlsr(vlsr, glon, glat=glat, R_0=R_0, t_0=t_0, precision=precision)

    # Check if the function runs without errors and returns a numpy array
    assert isinstance(result, np.ndarray), "Expected numpy array. Got %s." % type(result)
    assert np.all(result >= expected_min), "Expected minimum value of %s. Got %s." % (expected_min, result)
    assert np.all(result[1:]-result[:-1] > 0.0), "Expected increasing values. Got %s." % result


def test_getVlsrFromRgal(mocker):
    # Define parameters for the test
    R_gal = np.array([9., 10., 11., 12.])
    glon = np.array([270.])
    glat = 0.
    R_0 = 8.34
    t_0 = 240.
    precision = 0.001
    expected_min = np.array([0., 0., 0., 0.])

    # Call the function
    result = getVlsrFromRgal(R_gal, glon, glat=glat, R_0=R_0, t_0=t_0, precision=precision)

    # Check if the function runs without errors and returns a numpy array
    assert isinstance(result, np.ndarray), "Expected numpy array. Got %s." % type(result)
    assert np.all(result >= expected_min), "Expected minimum value of %s. Got %s." % (expected_min, result)
    assert np.all(result[1:]-result[:-1] > 0.0), "Expected increasing values. Got %s." % result
