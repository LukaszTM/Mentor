# pytest: test_, assert, uruchamianie, pytest.raises i pytest.approx
Tydzień 7 · lekcja 28 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** piszesz testy jednostkowe w pytest (pliki test_*.py, funkcje test_*, assert), czytasz wynik pytest -v, testujesz wyjątki pytest.raises i liczby zmiennoprzecinkowe pytest.approx oraz układasz test według schematu Arrange–Act–Assert.

**Po co mi to?** pytest to standard testów w Pythonie. Rekruter zapyta „jak sprawdzisz, że funkcja działa?” — odpowiedzią jest test, który przechodzi na dobrym kodzie i pada na złym.

## Czego potrzebujesz
- Lekcje „Funkcje”, „Obsługa błędów” i „Podstawy testowania”.
- pytest jest w środowisku kursu (pytest 9.2).

## 1 · Wyjaśnienie od podstaw
### Pierwszy test
```
# test_ceny.py
from ceny import brutto

def test_brutto_vat_23():
    assert brutto(10) == 12.3
```
pytest sam znajduje pliki `test_*.py` i funkcje `test_*`. `assert warunek` — jeśli warunek jest fałszywy, test pada (FAILED), a pytest pokazuje obie wartości.
### Uruchamianie
Terminal Mentora w katalogu z plikami: `python -m pytest -v` (verbose — każdy test osobno), `-q` krótko, `-k brutto` tylko testy z „brutto” w nazwie, `-x` stop na pierwszym błędzie. W Mentorze zadania z testami sprawdza „✔ Sprawdź wynik”.
### Schemat AAA
**Arrange** — przygotuj dane, **Act** — wywołaj funkcję, **Assert** — sprawdź wynik. Jeden test = jedno zachowanie; nazwa mówi, co sprawdza: `test_dostawa_darmowa_od_100`.
### Wyjątki: pytest.raises
```
import pytest

def test_wydaj_wiecej_niz_stan():
    with pytest.raises(ValueError):
        wydaj(10, 20)
```
Test przechodzi tylko wtedy, gdy blok RZUCI ValueError. `pytest.raises(ValueError, match="brak towaru")` sprawdza też treść komunikatu.
### Liczby zmiennoprzecinkowe: pytest.approx
`assert 0.1 + 0.2 == pytest.approx(0.3)` — porównanie z tolerancją. Kwoty po round() porównujesz zwykle, wyniki obliczeń — approx.
### Dobry test łapie błąd
Test, który przechodzi zawsze, jest bezwartościowy. Sprawdzian: celowo zepsuj funkcję (`>=` na `>`) — test musi paść. Taką zepsutą wersję nazywa się **mutantem**; weryfikatory Mentora uruchamiają Twoje testy na mutantach i zaliczają tylko testy, które je „zabijają”.
### Wynik pytest
`test_ceny.py::test_brutto_vat_23 PASSED`; przy FAILED pytest pokazuje linię assert z wartościami: `assert 12.299999 == 12.3`. Na dole podsumowanie: `3 passed, 1 failed in 0.05s`.

## 2 · Demonstracja — krok po kroku
**Pięć testów reguły dostawy**

```
# test_magazyn_demo.py — uruchom: python -m pytest -v test_magazyn_demo.py
import pytest


def koszt_dostawy(razem):
    if razem < 0:
        raise ValueError("kwota nie może być ujemna")
    if razem >= 100:
        return 0
    return 9.99 if razem >= 50 else 14.99


def test_dostawa_darmowa_od_100():
    assert koszt_dostawy(100) == 0


def test_dostawa_tuz_ponizej_progu():
    assert koszt_dostawy(99.99) == 9.99


def test_dostawa_mala_kwota():
    wynik = koszt_dostawy(49.99)
    assert wynik == 14.99


def test_ujemna_kwota_to_blad():
    with pytest.raises(ValueError, match="ujemna"):
        koszt_dostawy(-1)


def test_suma_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)

```

1. Plik nazywa się `test_….py`, funkcje `test_…` — tylko takie pytest uruchamia. (W prawdziwym projekcie funkcja jest w osobnym module i importujesz ją: `from dostawa import koszt_dostawy`.)
2. `test_dostawa_darmowa_od_100` — granica progu; `test_dostawa_tuz_ponizej_progu` — sąsiad granicy.
3. `test_dostawa_mala_kwota` — AAA rozpisane: Act (wywołanie do zmiennej) i Assert.
4. `pytest.raises(ValueError, match="ujemna")` — przechodzi tylko, gdy funkcja rzuci ValueError z „ujemna” w treści.
5. `pytest.approx` — 0.1 + 0.2 to 0.30000000000000004, a test przechodzi.
6. Uruchom `python -m pytest -v test_magazyn_demo.py` → 5 passed.
7. Mutacja: zmień w funkcji `razem >= 100` na `razem > 100` → pada dokładnie test granicy (1 failed). Przywróć.

✔ **Oczekiwany wynik:** 5 passed; po mutacji `>=` → `>` — 1 failed (test_dostawa_darmowa_od_100) z komunikatem assert 9.99 == 0.

## 3 · Jak to uruchomić
1. Zapisz jako test_magazyn_demo.py w PRACA.
2. Terminal Mentora: `cd` do PRACA → `python -m pytest -v test_magazyn_demo.py`.
3. PyCharm: zielony trójkąt przy funkcji testu (interpreter środowiska kursu).

## W praktyce
- Każdy defekt znaleziony ręcznie → test regresji w pytest.
- Nazwa testu = zdanie z wymagania: test_dostawa_darmowa_od_100.

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji: dla `brutto(netto, vat=23)` (round 2) napisz w głowie 3 asserty i podaj oczekiwane wartości: (1) brutto(100), (2) brutto(10, 8), (3) brutto(0). (4) Jaki fragment kodu napiszesz, by sprawdzić, że `wydaj(5, 10)` rzuca ValueError (wpisz pierwszą linię bloku)? Czas: 15 minut.

📄 `cwiczenia/tydzien_07/pytest_1.md` · rozwiązanie: `rozwiazania/tydzien_07/pytest_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kolega napisał test: `def test_rabat(): wynik = rabat(250)` (bez assert). (1) Czy pytest uzna go za PASSED, gdy rabat() działa źle, ale nie rzuca wyjątku (tak/nie)? (2) Dla reguły „od 200 zł rabat 5%” (rabat zwraca procent) — który JEDEN assert złapie mutanta `> 200` zamiast `>= 200` (wpisz)? (3) Jak uruchomić tylko testy z „rabat” w nazwie (wpisz polecenie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_07/pytest_2.md` · rozwiązanie: `rozwiazania/tydzien_07/pytest_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **collected 0 items / no tests ran**
  - Przyczyna: Plik nie zaczyna się od test_ albo funkcje nie zaczynają się od test_.
  - Jak sprawdzić: Nazwy pliku i funkcji.
  - Poprawka: test_nazwa.py i def test_cos():.
- ✘ **ModuleNotFoundError: No module named 'ceny' w teście**
  - Przyczyna: pytest uruchomiony z innego katalogu niż moduł.
  - Jak sprawdzić: `pwd` i `ls`.
  - Poprawka: Uruchamiaj z katalogu projektu; testy obok modułu albo conftest.py w katalogu głównym.
- ✘ **assert 12.299999999999999 == 12.3 — FAILED**
  - Przyczyna: Porównanie float bez zaokrąglenia/tolerancji.
  - Jak sprawdzić: Wynik przed porównaniem.
  - Poprawka: round() w funkcji albo pytest.approx w teście.

## Pułapki
- Testy zależne od kolejności (jeden zmienia dane, drugi na nich polega) — każdy test przygotowuje swoje dane.
- Test, który nigdy nie padł, może nic nie sprawdzać — zrób mutację.

## Dodatkowe zadania
1. 5 testów do funkcji z tygodnia 3 (pole, parzysta, maksimum, odwróć, silnia).
2. Test wyjątku z pytest.raises.
3. Mutacja: zepsuj funkcję i sprawdź, czy test pada.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jak pytest znajduje testy?**
  - Pliki test_*.py, funkcje test_*.
- **Po co pytest.raises?**
  - Sprawdza, że kod rzuca oczekiwany wyjątek.
- **Czym jest mutant?**
  - Celowo zepsuta wersja kodu — dobry test ją wykrywa.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz testy pytest według AAA, testujesz wyjątki i liczby zmiennoprzecinkowe, uruchamiasz wybrane testy i sprawdzasz mutacją, że testy łapią błędy.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- pytest — Get Started (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/getting-started.html>
- pytest — How to write and report assertions in tests (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/how-to/assert.html>
- pytest — Changelog (9.2.0 z 27.10.2026; 9.0 bez Pythona 3.9) (dostęp 23.11.2026) — <https://pytest.org/en/latest/changelog.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Plik testów musi się nazywać:
  - A) testy.py
  - B) test_cos.py
  - C) cos.test
  - D) TEST.py
- Test bez assert:
  - A) zawsze FAILED
  - B) PASSED, jeśli nie było wyjątku
  - C) nie uruchomi się
  - D) jest błędem składni
- pytest.approx służy do:
  - A) napisów
  - B) porównań liczb zmiennoprzecinkowych z tolerancją
  - C) wyjątków
  - D) plików
- -k brutto uruchamia:
  - A) wszystkie testy
  - B) testy z „brutto” w nazwie
  - C) brutto.py
  - D) nic

Odpowiedzi: B, B, B, B
