"""Logika menedżera zadań — bez input() i print()."""


def dodaj(zadania, tytul):
    tytul = tytul.strip()
    if not tytul:
        raise ValueError("tytuł nie może być pusty")
    zadania.append({"tytul": tytul, "zrobione": False})


def _sprawdz(zadania, nr):
    if not 1 <= nr <= len(zadania):
        raise ValueError(f"nie ma zadania nr {nr}")


def oznacz(zadania, nr):
    _sprawdz(zadania, nr)
    zadania[nr - 1]["zrobione"] = True


def usun(zadania, nr):
    _sprawdz(zadania, nr)
    return zadania.pop(nr - 1)["tytul"]


def otwarte(zadania):
    return [z["tytul"] for z in zadania if not z["zrobione"]]
