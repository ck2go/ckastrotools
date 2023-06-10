"""Test the spiralarms module."""

def test_getSpiralArms():
    from ckastro.milkyway.spiralarms import getSpiralArms
    arms = getSpiralArms()
    assert type(arms) is dict, "Type of arms should be dict, but is %s" % type(arms)
    assert len(arms) == 4, "Number of arms should be 4, but is %d" % len(arms)
    for arm, coords in arms.items():
        assert 'x' in coords, "x coordinate missing in arm %s" % arm
        assert 'y' in coords, "y coordinate missing in arm %s" % arm
        assert type(coords['x']) is list, "Type of x coordinate should be list, but is %s" % type(coords['x'])
        assert type(coords['y']) is list, "Type of y coordinate should be list, but is %s" % type(coords['y'])



