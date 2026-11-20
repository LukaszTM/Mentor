# -*- coding: utf-8 -*-
"""Kurs „Vibe coding od podstaw”: budowanie ze źródeł, standard lekcji, klucze odpowiedzi, kod w lekcjach, niezależne weryfikatory zadań
(przechodzą na rozwiązaniach wzorcowych, nie przechodzą na pustym katalogu, plikach startowych i zapisach agenta z błędem), paczka materiałów i Mentor end-to-end."""

import json
import shutil
import subprocess
import sys

import pytest

import cwiczenia as C
import odpowiedzi as O
import program


MODULY = ("zbuduj", "reszta", "powtorki", "wspolne", "sprawdz_weryfikatory", "zadania_wszystkie", "materialy",
          *(f"zadania{i}" for i in range(4)), *(f"etap{i}{b}" for i in range(4) for b in ("", "b")))


def _wyczysc():
    for m in MODULY:
        sys.modules.pop(m, None)


@pytest.fixture(scope="module")
def zrodla(repo):
    """Źródła kursu na początku sys.path; moduły o tych samych nazwach z innych kursów (zbuduj, reszta, powtorki) usunięte z pamięci."""
    z = repo / "programy" / "zrodla" / "vibe_coding"
    _wyczysc()
    sys.path.insert(0, str(z))
    yield z
    sys.path.remove(str(z))
    _wyczysc()


@pytest.fixture(scope="module")
def vibe(repo):
    return json.loads((repo / "programy" / "vibe-coding.json").read_text(encoding="utf-8"))


def test_json_zgodny_ze_zrodlami(zrodla, vibe):
    import zbuduj
    zbudowany = json.loads(json.dumps(zbuduj.zbuduj(), ensure_ascii=False))
    assert zbudowany == vibe, "programy/vibe-coding.json nieaktualny — uruchom programy/zrodla/vibe_coding/zbuduj.py"


def test_walidacja_i_struktura(vibe):
    assert program.waliduj(vibe) == []
    assert vibe["id"] == "vibe-coding" and len(vibe["tygodnie"]) == 16 and len(vibe["lekcje"]) == 48
    assert all(w["czas_min"] <= 540 for w in vibe["tygodnie"])
    assert 110 * 60 <= sum(w["czas_min"] for w in vibe["tygodnie"]) <= 130 * 60
    for l in vibe["lekcje"]:
        assert [c["rodzaj"] for c in l["cwiczenia"]] == ["prowadzone", "samodzielne"], l["id"]
        assert l["zrodla"] and all(z[1].startswith("https://") for z in l["zrodla"]), l["id"]
        assert len(l["typowe_bledy"]) >= 2 and 3 <= len(l["test"]) <= 5, l["id"]
    lekcje = {l["id"] for l in vibe["lekcje"]}
    assert all(q["lekcja"] in lekcje for qs in vibe["quizy"].values() for q in qs)
    assert all(q["lekcja"] in lekcje for q in vibe["diagnoza"])


def test_klucze_odpowiedzi_przyjmuja_poprawne_wartosci(vibe):
    n = 0
    for l in vibe["lekcje"]:
        for c in l["cwiczenia"]:
            if c.get("odpowiedzi"):
                assert O.waliduj_pola(c["odpowiedzi"], l["id"]) == []
                wynik = O.sprawdz(c["odpowiedzi"], {p["id"]: O.poprawna(p) for p in c["odpowiedzi"]})
                assert wynik["komplet"], (l["id"], wynik)
                n += 1
    assert n >= 90, n
    for f in vibe["formularze"]:
        pola = [p for s in f["sekcje"] for p in s["pola"]]
        assert O.sprawdz(pola, {p["id"]: O.poprawna(p) for p in pola})["komplet"], f["id"]


def test_typowe_pomylki_sa_rozpoznawane(vibe):
    """Pola z listą „bledy” dają podpowiedź (nie „nie zgadza się”) dla typowej pomyłki — i nigdy nie zaliczają jej."""
    for l in vibe["lekcje"]:
        for c in l["cwiczenia"]:
            for p in c.get("odpowiedzi") or []:
                for b in p.get("bledy") or []:
                    ok, info = O.sprawdz_pole(p, b["wartosc"])
                    assert ok is False and info == b["komunikat"], (l["id"], p["id"], b, info)


def test_kod_z_lekcji_daje_podane_wyjscie(zrodla, srodowisko_kursu):
    import wspolne
    import zbuduj  # noqa: F401  (rejestruje kod ze wszystkich lekcji)
    assert len(wspolne.KOD_DO_SPRAWDZENIA) >= 15
    for gdzie, kod, oczekiwane in wspolne.KOD_DO_SPRAWDZENIA:
        if oczekiwane is None:
            continue
        p = subprocess.run([str(srodowisko_kursu.python_venv()), "-X", "utf8", "-c", kod], capture_output=True, text=True, encoding="utf-8", timeout=60)
        assert p.stdout.replace("\r\n", "\n") == oczekiwane, (gdzie, p.stdout, p.stderr[-500:])


def test_sumy_weryfikatorow_w_zadaniach(zrodla, vibe):
    import zbuduj
    n = 0
    for w in vibe["tygodnie"]:
        for z in w["zadania"]:
            s = z["cwiczenie"]["sprawdzenie"]
            if s["rodzaj"] == "test_zewnetrzny":
                assert s["sha256"] == zbuduj.sha_weryfikatora(s["plik_testu"].split("/")[-1]), z["id"]
                n += 1
    assert n >= 35, n


@pytest.mark.skipif(not shutil.which("git"), reason="weryfikatory tygodni 6–15 wymagają programu git")
def test_weryfikatory_wzorce_puste_i_bledne(zrodla, srodowisko_kursu):
    import sprawdz_weryfikatory as SW
    assert SW.kontrola(log=lambda *_: None, python=str(srodowisko_kursu.python_venv())) == []


def test_paczka_materialow(repo, vibe):
    mat = repo / "programy" / "materialy" / "vibe-coding"
    p = subprocess.run([sys.executable, str(mat / "testy" / "sprawdz_kurs.py")], capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0, p.stdout + p.stderr
    assert json.loads((mat / "kurs_mentor.json").read_text(encoding="utf-8")) == vibe, "paczka nieaktualna — uruchom materialy.py"
    for f in ("START_TUTAJ.md", "mentor-manifest.json", "pytest.ini", "dane/rezerwacje.csv", "pomoc/diff_agenta.md", "pomoc/brief_klienta.md", "przyklady/odpowiedzi_agenta/v4z3.md", "rozwiazania/kod/system.py"):
        assert (mat / f).is_file(), f
    calosc = "\n".join(x.read_text(encoding="utf-8", errors="ignore") for x in mat.rglob("*") if x.is_file() and x.suffix in (".md", ".py", ".json", ".txt", ".csv", ".ini", ".bat"))
    import re
    assert not re.search(r"sk-" + r"ant-[A-Za-z0-9]", calosc), "klucz Anthropic w paczce"
    assert not re.search(r"[\w.]+@gmail\.com", calosc), "prawdziwy adres e-mail w paczce"
    assert "BEGIN PRIVATE KEY" not in calosc


def test_mentor_end_to_end(repo, vibe, srodowisko_kursu, tmp_path):
    """Kurs nie jest wbudowany: uczeń importuje Vibe-coding-kurs.zip (Importuj kurs ZIP…), a Mentor uruchamia weryfikator z zaimportowanej
    paczki tak jak u ucznia: suma SHA-256, izolacja, MENTOR_WORKSPACE."""
    import paczki
    import srodowisko
    zp = shutil.make_archive(str(tmp_path / "Vibe-coding-kurs"), "zip", repo / "programy" / "materialy", "vibe-coding")
    assert paczki.przejrzyj_zip(zp)["manifest"]["course_id"] == "vibe-coding"
    paczki.importuj_zip(zp, nadpisz=True, utworz_prace=False)
    assert program.katalog_materialow("vibe-coding") == program.KATALOG_KURSOW / "vibe-coding" / "paczka"
    sr = srodowisko.Srodowisko("vibe-coding", vibe.get("srodowisko"))
    sr.venv = srodowisko_kursu.venv
    zad = next(z for w in vibe["tygodnie"] for z in w["zadania"] if z["id"] == "v1z4")
    d = C.definicja(zad)
    praca = tmp_path / "PRACA"
    praca.mkdir()
    plik = praca / d["plik"]
    plik.write_text("def koszt_pobytu(noce, osoby, cena_za_osobe_noc=120):\n    return noce * osoby * cena_za_osobe_noc\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_BLAD and "nie przechodzą" in w["opis"], w
    shutil.copy(repo / "programy" / "zrodla" / "vibe_coding" / "wzorce" / "kalkulator_pobytu.py", plik)
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_ZALICZONE, w
    zad = next(z for w in vibe["tygodnie"] for z in w["zadania"] if z["id"] == "v3z3")
    d = C.definicja(zad)
    (praca / "rabaty.py").write_text("def inna():\n    pass\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, praca / "rabaty.py")
    assert w["status"] == C.STATUS_BLAD and "brakuje funkcji" in w["opis"], w
    paczki.usun_kurs("vibe-coding")
