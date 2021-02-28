"""
An example for how to use the conftest.py fixture
design patter, with unittests
"""


def test_version(version_test) -> None:
    """
    Test the package version number
    """
    assert version_test.__version__ == '0.1.0'
