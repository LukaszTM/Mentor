# -*- coding: utf-8 -*-
"""
Instrukcje „jak wykonać” do każdego zadania programu Python → Junior QA.
Klucz = id zadania z tresc.py. Pola:
  kroki    — lista kroków do wykonania po kolei (pełne zdania, konkretne komendy/kliknięcia)
  sprawdz  — jak samodzielnie sprawdzić, że zadanie jest zrobione
  problemy — typowe kłopoty i co wtedy zrobić
  czas     — orientacyjny czas w minutach
"""

JAK = {
    # ------------------------------------------------------------------ TYDZIEŃ 0
    "t0z1": {
        "czas": 60,
        "kroki": [
            "ŚRODOWISKO W MENTORZE. Zakładka Środowisko (pasek po lewej) → „Sprawdź ponownie”. Tabela pokazuje, co NAPRAWDĘ działa na Twoim komputerze: "
            "Python, środowisko kursu (.venv), biblioteki (pytest, requests, selenium, flask), Git, Claude Code, przeglądarka Edge. Statusy: GOTOWE / BRAK / OPCJONALNE. "
            "Na czystym komputerze zobaczysz sporo „BRAK” — to normalne, nic jeszcze nie rób ręcznie.",
            "Kliknij „Zainstaluj brakujące”. Mentor pokaże LISTĘ kroków, zanim cokolwiek zrobi: co pobierze, skąd (python.org/GitHub, PyPI), ile MB, czy potrzebny internet "
            "i jakie uprawnienia (żadne — wszystko trafia do katalogu Twojego użytkownika, bez administratora). Przeczytaj, potwierdź. "
            "Jeśli w systemie nie ma Pythona, Mentor pobierze Pythona 3.12 (ok. 46 MB) tylko dla kursów; jeśli jest — użyje go.",
            "Czekaj i patrz na pasek postępu i log (kilka minut). Mentor działa w tle — możesz w tym czasie czytać lekcję. Przyciski „Anuluj” i „Ponów” są pod paskiem; "
            "„Pokaż szczegóły” otwiera pełny log. Po zakończeniu Mentor sam uruchamia testy końcowe: interpreter, biblioteki, przykładowy pytest, lokalne API. "
            "Selenium (przeglądarka) będzie potrzebne dopiero w tygodniu 8 — może być „pominięto”.",
            "GIT (Mentor go nie instaluje — to oficjalny instalator). Wejdź na git-scm.com → „Download for Windows” → uruchom. We wszystkich oknach zostaw domyślne ustawienia i klikaj „Next”, "
            "na końcu „Install”. Potem w Mentorze: Środowisko → „Sprawdź ponownie” → Git ma status GOTOWE z numerem wersji.",
            "EDYTOR (opcjonalnie teraz, polecany od tygodnia 4). W tygodniach 0–3 wystarczy Notatnik: przycisk „Otwórz w edytorze” pod zadaniem otworzy plik w VS Code lub PyCharm, "
            "jeśli są, a jeśli nie — w Notatniku. Gdy chcesz kolorowanie i podpowiedzi: jetbrains.com/pycharm/download → „PyCharm Community Edition” (darmowy) → zainstaluj z domyślnymi ustawieniami.",
            "CLAUDE CODE (tylko gdy masz plan Pro/Max — inaczej pomiń i używaj zakładki Asystent → Offline lub API). Start → wpisz „PowerShell” → otwórz → wpisz:\n"
            "irm https://claude.ai/install.ps1 | iex\nPo instalacji ZAMKNIJ PowerShell. W Mentorze: Środowisko → „Sprawdź ponownie” → Claude Code GOTOWE. "
            "Potem Mój projekt → „Otwórz Claude Code tutaj” — przy pierwszym uruchomieniu zaloguj się w przeglądarce tym samym kontem co na claude.ai.",
        ],
        "sprawdz": "Zakładka Środowisko: Python, Środowisko kursu (.venv), pytest, requests, selenium, flask i Git mają GOTOWE; testy „interpreter”, „import bibliotek”, „pytest” i „lokalne API” zielone "
                   "(Selenium może być „pominięto” do tygodnia 8). Panel pokazuje plakietkę „środowisko gotowe”.",
        "problemy": [
            "„Brak połączenia z internetem” → Mentor nie pobierze Pythona ani bibliotek; lekcje działają. Podłącz sieć i kliknij „Ponów”.",
            "Python ma status BRAK, choć „coś” było zainstalowane → skrót ze Sklepu Windows nie jest prawdziwym Pythonem (Mentor go pomija). Po prostu pozwól Mentorowi pobrać własnego Pythona 3.12.",
            "Git po instalacji dalej BRAK → kliknij „Sprawdź ponownie”; jeśli nadal — zamknij i otwórz Mentora (nowe programy pojawiają się w PATH dopiero w nowo uruchomionych aplikacjach).",
            "Instalacja przerwana z błędem → „Pokaż szczegóły”, skopiuj ostatnie linie logu do Asystenta: „utknąłem: [tekst]”. Najczęściej: brak miejsca na dysku (potrzeba ok. 400 MB) albo antywirus blokujący pobieranie.",
            "Windows SmartScreen przy instalatorze Gita → „Więcej informacji” → „Uruchom mimo to” (instalator pobrany z git-scm.com jest podpisany).",
        ],
    },
    "t0z2": {
        "czas": 30,
        "kroki": [
            "KATALOG ROBOCZY. Zakładka Mój projekt → „Utwórz katalog roboczy kursu”. Mentor założy folder Dokumenty\\Mentor\\python-junior-qa\\PRACA i od teraz tu będą powstawać Twoje pliki. "
            "Wolisz własną nazwę (np. nauka-python w Dokumentach)? Utwórz folder w Eksploratorze (małe litery, myślnik, bez spacji i polskich znaków) i wskaż go przyciskiem „Wybierz katalog…”.",
            "CLAUDE.md. W Mój projekt kliknij „Utwórz CLAUDE.md z zasadami” — powstanie plik z zasadami nauki, które asystent czyta na starcie (nie pisz rozwiązań za mnie, pytaj przed kodem, po polsku…). "
            "Kliknij „Otwórz folder” i obejrzyj plik (prawy przycisk → Otwórz w → Notatnik).",
            "Wariant z Claude Code: Mój projekt → „Otwórz Claude Code tutaj” → wpisz  /init  → Claude utworzy CLAUDE.md. Potem DOPISZ na końcu zasady nauki (zakładka Prompty → „Treść pliku CLAUDE.md” → Kopiuj).",
            "Opcjonalnie PyCharm: File → Open → wskaż katalog roboczy → „Trust Project”. Po lewej zobaczysz drzewo plików z CLAUDE.md. Gdy PyCharm pyta o interpreter — wskaż Python z zakładki Środowisko "
            "(ścieżka .venv kursu jest wypisana w nagłówku zakładki) albo zostaw na później.",
            "Sprawdź w Mentorze: Mój projekt pokazuje ścieżkę katalogu i „CLAUDE.md z zasadami nauki — OK”. Od teraz Mentor widzi Twoje pliki i (po zadaniu 4) commity.",
        ],
        "sprawdz": "Mój projekt pokazuje ścieżkę katalogu roboczego i „CLAUDE.md z zasadami nauki — OK”; w pliku jest 5 zasad (nie pisz rozwiązań za mnie, pytaj przed kodem, po polsku, pokazuj różnicę…).",
        "problemy": [
            "„Utwórz katalog roboczy kursu” nie działa → brak uprawnień do Dokumentów (np. OneDrive w trybie tylko do odczytu). Wskaż inny folder przyciskiem „Wybierz katalog…”.",
            "Nie widzisz pliku CLAUDE.md w Eksploratorze → Widok → zaznacz „Rozszerzenia nazw plików”; plik nazywa się dokładnie CLAUDE.md, nie CLAUDE.md.txt.",
        ],
    },
    "t0z3": {
        "czas": 45,
        "kroki": [
            "Najpierw teoria na 10 minut. W Asystencie (lub Claude Code) wklej prompt: „Wytłumacz mi, czym jest plik .py, interpreter i katalog roboczy — jak dziesięciolatkowi.” "
            "W trybie Offline: wpisz  co to jest plik .py , potem  co to jest interpreter ,  co to jest katalog roboczy. Przeczytaj, powiedz własnymi słowami.",
            "Plan → tydzień 0 → to zadanie → pod opisem jest pasek „Ćwiczenie w Mentorze · hello.py”. Kliknij „Utwórz plik ćwiczenia” — Mentor zapisze hello.py w katalogu roboczym (z komentarzem na górze) "
            "i otworzy go w edytorze (Notatnik, VS Code albo PyCharm — co masz).",
            "Wpisz w pliku pod komentarzem (sam, nie wklejaj):\nprint(\"Cześć, tu Łukasz\")\nZamiast Łukasz — Twoje imię. Zapisz: Ctrl+S (w Notatniku: Plik → Zapisz; nie zmieniaj nazwy ani rozszerzenia).",
            "Wróć do Mentora i kliknij „▶ Uruchom”. Otworzy się okno z wyjściem programu — powinno być Twoje zdanie i „kod wyjścia 0”. To jest TEN moment: pierwszy program. "
            "Mentor uruchomił go interpreterem kursu (tym z zakładki Środowisko).",
            "Dodaj datę. Na górze pliku dopisz linię  import datetime , a na dole:\nprint(\"Dziś jest\", datetime.date.today())\nZapisz, kliknij „▶ Uruchom” ponownie. Jeśli nie rozumiesz, co robi import — zapytaj Asystenta: „co to jest moduł”.",
            "Kliknij „✔ Sprawdź wynik”. Mentor uruchamia program i sprawdza, czy wypisał co najmniej 2 linie i bieżący rok — gdy tak, zadanie odhacza się samo („ZALICZONE AUTOMATYCZNIE”).",
            "Zepsuj celowo: usuń jeden cudzysłów, zapisz, „▶ Uruchom”. W oknie zobaczysz czerwony komunikat i wyjaśnienie po polsku. Przeczytaj go OD DOŁU (ostatnia linia mówi CO, wyżej GDZIE). Napraw. Tak wygląda 50% programowania.",
            "Wariant terminalowy (poznasz go w tygodniu 4, teraz tylko spróbuj): Mój projekt → „Otwórz terminal tutaj” → wpisz  python hello.py  → Enter. To ta sama komenda, którą Mentor wykonuje za Ciebie przyciskiem.",
        ],
        "sprawdz": "„▶ Uruchom” pokazuje Twoje imię i dzisiejszą datę bez czerwonego tekstu; „✔ Sprawdź wynik” daje „Zaliczone”. W Planie przy zadaniu świeci „✔ wykryto hello.py”.",
        "problemy": [
            "„SyntaxError” z strzałką → sprawdź cudzysłowy i nawiasy w tej linii; muszą być parami.",
            "„Nic nie wypisał — brak print()?” → zapisałeś plik? (Ctrl+S). Notatnik zapisał jako hello.py.txt? → w oknie zapisu wybierz „Wszystkie pliki” i nazwę hello.py.",
            "Polskie znaki wyświetlają się krzywo → zapisz plik w kodowaniu UTF-8 (Notatnik: Plik → Zapisz jako → Kodowanie: UTF-8). Mentor uruchamia programy w UTF-8.",
            "„Brak Pythona do uruchomienia pliku” → wróć do zadania 1: zakładka Środowisko → Zainstaluj brakujące.",
        ],
    },
    "t0z4": {
        "czas": 60,
        "kroki": [
            "Załóż konto na github.com (jeśli nie masz): Sign up → e-mail → hasło → nazwa użytkownika (np. LukaszTM) → potwierdź e-mail.",
            "Otwórz terminal w katalogu roboczym: Mój projekt → „Otwórz terminal tutaj” (albo Terminal w PyCharm). Przedstaw się Gitowi (raz na komputer):\ngit config --global user.name \"Imię Nazwisko\"\ngit config --global user.email \"twoj@email.pl\"\n(ten sam e-mail co na GitHubie).",
            "Zamień folder w repozytorium:  git init  (Enter). Odpowiedź: „Initialized empty Git repository”. W folderze powstał ukryty podfolder .git — nie ruszaj go.",
            "Zobacz, co Git widzi:  git status  → pokaże CLAUDE.md i hello.py na czerwono jako „untracked” (nieśledzone). Dodaj je:  git add .  (kropka = wszystko). Jeszcze raz git status → na zielono.",
            "Zrób pierwszy commit (zdjęcie projektu z podpisem):  git commit -m \"dzień 1: hello.py i CLAUDE.md\"  . Odpowiedź z liczbą plików i linii. Sprawdź historię:  git log --oneline.",
            "Na GitHubie: zielony przycisk „New” (albo plus w prawym górnym rogu → New repository) → Repository name: nauka-python → Public → NIE zaznaczaj „Add a README” (masz już pliki) → Create repository.",
            "GitHub pokaże komendy „…or push an existing repository from the command line”. Wpisz w terminalu dokładnie te trzy linie (zaczynają się od git remote add origin …, git branch -M main, git push -u origin main). "
            "Przy pushu przeglądarka poprosi o zalogowanie do GitHuba — zaloguj, wróć do terminala.",
            "Odśwież stronę repozytorium na GitHubie — widzisz hello.py i CLAUDE.md. Od teraz koniec każdego dnia to: git add . → git commit -m \"dzień N: temat\" → git push.",
        ],
        "sprawdz": "Strona github.com/TwojaNazwa/nauka-python pokazuje Twoje pliki i commit „dzień 1…”. Mentor → Mój projekt → Git: „zdalne repo: tak”, „commity łącznie: 1”. (Nazwa repozytorium może być inna niż katalogu PRACA — to bez znaczenia.)",
        "problemy": [
            "„Please tell me who you are” → zrób krok 2 (git config).",
            "„remote origin already exists” → wpisałeś komendę remote dwa razy; to nie błąd, przejdź do git push.",
            "„Authentication failed” przy pushu → zainstaluj GitHub CLI (cli.github.com), wpisz  gh auth login  i przejdź przez logowanie w przeglądarce; potem git push jeszcze raz.",
            "Push odrzucony „rejected” → zaznaczyłeś „Add a README” na GitHubie. Wpisz  git pull origin main --allow-unrelated-histories , a potem git push.",
        ],
    },
    "t0z5": {
        "czas": 45,
        "kroki": [
            "Wklej do Asystenta prompt: „Wytłumacz mi, co to jest zmienna, funkcja i pętla — bez kodu, na przykładach z gospodarstwa.” (Offline:  co to jest zmienna ,  co to jest funkcja ,  co to jest pętla ).",
            "Nowy plik notatki.md w katalogu roboczym (md = Markdown, zwykły tekst z nagłówkami): w PyCharm prawy przycisk na folderze → New → File; bez PyCharma: Mój projekt → „Otwórz folder” → prawy przycisk → Nowy → Dokument tekstowy → nazwa  notatki.md  (potwierdź zmianę rozszerzenia). Nagłówek robisz znakiem #: pierwsza linia  # Notatki z nauki.",
            "Pod nagłówkiem  ## Tydzień 0  napisz trzy akapity WŁASNYMI słowami: „Zmienna to…”, „Funkcja to…”, „Pętla to…”. Każdy z przykładem z Twojego gospodarstwa (np. zmienna = tabliczka z wagą krowy). "
            "Nie kopiuj z Asystenta — jeśli nie umiesz napisać sam, jeszcze nie rozumiesz; zapytaj „dlaczego” i spróbuj ponownie.",
            "Dopisz sekcję  ## Czego się nauczyłem w tygodniu 0  z listą (każda linia zaczyna się od myślnika): Środowisko w Mentorze, plik .py i interpreter, ▶ Uruchom / python plik.py, git add/commit/push.",
            "Commit i push:  git add .  →  git commit -m \"dzień 5: notatki — zmienna, funkcja, pętla\"  →  git push. Potem w Mentorze: Sesja → zapisz minuty; Plan → odhacz; Dziennik → 2 zdania.",
            "Sobota: zakładka Quiz → tydzień 0. Potem Checklista → „Po tygodniu 0” — odhacz tylko to, co robisz bez zaglądania do notatek.",
        ],
        "sprawdz": "notatki.md jest na GitHubie i zawiera trzy definicje własnymi słowami z przykładami. Quiz z tygodnia 0 ≥ 60%.",
        "problemy": ["Markdown nie wygląda „ładnie” w edytorze → w PyCharm kliknij ikonę podglądu w prawym górnym rogu; w Notatniku to zwykły tekst — na GitHubie renderuje się sam."],
    },

    # ------------------------------------------------------------------ TYDZIEŃ 1
    "t1z1": {
        "czas": 60,
        "kroki": [
            "Lekcja: zakładka Lekcje → „Zmienne i typy danych” (10 min). Potem prompt „Nowy temat” z tematem „zmienne i typy”.",
            "Plan → „Utwórz plik ćwiczenia” (zmienne.py). Utwórz 5 zmiennych opisujących jedno zwierzę, każda innego typu: imie (str, w cudzysłowie), waga_kg (float, z kropką), wiek_lat (int), rasa (str), czy_zdrowe (bool: True/False).",
            "Dla każdej zmiennej jedna linia:  print(imie, type(imie))  — zobaczysz wartość i typ, np. <class 'str'>.",
            "Eksperyment: dopisz  print(waga_kg + 10)  oraz  print(imie + 10). Drugie wywali TypeError — przeczytaj komunikat, potem popraw na  print(imie + str(10)). Zapisz w notatkach, dlaczego.",
            "„▶ Uruchom” (albo python zmienne.py w terminalu). Commit: „dzień 6: zmienne i typy”.",
        ],
        "sprawdz": "Program wypisuje 5 linii z czterema różnymi typami (str, float, int, bool) i nie kończy się błędem.",
        "problemy": ["NameError: name 'True' is not defined → True i False z wielkiej litery.", "Polskie znaki w nazwach zmiennych (waga_kg, nie waga_kilogramów) — unikaj."],
    },
    "t1z2": {
        "czas": 75,
        "kroki": [
            "Lekcja „print i input” + „Instrukcje warunkowe”. Zapisz w notatkach jedno zdanie: co zwraca input().",
            "kalkulator.py: trzy pytania przez input() W TEJ KOLEJNOŚCI: pierwsza liczba, działanie (+ - * /), druga liczba. Pamiętaj: input() zwraca napis — zamień liczby przez float(). "
            "Program z input() uruchamiasz w Mentorze tak samo: „▶ Uruchom” — w oknie jest pole „Dane dla input()”, każda linia to jedna odpowiedź (np. 6, *, 3).",
            "Cztery gałęzie if/elif/elif/elif — każda dla innego działania — i else wypisujące „Nieznane działanie”. Porównanie działania:  if dzialanie == \"+\":  (podwójny znak równości).",
            "W gałęzi dzielenia, PRZED dzieleniem, sprawdź  if b == 0:  i wypisz komunikat zamiast dzielić. Przetestuj ręcznie: 5 / 0.",
            "Testuj jak tester: wpisz literę zamiast liczby — program się wywali (ValueError). To normalne na tym etapie; zapisz w notatkach, że obsłużysz to w tygodniu 3 (try/except).",
        ],
        "sprawdz": "Cztery działania dają poprawne wyniki; 5 / 0 wypisuje komunikat, nie traceback; „x” jako działanie daje „Nieznane działanie”. „✔ Sprawdź wynik” podaje 6, *, 3 i szuka 18.",
        "problemy": ["Wynik „53” zamiast 8 dla 5+3 → nie zamieniłeś input() na liczbę.", "IndentationError → wszystkie linie pod if wcięte dokładnie 4 spacjami."],
    },
    "t1z3": {
        "czas": 45,
        "kroki": [
            "wiek.py: zapytaj o rok urodzenia (int(input(...))). Pobierz bieżący rok:  import datetime  i  rok = datetime.date.today().year.",
            "Policz wiek = rok − rok_urodzenia. Wypisz f-stringiem:  print(f\"Masz {wiek} lat\").",
            "if wiek >= 18: wypisz „pełnoletni”, else „niepełnoletni”. Dodaj trzeci przypadek elif dla wieku ujemnego (ktoś wpisał rok z przyszłości): „to jeszcze nie ten rok”.",
            "Commit: „dzień 8: wiek i warunki”.",
        ],
        "sprawdz": "Rok 2000 → poprawny wiek i „pełnoletni”; rok 2015 → „niepełnoletni”; rok 2099 → komunikat o przyszłości.",
    },
    "t1z4": {
        "czas": 60,
        "kroki": [
            "litry.py: zapytaj o litry mleka (float) i zawartość tłuszczu w % (float).",
            "Przelicz litry na kilogramy: 1 litr mleka ≈ 1.03 kg → kg = litry * 1.03.",
            "Trzy progi ceny za litr przez if/elif/else: tłuszcz > 4.0 → 2.10 zł; > 3.5 → 1.90; inaczej 1.70. Zwróć uwagę na KOLEJNOŚĆ warunków — od najwyższego progu.",
            "Wypisz: kilogramy (zaokrąglone round(kg, 1)), cenę za litr i wartość dostawy (litry * cena) z dwoma miejscami po przecinku: f\"{wartosc:.2f} zł\".",
            "Test graniczny jak tester: tłuszcz dokładnie 4.0 — który próg? Czy to zgodne z zamiarem (> czy >=)? Zapisz decyzję w komentarzu nad if-em.",
        ],
        "sprawdz": "Dla 500 l i 4.2% → ok. 515 kg, 2.10 zł/l, 1050.00 zł. Dla 3.5% → 1.70 (bo > 3.5 jest fałszywe).",
        "problemy": ["Progi w złej kolejności (najpierw > 3.5) → wszystko powyżej 3.5 dostaje 1.90. Pierwszy prawdziwy warunek wygrywa."],
    },
    "t1z5": {
        "czas": 90,
        "kroki": [
            "Bez nowej teorii. Plik bmi.py. Dwa input(): wzrost w metrach (float, z kropką: 1.80) i waga w kg.",
            "BMI = waga / (wzrost * wzrost). Kategorie if/elif/else: < 18.5 niedowaga; < 25 norma; < 30 nadwaga; else otyłość. Wypisz BMI z jednym miejscem po przecinku i kategorię.",
            "Obsługa błędnego wpisu bez try/except (to tydzień 3): sprawdź if-em, czy wzrost > 0 i waga > 0 — jeśli nie, wypisz „Podaj wartości większe od zera” i NIE licz BMI. "
            "Wskazówka: najpierw walidacja, potem obliczenie — jak w każdym programie, który dostaje dane od człowieka.",
            "Testuj jak tester i zapisz wyniki w notatkach jako tabelę: wzrost, waga, oczekiwana kategoria, co wyszło. Minimum 5 przypadków, w tym wzrost 0 i wzrost podany w cm (180 → BMI ~0.002 — program „działa”, ale wynik bez sensu; dodaj ostrzeżenie if wzrost > 3).",
            "Recenzja: „przejrzyj @bmi.py jak cierpliwy mentor”. Wdróż uwagi. Commit: „dzień 10: kalkulator BMI”. Push. Odhacz. Sobota: quiz z tygodnia 1.",
        ],
        "sprawdz": "1.80 / 75 → 23.1, norma. 1.80 / 50 → niedowaga. 0 / 75 → komunikat. 180 / 75 → ostrzeżenie o jednostkach.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 2
    "t2z1": {
        "czas": 45,
        "kroki": [
            "Lekcja „Pętle for i while”. Zapisz w notatkach: range(1, 11) daje 1…10 — dlaczego 11?",
            "tabliczka.py: pętla  for i in range(1, 11):  i w środku  print(f\"{i} x 7 = {i * 7}\")  — najpierw tabliczka dla jednej liczby.",
            "Wersja pełna: pętla w pętli — zewnętrzna po a (1–10), wewnętrzna po b (1–10), print(f\"{a} x {b} = {a*b}\"). Po wewnętrznej pętli wypisz pustą linię print(), żeby oddzielić bloki.",
            "Wersja tabelki (opcjonalnie): print(f\"{a*b:4}\", end=\"\") w wewnętrznej, print() w zewnętrznej — zobaczysz siatkę 10×10. Zapytaj Asystenta, co robi end=\"\" i :4.",
        ],
        "sprawdz": "Wypisanych 100 działań (lub siatka 10×10), ostatnie to 10 x 10 = 100.",
    },
    "t2z2": {
        "czas": 60,
        "kroki": [
            "Lekcja „Listy”. lista_zakupow.py: zacznij od listy 5 napisów: zakupy = [\"pasza\", \"gwoździe\", ...].",
            "Funkcji jeszcze nie znasz — zrób pętlę  while True:  z menu: wypisz „1 dodaj, 2 usuń, 3 wypisz, 0 koniec”, wczytaj wybór input().",
            "1: input() nazwy → zakupy.append(nazwa). 2: input() nazwy → if nazwa in zakupy: zakupy.remove(nazwa) else komunikat „nie ma na liście”. 3: for nr, produkt in enumerate(zakupy, start=1): print(nr, produkt). 0: break.",
            "Przetestuj: usuń coś, czego nie ma. Dodaj pusty napis (sam Enter) — co się dzieje? Dodaj if, który nie pozwala dodać pustego.",
        ],
        "sprawdz": "Menu działa w pętli; usunięcie nieistniejącego produktu daje komunikat, nie błąd; wypisanie numeruje od 1.",
        "problemy": ["ValueError: list.remove(x): x not in list → zapomniałeś sprawdzić „in” przed remove."],
    },
    "t2z3": {
        "czas": 60,
        "kroki": [
            "suma.py: pusta lista  liczby = []  i pętla while True, która pyta o liczbę (float), a przy 0 → break; inaczej liczby.append(x).",
            "Po pętli: if len(liczby) == 0: wypisz „nic nie podano” — inaczej dzielenie przez zero przy średniej. To Twój pierwszy świadomy przypadek brzegowy.",
            "Wypisz sumę (sum(liczby)), średnią (sum/len) i maksimum (max(liczby)). Potem zrób to samo BEZ sum() i max(): własną pętlą for z akumulatorem suma += x i porównaniem if x > najwieksza.",
            "Zapisz w notatkach: czym jest akumulator (zmienna, która „zbiera” wynik w pętli).",
        ],
        "sprawdz": "Dane 5, 10, 15, 0 → suma 30, średnia 10, max 15. Od razu 0 → komunikat, nie ZeroDivisionError.",
    },
    "t2z4": {
        "czas": 45,
        "kroki": [
            "Lekcja „Napisy i ich metody”. napisy.py: tekst = input(\"Wpisz zdanie: \").strip().",
            "Wypisz: tekst.upper(), tekst[::-1] (od tyłu), len(tekst).",
            "Samogłoski: licznik = 0; for litera in tekst.lower(): if litera in \"aeiouyąęó\": licznik += 1. Wypisz licznik.",
            "Dodatkowo: liczba słów  len(tekst.split())  i najdłuższe słowo (pętla po tekst.split() z porównaniem len).",
            "Pułapka do sprawdzenia: wpisz zdanie ze spacjami na początku — czy strip() pomógł? Usuń strip() i zobacz różnicę w len().",
        ],
        "sprawdz": "„Krowa je trawę” → KROWA JE TRAWĘ, ęwart ej aworK, 14 znaków (ze spacjami), 5 samogłosek (o, a, e, a, ę), 3 słowa, najdłuższe „Krowa” lub „trawę” (oba mają 5 liter — Twój program wybierze pierwsze lub ostatnie; zapisz w notatkach, które i dlaczego).",
    },
    "t2z5": {
        "czas": 90,
        "kroki": [
            "zgadnij.py: import random; sekret = random.randint(1, 100); proby = 0.",
            "Pętla while True: wczytaj zgadywaną liczbę (int), proby += 1. if < sekret: „za mało”; elif > sekret: „za dużo”; else: wypisz „Brawo, w {proby} próbach” i break.",
            "Ranking: PRZED pętlą gry lista  wyniki = []  i zewnętrzna pętla „czy grasz jeszcze raz? (t/n)”. Po każdej grze wyniki.append(proby); wyniki.sort(); wypisz 3 najlepsze: wyniki[:3].",
            "Przypadek brzegowy: liczba spoza 1–100 → komunikat i NIE licz próby (continue przed proby += 1 albo if z pominięciem). Litera zamiast liczby → na razie program padnie; zapisz w notatkach jako „do naprawy w tygodniu 3”.",
            "Recenzja Asystenta, poprawki, commit „dzień 15: gra zgadnij liczbę”, push, odhacz. Sobota: quiz z tygodnia 2 i README do gry (co robi, jak uruchomić, przykładowa rozgrywka).",
        ],
        "sprawdz": "Da się wygrać i zagrać ponownie; ranking pokazuje najmniejsze liczby prób jako pierwsze; 0 lub 150 nie zwiększa licznika prób.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 3
    "t3z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Funkcje”. funkcje.py. Każda funkcja: def nazwa(argumenty): → docstring w \"\"\" \"\"\" → ciało → return. ŻADNEGO input() ani print() w środku — funkcja zwraca, program główny wypisuje.",
            "pole_prostokata(a, b) → a * b.  czy_parzysta(n) → n % 2 == 0 (zwraca bool).  maksimum(lista) → własna pętla z akumulatorem, bez max().  odwroc(napis) → napis[::-1].  silnia(n) → pętla for mnożąca od 1 do n.",
            "Na dole pliku blok wywołań: print(pole_prostokata(3, 4)), print(czy_parzysta(7)) itd. Potem spróbuj: help(silnia) — zobaczysz swój docstring.",
            "Przypadki brzegowe w notatkach: silnia(0) powinna dać 1 — czy daje? maksimum([]) — co robi? (Na razie może dać błąd; zapisz.)",
        ],
        "sprawdz": "pole 3×4=12, 7 nieparzyste, maksimum([3,9,2])=9, odwroc(\"kot\")=\"tok\", silnia(5)=120, silnia(0)=1.",
        "problemy": ["Funkcja wypisuje None → masz print zamiast return w środku.", "NameError przy wywołaniu → wywołanie jest wyżej niż def; definicja musi być przed użyciem."],
    },
    "t3z2": {
        "czas": 60,
        "kroki": [
            "Lekcja „Słowniki i krotki”. slownik.py: wagi = {\"Krasula\": 612, \"Mućka\": 580}.",
            "Cztery funkcje: dodaj(wagi, imie, waga) (wagi[imie] = waga), zmien (to samo, ale najpierw if imie in wagi), usun (del wagi[imie] po sprawdzeniu), wypisz_posortowane (for imie, waga in sorted(wagi.items(), key=lambda p: p[1])).",
            "Menu w pętli jak w liście zakupów, ale operacje wołają funkcje. Zapytaj Asystenta o lambda, jeśli nie rozumiesz key= — albo najpierw zrób wersję bez sortowania.",
            "Test: usuń zwierzę, którego nie ma → komunikat, nie KeyError. Dodaj drugi raz to samo imię → co się dzieje ze starą wagą? Zapisz.",
        ],
        "sprawdz": "Wypisanie posortowane rosnąco po wadze; brak KeyError przy nieistniejącym imieniu.",
    },
    "t3z3": {
        "czas": 45,
        "kroki": [
            "Lekcja „Obsługa błędów try / except”. bledy.py: funkcja wczytaj_liczbe(komunikat), która w pętli while True próbuje float(input(komunikat)) w bloku try i zwraca wynik; except ValueError: print(\"To nie liczba\") i pętla kręci się dalej.",
            "Użyj jej: a = wczytaj_liczbe(\"Pierwsza: \"), b = wczytaj_liczbe(\"Druga: \"). Dzielenie a / b w try z except ZeroDivisionError.",
            "Wróć do kalkulator.py, bmi.py i zgadnij.py z poprzednich tygodni: zamień input() na wczytaj_liczbe(). Masz ten sam kod w 3 plikach — zapisz w notatkach, że to problem (rozwiążesz modułem w tygodniu 5).",
            "Eksperyment: zamień except ValueError na gołe except: i w try zrób literówkę w nazwie zmiennej. Zobacz, jak błąd znika — i dlaczego to źle. Przywróć ValueError.",
        ],
        "sprawdz": "Litera zamiast liczby → komunikat i ponowne pytanie, program nie kończy się. Dzielenie przez 0 → komunikat.",
    },
    "t3z4": {
        "czas": 45,
        "kroki": [
            "Lekcja „Moduły random i datetime”. losowanie.py: lista 8 imion zwierząt.",
            "import random; do_kontroli = random.sample(stado, 3) — trzy RÓŻNE (sample), nie choice trzy razy (mógłby się powtórzyć; sprawdź to doświadczalnie w pętli).",
            "import datetime; dzis = datetime.date.today(); termin = dzis + datetime.timedelta(days=7). Wypisz termin.strftime(\"%d.%m.%Y\") i dzień tygodnia: termin.strftime(\"%A\").",
            "Dodatkowo: policz, ile dni zostało do 1 stycznia przyszłego roku (datetime.date(dzis.year + 1, 1, 1) - dzis).days.",
        ],
        "sprawdz": "Trzy różne imiona i data za tydzień w formacie DD.MM.RRRR.",
    },
    "t3z5": {
        "czas": 90,
        "kroki": [
            "menedzer_zadan.py. Struktura danych: lista słowników, każde zadanie {\"tytul\": str, \"zrobione\": False}. Zacznij od pustej listy zadania = [].",
            "Funkcje (każda z docstringiem, bez input/print w środku): dodaj(zadania, tytul), usun(zadania, nr), oznacz(zadania, nr), lista_tekstem(zadania) → zwraca napis z numeracją i [x]/[ ].",
            "Funkcja menu() z pętlą while True: wypisuje opcje, wczytuje wybór przez wczytaj_liczbe (skopiuj z bledy.py), woła odpowiednią funkcję, wypisuje wynik. 0 kończy.",
            "Walidacja numeru zadania: nr poza zakresem → komunikat, nie IndexError. Pusty tytuł → nie dodawaj.",
            "Na dole: if __name__ == \"__main__\": menu(). Zapytaj Asystenta, po co ta linia (przyda się w tygodniu 7 przy testach).",
            "Recenzja → poprawki → commit „dzień 20: menedżer zadań” → push → odhacz. Sobota: quiz tygodnia 3, README, i CHECKLISTA etapu 1 — uczciwie.",
        ],
        "sprawdz": "Dodanie, oznaczenie i usunięcie działają; zły numer i litera nie wywalają programu; każda operacja to osobna funkcja.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 4
    "t4z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Git: gałęzie, diff, log, cofanie, pull request”.",
            "W terminalu projektu:  git status  (ma być czysto — jeśli nie, zrób commit).  git checkout -b feature/csv  → „Switched to a new branch”. Sprawdź:  git branch  (gwiazdka przy aktywnej).",
            "Zrób zmianę: utwórz plik stado.csv z nagłówkiem nr,imie,rasa,waga i 4 wierszami danych. Zobacz:  git status  → nowy plik;  git diff  (pusty dla nowych plików — dlaczego? zapytaj) → git add stado.csv → git diff --staged (teraz widać).",
            "Commit na gałęzi:  git commit -m \"feature: dane stada w CSV\" . Wyślij gałąź:  git push -u origin feature/csv.",
            "Na GitHubie pojawi się żółty pasek „Compare & pull request” → kliknij → tytuł, opis (co i po co) → Create pull request. Obejrzyj zakładkę „Files changed” — tak koledzy będą oglądać Twój kod. → „Merge pull request” → Confirm.",
            "Lokalnie:  git checkout main  →  git pull  → plik stado.csv jest na main.  git log --oneline --graph  — zobacz rozgałęzienie i scalenie.",
        ],
        "sprawdz": "git log na main pokazuje commit z gałęzi i commit „Merge pull request”. Na GitHubie PR ma status Merged (fioletowy).",
        "problemy": ["„Your branch is behind” → git pull.", "Konflikt (CONFLICT) → nie panikuj: otwórz plik, usuń znaczniki <<<<<<< ======= >>>>>>> zostawiając właściwą wersję, git add, git commit."],
    },
    "t4z2": {
        "czas": 45,
        "kroki": [
            "Lekcja „Pliki: open, read, write, with”. zapis.py: lista 5 imion.",
            "Wersja 1 (bez with): f = open(\"stado.txt\", \"w\", encoding=\"utf-8\"); pętla f.write(imie + \"\\n\"); f.close(). Potem f = open(\"stado.txt\", encoding=\"utf-8\"); for linia in f: print(linia.strip()); f.close().",
            "Wersja 2 (z with): to samo w blokach  with open(...) as f:  — bez close(). Porównaj: która wersja zamknie plik, gdy w pętli wystąpi błąd? (Dopisz w środku 1/0 i sprawdź — a potem usuń).",
            "Otwórz stado.txt w PyCharm i zobacz, co jest w środku. Usuń \"\\n\" z write i zobacz jeszcze raz. Zapisz wniosek.",
        ],
        "sprawdz": "stado.txt ma 5 linii; odczyt wypisuje je bez pustych linii między nimi (strip()).",
    },
    "t4z3": {
        "czas": 60,
        "kroki": [
            "Lekcja „Moduł csv”. stado.csv masz z zadania 1 (nr,imie,rasa,waga + wiersze).",
            "csv_odczyt.py: import csv; with open(\"stado.csv\", encoding=\"utf-8\", newline=\"\") as f: wiersze = list(csv.DictReader(f)). Wypisz wiersze[0] — zobacz, że to słownik z kluczami z nagłówka.",
            "wagi = [float(w[\"waga\"]) for w in wiersze]  (to list comprehension — krótszy zapis pętli; zapytaj Asystenta, jeśli nowe). Średnia = sum/len. Wypisz z 1 miejscem po przecinku.",
            "Dodatkowo: wypisz imię najcięższego (max(wiersze, key=lambda w: float(w[\"waga\"]))[\"imie\"]) i liczbę zwierząt każdej rasy (słownik licznikowy z pętli).",
            "Zepsuj dane: w jednym wierszu wpisz „abc” jako wagę → ValueError. Obsłuż: pomiń wiersz z komunikatem, nie przerywaj.",
        ],
        "sprawdz": "Średnia liczona poprawnie; wiersz ze złą wagą jest pomijany z ostrzeżeniem.",
    },
    "t4z4": {
        "czas": 45,
        "kroki": [
            "git status → czysto. Otwórz zapis.py i skasuj połowę kodu (celowo). git status → „modified”.",
            "Sposób 1:  git checkout -- zapis.py  → plik wraca do stanu z ostatniego commita. Zmiany przepadły BEZPOWROTNIE. Otwórz i sprawdź.",
            "Zepsuj ponownie. Sposób 2:  git stash  → zmiany „odłożone na półkę”, plik czysty.  git stash list  → widzisz wpis.  git stash pop  → zmiany wracają. Teraz dopiero git checkout -- zapis.py.",
            "Zapytaj Asystenta: „wytłumacz różnicę między git checkout -- plik a git stash” (Offline: /temat git). Zapisz w notatkach: kiedy użyć którego.",
            "Dodatkowo: zrób commit z literówką w opisie i popraw go:  git commit --amend -m \"nowy opis\"  (tylko dla commitów, których jeszcze nie wypchnąłeś!).",
        ],
        "sprawdz": "W notatkach masz 2 zdania: checkout -- kasuje zmiany, stash odkłada i przywraca. git stash list jest pusty na koniec.",
    },
    "t4z5": {
        "czas": 90,
        "kroki": [
            "dziennik_stada.py. Funkcje: wczytaj(sciezka) → lista słowników z CSV (waga jako float); zapisz_zwierze(sciezka, nr, imie, rasa, waga) → dopisuje wiersz (tryb \"a\", csv.writer, newline=\"\"); statystyki(zwierzeta) → zwraca słownik {liczba, srednia, najciezsze}; po_rasie(zwierzeta, rasa) → lista.",
            "Menu w pętli: 1 dodaj zwierzę (z walidacją wagi > 0), 2 statystyki, 3 szukaj po rasie (bez względu na wielkość liter: .lower() po obu stronach), 0 koniec. Każdy wybór woła funkcję i wypisuje wynik.",
            "Przypadki brzegowe: pusty plik (tylko nagłówek) → statystyki nie dzielą przez zero; brak pliku → utwórz go z nagłówkiem przy pierwszym zapisie (try FileNotFoundError).",
            "Zrób to na gałęzi feature/dziennik i scal przez pull request — jak w zadaniu 1. Recenzja, commit, push, odhacz. Sobota: quiz 4, README.",
        ],
        "sprawdz": "Po dodaniu 2 zwierząt plik ma 2 nowe wiersze (sprawdź w PyCharm), statystyki się zgadzają, szukanie „hf” znajduje „HF”.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 5
    "t5z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Klasy i obiekty”. zwierze.py: class Zwierze: z __init__(self, imie, rasa, waga) ustawiającym self.imie, self.rasa, self.waga.",
            "Metoda opis(self) → zwraca f\"{self.imie} ({self.rasa}), {self.waga} kg\". Metoda przybierz(self, kg) → self.waga += kg.",
            "Na dole: 3 obiekty (krasula = Zwierze(\"Krasula\", \"HF\", 612) …), wywołaj przybierz na jednym, wypisz opisy wszystkich w pętli po liście [krasula, mucka, laciata].",
            "Eksperyment: wypisz krasula — zobaczysz <__main__.Zwierze object at 0x…>. Dodaj metodę __str__(self) zwracającą opis() i wypisz ponownie. Zapytaj Asystenta, co się zmieniło.",
        ],
        "sprawdz": "print(krasula) wypisuje czytelny opis; po przybierz(8) waga w opisie jest o 8 większa.",
        "problemy": ["TypeError: opis() takes 0 positional arguments but 1 was given → brak self w def opis(self)."],
    },
    "t5z2": {
        "czas": 60,
        "kroki": [
            "Lekcja „Podział kodu na moduły”. Nowy folder menedzer/ w projekcie. Trzy pliki: zadania.py (funkcje dodaj/usun/oznacz/lista_tekstem — przenieś z tygodnia 3), plik.py (zapisz(zadania, sciezka) i wczytaj(sciezka) do pliku JSON: import json; json.dump / json.load), main.py (menu i if __name__ == \"__main__\":).",
            "W main.py:  from zadania import dodaj, usun, oznacz, lista_tekstem  oraz  from plik import zapisz, wczytaj. Przy starcie wczytaj z zadania.json (jeśli jest), przy wyjściu zapisz.",
            "Uruchom: python main.py z folderu menedzer/. Dodaj zadanie, wyjdź, uruchom ponownie — zadanie ma zostać.",
            "Test podziału: uruchom  python zadania.py  — nic nie powinno się wypisać (bo nie ma tam kodu startowego). Jeśli coś się wypisuje — przenieś to do main.py.",
        ],
        "sprawdz": "Trzy pliki, każdy z jedną rolą; zadania przeżywają restart programu (plik zadania.json).",
        "problemy": ["ModuleNotFoundError: No module named 'zadania' → uruchamiasz z innego folderu; cd menedzer."],
    },
    "t5z3": {
        "czas": 45,
        "kroki": [
            "Lekcja „venv, pip, requirements.txt, .gitignore”. Mentor ma już SWOJE środowisko kursu (zakładka Środowisko) — teraz tworzysz WŁASNE, w projekcie, bo tak robi się w pracy: "
            "Mój projekt → „Otwórz terminal tutaj” (albo Terminal w PyCharm), w głównym folderze projektu:  python -m venv .venv  (powstanie folder .venv — kilkadziesiąt MB).",
            "Aktywuj:  .venv\\Scripts\\activate  (Windows; jeśli PowerShell odmawia: wpisz  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned , potwierdź T, spróbuj ponownie). Przed ścieżką pojawi się (.venv).",
            "pip install requests  → zobaczysz pobieranie.  pip list  → requests na liście.  pip freeze > requirements.txt  → plik z nazwami i wersjami.",
            "Utwórz .gitignore (plik zaczynający się od kropki) z liniami:  .venv/  ,  __pycache__/  ,  *.pyc . git status → .venv NIE pojawia się na liście. Commit requirements.txt i .gitignore.",
            "PyCharm: Settings → Project → Python Interpreter → upewnij się, że wskazuje .venv\\Scripts\\python.exe (zwykle wykryje sam i zapyta). "
            "Uwaga: przycisk „▶ Uruchom” w Mentorze nadal używa środowiska KURSU (ma requests) — terminal z aktywnym (.venv) używa Twojego. Oba to osobne „szafki” z bibliotekami.",
        ],
        "sprawdz": "git status nie pokazuje .venv; requirements.txt zawiera requests==x.y.z; w terminalu widać (.venv).",
        "problemy": ["pip nie jest rozpoznawany → venv nieaktywny; aktywuj albo użyj  python -m pip install requests."],
    },
    "t5z4": {
        "czas": 60,
        "kroki": [
            "Lekcja „Biblioteka requests i API”. W przeglądarce otwórz: https://api.open-meteo.com/v1/forecast?latitude=51.78&longitude=22.62&daily=temperature_2m_min,temperature_2m_max&timezone=Europe/Warsaw — zobacz surowy JSON. To jest to, co dostanie Twój program.",
            "api.py: import requests; odp = requests.get(url, timeout=10); print(odp.status_code) → 200. dane = odp.json(); print(type(dane)) → dict. print(dane.keys()).",
            "Wypisz 3 pola: dane[\"daily\"][\"time\"][0], dane[\"daily\"][\"temperature_2m_min\"][0], dane[\"daily\"][\"temperature_2m_max\"][0]. Dojdź do nich po kolei, wypisując po drodze print(dane[\"daily\"]) itd.",
            "Obsłuż błędy: try/except requests.exceptions.RequestException (brak internetu — wyłącz Wi‑Fi i sprawdź) i if odp.status_code != 200. Zepsuj URL (literówka) → jaki kod?",
        ],
        "sprawdz": "Wypisana data i dwie temperatury; bez internetu — komunikat, nie traceback.",
    },
    "t5z5": {
        "czas": 90,
        "kroki": [
            "pogoda.py: funkcja pobierz_prognoze(dni=3) → zwraca listę krotek (data, tmin, tmax) z open-meteo (parametr forecast_days=3). Funkcja zapisz_csv(prognoza, sciezka) → dopisuje wiersze z datą pobrania (datetime.date.today()). Funkcja ostrzezenia(prognoza) → lista dat, gdzie tmin < 0.",
            "main: pobierz → wypisz tabelkę → zapisz do pogoda.csv → jeśli ostrzeżenia: wypisz „PRZYMROZEK: daty” wyraźnie (np. wielkimi literami).",
            "Tryb planowania najpierw: w Asystencie „chcę zbudować program pogodowy…” (Offline: /plan pogoda) — wypełnij szkielet PLAN.md, dopiero potem koduj.",
            "Przypadki brzegowe: API nie odpowiada → komunikat i wyjście z kodem 1 (import sys; sys.exit(1)); pogoda.csv nie istnieje → utwórz z nagłówkiem.",
            "requirements.txt aktualny (pip freeze), .gitignore ok, README z instrukcją (venv → pip install -r requirements.txt → python pogoda.py). Commit, push, odhacz. Sobota: quiz 5.",
        ],
        "sprawdz": "Dwa uruchomienia → pogoda.csv ma 6 wierszy z datą pobrania; dla ujemnej tmin pojawia się ostrzeżenie.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 6
    "t6z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Debugowanie: print i debugger PyCharm”. W Asystencie Offline wpisz  /debug  i zgódź się — powstanie cwiczenie_debug.py (62 linie, 3 błędy logiczne). Z Claude Code: „napisz 80-liniowy program z 3 ukrytymi błędami, nie mów jakimi”.",
            "ZANIM uruchomisz: przeczytaj kod i zapisz, jaki wynik przewidujesz (średnia, najcięższe, lista HF). Uruchom. Porównaj.",
            "Debugger: kliknij w szary margines obok pierwszej linii funkcji srednia_waga → czerwona kropka (breakpoint). Prawy przycisk na pliku → Debug 'cwiczenie_debug'. Program zatrzyma się; na dole w „Variables” widzisz wartości. F8 (Step Over) wykonuje linię po linii — patrz, jak zmienia się suma. Kiedy zachowuje się inaczej niż myślisz — masz błąd.",
            "Powtórz dla najciezsze i po_rasie. Napraw każdy błąd, uruchom ponownie, aż wynik zgadza się z przewidywaniem. Dopiero potem /rozwiazanie.",
            "W notatkach: 3 błędy, jak każdy znalazłeś (co widziałeś w Variables), ile czasu zajął.",
        ],
        "sprawdz": "Program daje poprawne: średnia 570.5, najcięższe Łaciata, HF: Krasula, Łaciata. W notatkach opis 3 błędów.",
    },
    "t6z2": {
        "czas": 60,
        "kroki": [
            "Na GitHubie wyszukaj „python calculator beginner” albo „python todo cli” — wybierz MAŁE repozytorium (2–5 plików, < 300 linii). Alternatywa: repo kolegi z kursu.",
            "Sklonuj do osobnego folderu (NIE do nauka-python):  cd $HOME\\Documents  →  git clone <adres .git>  → otwórz w PyCharm.",
            "Czytaj od pliku startowego (main.py / nazwa repo). Dla każdego pliku w notatki.md: nazwa, co robi w 1–2 zdaniach, które funkcje woła z innych plików. Rysuj strzałki na kartce, jeśli pomaga.",
            "Uruchom program. Znajdź jedną rzecz, którą zrobiłbyś inaczej (nazwa, brak docstringa, powtórzony kod) — zapisz z uzasadnieniem. Zapytaj Asystenta: „myślę, że ten kod robi… @plik.py” (sprawdzenie zrozumienia).",
        ],
        "sprawdz": "notatki.md ma sekcję „Cudzy kod: <nazwa repo>” z opisem każdego pliku i jedną uwagą krytyczną.",
    },
    "t6z3": {
        "czas": 75,
        "kroki": [
            "Lekcja „README, docstringi, refaktoryzacja”. Otwórz bmi.py. Poproś o recenzję: „przejrzyj @bmi.py”. Zapisz uwagi.",
            "Refaktor bmi.py: funkcja oblicz_bmi(wzrost, waga) → float; kategoria(bmi) → str; wczytaj_liczbe z tygodnia 3; main() z pętlą pytań; if __name__ == \"__main__\". Docstring do każdej. Zachowanie IDENTYCZNE — sprawdź ręcznie 5 przypadków z notatek z tygodnia 1 przed i po.",
            "Refaktor zgadnij.py: losuj(), ocen_probe(sekret, proba) → \"za mało\"/\"za dużo\"/\"trafiony\", graj() → zwraca liczbę prób, ranking(wyniki). Teraz litera zamiast liczby już nie wywala (wczytaj_liczbe).",
            "Jeszcze raz recenzja obu plików. Commit: „refaktor: bmi i zgadywanka z funkcjami”.",
        ],
        "sprawdz": "Oba programy działają jak wcześniej, ale każda czynność jest funkcją z docstringiem; żaden input() w funkcjach liczących.",
    },
    "t6z4": {
        "czas": 60,
        "kroki": [
            "Dla każdego z 6 projektów (bmi, zgadnij, menedżer, dziennik stada, pogoda, zwierze) plik README.md w folderze projektu (jeśli projekt to jeden plik — README obok niego, nazwany README_bmi.md, albo zrób foldery już teraz, patrz zadanie 5).",
            "Szablon: # Nazwa → jedno zdanie co robi → ## Uruchomienie (komendy: venv, pip install -r, python plik.py) → ## Przykład (wklejony fragment z konsoli w bloku ``` ```) → ## Czego się nauczyłem (2 punkty).",
            "Zrzut ekranu z konsoli: uruchom program, Win+Shift+S, zaznacz, zapisz do folderu projektu jako przyklad.png, w README: ![przykład](przyklad.png).",
            "Obejrzyj README na GitHubie po pushu — czy ktoś obcy zrozumiałby w 30 sekund?",
        ],
        "sprawdz": "6 README na GitHubie, każde z sekcją Uruchomienie i przykładem.",
    },
    "t6z5": {
        "czas": 90,
        "kroki": [
            "Nowe repozytorium python-projekty (GitHub → New). Sklonuj. W środku folder na projekt: 01-bmi/, 02-zgadnij/, 03-menedzer/, 04-dziennik-stada/, 05-pogoda/, 06-zwierze/ — do każdego przenieś pliki, README, requirements.txt, jeśli są.",
            "Główne README.md: tytuł, 2 zdania o Tobie (15 lat gospodarstwa, uczysz się Pythona pod QA), tabela projektów: nazwa | co robi | technologie | link do folderu. Jeden .gitignore na całe repo.",
            "Każdy folder uruchom ponownie od zera (cd, python plik.py) — czy działa po przeniesieniu? Ścieżki do plików CSV mogły się zepsuć.",
            "Ocena „oczami rekrutera”: prompt z zakładki Prompty. Offline: sprawdź listę ręcznie — README główny, README w każdym folderze, brak .venv i __pycache__ w repo, opisy commitów po polsku z sensem. Wdróż 3 poprawki.",
            "Commit, push. Link do python-projekty wpisz do notatek — to zalążek portfolio. Sobota: quiz 6 i CHECKLISTA etapu 2.",
        ],
        "sprawdz": "github.com/Ty/python-projekty ma 6 folderów i główne README z tabelą; wszystko uruchamia się po sklonowaniu na czysto.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 7
    "t7z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „pytest: assert, nazewnictwo, uruchamianie”. W swoim venv: (.venv) pip install pytest; pip freeze > requirements.txt. (Środowisko kursu w Mentorze ma już pytest — „✔ Sprawdź wynik” uruchomi nim Twoje testy.)",
            "Obok funkcje.py utwórz test_funkcje.py. Na górze: from funkcje import pole_prostokata, czy_parzysta, maksimum, odwroc, silnia. (Jeśli funkcje.py ma printy na najwyższym poziomie — wykonają się przy imporcie; przenieś je pod if __name__ == \"__main__\".)",
            "5 funkcji testowych: def test_pole_3_na_4(): assert pole_prostokata(3, 4) == 12 … po jednej na funkcję. Nazwa testu mówi, CO sprawdza.",
            "Uruchom:  pytest -v  → 5 zielonych PASSED. Zepsuj funkcję silnia (zwróć n zamiast wyniku) → pytest → czerwony FAILED z pokazaniem obu wartości. Przeczytaj ten komunikat uważnie — to Twoje narzędzie pracy. Napraw.",
            "Dodaj test przypadku brzegowego: silnia(0) == 1 i maksimum([]) — co ma zwrócić? Zdecyduj (None? błąd?), napisz test, dopasuj funkcję.",
        ],
        "sprawdz": "pytest -v pokazuje ≥ 6 PASSED; celowe zepsucie funkcji daje FAILED.",
        "problemy": ["pytest: command not found → venv nieaktywny.", "ModuleNotFoundError: funkcje → uruchamiasz pytest z innego folderu; cd do folderu z plikami."],
    },
    "t7z2": {
        "czas": 45,
        "kroki": [
            "Lekcja „parametrize i fixtures”. test_bmi.py: from bmi import oblicz_bmi, kategoria (z refaktoru tygodnia 6).",
            "@pytest.mark.parametrize(\"wzrost, waga, oczekiwana\", [(1.80, 50, \"niedowaga\"), (1.80, 60, \"norma\"), (1.80, 75, \"norma\"), (1.80, 85, \"nadwaga\"), (1.80, 100, \"otyłość\"), (1.60, 47, \"niedowaga\")]) nad def test_kategoria(wzrost, waga, oczekiwana): assert kategoria(oblicz_bmi(wzrost, waga)) == oczekiwana.",
            "pytest -v → 6 linii test_kategoria[1.8-50-niedowaga] … Każdy przypadek osobno. Dodaj przypadek GRANICZNY: BMI dokładnie 25.0 (wzrost 2.0, waga 100) — norma czy nadwaga? Sprawdź, co mówi Twoja funkcja, i czy to zgodne z zamiarem.",
        ],
        "sprawdz": "7 parametryzowanych przypadków, wszystkie zielone, w tym graniczny.",
    },
    "t7z3": {
        "czas": 60,
        "kroki": [
            "W folderze menedzer/: test_zadania.py. Fixture: @pytest.fixture def menedzer(): z = []; dodaj(z, \"nakarmić\"); dodaj(z, \"zważyć\"); dodaj(z, \"szczepienie\"); return z.",
            "4 testy przyjmujące menedzer jako argument: test_dodaj_zwieksza_liste(menedzer) (len == 4 po dodaniu), test_usun(menedzer), test_oznacz_ustawia_zrobione(menedzer), test_lista_tekstem_zawiera_numeracje(menedzer).",
            "Sprawdź izolację: w pierwszym teście dodaj zadanie — czy drugi test widzi 3 czy 4? (Powinien 3 — fixture tworzy świeżą listę dla każdego testu.) Zapisz w notatkach, dlaczego to ważne.",
            "Przenieś fixture do conftest.py w tym samym folderze — testy nadal działają bez importu. Zapytaj Asystenta, jak pytest ją znajduje.",
        ],
        "sprawdz": "pytest -v: 4 PASSED; fixture w conftest.py; każdy test zaczyna z 3 zadaniami.",
    },
    "t7z4": {
        "czas": 60,
        "kroki": [
            "W Asystencie Offline: „Wprowadź do @dziennik_stada.py jeden ukryty błąd. Nie mów jaki.” → zgoda → powstaje dziennik_stada_z_bledem.py (oryginał nietknięty). Z Claude Code: ten sam prompt na kopii pliku.",
            "NIE czytaj kodu z błędem. Pisz testy do ORYGINALNYCH funkcji (test_dziennik.py), importując z pliku z błędem: from dziennik_stada_z_bledem import statystyki, po_rasie, wczytaj. Użyj tmp_path do testowego CSV: sciezka = tmp_path / \"stado.csv\"; sciezka.write_text(\"nr,imie,rasa,waga\\n1,A,HF,600\\n2,B,HF,500\\n\").",
            "Testy: liczba == 2, średnia == 550, najcięższe == A, po_rasie(\"hf\") ma 2, pusta lista → statystyki bez błędu. Uruchom — który test jest czerwony? Ten wskazuje błąd.",
            "Dopiero teraz otwórz plik, znajdź linię, napraw, pytest zielony. /rozwiazanie dla potwierdzenia. W notatkach: jaki błąd, który test go złapał, jakiego testu brakowało, jeśli żaden nie złapał.",
        ],
        "sprawdz": "Co najmniej jeden test był czerwony przed naprawą i jest zielony po; w notatkach opis.",
    },
    "t7z5": {
        "czas": 90,
        "kroki": [
            "Cel: ≥ 15 testów łącznie dla menedżera zadań i dziennika stada (test_zadania.py + test_dziennik.py). Lista przypadków brzegowych do pokrycia: pusta lista (statystyki, lista_tekstem), zły typ (dodaj(z, 123) — co ma się stać? zdecyduj i przetestuj), duplikat (dodanie tego samego tytułu dwa razy), zły numer (usun(z, 99) → brak zmian, nie błąd), wiersz CSV z błędną wagą → pominięty.",
            "Każdy test: jedna rzecz, nazwa mówiąca co sprawdza, assert z konkretną wartością. Testy wyjątków: with pytest.raises(ValueError): … — jeśli zdecydujesz, że funkcja ma rzucać.",
            "pytest -v z folderu głównego: wszystkie zielone. pytest --collect-only | wc -l (PowerShell: Measure-Object) → policz, ile masz.",
            "Recenzja testów: „przejrzyj @test_dziennik.py”. Commit „dzień 35: 15 testów z przypadkami brzegowymi”. Sobota: quiz 7.",
        ],
        "sprawdz": "pytest -v wypisuje ≥ 15 PASSED; co najmniej 5 testów dotyczy przypadków brzegowych.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 8
    "t8z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Selenium WebDriver i lokatory”. (.venv) pip install selenium; pip freeze > requirements.txt. Zainstalowany Chrome (Selenium 4 sam pobierze sterownik).",
            "saucedemo.py: from selenium import webdriver; from selenium.webdriver.common.by import By; driver = webdriver.Chrome(); driver.get(\"https://www.saucedemo.com\"). Uruchom — otworzy się Chrome z napisem „Chrome is being controlled by automated test software”. Zamknie się po końcu skryptu (dodaj input(\"Enter…\") na końcu, żeby zobaczyć).",
            "W Chrome na saucedemo: F12 → zakładka Elements → kliknij strzałkę (lewy górny róg) → kliknij pole login → zobacz id=\"user-name\". Tak samo hasło i przycisk.",
            "driver.find_element(By.ID, \"user-name\").send_keys(\"standard_user\"); …password → \"secret_sauce\"; …login-button → .click(). driver.save_screenshot(\"po_logowaniu.png\"); driver.quit().",
            "Sprawdź po_logowaniu.png — widać sklep? Zmień hasło na błędne i zrób drugi zrzut — widać czerwony komunikat?",
        ],
        "sprawdz": "Skrypt loguje się bez klikania ręcznego i zostawia zrzut ekranu ze sklepem.",
        "problemy": ["SessionNotCreatedException / wersja sterownika → zaktualizuj Chrome i selenium (pip install -U selenium).", "Okno zamyka się natychmiast → to normalne po quit(); dodaj time.sleep(3) przed quit, żeby zobaczyć (tylko do podglądu!)."],
    },
    "t8z2": {
        "czas": 60,
        "kroki": [
            "lokatory.py: driver.get(\"https://the-internet.herokuapp.com/login\"). Elementy: pole username, pole password, przycisk Login, nagłówek h2, link „Elemental Selenium” w stopce.",
            "Dla każdego znajdź trzema sposobami: By.ID (jeśli ma id), By.CSS_SELECTOR (#username, button[type='submit'], h2, a[href*='elemental']), By.XPATH (//input[@id='username'], //button[contains(., 'Login')], //h2).",
            "Wypisz dla każdego: element.tag_name, element.text lub get_attribute(\"placeholder\"). Jeśli trzy sposoby dają ten sam element — tekst się zgadza.",
            "Sprawdzaj selektory PRZED kodem w konsoli Chrome (F12 → Console): document.querySelector(\"#username\") dla CSS, $x(\"//h2\") dla XPath. Jeśli null — selektor zły.",
            "W notatkach tabela: element | id | CSS | XPath | który najstabilniejszy i dlaczego.",
        ],
        "sprawdz": "Skrypt wypisuje 5 elementów × 3 sposoby bez NoSuchElementException; tabela w notatkach.",
    },
    "t8z3": {
        "czas": 60,
        "kroki": [
            "Lekcja „WebDriverWait i Page Object Model” (część o Wait). formularz.py: the-internet.herokuapp.com/login → wpisz tomsmith / SuperSecretPassword! → kliknij Login.",
            "Po kliknięciu strona przeładowuje się — komunikat „You logged into a secure area!” pojawia się z opóźnieniem. BEZ time.sleep: from selenium.webdriver.support.ui import WebDriverWait; from selenium.webdriver.support import expected_conditions as EC; wait = WebDriverWait(driver, 10); komunikat = wait.until(EC.visibility_of_element_located((By.ID, \"flash\"))).text.",
            "assert \"secure area\" in komunikat — pierwszy assert w Selenium. Potem wersja z błędnym hasłem i assert \"invalid\" in komunikat.lower().",
            "Eksperyment: ustaw WebDriverWait(driver, 0.01) → TimeoutException. Przeczytaj, zapisz: co się stało i dlaczego sleep(5) nie jest odpowiedzią.",
        ],
        "sprawdz": "Oba scenariusze (dobre i złe hasło) kończą się bez wyjątku, asserty przechodzą, zero time.sleep w pliku.",
    },
    "t8z4": {
        "czas": 75,
        "kroki": [
            "Lekcja — część o POM. Folder meridianbank_tests/ (albo w projekcie MeridianBank, jeśli masz). Jeśli MeridianBank nie istnieje — użyj saucedemo.com z tymi samymi metodami.",
            "pages/login_page.py: class LoginPage z stałymi lokatorów jako krotki (USER = (By.ID, \"…\")), __init__(self, driver) z self.wait = WebDriverWait(driver, 10), open() → driver.get(URL), login(user, haslo) → send_keys + click, error_text() → wait.until(visibility…).text.",
            "pages/__init__.py (pusty plik — żeby folder był pakietem). Skrypt próbny: page = LoginPage(driver); page.open(); page.login(\"zly\", \"zle\"); print(page.error_text()).",
            "Zasada POM: w klasie strony NIE ma assertów; w testach NIE ma find_element. Sprawdź swój kod pod tym kątem.",
        ],
        "sprawdz": "LoginPage ma 3 metody i lokatory w jednym miejscu; skrypt próbny wypisuje komunikat błędu przez page.error_text().",
    },
    "t8z5": {
        "czas": 90,
        "kroki": [
            "conftest.py: fixture driver — tworzy webdriver.Chrome(), yield driver, po teście driver.quit(). (yield zamiast return — zapytaj Asystenta dlaczego.) Opcjonalnie opcje headless: from selenium.webdriver.chrome.options import Options; o = Options(); o.add_argument(\"--headless=new\").",
            "Page Objects: LoginPage (masz), DashboardPage (saldo(), wyloguj(), przejdz_do_przelewu()), TransferPage (wykonaj(odbiorca, kwota), komunikat()). Każda strona: lokatory + akcje, zero assertów.",
            "test_meridianbank.py — 5 testów: test_logowanie_poprawne (po login widać dashboard), test_bledne_haslo (error_text zawiera „invalid”/„błędn”), test_przelew (saldo przed − kwota == saldo po), test_saldo_wyswietla_liczbe, test_wylogowanie (po wyloguj widać formularz logowania). Każdy test: 3–8 linii, czyta się jak scenariusz.",
            "pytest -v: 5 PASSED. Zepsuj jeden lokator w LoginPage → wszystkie testy logowania czerwone → napraw w JEDNYM miejscu. To jest wartość POM — zapisz.",
            "README folderu: jak uruchomić (venv, requirements, pytest), zrzut z konsoli. Commit, push, odhacz. Sobota: quiz 8.",
        ],
        "sprawdz": "5 testów E2E zielonych; żaden test nie zawiera find_element; żadna strona nie zawiera assert.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 9
    "t9z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „Przypadki testowe i bug raporty”. Plik przypadki_testowe.md w repo testów. Tabela Markdown: | ID | Tytuł | Warunki wstępne | Kroki | Oczekiwany wynik | Priorytet |.",
            "10 przypadków dla MeridianBank (lub saucedemo), np. TC-01 logowanie poprawne, TC-02 błędne hasło, TC-03 puste pola, TC-04 przelew poprawny, TC-05 przelew kwoty 0, TC-06 przelew ujemny, TC-07 przelew ponad saldo, TC-08 wylogowanie, TC-09 odświeżenie strony po zalogowaniu (sesja), TC-10 bardzo długa nazwa odbiorcy.",
            "Każdy krok to jedna czynność („1. Wpisz w pole Login: standard_user”), oczekiwany wynik konkretny („saldo 1000,00 zł, komunikat ‘Przelew wysłany’”), nie „działa poprawnie”.",
            "Wykonaj ręcznie 5 z nich na stronie, zapisz wynik w dodatkowej kolumnie Status (PASS/FAIL). FAIL → to materiał na bug raport z zadania 2.",
        ],
        "sprawdz": "10 wierszy tabeli, każdy z krokami numerowanymi i konkretnym oczekiwanym wynikiem; 5 wykonanych ręcznie.",
    },
    "t9z2": {
        "czas": 60,
        "kroki": [
            "Z zadania 1 weź FAIL-e (albo szukaj celowo: wpisz w kwotę przelewu „abc”, „-5”, „0.001”, 1e9; w login spacje; kliknij przycisk dwa razy szybko). Znajdź 3 zachowania, które uznasz za błędne.",
            "bug_raporty.md: szablon z Asystenta (/bugraport) lub z zakładki Prompty. BUG-001…003: tytuł konkretny (co, gdzie, przy jakich danych), środowisko (Windows 11, Chrome wersja — chrome://version), kroki, oczekiwany, rzeczywisty, priorytet, zrzut ekranu (zapisz obok, wstaw ![](bug1.png)).",
            "Ocena: wklej raport do Asystenta z promptem „Ocena bug raportu”. Offline nie ocenia treści — zrób własną listę kontrolną: czy ktoś bez mojej pomocy odtworzy? czy wiadomo, co MIAŁO być? czy wiadomo, na jakiej wersji? Popraw.",
            "Dla jednego buga napisz test Selenium, który go wykrywa (czerwony, bo bug istnieje) — oznacz @pytest.mark.xfail(reason=\"BUG-002\") i zapytaj Asystenta, co to znaczy.",
        ],
        "sprawdz": "3 raporty z pełnymi sekcjami i zrzutami; jeden ma odpowiadający test xfail.",
    },
    "t9z3": {
        "czas": 60,
        "kroki": [
            "Lekcja „GitHub Actions i pytest-html”. W repo testów (lub python-projekty) utwórz foldery .github/workflows/ i plik tests.yml. Treść — z lekcji (checkout, setup-python 3.12, pip install -r requirements.txt, pytest -v). YAML: wcięcia SPACJAMI, dokładnie jak w przykładzie.",
            "Jeśli testy Selenium: dodaj krok instalujący Chrome (uses: browser-actions/setup-chrome@v1) i upewnij się, że fixture driver używa --headless=new (na serwerze nie ma ekranu). Testy jednostkowe z pytest wystarczą na start — Selenium w CI dołóż, gdy jednostkowe są zielone.",
            "Commit i push. Na GitHubie zakładka Actions → zobaczysz uruchomienie (żółte kółko → zielony ptaszek lub czerwony X). Kliknij, rozwiń kroki, czytaj logi — dokładnie jak terminal.",
            "Czerwony? Najczęściej: brak requirements.txt, inna ścieżka do testów (dodaj working-directory), brak Chrome. Popraw, push, patrz ponownie. Zielony = cel.",
        ],
        "sprawdz": "Zakładka Actions pokazuje zielony przebieg dla ostatniego commita.",
        "problemy": ["„No module named pytest” → pytest nie jest w requirements.txt.", "YAML error → sprawdź wcięcia (2 spacje), dwukropki i brak tabulatorów."],
    },
    "t9z4": {
        "czas": 45,
        "kroki": [
            "(.venv) pip install pytest-html; pip freeze > requirements.txt. Lokalnie:  pytest --html=raport.html --self-contained-html  → otwórz raport.html w przeglądarce. Obejrzyj: tabela testów, czasy, szczegóły błędów.",
            "Dodaj raport.html do .gitignore (generowany, nie commitujemy).",
            "W tests.yml zmień krok pytest na: pytest -v --html=raport.html --self-contained-html, a po nim dodaj krok upload-artifact (uses: actions/upload-artifact@v4, with: name: raport, path: raport.html, if: always() — żeby raport był też przy czerwonych testach).",
            "Push → Actions → przebieg → na dole „Artifacts” → pobierz raport.zip → otwórz. To jest raport, który pokażesz na rozmowie.",
        ],
        "sprawdz": "W Actions, sekcja Artifacts, jest „raport”; po pobraniu otwiera się w przeglądarce z listą testów.",
    },
    "t9z5": {
        "czas": 90,
        "kroki": [
            "Nowe repo meridianbank-tests (albo porządek w istniejącym): struktura pages/ (POM), tests/ (test_*.py), conftest.py, requirements.txt, .gitignore, przypadki_testowe.md, bug_raporty.md, .github/workflows/tests.yml.",
            "Dobij do 15+ testów: do 5 E2E dołóż testy formularza (puste pola, zły format kwoty), nawigacji, wylogowania z każdej strony; parametrize dla kilku zestawów danych logowania.",
            "README: opis, jak uruchomić lokalnie, odznaka CI (GitHub → Actions → workflow → ⋯ → Create status badge → wklej Markdown na górę README), link do przypadków testowych i bug raportów, zrzut raportu HTML.",
            "Ostatni push → Actions zielone → odznaka w README zielona. Odhacz. Sobota: quiz 9 i CHECKLISTA etapu 3 — to najważniejsza checklista w programie.",
        ],
        "sprawdz": "README ma zieloną odznakę; repo zawiera ≥ 15 testów, POM, raport HTML w artefaktach, przypadki i bug raporty.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 10
    "t10z1": {
        "czas": 60,
        "kroki": [
            "Lekcja „SQLite i planowanie projektu”. Nowe repo gospodarstwo (Public). Sklonuj, venv, .gitignore, requirements.txt (pusty na razie — sqlite3 jest w Pythonie).",
            "Tryb planowania: Claude Code Shift+Tab → „plan”, prompt „Plan projektu” z zakładki Prompty; Offline: /plan system zarządzania gospodarstwem → szkielet. Wypełnij PLAN.md: cel (1 zdanie), zakres WCHODZI (ewidencja zwierząt, zdarzenia: szczepienie/wycielenie/leczenie, lista zdarzeń po dacie, SQLite, menu konsolowe, potem Flask) i NIE WCHODZI (użytkownicy, logowanie, wykresy — świadomie), struktura plików (baza.py, stado.py, main.py, test_baza.py, test_stado.py, później app.py), kolejność kroków z kryterium „gotowe, gdy…”.",
            "Narysuj tabele: zwierzeta(id, imie, rasa, data_ur, waga) i zdarzenia(id, zwierze_id, data, typ, opis). Zapisz w PLAN.md jako listy. Zapytaj Asystenta: „co to klucz obcy” (zwierze_id wskazuje na zwierzeta.id).",
            "Commit PLAN.md. Od teraz każdy krok = jedna gałąź lub jeden commit opisany jak w planie.",
        ],
        "sprawdz": "PLAN.md ma cel, zakres (z „nie wchodzi”), 5+ plików, kolejność z kryteriami gotowości i dwie tabele.",
    },
    "t10z2": {
        "czas": 75,
        "kroki": [
            "baza.py: polacz(sciezka=\"stado.db\") → connection z CREATE TABLE IF NOT EXISTS dla obu tabel (zdarzenia z FOREIGN KEY(zwierze_id) REFERENCES zwierzeta(id)). Włącz klucze obce: con.execute(\"PRAGMA foreign_keys = ON\").",
            "Funkcje: dodaj_zwierze(con, imie, rasa, data_ur, waga) → zwraca nowe id (cursor.lastrowid); pobierz_zwierzeta(con) → lista krotek; usun_zwierze(con, id); dodaj_zdarzenie(con, zwierze_id, data, typ, opis); pobierz_zdarzenia(con, zwierze_id) → posortowane po dacie. ZAWSZE parametry przez ?, nigdy f-string w SQL.",
            "Skrypt próbny na dole pod if __name__: dodaj 2 zwierzęta, 1 zdarzenie, wypisz. Uruchom dwa razy — czy dane się dublują? (Tak — baza trwa. Usuń stado.db między próbami albo zrób funkcję wyczysc.) Dodaj stado.db do .gitignore.",
            "Obejrzyj bazę: PyCharm → View → Tool Windows → Database → + → Data Source → SQLite → wskaż stado.db. Zobacz tabele i dane.",
        ],
        "sprawdz": "Po skrypcie próbnym w stado.db są 2 zwierzęta i 1 zdarzenie (widać w PyCharm Database); usunięcie zwierzęcia z zdarzeniami daje błąd klucza obcego (zapisz, co z tym zrobisz).",
    },
    "t10z3": {
        "czas": 75,
        "kroki": [
            "stado.py — logika BEZ SQL i BEZ input/print: class Stado z con w __init__. zarejestruj(imie, rasa, data_ur, waga) → walidacja (imie niepuste, waga > 0, data w formacie RRRR-MM-DD przez datetime.date.fromisoformat) → ValueError z komunikatem albo baza.dodaj_zwierze.",
            "dodaj_zdarzenie(zwierze_id, data, typ, opis) → typ tylko z listy TYPY = (\"szczepienie\", \"wycielenie\", \"leczenie\", \"wazenie\") — inaczej ValueError; zwierze_id musi istnieć.",
            "zdarzenia_po_dacie(od, do=None) → lista zdarzeń wszystkich zwierząt w zakresie dat, posortowana; nadchodzace_szczepienia(dni=30) — jeśli ostatnie szczepienie > 365 dni temu.",
            "Zasada: stado.py woła baza.py, nigdy odwrotnie; main.py woła stado.py. Narysuj te trzy klocki ze strzałkami w PLAN.md.",
        ],
        "sprawdz": "Stado(con).zarejestruj(\"\", \"HF\", \"2020-01-01\", 600) rzuca ValueError; poprawne dane zwracają id; zdarzenie z typem „inne” rzuca ValueError.",
    },
    "t10z4": {
        "czas": 75,
        "kroki": [
            "conftest.py: @pytest.fixture def con(tmp_path): c = baza.polacz(tmp_path / \"test.db\"); yield c; c.close(). Każdy test ma CZYSTĄ bazę w katalogu tymczasowym — nigdy Twój stado.db.",
            "test_baza.py (≥ 6): dodanie zwraca rosnące id, pobierz po dodaniu ma 1 element, usunięcie usuwa, zdarzenia posortowane po dacie, zdarzenie dla nieistniejącego zwierzęcia → błąd (sqlite3.IntegrityError), pusta baza → pusta lista.",
            "test_stado.py (≥ 8): walidacje (puste imię, waga 0, zła data, zły typ zdarzenia) przez pytest.raises(ValueError), zdarzenia_po_dacie zwraca tylko zakres, nadchodzace_szczepienia dla zwierzęcia bez szczepień i ze starym szczepieniem.",
            "pytest -v → wszystko zielone. pip install pytest; requirements.txt; tests.yml jak w tygodniu 9 → Actions zielone od pierwszego pusha testów.",
        ],
        "sprawdz": "≥ 14 testów zielonych lokalnie i w Actions; żaden test nie dotyka stado.db (sprawdź: usuń stado.db i uruchom pytest — nadal zielone).",
    },
    "t10z5": {
        "czas": 90,
        "kroki": [
            "main.py: menu w pętli (1 lista zwierząt, 2 dodaj zwierzę, 3 dodaj zdarzenie, 4 historia zwierzęcia, 5 zdarzenia w zakresie dat, 6 nadchodzące szczepienia, 0 koniec). Każda opcja: wczytaj dane przez wczytaj_liczbe/input, zawołaj Stado, wypisz; ValueError z logiki → wypisz komunikat, wróć do menu.",
            "Dobij do 20+ testów (brakujące ścieżki: usunięcie zwierzęcia z historią, zdarzenia z tą samą datą, polskie znaki w imieniu).",
            "README: co robi, jak uruchomić, zrzut z menu, sekcja „Struktura” z trzema klockami. requirements.txt, .gitignore (stado.db, .venv). Actions zielone.",
            "Recenzja: „przejrzyj @stado.py”, „przejrzyj @main.py”. Poprawki. Commit, push, odhacz. Sobota: quiz 10. W Dzienniku: co w planie się nie sprawdziło i co zmieniłeś.",
        ],
        "sprawdz": "python main.py działa od pustej bazy do wpisania 2 zwierząt i 3 zdarzeń bez błędu; pytest ≥ 20 PASSED; Actions zielone.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 11
    "t11z1": {
        "czas": 75,
        "kroki": [
            "Lekcja „Flask: strony, formularze, walidacja”. (.venv) pip install flask; requirements.txt.",
            "app.py: from flask import Flask, render_template; app = Flask(__name__); @app.route(\"/\") def lista(): con = baza.polacz(); return render_template(\"lista.html\", zwierzeta=baza.pobierz_zwierzeta(con)). Na dole if __name__: app.run(debug=True).",
            "Folder templates/ i lista.html: minimalny HTML (<!doctype html>, <h1>Stado</h1>, <table>) z pętlą Jinja: {% for z in zwierzeta %}<tr><td>{{ z[1] }}</td><td>{{ z[2] }}</td></tr>{% endfor %}. Zapytaj Asystenta, czym jest szablon Jinja.",
            "python app.py → w przeglądarce http://127.0.0.1:5000 → tabela ze zwierzętami z bazy. Zmień coś w HTML, odśwież (debug=True przeładowuje sam). Ctrl+C zatrzymuje serwer.",
            "F12 → Elements: obejrzyj HTML, który wygenerował Flask — tydzień później będziesz pisać do niego lokatory, więc nadaj tabeli id=\"zwierzeta\" już teraz.",
        ],
        "sprawdz": "Strona główna pokazuje tabelę zwierząt z bazy; dodanie zwierzęcia przez main.py i odświeżenie strony pokazuje nowe.",
        "problemy": ["TemplateNotFound → folder musi nazywać się dokładnie templates i leżeć obok app.py.", "Port zajęty → app.run(port=5001)."],
    },
    "t11z2": {
        "czas": 75,
        "kroki": [
            "@app.route(\"/dodaj\", methods=[\"GET\", \"POST\"]). GET → render dodaj.html z formularzem (<form method=\"post\">, pola name=imie, rasa, data_ur, waga, przycisk). POST → request.form.get(...) → Stado(con).zarejestruj(...) w try: ValueError → render dodaj.html z blad=str(e) (wyświetl <p class=\"blad\" id=\"blad\">{{ blad }}</p>); sukces → redirect(\"/\").",
            "Walidacja jest JUŻ w stado.py — nie duplikuj jej w app.py; tylko złap wyjątek. To nagroda za rozdzielenie warstw w tygodniu 10.",
            "Testuj jak tester w przeglądarce: puste imię, waga -5, waga „abc”, data 2020-13-45, bardzo długie imię, imię z polskimi znakami. Każdy przypadek → czytelny komunikat, nie strona błędu 500. Zapisz tabelkę w przypadki_testowe.md projektu.",
            "Link „Dodaj zwierzę” na stronie głównej i link „Wróć” na formularzu. Nadaj id każdemu polu i przyciskowi (id=\"imie\", id=\"zapisz\") — pod Selenium.",
        ],
        "sprawdz": "6 błędnych przypadków daje komunikat pod formularzem; poprawny zapis przekierowuje na listę z nowym zwierzęciem.",
    },
    "t11z3": {
        "czas": 60,
        "kroki": [
            "@app.route(\"/zwierze/<int:zid>\") → historia.html: nagłówek z imieniem, tabela zdarzeń (data, typ, opis) z pobierz_zdarzenia(con, zid), posortowana po dacie. Nieistniejące id → return \"Nie ma takiego zwierzęcia\", 404 (zapytaj Asystenta o kody HTTP).",
            "Na liście zwierząt imię staje się linkiem: <a href=\"/zwierze/{{ z[0] }}\">{{ z[1] }}</a>.",
            "Opcjonalnie: formularz dodawania zdarzenia na stronie historii (/zwierze/<id>/zdarzenie, POST) — ten sam wzorzec co dodaj: try/ValueError/redirect.",
            "Testuj: zwierzę bez zdarzeń (pusta tabela z komunikatem „brak zdarzeń”), id = 999 → 404, id = abc → 404 od Flaska (int: w route).",
        ],
        "sprawdz": "Kliknięcie imienia pokazuje historię; /zwierze/999 daje 404 z komunikatem; zdarzenia w kolejności dat.",
    },
    "t11z4": {
        "czas": 90,
        "kroki": [
            "pages/: ListaPage (open(), imiona() → lista tekstów z tabeli #zwierzeta, kliknij_dodaj(), otworz_historie(imie)), DodajPage (wypelnij(imie, rasa, data, waga), zapisz(), blad()), HistoriaPage (naglowek(), zdarzenia() → lista wierszy).",
            "conftest.py: fixture serwer — uruchamia Flask w osobnym wątku lub procesie na porcie 5001 z bazą tymczasową (podaj ścieżkę przez zmienną środowiskową, np. STADO_DB; app.py czyta os.environ.get(\"STADO_DB\", \"stado.db\")); yield; zatrzymaj. Fixture driver z --headless=new. To najtrudniejszy kawałek tygodnia — zapytaj Asystenta: „jak uruchomić Flask w tle na czas testów pytest” (Offline: /temat flask + własna próba; API/Claude Code: pełna pomoc, ale tłumacz każdą linię).",
            "3 testy: test_lista_pokazuje_zwierzeta (dodaj przez bazę → otwórz → imię na liście), test_dodanie_przez_formularz (wypełnij → zapisz → na liście), test_historia (zdarzenie przez bazę → otwórz historię → widać typ).",
            "tests.yml: krok setup-chrome, STADO_DB w env, pytest tests/ -v. Push → Actions zielone (jednostkowe + Selenium). Czerwone w CI, zielone lokalnie? Czytaj log: zwykle brak headless albo serwer nie zdążył wstać (dodaj pętlę czekania na odpowiedź HTTP, max 10 s).",
        ],
        "sprawdz": "3 testy Selenium zielone lokalnie i w Actions obok testów jednostkowych.",
    },
    "t11z5": {
        "czas": 90,
        "kroki": [
            "Jedna komenda: python app.py — od czystego klona (sprawdź: sklonuj repo do innego folderu, venv, pip install -r requirements.txt, python app.py → działa?). Jeśli trzeba najpierw utworzyć bazę — niech app.py robi to sam przy starcie (polacz tworzy tabele).",
            "Domknij: nawigacja między stronami (linki w nagłówku każdej strony — zrób base.html i {% extends %}), minimalny CSS (jeden plik static/style.css), tytuły stron.",
            "Pełny przebieg testów: pytest -v → jednostkowe (≥ 20) + Selenium (3) zielone; Actions zielone; raport HTML w artefaktach.",
            "Recenzja app.py i szablonów. Commit „tydzień 11: interfejs webowy”, push, odhacz. Sobota: quiz 11. Dziennik: co było najtrudniejsze w Flasku.",
        ],
        "sprawdz": "Czysty klon → 4 komendy → aplikacja w przeglądarce; pytest ≥ 23 PASSED; Actions zielone.",
    },

    # ------------------------------------------------------------------ TYDZIEŃ 12
    "t12z1": {
        "czas": 60,
        "kroki": [
            "README projektu gospodarstwo — rekruter czyta je PIERWSZE: tytuł + 1 zdanie co to jest i dla kogo (z Twoim doświadczeniem: „powstało z potrzeby ewidencji stada w gospodarstwie, które prowadzę od 15 lat”).",
            "Sekcje: Funkcje (lista), Zrzuty ekranu (lista, formularz, historia — 3 obrazki), Uruchomienie (4 komendy), Struktura (baza/stado/app + testy — ten rysunek z PLAN.md), „Jak testuję” (pytest: ile testów jednostkowych, fixtures z bazą tymczasową; Selenium: POM, 3 testy E2E; CI: GitHub Actions, raport HTML — odznaka), Czego się nauczyłem (3 punkty), Plany (2 punkty z „nie wchodzi”).",
            "Odznaka CI na górze. Link do PLAN_TESTOW.md i bug raportów (zadanie 2).",
            "Test czytelnika: daj README komuś z rodziny — czy po 1 minucie powie, co program robi? Jeśli nie — skróć i uprość pierwsze 3 linie.",
        ],
        "sprawdz": "README ma 7 sekcji, 3 zrzuty, odznakę; osoba bez IT po minucie wie, co to jest.",
    },
    "t12z2": {
        "czas": 75,
        "kroki": [
            "PLAN_TESTOW.md: Zakres (co testujemy: logika stada, baza, formularze; czego nie: wydajność, bezpieczeństwo — świadomie), Poziomy (jednostkowe — które moduły; integracyjne — stado+baza; E2E — które przepływy), Przypadki testowe (tabela 10+ z ID, krokami, oczekiwanym, status: auto/manual), Co zautomatyzowane (lista testów z nazwami plików), Co manualne i dlaczego (np. wygląd, UX), Środowisko (Python, Chrome, CI), Kryteria wyjścia (wszystkie auto zielone, brak bugów krytycznych).",
            "3 bug raporty z WŁASNEJ aplikacji — szukaj celowo: data urodzenia z przyszłości, waga 100000, dwa zwierzęta o tym samym imieniu, bardzo szybkie podwójne kliknięcie „Zapisz”, znaki specjalne w opisie zdarzenia (<script>), bardzo długi opis. Każdy raport pełny (szablon z Prompty). Które naprawisz teraz, które zostawiasz jako „znane” — zapisz w raporcie.",
            "Dla każdego naprawionego buga: test, który go pilnuje (regresja). Commit „fix: BUG-00x + test regresji”.",
        ],
        "sprawdz": "PLAN_TESTOW.md z 7 sekcjami; 3 bug raporty; ≥ 1 naprawiony z testem regresji.",
    },
    "t12z3": {
        "czas": 75,
        "kroki": [
            "Prompt „Senior tester przed code review” (Claude Code / API: wklej z @stado.py @app.py @tests/…). Offline: użyj listy kontrolnej seniora — każdy punkt sprawdź sam: (1) czy test o nazwie X faktycznie sprawdza X (zepsuj kod, czy test czerwienieje?), (2) czy są testy na każdą walidację, (3) czy fixtures nie współdzielą stanu, (4) czy testy E2E nie zależą od kolejności, (5) czy w testach nie ma time.sleep, (6) czy komunikaty błędów są dla człowieka, (7) czy README uruchamia się od zera, (8) czy nazwy mówią co, nie jak.",
            "Wybierz 3 najważniejsze uwagi (najpoważniejsza pierwsza), wdróż każdą osobnym commitem z opisem „review: …”.",
            "Mutation testing na piechotę: zmień 5 losowych linii w stado.py (znak <, +=, wartość domyślną), uruchom pytest po każdej — ile mutacji testy złapały? Każda niezłapana = brakujący test. Dopisz.",
        ],
        "sprawdz": "3 commity „review: …”; z 5 mutacji ≥ 4 łapane przez testy.",
    },
    "t12z4": {
        "czas": 90,
        "kroki": [
            "Sesja rekrutacyjna: Asystent Offline → „odpytaj mnie jak rekruter” (15 pytań, wzorce po każdej odpowiedzi); Claude Code/API → prompt „Próbna rozmowa rekrutacyjna”. Odpowiadaj NA GŁOS, pełnymi zdaniami, z przykładem z projektu. Zapisz 3 najsłabsze odpowiedzi.",
            "Opowieść o projekcie: struktura Problem → Rozwiązanie → Jak testuję → Czego się nauczyłem. Napisz 10 zdań. Nagraj się telefonem (2 min max). Odsłuchaj. Wytnij „yyy”, skróć, nagraj ponownie — 3 podejścia.",
            "Transkrypcję (sam ją spisz — to też ćwiczenie) wklej do Asystenta API/Claude Code: „skróć i wzmocnij” — albo Offline: sprawdź listę: czy w pierwszym zdaniu jest problem? czy są liczby (ile testów, ile tabel)? czy jest jedno „czego się nauczyłem”?",
            "Pytania, na które nie znałeś odpowiedzi → /temat albo Lekcje; jutro powtórka tych 3.",
        ],
        "sprawdz": "Nagranie ≤ 2 min, które możesz puścić znajomemu bez wstydu; lista 3 pytań do powtórki w Dzienniku.",
    },
    "t12z5": {
        "czas": 120,
        "kroki": [
            "CV (1 strona, PDF): nagłówek z linkiem do GitHuba; sekcja Projekty NA GÓRZE (przed doświadczeniem): gospodarstwo (Python, SQLite, Flask, pytest N testów, Selenium POM, GitHub Actions — link + odznaka), meridianbank-tests (link), python-projekty (link). Każdy wpis: co robi, technologie, liczba testów, link. Umiejętności: Python, pytest, Selenium, Git/GitHub, CI, SQL podstawy, bug raporty, przypadki testowe. Doświadczenie: gospodarstwo — 2 punkty o odpowiedzialności, planowaniu, ewidencji (to są kompetencje, nie przeszkoda).",
            "Sprawdź każdy link w CV klikając z PDF-a. Repo publiczne? README na górze? Actions zielone? Rekruter klika TYLKO pierwszy link.",
            "5 aplikacji: justjoin.it, nofluffjobs.com, pracuj.pl — filtr „junior QA”, „tester”, „QA automation junior”, zdalnie/hybrydowo. Do każdej 3 zdania listu: kim jesteś, link do projektu, dlaczego ta firma. Zapisz w notatkach: firma, data, link, status.",
            "Panel Mentora: odhacz ostatnie zadanie. Checklista etapu 4. Dziennik: najdłuższy wpis — co 12 tygodni temu wydawało się niemożliwe.",
            "Nie koniec: codziennie 20 min — powtórka tematu z najsłabszego quizu, 1 commit do projektu, 1 aplikacja. Seria trwa.",
        ],
        "sprawdz": "CV PDF z działającymi linkami; 5 wpisów w notatkach z datą wysłania; program 65/65.",
    },
}
