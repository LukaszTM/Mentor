import random


def ocen(strzal, sekret):
    """Zwraca „za mało”, „za dużo” albo „trafione”."""
    if strzal < sekret:
        return "za mało"
    if strzal > sekret:
        return "za dużo"
    return "trafione"


def gra(sekret):
    proby = 0
    while True:
        try:
            strzal = int(input("Twoja liczba (1–100): "))
        except ValueError:
            print("To nie liczba całkowita")
            continue
        proby += 1
        wynik = ocen(strzal, sekret)
        print(wynik)
        if wynik == "trafione":
            return proby


if __name__ == "__main__":
    wyniki = []
    proby = gra(random.randint(1, 100))
    wyniki.append(proby)
    print(f"Brawo! Liczba prób: {proby}. Najlepszy wynik: {min(wyniki)}")
