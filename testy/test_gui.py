# -*- coding: utf-8 -*-
"""Smoke GUI (Tkinter): nowe widoki, import ZIP przez Ustawienia, pasek ćwiczeń, nieblokująca diagnoza. Pomijane bez wyświetlacza."""

import json
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import pytest


def _ma_display():
    try:
        r = tk.Tk()
        r.destroy()
        return True
    except tk.TclError:
        return False


pytestmark = pytest.mark.skipif(not _ma_display(), reason="brak wyświetlacza (uruchom pod xvfb-run)")


@pytest.fixture(scope="module")
def app():
    import mentor
    klasa = [o for n in dir(mentor) if isinstance((o := getattr(mentor, n)), type) and issubclass(o, tk.Tk) and o is not tk.Tk][0]
    a = klasa()
    a.update()
    yield a
    try:
        a.destroy()
    except tk.TclError:
        pass


def _czekaj(app, warunek, limit=60):
    t0 = time.time()
    while time.time() - t0 < limit:
        app.update()
        if warunek():
            return True
        time.sleep(0.03)
    return False


def test_widoki_otwieraja_sie(app):
    import widok_srodowisko
    from program import P
    for w in ("panel", "start", "plan", "projekt", "srodowisko", "ustawienia"):
        app.pokaz(w)
        app.update()
        assert app.aktywny == w
    st = widok_srodowisko._stan(app)
    assert st["kurs"] == P.id
    assert _czekaj(app, lambda: not st.get("w_toku")), "diagnoza w tle musi się skończyć"
    assert st.get("diag"), "tabela statusów wypełniona z realnej diagnozy"


def test_diagnoza_nie_blokuje_gui(app):
    import widok_srodowisko
    app.pokaz("srodowisko")
    app.update()
    st = widok_srodowisko._stan(app)
    _czekaj(app, lambda: not st.get("w_toku"))
    widok_srodowisko._diagnozuj(app, odswiez=True)
    t0 = time.time()
    klatki = 0
    while st.get("w_toku") and time.time() - t0 < 60:
        app.update()
        klatki += 1
        time.sleep(0.01)
    assert not st.get("w_toku") and klatki > 3, "pętla GUI obracała się w czasie diagnozy"


def test_import_zip_przez_ustawienia(app, zip_kursu, monkeypatch, tmp_path):
    import paczki
    from program import P
    zipp = zip_kursu("kurs-gui", "1.0", skrypty=True)
    monkeypatch.setattr(filedialog, "askopenfilename", lambda **k: str(zipp))
    dialogi = []
    monkeypatch.setattr(messagebox, "askyesno", lambda t, m, **k: (dialogi.append(("pyt", t, m)), True)[1])
    monkeypatch.setattr(messagebox, "showinfo", lambda t, m, **k: dialogi.append(("info", t, m)))
    monkeypatch.setattr(messagebox, "showerror", lambda t, m, **k: dialogi.append(("err", t, m)))
    stary = P.id
    app._importuj_zip()
    app.update()
    assert P.id == "kurs-gui", dialogi
    assert dialogi[0][0] == "pyt" and "Identyfikator: kurs-gui" in dialogi[0][2] and "skrypty" in dialogi[0][2].lower()
    assert app.aktywny == "srodowisko", "kurs wymaga środowiska → zakładka Środowisko"
    assert app.stan.d["projekt"].endswith("PRACA")
    # wrogi zip → błąd, bez zmiany kursu
    zly = tmp_path / "zly.zip"
    import zipfile
    with zipfile.ZipFile(zly, "w") as z:
        z.writestr("kurs_mentor.json", json.dumps({"format": "mentor-program/1", "id": "zly", "nazwa": "Zły", "tygodnie": [], "lekcje": []}))
        z.writestr("../evil.txt", "x")
    monkeypatch.setattr(filedialog, "askopenfilename", lambda **k: str(zly))
    dialogi.clear()
    app._importuj_zip()
    assert dialogi and dialogi[0][0] == "err" and P.id == "kurs-gui"
    # powrót do poprzedniego programu i sprzątanie
    for sc, *_ in __import__("program").lista_programow():
        if sc.stem == stary or (sc.name == "kurs.json" and sc.parent.name == stary):
            app.ustaw_program(sc)
            break
    paczki.usun_kurs("kurs-gui")
    assert P.id == stary


def test_pasek_cwiczen_w_planie(app, tmp_path):
    import cwiczenia
    from program import P
    app.stan.d["projekt"] = str(tmp_path)
    app.stan.zapisz()
    app._pliki_cache.clear()
    app.pokaz_tydzien(1)
    app.update()
    teksty = []

    def zbierz(w):
        for c in w.winfo_children():
            if isinstance(c, (tk.Label, tk.Button)):
                try:
                    teksty.append(c.cget("text"))
                except tk.TclError:
                    pass
            zbierz(c)
    zbierz(app.tresc)
    assert any("Ćwiczenie w Mentorze" in t for t in teksty)
    assert any("Utwórz plik ćwiczenia" in t for t in teksty) and any("Sprawdź wynik" in t for t in teksty)
    zad = next(z for t in P.tygodnie for z in t["zadania"] if z["id"] == "t1z1")
    d = cwiczenia.definicja(zad)
    assert d["plik"] == "zmienne.py"
