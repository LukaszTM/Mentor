a = float(input("Pierwsza liczba: "))
dzialanie = input("Działanie (+ - * /): ").strip()
b = float(input("Druga liczba: "))

if dzialanie == "+":
    print("Wynik:", a + b)
elif dzialanie == "-":
    print("Wynik:", a - b)
elif dzialanie == "*":
    print("Wynik:", a * b)
elif dzialanie == "/":
    if b == 0:
        print("Nie można dzielić przez zero")
    else:
        print("Wynik:", a / b)
else:
    print("Nieznane działanie:", dzialanie)
