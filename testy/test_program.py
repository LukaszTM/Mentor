# -*- coding: utf-8 -*-
"""Katalog danych, migracja, lista programów (wbudowane + paczki), walidacja kursów."""

import json
import os
from pathlib import Path

import paczki
import program
import pytest


def test_katalog_danych_z_env():
    assert program.KATALOG_DANYCH.resolve() == Path(os.environ["MENTOR_DANE"]).resolve()
    for k in (program.KATALOG_PROGRAMOW, program.KATALOG_KURSOW, program.KATALOG_SRODOWISK, program.KATALOG_LOGOW, program.KATALOG_POBRANE):
        assert k.is_dir() and k.resolve().is_relative_to(program.KATALOG_DANYCH.resolve())
    assert program.PLIK_DANYCH.parent == program.KATALOG_DANYCH


def test_wbudowane_programy_rozpakowane():
    nazwy = {sc.name for sc, *_ in program.lista_programow()}
    assert {"python-junior-qa.json", "kadry-i-place.json"} <= nazwy


def test_kursy_nie_sa_wbudowane_w_mentora(repo):
    """Jedyny program w EXE i w Mentor-windows.zip to domyślny python-junior-qa; kursy (kadry, vibe) to osobne paczki ZIP do importu."""
    spec = (repo / "mentor.spec").read_text(encoding="utf-8")
    datas = spec[spec.index("datas=["):spec.index("],", spec.index("datas=["))]
    assert '"programy/python-junior-qa.json"' in datas
    for zakazane in ("kadry-i-place", "vibe-coding", "programy/materialy"):
        assert zakazane not in datas, zakazane
    ci = (repo / ".github" / "workflows" / "build-exe.yml").read_text(encoding="utf-8")
    pakowanie = ci[ci.index("- name: Spakuj"):ci.index("Compress-Archive -Path pakiet\\Mentor")]
    assert "Copy-Item -Recurse programy pakiet" not in pakowanie and "materialy" not in pakowanie
    assert "sprawdz_paczki.py Mentor-windows.zip Kadry-i-place-kurs.zip Vibe-coding-kurs.zip" in ci
    for kid in ("kadry-i-place", "vibe-coding"):
        assert "nie jest wbudowany w Mentora" in (repo / "programy" / "materialy" / kid / "START_TUTAJ.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("kid", ["kadry-i-place", "vibe-coding"])
def test_paczka_kursu_importuje_sie_z_zip(repo, kid, tmp_path):
    """Paczka kursu (tak jak w CI: folder w ZIP) ma mentor-manifest.json, importuje się, a Mentor bierze materiały z kursy/<id>/paczka."""
    import shutil
    zp = shutil.make_archive(str(tmp_path / kid), "zip", repo / "programy" / "materialy", kid)
    pg = paczki.przejrzyj_zip(zp)
    assert pg["manifest"] and pg["manifest"]["course_id"] == kid and pg["id"] == kid
    w = paczki.importuj_zip(zp, nadpisz=True, utworz_prace=False)
    try:
        assert w["id"] == kid
        assert program.katalog_materialow(kid) == program.KATALOG_KURSOW / kid / "paczka"
        assert (program.katalog_materialow(kid) / "START_TUTAJ.md").is_file()
        assert kid in {json.loads(p.read_text(encoding="utf-8")).get("id") for p, *_ in program.lista_programow()}
    finally:
        paczki.usun_kurs(kid)


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
    """Kurs kadrowy 3.1: 48 lekcji, lekcje z materiałów zagranicznych w planie, źródła lekcji [tytuł, https, data dostępu], rejestr źródeł programu."""
    d = json.loads((repo / "programy" / "kadry-i-place.json").read_text(encoding="utf-8"))
    assert d["wersja"] == "3.1" and d["stan_prawny"] == "18 listopada 2026"
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
