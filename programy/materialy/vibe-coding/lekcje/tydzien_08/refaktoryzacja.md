# Refaktoryzacja z agentem: lepszy kod, to samo zachowanie
Tydzień 8 · lekcja 27 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** zlecasz agentowi refaktoryzację pod osłoną testów: najpierw testy utrwalające obecne zachowanie, potem małe zmiany struktury (nazwy, funkcje, usuwanie powtórzeń) bez zmiany wyników.

**Po co mi to?** Kod od AI szybko rośnie i się powtarza. Refaktoryzacja utrzymuje projekt czytelnym dla Ciebie, klienta i kolejnych sesji agenta (krótszy kod = mniej kontekstu).

## Czego potrzebujesz
- Lekcja „Testy jako umowa”.
- Plik raport_obroty.py z materiałów (zadanie tygodnia).

## 1 · Wyjaśnienie od podstaw
### Definicja
Martin Fowler: refaktoryzacja to zmiana wewnętrznej struktury kodu, która ułatwia jego zrozumienie i modyfikację, BEZ zmiany zachowania widocznego z zewnątrz. Jeśli zmienia się wynik — to nie refaktoryzacja, tylko nowa funkcja albo błąd.
### Najpierw siatka: testy charakteryzujące
Zanim ruszysz brzydki, ale działający kod, utrwal jego zachowanie testami: uruchom funkcje na kilku danych, zapisz wyniki jako asserty. To testy charakteryzujące — opisują, co kod ROBI (nawet jeśli to dziwne). Po refaktoryzacji muszą przejść bez zmian.
### Sygnały, że kod trzeba uporządkować
| sygnał | przykład | ruch |
|---|---|---|
| powtórzony blok | ten sam kod sumowania w 3 miejscach | wydziel funkcję |
| długa funkcja | > 25–30 linii, kilka poziomów if/for | podziel na kroki |
| tajemnicze nazwy | `x`, `tmp2`, `dane_new` | nazwa mówi, co to jest |
| magiczne liczby | `* 0.9`, `if m in (6, 7, 8, 12)` w wielu miejscach | stała z nazwą: `RABAT_DLUGI = 0.10` |
| zmienne globalne zmieniane w funkcjach | `WYNIKI.append(...)` | parametry i return |
| martwy kod | zakomentowane stare wersje, nieużywane funkcje | usuń — historia jest w Gicie |
### Prośba do agenta
„Refaktoryzacja raport_obroty.py: usuń powtórzenia, podziel funkcje dłuższe niż 25 linii, nadaj czytelne nazwy, dodaj docstringi. Zachowanie BEZ ZMIAN: testy test_raport_obroty.py muszą przejść bez modyfikacji. Małe kroki: po każdej zmianie uruchom testy. Nie dodawaj zależności.”
### Jak sprawdzisz efekt
- Testy zielone bez zmian w plikach test_*.
- Diff: więcej usuniętych linii niż dodanych to dobry znak (ale nie reguła).
- Umiesz każdą funkcję opisać jednym zdaniem — docstring.
- PEP 8 (oficjalny przewodnik stylu Pythona): nazwy funkcji małymi literami z podkreśleniami, 4 spacje wcięcia.

## 2 · Demonstracja — krok po kroku
**Refaktoryzacja pod osłoną testów**

```
Przed:

def r(d):
    s = 0
    for x in d:
        if x['m'] in (6, 7, 8, 12):
            s = s + x['n'] * 150 * 0.9 if x['n'] >= 7 else s + x['n'] * 150
        else:
            s = s + x['n'] * 110 * 0.9 if x['n'] >= 7 else s + x['n'] * 110
    return s

Po:

SEZON_WYSOKI = (6, 7, 8, 12)
RABAT_DLUGI = 0.10

def cena_nocy(miesiac):
    """Cena za osobę za noc zależna od sezonu."""
    return 150 if miesiac in SEZON_WYSOKI else 110

def koszt(rezerwacja):
    """Koszt jednej rezerwacji z rabatem od 7 nocy."""
    k = rezerwacja['n'] * cena_nocy(rezerwacja['m'])
    return k * (1 - RABAT_DLUGI) if rezerwacja['n'] >= 7 else k

def przychod(rezerwacje):
    """Suma kosztów wszystkich rezerwacji."""
    return sum(koszt(r) for r in rezerwacje)
```

1. Testy charakteryzujące: dla 3 zestawów danych zapisujesz obecne wyniki r(d) w test_przychod.py. Zielone.
2. Krok 1 (agent): wydziel cena_nocy i stałe. Testy zielone. Commit.
3. Krok 2: wydziel koszt(rezerwacja). Testy zielone. Commit.
4. Krok 3: przemianuj r → przychod. Testy czerwone — test woła r! Decyzja: zostawiasz alias `r = przychod` na czas przejścia albo świadomie aktualizujesz test (to Twoja decyzja, nie agenta) i zapisujesz w opisie commita.
5. Diff całości: −9 / +12 linii, ale każda funkcja ma jedną odpowiedzialność i opis.

✔ **Oczekiwany wynik:** Ten sam wynik dla wszystkich danych testowych, czytelniejszy kod w 3 commitach, świadoma decyzja o zmianie nazwy.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „raport_obroty.py” → testy charakteryzujące (w materiałach) → refaktoryzacja z agentem → „✔ Sprawdź wynik”.

## W praktyce
- Raz w tygodniu 30 minut refaktoryzacji z testami.
- Osobne commity: refaktoryzacja / nowa funkcja / poprawka.

## 4 · Ćwiczenie prowadzone
Czy to refaktoryzacja (tak/nie)? (1) zmiana nazwy funkcji `r` na `przychod` z zachowaniem wyników, (2) zmiana rabatu z 10% na 15%, (3) wydzielenie powtórzonego bloku do funkcji, (4) „przy okazji” poprawienie błędu zaokrąglenia, który zmienia wynik o 1 grosz. Ile odpowiedzi „tak”? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/refaktoryzacja_1.md` · rozwiązanie: `rozwiazania/tydzien_08/refaktoryzacja_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
W kodzie liczba `0.9` występuje 4 razy, a `(6, 7, 8, 12)` — 3 razy. Ile stałych z nazwą warto utworzyć? Jaką nazwę według PEP 8 nadasz funkcji „oblicz przychód miesięczny”: `ObliczPrzychod`, `oblicz_przychod_miesieczny`, `OBLICZ`? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/refaktoryzacja_2.md` · rozwiązanie: `rozwiazania/tydzien_08/refaktoryzacja_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Po refaktoryzacji testy czerwone, agent proponuje „zaktualizować testy”.**
  - Przyczyna: Zmieniło się zachowanie albo nazwy publicznych funkcji.
  - Jak sprawdzić: Który test i dlaczego?
  - Poprawka: Cofnij krok; jeśli zmiana nazwy jest celowa — Twoja decyzja i alias albo świadoma aktualizacja testu.
- ✘ **Agent przepisał plik od nowa „czyściej”, testy zielone, ale diff ma 300 linii.**
  - Przyczyna: Za duży krok.
  - Jak sprawdzić: git diff --stat.
  - Poprawka: Cofnij, prośba o refaktoryzację krok po kroku, commit po każdym.

## Pułapki
- Refaktoryzacja bez testów to zmiana na ślepo — najpierw testy charakteryzujące.
- Nie łącz refaktoryzacji z nowymi funkcjami w jednym commicie — przegląd staje się niemożliwy.

## Dodatkowe zadania
1. Zrefaktoryzuj raport_obroty.py pod osłoną testów (zadanie tygodnia).
2. Znajdź w swoim projekcie 2 magiczne liczby i zamień na stałe.
3. Dodaj docstringi do 3 funkcji.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym jest refaktoryzacja?**
  - Zmianą struktury kodu bez zmiany zachowania widocznego z zewnątrz.
- **Po co testy charakteryzujące?**
  - Utrwalają obecne zachowanie, żeby refaktoryzacja go nie zmieniła.
- **Dlaczego martwy kod usuwasz zamiast komentować?**
  - Bo historia jest w Gicie, a martwy kod myli ludzi i agentów oraz zużywa kontekst.

## Co potrafię teraz bez patrzenia na przykład?
Refaktoryzujesz pod osłoną testów charakteryzujących, małymi krokami, z czytelnymi nazwami, stałymi i docstringami — wynik się nie zmienia.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Martin Fowler — Refactoring (definicja i katalog refaktoryzacji) (dostęp 20.11.2026) — <https://refactoring.com/>
- PEP 8 — Style Guide for Python Code (dostęp 20.11.2026) — <https://peps.python.org/pep-0008/>
- Claude Code — Best practices (test-driven, weryfikacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Refaktoryzacja zmienia:
  - A) Wyniki programu
  - B) Strukturę kodu bez zmiany zachowania
  - C) Wymagania klienta
  - D) Testy
- Zanim zrefaktoryzujesz kod bez testów:
  - A) Piszesz testy charakteryzujące
  - B) Usuwasz go
  - C) Zmieniasz język
  - D) Nic
- Magiczna liczba to:
  - A) Liczba losowa
  - B) Wartość bez nazwy powtarzana w kodzie
  - C) Błąd składni
  - D) Liczba pierwsza
- Nazwa funkcji zgodna z PEP 8:
  - A) ObliczKoszt
  - B) oblicz_koszt
  - C) OBLICZKOSZT
  - D) oblicz-koszt

Odpowiedzi: B, A, B, B
