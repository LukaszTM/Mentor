import pytest

from magazyn_ukryty import wydaj


def test_wydanie_calego_stanu():
    assert wydaj(10, 10) == 0


def test_wydanie_ponad_stan():
    with pytest.raises(ValueError):
        wydaj(10, 11)
