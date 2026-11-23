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

## Pliki: open, read, write, with i kodowanie utf-8 (tydzień 4)
- **FileNotFoundError: [Errno 2] No such file or directory: 'dane.csv'** — Plik w innym katalogu niż katalog roboczy. → Uruchom z katalogu z plikiem albo podaj ścieżkę Path(__file__).parent / "dane.csv".
- **UnicodeDecodeError: 'charmap' codec can't decode byte…** — Plik utf-8 czytany domyślnym kodowaniem Windows. → open(…, encoding="utf-8").
- **Plik pusty po uruchomieniu** — Tryb "w" przy każdym uruchomieniu kasuje dane / plik nie zamknięty. → "a" do dopisywania; zawsze with.

## Moduł csv: DictReader, DictWriter i statystyki z pliku (tydzień 4)
- **KeyError: 'cena'** — Separator ; w pliku — DictReader widzi jeden klucz „nazwa;cena;ilosc”; albo literówka/BOM w nagłówku. → `delimiter=";"`; plik z Excela zapisuj jako CSV UTF-8 i otwieraj encoding="utf-8-sig".
- **ValueError: could not convert string to float: '4,50'** — Przecinek dziesiętny z polskiego Excela. → `float(w["cena"].replace(",", "."))`.
- **Puste linie między wierszami w zapisanym CSV** — Brak newline="" przy zapisie w Windows. → open(…, "w", encoding="utf-8", newline="").

## Git w zespole: gałęzie, diff, log, cofanie zmian i pull request (tydzień 4)
- **error: Your local changes to the following files would be overwritten by checkout** — Niezacommitowane zmiany przy przełączaniu gałęzi. → commit albo `git stash`, potem switch.
- **CONFLICT (content): Merge conflict in csv_odczyt.py** — Ta sama linia zmieniona na dwóch gałęziach. → Zostaw właściwą wersję, usuń znaczniki, git add, git commit.
- **fatal: The current branch feature/csv has no upstream branch** — Pierwszy push gałęzi bez -u. → `git push -u origin feature/csv`.

## Klasy i obiekty: __init__, self, metody, __str__ (tydzień 5)
- **TypeError: wydaj() takes 1 positional argument but 2 were given** — Brak self w definicji metody. → def wydaj(self, n):
- **AttributeError: 'Produkt' object has no attribute 'ilosc'** — W __init__ zabrakło self.ilosc = … (albo literówka). → Ustaw wszystkie atrybuty w __init__.
- **NameError: name 'ilosc' is not defined w metodzie** — Użycie `ilosc` zamiast `self.ilosc`. → Atrybuty obiektu zawsze przez self.

## Podział kodu na moduły i import własnych plików (tydzień 5)
- **ModuleNotFoundError: No module named 'zadania'** — main.py uruchomiony z innego katalogu albo literówka w nazwie pliku. → Uruchamiaj z katalogu projektu; nazwa pliku = nazwa w import (bez .py).
- **ImportError: cannot import name 'dodaj' from 'zadania'** — Brak funkcji o tej nazwie (literówka) albo import cykliczny. → Popraw nazwę; moduły nie importują się nawzajem w kółko.
- **Import uruchamia menu** — Kod menu poza blokiem __main__ w module. → Przenieś do if __name__ == "__main__":.

## venv, pip, requirements.txt i .gitignore (tydzień 5)
- **.\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system** — Domyślna polityka PowerShell blokuje skrypty. → `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` albo aktywacja w CMD (activate.bat).
- **pip install działa, a import nie (ModuleNotFoundError)** — Pakiet zainstalowany do innego Pythona. → Aktywuj .venv i używaj `python -m pip`.
- **Na GitHubie tysiące plików z .venv** — .gitignore dodany po commicie. → `git rm -r --cached .venv`, commit; .gitignore z .venv/.

## Biblioteka requests i API: GET, kody HTTP, JSON (tydzień 5)
- **requests.exceptions.ConnectionError: … Failed to establish a new connection** — Serwer nie działa / brak internetu / zły port. → Uruchom serwer (python app.py) albo sprawdź adres; łap RequestException.
- **requests.exceptions.JSONDecodeError: Expecting value** — Odpowiedź nie jest JSON-em (np. strona błędu HTML). → Sprawdź status przed .json().
- **KeyError: 'temperature' przy czytaniu JSON** — Inna struktura odpowiedzi niż zakładasz. → Dopasuj klucze do prawdziwej odpowiedzi; używaj .get().

## Debugowanie: print, breakpoint() i debugger krok po kroku (tydzień 6)
- **breakpoint() nic nie robi w Mentorze** — Przycisk ▶ uruchamia program bez interaktywnej konsoli pdb. → Uruchom w terminalu (`python plik.py`) albo w debuggerze PyCharm.
- **PyCharm: Debug nie zatrzymuje się na kropce** — Linia nigdy nie jest wykonywana albo uruchomiono Run zamiast Debug. → Debug (ikona robaka); kropka w linii, która na pewno się wykona.

## README, docstringi, PEP 8 i refaktoryzacja (tydzień 6)
- **Po refaktoryzacji inny wynik** — Zmiana działania przy okazji „porządków”. → Refaktoryzuj małymi krokami, po każdym uruchom testy.
- **README na GitHubie bez formatowania** — Plik nazwany README.txt albo brak pustej linii przed listą/nagłówkiem. → README.md; puste linie wokół bloków Markdown.

## Powtórka etapu 2: projekt jak w zespole — struktura, Git, środowisko, czytanie cudzego kodu (tydzień 6)
- **Po przeniesieniu plików importy nie działają** — Moduły w różnych folderach, a import zakłada ten sam katalog. → Każdy projekt uruchamiaj z jego folderu (cd kalkulator_bmi).
- **Historia pliku „zniknęła” po przeniesieniu** — Przeniesienie w Eksploratorze + nowy plik. → Przenoś `git mv` — historia zostaje.

## Podstawy testowania: pomyłka, defekt, awaria, poziomy testów, klasy równoważności i wartości brzegowe (tydzień 7)
- **„Przetestowałem 100 losowych wartości i jest OK”, a defekt na granicy przeszedł.** — Testy bez techniki — wszystkie wartości z jednej klasy. → Klasy równoważności + wartości brzegowe przed pisaniem testów.
- **Przypadek testowy „sprawdzić logowanie”.** — Brak danych i oczekiwanego wyniku. → Kroki, dane (login/hasło) i oczekiwany wynik (komunikat, strona).

## pytest: test_, assert, uruchamianie, pytest.raises i pytest.approx (tydzień 7)
- **collected 0 items / no tests ran** — Plik nie zaczyna się od test_ albo funkcje nie zaczynają się od test_. → test_nazwa.py i def test_cos():.
- **ModuleNotFoundError: No module named 'ceny' w teście** — pytest uruchomiony z innego katalogu niż moduł. → Uruchamiaj z katalogu projektu; testy obok modułu albo conftest.py w katalogu głównym.
- **assert 12.299999999999999 == 12.3 — FAILED** — Porównanie float bez zaokrąglenia/tolerancji. → round() w funkcji albo pytest.approx w teście.

## parametrize i fixtures: wiele przypadków w jednym teście, wspólne dane, tmp_path (tydzień 7)
- **fixture 'menedzer' not found** — Literówka w nazwie parametru albo fixtura w innym pliku bez conftest.py. → Ta sama nazwa; fixtury wspólne w conftest.py.
- **ValueError/TypeError w parametrize: wrong number of values** — Liczba nazw w napisie ≠ liczba elementów w krotkach. → Ta sama liczba nazw i wartości w każdej krotce.
- **Test przechodzi pojedynczo, pada w całym zestawie** — Wspólne dane modyfikowane przez inne testy. → Dane w fixturze, nie w zmiennej globalnej.

## Selenium WebDriver: przeglądarka, lokatory (ID, CSS, XPath), formularze (tydzień 8)
- **selenium.common.exceptions.NoSuchElementException: Unable to locate element** — Zły lokator albo element jeszcze się nie pojawił. → Popraw lokator; dla elementów ładowanych później — WebDriverWait (następna lekcja).
- **SessionNotCreatedException / Unable to obtain driver** — Brak przeglądarki albo brak internetu przy pierwszym pobraniu sterownika. → Uruchom z internetem raz (sterownik trafi do pamięci podręcznej) albo użyj innej przeglądarki.
- **ConnectionRefusedError / ERR_CONNECTION_REFUSED na stronie** — Sklep testowy nie jest uruchomiony. → W osobnym oknie `python app.py` w projekty/sklep_testowy.

## WebDriverWait i Page Object Model (tydzień 8)
- **selenium.common.exceptions.TimeoutException: Message:** — Warunek nie spełnił się w czasie: zły lokator albo element naprawdę się nie pojawił (bug?). → Popraw lokator; jeśli element powinien być — zgłoś defekt.
- **ElementClickInterceptedException** — Inny element (baner, okno) zasłania przycisk. → Zamknij baner w kroku testu albo czekaj element_to_be_clickable.
- **StaleElementReferenceException** — Strona się przeładowała, a używasz starego elementu. → Znajdź element ponownie po przeładowaniu (metoda strony za każdym razem szuka od nowa).

## Przypadki testowe i raporty błędów, które programista rozumie bez pytań (tydzień 9)
- **Zgłoszenie wraca z „Cannot reproduce”** — Brak danych, środowiska albo kroków wstępnych. → Dopisz dane, wersje, warunki wstępne; nagraj ekran.
- **Spór o ważność** — Ocena wpływu z perspektywy „mnie to irytuje”. → Opisz skutki faktami (np. „klient płaci 4,50 zamiast 45 zł”).

## GitHub Actions i pytest-html: testy uruchamiane przy każdym pushu (tydzień 9)
- **Zakładka Actions pusta po pushu** — Plik w złym miejscu (np. github/workflows bez kropki) albo rozszerzenie .yml.txt. → Przenieś plik do .github/workflows/ z rozszerzeniem .yml.
- **ERROR: file or directory not found: tests/** — Polecenie pytest wskazuje katalog, którego nie ma w repozytorium. → Popraw ścieżkę albo uruchamiaj samo `python -m pytest`.
- **Selenium w CI: SessionNotCreatedException / brak ekranu** — Przeglądarka bez trybu headless na serwerze bez ekranu. → `--headless=new`; w CI Chrome (`webdriver.Chrome(options=...)`).

## Powtórka etapu 3: strategia testów małego projektu (tydzień 9)
- **Odpowiedź na rozmowie: lista 30 kliknięć bez struktury.** — Brak strategii. → 5 pytań strategii: ryzyko → logika → integracja → ścieżki krytyczne → ręczne.
- **Wszystko automatyzowane E2E.** — „Bo to wygląda najlepiej”. → Piramida: reguły jednostkowo, E2E tylko krytyczne.

## SQLite i plan projektu: tabele, CREATE/INSERT/SELECT/UPDATE/DELETE, zapytania z parametrami (tydzień 10)
- **Dane „znikają” po zamknięciu programu** — Brak con.commit() (albo with con:). → `with con:` wokół zmian albo con.commit().
- **sqlite3.OperationalError: no such table: produkty** — Tabela nie utworzona albo inny plik bazy (np. inny katalog roboczy). → CREATE TABLE IF NOT EXISTS przy starcie; ścieżka względem pliku programu.
- **sqlite3.ProgrammingError: Incorrect number of bindings supplied** — `("biuro")` to napis, nie krotka. → `("biuro",)`.

## Flask: strony, szablony, formularze z walidacją i komunikaty (tydzień 11)
- **jinja2.exceptions.TemplateNotFound: index.html** — Szablon nie leży w katalogu templates/ obok app.py. → templates/index.html w katalogu aplikacji.
- **405 Method Not Allowed po wysłaniu formularza** — Trasa bez methods=["GET", "POST"]. → Dodaj methods=["GET", "POST"].
- **OSError: [Errno 98/10048] Address already in use** — Port zajęty (druga kopia aplikacji albo inny program). → Zamknij poprzednią (Ctrl+C) albo użyj innego portu.
- **KeyError / BadRequest: The browser sent a request that this server could not understand** — request.form["pole"] dla pola, którego nie ma w formularzu. → request.form.get("pole", "") i zgodne atrybuty name.

## Testy aplikacji webowej: Flask test_client, testy E2E Selenium własnej aplikacji i CI (tydzień 11)
- **Testy zmieniają prawdziwe dane** — Aplikacja na stałe łączy się z magazyn.db. → Fabryka aplikacji z parametrem i tmp_path w fixturze.
- **Test E2E czasem pada: element nie znaleziony** — Brak czekania po przeładowaniu strony. → WebDriverWait w metodach Page Objectów.

## CV, opowieść o projekcie i rozmowa rekrutacyjna Junior QA (tydzień 12)
- **Brak odpowiedzi na 50 wysłanych CV.** — Jednakowe CV bez projektów i słów kluczowych z ogłoszenia. → Projekty na górze, technologie z ogłoszenia, 5 dopasowanych aplikacji tygodniowo.
- **Na rozmowie: „nie wiem” i cisza.** — Brak struktury odpowiedzi. → Powiedz, jak byś to sprawdził(a): „Nie używałam X, ale zrobiłabym to tak…” + przykład z projektu.

## Powtórka końcowa: przegląd projektu jak senior tester i plan dalszej nauki (tydzień 12)
- **Wdrożenie wszystkich 20 uwag naraz w jednym commicie.** — Brak priorytetów. → 3 najważniejsze, każda osobnym commitem, CI po każdym.
- **Projekt „skończony”, a CI czerwone od tygodnia.** — Brak sprawdzenia po ostatnich zmianach. → Napraw przed wysłaniem CV — rekruter widzi czerwony znaczek.

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
