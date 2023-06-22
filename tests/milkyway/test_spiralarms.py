"""Test the spiralarms module."""
import numpy as np
import pytest
from astropy.coordinates import SkyCoord

from ckastrotools.milkyway.spiralarms import getSpiralArms, getSpiralArm


def test_getSpiralArms():
    arms = getSpiralArms()
    assert type(arms) is dict, "Type of arms should be dict, but is %s" % type(arms)
    assert len(arms) == 4, "Number of arms should be 4, but is %d" % len(arms)
    for arm, coords in arms.items():
        assert type(arm) is str
        assert isinstance(coords, SkyCoord)


def test_getOuterArmCK():
    outer = getSpiralArm(name='outer', model='ck2021')
    assert np.min(outer.galactic.l.deg) == pytest.approx(180., 0.01)
    assert np.max(outer.galactic.l.deg) == pytest.approx(280., 0.01)


def test_getPerseusArmLimitedLongitude():
    per = getSpiralArm(name='perseus', model='reid2014',
                         glon_min=180., glon_max=280.)
    assert np.min(per.galactic.l.deg) == pytest.approx(180., 0.01)
    assert np.max(per.galactic.l.deg) == pytest.approx(280., 0.01)


def test_getScutumArmLimitedRgal():
    per = getSpiralArm(name='scutum', model='reid2014',
                         r_gal_min=8., r_gal_max=10.)
    assert np.min(per.galactic.distance.kpc) == pytest.approx(8., 0.01)
    assert np.max(per.galactic.distance.kpc) == pytest.approx(10., 0.01)