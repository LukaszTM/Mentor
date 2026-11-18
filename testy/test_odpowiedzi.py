# -*- coding: utf-8 -*-
"""Sprawdzanie automatyczne: silnik odpowiedzi.py, klucze ćwiczeń i formularzy kursu „Kadry i płace”."""

import datetime as dt
import importlib.util
import json
import sys

import pytest

import odpowiedzi as O
import program


@pytest.fixture(scope="module")
def kurs(repo):
    return json.loads((repo / "programy" / "kadry-i-place.json").read_text(encoding="utf-8"))


def _pola_kursu(kurs):
    for l in kurs["lekcje"]:
        for i, c in enumerate(l.get("cwiczenia", []), 1):
            for p in c.get("odpowiedzi") or []:
                yield f"{l['id']}:{i}", p, c
    for f in kurs["formularze"]:
        for s in f["sekcje"]:
            for p in s["pola"]:
                yield "formularz:" + f["id"], p, None


def test_odczyt_liczb_dat_i_tekstu():
    assert O.liczba("3 605,85 zł") == 3605.85 == O.liczba("3605.85") == O.liczba("3.605,85")
    assert O._warianty_liczby("3.605") == [3.605, 3605.0]
    assert O.liczba("1 993") == 1993.0 and O.liczba("12,5%") == 12.5 and O.liczba("−40") == -40.0 and O.liczba("abc") is None and O.liczba("") is None
    d = dt.date(2027, 2, 28)
    assert O.data("2027-02-28") == d == O.data("28.02.2027") == O.data("28.2.27") == O.data("28 lutego 2027 r.") == O.data("28/02/2027")
    assert O.data("28.02", rok=2027) == d and O.data("28.02") is None and O.data("31.02.2027") is None
    assert O.tekst_norm("01 10 00") == O.tekst_norm("011000") and O.tekst_norm("Łódź") == "lodz" and O.tekst_norm("art. 52 §1 pkt 1") == "art521pkt1"


def test_sprawdzanie_pol_i_podpowiedzi():
    p = {"id": "n", "etykieta": "Netto", "typ": "kwota", "wartosc": 3605.85, "bledy": [{"wartosc": 3501.73, "komunikat": "to netto z PPK"}]}
    assert O.sprawdz_pole(p, "3 605,85") == (True, "dobrze") and O.sprawdz_pole(p, "3501,73") == (False, "to netto z PPK")
    assert O.sprawdz_pole(p, "")[0] is None and "liczb" in O.sprawdz_pole(p, "trzy tysiące")[1] and "poniżej 1 zł" in O.sprawdz_pole(p, "3605,35")[1]
    for wpis in ("1", "3605", "3605,35", "9999", "abc"):                     # komunikat nigdy nie zdradza wyniku
        assert "3605,85" not in O.sprawdz_pole(p, wpis)[1] and "3 605,85" not in O.sprawdz_pole(p, wpis)[1]
    d = {"id": "d", "etykieta": "Termin", "typ": "data", "wartosc": "2027-03-01"}
    assert O.sprawdz_pole(d, "1.03.2027")[0] is True and O.sprawdz_pole(d, "1.03")[0] is True
    assert "sobota lub niedziela" in O.sprawdz_pole(d, "28.02.2027")[1] and "jednego dnia" in O.sprawdz_pole(d, "2.03.2027")[1]
    t = {"id": "t", "etykieta": "Kod", "typ": "tekst", "wartosc": ["23R"]}
    assert O.sprawdz_pole(t, "23 r")[0] is True and O.sprawdz_pole(t, "22R")[0] is False
    z = {"id": "z", "etykieta": "Podstawa", "typ": "tekst", "zawiera": ["52", "pkt 1"]}
    assert O.sprawdz_pole(z, "art. 52 §1 pkt 1 KP")[0] is True and O.sprawdz_pole(z, "art. 52")[0] is False
    w = {"id": "w", "etykieta": "Odprawa?", "typ": "wybor", "opcje": ["tak", "nie"], "wartosc": "nie"}
    r = O.sprawdz([p, d, t, w], {"n": "3605,85", "d": "1.03.2027", "t": "23R"})
    assert (r["ok"], r["max"], r["puste"], r["komplet"]) == (3, 4, 1, False)
    assert O.poprawna(p) == "3 605,85" and O.poprawna(d) == "01.03.2027" and O.poprawna(t) == "23R"
    assert O.waliduj_pola([p, d, t, z, w]) == [] and O.waliduj_pola([]) and O.waliduj_pola([p, p])
    assert O.waliduj_pola([{"id": "x", "etykieta": "X", "typ": "data", "wartosc": "32.01"}])


def test_kurs_kadry_ma_klucze_i_formularze(kurs):
    z_kluczem = [(l["id"], i) for l in kurs["lekcje"] for i, c in enumerate(l["cwiczenia"], 1) if c.get("odpowiedzi")]
    assert len(z_kluczem) >= 85 and len([1 for _ in _pola_kursu(kurs)]) >= 500
    assert "formularze" in kurs["narzedzia"] and len(kurs["formularze"]) >= 10
    for f in kurs["formularze"]:
        assert f["scenariusz"] and f["wzor"] and f["lekcja"] in {l["id"] for l in kurs["lekcje"]}
    assert program.waliduj(json.loads(json.dumps(kurs))) == []
    zepsuty = json.loads(json.dumps(kurs))
    zepsuty["lekcje"][3]["cwiczenia"][0]["odpowiedzi"][0]["typ"] = "nieznany"
    assert any("nieznany typ" in b for b in program.waliduj(zepsuty))


def test_kazdy_klucz_zalicza_sie_i_nie_przepuszcza_typowych_bledow(kurs):
    for gdzie, p, _c in _pola_kursu(kurs):
        assert O.waliduj_pola([p], gdzie) == [], (gdzie, p["id"])
        assert O.sprawdz_pole(p, O.poprawna(p))[0] is True, (gdzie, p["id"])
        for b in p.get("bledy") or []:
            wpis = O.poprawna(dict(p, wartosc=b["wartosc"], bledy=None))
            ok, info = O.sprawdz_pole(p, wpis)
            assert ok is False and info == b["komunikat"], (gdzie, p["id"], wpis, info)
            assert len(O.poprawna(p)) < 4 or O.poprawna(p) not in info, (gdzie, p["id"])


def test_klucze_cwiczen_wystepuja_w_rozwiazaniach(kurs, repo):
    """Ten sam strażnik co przy budowaniu kursu: wartość klucza musi być w treści, wyniku albo rozwiązaniu ćwiczenia."""
    zr = repo / "programy" / "zrodla" / "kadry_i_place"
    sys.path.insert(0, str(zr))
    try:
        spec = importlib.util.spec_from_file_location("zbuduj_kadry", zr / "zbuduj.py")
        zb = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(zb)
    finally:
        sys.path.remove(str(zr))
    brak = []
    for gdzie, p, c in _pola_kursu(kurs):
        if c is not None and not zb.klucz_w_tekscie(p, " ".join(str(c.get(k, "")) for k in ("tresc", "wynik", "rozwiazanie"))):
            brak.append((gdzie, p["id"]))
    assert not brak, brak
    assert len(kurs["aktualizacje"]) >= 15 and [a["data"] for a in kurs["aktualizacje"]] == sorted(a["data"] for a in kurs["aktualizacje"])
