import pytest

from zadania import dodaj, oznacz, otwarte, usun


@pytest.fixture
def lista():
    z = []
    dodaj(z, "Zamówić papier")
    dodaj(z, "  Policzyć zeszyty ")
    dodaj(z, "Wysłać paczkę")
    return z


def test_dodaj_usuwa_spacje(lista):
    assert otwarte(lista)[1] == "Policzyć zeszyty"


def test_oznacz_drugie(lista):
    oznacz(lista, 2)
    assert otwarte(lista) == ["Zamówić papier", "Wysłać paczkę"]


def test_oznacz_ostatnie(lista):
    oznacz(lista, 3)
    assert otwarte(lista) == ["Zamówić papier", "Policzyć zeszyty"]


def test_zly_numer(lista):
    for nr in (0, 4):
        with pytest.raises(ValueError):
            oznacz(lista, nr)


def test_usun_zwraca_tytul(lista):
    assert usun(lista, 1) == "Zamówić papier"
    assert len(lista) == 2
