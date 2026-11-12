# -*- coding: utf-8 -*-
"""Sprawdza paczkę kursu bez Mentora: plik JSON, strukturę mentor-program/1, obecność plików ćwiczeń/rozwiązań
i sumy kontrolne z manifest.json. Uruchom: python testy/sprawdz_kurs.py (z katalogu paczki) — kod wyjścia 0 = OK."""
import hashlib
import json
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent.parent
bledy = []
js = TU / "kurs_mentor.json"
if not js.exists():
    js = TU.parent.parent / "kadry-i-place.json"
if not js.exists():
    print("BRAK pliku kursu (kurs_mentor.json)"); sys.exit(1)
d = json.loads(js.read_text(encoding="utf-8"))
for k in ("nazwa", "etapy", "tygodnie", "lekcje"):
    if k not in d:
        bledy.append(f"brak pola {k}")
ids = {l["id"] for l in d.get("lekcje", [])}
for w in d.get("tygodnie", []):
    for lid in w.get("lekcje", []):
        if lid not in ids:
            bledy.append(f"tydzień {w.get('tydzien')}: lekcja {lid} nie istnieje")
    for z in w.get("zadania", []):
        for k in ("id", "tytul", "opis", "kroki", "sprawdz", "problemy", "pliki", "xp", "czas_min"):
            if k not in z:
                bledy.append(f"zadanie {z.get('id')}: brak {k}")
for l in d.get("lekcje", []):
    for k in ("id", "tydzien", "nazwa", "slowa", "wyjasnienie", "przyklad", "zadania", "pytania", "pulapki", "test", "cwiczenia", "demonstracja", "typowe_bledy", "podsumowanie"):
        if k not in l:
            bledy.append(f"lekcja {l.get('id')}: brak {k}")
    for q in l.get("test", []):
        if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
            bledy.append(f"lekcja {l.get('id')}: zły odp w teście")
    for cw in l.get("cwiczenia", []):
        for k in ("plik", "rozwiazanie_plik"):
            if cw.get(k) and not (TU / cw[k]).exists():
                bledy.append(f"brak pliku {cw[k]}")
for t, qs in d.get("quizy", {}).items():
    for q in qs:
        if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
            bledy.append(f"quiz {t}: zły odp")
        if q.get("lekcja") and q["lekcja"] not in ids:
            bledy.append(f"quiz {t}: lekcja {q['lekcja']} nie istnieje")
man = TU / "manifest.json"
if man.exists():
    m = json.loads(man.read_text(encoding="utf-8"))
    for sc, h in m.get("pliki", {}).items():
        p = TU / sc
        if not p.exists():
            bledy.append(f"manifest: brak {sc}")
        elif hashlib.sha256(p.read_bytes()).hexdigest() != h:
            bledy.append(f"manifest: zmieniony {sc}")
else:
    bledy.append("brak manifest.json")
print(f"Kurs: {d.get('nazwa')} v{d.get('wersja')} — tygodni {len(d.get('tygodnie', []))}, lekcji {len(d.get('lekcje', []))}, zadań {sum(len(w.get('zadania', [])) for w in d.get('tygodnie', []))}")
if bledy:
    print("DO POPRAWY:"); [print(" -", b) for b in bledy]; sys.exit(1)
print("OK — paczka kompletna, JSON poprawny, sumy kontrolne zgodne.")
