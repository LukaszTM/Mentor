# Powtórka etapu 1: podstawy Pythona w jednym programie
Tydzień 3 · lekcja 16 z 16 · ≈ 50 min

**Po tej lekcji potrafisz:** łączysz wszystkie podstawy (typy, warunki, pętle, listy, słowniki, funkcje, wyjątki) w program z menu, rozbijasz go na funkcje i sprawdzasz, które tematy etapu 1 musisz powtórzyć.

**Po co mi to?** Na rozmowie Junior QA dostaniesz małe zadanie z kodem: przeczytaj, znajdź błąd, dopisz warunek. To są dokładnie podstawy z tego etapu — połączone.

## Czego potrzebujesz
- Wszystkie lekcje tygodni 1–3.
- Wyniki quizów tygodni 1–3 (Statystyki).

## 1 · Wyjaśnienie od podstaw
### Mapa etapu 1
| temat | kluczowa umiejętność | typowy błąd |
|---|---|---|
| zmienne, typy | int/float/str/bool, rzutowanie | "5" + 5 |
| input/print | input zawsze str | brak int() |
| warunki | kolejność progów, granice | >= vs > |
| pętle | akumulator przed pętlą | pętla nieskończona |
| listy | indeks od 0, pusta lista | IndexError |
| napisy | metody zwracają nowy napis | brak przypisania |
| funkcje | return, blok main | None zamiast wyniku |
| słowniki | get, items, lista słowników | KeyError |
| wyjątki | konkretne except, raise | except: pass |
| random/datetime | seed, timedelta | test flaky |
### Jak zaplanować program z menu
1. Dane: jak je trzymasz? (lista słowników `{"tytul": …, "zrobione": False}`).
2. Operacje: każda jako funkcja **bez input()** — dostaje dane parametrami, zwraca wynik (dodaj, oznacz, usuń, lista otwartych).
3. Menu: pętla `while True` w bloku main — tylko tu input() i print().
4. Złe dane: nieznana opcja, numer spoza listy, pusty tytuł — każda funkcja rzuca ValueError, menu łapie i wypisuje komunikat.
### Samoocena
Napisz z pamięci (bez patrzenia w lekcje) funkcję, która z listy słowników zwraca te z ceną poniżej progu. Jeśli w 15 minut nie dasz rady — wróć do lekcji „Słowniki” i „Funkcje”.

## 2 · Demonstracja — krok po kroku
**Szkielet menedżera zadań: funkcje bez input()**

```
def dodaj(zadania, tytul):
    tytul = tytul.strip()
    if not tytul:
        raise ValueError("tytuł nie może być pusty")
    zadania.append({"tytul": tytul, "zrobione": False})


def oznacz(zadania, nr):
    if not 1 <= nr <= len(zadania):
        raise ValueError(f"nie ma zadania nr {nr}")
    zadania[nr - 1]["zrobione"] = True


def otwarte(zadania):
    return [z["tytul"] for z in zadania if not z["zrobione"]]


lista = []
dodaj(lista, "Zamówić papier")
dodaj(lista, "  Policzyć zeszyty ")
oznacz(lista, 1)
print(otwarte(lista))
for blad in [lambda: dodaj(lista, "   "), lambda: oznacz(lista, 5)]:
    try:
        blad()
    except ValueError as e:
        print("Błąd:", e)

```

1. `dodaj` — strip() i walidacja pustego tytułu (raise), dopisanie słownika do listy.
2. `oznacz` — numer dla człowieka od 1, indeks od 0: stąd `nr - 1`; zakres sprawdzony `1 <= nr <= len(zadania)`.
3. `otwarte` — lista tytułów niezrobionych zadań. Zapis `[z["tytul"] for z in zadania if not z["zrobione"]]` to **lista składana**: krótsza wersja pętli for z append.
4. Wywołania: dwa zadania, pierwsze oznaczone → otwarte: ['Policzyć zeszyty'] (spacje usunięte).
5. Dwa przypadki negatywne w try/except — dokładnie tak sprawdza je weryfikator zadania t3z5.
6. `lambda: …` — mała funkcja bez nazwy; tu tylko po to, żeby wywołać błąd w pętli. Nie musisz jej jeszcze używać sam.

✔ **Oczekiwany wynik:** „['Policzyć zeszyty']” i dwa komunikaty błędów.

## 3 · Jak to uruchomić
1. Zapisz jako szkielet.py → ▶ Uruchom.
2. Dopisz menu w bloku `if __name__ == "__main__":` z pętlą while True i opcjami 1–4, 0 = koniec.

## W praktyce
- Przed kodowaniem: na kartce dane + lista funkcji + przypadki złych danych.
- Zadanie rekrutacyjne: najpierw przeczytaj kod na głos, potem zmieniaj.

## 4 · Ćwiczenie prowadzone
Dla `lista` z demonstracji po wywołaniach: (1) ile elementów ma lista? (2) jaka jest wartość `lista[0]["zrobione"]`? (3) co zwróci `otwarte(lista)` po dodatkowym `oznacz(lista, 2)`? (4) jaki wyjątek rzuci `oznacz(lista, 0)`? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/powtorka_podstawy_1.md` · rozwiązanie: `rozwiazania/tydzien_03/powtorka_podstawy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Napisz funkcję `def usun(zadania, nr):` (bez input), która usuwa zadanie o numerze nr (od 1) i zwraca jego tytuł; dla złego numeru — ValueError. Dla listy ["A", "B", "C"] (jako słowniki) podaj: (1) co zwróci usun(…, 2), (2) ile zostanie zadań, (3) jaki tytuł ma teraz zadanie nr 2. Czas: 20 minut.

📄 `cwiczenia/tydzien_03/powtorka_podstawy_2.md` · rozwiązanie: `rozwiazania/tydzien_03/powtorka_podstawy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **IndexError przy oznaczaniu ostatniego zadania**
  - Przyczyna: Numer od 1 użyty jako indeks od 0.
  - Jak sprawdzić: Wypisz nr i len(lista).
  - Poprawka: Indeks = nr - 1, zakres 1 ≤ nr ≤ len.
- ✘ **Menu kończy się po pierwszym błędnym wpisie**
  - Przyczyna: Brak try/except wokół int(input()).
  - Jak sprawdzić: Wpisz „x” jako opcję.
  - Poprawka: try/except ValueError w pętli menu.

## Pułapki
- Funkcje z input() w środku — nie da się ich przetestować; input tylko w menu.
- Jedna wielka funkcja main na 100 linii — dziel na funkcje po 5–15 linii.

## Dodatkowe zadania
1. Menedżer zadań w konsoli: menu w pętli, każda operacja funkcją, lista słowników.
2. Powtórz lekcje z czerwonymi quizami.
3. Napisz z pamięci filtr produktów poniżej progu ceny.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego funkcje menedżera nie używają input()?**
  - Żeby dało się je testować i używać w innym interfejsie (np. web).
- **Jak zamienić numer zadania na indeks?**
  - indeks = nr - 1.
- **Co robi lista składana [x for x in l if w]?**
  - Buduje nową listę z elementów spełniających warunek.

## Co potrafię teraz bez patrzenia na przykład?
Łączysz podstawy w program z menu, rozdzielasz logikę od rozmowy z użytkownikiem, walidujesz dane wyjątkami i wiesz, co powtórzyć przed etapem 2.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Struktury danych (listy, krotki, słowniki) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/datastructures.html>
- Python — Poradnik: Więcej narzędzi kontroli przepływu (if, for, range, funkcje) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/controlflow.html>
- Python — Poradnik: Błędy i wyjątki (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/errors.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Numer zadania 3 to indeks:
  - A) 3
  - B) 2
  - C) 4
  - D) -3
- Gdzie input() w programie z menu?
  - A) w każdej funkcji
  - B) tylko w pętli menu (blok main)
  - C) w testach
  - D) nigdzie
- [x * 2 for x in [1, 2, 3]] to:
  - A) [1, 2, 3]
  - B) [2, 4, 6]
  - C) 6
  - D) 12
- lista.pop(0) zwraca:
  - A) None
  - B) pierwszy element (i go usuwa)
  - C) długość
  - D) ostatni element

Odpowiedzi: B, B, B, B
