# -*- coding: utf-8 -*-
"""Katalog danych, migracja, lista programów (wbudowane + paczki), walidacja kursów."""

import json
import os
from pathlib import Path

import program


def test_katalog_danych_z_env():
    assert str(program.KATALOG_DANYCH) == os.environ["MENTOR_DANE"]
    for k in (program.KATALOG_PROGRAMOW, program.KATALOG_KURSOW, program.KATALOG_SRODOWISK, program.KATALOG_LOGOW, program.KATALOG_POBRANE):
        assert k.is_dir() and k.is_relative_to(program.KATALOG_DANYCH)
    assert program.PLIK_DANYCH.parent == program.KATALOG_DANYCH


def test_wbudowane_programy_rozpakowane():
    nazwy = {sc.name for sc, *_ in program.lista_programow()}
    assert {"python-junior-qa.json", "kadry-i-place.json"} <= nazwy


def test_walidacja_wbudowanych(repo):
    for f in ("python-junior-qa.json", "kadry-i-place.json"):
        dane, bledy = program.wczytaj_plik(repo / "programy" / f)
        assert not bledy, (f, bledy)


def test_kurs_python_ma_srodowisko_i_cwiczenia(kurs_json):
    s = kurs_json["srodowisko"]
    assert s["python"] == ">=3.11,<3.14" and set(s["pakiety"]) == {"pytest", "requests", "selenium", "flask"}
    assert s["przegladarka"] == "edge" and s["przegladarka_od_tygodnia"] == 8
    cw = [z for t in kurs_json["tygodnie"] for z in t["zadania"] if z.get("cwiczenie")]
    assert len(cw) >= 30
    for z in cw:
        spr = z["cwiczenie"].get("sprawdzenie") or {}
        assert spr.get("rodzaj") in ("uruchom_bez_bledu", "wyjscie_zawiera", "pytest", "plik_istnieje"), z["id"]


def test_meta_kursu_brak():
    assert program.meta_kursu("nie-ma-takiego") == {}
    assert program.katalog_kursu("nie-ma-takiego") is None


def test_migracja_struktura():
    assert set(program.MIGRACJA) == {"wykonana", "kroki", "bledy"}
    assert not program.MIGRACJA["bledy"], program.MIGRACJA["bledy"]
