"""Menedżer zadań — menu w konsoli (logika: zadania.py, zapis: plik.py)."""
import plik
import zadania

PLIK = "zadania.json"


def menu():
    lista = plik.wczytaj(PLIK)
    while True:
        wybor = input("1 dodaj, 2 oznacz, 3 lista, 4 usuń, 0 koniec: ").strip()
        try:
            if wybor == "1":
                zadania.dodaj(lista, input("Tytuł: "))
            elif wybor == "2":
                zadania.oznacz(lista, int(input("Numer: ")))
            elif wybor == "3":
                for nr, z in enumerate(lista, 1):
                    print(f"{nr}. [{'x' if z['zrobione'] else ' '}] {z['tytul']}")
            elif wybor == "4":
                print("Usunięto:", zadania.usun(lista, int(input("Numer: "))))
            elif wybor == "0":
                break
            else:
                print("Nieznana opcja")
        except ValueError as e:
            print("Błąd:", e)
    plik.zapisz(lista, PLIK)


if __name__ == "__main__":
    menu()
