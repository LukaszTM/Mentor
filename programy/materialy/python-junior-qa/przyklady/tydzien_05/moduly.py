import json
import tempfile
from pathlib import Path

katalog = Path(tempfile.mkdtemp())
(katalog / "zadania.py").write_text(
    "def dodaj(lista, tytul):\n"
    "    lista.append({'tytul': tytul.strip(), 'zrobione': False})\n", encoding="utf-8")
(katalog / "plik.py").write_text(
    "import json\n"
    "def zapisz(lista, sciezka):\n"
    "    with open(sciezka, 'w', encoding='utf-8') as f:\n"
    "        json.dump(lista, f, ensure_ascii=False)\n"
    "def wczytaj(sciezka):\n"
    "    with open(sciezka, encoding='utf-8') as f:\n"
    "        return json.load(f)\n", encoding="utf-8")

import sys
sys.path.insert(0, str(katalog))
import zadania
from plik import zapisz, wczytaj

lista = []
zadania.dodaj(lista, " Zamówić zszywki ")
zapisz(lista, katalog / "zadania.json")
print(wczytaj(katalog / "zadania.json"))
print(sorted(p.name for p in katalog.iterdir() if p.suffix in (".py", ".json")))
