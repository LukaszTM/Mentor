# -*- coding: utf-8 -*-
"""Katalog danych, migracja, lista programów (wbudowane + paczki), walidacja kursów."""

import json
import os
from pathlib import Path

import program


def test_katalog_danych_z_env():
    assert program.KATALOG_DANYCH.resolve() == Path(os.environ["MENTOR_DANE"]).resolve()
    for k in (program.KATALOG_PROGRAMOW, program.KATALOG_KURSOW, program.KATALOG_SRODOWISK, program.KATALOG_LOGOW, program.KATALOG_POBRANE):
        assert k.is_dir() and k.resolve().is_relative_to(program.KATALOG_DANYCH.resolve())
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


def test_kurs_kadry_zrodla_i_lekcje_zagraniczne(repo):
    """Kurs kadrowy 3.0: 48 lekcji, lekcje z materiałów zagranicznych w planie, źródła lekcji [tytuł, https, data dostępu], rejestr źródeł programu."""
    d = json.loads((repo / "programy" / "kadry-i-place.json").read_text(encoding="utf-8"))
    assert d["wersja"] == "3.0" and d["stan_prawny"] == "18 listopada 2026"
    lekcje = {l["id"]: l for l in d["lekcje"]}
    assert len(lekcje) == 48
    assert lekcje["praktyki_hr_zagranica"]["tydzien"] == 2 and lekcje["prawo_ue_i_swiat"]["tydzien"] == 11
    for lid in ("mobbing_dyskryminacja_2026", "kontrola_pip_zus", "cudzoziemcy_b2b", "prawo_ue_i_swiat", "praktyki_hr_zagranica", "wskazniki_2026"):
        zr = lekcje[lid]["zrodla"]
        assert zr, lid
        for z in zr:
            assert len(z) == 3 and z[1].startswith("https://") and z[2].startswith("dostęp "), (lid, z)
    assert len(d["zrodla_kursu"]) >= 50 and all(len(z) == 3 for z in d["zrodla_kursu"])
    # poprawki audytu widoczne w treści
    m = lekcje["mobbing_dyskryminacja_2026"]["wyjasnienie"]
    assert "ZADOŚĆUCZYNIENIE" in m and "NIE zawiera przepisu zwalniającego" in m and "obwieszczenie" not in m.split("Nie „obwieszczenie”")[0][-200:]
    p = lekcje["kontrola_pip_zus"]["wyjasnienie"]
    assert "2 000–60 000" in p and "do 10 000 zł" in p and "8.07.2026" in p
    c = lekcje["cudzoziemcy_b2b"]["wyjasnienie"]
    assert "7 DNI" in c and "4.03.2027" in c
    for w in d["tygodnie"]:
        assert w["czas_min"] <= 540, w["tydzien"]
