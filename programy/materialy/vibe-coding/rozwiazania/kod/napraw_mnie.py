# napraw_mnie.py — wersja poprawiona


def srednia_ocen(oceny):
    """Średnia ocen gości (1–5); dla pustej listy 0."""
    if not oceny:
        return 0
    return round(sum(oceny) / len(oceny), 2)


def najlepsza(oceny):
    """Najwyższa ocena; dla pustej listy None."""
    if not oceny:
        return None
    return max(oceny)


def liczba_noclegow(rezerwacje):
    """Suma nocy ze wszystkich rezerwacji (lista słowników z kluczem 'noce')."""
    suma = 0
    for r in rezerwacje:
        suma += r["noce"]
    return suma


if __name__ == "__main__":
    print(srednia_ocen([5, 4, 5]))
    print(najlepsza([3, 5, 4]))
    print(liczba_noclegow([{"noce": 2}, {"noce": 3}]))
