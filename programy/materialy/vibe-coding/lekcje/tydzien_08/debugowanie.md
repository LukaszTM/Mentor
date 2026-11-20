# Debugowanie z AI: odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem
Tydzień 8 · lekcja 26 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** prowadzisz debugowanie metodą 5 kroków (odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem) i używasz AI jako partnera do hipotez — nie jako maszyny do losowych poprawek.

**Po co mi to?** Ankieta Stack Overflow 2025: 45% programistów mówi, że debugowanie kodu wygenerowanego przez AI zajmuje więcej czasu niż się spodziewali. Metoda skraca ten czas.

## Czego potrzebujesz
- Lekcje „Komunikat błędu”, „Gdy agent się myli”, „Testy jako umowa”.

## 1 · Wyjaśnienie od podstaw
### Pięć kroków
| krok | pytanie | narzędzie |
|---|---|---|
| 1. Odtwórz | czy umiem wywołać błąd na żądanie? | dokładne dane i polecenie |
| 2. Zawęź | najmniejszy przykład, który nadal psuje | usuwanie kawałków danych/kodu |
| 3. Wyjaśnij | dlaczego dokładnie tak się dzieje? | print, breakpoint(), traceback, AI: hipotezy |
| 4. Napraw | jedna zmiana przyczyny | agent lub Ty |
| 5. Zabezpiecz | czy błąd nie wróci? | test regresji z przykładem z kroku 2 |
### Krok 1–2: błąd, którego nie umiesz powtórzyć, nie jest naprawiony
Zgłoszenie „czasem liczy źle” zamieniasz w „dla rezerwacji 20.12–23.12 i 2 osób zwraca 0”. Potem zmniejszasz: czy przy 1 rezerwacji też? czy bez dzieci też? Minimalny przykład to połowa sukcesu — i idealny materiał dla agenta.
### Krok 3: patrzenie do środka
- `print(f"{zmienna=}")` — wypisuje nazwę i wartość (np. `noce=0`). Usuń po naprawie.
- `breakpoint()` — zatrzymuje program w tym miejscu (debugger pdb): `p zmienna` wypisuje, `n` następna linia, `c` dalej, `q` koniec.
- Agent w trybie diagnozy: „Nie zmieniaj plików. Dla tego minimalnego przykładu wyjaśnij krok po kroku, co dzieje się w funkcji, i wskaż linię, w której wartość staje się zła.”
### Dwa podstępne błędy, które AI lubi popełniać
- Mutowalna wartość domyślna: `def dodaj(r, lista=[])` — lista tworzy się RAZ i jest wspólna dla wszystkich wywołań (oficjalne FAQ Pythona). Objaw: dane „przeciekają” między wywołaniami. Poprawka: `lista=None` i w środku `if lista is None: lista = []`.
- Format daty: `"%m.%d.%Y"` zamiast `"%d.%m.%Y"` — dla 05.07.2026 nie ma błędu, tylko zła data (7 maja zamiast 5 lipca). Dla 20.12.2026 — ValueError. Objaw: błąd „tylko dla niektórych dat”.
### Krok 5: test regresji
Minimalny przykład z kroku 2 zamieniasz w test: `def test_dwa_wywolania_nie_dziela_listy(): …`. Jeśli kiedyś agent przywróci błąd, test go złapie. Regresja = powrót naprawionego błędu.

## 2 · Demonstracja — krok po kroku
**Błąd „tylko w grudniu” — od zgłoszenia do testu regresji**

```
def dodaj_rezerwacje(r, lista=[]):
    lista.append(r)
    return lista

print(dodaj_rezerwacje("Anna"))
print(dodaj_rezerwacje("Piotr"))   # oczekujesz ['Piotr']…

```

1. Zgłoszenie klientki: „import rezerwacji wywala się przy grudniowych”. Odtwarzasz: wczytaj_rezerwacje(["Anna;Lipowy;20.12.2026;23.12.2026"]) → ValueError: time data '20.12.2026' does not match format '%m.%d.%Y'.
2. Zawężasz: "05.07.2026" nie wywołuje błędu. Sprawdzasz wynik: 2026-05-07 — maj zamiast lipca! Błąd był zawsze, wybuchał tylko dla dni > 12.
3. Wyjaśnienie: format ma miesiąc i dzień zamienione. To nie „błąd grudnia”, tylko cichy błąd każdej daty.
4. Naprawa: "%d.%m.%Y". Test regresji: wczytanie "05.07.2026" daje date(2026, 7, 5) oraz "20.12.2026" działa.
5. Wniosek: ciche złe dane są groźniejsze niż wyjątek — dlatego testy sprawdzają WYNIK, nie tylko brak błędu.

✔ **Oczekiwany wynik:** Błąd zdiagnozowany jako zamiana dnia z miesiącem, naprawiony jedną zmianą i zabezpieczony testem dla dnia ≤ 12 i > 12.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „debug_rezerwacje.py” → „📄 Otwórz przykład” → 5 kroków → „✔ Sprawdź wynik”.
2. `breakpoint()` działa po uruchomieniu w terminalu Mentora (`python plik.py`).

## W praktyce
- Każde zgłoszenie błędu od klienta → minimalny przykład → test.
- Agent dostaje minimalny przykład, nie cały log.

## 4 · Ćwiczenie prowadzone
Co wypisze przykład lekcji (dwie linie)? Wpisz drugą linię dokładnie. Ile elementów będzie miała lista po trzecim wywołaniu `dodaj_rezerwacje("Ewa")`? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/debugowanie_1.md` · rozwiązanie: `rozwiazania/tydzien_08/debugowanie_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Funkcja parsuje datę formatem "%m.%d.%Y". Dla wejścia "05.07.2026": (1) czy będzie wyjątek (tak/nie)? (2) Jaki miesiąc (numer) wyjdzie w dacie? (3) Dla "20.12.2026" — jaki wyjątek? Czas: 15 minut.

📄 `cwiczenia/tydzien_08/debugowanie_2.md` · rozwiązanie: `rozwiazania/tydzien_08/debugowanie_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Dane z poprzedniego wywołania „pojawiają się” w nowym.**
  - Przyczyna: Mutowalna wartość domyślna (lista=[] / słownik={}).
  - Jak sprawdzić: Szukaj `=[]` i `={}` w linii def.
  - Poprawka: `lista=None` + `if lista is None: lista = []`.
- ✘ **Błąd „tylko czasem”.**
  - Przyczyna: Zależność od danych (dzień > 12, pusty wiersz, polski znak).
  - Jak sprawdzić: Zbierz 2 przykłady: działający i psujący — czym się różnią?
  - Poprawka: Minimalny przykład → hipoteza → test.
- ✘ **Program zatrzymał się z (Pdb) i nie reaguje.**
  - Przyczyna: breakpoint() został w kodzie.
  - Jak sprawdzić: Szukaj breakpoint( w plikach.
  - Poprawka: `c` kontynuuje, `q` kończy; usuń breakpoint przed commitem.

## Pułapki
- „Napraw” bez odtworzenia to zgadywanie — także dla agenta.
- Tymczasowe print i breakpoint nie trafiają do commita — sprawdź diff.

## Dodatkowe zadania
1. Napraw debug_rezerwacje.py metodą 5 kroków (zadanie tygodnia).
2. Dopisz 2 testy regresji do własnego test_*.py.
3. W dzienniku: minimalny przykład każdego błędu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie jest 5 kroków debugowania?**
  - Odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem.
- **Dlaczego lista=[] jako wartość domyślna jest groźna?**
  - Tworzy się raz i jest współdzielona między wywołaniami.
- **Co to jest test regresji?**
  - Test, który pilnuje, żeby naprawiony błąd nie wrócił.

## Co potrafię teraz bez patrzenia na przykład?
Debugujesz metodą 5 kroków, używasz print/breakpoint i AI do hipotez, znasz pułapki mutowalnych wartości domyślnych i formatów dat, zabezpieczasz naprawę testem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — pdb i breakpoint() (oficjalna dokumentacja) (dostęp 20.11.2026) — <https://docs.python.org/3/library/pdb.html>
- Python FAQ — Why are default values shared between objects? (mutowalne wartości domyślne) (dostęp 20.11.2026) — <https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects>
- Python — datetime.strptime: kody formatu (%d, %m, %Y) (dostęp 20.11.2026) — <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>
- Stack Overflow Developer Survey 2025 — AI (debugowanie kodu AI czasochłonne) (dostęp 20.11.2026) — <https://survey.stackoverflow.co/2025/ai>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Pierwszy krok debugowania:
  - A) Napraw
  - B) Odtwórz błąd na żądanie
  - C) Zmień model AI
  - D) Usuń test
- `print(f"{noce=}")` wypisze dla noce = 3:
  - A) 3
  - B) noce=3
  - C) {noce=}
  - D) Błąd
- `def f(x, wynik=[])` grozi:
  - A) Błędem składni
  - B) Współdzieloną listą między wywołaniami
  - C) Wolnym działaniem
  - D) Niczym
- Format daty dzień.miesiąc.rok w strptime:
  - A) %m.%d.%Y
  - B) %d.%m.%Y
  - C) %Y.%d.%m
  - D) %D.%M.%Y

Odpowiedzi: B, B, B, B
