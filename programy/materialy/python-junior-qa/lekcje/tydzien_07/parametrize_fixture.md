# parametrize i fixtures: wiele przypadków w jednym teście, wspólne dane, tmp_path
Tydzień 7 · lekcja 29 z 39 · ≈ 50 min

**Po tej lekcji potrafisz:** uruchamiasz jeden test dla wielu danych (@pytest.mark.parametrize), przygotowujesz wspólne dane fixturą (także z yield i w conftest.py) i testujesz zapis do plików w katalogu tymczasowym tmp_path.

**Po co mi to?** Tabela klas równoważności i wartości brzegowych zamienia się 1:1 w parametrize. Fixtury to podstawa każdego frameworka testów — także Selenium (przeglądarka jako fixture w tygodniu 8).

## Czego potrzebujesz
- Lekcja „pytest”.
- Menedżer zadań i kalkulator BMI z wcześniejszych tygodni.

## 1 · Wyjaśnienie od podstaw
### parametrize — tabela przypadków
```
import pytest

@pytest.mark.parametrize("razem, oczekiwany", [
    (49.99, 14.99),
    (50, 9.99),
    (99.99, 9.99),
    (100, 0),
])
def test_koszt_dostawy(razem, oczekiwany):
    assert koszt_dostawy(razem) == oczekiwany
```
Pierwszy argument — nazwy parametrów (przecinek w napisie), drugi — lista krotek. pytest uruchomi 4 osobne testy: `test_koszt_dostawy[49.99-14.99]` itd. Padnie tylko przypadek z defektem — reszta pokaże, że działa.
### fixture — przygotowanie danych
```
@pytest.fixture
def menedzer():
    lista = []
    dodaj(lista, "Zamówić papier")
    dodaj(lista, "Policzyć zeszyty")
    return lista

def test_otwarte(menedzer):
    assert len(otwarte(menedzer)) == 2
```
Test prosi o fixturę przez **nazwę parametru**. Każdy test dostaje **świeżą** kopię — testy nie psują sobie danych.
### yield — sprzątanie
W fixturze `yield wartosc` zamiast return: kod po yield wykona się po teście (zamknij plik, bazę, przeglądarkę).
### conftest.py
Fixtury w pliku conftest.py w katalogu testów są dostępne we wszystkich testach bez importu.
### tmp_path — pliki w testach
Wbudowana fixtura: osobny pusty katalog dla każdego testu. `plik = tmp_path / "zadania.json"` — test zapisuje i czyta, nie dotykając Twoich prawdziwych danych.
### Inne wbudowane
`monkeypatch` podmienia na czas testu np. funkcję input() albo zmienną środowiskową; `capsys` przechwytuje to, co wypisał print.

## 2 · Demonstracja — krok po kroku
**6 granic BMI, fixture z zadaniami i zapis w tmp_path**

```
# test_menedzer_demo.py — python -m pytest -v test_menedzer_demo.py
import json
import pytest


def kategoria_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    if bmi < 25:
        return "norma"
    if bmi < 30:
        return "nadwaga"
    return "otyłość"


@pytest.mark.parametrize("bmi, oczekiwana", [
    (18.4, "niedowaga"), (18.5, "norma"), (24.9, "norma"),
    (25, "nadwaga"), (29.9, "nadwaga"), (30, "otyłość"),
])
def test_kategoria_bmi(bmi, oczekiwana):
    assert kategoria_bmi(bmi) == oczekiwana


@pytest.fixture
def zadania():
    return [{"tytul": "Zamówić papier", "zrobione": False}, {"tytul": "Policzyć zeszyty", "zrobione": True}]


def test_otwarte(zadania):
    assert [z["tytul"] for z in zadania if not z["zrobione"]] == ["Zamówić papier"]


def test_zapis_i_odczyt(zadania, tmp_path):
    plik = tmp_path / "zadania.json"
    plik.write_text(json.dumps(zadania, ensure_ascii=False), encoding="utf-8")
    assert json.loads(plik.read_text(encoding="utf-8")) == zadania

```

1. `@pytest.mark.parametrize("bmi, oczekiwana", [...])` — 6 par = 6 testów; dane to wartości brzegowe progów 18.5, 25 i 30.
2. `pytest -v` pokaże `test_kategoria_bmi[18.4-niedowaga] PASSED` itd. — od razu widać, który przypadek pada.
3. `@pytest.fixture def zadania()` — wspólne dane; zwraca nową listę dla KAŻDEGO testu.
4. `test_otwarte(zadania)` — nazwa parametru = nazwa fixtury; pytest sam ją wywoła.
5. `test_zapis_i_odczyt(zadania, tmp_path)` — dwie fixtury naraz; tmp_path to pusty katalog tymczasowy.
6. Zapis JSON i odczyt — porównanie całych list słowników jednym assert.
7. Uruchom: 8 passed. Zmień w kategoria_bmi `< 25` na `<= 25` — padnie dokładnie przypadek [25-nadwaga].

✔ **Oczekiwany wynik:** 8 passed (6 z parametrize + 2); po mutacji progu 25 — 1 failed z nazwą przypadku w nawiasie.

## 3 · Jak to uruchomić
1. Zapisz jako test_menedzer_demo.py → terminal Mentora → `python -m pytest -v test_menedzer_demo.py`.

## W praktyce
- Tabela z przypadkami testowymi (tydz. 9) i parametrize mają te same wiersze.
- Przeglądarka, baza testowa, zalogowany użytkownik — wszystko jako fixtury.

## 4 · Ćwiczenie prowadzone
Reguła rabatu: < 100 → 0, 100–299.99 → 5, ≥ 300 → 10. Na wzór demonstracji wypisz listę par dla parametrize (wartości brzegowe dwupunktowo). (1) Ile par? (2) Jaki oczekiwany rabat dla 299.99? (3) Ile testów pokaże pytest -v dla parametrize z tą listą? Czas: 15 minut.

📄 `cwiczenia/tydzien_07/parametrize_fixture_1.md` · rozwiązanie: `rozwiazania/tydzien_07/parametrize_fixture_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dwa testy używają tej samej listy produktów: test_a usuwa pierwszy produkt, test_b sprawdza, że lista ma 3 produkty. (1) Lista jako zmienna globalna w pliku testów — czy test_b może paść zależnie od kolejności (tak/nie)? (2) Jakim dekoratorem zrobisz z funkcji tworzącej listę fixturę (wpisz)? (3) Gdzie zapisze plik test zapisu, żeby nie zniszczyć Twoich danych — wybierz: katalog PRACA / tmp_path / pulpit. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/parametrize_fixture_2.md` · rozwiązanie: `rozwiazania/tydzien_07/parametrize_fixture_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **fixture 'menedzer' not found**
  - Przyczyna: Literówka w nazwie parametru albo fixtura w innym pliku bez conftest.py.
  - Jak sprawdzić: Lista dostępnych: `python -m pytest --fixtures`.
  - Poprawka: Ta sama nazwa; fixtury wspólne w conftest.py.
- ✘ **ValueError/TypeError w parametrize: wrong number of values**
  - Przyczyna: Liczba nazw w napisie ≠ liczba elementów w krotkach.
  - Jak sprawdzić: Porównaj "a, b" z (x, y).
  - Poprawka: Ta sama liczba nazw i wartości w każdej krotce.
- ✘ **Test przechodzi pojedynczo, pada w całym zestawie**
  - Przyczyna: Wspólne dane modyfikowane przez inne testy.
  - Jak sprawdzić: Uruchom `-p no:randomly`/pojedynczo i porównaj.
  - Poprawka: Dane w fixturze, nie w zmiennej globalnej.

## Pułapki
- parametrize z 50 przypadkami „na wszelki wypadek” — wybieraj technikami, nie losowo.
- Fixture, która łączy się z prawdziwą bazą lub siecią — w testach jednostkowych używaj danych w pamięci i tmp_path.

## Dodatkowe zadania
1. parametrize: 6 przypadków BMI w jednym teście.
2. Fixture z menedżerem zadań użyta w 4 testach.
3. Test zapisu/odczytu z tmp_path.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi parametrize?**
  - Uruchamia ten sam test dla wielu zestawów danych.
- **Jak test dostaje fixturę?**
  - Przez parametr o nazwie fixtury.
- **Po co tmp_path?**
  - Pusty katalog tymczasowy na pliki testu.

## Co potrafię teraz bez patrzenia na przykład?
Zamieniasz tabelę przypadków w parametrize, przygotowujesz świeże dane fixturami (także w conftest.py) i testujesz pliki w tmp_path.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- pytest — How to parametrize fixtures and test functions (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/how-to/parametrize.html>
- pytest — How to use fixtures (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/how-to/fixtures.html>
- pytest — How to use temporary directories and files in tests (tmp_path) (dostęp 23.11.2026) — <https://docs.pytest.org/how-to/tmp_path.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ile testów da parametrize z listą 5 krotek?
  - A) 1
  - B) 5
  - C) 10
  - D) zależy od assert
- Fixture domyślnie tworzy dane:
  - A) raz na cały plik
  - B) od nowa dla każdego testu
  - C) nigdy
  - D) tylko dla pierwszego testu
- Kod po yield w fixturze wykona się:
  - A) przed testem
  - B) po teście
  - C) nigdy
  - D) dwa razy
- Plik z fixturami wspólnymi dla wielu plików testów:
  - A) fixtures.py
  - B) conftest.py
  - C) setup.py
  - D) __init__.py

Odpowiedzi: B, B, B, B
