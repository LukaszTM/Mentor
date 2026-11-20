# -*- coding: utf-8 -*-
"""Sprawdza paczkę kursu: sumy SHA-256 z manifest.json i INTEGRITY.json, poprawność kurs_mentor.json. Uruchom: python testy/sprawdz_kurs.py"""
import hashlib
import json
import sys
from pathlib import Path

K = Path(__file__).resolve().parent.parent
m = json.loads((K / "manifest.json").read_text(encoding="utf-8"))
zle = [p for p, h in m["pliki"].items() if not (K / p).is_file() or hashlib.sha256((K / p).read_bytes()).hexdigest() != h]
integ = json.loads((K / "INTEGRITY.json").read_text(encoding="utf-8"))
zle += [p for p, h in integ.items() if hashlib.sha256((K / p).read_bytes()).hexdigest() != h]
kurs = json.loads((K / "kurs_mentor.json").read_text(encoding="utf-8"))
for w in kurs["tygodnie"]:
    for z in w["zadania"]:
        s = (z.get("cwiczenie") or {}).get("sprawdzenie") or {}
        if s.get("rodzaj") == "test_zewnetrzny" and integ.get(s["plik_testu"]) != s.get("sha256"):
            zle.append(z["id"] + ": suma weryfikatora niezgodna z INTEGRITY.json")
print(f"Plików w manifeście: {len(m['pliki'])}, weryfikatorów: {len(integ)}, lekcji: {len(kurs['lekcje'])}")
print("OK — paczka kompletna" if not zle else "BŁĘDY:\n" + "\n".join(zle))
sys.exit(1 if zle else 0)
