# Moduły standardowe: random i datetime
Tydzień 3 · lekcja 15 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** importujesz moduły standardowe, losujesz (randint, choice, sample) — także powtarzalnie z seed — i liczysz na datach (date, timedelta, strftime, strptime).

**Po co mi to?** Losowe dane testowe i daty (terminy, ważność, „za 7 dni”) są w każdym systemie. Testy z losowością bez seed są niepowtarzalne — a test musi dać ten sam wynik za każdym razem.

## Czego potrzebujesz
- Lekcje „Funkcje” i „Listy”.

## 1 · Wyjaśnienie od podstaw
### import
`import random` — cały moduł, używasz `random.randint(...)`. `from datetime import date, timedelta` — konkretne nazwy, używasz `date.today()`. Moduły standardowe są w każdym Pythonie, bez instalacji.
### random
- `random.randint(1, 100)` — liczba całkowita od 1 do 100 **włącznie**;
- `random.choice(lista)` — jeden losowy element;
- `random.sample(lista, 3)` — 3 różne elementy (bez powtórzeń);
- `random.shuffle(lista)` — tasuje listę w miejscu;
- `random.seed(42)` — ustawia ziarno: od tej chwili losowania są **powtarzalne** (ważne w testach i przy odtwarzaniu błędu).
### datetime
- `date.today()` — dzisiejsza data; `date(2026, 12, 24)` — konkretna;
- `timedelta(days=7)` — odcinek czasu: `dzis + timedelta(days=7)` to data za tydzień; różnica dwóch dat to timedelta, `.days` — liczba dni;
- `strftime("%d.%m.%Y")` — data → napis po polsku (23.11.2026); `%A` — nazwa dnia (po angielsku w domyślnych ustawieniach);
- `datetime.strptime("24.12.2026", "%d.%m.%Y").date()` — napis → data.
### Funkcja testowalna z datą
Zamiast `date.today()` w środku funkcji przekaż datę parametrem: `def termin(od, dni=7): return od + timedelta(days=dni)`. Test poda stałą datę i zawsze dostanie ten sam wynik.

## 2 · Demonstracja — krok po kroku
**Losowanie produktów do inwentaryzacji i termin za 7 dni**

```
import random
from datetime import date, datetime, timedelta

random.seed(7)
produkty = ["zeszyt", "długopis", "klej", "gumka", "blok", "kredki"]
print("Do inwentaryzacji:", random.sample(produkty, 3))
print("Kostka:", random.randint(1, 6))

def termin(od, dni=7):
    return od + timedelta(days=dni)

start = date(2026, 11, 23)
print("Termin:", termin(start).strftime("%d.%m.%Y"))
wigilia = datetime.strptime("24.12.2026", "%d.%m.%Y").date()
print("Dni do Wigilii:", (wigilia - start).days)

```

1. `import random` i `from datetime import date, datetime, timedelta` — dwa sposoby importu.
2. `random.seed(7)` — ziarno: przy każdym uruchomieniu wylosujesz te same 3 produkty. Usuń tę linię, uruchom 3 razy — wyniki będą różne.
3. `random.sample(produkty, 3)` — 3 RÓŻNE produkty (choice mógłby się powtórzyć).
4. `random.randint(1, 6)` — obie granice wchodzą.
5. `termin(od, dni=7)` — data przekazana parametrem, więc wynik jest przewidywalny: 23.11.2026 + 7 dni = 30.11.2026.
6. `strftime("%d.%m.%Y")` — format polski.
7. `strptime` zamienia napis na datę; różnica dat `.days` → 31.

✔ **Oczekiwany wynik:** Trzy wylosowane produkty (te same przy każdym uruchomieniu z seed), liczba z kostki, „Termin: 30.11.2026”, „Dni do Wigilii: 31”.

## 3 · Jak to uruchomić
1. Zapisz jako losowanie_demo.py → ▶ Uruchom dwa razy — porównaj wyniki z seed i bez seed.

## W praktyce
- Dane losowe w testach zawsze z seed, a seed zapisany w raporcie.
- Daty graniczne do testów: 28/29 lutego, 31 grudnia, przejście czasu letniego.

## 4 · Ćwiczenie prowadzone
Na wzór `termin`: start = date(2026, 1, 28). Podaj datę w formacie DD.MM.RRRR dla: (1) termin(start) (7 dni), (2) termin(start, 30), (3) liczbę dni między date(2026, 3, 1) a date(2026, 2, 1). Czas: 15 minut.

📄 `cwiczenia/tydzien_03/moduly_std_1.md` · rozwiązanie: `rozwiazania/tydzien_03/moduly_std_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Test: `def test_losowanie(): assert wybierz_3(produkty) == ["klej", "blok", "zeszyt"]` — raz przechodzi, raz nie. (1) Dlaczego (wybierz)? (2) Jaką linię dodasz w teście przed losowaniem, żeby wynik był powtarzalny (wpisz z dowolną liczbą, np. 1)? (3) Które losowanie gwarantuje brak powtórzeń: choice 3 razy / sample(…, 3)? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/moduly_std_2.md` · rozwiązanie: `rozwiazania/tydzien_03/moduly_std_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **AttributeError: module 'datetime' has no attribute 'today'**
  - Przyczyna: `import datetime`, a potem `datetime.today()` (moduł, nie klasa).
  - Jak sprawdzić: Jak zaimportowałeś?
  - Poprawka: `datetime.date.today()` albo `from datetime import date` → `date.today()`.
- ✘ **ValueError: time data '2026-12-24' does not match format '%d.%m.%Y'**
  - Przyczyna: Format w strptime nie pasuje do napisu.
  - Jak sprawdzić: Porównaj znak po znaku.
  - Poprawka: Dopasuj format: "%Y-%m-%d" dla 2026-12-24.
- ✘ **Test raz zielony, raz czerwony (flaky)**
  - Przyczyna: Losowość albo date.today() w testowanej funkcji.
  - Jak sprawdzić: Uruchom test 5 razy.
  - Poprawka: random.seed(...) albo data przekazana parametrem.

## Pułapki
- Nazwanie własnego pliku random.py albo datetime.py — import weźmie Twój plik zamiast modułu.
- randint(1, 6) włącza 6, a range(1, 6) — nie.

## Dodatkowe zadania
1. Wylosuj 3 produkty do inwentaryzacji i wypisz datę kontroli za 7 dni.
2. Funkcja dni_do(data_docelowa, od) z testowalną datą.
3. Sprawdź, czy wynik losowania z seed jest stały.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co random.seed?**
  - Żeby losowanie było powtarzalne (testy, odtwarzanie błędu).
- **Jak dodać 7 dni do daty?**
  - data + timedelta(days=7).
- **Jak zamienić datę na napis 23.11.2026?**
  - data.strftime("%d.%m.%Y").

## Co potrafię teraz bez patrzenia na przykład?
Importujesz moduły, losujesz powtarzalnie (seed), liczysz terminy na datach i piszesz funkcje z datą w parametrze — testowalne.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — random: Generate pseudo-random numbers (dostęp 23.11.2026) — <https://docs.python.org/3/library/random.html>
- Python — datetime: Basic date and time types (dostęp 23.11.2026) — <https://docs.python.org/3/library/datetime.html>
- Python — Poradnik: Moduły (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/modules.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- random.randint(1, 3) może zwrócić:
  - A) tylko 1 lub 2
  - B) 1, 2 lub 3
  - C) 0–3
  - D) liczbę z kropką
- date(2026, 1, 31) + timedelta(days=1):
  - A) 2026-01-32
  - B) 2026-02-01
  - C) błąd
  - D) 2026-01-30
- Powtarzalne losowanie zapewnia:
  - A) random.repeat()
  - B) random.seed(stała)
  - C) import random dwa razy
  - D) sample
- sample(lista, 2):
  - A) może powtórzyć element
  - B) 2 różne elementy
  - C) sortuje
  - D) usuwa 2 elementy

Odpowiedzi: B, B, B, B
