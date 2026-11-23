import json
from pathlib import Path

PLIK = Path(__file__).with_name("wypozyczenia.json")


def wczytaj():
    """Lista wypożyczeń z pliku JSON; brak pliku → pusta lista."""
    if not PLIK.exists():
        return []
    return json.loads(PLIK.read_text(encoding="utf-8"))


def zapisz(wypozyczenia):
    PLIK.write_text(json.dumps(wypozyczenia, ensure_ascii=False, indent=2), encoding="utf-8")
