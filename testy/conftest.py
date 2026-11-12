# -*- coding: utf-8 -*-
"""
Testy Mentora (pytest). Uruchom z katalogu repozytorium:  python -m pytest testy -q

Każda sesja testowa dostaje własny katalog danych (MENTOR_DANE) i katalog PRACA (MENTOR_PRACA) w tmp — testy nie dotykają
%LOCALAPPDATA%\\Mentor ani Dokumentów użytkownika. Zmienne muszą być ustawione PRZED importem modułu program.
"""

import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
_TMP = Path(tempfile.mkdtemp(prefix="mentor-testy-"))
os.environ["MENTOR_DANE"] = str(_TMP / "dane")
os.environ["MENTOR_PRACA"] = str(_TMP / "praca")
sys.path.insert(0, str(REPO))

import program  # noqa: E402
import paczki  # noqa: E402
import srodowisko  # noqa: E402


@pytest.fixture(scope="session")
def repo():
    return REPO


@pytest.fixture(scope="session")
def tmp_sesji():
    return _TMP


@pytest.fixture(scope="session")
def kurs_json():
    return json.loads((REPO / "programy" / "python-junior-qa.json").read_text(encoding="utf-8"))


@pytest.fixture
def zip_kursu(tmp_path, kurs_json):
    """Fabryka paczek ZIP: zip_kursu(id, wersja, manifest=None, skrypty=False, requirements=None, nazwa_json=...)."""

    def fabryka(kurs_id="kurs-testowy", wersja="1.0", manifest=None, skrypty=False, requirements=None, nazwa_json="kurs_mentor.json", dodatkowe=None):
        src = tmp_path / f"src-{kurs_id}-{wersja}"
        src.mkdir(parents=True, exist_ok=True)
        d = dict(kurs_json)
        d["id"] = kurs_id
        d["wersja"] = wersja
        d["nazwa"] = f"Kurs testowy {kurs_id}"
        (src / nazwa_json).write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        if skrypty:
            (src / "install.bat").write_text("@echo off\necho NIE > %TEMP%\\mentor_test_bat.txt\n", encoding="utf-8")
            (src / "setup.ps1").write_text("New-Item $env:TEMP\\mentor_test_ps1.txt\n", encoding="utf-8")
        if requirements:
            (src / "requirements.txt").write_text(requirements, encoding="utf-8")
        (src / "materialy").mkdir(exist_ok=True)
        (src / "materialy" / "START_TUTAJ.md").write_text("# start\n", encoding="utf-8")
        for nazwa, tresc in (dodatkowe or {}).items():
            (src / nazwa).parent.mkdir(parents=True, exist_ok=True)
            (src / nazwa).write_text(tresc, encoding="utf-8")
        cel = tmp_path / f"{kurs_id}-{wersja}.zip"
        return paczki.zbuduj_paczke(src, cel, manifest=manifest)
    return fabryka


@pytest.fixture(scope="session")
def srodowisko_kursu(kurs_json):
    """Prawdziwe środowisko kursu (.venv + biblioteki z locka) — budowane raz na sesję. Wymaga internetu (PyPI)."""
    wym = paczki.wymagania_kursu(kurs_json)
    sr = srodowisko.Srodowisko("python-junior-qa", wym)
    if not sr.python_venv():
        import queue
        import threading
        q = queue.Queue()
        d = sr.diagnoza(0)
        kroki = [k["id"] for k in sr.plan(d) if k["id"] in ("venv", "pakiety")]
        sr.instaluj(kroki, q, threading.Event(), 0)
        wiad = []
        while True:
            m = q.get(timeout=5)
            wiad.append(m)
            if m[0] == "koniec":
                break
        assert wiad[-1][1]["ok"], wiad[-1][1]["bledy"]
        sr._wiadomosci_instalacji = wiad
    return sr


@pytest.fixture
def wymagania_kursu(kurs_json):
    return paczki.wymagania_kursu(kurs_json)
