"""Lista gości gospodarstwa „Pod Lipą”."""


def odmiana_nocy(n):
    if n == 1:
        return "noc"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return "noce"
    return "nocy"


def dodaj_goscia(lista, imie, noce):
    imie = (imie or "").strip()
    if not imie:
        raise ValueError("imię nie może być puste")
    if noce < 1:
        raise ValueError("noce muszą być co najmniej 1")
    lista.append({"imie": imie, "noce": noce})
    return lista


def liczba_gosci(lista):
    return len(lista)


def raport(lista):
    if not lista:
        return "Brak gości"
    return "\n".join(f"{g['imie']}: {g['noce']} {odmiana_nocy(g['noce'])}" for g in lista)


if __name__ == "__main__":
    goscie = []
    dodaj_goscia(goscie, "Anna", 2)
    dodaj_goscia(goscie, "Piotr", 5)
    print(raport(goscie))
