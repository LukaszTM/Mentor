# -*- coding: utf-8 -*-
"""Kontrola paczek wydania (CI i ręcznie): python programy/zrodla/sprawdz_paczki.py Mentor-windows.zip Python-junior-qa-kurs.zip Kadry-i-place-kurs.zip Vibe-coding-kurs.zip

- Mentor-windows.zip: bez żadnego kursu (plików kursów, materiałów, kurs_mentor.json).
- paczka kursu: ma mentor-manifest.json, importuje się przez „Importuj kurs ZIP…” (paczki.importuj_zip) do pustego katalogu danych,
  Mentor znajduje materiały w kursy/<id>/paczka, a weryfikatory zadań mają sumy SHA-256 zgodne z kursem; sprawdz_kurs.py z paczki przechodzi.
Kod wyjścia 0 = OK."""

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NIE_W_MENTORZE = ("python-junior-qa.json", "python-junior-qa-demo.json", "kadry-i-place.json", "vibe-coding.json", "kurs_mentor.json", "materialy/", "START_TUTAJ.md", "WERYFIKATORY/")


def sprawdz_mentora(zp):
    with zipfile.ZipFile(zp) as z:
        nazwy = [n.replace("\\", "/") for n in z.namelist()]
    bledy = [f"{zp.name}: kurs wbudowany w paczkę Mentora — {n}" for n in nazwy if any(x in n for x in NIE_W_MENTORZE)]
    if not any(n.endswith("Mentor.exe") for n in nazwy):
        bledy.append(f"{zp.name}: brak Mentor.exe")
    return bledy


def sprawdz_kurs(zp, paczki, program):
    bledy = []
    pg = paczki.przejrzyj_zip(zp)
    if not pg["manifest"]:
        bledy.append(f"{zp.name}: brak mentor-manifest.json")
    w = paczki.importuj_zip(zp, nadpisz=True, utworz_prace=False)
    kid = w["id"]
    mat = program.katalog_materialow(kid)
    if mat != program.KATALOG_KURSOW / kid / "paczka":
        bledy.append(f"{zp.name}: materiały nie z paczki ({mat})")
        return bledy
    if kid not in {json.loads(p.read_text(encoding="utf-8")).get("id") for p, *_ in program.lista_programow()}:
        bledy.append(f"{zp.name}: kurs {kid} nie pojawił się na liście programów")
    kurs = json.loads((program.KATALOG_KURSOW / kid / "kurs.json").read_text(encoding="utf-8"))
    n = 0
    for t in kurs["tygodnie"]:
        for z in t["zadania"]:
            s = (z.get("cwiczenie") or {}).get("sprawdzenie") or {}
            if s.get("rodzaj") == "test_zewnetrzny":
                f = mat / s["plik_testu"]
                if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != s["sha256"]:
                    bledy.append(f"{zp.name}: {z['id']} — weryfikator {s['plik_testu']} brak albo zła suma")
                n += 1
    p = subprocess.run([sys.executable, str(mat / "testy" / "sprawdz_kurs.py")], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        bledy.append(f"{zp.name}: sprawdz_kurs.py: {(p.stdout + p.stderr)[-800:]}")
    print(f"{zp.name}: {kid} {w['wersja']} — import OK, materiały w kursy/{kid}/paczka, weryfikatory zadań: {n}")
    return bledy


def main(argv):
    tmp = Path(tempfile.mkdtemp(prefix="mentor-paczki-"))
    os.environ["MENTOR_DANE"] = str(tmp / "dane")
    os.environ["MENTOR_PRACA"] = str(tmp / "praca")
    sys.path.insert(0, str(REPO))
    import paczki
    import program
    bledy = []
    for a in argv:
        zp = Path(a)
        if zp.name.startswith("Mentor"):
            bledy += sprawdz_mentora(zp)
            print(f"{zp.name}: bez wbudowanych kursów" if not bledy else "")
        else:
            bledy += sprawdz_kurs(zp, paczki, program)
    for b in bledy:
        print("BŁĄD:", b)
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
