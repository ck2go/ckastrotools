"""Test the spiralarms module."""
import numpy as np


def test_getSpiralArms():
    from ckastro.milkyway.spiralarms import getSpiralArms
    arms = getSpiralArms()
    assert type(arms) is dict, "Type of arms should be dict, but is %s" % type(arms)
    assert len(arms) == 4, "Number of arms should be 4, but is %d" % len(arms)
    for arm, coords in arms.items():
        assert 'x' in coords, "x coordinate missing in arm %s" % arm
        assert 'y' in coords, "y coordinate missing in arm %s" % arm
        assert type(coords['x']) is np.ndarray, "Type of x coordinate should be Numpy ndarray, but is %s" % type(coords['x'])
        assert type(coords['y']) is np.ndarray, "Type of y coordinate should be Numpy ndarray, but is %s" % type(coords['y'])



