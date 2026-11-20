# Testy charakteryzujące raport_obroty.py — utrwalają obecne wyniki. Po refaktoryzacji muszą przejść BEZ ZMIAN.
from raport_obroty import przychod, raport_tekstowy

R = [{"miesiac": 7, "noce": 3, "osoby": 2}, {"miesiac": 7, "noce": 7, "osoby": 1}, {"miesiac": 3, "noce": 2, "osoby": 2},
     {"miesiac": 12, "noce": 10, "osoby": 4}, {"miesiac": 3, "noce": 8, "osoby": 1}]


def test_przychod():
    assert przychod(R) == 8477.0


def test_przychod_pusty():
    assert przychod([]) == 0


def test_raport():
    assert raport_tekstowy(R) == "Marzec: 1 232,00 zł\nLipiec: 1 845,00 zł\nGrudzień: 5 400,00 zł\nRazem: 8 477,00 zł"


def test_raport_jeden():
    assert raport_tekstowy([{"miesiac": 1, "noce": 1, "osoby": 1}]) == "Styczeń: 110,00 zł\nRazem: 110,00 zł"
