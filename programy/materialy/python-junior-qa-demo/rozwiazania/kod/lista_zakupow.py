lista = []

while True:
    wybor = input("1 dodaj, 2 usuń, 3 wypisz, 0 koniec: ").strip()
    if wybor == "1":
        lista.append(input("Produkt: ").strip())
    elif wybor == "2":
        produkt = input("Który usunąć: ").strip()
        if produkt in lista:
            lista.remove(produkt)
        else:
            print("Nie ma takiego produktu na liście")
    elif wybor == "3":
        if not lista:
            print("Lista jest pusta")
        for nr, produkt in enumerate(lista, 1):
            print(f"{nr}. {produkt}")
    elif wybor == "0":
        break
    else:
        print("Nieznana opcja")
