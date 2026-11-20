import pytest

from cennik import cena_pokoju, oplata_klimatyczna


@pytest.mark.parametrize("pokoj, miesiac, cena", [("Lipowy", 7, 180), ("Lipowy", 3, 140), ("Dębowy", 6, 160), ("Dębowy", 5, 120),
                                                   ("Klonowy", 12, 200), ("Klonowy", 11, 150), ("Lipowy", 8, 180), ("Lipowy", 9, 140)])
def test_cena_pokoju(pokoj, miesiac, cena):
    assert cena_pokoju(pokoj, miesiac) == cena


def test_oplata_dorosli():
    assert oplata_klimatyczna(2, 3) == 15.0


def test_dzieci_nie_placa():
    assert oplata_klimatyczna(2, 2, dzieci=3) == 10.0


def test_nieznany_pokoj():
    with pytest.raises(ValueError):
        cena_pokoju("Brzozowy", 7)


def test_zly_miesiac():
    with pytest.raises(ValueError):
        cena_pokoju("Lipowy", 13)


def test_zero_nocy():
    with pytest.raises(ValueError):
        oplata_klimatyczna(2, 0)
