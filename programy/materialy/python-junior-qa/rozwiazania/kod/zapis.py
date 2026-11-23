from pathlib import Path


def zapisz_liste(lista, sciezka):
    """Zapisuje każdy element listy w osobnej linii (utf-8)."""
    with open(sciezka, "w", encoding="utf-8") as f:
        for element in lista:
            f.write(f"{element}\n")


def dopisz(sciezka, element):
    """Dopisuje jeden element na końcu pliku."""
    with open(sciezka, "a", encoding="utf-8") as f:
        f.write(f"{element}\n")


def wczytaj_liste(sciezka):
    """Lista niepustych linii bez spacji na brzegach; brak pliku → []."""
    if not Path(sciezka).exists():
        return []
    with open(sciezka, encoding="utf-8") as f:
        return [linia.strip() for linia in f if linia.strip()]


if __name__ == "__main__":
    zapisz_liste(["Zeszyt A5", "Długopis niebieski", "Gumka"], "produkty.txt")
    dopisz("produkty.txt", "Klej w sztyfcie")
    for nr, p in enumerate(wczytaj_liste("produkty.txt"), 1):
        print(nr, p)
