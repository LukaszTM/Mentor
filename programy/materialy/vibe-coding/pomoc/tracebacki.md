# Trzy tracebacki do analizy (zadanie v2z3)

Każdy pochodzi z kodu, który wygenerował model AI dla gospodarstwa „Pod Lipą” (dane fikcyjne).
Dla każdego ustal: typ wyjątku, linię wybuchu, kto wywołał, hipotezę przyczyny, poprawkę i sposób sprawdzenia.

## Traceback 1 — raport obłożenia

```
Traceback (most recent call last):
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\oblozenie.py", line 14, in <module>
    print(procent_oblozenia(rezerwacje, pokoje_wolne))
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\oblozenie.py", line 6, in procent_oblozenia
    return round(zajete / (zajete + wolne) * 100, 1)
ZeroDivisionError: division by zero
```

Fragment kodu: `rezerwacje = []` (filtr „tylko grudzień” nic nie znalazł), `pokoje_wolne = 0`, w funkcji `zajete = len(rezerwacje)`.

## Traceback 2 — wczytanie cennika

```
Traceback (most recent call last):
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\cennik.py", line 11, in <module>
    ceny = wczytaj("dane\\cennik.csv")
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\cennik.py", line 7, in wczytaj
    wynik[wiersz["pokoj"]] = float(wiersz["cena"])
ValueError: could not convert string to float: '150,00'
```

Plik cennik.csv (zapisany z arkusza): `pokoj;cena` / `Lipowy;150,00` / `Dębowy;130,00`.

## Traceback 3 — powitanie gościa

```
Traceback (most recent call last):
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\powitanie_sms.py", line 9, in <module>
    wyslij(tekst_sms(gosc))
  File "C:\Users\Anna\Documents\Mentor\vibe-coding\PRACA\powitanie_sms.py", line 4, in tekst_sms
    return "Dzień dobry, " + g["imie"] + "! Pokój: " + g["pokoj"] + ", noce: " + g["noce"]
TypeError: can only concatenate str (not "int") to str
```

Dane: `gosc = {"imie": "Ola", "pokoj": "Lipowy", "noce": 3}`.

## Wskazówki (przeczytaj dopiero po własnej analizie)

- 1: dzielnik jest zerem, bo i lista, i liczba wolnych pokoi są puste/zerowe — specyfikacja musi powiedzieć, co zwrócić (np. 0.0).
- 2: polski arkusz zapisał przecinek dziesiętny; zamiana `.replace(",", ".")` przed float() — albo lepiej: ustal format pliku w specyfikacji.
- 3: `g["noce"]` to int — f-string: `f"Dzień dobry, {g['imie']}! Pokój: {g['pokoj']}, noce: {g['noce']}"`.
