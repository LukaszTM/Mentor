# -*- coding: utf-8 -*-
"""Wszystkie zadania i tygodnie kursu w jednym miejscu (dla zbuduj.py i kontroli weryfikatorów)."""
from zadania0 import QUIZY_0, TYGODNIE_0
from zadania1 import QUIZY_1, TYGODNIE_1
from zadania2 import QUIZY_2, TYGODNIE_2
from zadania3 import QUIZY_3, TYGODNIE_3

TYGODNIE = TYGODNIE_0 + TYGODNIE_1 + TYGODNIE_2 + TYGODNIE_3
QUIZY = {**QUIZY_0, **QUIZY_1, **QUIZY_2, **QUIZY_3}
from powtorki import powtorka  # noqa: E402

for _w in TYGODNIE:
    if _w["tydzien"] < 15 and not any(z["id"].endswith("z9") for z in _w["zadania"]):
        _w["zadania"].append(powtorka(_w["tydzien"], _w["lekcje"]))

ZADANIA = [z for t in TYGODNIE for z in t["zadania"]]
