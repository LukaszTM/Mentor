def dodaj(zadania, tytul):
    tytul = tytul.strip()
    if not tytul:
        raise ValueError("tytuł nie może być pusty")
    zadania.append({"tytul": tytul, "zrobione": False})


def oznacz(zadania, nr):
    if not 1 <= nr <= len(zadania):
        raise ValueError(f"nie ma zadania nr {nr}")
    zadania[nr - 1]["zrobione"] = True


def otwarte(zadania):
    return [z["tytul"] for z in zadania if not z["zrobione"]]


lista = []
dodaj(lista, "Zamówić papier")
dodaj(lista, "  Policzyć zeszyty ")
oznacz(lista, 1)
print(otwarte(lista))
for blad in [lambda: dodaj(lista, "   "), lambda: oznacz(lista, 5)]:
    try:
        blad()
    except ValueError as e:
        print("Błąd:", e)
