# test_magazyn_demo.py — uruchom: python -m pytest -v test_magazyn_demo.py
import pytest


def koszt_dostawy(razem):
    if razem < 0:
        raise ValueError("kwota nie może być ujemna")
    if razem >= 100:
        return 0
    return 9.99 if razem >= 50 else 14.99


def test_dostawa_darmowa_od_100():
    assert koszt_dostawy(100) == 0


def test_dostawa_tuz_ponizej_progu():
    assert koszt_dostawy(99.99) == 9.99


def test_dostawa_mala_kwota():
    wynik = koszt_dostawy(49.99)
    assert wynik == 14.99


def test_ujemna_kwota_to_blad():
    with pytest.raises(ValueError, match="ujemna"):
        koszt_dostawy(-1)


def test_suma_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
