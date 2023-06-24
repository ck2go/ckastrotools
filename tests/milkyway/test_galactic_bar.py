"""Test the galacic_bar module."""
import numpy as np
import pytest
from astropy import units as u

from ckastrotools.milkyway.galactic_bar import getGalacticBar


def test_getGalacticBar():
    bar = getGalacticBar()
    assert np.min(bar.x.value)/-3. == pytest.approx(np.cos(np.radians(-50)))
    assert np.min(bar.y.value)/3. == pytest.approx(np.sin(np.radians(-50)))

    assert np.max(bar.x.value)/3. == pytest.approx(np.cos(np.radians(-50)))
    assert np.max(bar.y.value)/-3. == pytest.approx(np.sin(np.radians(-50)))

def test_getGalacticBarParameters():
    length = 5
    angle = -40
    bar = getGalacticBar(length=length, angle=angle)
    assert np.min(bar.x.value)/(-1*length/2) == pytest.approx(np.cos(np.radians(angle)))
    assert np.min(bar.y.value)/(length/2) == pytest.approx(np.sin(np.radians(angle)))

    assert np.max(bar.x.value)/(length/2) == pytest.approx(np.cos(np.radians(angle)))
    assert np.max(bar.y.value)/(-1*length/2) == pytest.approx(np.sin(np.radians(angle)))