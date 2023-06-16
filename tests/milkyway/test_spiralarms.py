"""Test the spiralarms module."""
from ckastro.milkyway.spiralarms import getSpiralArms
from astropy.coordinates import SkyCoord

def test_getSpiralArms():
    arms = getSpiralArms()
    assert type(arms) is dict, "Type of arms should be dict, but is %s" % type(arms)
    assert len(arms) == 4, "Number of arms should be 4, but is %d" % len(arms)
    for arm, coords in arms.items():
        assert type(arm) is str
        assert isinstance(coords, SkyCoord)


