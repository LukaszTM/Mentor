# Testy jako umowa z agentem: pytest od zera
Tydzień 8 · lekcja 25 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** piszesz testy pytest (assert, pytest.raises, parametrize) dla specyfikacji, uruchamiasz je i używasz ich jako umowy: agent dostaje czerwone testy i ma je zazielenić bez ich zmieniania.

**Po co mi to?** Dokumentacja Claude Code nazywa dawanie agentowi sposobu weryfikacji (testów) najskuteczniejszą praktyką. Testy, które piszesz Ty, to Twoja kontrola nad kodem, którego nie piszesz.

## Czego potrzebujesz
- Środowisko kursu (pytest jest zainstalowany przez Mentora).
- Lekcja „Specyfikacja” (przykłady wejście → wynik).

## 1 · Wyjaśnienie od podstaw
### Test w pytest
Plik `test_cennik.py`, funkcje zaczynające się od `test_`, w środku `assert warunek`. pytest sam znajduje takie pliki i funkcje:
```
from cennik import cena_pokoju

def test_lipowy_w_lipcu():
    assert cena_pokoju("Lipowy", 7) == 180
```
Uruchomienie w terminalu Mentora: `python -m pytest -q` (wszystkie testy) albo `python -m pytest -q test_cennik.py -k lipowy` (wybrane). Wynik: kropka = przeszedł, F = nie przeszedł z pokazaniem oczekiwanej i otrzymanej wartości.
### Trzy narzędzia na start
| narzędzie | do czego | przykład |
|---|---|---|
| `assert` | wynik równy oczekiwanemu | `assert oplata_klimatyczna(2, 3) == 15.0` |
| `pytest.raises` | funkcja ma odmówić | `with pytest.raises(ValueError): cena_pokoju("Brzozowy", 7)` |
| `@pytest.mark.parametrize` | ta sama reguła, wiele danych | jedna funkcja testu, tabela 8 przypadków |
Liczby z przecinkiem porównuj z tolerancją: `assert wynik == pytest.approx(629.94)`.
### Testy przed kodem (TDD w wersji vibe)
- Ze specyfikacji piszesz testy (sam albo z agentem w osobnej prośbie: „napisz TYLKO testy do specyfikacji, nie implementuj”).
- Uruchamiasz — czerwone (kodu jeszcze nie ma). To dowód, że test cokolwiek sprawdza.
- Prośba do agenta: „Zaimplementuj tak, żeby przeszły testy test_cennik.py. Nie zmieniaj testów.”
- Zielone → przegląd kodu → commit (kod i testy razem).
### Czy test w ogóle coś łapie? (mutanty)
Test, który przechodzi zawsze, jest bezwartościowy. Sprawdzian: celowo zepsuj kod (zmień `>=` na `>`, usuń `raise`) — dobry test robi się czerwony. Taki zepsuty wariant nazywa się mutantem. Zadanie tygodnia sprawdza Twoje testy właśnie tak: uruchamia je na poprawnym cenniku (muszą przejść) i na trzech mutantach (każdy musi zostać złapany).
### Co testować
- Przykłady ze specyfikacji (szczęśliwa ścieżka).
- Granice (pierwszy i ostatni miesiąc sezonu, 0 dzieci).
- Odmowy (ValueError dla złych danych).
- Jedna rzecz na test, nazwa mówi co: `test_dzieci_nie_placa_oplaty`.
### Testy Mentora a Twoje testy
Testy z WERYFIKATORY to niezależny egzamin — agent ich nie widzi w Twoim projekcie i nie zmieni. Twoje testy (test_*.py w PRACA) są częścią projektu i trafiają do Gita oraz do CI (tydzień 13).

## 2 · Demonstracja — krok po kroku
**Testy łapią mutanta**

```
import pytest


def oplata_klimatyczna(dorosli, noce, dzieci=0):
    if dorosli < 0 or noce < 1 or dzieci < 0:
        raise ValueError("złe dane")
    return round(dorosli * noce * 2.5, 2)


@pytest.mark.parametrize("dorosli, noce, dzieci, oczekiwane", [
    (2, 3, 0, 15.0),
    (1, 1, 0, 2.5),
    (2, 2, 3, 10.0),   # dzieci nie płacą
])
def test_oplata(dorosli, noce, dzieci, oczekiwane):
    assert oplata_klimatyczna(dorosli, noce, dzieci) == oczekiwane


def test_zero_nocy_odmowa():
    with pytest.raises(ValueError):
        oplata_klimatyczna(2, 0)


if __name__ == "__main__":
    print(oplata_klimatyczna(2, 3), oplata_klimatyczna(2, 2, 3))

```

1. Zapisz przykład jako test_oplata.py w PRACA. `python -m pytest -q test_oplata.py` → „4 passed” (3 przypadki parametrize + 1 test odmowy).
2. Mutant 1: zmień `dorosli * noce * 2.5` na `(dorosli + dzieci) * noce * 2.5`. Uruchom: przypadek (2, 2, 3) czerwony — test złapał, że dzieci zaczęły płacić.
3. Mutant 2: usuń `noce < 1 or`. test_zero_nocy_odmowa czerwony — „DID NOT RAISE ValueError”.
4. Mutant 3: zaokrąglanie do 1 miejsca. Testy dalej zielone! Żaden przykład nie ma groszy — to luka w testach. Dopisujesz przypadek (1, 3, 0, 7.5) — wciąż zielono (7.5 ma jedno miejsce). Dopiero stawka 2.35 zł ujawniłaby różnicę — zapisujesz to jako wniosek o doborze danych testowych.
5. Przywróć kod. Wniosek: testy są tak dobre, jak dane, które w nich wymyślisz.

✔ **Oczekiwany wynik:** Dwa mutanty złapane, jeden przeżył — wiesz, jak sprawdzić, czy testy naprawdę czegoś pilnują.

## 3 · Jak to uruchomić
1. Terminal Mentora w PRACA: `python -m pytest -q` albo `python -m pytest -q plik_testu.py -k fragment_nazwy`.
2. Zadanie z paskiem → „✔ Sprawdź wynik”.

## W praktyce
- Każda funkcja w projekcie ma co najmniej jeden test granicy i jeden odmowy.
- Raz na jakiś czas — ręczny mutant.

## 4 · Ćwiczenie prowadzone
Wynik pytest: `..F.F` i na końcu `2 failed, 3 passed`. (1) Ile testów uruchomiono? (2) Który z kolei test (numer) pierwszy nie przeszedł? (3) Test sprawdza `cena_pokoju("Klonowy", 12) == 200`, a funkcja zwraca 150. Co najpewniej jest nie tak w kodzie — miesiąc 12 nie jest traktowany jako sezon wysoki (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/testy_umowa_1.md` · rozwiązanie: `rozwiazania/tydzien_08/testy_umowa_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Napisz w myślach test odmowy: funkcja `cena_pokoju("Brzozowy", 7)` ma rzucić ValueError. Która linia otwiera blok sprawdzający wyjątek? Wpisz ją dokładnie (bez dwukropka też zaliczy). Drugie: mutant zamienia `>=` na `>` w warunku „od 7 nocy rabat”. Jaką liczbę nocy MUSI zawierać test, żeby go złapać? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/testy_umowa_2.md` · rozwiązanie: `rozwiazania/tydzien_08/testy_umowa_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„ModuleNotFoundError: No module named 'cennik'” przy pytest.**
  - Przyczyna: pytest uruchomiony z innego folderu niż plik cennik.py.
  - Jak sprawdzić: `cd` — czy jesteś w PRACA?
  - Poprawka: Uruchamiaj `python -m pytest` w katalogu z plikami (terminal Mentora otwiera się w PRACA).
- ✘ **„collected 0 items”.**
  - Przyczyna: Plik albo funkcje nie zaczynają się od test_.
  - Jak sprawdzić: Nazwy pliku i funkcji.
  - Poprawka: test_cennik.py, def test_…().
- ✘ **assert 0.30000000000000004 == 0.3 nie przechodzi.**
  - Przyczyna: Liczby zmiennoprzecinkowe.
  - Jak sprawdzić: Czy porównujesz float?
  - Poprawka: `== pytest.approx(0.3)` albo zaokrąglenie w kodzie do groszy.

## Pułapki
- Testy napisane przez agenta do kodu napisanego przez agenta często sprawdzają to, co kod robi, a nie to, co powinien. Przykłady w testach bierzesz ze SPECYFIKACJI.
- Zielone testy po zmianie testów to nie sukces — sprawdź diff plików test_*.

## Dodatkowe zadania
1. Napisz test_cennik.py, który łapie 3 mutanty (zadanie tygodnia).
2. Przećwicz własnego mutanta na kalkulator_pobytu.py.
3. Dopisz do AGENTS.md: „testy piszemy ze specyfikacji; nie zmieniaj test_*.py bez pytania”.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co sprawdzać testy mutantami?**
  - Żeby upewnić się, że test wykrywa błąd — test, który zawsze przechodzi, niczego nie pilnuje.
- **Jak testujesz, że funkcja rzuca wyjątek?**
  - with pytest.raises(ValueError): wywołanie.
- **Skąd bierzesz przykłady do testów?**
  - Ze specyfikacji, nie z zachowania istniejącego kodu.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz testy pytest z assert, raises i parametrize, uruchamiasz je, sprawdzasz mutantami i używasz jako umowy z agentem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- pytest — Get started (oficjalna dokumentacja) (dostęp 20.11.2026) — <https://docs.pytest.org/en/stable/getting-started.html>
- pytest — How to write and report assertions (pytest.raises) (dostęp 20.11.2026) — <https://docs.pytest.org/en/stable/how-to/assert.html>
- pytest — Parametrizing tests (dostęp 20.11.2026) — <https://docs.pytest.org/en/stable/how-to/parametrize.html>
- Claude Code — Best practices (test-driven, weryfikacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- pytest znajduje testy w funkcjach, których nazwa zaczyna się od:
  - A) check_
  - B) test_
  - C) spr_
  - D) assert_
- Mutant to:
  - A) Nowa funkcja
  - B) Celowo zepsuty wariant kodu do sprawdzenia testów
  - C) Błąd pytest
  - D) Biblioteka
- Porównanie liczb z przecinkiem w teście:
  - A) ==
  - B) pytest.approx
  - C) is
  - D) str()
- Prośba do agenta przy TDD:
  - A) Napisz kod i testy, jak chcesz
  - B) Zaimplementuj tak, żeby przeszły testy; nie zmieniaj testów
  - C) Usuń testy
  - D) Pomiń czerwone

Odpowiedzi: B, B, B, B
