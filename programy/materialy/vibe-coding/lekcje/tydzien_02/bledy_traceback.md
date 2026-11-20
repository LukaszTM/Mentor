# Komunikat błędu (traceback) — czytanie od dołu
Tydzień 2 · lekcja 8 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** czytasz traceback od dołu: nazwa wyjątku, komunikat, plik i linia — i umiesz przekazać AI błąd tak, żeby poprawiło przyczynę, a nie objaw.

**Po co mi to?** Błędy to codzienność — także w kodzie od AI. Kto czyta traceback, naprawia w minutę; kto wkleja „nie działa”, kręci się w kółko godzinę.

## Czego potrzebujesz
- Lekcja „Czytanie kodu 2”.
- Plik napraw_mnie.py z materiałów kursu (przyklady/napraw_mnie.py) — do zadania tygodnia.

## 1 · Wyjaśnienie od podstaw
### Anatomia tracebacku
Gdy Python trafia na błąd, którego nikt nie obsłużył, wypisuje „Traceback (most recent call last):” i ścieżkę wywołań. Czytaj OD DOŁU:
```
Traceback (most recent call last):
  File "C:\...\PRACA\raport.py", line 9, in <module>
    print(srednia(ceny))
  File "C:\...\PRACA\raport.py", line 4, in srednia
    return suma / len(lista)
ZeroDivisionError: division by zero
```
- Ostatnia linia: typ wyjątku (ZeroDivisionError) i komunikat (division by zero) — CO się stało.
- Linia nad nią: plik, numer linii i funkcja (line 4, in srednia) — GDZIE się stało.
- Wyższe linie: KTO wywołał (line 9 wywołał srednia). Przyczyna bywa wyżej niż miejsce wybuchu: tu lista była pusta.
### Najczęstsze wyjątki
| wyjątek | co znaczy | typowa przyczyna w kodzie od AI |
|---|---|---|
| SyntaxError | kod jest niepoprawnie zapisany | ucięta odpowiedź, wklejony fragment bez nawiasu |
| IndentationError | złe wcięcie | mieszane spacje/tabulatory po wklejeniu |
| NameError: name 'x' is not defined | nazwa nie istnieje | literówka, brak importu, zmienna z innej funkcji |
| TypeError | zła operacja dla typu | napis + liczba, wywołanie z złą liczbą argumentów |
| ValueError | dobry typ, zła wartość | int("abc"), Twoje raise dla złych danych |
| KeyError / IndexError | brak klucza / indeksu | inne nazwy kolumn w CSV niż założyło AI |
| FileNotFoundError | brak pliku | zła ścieżka, uruchomienie z innego folderu |
| ModuleNotFoundError | brak biblioteki | nieinstalowana paczka (sprawdź, czy istnieje! — lekcja o halucynacjach) |
| AssertionError | test nie przeszedł | wynik różny od oczekiwanego |
### Metoda 4 kroków
- Przeczytaj ostatnią linię i przetłumacz ją na zdanie („dzielę przez zero”).
- Otwórz plik w linii z przedostatniego wpisu. Co tam jest? Jakie wartości mają zmienne? (wstaw tymczasowo `print(lista)` przed linią).
- Postaw hipotezę przyczyny („lista jest pusta, bo plik CSV nie miał wierszy”).
- Popraw przyczynę i uruchom ponownie. Jedna zmiana naraz.
### Jak zgłaszać błąd AI (szablon)
„Uruchamiam `python raport.py` w Windows. Oczekuję: średnia cen. Dostaję traceback (cały poniżej). Moja hipoteza: lista ceny jest pusta, gdy plik nie ma danych. Popraw tak, żeby dla pustej listy funkcja zwracała 0 i nie zmieniaj niczego innego.” + pełny traceback.
Pełny traceback, polecenie, którego użyłeś, i oczekiwany wynik — to trzy rzeczy, bez których AI zgaduje.
### Mentor pomaga
Okno wyniku „▶ Uruchom” tłumaczy najczęstsze wyjątki po polsku i pokazuje linię. Zakładka Asystent ma tryb „wyjaśnij błąd”.

## 2 · Demonstracja — krok po kroku
**Naprawa błędu z przyczyną wyżej niż wybuch**

```
Ten sam błąd zgłoszony źle i dobrze:

Źle: „nie działa, popraw”.

Dobrze: „Polecenie: python lista_gosci.py. Oczekiwane: 3 gości. Wynik: KeyError: 'imie' w linii 12 (funkcja raport). W słownikach klucz nazywa się 'imię' (z ogonkiem) — ujednolić na 'imie' w całym pliku, nic więcej nie zmieniaj.”
```

1. Program raport.py liczy średnią cenę z listy. Uruchamiasz i dostajesz traceback z ZeroDivisionError w line 4, in srednia.
2. Ostatnia linia: dzielenie przez zero. Line 4: return suma / len(lista) — dzielimy przez len(lista), więc len(lista) = 0: lista jest pusta.
3. Wyżej: line 9 wywołuje srednia(ceny). Wstawiasz przed nią print(ceny) → []. Hipoteza: filtr „ceny powyżej 1000” niczego nie znalazł.
4. Decyzja: co ma się dziać dla pustej listy? Specyfikacja mówi: zwróć 0. Dopisujesz w srednia: if not lista: return 0.
5. Uruchamiasz ponownie — działa. Usuwasz tymczasowy print. W dzienniku: „ZeroDivisionError — pusta lista; dodałem przypadek brzegowy”.

✔ **Oczekiwany wynik:** Błąd naprawiony u przyczyny (pusta lista), a nie przez „łatanie” miejsca wybuchu; masz zapis przypadku brzegowego do testów (tydzień 8).

## 3 · Jak to uruchomić
1. Zadanie tygodnia „Napraw mnie” → „📄 Otwórz przykład” → przepisz do napraw_mnie.py → „▶ Uruchom” i czytaj traceback od dołu.

## W praktyce
- Zawsze wklejaj pełny traceback, nie streszczenie.
- Po naprawie zapisz przypadek, który wywołał błąd — to przyszły test.

## 4 · Ćwiczenie prowadzone
Przeczytaj traceback:

Traceback (most recent call last):
  File "C:\PRACA\lista_gosci.py", line 15, in <module>
    raport(goscie)
  File "C:\PRACA\lista_gosci.py", line 8, in raport
    print("Gość: " + g["imie"] + ", noce: " + g["noce"])
TypeError: can only concatenate str (not "int") to str

Podaj: typ wyjątku, numer linii, w której wybuchło, nazwę funkcji i który klucz słownika jest liczbą. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/bledy_traceback_1.md` · rozwiązanie: `rozwiazania/tydzien_02/bledy_traceback_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj wyjątek do sytuacji: (1) `int("dwa")`, (2) `open("dane\\brak.csv")` gdy pliku nie ma, (3) `import pandass` (literówka), (4) `print(cena_kocowa)` przy zmiennej cena_koncowa. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/bledy_traceback_2.md` · rozwiązanie: `rozwiazania/tydzien_02/bledy_traceback_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **AI „poprawia” błąd, a pojawia się nowy, potem stary wraca.**
  - Przyczyna: Zgłoszenie bez tracebacku i bez hipotezy — model zgaduje i łata objawy.
  - Jak sprawdzić: Czy podałeś pełny traceback, polecenie i oczekiwany wynik?
  - Poprawka: Szablon zgłoszenia z lekcji; po 2 nieudanych poprawkach — nowa rozmowa z podsumowaniem.
- ✘ **Poprawiłeś linię z tracebacku, ale wynik nadal jest zły.**
  - Przyczyna: Przyczyna leży wyżej (złe dane wejściowe).
  - Jak sprawdzić: print zmiennych przed linią błędu.
  - Poprawka: Szukaj, skąd wzięła się zła wartość — idź w górę tracebacku.
- ✘ **„ModuleNotFoundError: No module named 'requests'” w terminalu, a w Mentorze działa.**
  - Przyczyna: Terminal używa innego Pythona niż środowisko kursu.
  - Jak sprawdzić: `where python` w CMD.
  - Poprawka: Otwieraj terminal przyciskiem Mentora (Python kursu jest pierwszy w PATH).

## Pułapki
- Nie owijaj wszystkiego w `try: … except: pass` — AI czasem tak „naprawia” błędy. Błąd znika z ekranu, a program liczy źle po cichu.
- Traceback może zawierać ścieżki z Twoim imieniem (C:\Users\Imie) — przy wklejaniu do publicznych miejsc (forum, GitHub) zamaskuj je.

## Dodatkowe zadania
1. Celowo wywołaj 3 różne wyjątki z tabeli w proby.py i przeczytaj każdy traceback od dołu.
2. Zgłoś jeden błąd czatowi AI według szablonu i porównaj z „nie działa, popraw”.
3. Zapisz w dzienniku swoją listę 3 najczęstszych błędów.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego traceback czytamy od dołu?**
  - Na dole jest typ i opis błędu oraz miejsce wybuchu; wyżej — kto to wywołał.
- **Co musi zawierać dobre zgłoszenie błędu do AI?**
  - Polecenie, oczekiwany wynik, pełny traceback, hipotezę i granice zmiany.
- **Dlaczego except: pass jest groźne?**
  - Ukrywa błąd — program działa dalej z błędnymi danymi i nikt o tym nie wie.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz traceback od dołu, rozpoznajesz najczęstsze wyjątki, szukasz przyczyny wyżej niż wybuch i zgłaszasz błąd AI według szablonu.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Błędy i wyjątki (oficjalny tutorial, rozdz. 8) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/errors.html>
- Python — Built-in Exceptions (lista wyjątków i ich znaczenie) (dostęp 19.11.2026) — <https://docs.python.org/3/library/exceptions.html>
- Claude Code — Best practices (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ostatnia linia tracebacku zawiera:
  - A) Pierwszą linię programu
  - B) Typ wyjątku i komunikat
  - C) Nazwę autora
  - D) Wersję Pythona
- `NameError: name 'sume' is not defined` najczęściej oznacza:
  - A) Brak internetu
  - B) Literówkę lub niezdefiniowaną zmienną
  - C) Błąd dysku
  - D) Zły system
- Co NIE jest dobrym sposobem naprawy błędu od AI?
  - A) Pełny traceback i hipoteza
  - B) Owinięcie kodu w try/except: pass
  - C) Jedna zmiana naraz
  - D) Sprawdzenie danych wejściowych
- ZeroDivisionError w funkcji średniej zwykle oznacza:
  - A) Zbyt duże liczby
  - B) Pustą listę
  - C) Złe wcięcie
  - D) Brak modułu

Odpowiedzi: B, B, B, B
