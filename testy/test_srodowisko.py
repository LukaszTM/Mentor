# -*- coding: utf-8 -*-
"""Menedżer środowisk: lock, wersje, diagnoza z realnych uruchomień, .venv + pip z hashami, testy końcowe (pytest, API, Selenium osobno)."""

import json
import os
import queue
import sys
import threading
from pathlib import Path

import pytest

import srodowisko as S
from program import KATALOG_SRODOWISK


# ---------------------------------------------------------------- funkcje pomocnicze
@pytest.mark.parametrize("wersja,spec,oczek", [
    ("3.12.4", ">=3.11,<3.14", True), ("3.10.9", ">=3.11,<3.14", False), ("3.14.0", ">=3.11,<3.14", False),
    ("3.12.1", "3.12", True), ("3.13.2", "3.12", False), ("3.11.0", ">=3.11", True), ("3.12.0", "", True),
])
def test_wersja_spelnia(wersja, spec, oczek):
    assert S.wersja_spelnia(wersja, spec) is oczek


def test_sprawdz_lock_mentora():
    sc = S.sciezka_locka_mentora()
    assert sc and sc.exists()
    tekst = sc.read_text(encoding="utf-8")
    pakiety, bledy = S.sprawdz_lock(tekst)
    assert not bledy, bledy
    assert {p["nazwa"] for p in pakiety} >= {"pytest", "requests", "selenium", "flask"} and all(p["hashe"] >= 1 for p in pakiety)
    assert "--hash=sha256:" in tekst and "pytest==" in tekst and "selenium==" in tekst


@pytest.mark.parametrize("tekst", [
    "pytest==9.2.0\n",                                              # bez hasha
    "pytest==9.2.0 --hash=sha256:zzz\n",                           # zły hash
    "-e git+https://example.com/x.git#egg=x --hash=sha256:" + "a" * 64 + "\n",  # opcja instalacyjna
    "pytest>=9 --hash=sha256:" + "a" * 64 + "\n",                   # nieprzypięta wersja
    "--index-url https://zly.example\npytest==9.2.0 --hash=sha256:" + "a" * 64 + "\n",  # obce źródło
])
def test_sprawdz_lock_odrzuca(tekst):
    assert S.sprawdz_lock(tekst)[1], tekst


def test_sprawdz_pythona_realnie():
    info = S.sprawdz_pythona(sys.executable)
    assert info and info["wersja"].count(".") == 2
    assert S.sprawdz_pythona("/nie/ma/takiego/python") is None


def test_znajdz_pythony_znajduje_dzialajacy():
    pyth = S.znajdz_pythony(">=3.8")
    assert pyth, "co najmniej jeden działający Python poza venv"
    assert all(not p["venv"] for p in pyth)


def test_runtime_zadeklarowany_z_hashem():
    r = S.RUNTIME
    assert r["url"].startswith("https://github.com/astral-sh/python-build-standalone/releases/download/")
    assert len(r["sha256"]) == 64 and r["rozmiar"] > 10_000_000 and r["wersja"].startswith("3.12")


def test_env_czysty_bez_zmiennych_mentora(monkeypatch):
    monkeypatch.setenv("PYTHONHOME", "/x")
    monkeypatch.setenv("PYTHONPATH", "/y")
    monkeypatch.setenv("_MEIPASS2", "/z")
    env = S._env_czysty()
    for k in ("PYTHONHOME", "PYTHONPATH", "_MEIPASS2", "TCL_LIBRARY", "TK_LIBRARY"):
        assert k not in env


# ---------------------------------------------------------------- diagnoza i plan (nic nie instaluje)
def test_kurs_bez_wymagan_jest_gotowy():
    sr = S.Srodowisko("kurs-bez", {"zrodlo": "brak", "python": None, "pakiety": [], "narzedzia_wymagane": [], "narzedzia_opcjonalne": [], "przegladarka": None})
    assert not sr.wymaga_srodowiska()
    d = sr.diagnoza(0)
    assert d and d[0]["status"] == S.GOTOWE and sr.plan(d) == []


def test_diagnoza_przed_instalacja(wymagania_kursu):
    sr = S.Srodowisko("kurs-diag", wymagania_kursu)
    sr.usun_srodowisko()
    d = sr.diagnoza(0)
    st = {p["klucz"]: p for p in d}
    assert st["python"]["status"] in (S.GOTOWE, S.BRAK, S.ZLA_WERSJA)
    assert st["venv"]["status"] == S.BRAK and st["venv"]["akcja"] == "venv"
    for pak in ("pytest", "requests", "selenium", "flask"):
        assert st[f"pakiet:{pak}"]["status"] == S.BRAK
    assert st["przegladarka"]["status"] in (S.GOTOWE, S.OPCJONALNE), "przeglądarka potrzebna dopiero od tygodnia 8"
    assert st["przegladarka"]["wymagane"] is (st["przegladarka"]["status"] == S.GOTOWE)
    assert all(p["status"] == S.NIE_SPRAWDZONO for p in d if p["klucz"].startswith("test:"))
    assert not sr.gotowe()
    plan = sr.plan(d)
    ids = [k["id"] for k in plan]
    assert "venv" in ids and "pakiety" in ids and "testy" in ids
    for k in plan:
        assert k["opis"] and "zrodlo" in k and "rozmiar" in k and "internet" in k and "uprawnienia" in k
    d8 = sr.diagnoza(8)
    st8 = {p["klucz"]: p for p in d8}
    assert st8["przegladarka"]["wymagane"] is True
    sr.usun_srodowisko()


# ---------------------------------------------------------------- instalacja (realna; PyPI) — wykonana przez fixture srodowisko_kursu
def test_instalacja_venv_i_pakietow(srodowisko_kursu):
    sr = srodowisko_kursu
    assert sr.python_venv() and sr.python_venv().exists()
    wiad = getattr(sr, "_wiadomosci_instalacji", None)
    if wiad is not None:
        assert any(m[0] == "postep" for m in wiad) and any(m[0] == "log" for m in wiad) and any(m[0] == "krok" for m in wiad)
    wersje = sr.wersje_pakietow()
    assert wersje["pytest"].startswith("9.") and wersje["selenium"].startswith("4.") and wersje["flask"].startswith("3.")
    assert sr.log.exists()
    st = sr.stan()
    assert st["lock_sha"] == sr.lock_sha() and st["python_venv"]
    if not st.get("testy"):
        assert not sr.gotowe(), "bez testów końcowych nie ma GOTOWE"


def test_testy_koncowe(srodowisko_kursu):
    sr = srodowisko_kursu
    assert sr.python_venv(), "wymaga wcześniejszego test_instalacja_venv_i_pakietow"
    wyniki = sr.testy()
    assert wyniki["python"]["status"] == S.GOTOWE
    assert wyniki["importy"]["status"] == S.GOTOWE
    assert wyniki["pytest"]["status"] == S.GOTOWE and "passed" in wyniki["pytest"]["szczegoly"]
    assert wyniki["api"]["status"] == S.GOTOWE and "200" in wyniki["api"]["szczegoly"]
    # Selenium: raportowany osobno — GOTOWE tylko z realną przeglądarką, inaczej POMINIĘTO (nigdy udawane GOTOWE)
    assert wyniki["selenium"]["status"] in (S.GOTOWE, S.POMINIETO, S.BLAD)
    if S.znajdz_przegladarke("edge") and sys.platform.startswith("win"):
        assert wyniki["selenium"]["status"] == S.GOTOWE, wyniki["selenium"]
    d = sr.diagnoza(0)
    st = {p["klucz"]: p for p in d}
    assert st["test:pytest"]["status"] == S.GOTOWE and st["test:api"]["status"] == S.GOTOWE
    assert sr.gotowe()
    assert all("data" in t for t in wyniki.values())


def test_uruchom_plik_ucznia(srodowisko_kursu, tmp_path):
    sr = srodowisko_kursu
    inter, opis = sr.interpreter_ucznia()
    assert inter == sr.python_venv() and "venv" in opis
    p = tmp_path / "x.py"
    p.write_text("import requests, pytest\nn = input('n: ')\nprint('hej', n, requests.__version__)\n", encoding="utf-8")
    kod, out, err = sr.uruchom_plik_ucznia(p, wejscie="7\n", limit=30)
    assert kod == 0 and "hej 7 2." in out, (out, err)
    p.write_text("print(1/0)\n", encoding="utf-8")
    kod, out, err = sr.uruchom_plik_ucznia(p, limit=30)
    assert kod == 1 and "ZeroDivisionError" in err
    p.write_text("while True:\n    pass\n", encoding="utf-8")
    kod, out, err = sr.uruchom_plik_ucznia(p, limit=2)
    assert kod == -1 and "przerwano" in err
    anuluj = threading.Event()
    anuluj.set()
    kod, out, err = sr.uruchom_plik_ucznia(p, limit=30, anuluj=anuluj)
    assert kod == -1 and "anulowano" in err


def test_zmiana_locka_uniewaznia_gotowe(srodowisko_kursu, monkeypatch):
    sr = srodowisko_kursu
    assert sr.gotowe()
    monkeypatch.setattr(sr, "lock_sha", lambda: "inny")
    assert not sr.gotowe()
    d = sr.diagnoza(0)
    assert any(p["klucz"] == "test:pytest" and p["status"] == S.NIE_SPRAWDZONO for p in d)


def test_srodowisko_w_katalogu_danych(srodowisko_kursu):
    assert srodowisko_kursu.venv.is_relative_to(KATALOG_SRODOWISK)
    assert str(KATALOG_SRODOWISK).startswith(os.environ["MENTOR_DANE"])


# ---------------------------------------------------------------- runtime Pythona (etap 2) — tylko Windows, pobiera ok. 46 MB
@pytest.mark.skipif(not sys.platform.startswith("win"), reason="zarządzany runtime Pythona dotyczy Windows")
def test_runtime_pobranie_i_venv(wymagania_kursu):
    sr = S.Srodowisko("kurs-runtime", wymagania_kursu)
    q = queue.Queue()
    logi = []
    exe = sr._zainstaluj_runtime(q, threading.Event(), logi.append)
    assert Path(exe).exists() and "python.exe" in exe
    info = S.sprawdz_pythona(exe)
    assert info and info["wersja"] == S.RUNTIME["wersja"]
    assert any(m[0] == "postep" for m in list(q.queue))
    assert any("SHA-256" in l for l in logi)
    # runtime jest widoczny jako „zarządzany” i NIE jest Pythonem Mentora
    znal = [p for p in S.znajdz_pythony(">=3.12,<3.13") if p["zarzadzany"]]
    assert znal and Path(znal[0]["exe"]).resolve() == Path(exe).resolve()
    sr._utworz_venv(exe, logi.append)
    pv = sr.python_venv()
    assert pv and S.sprawdz_pythona(pv)["venv"]
    kod, out, err = S.uruchom([str(pv), "-m", "pip", "--version"], timeout=60)
    assert kod == 0 and "pip" in out
    sr.usun_srodowisko()


def test_pobierz_odrzuca_zly_hash(tmp_path, monkeypatch):
    """Pobranie z niezgodną sumą SHA-256 musi być odrzucone (plik usunięty), nawet gdy serwer odpowiada poprawnie."""
    import http.server
    import threading as th
    import urllib.request

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Length", "5")
            self.end_headers()
            self.wfile.write(b"abcde")

        def log_message(self, *a):
            pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    t = th.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        cel = tmp_path / "plik.bin"
        with pytest.raises(RuntimeError):
            S.pobierz(f"http://127.0.0.1:{srv.server_port}/x", cel, "0" * 64, 5, lambda p, c: None, threading.Event())
        assert not cel.exists()
    finally:
        srv.shutdown()
