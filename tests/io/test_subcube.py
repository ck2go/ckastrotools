"""Test the subcube module."""

from unittest.mock import Mock

from spectral_cube import SpectralCube

from ckastro.io.subcube import extractCutout


def test_extractCutout():
    mock_cube = Mock()
    mock_cube.subcube.return_value = Mock(spec=SpectralCube)

    result = extractCutout(mock_cube, glon=42.0, glat=0., width=0.5)

    assert mock_cube.subcube.called_once()
    assert isinstance(result, SpectralCube)
