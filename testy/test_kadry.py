# -*- coding: utf-8 -*-
"""Silnik płacowy kadry.py na przypadkach policzonych ręcznie w lekcjach kursu „Kadry i płace” (parametry 2026)."""

import datetime as dt
import json

import pytest

import kadry


@pytest.fixture(scope="module")
def firma(repo):
    d = json.loads((repo / "programy" / "kadry-i-place.json").read_text(encoding="utf-8"))
    return d["parametry"]


def test_lista_plac_minimalne_i_ppk():
    assert kadry.lista_plac(zasadnicze=4806, ppk_prac=0, ppk_pracod=0)["netto"] == 3605.85
    r = kadry.lista_plac(zasadnicze=4806)
    assert (r["spol"], r["zdrowotna"], r["zaliczka"], r["netto"]) == (658.91, 373.24, 176.0, 3501.73)
    assert kadry.lista_plac(zasadnicze=7200)["netto"] == 5080.72


def test_lista_plac_lekcja_wskazniki(firma):
    r = kadry.lista_plac(zasadnicze=5400, kup=250, pit2=300, ppk_prac=2, ppk_pracod=1.5, par=firma)
    assert (r["emer"], r["rent"], r["chor"], r["spol"]) == (527.04, 81.0, 132.3, 740.34)
    assert (r["podstawa_zdr"], r["zdrowotna"], r["podstawa_pit"], r["zaliczka"], r["netto"]) == (4659.66, 419.37, 4491.0, 239.0, 3893.29)
    assert (r["emer_p"], r["rent_p"], r["wyp"], r["ppk_pracod"]) == (527.04, 351.0, 64.8, 81.0)          # RCA: pola 11, 12, 14, 28


def test_lista_plac_bilans_brutto_netto(firma):
    r = kadry.lista_plac(zasadnicze=5200, zmienne=573.75, par=firma)
    assert round(r["netto"] + r["spol"] + r["zdrowotna"] + r["zaliczka"] + r["ppk_prac"], 2) == 5773.75
    assert r["netto"] == 4140.29


def test_swiadczenia_bez_zus_po_ustaniu(firma):
    """Lista końcowa z odprawą: bez składek, z PIT; po ustaniu zatrudnienia bez PIT-2."""
    r = kadry.lista_plac(zasadnicze=1890, zmienne=1290.80, wyn_chorobowe=1201.14, zasilek=800.76, bez_zus=5400, kup=250, pit2=0, ppk_prac=2, ppk_pracod=1.5,
                         par=firma, pensja_umowna=5400)
    assert (r["spol"], r["zdrowotna"], r["zaliczka"], r["netto"]) == (436.09, 355.13, 1193.0, 8534.86)
    r = kadry.lista_plac(zasadnicze=4200, zmienne=1434, bez_zus=12000, pit2=0, ppk_prac=0, ppk_pracod=0, pensja_umowna=6000, par=firma)
    assert (r["zaliczka"], r["netto"]) == (1993.0, 14431.04)


def test_projekt_koncowy_zgodny_z_silnikiem(firma, repo):
    """Klucz projektu końcowego (Formularze) nie może się rozjechać z silnikiem."""
    d = json.loads((repo / "programy" / "kadry-i-place.json").read_text(encoding="utf-8"))
    f = next(x for x in d["formularze"] if x["id"] == "projekt_zamkniecie_roku")
    k = {p["id"]: p["wartosc"] for s in f["sekcje"] for p in s["pola"]}
    lis = kadry.lista_plac(zasadnicze=14000, zmienne=16800, ppk_prac=2, ppk_pracod=1.5, pensja_umowna=14000, par=firma)
    woj = kadry.lista_plac(zasadnicze=4165.20, wyn_chorobowe=442.36, ppk_prac=2, ppk_pracod=1.5, pensja_umowna=4806, par=firma)
    kow = kadry.lista_plac(zasadnicze=6000, ppk_prac=0, ppk_pracod=0, par=firma)
    assert (k["lis_spol"], k["lis_zdr"], k["lis_zal"], k["lis_netto"]) == (lis["spol"], lis["zdrowotna"], lis["zaliczka"], lis["netto"])
    assert (k["woj_spol"], k["woj_zdr"], k["woj_zal"], k["woj_netto"]) == (woj["spol"], woj["zdrowotna"], woj["zaliczka"], woj["netto"])
    assert k["woj_pensja"] == round(4806 - 4806 / 30 * 4, 2) and k["woj_chor"] == round(4 * 110.59, 2)
    assert k["kow_netto"] == kow["netto"]
    assert k["przelewy"] == round(lis["netto"] + woj["netto"] + kow["netto"], 2)
    assert k["pit_suma"] == lis["zaliczka"] + woj["zaliczka"] + kow["zaliczka"]
    min27 = kadry.lista_plac(zasadnicze=4950, ppk_prac=0, ppk_pracod=0, pensja_umowna=4950, par=dict(firma, minimalne=4950.0))
    assert k["wolna"] == min27["netto"] == 3703.93


def test_czas_pracy_i_nadgodziny():
    assert kadry.wymiar(2026, 12)["godziny"] == 160 and kadry.wymiar(2027, 1)["godziny"] == 152 and kadry.wymiar(2027, 5)["godziny"] == 144
    assert kadry.nadgodziny(6000, 168, 4, 8)["razem"] == 785.62
    n = kadry.nadgodziny(5400, 160, 6, 4)
    assert (n["stawka"], n["normalne"], n["dod50"], n["dod100"], n["razem"]) == (33.75, 337.5, 101.25, 135.0, 573.75)
    assert kadry.dodatek_nocny(2026, 11, 64)["kwota"] == 384.64
    assert kadry.wspolczynnik_ekwiwalentu(2026) == 20.92 == kadry.wspolczynnik_ekwiwalentu(2027)


def test_wypowiedzenie():
    d = dt.date(2026, 11, 17)
    assert kadry.koniec_wypowiedzenia(d, "3m") == dt.date(2027, 2, 28)
    assert kadry.koniec_wypowiedzenia(d, "1m") == dt.date(2026, 12, 31)
    assert kadry.koniec_wypowiedzenia(d, "2t") == dt.date(2026, 12, 5)
    assert kadry.koniec_wypowiedzenia(dt.date(2027, 1, 29), "3m") == dt.date(2027, 4, 30)


def test_potracenia_z_wynagrodzenia_i_zasilku():
    assert kadry.minimalne_netto(250, 300, 2.0) == 3501.73 and kadry.minimalne_netto(250, 300, 0) == 3605.85 and kadry.minimalne_netto(250, 0, 2.0) == 3201.73
    p = kadry.potracenia(3893.29, "inne", 1200, 250, 300, 2.0)
    assert (p["granica"], p["kwota_wolna"], p["max"]) == (1946.65, 3501.73, 391.56)
    z = kadry.potracenia_zasilek(800.76, 6, "inne", 9000)
    assert (z["granica"], z["kwota_wolna"], z["max"]) == (200.19, 280.31, 200.19)
    assert kadry.potracenia(7830.19, "inne", 8799.81, 250, 0, 2.0)["max"] == 3915.10


def test_kody_zwua_spojne():
    assert {"20R", "22R", "23R", "24R", "25R", "28R", "43R", "46R", "53W"} <= set(kadry.TRYBY_ROZW)
    assert {"400", "402", "403", "404", "407", "442", "550"} <= set(kadry.PODSTAWY_ROZW)
    for tryb, podstawy in kadry.PARY_TRYB_PODSTAWA.items():
        assert tryb in kadry.TRYBY_ROZW, tryb
        assert all(p in kadry.PODSTAWY_ROZW for p in podstawy), (tryb, podstawy)
    assert "403" in kadry.PARY_TRYB_PODSTAWA["23R"] and "402" in kadry.PARY_TRYB_PODSTAWA["46R"]
