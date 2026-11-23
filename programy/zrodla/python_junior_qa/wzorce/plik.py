"""Zapis i odczyt listy zadań w JSON."""
import json
from pathlib import Path


def zapisz(lista, sciezka):
    with open(sciezka, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def wczytaj(sciezka):
    if not Path(sciezka).exists():
        return []
    with open(sciezka, encoding="utf-8") as f:
        return json.load(f)
