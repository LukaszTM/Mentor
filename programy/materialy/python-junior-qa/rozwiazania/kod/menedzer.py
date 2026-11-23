def dodaj(zadania, tytul):
    """Dodaje zadanie; pusty tytuł → ValueError."""
    tytul = tytul.strip()
    if not tytul:
        raise ValueError("tytuł nie może być pusty")
    zadania.append({"tytul": tytul, "zrobione": False})


def _sprawdz(zadania, nr):
    if not 1 <= nr <= len(zadania):
        raise ValueError(f"nie ma zadania nr {nr}")


def oznacz(zadania, nr):
    """Oznacza zadanie nr (od 1) jako zrobione."""
    _sprawdz(zadania, nr)
    zadania[nr - 1]["zrobione"] = True


def usun(zadania, nr):
    """Usuwa zadanie nr (od 1) i zwraca jego tytuł."""
    _sprawdz(zadania, nr)
    return zadania.pop(nr - 1)["tytul"]


def otwarte(zadania):
    """Tytuły niezrobionych zadań."""
    return [z["tytul"] for z in zadania if not z["zrobione"]]


if __name__ == "__main__":
    lista = []
    while True:
        wybor = input("1 dodaj, 2 oznacz, 3 lista, 4 usuń, 0 koniec: ").strip()
        try:
            if wybor == "1":
                dodaj(lista, input("Tytuł: "))
            elif wybor == "2":
                oznacz(lista, int(input("Numer: ")))
            elif wybor == "3":
                for nr, z in enumerate(lista, 1):
                    print(f"{nr}. [{'x' if z['zrobione'] else ' '}] {z['tytul']}")
            elif wybor == "4":
                print("Usunięto:", usun(lista, int(input("Numer: "))))
            elif wybor == "0":
                break
            else:
                print("Nieznana opcja")
        except ValueError as e:
            print("Błąd:", e)
