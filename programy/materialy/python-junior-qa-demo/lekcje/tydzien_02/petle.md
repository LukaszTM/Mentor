# Pętle for i while, range, break i continue
Tydzień 2 · lekcja 9 z 16 · ≈ 45 min

**Po tej lekcji potrafisz:** powtarzasz czynności pętlą for (po liście i range) i while (dopóki warunek), liczysz sumy i liczniki, przerywasz pętlę break i pomijasz obrót continue — bez pętli nieskończonej.

**Po co mi to?** Testy przechodzą po listach danych (dziesiątki kwot, loginów, produktów). Pętla zamienia 50 linii kopiuj-wklej w 3.

## Czego potrzebujesz
- Lekcja „Warunki”.

## 1 · Wyjaśnienie od podstaw
### for — dla każdego elementu
```
for cena in [4.5, 2.3, 7.5]:
    print(cena)
```
Zmienna `cena` przyjmuje po kolei każdą wartość z listy; wcięty blok wykonuje się raz dla każdej. Liczba obrotów jest znana z góry.
### range — liczby po kolei
`range(5)` → 0, 1, 2, 3, 4 (bez 5!). `range(1, 11)` → 1…10. `range(0, 20, 5)` → 0, 5, 10, 15 (krok 5).
### Akumulator i licznik
`suma = 0` przed pętlą, `suma = suma + x` (krócej `suma += x`) w pętli. Licznik: `ile = 0`, `ile += 1` gdy warunek spełniony. Zmienną startową ustawiasz ZAWSZE przed pętlą.
### while — dopóki
`while warunek:` powtarza blok, dopóki warunek jest prawdziwy. Coś w środku musi go w końcu zmienić — inaczej pętla nieskończona (zatrzymasz ją przyciskiem ■ w Mentorze albo Ctrl+C w terminalu).
### break i continue
`break` kończy pętlę natychmiast (np. użytkownik wpisał 0). `continue` pomija resztę bloku i przechodzi do następnego obrotu (np. pomiń produkty z ilością 0).
### Pętla w pętli
Zagnieżdżona pętla wykonuje wewnętrzną w całości dla każdego obrotu zewnętrznej: 10 × 10 = 100 obrotów (tabliczka mnożenia).

## 2 · Demonstracja — krok po kroku
**Suma koszyka, tabliczka i wydawanie z magazynu**

```
ceny = [4.5, 2.3, 0, 7.5, 24.99]
suma = 0
ile_drogich = 0
for cena in ceny:
    if cena == 0:
        continue
    suma += cena
    if cena > 5:
        ile_drogich += 1
print(f"Suma: {suma:.2f}, droższe niż 5 zł: {ile_drogich}")

for n in range(1, 4):
    print(n, "x 7 =", n * 7)

stan = 10
while stan > 0:
    stan -= 4
    print("Zostało:", stan)

```

1. `suma = 0` i `ile_drogich = 0` — akumulator i licznik ustawione PRZED pętlą.
2. `for cena in ceny:` — 5 obrotów, `cena` to kolejno 4.5, 2.3, 0, 7.5, 24.99.
3. `if cena == 0: continue` — pozycja z ceną 0 jest pomijana (nie dodaje się i nie liczy).
4. `suma += cena` — dopisanie do sumy; `if cena > 5: ile_drogich += 1` — 7.5 i 24.99.
5. `for n in range(1, 4)` — n = 1, 2, 3 (4 nie wchodzi).
6. `while stan > 0:` — dopóki jest towar: odejmij 4 i wypisz. 10 → 6 → 2 → -2 i koniec (warunek fałszywy).
7. Zwróć uwagę: stan zszedł do -2 — w prawdziwym magazynie to błąd. W zadaniu z menu sprawdzisz warunek PRZED wydaniem.

✔ **Oczekiwany wynik:** „Suma: 39.29, droższe niż 5 zł: 2”, trzy linie tabliczki 7 i trzy linie „Zostało: 6 / 2 / -2”.

## 3 · Jak to uruchomić
1. Zapisz jako petle.py → ▶ Uruchom.
2. Pętla się nie kończy? Przycisk ■ Zatrzymaj w Mentorze (w terminalu Ctrl+C).

## W praktyce
- Dane testowe trzymasz w liście i przechodzisz pętlą — w tygodniu 7 zrobi to za Ciebie parametrize.
- Każdą pętlę while sprawdź: co ją zakończy?

## 4 · Ćwiczenie prowadzone
Lista ilości w magazynie: [120, 0, 80, 0, 35]. Na wzór demonstracji policz pętlą for: (1) sumę sztuk, (2) ile produktów ma ilość 0, (3) ile obrotów wykona `for i in range(2, 10, 3)`. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/petle_1.md` · rozwiązanie: `rozwiazania/tydzien_02/petle_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Pętla `x = 5` / `while x != 0:` / `    x -= 2` / `    print(x)`. (1) Czy się zakończy? (2) Jak minimalnie poprawić warunek, żeby kończyła się dla każdej dodatniej wartości startowej (wpisz nowy warunek)? (3) Co wypisze poprawiona pętla dla x = 5? Czas: 15 minut.

📄 `cwiczenia/tydzien_02/petle_2.md` · rozwiązanie: `rozwiazania/tydzien_02/petle_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Program „wisi”, brak wyniku**
  - Przyczyna: Pętla while bez zmiany warunku.
  - Jak sprawdzić: Dodaj print(x) w pętli — czy x się zmienia?
  - Poprawka: Zmieniaj zmienną warunku w środku pętli albo użyj break.
- ✘ **Suma za duża przy drugim uruchomieniu funkcji**
  - Przyczyna: Akumulator ustawiony poza funkcją/pętlą raz na zawsze.
  - Jak sprawdzić: Gdzie jest `suma = 0`?
  - Poprawka: Zeruj akumulator tuż przed pętlą, w tym samym bloku.
- ✘ **Brakuje ostatniej liczby (np. 10 w tabliczce)**
  - Przyczyna: range(1, 10) kończy się na 9.
  - Jak sprawdzić: Wypisz list(range(1, 10)).
  - Poprawka: range(1, 11).

## Pułapki
- Zmiana listy w trakcie pętli po niej (usuwanie elementów) — pomija elementy; twórz nową listę.
- while True bez break = pętla nieskończona.

## Dodatkowe zadania
1. Tabliczka mnożenia 1–10 pętlą zagnieżdżoną.
2. Suma i średnia cen z listy (pomiń zera continue).
3. Pętla while pytająca o liczby do wpisania 0 (break).

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Kiedy for, a kiedy while?**
  - for — znana kolekcja/liczba obrotów; while — dopóki warunek (np. do wpisania 0).
- **Co robi continue?**
  - Pomija resztę bloku i przechodzi do następnego obrotu.
- **Ile liczb daje range(3, 8)?**
  - 5: 3, 4, 5, 6, 7.

## Co potrafię teraz bez patrzenia na przykład?
Używasz for z listą i range, while z warunkiem, akumulatorów i liczników oraz break/continue; rozpoznajesz i naprawiasz pętlę nieskończoną.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Więcej narzędzi kontroli przepływu (if, for, range, funkcje) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/controlflow.html>
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- list(range(4)) to:
  - A) [1, 2, 3, 4]
  - B) [0, 1, 2, 3]
  - C) [0, 1, 2, 3, 4]
  - D) [4]
- break w pętli:
  - A) pomija obrót
  - B) kończy pętlę
  - C) restartuje pętlę
  - D) nic nie robi
- Gdzie ustawiasz suma = 0?
  - A) w pętli
  - B) przed pętlą
  - C) po pętli
  - D) nigdzie
- Zagnieżdżone pętle 3 × 4 wykonają wewnętrzny blok:
  - A) 7 razy
  - B) 12 razy
  - C) 3 razy
  - D) 4 razy

Odpowiedzi: B, B, B, B
