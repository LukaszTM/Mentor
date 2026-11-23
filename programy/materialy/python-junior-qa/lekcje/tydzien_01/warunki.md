# Instrukcje warunkowe if / elif / else
Tydzień 1 · lekcja 8 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** piszesz decyzje if/elif/else z porównaniami (== != < <= > >=) i łączysz warunki and/or/not, dbając o wcięcia i kolejność progów.

**Po co mi to?** Reguły biznesowe (rabaty, progi, walidacja) to warunki — a tester sprawdza właśnie ich granice: co dla 99 zł, 100 zł i 100,01 zł?

## Czego potrzebujesz
- Lekcje „Zmienne” i „print i input”.

## 1 · Wyjaśnienie od podstaw
### if — jeśli
```
if razem >= 100:
    print("Darmowa dostawa")
```
Dwukropek kończy warunek, a wcięcie (4 spacje) pokazuje, co należy do if. Bez wcięcia: IndentationError.
### Porównania
`==` równe, `!=` różne, `<` `<=` `>` `>=`. Wynik porównania to bool: `5 > 3` → True. Napisy porównujesz dokładnie: `"Tak" == "tak"` → False (użyj `.lower()`).
### elif i else
`elif` = „w przeciwnym razie, jeśli…”, `else` = „we wszystkich pozostałych przypadkach”. Python sprawdza warunki **od góry** i wykonuje **tylko pierwszy prawdziwy**. Dlatego progi układasz od największego:
```
if razem >= 300:
    rabat = 10
elif razem >= 100:
    rabat = 5
else:
    rabat = 0
```
Gdybyś zaczął od `>= 100`, kwota 350 dostałaby 5% — klasyczny błąd kolejności.
### and, or, not
`and` — oba warunki prawdziwe; `or` — co najmniej jeden; `not` — odwrócenie. `if ilosc > 0 and ilosc <= 50:` można zapisać krócej `if 0 < ilosc <= 50:`.
### Wartości brzegowe
Dla reguły „od 100 zł darmowa dostawa” testujesz 99.99, 100 i 100.01. To technika z sylabusa ISTQB (analiza wartości brzegowych) — wrócisz do niej w tygodniu 7.

## 2 · Demonstracja — krok po kroku
**Koszt dostawy w sklepie — trzy progi i ich granice**

```
def koszt_dostawy(razem):
    if razem >= 100:
        return 0
    elif razem >= 50:
        return 9.99
    else:
        return 14.99


for kwota in [49.99, 50, 99.99, 100, 250]:
    print(kwota, "->", koszt_dostawy(kwota))

```

1. `def koszt_dostawy(razem):` — zamknięcie reguły w funkcji (funkcje poznasz w tygodniu 3; tu: „przepis z nazwą, który dostaje kwotę i zwraca koszt”).
2. `if razem >= 100: return 0` — najwyższy próg pierwszy; `return` oddaje wynik i kończy funkcję.
3. `elif razem >= 50: return 9.99` — sprawdzany tylko, gdy pierwszy warunek był fałszywy, czyli dla kwot poniżej 100.
4. `else: return 14.99` — wszystko poniżej 50.
5. Pętla `for kwota in [...]` sprawdza 5 kwot — w tym granice 50 i 100 oraz wartości tuż pod nimi (49.99, 99.99).
6. Zamień kolejność warunków (najpierw `>= 50`) i uruchom — 100 i 250 dostaną 9.99. Tak wygląda błąd, który łapie test wartości brzegowych.

✔ **Oczekiwany wynik:** 49.99 → 14.99, 50 → 9.99, 99.99 → 9.99, 100 → 0, 250 → 0.

## 3 · Jak to uruchomić
1. Zapisz jako dostawa.py → ▶ Uruchom.
2. Eksperyment: zmień kolejność warunków, uruchom, porównaj wynik i przywróć poprawną wersję.

## W praktyce
- Każdy próg w wymaganiach = co najmniej 2 przypadki testowe (pod i na granicy).
- W bug raporcie podajesz dokładną kwotę, dla której reguła działa źle.

## 4 · Ćwiczenie prowadzone
Reguła rabatu: od 300 zł — 10%, od 100 zł — 5%, poniżej — 0%. Jaki rabat (w %) dostaną kwoty: (1) 99.99, (2) 100, (3) 299.99, (4) 300? Czas: 10 minut.

📄 `cwiczenia/tydzien_01/warunki_1.md` · rozwiązanie: `rozwiazania/tydzien_01/warunki_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kolega napisał: `if razem >= 100: rabat = 5` / `elif razem >= 300: rabat = 10` / `else: rabat = 0`. (1) Jaki rabat dostanie 500 zł? (2) Czy kiedykolwiek ktoś dostanie 10%? (3) Ile minimum przypadków testowych (kwot) sprawdza granice obu progów, jeśli dla każdej granicy bierzesz wartość tuż pod i dokładnie na granicy? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/warunki_2.md` · rozwiązanie: `rozwiazania/tydzien_01/warunki_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **IndentationError: expected an indented block after 'if' statement**
  - Przyczyna: Brak wcięcia po dwukropku.
  - Jak sprawdzić: Linia po if musi zaczynać się 4 spacjami.
  - Poprawka: Wcięcie 4 spacje (Tab w edytorze Mentora wstawia 4 spacje).
- ✘ **SyntaxError: invalid syntax przy `if x = 5:`**
  - Przyczyna: Przypisanie = zamiast porównania ==.
  - Jak sprawdzić: Szukaj pojedynczego = w warunku.
  - Poprawka: `if x == 5:`.
- ✘ **Zła kategoria dla dużych kwot (bez komunikatu błędu)**
  - Przyczyna: Progi w złej kolejności.
  - Jak sprawdzić: Przetestuj wartości brzegowe każdego progu.
  - Poprawka: Ułóż warunki od największego progu.

## Pułapki
- Porównywanie float z == (0.1 + 0.2 == 0.3 → False) — dla kwot używaj progów >= lub zaokrąglenia.
- else łapie WSZYSTKO, także wartości ujemne — sprawdzaj dane wejściowe osobnym if.

## Dodatkowe zadania
1. Napisz regułę rabatu z 3 progami i sprawdź 4 wartości brzegowe.
2. Program pyta „Czy masz kartę stałego klienta? (tak/nie)” i działa dla „TAK”, „ tak ”.
3. Zapisz w notatki.md, dlaczego kolejność elif ma znaczenie.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Ile gałęzi if/elif/else się wykona?**
  - Dokładnie jedna — pierwsza z prawdziwym warunkiem (albo else).
- **Dlaczego progi układa się od największego?**
  - Bo większa kwota spełnia też niższe progi — wygrałby niższy.
- **Jakie wartości testujesz dla „od 100 zł”?**
  - 99.99, 100, 100.01 — wartości brzegowe.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz decyzje if/elif/else, łączysz warunki and/or/not, pilnujesz wcięć i kolejności progów oraz testujesz wartości brzegowe.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Więcej narzędzi kontroli przepływu (if, for, range, funkcje) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/controlflow.html>
- SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe) (dostęp 23.11.2026) — <https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad>
- ISTQB Glossary — słownik terminów testowania (dostępny w języku polskim) (dostęp 23.11.2026) — <https://glossary.istqb.org/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co wypisze: x = 100; if x > 100: print("A") elif x >= 100: print("B") else: print("C")
  - A) A
  - B) B
  - C) C
  - D) A i B
- Operator „różne od”:
  - A) <>
  - B) !=
  - C) =!
  - D) not=
- True and False daje:
  - A) True
  - B) False
  - C) None
  - D) błąd
- Granice reguły „od 50 zł” do testu:
  - A) 0 i 1000
  - B) 49.99 i 50
  - C) tylko 50
  - D) 100

Odpowiedzi: B, B, B, B
