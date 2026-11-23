"""Moduł magazynu z paczki kursu (tydzień 7) — wersja poprawiona po znalezieniu błędu testem."""


def przyjmij(stan, n):
    """Nowy stan po przyjęciu n sztuk; n ≤ 0 → ValueError."""
    if n <= 0:
        raise ValueError("ilość musi być dodatnia")
    return stan + n


def wydaj(stan, n):
    """Nowy stan po wydaniu n sztuk; n ≤ 0 albo więcej niż stan → ValueError."""
    if n <= 0 or n > stan:
        raise ValueError(f"nie można wydać {n} szt. (stan: {stan})")
    return stan - n


def wartosc(stan, cena):
    """Wartość towaru na stanie."""
    return round(stan * cena, 2)
