import pytest
from fleet import Bus


def test_maut():
    """Tests whether the toll is calculated correctly."""
    bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
    assert bus.maut() == 3500


def test_assert():
    """Tests whether the attribute assertions work by providing an incorrect number."""
    with pytest.raises(AssertionError):
        Bus(25, 100000, -2500, 1995, 200, 80, 40)
