# -*- coding: utf-8 -*-
"""Ćwiczenia w Mentorze: definicje, sprawdzenia (istnienie pliku ≠ zaliczenie), uruchamianie interpreterem kursu, pytest."""

import pytest

import cwiczenia as C


def _zad(kurs_json, zid):
    return next(z for t in kurs_json["tygodnie"] for z in t["zadania"] if z["id"] == zid)


def test_definicje_z_kursu(kurs_json):
    d = C.definicja(_zad(kurs_json, "t0z3"))
    assert d["plik"] == "hello.py" and d["sprawdzenie"]["rodzaj"] == "wyjscie_zawiera" and d["przyklad"] and d["szablon"]
    d = C.definicja(_zad(kurs_json, "t1z2"))
    assert d["sprawdzenie"]["stdin"] == "6\n*\n3\n" and d["sprawdzenie"]["tekst"] == ["18"]
    d = C.definicja(_zad(kurs_json, "t7z1"))
    assert d["sprawdzenie"]["rodzaj"] == "pytest"
    assert C.definicja(_zad(kurs_json, "t0z1")) is None, "zadanie bez pliku .py — bez ćwiczenia"
    assert C.definicja(_zad(kurs_json, "t0z2")) is None, "CLAUDE.md to nie .py"
    d = C.definicja({"id": "x", "tytul": "X", "pliki": ["cos.py"]})
    assert d["sprawdzenie"] == {"rodzaj": "plik_istnieje"} and "cos.py" in d["szablon"], "domyślne: tylko istnienie pliku"
    d = C.definicja({"id": "x", "tytul": "X", "pliki": ["cos.py"], "cwiczenie": {"sprawdzenie": {"rodzaj": "nieznany"}}})
    assert d["sprawdzenie"]["rodzaj"] == "plik_istnieje", "nieznany rodzaj sprawdzenia → bezpieczny domyślny"
    assert C.definicja({"id": "x", "tytul": "X", "pliki": [], "cwiczenie": {"plik": "../x.py"}}) is None, "ścieżka poza PRACA odrzucona"


def test_istnienie_pliku_nie_zalicza(srodowisko_kursu, tmp_path):
    d = C.definicja({"id": "x", "tytul": "X", "pliki": ["cos.py"]})
    w = C.wykonaj_sprawdzenie(srodowisko_kursu, d, tmp_path / "cos.py")
    assert w["status"] == C.STATUS_BLAD and "Brak pliku" in w["opis"]
    (tmp_path / "cos.py").write_text("print('x')\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(srodowisko_kursu, d, tmp_path / "cos.py")
    assert w["status"] == C.STATUS_WYMAGA and w["opis"] == "Plik istnieje — wymaga sprawdzenia"


def test_wyjscie_zawiera_i_bledy(srodowisko_kursu, kurs_json, tmp_path):
    sr = srodowisko_kursu
    d = C.definicja(_zad(kurs_json, "t0z3"))
    p = tmp_path / "hello.py"
    p.write_text(d["szablon"], encoding="utf-8")
    assert C.wykonaj_sprawdzenie(sr, d, p)["status"] == C.STATUS_BLAD, "sam szablon nie zalicza"
    p.write_text('import datetime\nprint("Cześć")\nprint("Dziś", datetime.date.today())\n', encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_ZALICZONE, w
    p.write_text('print("Cześć"\n', encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_BLAD and "SyntaxError" in w["opis"]
    d = C.definicja(_zad(kurs_json, "t1z3"))
    p = tmp_path / "wiek.py"
    p.write_text('r=int(input())\nprint("niepełnoletni" if 2026-r<18 else "pełnoletni")\n', encoding="utf-8")
    assert C.wykonaj_sprawdzenie(sr, d, p)["status"] == C.STATUS_ZALICZONE
    p.write_text('r=int(input())\nprint("niepełnoletni")\n', encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_BLAD and "niepożądane" in w["opis"]
    p.write_text("while True:\n    pass\n", encoding="utf-8")
    d["sprawdzenie"]["limit_s"] = 2
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_BLAD and "nie skończył" in w["opis"]


def test_sprawdzenie_pytest(srodowisko_kursu, kurs_json, tmp_path):
    sr = srodowisko_kursu
    d = C.definicja(_zad(kurs_json, "t7z1"))
    (tmp_path / "funkcje.py").write_text("def pole_prostokata(a, b):\n    return a * b\n", encoding="utf-8")
    p = tmp_path / "test_funkcje.py"
    p.write_text(d["szablon"], encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_ZALICZONE and "passed" in w["opis"], w
    p.write_text("def test_zle():\n    assert 1 == 2\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, p)
    assert w["status"] == C.STATUS_BLAD and "nie przechodzą" in w["opis"]
    assert not (tmp_path / ".pytest_cache").exists(), "bez śmieci w katalogu ucznia"


def test_edytor_nigdy_startfile():
    """Plik .py nie może być otwierany przez os.startfile (Windows uruchomiłby go) — tylko edytorem."""
    import ast
    import inspect
    drzewo = ast.parse(inspect.getsource(C))
    wywolania = [n for n in ast.walk(drzewo) if isinstance(n, ast.Attribute) and n.attr == "startfile"]
    assert not wywolania
