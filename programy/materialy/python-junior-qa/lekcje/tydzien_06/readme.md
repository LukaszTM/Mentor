# README, docstringi, PEP 8 i refaktoryzacja
Tydzień 6 · lekcja 25 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** piszesz README projektu (co robi, jak uruchomić, przykład, jak testować) w Markdown, dokumentujesz funkcje docstringami, poprawiasz styl wg PEP 8 i refaktoryzujesz kod (nazwy, wydzielenie funkcji, stałe) bez zmiany działania.

**Po co mi to?** Rekruter otwiera README zanim spojrzy na kod. Czytelny, udokumentowany kod pokazuje, że umiesz pracować w zespole — to waży więcej niż liczba projektów.

## Czego potrzebujesz
- Projekty z tygodni 1–5 w repozytorium.
- Lekcje „Funkcje” i „Moduły”.

## 1 · Wyjaśnienie od podstaw
### README.md — wizytówka projektu
GitHub pokazuje README.md na stronie repozytorium. Markdown: `# Tytuł`, `## Sekcja`, `- lista`, `` `kod` ``, blok kodu w potrójnych odwrotnych apostrofach, `**pogrubienie**`, link `[tekst](adres)`, obraz `![opis](zrzut.png)`.
Minimum dla projektu w portfolio:
1. **Tytuł i jedno zdanie**: co robi i dla kogo.
2. **Jak uruchomić**: kroki od sklonowania (`git clone`, venv, `pip install -r requirements.txt`, `python main.py`).
3. **Przykład użycia**: wejście → wynik (blok kodu albo zrzut ekranu).
4. **Jak testować**: polecenie `pytest -v` i co jest testowane.
5. **Technologie** i ewentualnie „Co dalej” (znane ograniczenia).
### Docstring
Krótko: pierwsza linia — co robi funkcja (tryb rozkazujący lub opis), potem parametry, wynik, wyjątki. Konwencja PEP 257.
### PEP 8 — wspólny styl
Wcięcia 4 spacje, linie do ok. 79–100 znaków, nazwy `snake_case` dla funkcji i zmiennych, `CamelCase` dla klas, `WIELKIE_LITERY` dla stałych, spacje wokół operatorów (`a + b`), dwie puste linie między funkcjami. PyCharm podkreśla naruszenia; Code → Reformat Code poprawia formatowanie.
### Refaktoryzacja
Zmiana budowy kodu **bez zmiany działania**. Przed refaktoryzacją uruchom i zapisz wyniki (albo testy) — po refaktoryzacji muszą być identyczne. Typowe ruchy:
- lepsze nazwy (`x` → `cena_brutto`);
- wydzielenie funkcji z powtarzanego fragmentu;
- **magiczne liczby** w stałe (`0.23` → `VAT = 0.23`);
- logika z input()/print() do funkcji z return (testowalność).

## 2 · Demonstracja — krok po kroku
**Refaktoryzacja: z „x * 1.23 + 14.99” do czytelnych funkcji**

```
VAT = 0.23
PROG_DARMOWEJ_DOSTAWY = 100
KOSZT_DOSTAWY = 14.99


def brutto(netto):
    """Zwraca cenę brutto zaokrągloną do groszy."""
    return round(netto * (1 + VAT), 2)


def do_zaplaty(ceny_netto):
    """Suma brutto koszyka plus dostawa (darmowa od PROG_DARMOWEJ_DOSTAWY zł).

    ceny_netto: lista cen netto; pusta lista → 0.
    """
    if not ceny_netto:
        return 0
    suma = round(sum(brutto(c) for c in ceny_netto), 2)
    dostawa = 0 if suma >= PROG_DARMOWEJ_DOSTAWY else KOSZT_DOSTAWY
    return round(suma + dostawa, 2)


print(do_zaplaty([10, 20]), do_zaplaty([50, 40]), do_zaplaty([]))
print(do_zaplaty.__doc__.splitlines()[0])

```

1. Wersja przed (w głowie): `def f(x): s = 0; for i in x: s = s + i * 1.23; if s < 100: s = s + 14.99; return s` — działa, ale nic nie mówi.
2. Stałe `VAT`, `PROG_DARMOWEJ_DOSTAWY`, `KOSZT_DOSTAWY` zamiast liczb rozsianych po kodzie — zmiana VAT w jednym miejscu.
3. Wydzielona `brutto(netto)` — mała funkcja, łatwa do przetestowania osobno.
4. `do_zaplaty` z nazwą mówiącą, co zwraca, i docstringiem z opisem parametru i przypadku pustej listy.
5. Sprawdzenie, że działanie się nie zmieniło: 10 + 20 netto → 36.90 brutto + 14.99 = 51.89; 90 netto → 110.70 (darmowa dostawa).
6. `__doc__` — docstring jest dostępny w programie (i w help()).

✔ **Oczekiwany wynik:** „51.89 110.7 0” i pierwsza linia docstringu.

## 3 · Jak to uruchomić
1. Zapisz jako koszyk_refaktor.py → ▶ Uruchom.
2. README: utwórz README.md w katalogu projektu, wyślij na GitHub i sprawdź podgląd na stronie repozytorium.

## W praktyce
- Recenzując kod: nazwy, długość funkcji, duplikacje, magiczne liczby, brak docstringów.
- README każdego projektu w portfolio sprawdź „oczami rekrutera”: 30 sekund i wiesz, co to jest?

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji policz `do_zaplaty` dla: (1) [50, 31.3] netto, (2) [81.31] netto, (3) [81.30] netto. Czas: 15 minut.

📄 `cwiczenia/tydzien_06/readme_1.md` · rozwiązanie: `rozwiazania/tydzien_06/readme_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Oceń README (tak/nie — czy jest wystarczające): „# kalkulator\nmój projekt”. Wybierz, czego brakuje najbardziej (jedna odpowiedź): jak uruchomić / kolor tła / lista commitów. Następnie oceń nazwy wg PEP 8 (dobra/zła): (1) `def ObliczRabat(x):`, (2) `MAX_RABAT = 30`, (3) `class kalkulator:`, (4) `def cena_po_rabacie(cena, procent):`. Czas: 15 minut.

📄 `cwiczenia/tydzien_06/readme_2.md` · rozwiązanie: `rozwiazania/tydzien_06/readme_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Po refaktoryzacji inny wynik**
  - Przyczyna: Zmiana działania przy okazji „porządków”.
  - Jak sprawdzić: Porównaj wyniki przed/po na tych samych danych.
  - Poprawka: Refaktoryzuj małymi krokami, po każdym uruchom testy.
- ✘ **README na GitHubie bez formatowania**
  - Przyczyna: Plik nazwany README.txt albo brak pustej linii przed listą/nagłówkiem.
  - Jak sprawdzić: Nazwa pliku i podgląd.
  - Poprawka: README.md; puste linie wokół bloków Markdown.

## Pułapki
- README pisane na końcu „na szybko” — pisz je od początku i aktualizuj z kodem.
- Refaktoryzacja bez testów to zgadywanie — od tygodnia 7 zawsze najpierw testy.

## Dodatkowe zadania
1. README dla każdego projektu: opis, jak uruchomić, przykład, jak testować.
2. Docstringi do wszystkich funkcji kalkulatora BMI i zgadywanki.
3. Refaktoryzacja BMI: funkcje oblicz_bmi i kategoria, stałe progów.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co musi mieć README?**
  - Co robi, jak uruchomić, przykład, jak testować.
- **Czym jest refaktoryzacja?**
  - Zmiana budowy kodu bez zmiany działania.
- **Co to magiczna liczba?**
  - Liczba bez nazwy w kodzie (np. 0.23) — zamieniasz na stałą.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz README, które pozwala obcej osobie uruchomić projekt, dokumentujesz funkcje, trzymasz się PEP 8 i refaktoryzujesz kod bez zmiany działania.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- PEP 8 — Style Guide for Python Code (dostęp 23.11.2026) — <https://peps.python.org/pep-0008/>
- PEP 257 — Docstring Conventions (dostęp 23.11.2026) — <https://peps.python.org/pep-0257/>
- GitHub Docs — About READMEs (dostęp 23.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Nazwa funkcji zgodna z PEP 8:
  - A) LiczSume
  - B) licz_sume
  - C) LICZ_SUME
  - D) liczSume
- Refaktoryzacja zmienia:
  - A) działanie programu
  - B) budowę kodu, nie działanie
  - C) wymagania
  - D) testy na zielono
- Pierwsza sekcja, której szuka obca osoba w README:
  - A) licencja
  - B) jak uruchomić
  - C) historia
  - D) podziękowania
- Docstring umieszczasz:
  - A) na końcu pliku
  - B) jako pierwszy napis w funkcji
  - C) w README
  - D) w komentarzu #

Odpowiedzi: B, B, B, B
