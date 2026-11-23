import pytest

from funkcje import czy_parzysta, maksimum, odwroc, pole_prostokata, silnia


def test_pole_prostokata():
    assert pole_prostokata(3, 4) == 12


def test_czy_parzysta():
    assert czy_parzysta(4) is True
    assert czy_parzysta(7) is False


def test_maksimum_szuka_najwiekszego():
    assert maksimum([3, 9, 2]) == 9
    assert maksimum([-5, -2, -9]) == -2


def test_maksimum_pusta_lista_to_blad():
    with pytest.raises(ValueError):
        maksimum([])


def test_odwroc():
    assert odwroc("kot") == "tok"


def test_silnia_granice():
    assert silnia(0) == 1
    assert silnia(5) == 120
    with pytest.raises(ValueError):
        silnia(-1)
