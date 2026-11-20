"""Porządkowanie plików według rozszerzeń — tryb próby, bez nadpisywania i usuwania."""
import shutil
import sys
from datetime import datetime
from pathlib import Path

REGULY = {".jpg": "zdjecia", ".jpeg": "zdjecia", ".png": "zdjecia", ".heic": "zdjecia", ".pdf": "dokumenty", ".doc": "dokumenty",
          ".docx": "dokumenty", ".csv": "dane", ".xlsx": "dane", ".xls": "dane"}


def _wolna_nazwa(folder, nazwa, zajete):
    p = Path(nazwa)
    kandydat, i = nazwa, 0
    while (folder / kandydat).exists() or (folder.name, kandydat) in zajete:
        i += 1
        kandydat = f"{p.stem}_{i}{p.suffix}"
    return kandydat


def uporzadkuj(katalog, wykonaj=False):
    """Lista (plik, 'folder/nazwa'); z wykonaj=True przenosi i dopisuje log .porzadki.log."""
    kat = Path(katalog)
    plan, zajete = [], set()
    for p in sorted((x for x in kat.iterdir() if x.is_file() and not x.name.startswith(".")), key=lambda x: x.name):
        folder = REGULY.get(p.suffix.lower(), "inne")
        nowa = _wolna_nazwa(kat / folder, p.name, zajete)
        zajete.add((folder, nowa))
        plan.append((p.name, f"{folder}/{nowa}"))
    if wykonaj:
        with open(kat / ".porzadki.log", "a", encoding="utf-8") as log:
            for nazwa, cel in plan:
                (kat / cel).parent.mkdir(exist_ok=True)
                shutil.move(str(kat / nazwa), str(kat / cel))
                log.write(f"{datetime.now():%Y-%m-%d %H:%M} {nazwa} -> {cel}\n")
    return plan


if __name__ == "__main__":
    for a, b in uporzadkuj(sys.argv[1], wykonaj="--wykonaj" in sys.argv):
        print(a, "->", b)
