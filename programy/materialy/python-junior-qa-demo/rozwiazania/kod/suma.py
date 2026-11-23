liczby = []
while True:
    x = float(input("Liczba (0 = koniec): ").replace(",", "."))
    if x == 0:
        break
    liczby.append(x)

if not liczby:
    print("Nie podano żadnej liczby")
else:
    print("suma:", sum(liczby))
    print("średnia:", sum(liczby) / len(liczby))
    print("max:", max(liczby))
