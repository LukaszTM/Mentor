# Ćwiczenie 1 (prowadzone) — Czytanie kodu 2: listy, pętle, słowniki i funkcje
Tydzień 2 · lekcja `czytanie_kodu_2`

## Zadanie
Co zwróci funkcja i co wypisze program?

def policz_dorosłych(goscie):
    n = 0
    for g in goscie:
        if g["wiek"] >= 18:
            n += 1
    return n

lista = [{"imie": "Ola", "wiek": 34}, {"imie": "Kuba", "wiek": 12}, {"imie": "Ewa", "wiek": 18}]
print(policz_dorosłych(lista))
print(lista[1]["imie"])
print(len(lista))

Wpisz trzy linie wyniku. Czas: 20 minut.

## Jak sprawdzić
1. Zrób ćwiczenie (w Mentorze: Lekcje → ta lekcja → pola „Twoje odpowiedzi”; kod uruchamiasz w pliku .py w PRACA).
2. Utknąłeś? Podpowiedzi po kolei w Mentorze albo w pliku rozwiązania — najpierw podpowiedź 1.
3. Po własnej próbie: `rozwiazania/tydzien_02/czytanie_kodu_2_1.md`.

## Twoja odpowiedź

(pisz tutaj)
