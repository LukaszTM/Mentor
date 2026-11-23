# Typowe błędy — z każdej lekcji

## Start: jak uczyć się z tego kursu (przeczytaj najpierw) (tydzień 0)
- **„Zrobię cały tydzień w sobotę”.** — Nauka zrywami — po 6 godzinach naraz pamięć i motywacja spadają. → Krótko, ale codziennie: 60–90 minut dziennie, sobota na quiz.
- **Zadanie zielone, a na quizie pustka.** — Kod skopiowany bez zrozumienia. → Przepisz kod ręcznie, zmień jedną wartość i przewidź wynik, zanim uruchomisz.

## Terminal, katalogi i pierwszy program w Pythonie (tydzień 0)
- **python: can't open file '…\hello.py': [Errno 2] No such file or directory** — Jesteś w innym katalogu niż plik. → `cd` do katalogu z plikiem albo podaj pełną ścieżkę.
- **'python' is not recognized as an internal or external command** — Python nie jest dostępny w tym terminalu. → Użyj terminala Mentora albo przycisku ▶ Uruchom — korzystają ze środowiska kursu.
- **SyntaxError: unterminated string literal** — Brakuje zamykającego cudzysłowu. → Każdy napis zaczyna się i kończy tym samym cudzysłowem: "…".

## Narzędzia: środowisko kursu w Mentorze, Git, edytor i (opcjonalnie) Claude Code (tydzień 0)
- **'git' is not recognized as an internal or external command** — Git niezainstalowany albo terminal otwarty przed instalacją. → Zainstaluj Git for Windows z git-scm.com (domyślne opcje) i otwórz nowe okno.
- **ModuleNotFoundError: No module named 'pytest'** — Program uruchomiony innym Pythonem niż środowisko kursu. → Uruchamiaj przyciskiem ▶ w Mentorze albo w terminalu Mentora.
- **Instalacja środowiska przerwana (brak internetu / miejsca)** — Pobieranie nie mogło się dokończyć. → Zwolnij miejsce / podłącz sieć → „Napraw”. Instalację można powtórzyć bez szkody.

## Git i GitHub — pierwszy commit i push (tydzień 0)
- **Author identity unknown *** Please tell me who you are.** — Brak user.name / user.email. → `git config --global user.name "…"` i `user.email "…"`.
- **fatal: not a git repository (or any of the parent directories): .git** — Polecenie wpisane poza repozytorium. → `cd` do katalogu projektu albo `git init`.
- **! [rejected] main -> main (fetch first)** — Na GitHubie są commity, których nie masz (np. repo założone z README). → `git pull --rebase origin main`, potem `git push`. Na przyszłość zakładaj puste repozytorium.

## Jak uczyć się z asystentem AI, żeby to Ty umiał programować (tydzień 0)
- **Kod od AI działa, ale nie wiesz dlaczego.** — Poziom 4 drabiny od razu. → Poproś: „wyjaśnij linia po linii” i przepisz ręcznie.
- **AttributeError / ModuleNotFoundError w kodzie od AI.** — Halucynacja: nieistniejąca metoda lub biblioteka. → Zapytaj AI: „czy ta funkcja na pewno istnieje? podaj link do dokumentacji” i sprawdź sam.

## Zmienne i typy danych: int, float, str, bool (tydzień 1)
- **TypeError: can only concatenate str (not "int") to str** — Sklejanie napisu z liczbą: `"Ilość: " + 3`. → `"Ilość: " + str(3)` albo f-string `f"Ilość: {3}"`.
- **ValueError: invalid literal for int() with base 10: '4,5'** — Przecinek zamiast kropki albo tekst w int(). → `float(x.replace(",", "."))` — albo wpisuj z kropką.
- **NameError: name 'Cena' is not defined** — Literówka lub wielkość liter w nazwie zmiennej. → Ujednolić nazwę: `cena` wszędzie małymi literami.

## print i input — rozmowa programu z użytkownikiem (tydzień 1)
- **TypeError: unsupported operand type(s) for *: 'float' and 'str'** — Liczba z input() nie została zamieniona: `cena * input()`. → `ilosc = int(input(...))`.
- **EOFError: EOF when reading a line** — Program czeka na dane, a nikt ich nie podał (pole danych w Mentorze puste). → Wpisz dane w polu nad wynikiem — po jednej linii na każde input().

## Instrukcje warunkowe if / elif / else (tydzień 1)
- **IndentationError: expected an indented block after 'if' statement** — Brak wcięcia po dwukropku. → Wcięcie 4 spacje (Tab w edytorze Mentora wstawia 4 spacje).
- **SyntaxError: invalid syntax przy `if x = 5:`** — Przypisanie = zamiast porównania ==. → `if x == 5:`.
- **Zła kategoria dla dużych kwot (bez komunikatu błędu)** — Progi w złej kolejności. → Ułóż warunki od największego progu.

## Pętle for i while, range, break i continue (tydzień 2)
- **Program „wisi”, brak wyniku** — Pętla while bez zmiany warunku. → Zmieniaj zmienną warunku w środku pętli albo użyj break.
- **Suma za duża przy drugim uruchomieniu funkcji** — Akumulator ustawiony poza funkcją/pętlą raz na zawsze. → Zeruj akumulator tuż przed pętlą, w tym samym bloku.
- **Brakuje ostatniej liczby (np. 10 w tabliczce)** — range(1, 10) kończy się na 9. → range(1, 11).

## Listy: indeksy, append, remove, sortowanie, len, sum, max (tydzień 2)
- **IndexError: list index out of range** — Indeks ≥ len(lista) (np. lista[3] dla 3 elementów). → Ostatni element to lista[-1] albo lista[len(lista) - 1].
- **ValueError: list.remove(x): x not in list** — Usuwasz wartość, której nie ma. → `if x in lista: lista.remove(x)`.
- **TypeError: 'NoneType' object is not subscriptable** — Wynik lista.sort() (None) użyty jak lista. → sorted(lista) albo samo lista.sort() bez przypisania.

## Napisy i ich metody: upper, lower, strip, split, replace, len, wycinki (tydzień 2)
- **Napis się „nie zmienia” po .upper()** — Wynik metody nie został zapisany. → Przypisz wynik albo użyj go od razu.
- **AttributeError: 'list' object has no attribute 'lower'** — Metoda napisu wywołana na liście (np. po split()). → Wywołaj na każdym elemencie w pętli albo przed split().
- **TypeError: 'str' object does not support item assignment** — Próba zmiany znaku: `t[0] = "z"`. → Zbuduj nowy napis: `t = "z" + t[1:]`.

## Funkcje: def, parametry, return, docstring, if __name__ == "__main__" (tydzień 3)
- **TypeError: brutto() missing 1 required positional argument: 'netto'** — Wywołanie bez wymaganego argumentu. → Podaj argument albo dodaj wartość domyślną.
- **Wynik funkcji to None** — Brak return (jest tylko print) albo return w złym miejscu. → return w każdej gałęzi, która ma oddać wynik.
- **Test „wisi” albo EOFError przy imporcie** — input() poza blokiem `if __name__ == "__main__":`. → Przenieś input()/print() programu do bloku main.

## Słowniki i krotki: klucz → wartość (tydzień 3)
- **KeyError: 'farby'** — Odczyt nieistniejącego klucza nawiasem []. → `stany.get("farby", 0)` albo `if "farby" in stany:`.
- **RuntimeError: dictionary changed size during iteration** — Usuwanie kluczy w pętli po tym samym słowniku. → Pętla po `list(stany.keys())` albo zbuduj nowy słownik.
- **TypeError: unhashable type: 'list'** — Lista jako klucz słownika. → Kluczem może być napis, liczba albo krotka.

## Obsługa błędów: try / except / else / finally i raise (tydzień 3)
- **Program „działa”, ale wynik bez sensu i bez komunikatu** — `except:` albo `except Exception: pass` połknęło błąd. → Łap konkretny wyjątek i reaguj komunikatem.
- **UnboundLocalError / NameError po bloku try** — Zmienna przypisana w try, który się nie udał, użyta dalej. → Użyj zmiennej w else albo nadaj wartość przed try.

## Moduły standardowe: random i datetime (tydzień 3)
- **AttributeError: module 'datetime' has no attribute 'today'** — `import datetime`, a potem `datetime.today()` (moduł, nie klasa). → `datetime.date.today()` albo `from datetime import date` → `date.today()`.
- **ValueError: time data '2026-12-24' does not match format '%d.%m.%Y'** — Format w strptime nie pasuje do napisu. → Dopasuj format: "%Y-%m-%d" dla 2026-12-24.
- **Test raz zielony, raz czerwony (flaky)** — Losowość albo date.today() w testowanej funkcji. → random.seed(...) albo data przekazana parametrem.

## Powtórka etapu 1: podstawy Pythona w jednym programie (tydzień 3)
- **IndexError przy oznaczaniu ostatniego zadania** — Numer od 1 użyty jako indeks od 0. → Indeks = nr - 1, zakres 1 ≤ nr ≤ len.
- **Menu kończy się po pierwszym błędnym wpisie** — Brak try/except wokół int(input()). → try/except ValueError w pętli menu.

## Komunikaty Pythona i Selenium (Asystent offline)

- **SyntaxError** — {'co': 'Błąd składni: brakujący nawias, cudzysłów albo dwukropek po if/for/def. Sprawdź wskazaną linię i tę przed nią.', 'pytanie': 'Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?'}
- **IndentationError** — {'co': 'Złe wcięcie: po linii z dwukropkiem blok musi być wcięty 4 spacjami; nie mieszaj Tab ze spacjami.', 'pytanie': 'Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?'}
- **NameError** — {'co': 'Nazwa nieznana: literówka, wielkość liter albo zmienna/moduł użyte przed utworzeniem/importem.', 'pytanie': 'Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?'}
- **TypeError** — {'co': 'Zły typ: np. "a" + 1, brak argumentu funkcji albo metoda bez self.', 'pytanie': 'Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?'}
- **ValueError** — {'co': 'Zła wartość: int("abc"), float("4,5") albo Twój raise przy złych danych.', 'pytanie': 'Przeczytaj ostatnią linię tracebacku i linię wskazaną w File … line N — co jest tam inaczej, niż zakładasz?'}
- **ZeroDivisionError** — {'co': 'Dzielenie przez zero', 'pytanie': 'sprawdź mianownik (pusta lista?) przed dzieleniem.'}
- **IndexError** — {'co': 'Indeks poza listą', 'pytanie': 'ostatni element to lista[-1] albo lista[len(lista) - 1].'}
- **KeyError** — {'co': 'Brak klucza w słowniku', 'pytanie': 'użyj d.get(klucz) albo sprawdź `in`.'}
- **AttributeError** — {'co': 'Obiekt nie ma takiej metody/atrybutu', 'pytanie': 'sprawdź typ (print(type(x))) i pisownię.'}
- **FileNotFoundError** — {'co': 'Plik nie istnieje w katalogu roboczym', 'pytanie': 'sprawdź os.getcwd() i nazwę z rozszerzeniem.'}
- **ModuleNotFoundError** — {'co': 'Moduł niezainstalowany w tym Pythonie albo plik w innym katalogu', 'pytanie': 'uruchamiaj w środowisku kursu (▶ w Mentorze).'}
- **NoSuchElementException** — {'co': 'Selenium nie znalazł elementu', 'pytanie': 'popraw lokator (DevTools) albo czekaj WebDriverWait.'}
- **TimeoutException** — {'co': 'Warunek WebDriverWait nie spełnił się w czasie', 'pytanie': 'zły lokator albo element się nie pojawił (defekt?).'}
