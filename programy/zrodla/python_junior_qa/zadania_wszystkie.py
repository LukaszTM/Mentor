# -*- coding: utf-8 -*-
"""Wszystkie tygodnie, zadania i quizy kursu w jednym miejscu (kolejność tygodni = kolejność w Mentorze)."""
import importlib

TYGODNIE, QUIZY = [], {}
for nazwa in ("zadania0", "zadania1", "zadania2", "zadania3"):
    try:
        m = importlib.import_module(nazwa)
    except ModuleNotFoundError as e:
        if e.name != nazwa:
            raise
        continue
    TYGODNIE += getattr(m, f"TYGODNIE_{nazwa[-1]}")
    QUIZY.update({str(k): v for k, v in getattr(m, f"QUIZY_{nazwa[-1]}").items()})
ZADANIA = [z for w in TYGODNIE for z in w["zadania"]]
