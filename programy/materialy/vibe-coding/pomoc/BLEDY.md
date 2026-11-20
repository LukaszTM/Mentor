# Typowe błędy — z każdej lekcji

## Jak uczyć się z tego kursu — czym jest vibe coding (tydzień 0)
- **„Nie mam czasu na lekcje, od razu każę AI zrobić całą aplikację”.** — Pokusa skrótu — agent naprawdę potrafi wygenerować dużo kodu. → Zacznij od małego kawałka ze specyfikacją i testem; dużą aplikację budujesz w tygodniu 15 — z kamieniami milowymi.
- **„Panel pokazuje zaległości z trzech dni”.** — Przerwa w nauce. → Nie nadrabiaj wszystkiego: jedna lekcja + jedno zadanie dziennie; Mentor nie karze za przerwy.
- **„Kupiłem od razu dwa plany i Max”.** — Obawa, że jeden nie wystarczy. → Zacznij od jednego planu za 20 USD; limity widzisz w /usage (Claude Code) — podnoś plan dopiero, gdy limit naprawdę blokuje pracę.

## Jak działa model AI i czego się po nim spodziewać (tydzień 0)
- **Model podał nazwę biblioteki, `pip install` kończy się „ERROR: No matching distribution found”.** — Halucynacja — paczka nie istnieje (albo ma inną nazwę). → Nie instaluj niczego, czego nie znalazłeś w oficjalnym źródle; poproś model o rozwiązanie bez tej paczki.
- **„Wczoraj model znał mój projekt, dziś nic nie pamięta”.** — Nowa rozmowa = nowe okno kontekstu. → Zapisuj ustalenia w pliku (od tygodnia 5: CLAUDE.md / AGENTS.md) albo wklej streszczenie na początku.
- **Po godzinie rozmowy model myli wcześniejsze ustalenia.** — Długi kontekst — starsze fragmenty są streszczane albo „rozmywają się”. → Nowa rozmowa ze streszczeniem ustaleń; jedna rozmowa = jedno zadanie.

## Pliki, foldery, rozszerzenia i ścieżki (tydzień 0)
- **Plik nazywa się `witaj.py.txt` i Python mówi „can't open file 'witaj.py'”.** — Notatnik dopisał .txt, a rozszerzenia były ukryte. → Zmień nazwę na `witaj.py`; w Notatniku przy zapisie wybierz „Wszystkie pliki (*.*)”.
- **„Nie mogę znaleźć pliku, który utworzył agent”.** — Agent pracował w innym folderze niż myślisz. → Uruchamiaj agenta zawsze w katalogu PRACA (przycisk „Otwórz Claude Code tutaj”).
- **Program nie widzi pliku `dane\rezerwacje.csv`.** — Uruchomiony z innego folderu — ścieżka względna liczy się od bieżącego folderu. → Uruchamiaj programy z katalogu PRACA albo użyj ścieżki bezwzględnej.

## Terminal bez strachu: CMD i PowerShell (tydzień 1)
- **„'python' is not recognized as an internal or external command”.** — Python nie jest zainstalowany albo terminal nie ma go w PATH. → Środowisko → „⬇ Zainstaluj brakujące”, potem otwórz terminal przyciskiem Mentora (ustawia Pythona kursu na początku PATH).
- **„The system cannot find the path specified.” po `cd`.** — Literówka albo folder nie istnieje w bieżącym miejscu. → Użyj Tab do dopełniania nazwy; sprawdź `cd`, gdzie jesteś.
- **Terminal „wisi” — kursor miga, nic się nie dzieje.** — Program czeka na dane (input) albo zapętlił się. → Wpisz dane i Enter, a jeśli to pętla — Ctrl + C.

## Python: instalacja przez Mentora i pierwszy program (tydzień 1)
- **Instalacja środowiska kończy się błędem pobierania.** — Brak internetu, zapora sieciowa lub chwilowa awaria serwera. → Sprawdź połączenie i kliknij „Ponów”; w sieci firmowej poproś administratora o dostęp do pypi.org.
- **„SyntaxError: unterminated string literal”.** — Brak zamykającego cudzysłowu. → Każdy napis ma cudzysłów otwierający i zamykający tego samego rodzaju.
- **Okno wyniku pokazuje „Program pyta o więcej danych, niż podaje test”.** — W kodzie jest input(), a test nie podał wszystkich odpowiedzi. → Wpisz dane w polu „Dane dla input()” (jedna linia = jedna odpowiedź) albo usuń zbędne input().

## Czytanie kodu 1: zmienne, napisy, liczby i warunki (tydzień 1)
- **„TypeError: can only concatenate str (not "int") to str”.** — Sklejasz napis z liczbą: "Koszt: " + 100. → Użyj f-stringa: f"Koszt: {koszt}" albo str(koszt).
- **„IndentationError: expected an indented block”.** — Po if/else brakuje wciętej linii albo wcięcia są niespójne. → Wcięcie 4 spacje pod każdym if/elif/else; nie mieszaj tabulatora ze spacjami.
- **„SyntaxError: invalid syntax” przy `if noce = 7:`.** — Pojedyncze = to przypisanie; porównanie to ==. → `if noce == 7:`

## Czytanie kodu 2: listy, pętle, słowniki i funkcje (tydzień 2)
- **„IndexError: list index out of range”.** — Sięgasz po element o numerze, którego nie ma (np. lista[3] w liście 3-elementowej). → Pamiętaj: ostatni element to lista[len(lista) - 1] albo lista[-1].
- **„KeyError: 'nocy'”.** — Klucz w słowniku nazywa się inaczej (literówka, wielkość liter). → Popraw nazwę klucza albo użyj .get("klucz", domyślna).
- **Test: „assert None == …”.** — Funkcja nie ma return (albo return jest w złym miejscu, np. w pętli). → Dodaj return z wynikiem; nie zastępuj return przez print.

## Komunikat błędu (traceback) — czytanie od dołu (tydzień 2)
- **AI „poprawia” błąd, a pojawia się nowy, potem stary wraca.** — Zgłoszenie bez tracebacku i bez hipotezy — model zgaduje i łata objawy. → Szablon zgłoszenia z lekcji; po 2 nieudanych poprawkach — nowa rozmowa z podsumowaniem.
- **Poprawiłeś linię z tracebacku, ale wynik nadal jest zły.** — Przyczyna leży wyżej (złe dane wejściowe). → Szukaj, skąd wzięła się zła wartość — idź w górę tracebacku.
- **„ModuleNotFoundError: No module named 'requests'” w terminalu, a w Mentorze działa.** — Terminal używa innego Pythona niż środowisko kursu. → Otwieraj terminal przyciskiem Mentora (Python kursu jest pierwszy w PATH).

## Rozmowa z AI: kontekst, przykłady, ograniczenia, format (tydzień 2)
- **Model pisze dużo więcej, niż prosiłeś (GUI, baza, logowanie).** — Brak ograniczeń zakresu. → Dopisz „tylko X; bez interfejsu graficznego, bez bibliotek, maks. 40 linii”.
- **Każda poprawka psuje coś innego.** — Za długa rozmowa, model miesza wersje plików. → Nowa rozmowa: wklej aktualny plik + 3 zdania ustaleń + jedną prośbę.
- **Kod nie pasuje do Twojego Pythona/systemu (ścieżki /home/…, komendy Linuksa).** — Brak kontekstu systemu. → Kontekst: „Windows 11, CMD, Python 3.12”.

## Specyfikacja: „Gotowe, gdy…” — zamówienie, które da się sprawdzić (tydzień 3)
- **Agent zrobił „coś innego”, niż chciałeś.** — Specyfikacja bez przykładów — model zinterpretował słowa po swojemu. → Minimum 4 przykłady, w tym 2 brzegowe.
- **Agent dodał bibliotekę i przerobił 5 plików.** — Brak sekcji „Poza zakresem”. → Dopisz listę plików i rzeczy zakazanych; w Claude Code użyj trybu planu (tydzień 5).
- **Klient przy odbiorze: „miało być inaczej”.** — Decyzje podjęte po cichu zamiast zapisane i potwierdzone. → Sekcja „Decyzje i pytania do klienta” — wysyłasz ją przed budową.

## Pierwszy program z AI: od specyfikacji do zielonego testu (tydzień 3)
- **Mentor: „Brak pliku kalkulator_pobytu.py”.** — Plik zapisany pod inną nazwą lub w innym folderze (albo jako .py.txt). → Nazwa dokładnie jak w zadaniu, w katalogu PRACA.
- **„AssertionError: Brak funkcji koszt_pobytu”.** — Model nazwał funkcję inaczej (np. oblicz_koszt). → Zmień nazwę na tę ze specyfikacji — nazwy to umowa z testem.
- **Testy „wiszą” i kończą się po czasie.** — W kodzie jest input() poza blokiem __main__ — test czeka na klawiaturę. → Przenieś input() do bloku if __name__ == "__main__":.

## Powtórka etapu 0 i mini-projekt: rabaty sezonowe (tydzień 3)
- **Rabat 7 nocy + 4 osoby wychodzi 10 zamiast 15.** — elif zamiast niezależnych if — rabaty się nie sumują. → Dwa osobne if dodające do zmiennej, potem min(…, 15).
- **sezon("7") zwraca „niski”.** — Napis "7" to nie liczba 7 — `"7" in (6, 7, 8, 12)` to False. → Zamień na int przy wczytywaniu danych; w specyfikacji zapisz typ wejścia.

## Konta, plany i koszty: ile naprawdę kosztuje agent (tydzień 4)
- **„You've hit your session limit” w środku zadania.** — Wyczerpane okno 5-godzinne (długa sesja, duży kontekst). → Poczekaj do odnowienia okna; na przyszłość krótsze sesje, `/clear` między zadaniami (tydzień 7).
- **Claude Code po zalogowaniu mówi, że plan nie obejmuje dostępu.** — Darmowy plan claude.ai nie obejmuje Claude Code. → Pro lub wyższy albo konto API (Console); albo ścieżka bez konta.
- **Rachunek API wyższy niż subskrypcja.** — Płatność za tokeny bez limitu. → Ustaw limit wydatków w panelu API albo wróć do subskrypcji.

## Instalacja Claude Code w Windows i pierwsze uruchomienie (tydzień 4)
- **„'claude' is not recognized as an internal or external command” w nowym oknie.** — Folder %USERPROFILE%\.local\bin nie trafił do PATH. → PowerShell: `$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')` i `[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')`, potem nowe okno (polecenia z dokumentacji).
- **„The token '&&' is not a valid statement separator”.** — Komenda CMD wklejona do PowerShell. → Użyj wersji irm … install.ps1 | iex albo otwórz CMD.
- **Błąd SSL/TLS przy pobieraniu.** — Starszy Windows 10 bez TLS 1.2 domyślnie. → W PowerShell: `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`, potem instalacja.

## Codex: CLI i aplikacja na Windows, logowanie i tryby pracy (tydzień 4)
- **„running scripts is disabled on this system” przy instalacji.** — Zasady wykonywania skryptów PowerShell. → Skopiuj komendę z dokumentacji w całości: powershell -ExecutionPolicy ByPass -c "irm … | iex".
- **`npm` is not recognized.** — Brak Node.js (wariant instalacji przez npm). → Użyj instalatora PowerShell albo zainstaluj Node.js LTS z nodejs.org.
- **Codex po zalogowaniu nie daje dostępu w CLI.** — Plan Free/Go — CLI wymaga Plus lub wyższego. → Plus albo aplikacja desktop (ograniczony dostęp) albo ścieżka bez konta.

## Sesja z agentem: prośba, zgody, tryby, przerwanie i cofnięcie (tydzień 5)
- **Agent zmienił 6 plików, a prosiłeś o jedną funkcję.** — Ogólna prośba i tryb bez planu. → Tryb planu, lista plików w prośbie, potem /rewind do stanu sprzed zmiany.
- **Kliknąłeś „don't ask again” dla komendy, której nie chcesz.** — Reguła zapisana na stałe w .claude/settings.local.json. → Usuń regułę w /permissions.
- **Agent „myśli” od kilku minut i zużywa limit.** — Zbyt szerokie zadanie, pętla prób. → Esc, potem krótsza, konkretniejsza prośba albo tryb planu.

## Instrukcje projektu: AGENTS.md i CLAUDE.md — pamięć agenta (tydzień 5)
- **Agent ignoruje część zasad.** — Plik za długi albo zasady sprzeczne/ogólne. → Skróć do najważniejszych, konkretnych zasad; usuń sprzeczności.
- **Codex nie stosuje się do zasad z CLAUDE.md.** — Codex czyta AGENTS.md, nie CLAUDE.md. → Wspólne zasady w AGENTS.md, w CLAUDE.md tylko `@AGENTS.md`.
- **W repozytorium widać prywatne ścieżki i notatki.** — Osobiste rzeczy w CLAUDE.md projektu. → Osobiste ustawienia w CLAUDE.local.md (dodaj do .gitignore) albo ~/.claude/CLAUDE.md.

## Małe kroki: plan → jedna zmiana → test → zapis (tydzień 5)
- **Agent „przy okazji” refaktoryzuje sąsiednie funkcje.** — Brak granicy kroku w prośbie. → „Zrób tylko punkt 1, nie zmieniaj innych funkcji”; zasada w AGENTS.md.
- **Testy czerwone po kroku, nie wiesz dlaczego.** — Krok obejmował kilka zmian. → Cofnij (/rewind lub git restore) i podziel krok.

## Git: zapisujesz wersje i cofasz się w czasie (tydzień 6)
- **„Author identity unknown — Please tell me who you are”.** — Brak git config user.name / user.email. → Ustaw oba: git config --global user.name "…" i user.email "…".
- **„fatal: not a git repository”.** — Terminal nie jest w folderze z repozytorium. → Przejdź do PRACA albo zrób git init.
- **Do repozytorium trafił .env albo .venv.** — `git add .` przed utworzeniem .gitignore. → `git rm --cached .env`, dopisz do .gitignore, commit; jeśli klucz trafił do GitHuba — UNIEWAŻNIJ klucz u dostawcy (historia go pamięta).

## GitHub: konto z 2FA, repozytorium prywatne i wysyłanie zmian (tydzień 6)
- **„remote origin already exists”.** — Remote dodany wcześniej (może z literówką). → `git remote set-url origin <poprawny adres>`.
- **„failed to push some refs … Updates were rejected”.** — Na GitHubie są commity, których nie masz lokalnie (np. README utworzone na stronie). → `git pull --rebase origin main`, potem `git push`. Na przyszłość: repo bez README przy tworzeniu.
- **„Repository not found” przy push.** — Literówka w adresie albo zalogowane inne konto. → Popraw adres; w Menedżerze poświadczeń Windows usuń stare dane github.com i zaloguj ponownie.

## Przegląd zmian agenta: czytasz diff jak recenzent (tydzień 6)
- **Commit zawiera zmiany, których nie przeglądałeś.** — `git add .` po pracy agenta. → Dodawaj pliki po nazwie po przeglądzie; jeśli trzeba — `git revert HEAD`.
- **Testy zielone, ale klient zgłasza błąd.** — Agent osłabił lub usunął test. → Przywróć test, zasada „nie zmieniaj testów” w AGENTS.md, przegląd pytania 2 przy każdym commicie.

## Kontekst, limity i koszt sesji: /context, /clear, /compact, /usage (tydzień 7)
- **Agent „zapomina” ustalenia z początku sesji.** — Zapełnione okno — wcześniejsze fragmenty streszczone lub rozmyte. → Notatka stan.md + /clear; ważne decyzje do AGENTS.md.
- **Limit kończy się w 2 godziny.** — Długie sesje, ogólne prośby, mocny model do wszystkiego. → /clear między zadaniami, konkretne prośby, lżejszy model do prostych zmian.

## Gdy agent się myli: pętle, zmyślenia, „gotowe” bez dowodu (tydzień 7)
- **„AttributeError: module 'csv' has no attribute 'read_table'”.** — Zmyślona funkcja w prawdziwym module. → Pokaż agentowi właściwą funkcję (csv.DictReader) albo każ sprawdzić dokumentację.
- **Agent mówi, że test „ma błąd” i proponuje go zmienić.** — Agent optymalizuje „zielony wynik”, nie poprawność. → Jeśli tak — „napraw kod, nie test”; jeśli test naprawdę jest zły — zmieniasz go Ty, świadomie.

## Powtórka etapu 1 i mini-projekt z agentem: kalendarz dostępności (tydzień 7)
- **Wyjazd w dniu przyjazdu wykrywany jako kolizja.** — <= zamiast < w warunku nakładania. → Warunek przedziałów półotwartych: a.od < b.do and b.od < a.do.
- **Kolizja między różnymi pokojami.** — Brak sprawdzenia pokoju. → Najpierw: jeśli pokoje różne → False.
- **„TypeError: '<' not supported between instances of 'str' and 'datetime.date'”.** — Porównanie napisu z datą. → Zamieniaj napisy na daty date.fromisoformat() na początku funkcji.

## Testy jako umowa z agentem: pytest od zera (tydzień 8)
- **„ModuleNotFoundError: No module named 'cennik'” przy pytest.** — pytest uruchomiony z innego folderu niż plik cennik.py. → Uruchamiaj `python -m pytest` w katalogu z plikami (terminal Mentora otwiera się w PRACA).
- **„collected 0 items”.** — Plik albo funkcje nie zaczynają się od test_. → test_cennik.py, def test_…().
- **assert 0.30000000000000004 == 0.3 nie przechodzi.** — Liczby zmiennoprzecinkowe. → `== pytest.approx(0.3)` albo zaokrąglenie w kodzie do groszy.

## Debugowanie z AI: odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem (tydzień 8)
- **Dane z poprzedniego wywołania „pojawiają się” w nowym.** — Mutowalna wartość domyślna (lista=[] / słownik={}). → `lista=None` + `if lista is None: lista = []`.
- **Błąd „tylko czasem”.** — Zależność od danych (dzień > 12, pusty wiersz, polski znak). → Minimalny przykład → hipoteza → test.
- **Program zatrzymał się z (Pdb) i nie reaguje.** — breakpoint() został w kodzie. → `c` kontynuuje, `q` kończy; usuń breakpoint przed commitem.

## Refaktoryzacja z agentem: lepszy kod, to samo zachowanie (tydzień 8)
- **Po refaktoryzacji testy czerwone, agent proponuje „zaktualizować testy”.** — Zmieniło się zachowanie albo nazwy publicznych funkcji. → Cofnij krok; jeśli zmiana nazwy jest celowa — Twoja decyzja i alias albo świadoma aktualizacja testu.
- **Agent przepisał plik od nowa „czyściej”, testy zielone, ale diff ma 300 linii.** — Za duży krok. → Cofnij, prośba o refaktoryzację krok po kroku, commit po każdym.

## Strona internetowa: HTML (treść) i CSS (wygląd), także na telefonie (tydzień 9)
- **Polskie znaki wyświetlają się jako krzaczki („Ä…”).** — Brak meta charset utf-8 albo plik zapisany w innym kodowaniu. → `<meta charset="utf-8">` jako pierwszy element head; zapisz plik w UTF-8.
- **CSS nie działa.** — Zła ścieżka w link href (wielkość liter, folder). → href="styl.css" i plik obok index.html (albo poprawna ścieżka do folderu).
- **Na telefonie trzeba przewijać w bok.** — Stała szerokość w px albo brak viewport. → max-width zamiast width, meta viewport.

## JavaScript na stronie: formularz liczy koszt bez serwera (tydzień 9)
- **„Uncaught ReferenceError: obliczKoszt is not defined”.** — Plik JS nie wczytany (zła ścieżka) albo literówka w nazwie. → `<script src="kalkulator.js"></script>` przed `</body>`, plik obok index.html.
- **Wynik „NaN zł”.** — Wartość pola nie jest liczbą (pusta, tekst). → Number() + walidacja Number.isInteger i ≥ 1 z komunikatem.
- **Wynik pojawia się na ułamek sekundy.** — Brak e.preventDefault() w submit. → Pierwsza linia obsługi: e.preventDefault();

## Publikacja: GitHub Pages — strona pod własnym adresem (tydzień 9)
- **404 „There isn't a GitHub Pages site here”.** — Pages nie włączone, wdrożenie trwa albo brak index.html w korzeniu. → Włącz źródło main / (root), poczekaj do 10 min, index.html w korzeniu repozytorium.
- **Obrazek działa lokalnie, na Pages nie.** — Wielkość liter w nazwie pliku. → Ujednolić nazwy na małe litery w plikach i HTML.
- **Opcja Pages niedostępna dla repozytorium.** — Repozytorium prywatne na GitHub Free. → Osobne publiczne repo tylko z plikami strony.

## Dane: CSV z arkusza i JSON — wczytaj, policz, zapisz (tydzień 10)
- **„UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9”.** — Plik zapisany w Windows-1250 (stary Excel „CSV (rozdzielany przecinkami)”). → Zapisz plik jako „CSV UTF-8” w Excelu albo wczytaj encoding="cp1250" (i zapisz to w specyfikacji).
- **Raport ma mniej wierszy niż plik.** — Ciche pomijanie (except: continue) albo puste wiersze. → Zgłaszaj zły wiersz z numerem zamiast pomijać; puste wiersze pomijaj jawnie (if not any(w.values())).
- **Kwoty 10 razy za duże/małe.** — Kropka jako separator tysięcy („1.080,00”). → Usuń kropki i spacje tysięcy, potem przecinek → kropka.

## Aplikacja internetowa we Flask: trasy, parametry, JSON i testy (tydzień 10)
- **„Error: Could not locate a Flask application”.** — Uruchomienie z innego folderu albo zła nazwa w --app. → `flask --app app run` w PRACA (app = nazwa pliku bez .py); w pliku funkcja create_app albo zmienna app.
- **„Address already in use” / port 5000 zajęty.** — Serwer działa w innym oknie. → Zatrzymaj Ctrl + C albo `flask --app app run --port 5001`.
- **Testy: „TypeError: 'NoneType' object is not subscriptable” na get_json().** — Trasa zwraca HTML albo tekst, nie JSON. → Zwracaj jsonify(...) w trasach API.

## Baza danych SQLite: tabela, zapis, wyszukiwanie — bez SQL injection (tydzień 10)
- **„sqlite3.ProgrammingError: Incorrect number of bindings supplied”.** — `(email)` zamiast `(email,)` — napis traktowany jak sekwencja znaków. → Krotka z przecinkiem: (email,).
- **Dane „znikają” po zamknięciu programu.** — Brak commit (zapis bez with con: ani con.commit()). → with con: wokół zapisów.
- **„sqlite3.OperationalError: no such table: goscie”.** — Tabela nie utworzona w tej bazie (inna ścieżka pliku, :memory: w innym połączeniu). → CREATE TABLE IF NOT EXISTS przy połączeniu (funkcja polacz).

## API i klucze: pobierasz dane z internetu i nie zdradzasz sekretów (tydzień 11)
- **„requests.exceptions.ConnectTimeout” albo program wisi.** — Brak sieci, usługa nie odpowiada, brak timeout. → timeout=10 i obsługa wyjątku z czytelnym komunikatem („usługa pogody nie odpowiada”).
- **„401 Unauthorized” / „403 Forbidden”.** — Zły/nieaktywny klucz albo zły sposób przekazania (nagłówek vs parametr). → Sprawdź zmienną (echo %POGODA_API_KEY% — tylko u siebie!), sposób przekazania, aktywację klucza.
- **GitHub odrzuca push: „Push cannot contain secrets”.** — Ochrona przed wypchnięciem sekretu (push protection). → Usuń klucz z commita (zanim trafi do historii), unieważnij go, ustaw w zmiennej.

## Automatyzacje: skrypt porządkujący pliki z trybem próby i harmonogram (tydzień 11)
- **Pliki zniknęły / zostały nadpisane.** — shutil.move do istniejącej nazwy, brak trybu próby. → Zasada „nie nadpisuj” + test konfliktu + zawsze najpierw tryb próby na kopii.
- **Zadanie harmonogramu „działa”, ale nic się nie dzieje.** — Względne ścieżki albo inny Python (bez bibliotek) w harmonogramie. → Pełne ścieżki do python.exe środowiska kursu i do skryptu; katalog roboczy jako argument.
- **„PermissionError: [WinError 32] The process cannot access the file”.** — Plik otwarty w innym programie (np. Excel) albo synchronizowany przez OneDrive. → Pomiń plik z wpisem w logu zamiast przerywać całość; uruchamiaj, gdy pliki nie są używane.

## Powtórka etapu 2: aplikacja „wolne pokoje” — strona, API, dane (tydzień 11)
- **500 przy braku parametru.** — Łapany tylko ValueError, a None daje TypeError. → Łap (TypeError, ValueError) albo sprawdź None jawnie.
- **Testy /api/cena czerwone po dodaniu /api/wolne.** — Zmieniona sygnatura create_app albo importy. → create_app(rezerwacje=None) z wartością domyślną — stare wywołania create_app() działają.

## Bezpieczeństwo kodu od AI: XSS, wstrzyknięcia, sekrety, zależności (tydzień 12)
- **Po „naprawie” XSS strona pokazuje &amp;lt; zamiast <.** — Podwójne escapowanie (escape + szablon z autoescape). → Escapuj w jednym miejscu: szablon z autoescape albo escape() przy sklejaniu, nie oba.
- **Aplikacja nie startuje: KeyError 'FLASK_SECRET_KEY'.** — Zmienna nie ustawiona w tym oknie. → set FLASK_SECRET_KEY=… (lokalnie) — i czytelny RuntimeError zamiast KeyError.

## Bezpieczeństwo agenta: prompt injection, uprawnienia, sekrety, obce repozytoria (tydzień 12)
- **Reguły z .claude/settings.json nie działają.** — Błąd składni JSON (przecinek, cudzysłów) albo plik w złym miejscu. → Popraw JSON (każdy element w cudzysłowie, przecinki między elementami), plik w PRACA\.claude\settings.json.
- **Agent poprosił o zgodę na `curl … | bash` z adresu z README.** — Prompt injection albo zła instrukcja w obcym projekcie. → Odmów; reguła deny Bash(curl *); przeczytaj README sam; nie używaj trybu auto/Full access w obcych repozytoriach.

## Prawo: prawa do kodu z AI, licencje, RODO i AI Act (tydzień 12)
- **Publiczne repo bez pliku LICENSE, ktoś pyta, czy może użyć kodu.** — Brak licencji = wszystkie prawa zastrzeżone. → Dodaj licencję (np. MIT) — albo świadomie zostaw bez, jeśli nie chcesz udostępniać.
- **Do czatu trafił eksport z prawdziwymi danymi gości.** — Brak minimalizacji danych. → Usuń rozmowę, poinformuj administratora danych (klienta) zgodnie z umową; na przyszłość — dane fikcyjne lub zanonimizowane.

## Przegląd kodu jak w zespole: pull request, recenzja AI i Twoja decyzja (tydzień 13)
- **PR ma 40 plików i 2 000 linii.** — Wiele tematów naraz albo przepisanie przez agenta. → Podziel na kilka PR po jednym temacie; formatowanie osobno.
- **Recenzja AI „zatwierdziła” błąd.** — Recenzja w tej samej sesji albo bez listy kryteriów. → Nowa sesja, lista obszarów, testy — i Twoja recenzja jako ostatnia.

## Dokumentacja: README, które pozwala uruchomić projekt w 10 minut (tydzień 13)
- **„'source' is not recognized”.** — Polecenie Linuksa w README. → Wersje dla CMD i PowerShell.
- **„Activate.ps1 cannot be loaded because running scripts is disabled”.** — Zasady wykonywania skryptów PowerShell. → Użyj CMD (`.venv\Scripts\activate`) albo `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (świadomie) — opisz w README.

## Automatyczne testy w chmurze: GitHub Actions (CI) (tydzień 13)
- **Workflow się nie uruchamia.** — Plik w złym folderze (musi być .github/workflows/) albo błąd YAML. → Ścieżka .github/workflows/testy.yml, wcięcia spacjami.
- **Testy w CI wiszą.** — input() albo prawdziwe wywołanie API bez timeout. → input() tylko w __main__, testy z fałszywym klientem.

## Praca z klientem: od maila do wymagań, wyceny i odbioru (tydzień 14)
- **Klient przy odbiorze: „myślałam, że będzie też…”.** — Zakres nie spisany, brak „Poza zakresem”. → Wymagania z sekcją Poza zakresem wysłane i potwierdzone przed pracą; zmiany = nowa wycena.
- **Projekt trwa 2× dłużej niż wycena.** — Brak bufora, nieuwzględnione testy/README/poprawki. → Bufor 30–50%, osobne pozycje na testy, dokumentację i poprawki.

## Portfolio i ścieżki zawodowe vibe codera (tydzień 14)
- **Rekruter: „nie widzę, co Pan/Pani umie”.** — Repozytoria bez README, brak opisu profilu. → Profile README, przypięte 3 projekty z README i CI.
- **W publicznym repo znaleziono stary klucz.** — Klucz w historii commitów. → Unieważnij klucz; jeśli repo to portfolio — rozważ nowe repo bez tej historii.

## Rozmowa rekrutacyjna i zadanie praktyczne z AI (tydzień 14)
- **Na prośbę „wyjaśnij ten kod” — cisza.** — Kod w portfolio pisał agent, a nie był czytany. → Przed rozmową: przejdź swój projekt plik po pliku i opowiedz go na głos.
- **Odpowiedzi ogólne („zawsze testuję”).** — Brak przykładów. → Przygotuj 3 historie STAR z kursu i projektu końcowego.

## Projekt końcowy: plan, kamienie milowe i praca z agentem (tydzień 15)
- **Projekt „rozlewa się” — po tygodniu brak działającej wersji.** — Za duży zakres, brak MVP i kamieni. → Utnij do MVP; kamień po kamieniu z merge.
- **Agent skopiował kalendarz.py do system.py.** — Brak zasady importu. → Zasada w AGENTS.md: „importuj moduły kursu, nie kopiuj”; cofnij i powtórz krok.

## Wydanie wersji 1.0: CHANGELOG, tag, release i przekazanie (tydzień 15)
- **Tag jest lokalnie, ale nie ma go na GitHubie.** — `git push` nie wysyła tagów domyślnie. → `git push origin v1.0.0`.
- **Release zawiera plik .env albo bazę z danymi.** — Ręcznie dołączony ZIP z całego folderu. → Usuń zasób z release, unieważnij sekrety; ZIP buduj z `git archive` (tylko pliki z repo).

## Podsumowanie kursu: Twój proces, mapa dalszej nauki i plan utrzymania wiedzy (tydzień 15)
- **Po kursie wracasz do „kopiuj-wklej bez testów”.** — Brak spisanego procesu i szablonów. → Szablony (specyfikacja, AGENTS.md, PR) w Mentorze → Ściąga; proces na jednej stronie przy biurku.
- **Instrukcje z kursu przestały pasować do nowej wersji narzędzia.** — Zmiany w narzędziach (tryby, polecenia). → Kalendarz aktualizacji; zasady (testy, przegląd, sekrety) są niezależne od wersji.

## Komunikaty i sytuacje (Asystent offline)

- **SyntaxError** — Kod jest niepoprawnie zapisany — często ucięta odpowiedź AI, brak nawiasu, dwukropka albo cudzysłowu po wklejeniu. Spójrz na wskazaną linię i poprzednią. Czy skopiowałeś cały blok kodu przyciskiem Copy? Czy nawiasy i cudzysłowy się zamykają?
- **IndentationError** — Wcięcia są nierówne — po wklejeniu kodu z czatu spacje mieszają się z tabulatorami. Czy linie pod if/for/def mają po 4 spacje? Czy edytor nie zamienił spacji na tabulatory?
- **NameError** — Nazwa nie istnieje: literówka, brak importu albo zmienna z innej funkcji. Gdzie ta nazwa jest zdefiniowana? Czy jest import? Czy pisownia (także wielkość liter) jest identyczna?
- **TypeError** — Zła operacja dla typu: napis + liczba, wywołanie ze złą liczbą lub nazwą argumentów (np. parametr nazwany inaczej niż w specyfikacji). Jakie typy mają obie strony operacji? Czy nazwy parametrów zgadzają się ze specyfikacją?
- **ValueError** — Dobry typ, zła wartość: int("abc"), zła data, albo Twoja funkcja celowo odmawia złych danych. Jaka wartość trafiła do funkcji? Czy to błąd danych, czy kod powinien ją obsłużyć komunikatem?
- **KeyError** — Brak klucza w słowniku — inne nazwy kolumn w CSV, BOM w pierwszej kolumnie, literówka. Wypisz klucze słownika (print(d.keys())). Czy pierwsza kolumna nie ma niewidocznego \ufeff?
- **ModuleNotFoundError** — Brak biblioteki w środowisku albo nazwa paczki zmyślona przez AI. Czy paczka istnieje na pypi.org? Czy uruchamiasz Pythonem kursu (terminal z Mentora)? Czy jest w requirements.txt?
- **FileNotFoundError** — Brak pliku pod podaną ścieżką — zły folder roboczy, ukośnik wsteczny na Linuksie (CI), wielkość liter. Gdzie jesteś (cd)? Czy ścieżka jest względna od właściwego folderu? Czy używasz pathlib?
- **AssertionError** — Test nie przeszedł — wynik różny od oczekiwanego (Mentor pokazuje: dane → oczekiwano → otrzymano). Który przypadek jest czerwony? Czy oczekiwana wartość pochodzi ze specyfikacji? Czy agent nie zmienił testu?
- **Agent się zapętla** — Ten sam błąd wraca po kolejnych poprawkach; agent przeprasza i próbuje „inaczej”. Czy to trzecia próba? Esc, cofnij zmiany, nowa sesja z prośbą o diagnozę bez zmian w plikach.
- **Agent zmienił testy** — Testy zielone, ale w diffie zmieniony plik test_* — „naprawa” przez osłabienie testu. Czy git diff obejmuje test_*.py? Przywróć test (git restore) i poproś: „napraw kod, nie test”.
- **Limit planu** — Komunikat o wyczerpanym limicie sesji lub tygodnia. Co pokazuje /usage (Claude Code) albo /status (Codex)? Czy sesje są długie bez /clear? Pracuj w tym czasie nad testami, README i przeglądem.
