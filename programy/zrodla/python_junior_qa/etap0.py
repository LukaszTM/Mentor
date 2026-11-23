# -*- coding: utf-8 -*-
"""Etap 0, tydzień 0: jak się uczyć, terminal i pierwszy program, środowisko kursu, Git i GitHub, nauka z asystentem AI."""

from wspolne import B, C, L, T, kod, li, tx, wy
import zrodla as Z

START = L(
    id="start_jak_sie_uczyc", nazwa="Start: jak uczyć się z tego kursu (przeczytaj najpierw)", tydzien=0,
    slowa=["plan", "jak się uczyć", "rytm dnia", "zasady", "70/30", "diagnoza", "quiz", "XP", "weryfikator"],
    cel="Po tej lekcji wiesz, co umiesz po 13 tygodniach, ile czasu to zajmie, jak wygląda dzień nauki i jak Mentor sprawdza zadania — i ustawiasz swój plan.",
    po_co="Kurs to 13 tygodni po ok. 7,5 godziny. Bez planu i jasnych zasad większość osób odpada w 3. tygodniu — z planem i małymi krokami dochodzi do końca.",
    wymagania=["Mentor uruchomiony (Mentor.exe) i ten kurs wgrany (Ustawienia → Program nauczania → „📦 Importuj kurs ZIP…”).", "Kartka albo plik notatki.md na zapiski."],
    wyjasnienie=(
        "## Co umiesz po kursie\n"
        "- Piszesz samodzielnie programy w Pythonie na 100–300 linii: zmienne, warunki, pętle, funkcje, listy i słowniki, pliki CSV, klasy, moduły.\n"
        "- Testujesz: projektujesz przypadki testowe (klasy równoważności, wartości brzegowe), piszesz testy w pytest, testy przeglądarki w Selenium (Page Object Model), raporty błędów, które programista rozumie bez pytań.\n"
        "- Pracujesz jak w zespole: Git (gałęzie, pull request), GitHub, automatyczne testy w GitHub Actions.\n"
        "- Masz na GitHubie projekt portfolio — aplikację „Magazyn” (Python, SQLite, Flask) z testami jednostkowymi, testami Selenium i CI — i umiesz o nim opowiedzieć na rozmowie Junior QA.\n"
        "## Ile to trwa\n"
        "13 tygodni (tydzień 0–12), 5 dni w tygodniu po ok. 90 minut + sobota na quiz i powtórkę. Razem ok. 100 godzin. Każdy tydzień mieści się w 9 godzinach — Mentor pokazuje czas lekcji i zadań.\n"
        "## Jak wygląda jedna lekcja\n"
        "Zawsze ta sama kolejność: **po co** → **wyjaśnienie od podstaw** → **demonstracja** (gotowy program omówiony linia po linii) → **jak uruchomić** → **ćwiczenie prowadzone** (prawie jak demonstracja) → **ćwiczenie samodzielne** (musisz podjąć decyzję) → **typowe błędy** → **pytania i test**. "
        "Każde ćwiczenie ma 3 poziomy podpowiedzi: pytanie naprowadzające → wskazanie fragmentu → częściowe rozwiązanie. Pełne rozwiązanie jest osobno, do samosprawdzenia.\n"
        "## Jak Mentor sprawdza zadania\n"
        "- Zadanie z kodem sprawdza **niezależny test z paczki kursu** (folder WERYFIKATORY, zabezpieczony sumą SHA-256). Test uruchamia Twoje funkcje na wielu danych — także błędnych — i mówi po polsku, czego brakuje.\n"
        "- Zadanie z dokumentem (np. bug raport) sprawdza test struktury (czy są wymagane sekcje i treść), a jakość oceniasz według listy „Gotowe, gdy”.\n"
        "- Zielony wynik to nie wszystko: po zadaniu wyjaśnij na głos (albo w notatki.md), **co i dlaczego działa**. To jest prawdziwe zaliczenie.\n"
        "## Zasada 70/30 z asystentem AI\n"
        "70% kodu piszesz sam, 30% może pochodzić z podpowiedzi. Asystent (Offline w Mentorze, API albo Claude Code) jest nauczycielem: najpierw pytasz o wskazówkę, potem o fragment, na końcu o pełne rozwiązanie — z omówieniem. "
        "Każdy fragment od AI przepisujesz ręcznie i umiesz go wytłumaczyć.\n"
        "## Diagnoza na start\n"
        "Plan → „Diagnoza” to 10 krótkich pytań. Wynik nie blokuje nauki — pokazuje, które lekcje warto przeczytać uważniej.\n"
        "## Uczciwie o rynku pracy\n"
        "W I kwartale 2026 oferty juniorskie stanowiły ok. 5% ogłoszeń w portalu justjoin.it, a odsetek kandydatów z doświadczeniem rósł. Kurs daje solidne podstawy i projekt portfolio, ale pierwszej pracy nie gwarantuje — "
        "w tygodniu 12 dostajesz plan szukania (CV, portfolio, rozmowa) zamiast obietnic."),
    przyklad=kod("start_jak_sie_uczyc", (
        "tygodnie = 13\n"
        "dni_w_tygodniu = 5\n"
        "minut_dziennie = 90\n"
        "godziny = tygodnie * dni_w_tygodniu * minut_dziennie / 60\n"
        "print(\"Godzin nauki w dni robocze:\", godziny)\n"), "Godzin nauki w dni robocze: 97.5\n"),
    demonstracja={"tytul": "Plan nauki policzony w 4 linijkach Pythona", "kroki": [
        "`tygodnie = 13` — zmienna (pudełko z etykietą) przechowuje liczbę tygodni. Zmienisz na 10 — wynik się zmieni.",
        "`dni_w_tygodniu = 5` i `minut_dziennie = 90` — dwa kolejne pudełka. Nazwy mówią, co jest w środku.",
        "`godziny = tygodnie * dni_w_tygodniu * minut_dziennie / 60` — mnożysz i dzielisz przez 60 (minuty → godziny). Gwiazdka `*` to mnożenie, `/` dzielenie.",
        "`print(...)` wypisuje tekst i wynik. Wynik 97.5 ma kropkę, bo dzielenie `/` w Pythonie zawsze daje liczbę z przecinkiem (float).",
        "Nie musisz jeszcze rozumieć składni — w tygodniu 1 przerobisz to dokładnie. Teraz zobacz tylko, że program to lista poleceń wykonywanych od góry."],
        "wynik": "Na ekranie: „Godzin nauki w dni robocze: 97.5” — plus soboty na quiz i powtórkę daje ok. 100 godzin."},
    jak_uruchomic=["Mentor → Lekcje → ta lekcja: przeczytaj w kolejności sekcji.",
                   "Plan → Diagnoza: odpowiedz na 10 pytań (ok. 10 minut).",
                   "Demonstrację uruchomisz po lekcji „Terminal”: wklej kod do pliku plan.py i kliknij ▶ Uruchom w pasku ćwiczenia."],
    cwiczenia=[
        C("prowadzone",
          "Policz jak w demonstracji, ale dla planu „wolniejszego”: 13 tygodni, 4 dni w tygodniu, 60 minut dziennie. (1) Ile minut tygodniowo? (2) Ile godzin razem? Czas: 10 minut.",
          "(1) 240 minut tygodniowo; (2) 52 godziny razem.",
          ["Minuty tygodniowo = dni × minuty dziennie.", "Godziny razem = minuty tygodniowo × tygodnie ÷ 60.", "4 × 60 = 240; 240 × 13 = 3120; 3120 ÷ 60 = …"],
          "4 × 60 = 240 minut tygodniowo; 240 × 13 = 3120 minut = 52 godziny. Plan wolniejszy jest w porządku — kurs po prostu potrwa dłużej niż 13 tygodni.",
          [li("tydz", "Minut tygodniowo", 240), li("razem", "Godzin razem", 52)]),
        C("samodzielne",
          "Zdecyduj, co robisz w każdej sytuacji: (1) nie rozumiesz komunikatu błędu po 10 minutach prób; (2) asystent podał gotowe rozwiązanie całego zadania; (3) test Mentora jest zielony, ale nie umiesz wyjaśnić, dlaczego kod działa; "
          "(4) opuściłeś(-aś) tydzień nauki. Opcje: poproś asystenta o wskazówkę (nie rozwiązanie) / przepisz ręcznie, linia po linii z wyjaśnieniem / wróć do lekcji i wyjaśnij w notatki.md / wróć do planu bez nadrabiania wszystkiego naraz. Czas: 10 minut.",
          "(1) wskazówka od asystenta; (2) przepisz ręcznie z wyjaśnieniem; (3) wróć do lekcji i wyjaśnij w notatki.md; (4) wróć do planu bez nadrabiania wszystkiego naraz.",
          ["Najpierw wskazówka, potem fragment, na końcu rozwiązanie.", "Kod od AI jest Twój dopiero, gdy umiesz go wytłumaczyć.", "Przerwa w nauce to nie kara — Mentor pokazuje, od czego zacząć."],
          "(1) poproś o wskazówkę; (2) przepisz ręcznie z wyjaśnieniem; (3) wróć do lekcji i wyjaśnij w notatki.md; (4) wróć do planu bez nadrabiania wszystkiego naraz.",
          [wy("s1", "(1) błąd po 10 min", ["wskazówka od asystenta", "przepisz ręcznie z wyjaśnieniem", "wróć do lekcji i wyjaśnij w notatki.md", "wróć do planu bez nadrabiania"], "wskazówka od asystenta"),
           wy("s2", "(2) gotowe rozwiązanie od AI", ["wskazówka od asystenta", "przepisz ręcznie z wyjaśnieniem", "wróć do lekcji i wyjaśnij w notatki.md", "wróć do planu bez nadrabiania"], "przepisz ręcznie z wyjaśnieniem"),
           wy("s3", "(3) zielone, ale nie rozumiem", ["wskazówka od asystenta", "przepisz ręcznie z wyjaśnieniem", "wróć do lekcji i wyjaśnij w notatki.md", "wróć do planu bez nadrabiania"], "wróć do lekcji i wyjaśnij w notatki.md"),
           wy("s4", "(4) tydzień przerwy", ["wskazówka od asystenta", "przepisz ręcznie z wyjaśnieniem", "wróć do lekcji i wyjaśnij w notatki.md", "wróć do planu bez nadrabiania"], "wróć do planu bez nadrabiania")]),
    ],
    typowe_bledy=[
        B("„Zrobię cały tydzień w sobotę”.", "Nauka zrywami — po 6 godzinach naraz pamięć i motywacja spadają.", "Spójrz na Statystyki w Mentorze: ile dni z nauką w tygodniu?", "Krótko, ale codziennie: 60–90 minut dziennie, sobota na quiz."),
        B("Zadanie zielone, a na quizie pustka.", "Kod skopiowany bez zrozumienia.", "Spróbuj wyjaśnić na głos każdą linię.", "Przepisz kod ręcznie, zmień jedną wartość i przewidź wynik, zanim uruchomisz."),
    ],
    pulapki=["Porównywanie się z innymi („ktoś zrobił kurs w miesiąc”) — liczy się, czy umiesz wyjaśnić swój kod.",
             "Kupowanie płatnych narzędzi na start — kurs przechodzisz za 0 zł (Mentor, Python, Git, GitHub i PyCharm w wersji darmowej)."],
    zadania=["Zrób Diagnozę w Planie.", "Wpisz do kalendarza 5 stałych godzin nauki w tygodniu.", "Załóż notatki.md i zapisz w 3 zdaniach, po co robisz ten kurs."],
    pytania=[["Ile godzin trwa kurs?", "Ok. 100 godzin: 13 tygodni po ok. 7,5 h."],
             ["Kiedy zadanie jest naprawdę zaliczone?", "Gdy test Mentora jest zielony I umiesz wyjaśnić, co i dlaczego działa."],
             ["Co robisz, gdy asystent poda gotowe rozwiązanie?", "Przepisujesz ręcznie linia po linii i tłumaczysz każdą linię."]],
    podsumowanie="Znasz cel kursu, rytm dnia (90 minut, 5 dni), kolejność pracy z lekcją, sposób sprawdzania zadań i zasadę 70/30 z asystentem.",
    test=[T("Ile mniej więcej trwa kurs?", ["10 godzin", "ok. 100 godzin", "500 godzin", "tyle, ile chcesz — bez planu"], 1, "13 tygodni × ok. 7,5 h."),
          T("Co sprawdza zadanie z kodem?", ["tylko czy plik istnieje", "niezależny test z paczki kursu", "liczba linii", "nic — odhaczasz sam"], 1, "Weryfikatory z paczki uruchamiają Twoje funkcje na wielu danych."),
          T("Zasada 70/30 oznacza:", ["70% czasu oglądasz filmy", "70% kodu piszesz sam", "70% zadań robi AI", "70% na quizie wystarczy"], 1, "AI pomaga, Ty piszesz i rozumiesz."),
          T("Diagnoza na start:", ["blokuje dostęp do lekcji", "pokazuje, co warto powtórzyć", "jest płatna", "zastępuje kurs"], 1, "Nie blokuje — wskazuje powtórki.")],
    w_praktyce=["Codziennie: lekcja dnia → zadanie → 3 zdania w notatki.md (co zrobiłem, co było trudne, pytanie na jutro).",
                "Sobota: quiz tygodnia i powtórka tematów z czerwonymi wynikami."],
    zrodla=[Z.ISTQB_CTFL, Z.RYNEK_JJ, Z.PY_TUT_PL],
)

TERMINAL = L(
    id="terminal", nazwa="Terminal, katalogi i pierwszy program w Pythonie", tydzien=0,
    slowa=["terminal", "PowerShell", "katalog", "folder", "ścieżka", "cd", "ls", "mkdir", "python", "hello.py", "katalog roboczy"],
    cel="Po tej lekcji poruszasz się po katalogach w terminalu (cd, ls, mkdir), rozumiesz ścieżkę pliku i uruchamiasz pierwszy program Pythona — w terminalu i przyciskiem ▶ w Mentorze.",
    po_co="Testy, Git i serwery uruchamia się z terminala. Tester, który nie boi się wiersza poleceń, pracuje szybciej i rozumie, co robi CI.",
    wymagania=["Windows 10/11 z Mentorem.", "Środowisko kursu zainstalowane w Mentorze (lekcja „Narzędzia”) — przycisk ▶ Uruchom działa po instalacji."],
    wyjasnienie=(
        "## Plik, katalog, ścieżka\n"
        "Plik to dokument (np. hello.py), katalog (folder) to szuflada na pliki. **Ścieżka** to adres pliku: `C:\\Users\\Ania\\Documents\\PRACA\\hello.py` — dysk, potem kolejne katalogi oddzielone `\\`, na końcu nazwa pliku. "
        "Rozszerzenie `.py` mówi, że to program w Pythonie.\n"
        "## Terminal\n"
        "Terminal to okno, w którym wpisujesz polecenia zamiast klikać. W Windows: Start → wpisz „PowerShell” → Enter (albo zakładka Terminal w Mentorze). Zachęta `PS C:\\Users\\Ania>` pokazuje **katalog roboczy** — miejsce, w którym teraz „stoisz”.\n"
        "| polecenie | co robi | przykład |\n|---|---|---|\n"
        "| `pwd` | pokazuje, gdzie jesteś | `pwd` |\n"
        "| `ls` (albo `dir`) | lista plików w katalogu | `ls` |\n"
        "| `cd nazwa` | wejdź do katalogu | `cd Documents` |\n"
        "| `cd ..` | wyjdź piętro wyżej | `cd ..` |\n"
        "| `mkdir nazwa` | utwórz katalog | `mkdir PRACA` |\n"
        "| `python plik.py` | uruchom program | `python hello.py` |\n"
        "Klawisz **Tab** dopełnia nazwę pliku, strzałka ↑ przywraca poprzednie polecenie. Ścieżkę ze spacją bierzesz w cudzysłów: `cd \"Moje dokumenty\"`.\n"
        "## Pierwszy program\n"
        "Program w Pythonie to zwykły plik tekstowy. `print(\"Cześć\")` wypisuje tekst. `import datetime` dołącza moduł z datami, a `datetime.date.today()` zwraca dzisiejszą datę. "
        "Python wykonuje linie **od góry do dołu**.\n"
        "## Mentor bez terminala\n"
        "Pod każdym zadaniem z kodem jest pasek „Ćwiczenie w Mentorze”: **Utwórz plik ćwiczenia** → piszesz w edytorze → **Ctrl+S** → **▶ Uruchom** (wynik pod spodem, dane dla `input()` wpisujesz w polu nad wynikiem) → **✔ Sprawdź wynik**. "
        "Plik trafia do Twojego katalogu roboczego PRACA. Terminal przyda się od tygodnia 4 (Git) i 7 (pytest)."),
    przyklad=kod("terminal", (
        "import datetime\n\n"
        "print(\"Cześć! To mój pierwszy program.\")\n"
        "dzis = datetime.date(2026, 11, 23)\n"
        "print(\"Data:\", dzis)\n"
        "print(\"Rok:\", dzis.year)\n"), "Cześć! To mój pierwszy program.\nData: 2026-11-23\nRok: 2026\n"),
    demonstracja={"tytul": "Od pustego katalogu do działającego programu", "kroki": [
        "W terminalu: `cd Documents` → `mkdir PRACA` → `cd PRACA` → `pwd`. Zobaczysz `...\\Documents\\PRACA` — tu będą Twoje pliki.",
        "W Mentorze (albo w Notatniku) utwórz plik `hello.py` w PRACA i wpisz kod z ramki.",
        "`import datetime` — na górze pliku dołączasz moduł z datami. Bez tej linii następna dałaby błąd NameError.",
        "`print(\"Cześć! …\")` — tekst w cudzysłowie to napis; print wypisuje go w nowej linii.",
        "`dzis = datetime.date(2026, 11, 23)` — tworzysz datę (rok, miesiąc, dzień) i zapisujesz w zmiennej `dzis`. W zadaniu użyjesz `datetime.date.today()` — wtedy data będzie dzisiejsza.",
        "`print(\"Data:\", dzis)` — print z dwoma argumentami wstawia między nie spację; data wypisuje się w formacie ROK-MIESIĄC-DZIEŃ.",
        "`dzis.year` — z daty wyciągasz sam rok.",
        "W terminalu w katalogu PRACA: `python hello.py`. W Mentorze: ▶ Uruchom."],
        "wynik": "Trzy linie: powitanie, „Data: 2026-11-23” i „Rok: 2026”."},
    jak_uruchomic=["Mentor → zadanie t0z3 → pasek „Ćwiczenie w Mentorze” → Utwórz plik ćwiczenia → wklej/napisz kod → Ctrl+S → ▶ Uruchom.",
                   "Albo terminal: `cd` do katalogu PRACA → `python hello.py` (w terminalu Mentora polecenie `python` wskazuje środowisko kursu)."],
    cwiczenia=[
        C("prowadzone",
          "Jesteś w `C:\\Users\\Ania`. Wpisujesz kolejno: `cd Documents`, `mkdir PRACA`, `cd PRACA`, `mkdir testy`, `cd testy`, `cd ..`. (1) W jakim katalogu jesteś na końcu (pełna ścieżka)? (2) Ile nowych katalogów utworzyłaś? Czas: 10 minut.",
          "(1) C:\\Users\\Ania\\Documents\\PRACA; (2) 2 katalogi (PRACA i testy).",
          ["Każde `cd nazwa` dopisuje nazwę do ścieżki.", "`cd ..` usuwa ostatni element ścieżki.", "Policz polecenia `mkdir`."],
          "Documents → PRACA → testy → `cd ..` wraca do PRACA: C:\\Users\\Ania\\Documents\\PRACA. Utworzone: PRACA i testy = 2.",
          [tx("sciezka", "Katalog na końcu", "C:\\Users\\Ania\\Documents\\PRACA"), li("ile", "Ile katalogów utworzono", 2)]),
        C("samodzielne",
          "Dopasuj polecenie do celu: (1) zobaczyć pliki w katalogu; (2) wyjść piętro wyżej; (3) uruchomić program raport.py; (4) wejść do katalogu „Moje projekty” (ze spacją). Opcje: `ls`, `cd ..`, `python raport.py`, `cd \"Moje projekty\"`. Czas: 10 minut.",
          "(1) ls; (2) cd ..; (3) python raport.py; (4) cd \"Moje projekty\".",
          ["Lista plików to jedno krótkie polecenie.", "Dwie kropki oznaczają katalog nadrzędny.", "Ścieżka ze spacją musi być w cudzysłowie."],
          "(1) `ls`; (2) `cd ..`; (3) `python raport.py`; (4) `cd \"Moje projekty\"` — bez cudzysłowu terminal wziąłby tylko słowo „Moje”.",
          [wy("p1", "(1) lista plików", ["ls", "cd ..", "python raport.py", "cd \"Moje projekty\""], "ls"),
           wy("p2", "(2) piętro wyżej", ["ls", "cd ..", "python raport.py", "cd \"Moje projekty\""], "cd .."),
           wy("p3", "(3) uruchom raport.py", ["ls", "cd ..", "python raport.py", "cd \"Moje projekty\""], "python raport.py"),
           wy("p4", "(4) katalog ze spacją", ["ls", "cd ..", "python raport.py", "cd \"Moje projekty\""], "cd \"Moje projekty\"")]),
    ],
    typowe_bledy=[
        B("python: can't open file '…\\hello.py': [Errno 2] No such file or directory", "Jesteś w innym katalogu niż plik.", "`pwd` i `ls` — czy widzisz hello.py?", "`cd` do katalogu z plikiem albo podaj pełną ścieżkę."),
        B("'python' is not recognized as an internal or external command", "Python nie jest dostępny w tym terminalu.", "Mentor → Środowisko: status Pythona.", "Użyj terminala Mentora albo przycisku ▶ Uruchom — korzystają ze środowiska kursu."),
        B("SyntaxError: unterminated string literal", "Brakuje zamykającego cudzysłowu.", "Sprawdź linię wskazaną w komunikacie.", "Każdy napis zaczyna się i kończy tym samym cudzysłowem: \"…\"."),
    ],
    pulapki=["Plik zapisany jako hello.py.txt (Notatnik dopisuje .txt) — w Eksploratorze włącz „Rozszerzenia nazw plików”.",
             "Spacja w nazwie pliku programu — nazywaj pliki małymi literami z podkreśleniem: lista_zakupow.py."],
    zadania=["Utwórz katalog PRACA i sprawdź jego pełną ścieżkę poleceniem pwd.", "Uruchom hello.py w terminalu i przyciskiem ▶ w Mentorze.", "Zmień datę w przykładzie i przewidź wynik przed uruchomieniem."],
    pytania=[["Co pokazuje zachęta PS C:\\Users\\Ania>?", "Katalog roboczy — miejsce, w którym działają polecenia."],
             ["Jak wejść do katalogu ze spacją w nazwie?", "cd \"Nazwa ze spacją\" — w cudzysłowie."],
             ["W jakiej kolejności Python wykonuje linie?", "Od góry do dołu."]],
    podsumowanie="Poruszasz się po katalogach (pwd, ls, cd, mkdir), rozumiesz ścieżkę pliku i uruchamiasz program w terminalu oraz w Mentorze.",
    test=[T("Które polecenie wychodzi piętro wyżej?", ["cd ..", "cd /", "ls ..", "up"], 0, "Dwie kropki = katalog nadrzędny."),
          T("Co zrobi `python hello.py`, gdy pliku nie ma w bieżącym katalogu?", ["uruchomi go i tak", "błąd No such file or directory", "utworzy plik", "otworzy edytor"], 1, "Python szuka pliku w katalogu roboczym."),
          T("Po co `import datetime` na górze pliku?", ["dla ozdoby", "żeby móc użyć modułu z datami", "żeby przyspieszyć program", "to komentarz"], 1, "Bez importu nazwa datetime jest nieznana (NameError).")],
    w_praktyce=["Każdy projekt w osobnym katalogu w PRACA.", "Przed uruchomieniem: pwd — czy jestem tam, gdzie plik?"],
    zrodla=[Z.PY_WIN, Z.PY_TUT_INTRO, Z.PY_DATETIME],
)

INSTALACJA = L(
    id="instalacja", nazwa="Narzędzia: środowisko kursu w Mentorze, Git, edytor i (opcjonalnie) Claude Code", tydzien=0,
    slowa=["instalacja", "środowisko", "venv", "Python", "pip", "Git", "PyCharm", "Claude Code", "lock", "biblioteki"],
    cel="Po tej lekcji masz zainstalowane środowisko kursu (Python + pytest, requests, selenium, flask) w Mentorze, Git for Windows i wiesz, jak sprawdzić każde narzędzie — oraz co zrobić przy typowym błędzie instalacji.",
    po_co="Połowa problemów początkujących to „u mnie nie działa” przez złą wersję Pythona albo brak biblioteki. Środowisko kursu jest takie samo u każdego ucznia — błędy dotyczą kodu, nie instalacji.",
    wymagania=["Windows 10/11, ok. 1 GB wolnego miejsca, internet przy pierwszej instalacji.", "Uprawnienia administratora NIE są potrzebne."],
    wyjasnienie=(
        "## Środowisko kursu (Mentor → Środowisko)\n"
        "Mentor tworzy **osobne środowisko wirtualne** (.venv) tylko dla tego kursu. Jeśli na komputerze nie ma odpowiedniego Pythona (3.11–3.13), Mentor za Twoją zgodą pobiera Pythona 3.12 z zaufanego, podpisanego sumą archiwum. "
        "Biblioteki instaluje z pliku blokady (lock) — dokładne wersje sprawdzone sumami SHA-256: pytest 9.2, requests 2.34, selenium 4.52, flask 3.1. Dzięki temu nie trafisz na „najnowszą” wersję, która akurat coś zmieniła.\n"
        "- Status zielony = gotowe. Żółty = brak elementu, przycisk „Napraw”. Czerwony = opis błędu po polsku i następny krok.\n"
        "- Środowisko możesz usunąć i odtworzyć jednym przyciskiem — Twoje pliki w PRACA zostają.\n"
        "## Wersje Pythona — skąd różnica?\n"
        "Na python.org najnowszy jest Python 3.15 (wydany 9.10.2026). Kurs używa 3.11–3.13, bo dla tych wersji zablokowano i przetestowano biblioteki. Wszystko, czego się uczysz, działa tak samo w 3.15.\n"
        "## Git for Windows (potrzebny od tygodnia 0)\n"
        "Git zapisuje historię zmian w projekcie. Instalacja: oficjalna strona git-scm.com → Download for Windows → instalator 64-bit; w kreatorze zostaw domyślne opcje (edytor możesz zmienić na Notepad). "
        "Albo w PowerShell: `winget install --id Git.Git -e`. Sprawdzenie w NOWYM oknie terminala: `git --version` → np. `git version 2.5x.x.windows.1`.\n"
        "## Edytor\n"
        "Wystarczy edytor Mentora. Jeśli chcesz IDE: **PyCharm** — od 2025 r. jeden produkt; podstawowe funkcje (edytor, debugger, uruchamianie testów) są darmowe, funkcje Pro wymagają subskrypcji (30 dni próbnych). "
        "W PyCharm wskaż interpreter środowiska kursu: Settings → Python Interpreter → Add → Existing → `…\\.venv\\Scripts\\python.exe` (ścieżkę pokazuje Mentor → Środowisko).\n"
        "## Claude Code (opcjonalny)\n"
        "Asystent AI w terminalu. Wymaga płatnego planu (Pro lub wyższy) albo konta API. Kurs **nie wymaga** Claude Code — Asystent Offline w Mentorze i darmowy czat wystarczą. "
        "Jeśli chcesz: instalacja według oficjalnej dokumentacji (PowerShell: `irm https://claude.ai/install.ps1 | iex`), sprawdzenie `claude --version`.\n"
        "## Sprawdzanie każdego narzędzia\n"
        "| narzędzie | polecenie | dobry wynik |\n|---|---|---|\n"
        "| środowisko kursu | Mentor → Środowisko → Sprawdź | wszystkie pozycje zielone |\n"
        "| Python kursu | terminal Mentora: `python --version` | Python 3.11–3.13 |\n"
        "| Git | `git --version` | git version 2.… |\n"
        "| pytest | terminal Mentora: `python -m pytest --version` | pytest 9.2.0 |"),
    przyklad=kod("instalacja", (
        "import sys\n"
        "import importlib.util\n\n"
        "print(\"Python:\", sys.version_info.major, sys.version_info.minor)\n"
        "for nazwa in [\"pytest\", \"requests\", \"selenium\", \"flask\"]:\n"
        "    jest = importlib.util.find_spec(nazwa) is not None\n"
        "    print(nazwa, \"OK\" if jest else \"BRAK\")\n"), None),
    demonstracja={"tytul": "Program, który sprawdza środowisko kursu", "kroki": [
        "`import sys` — moduł z informacjami o uruchomionym Pythonie; `sys.version_info.major` i `.minor` to np. 3 i 12.",
        "`import importlib.util` — narzędzie do sprawdzania, czy moduł da się zaimportować, bez importowania go.",
        "`for nazwa in [...]` — pętla przechodzi po czterech nazwach bibliotek (pętle poznasz w tygodniu 2; tu wystarczy: „dla każdej nazwy zrób…”).",
        "`importlib.util.find_spec(nazwa) is not None` — prawda, gdy biblioteka jest zainstalowana w TYM Pythonie.",
        "`\"OK\" if jest else \"BRAK\"` — wybór jednego z dwóch napisów.",
        "Uruchom przyciskiem ▶ w Mentorze (środowisko kursu): wszystkie 4 = OK. Uruchom zwykłym `python` spoza Mentora: często zobaczysz BRAK — to dowód, że środowisko kursu jest osobne."],
        "wynik": "Python: 3 12 (albo 3 11 / 3 13) i cztery linie „… OK”."},
    jak_uruchomic=["Mentor → Środowisko → „Sprawdź” → jeśli trzeba „Zainstaluj / Napraw” → potwierdź.",
                   "Git: git-scm.com → Download for Windows → instalator → domyślne opcje → nowe okno terminala → `git --version`.",
                   "Program z demonstracji: zapisz jako srodowisko.py w PRACA → ▶ Uruchom."],
    cwiczenia=[
        C("prowadzone",
          "Odczytaj wyniki sprawdzenia: `python --version` → „Python 3.12.12”, `python -m pytest --version` → „pytest 9.2.0”, `git --version` → „'git' is not recognized…”. (1) Czy Python kursu jest w obsługiwanej wersji? (2) Którego narzędzia brakuje? Czas: 10 minut.",
          "(1) tak — 3.12 mieści się w 3.11–3.13; (2) brakuje Gita.",
          ["Kurs obsługuje wersje 3.11–3.13.", "„is not recognized” znaczy: system nie zna takiego polecenia.", "pytest odpowiedział numerem wersji — jest."],
          "Python 3.12 jest w zakresie 3.11–3.13; pytest działa; Git nie jest zainstalowany (albo terminal otwarto przed instalacją — wtedy wystarczy nowe okno).",
          [wy("ok", "(1) Python w obsługiwanej wersji?", ["tak", "nie"], "tak"), wy("brak", "(2) Czego brakuje?", ["Pythona", "pytest", "Gita", "niczego"], "Gita")]),
        C("samodzielne",
          "Dobierz naprawę: (1) zainstalowałeś(-aś) Gita, ale terminal dalej mówi „git is not recognized”; (2) Mentor → Środowisko: „Brak gotowego pakietu (wheel) dla tej wersji Pythona”; (3) PyCharm podkreśla `import pytest` na czerwono, a w Mentorze testy działają. "
          "Opcje: otwórz nowe okno terminala / pozwól Mentorowi pobrać Pythona 3.12 / wskaż w PyCharm interpreter z .venv kursu. Czas: 10 minut.",
          "(1) nowe okno terminala; (2) Python 3.12 od Mentora; (3) interpreter .venv kursu w PyCharm.",
          ["Stare okno terminala nie zna nowego PATH.", "Lock jest przygotowany dla 3.11–3.13.", "PyCharm używa innego Pythona niż Mentor."],
          "(1) nowe okno terminala (PATH wczytuje się przy otwarciu); (2) pozwól Mentorowi pobrać 3.12; (3) PyCharm → Python Interpreter → .venv kursu.",
          [wy("n1", "(1) git nieznany po instalacji", ["otwórz nowe okno terminala", "pozwól Mentorowi pobrać Pythona 3.12", "wskaż w PyCharm interpreter z .venv kursu"], "otwórz nowe okno terminala"),
           wy("n2", "(2) brak pakietu wheel", ["otwórz nowe okno terminala", "pozwól Mentorowi pobrać Pythona 3.12", "wskaż w PyCharm interpreter z .venv kursu"], "pozwól Mentorowi pobrać Pythona 3.12"),
           wy("n3", "(3) PyCharm nie widzi pytest", ["otwórz nowe okno terminala", "pozwól Mentorowi pobrać Pythona 3.12", "wskaż w PyCharm interpreter z .venv kursu"], "wskaż w PyCharm interpreter z .venv kursu")]),
    ],
    typowe_bledy=[
        B("'git' is not recognized as an internal or external command", "Git niezainstalowany albo terminal otwarty przed instalacją.", "Nowe okno → `git --version`.", "Zainstaluj Git for Windows z git-scm.com (domyślne opcje) i otwórz nowe okno."),
        B("ModuleNotFoundError: No module named 'pytest'", "Program uruchomiony innym Pythonem niż środowisko kursu.", "W tym samym terminalu: `python -c \"import sys; print(sys.executable)\"` — czy ścieżka zawiera .venv kursu?", "Uruchamiaj przyciskiem ▶ w Mentorze albo w terminalu Mentora."),
        B("Instalacja środowiska przerwana (brak internetu / miejsca)", "Pobieranie nie mogło się dokończyć.", "Mentor → Środowisko → opis błędu.", "Zwolnij miejsce / podłącz sieć → „Napraw”. Instalację można powtórzyć bez szkody."),
    ],
    pulapki=["Instalowanie bibliotek „na ślepo” poleceniem pip do systemowego Pythona — w kursie robi to wyłącznie Mentor, do .venv kursu.",
             "Pobieranie instalatorów z nieoficjalnych stron — tylko git-scm.com, python.org, jetbrains.com, claude.ai."],
    zadania=["Zainstaluj środowisko kursu w Mentorze (wszystko zielone).", "Zainstaluj Git for Windows i sprawdź git --version.", "Uruchom program z demonstracji i porównaj wynik z uruchomieniem spoza Mentora."],
    pytania=[["Dlaczego kurs ma osobne środowisko .venv?", "Żeby wersje bibliotek były takie same u wszystkich i nie mieszały się z innymi programami."],
             ["Co zrobić, gdy po instalacji Gita polecenie nie działa?", "Otworzyć nowe okno terminala (nowy PATH)."],
             ["Czy Claude Code jest wymagany?", "Nie — Asystent Offline i darmowy czat wystarczą."]],
    podsumowanie="Masz środowisko kursu z dokładnymi wersjami bibliotek, Gita i edytor; umiesz sprawdzić każde narzędzie i naprawić typowe błędy instalacji.",
    test=[T("Gdzie Mentor instaluje biblioteki kursu?", ["do systemowego Pythona", "do osobnego .venv kursu", "do folderu Windows", "nigdzie — są w chmurze"], 1, "Osobne środowisko kursu."),
          T("Po co plik blokady (lock)?", ["żeby nikt nie zmienił kodu", "dokładne, sprawdzone wersje bibliotek z sumami SHA-256", "żeby kurs był płatny", "blokuje internet"], 1, "Powtarzalna instalacja."),
          T("Git zainstalowany, ale „not recognized”. Pierwszy krok?", ["reinstalacja Windows", "nowe okno terminala", "usunąć Mentora", "zainstalować Pythona"], 1, "PATH wczytuje się przy otwarciu okna."),
          T("PyCharm w 2026 r.:", ["jest tylko płatny", "ma darmowe funkcje podstawowe, Pro w subskrypcji", "nie obsługuje Pythona", "wymaga Linuksa"], 1, "Unified PyCharm: rdzeń za darmo.")],
    w_praktyce=["Po każdej większej aktualizacji Windows: Mentor → Środowisko → Sprawdź.", "Zgłaszając problem, zawsze podaj wynik `python --version` i `git --version`."],
    zrodla=[Z.PY_WIN, Z.PY_315, Z.PY_TUT_VENV, Z.PYCHARM, Z.CC_SETUP, Z.GIT_PL],
)

GIT_START = L(
    id="git_start", nazwa="Git i GitHub — pierwszy commit i push", tydzien=0,
    slowa=["git", "repozytorium", "commit", "git init", "git add", "git status", "git log", "push", "GitHub", "remote", "origin", "token"],
    cel="Po tej lekcji tworzysz repozytorium Git, zapisujesz zmiany commitem (add → commit), czytasz git status i git log oraz wysyłasz projekt na GitHub (remote, push).",
    po_co="Każdy zespół trzyma kod w Gicie, a rekruter ogląda Twój GitHub zanim zaprosi na rozmowę. Historia commitów pokazuje, jak pracujesz.",
    wymagania=["Git for Windows (lekcja „Narzędzia”).", "Darmowe konto na github.com (e-mail, hasło, nazwa użytkownika; włącz weryfikację dwuetapową).", "Katalog PRACA z plikiem hello.py."],
    wyjasnienie=(
        "## Repozytorium i commit\n"
        "**Repozytorium** to katalog, w którym Git pamięta historię. **Commit** to zapisany punkt historii: zestaw zmian + opis + autor + data — jak zapis gry, do którego zawsze możesz wrócić.\n"
        "## Trzy miejsca\n"
        "1. katalog roboczy — pliki, które edytujesz; 2. **poczekalnia** (staging) — zmiany wybrane do commita (`git add`); 3. historia — commity (`git commit`).\n"
        "## Pierwsza konfiguracja (raz na komputer)\n"
        "`git config --global user.name \"Anna Nowak\"` i `git config --global user.email \"anna@example.com\"` — te dane będą w każdym commicie. Na GitHubie możesz użyć adresu prywatności `…@users.noreply.github.com`.\n"
        "## Codzienny cykl\n"
        "| polecenie | co robi |\n|---|---|\n"
        "| `git init` | zamienia katalog w repozytorium (raz) |\n"
        "| `git status` | co się zmieniło, co jest w poczekalni |\n"
        "| `git add hello.py` | dodaje plik do poczekalni (`git add .` — wszystkie) |\n"
        "| `git commit -m \"Dodaj hello.py\"` | zapisuje commit z opisem |\n"
        "| `git log --oneline` | historia w skrócie |\n"
        "Opis commita: tryb rozkazujący, co zmienia — „Dodaj kalkulator”, „Popraw dzielenie przez zero”.\n"
        "## GitHub — kopia w internecie\n"
        "1. github.com → New repository → nazwa `nauka-python`, Public, BEZ README (repo puste). 2. W PRACA: `git remote add origin https://github.com/TWOJA-NAZWA/nauka-python.git` — `origin` to skrót adresu. "
        "3. `git branch -M main` — główna gałąź nazywa się main. 4. `git push -u origin main` — wysyła commity. Przy pierwszym push okno logowania (Git Credential Manager) otworzy przeglądarkę — logujesz się do GitHuba, hasło nie trafia do terminala.\n"
        "## Czego NIE commitować\n"
        "Haseł, tokenów, plików .env, katalogu .venv. Od tygodnia 5 pilnuje tego plik `.gitignore`."),
    przyklad=("PS C:\\Users\\Ania\\Documents\\PRACA> git init\n"
              "Initialized empty Git repository in C:/Users/Ania/Documents/PRACA/.git/\n"
              "PS …\\PRACA> git status\n"
              "Untracked files:\n  hello.py\n"
              "PS …\\PRACA> git add hello.py\n"
              "PS …\\PRACA> git commit -m \"Dodaj pierwszy program hello.py\"\n"
              "[master (root-commit) 3f2a1c9] Dodaj pierwszy program hello.py\n 1 file changed, 6 insertions(+)\n"
              "PS …\\PRACA> git branch -M main\n"
              "PS …\\PRACA> git remote add origin https://github.com/anna-nowak/nauka-python.git\n"
              "PS …\\PRACA> git push -u origin main\n"
              "To https://github.com/anna-nowak/nauka-python.git\n * [new branch]      main -> main"),
    demonstracja={"tytul": "Pierwszy commit i wysłanie na GitHub", "kroki": [
        "`git init` — w katalogu PRACA powstaje ukryty folder .git (tam jest cała historia). Nie usuwaj go.",
        "`git status` — hello.py jest „Untracked”: Git go widzi, ale jeszcze nie śledzi.",
        "`git add hello.py` — plik trafia do poczekalni. `git status` pokaże go teraz na zielono w „Changes to be committed”.",
        "`git commit -m \"…\"` — zapis w historii. 3f2a1c9 to początek identyfikatora commita (skrót SHA).",
        "`git branch -M main` — zmiana nazwy gałęzi na main (GitHub używa tej nazwy domyślnie).",
        "`git remote add origin <adres>` — zapamiętanie adresu repozytorium na GitHubie pod nazwą origin.",
        "`git push -u origin main` — wysłanie commitów; `-u` zapamiętuje, że main wysyłasz do origin (później wystarczy `git push`).",
        "Odśwież stronę repozytorium na GitHubie — widzisz hello.py i opis commita."],
        "wynik": "Na GitHubie repozytorium nauka-python z plikiem hello.py i jednym commitem."},
    jak_uruchomic=["Terminal (PowerShell albo terminal Mentora) w katalogu PRACA → polecenia z ramki po kolei.",
                   "Po każdym poleceniu `git status` — to najlepszy sposób, żeby wiedzieć, co się stało."],
    cwiczenia=[
        C("prowadzone",
          "Ułóż w kolejności (wpisz numery po przecinku): 1 `git commit -m \"Dodaj kalkulator\"`, 2 `git add kalkulator.py`, 3 `git push`, 4 `git status`. Zaczynasz od sprawdzenia stanu. Czas: 10 minut.",
          "4, 2, 1, 3 — status → add → commit → push.",
          ["Najpierw sprawdź, co się zmieniło.", "Do poczekalni przed zapisem.", "Wysyłasz to, co już zapisane."],
          "4 (status), 2 (add), 1 (commit), 3 (push).",
          [tx("kolejnosc", "Kolejność numerów", "4, 2, 1, 3")]),
        C("samodzielne",
          "Co się stanie? (1) Zmieniasz hello.py i od razu robisz `git commit -m \"Zmiana\"` bez `git add`; (2) robisz commit, ale nie push — czy zmiana jest na GitHubie?; (3) commitujesz plik haslo.txt z hasłem i potem go usuwasz nowym commitem — czy hasło zniknęło z historii? "
          "Opcje dla każdego: tak / nie. (1) Czy zmiana trafi do commita? Czas: 15 minut.",
          "(1) nie — bez git add zmiana nie jest w poczekalni; (2) nie — commit jest tylko lokalnie; (3) nie — hasło zostaje w historii, trzeba je zmienić.",
          ["Commit zapisuje tylko to, co jest w poczekalni.", "push wysyła, commit zapisuje lokalnie.", "Historia pamięta każdą poprzednią wersję."],
          "(1) nie; (2) nie; (3) nie — usunięcie pliku nowym commitem nie usuwa go z poprzednich commitów. Hasło, które trafiło do repozytorium, trzeba natychmiast zmienić.",
          [wy("q1", "(1) zmiana w commicie bez git add?", ["tak", "nie"], "nie"), wy("q2", "(2) commit bez push — na GitHubie?", ["tak", "nie"], "nie"),
           wy("q3", "(3) hasło zniknęło z historii?", ["tak", "nie"], "nie")]),
    ],
    typowe_bledy=[
        B("Author identity unknown *** Please tell me who you are.", "Brak user.name / user.email.", "`git config --global --list`.", "`git config --global user.name \"…\"` i `user.email \"…\"`."),
        B("fatal: not a git repository (or any of the parent directories): .git", "Polecenie wpisane poza repozytorium.", "`pwd` — czy jesteś w PRACA?", "`cd` do katalogu projektu albo `git init`."),
        B("! [rejected] main -> main (fetch first)", "Na GitHubie są commity, których nie masz (np. repo założone z README).", "Strona repozytorium — czy jest README?", "`git pull --rebase origin main`, potem `git push`. Na przyszłość zakładaj puste repozytorium."),
    ],
    pulapki=["Commit „wszystkiego” z opisem „zmiany” — po tygodniu nie wiesz, co zmieniłeś. Mały commit = jedna rzecz.",
             "Hasło lub token w repozytorium publicznym — boty skanują GitHub w ciągu minut."],
    zadania=["Skonfiguruj user.name i user.email.", "Utwórz repozytorium w PRACA, zrób commit z hello.py.", "Wyślij na GitHub i sprawdź stronę repozytorium."],
    pytania=[["Co robi git add?", "Dodaje zmiany do poczekalni — wybiera, co trafi do commita."],
             ["Różnica między commit a push?", "Commit zapisuje lokalnie; push wysyła commity na serwer (GitHub)."],
             ["Czy usunięcie pliku z hasłem nowym commitem usuwa hasło z historii?", "Nie — trzeba zmienić hasło."]],
    podsumowanie="Tworzysz repozytorium, zapisujesz commity (status → add → commit), czytasz historię i wysyłasz projekt na GitHub.",
    test=[T("Które polecenie dodaje plik do poczekalni?", ["git commit", "git add", "git push", "git log"], 1, "add → poczekalnia."),
          T("Co pokazuje git status?", ["historię commitów", "co zmienione i co w poczekalni", "adres GitHuba", "wersję Gita"], 1, "Stan katalogu i poczekalni."),
          T("Commit bez push:", ["jest na GitHubie", "jest tylko na Twoim komputerze", "znika po zamknięciu terminala", "jest błędem"], 1, "push wysyła na serwer."),
          T("Dobry opis commita:", ["zmiany", "asdf", "Dodaj walidację wieku w wiek.py", "commit 5"], 2, "Mówi, co i gdzie się zmieniło.")],
    w_praktyce=["Commit po każdym działającym kroku, push na koniec dnia.", "git status przed każdym commitem."],
    zrodla=[Z.GIT_PL, Z.GIT_PL_PODST, Z.GH_README],
)

ASYSTENT = L(
    id="nauka_z_asystentem", nazwa="Jak uczyć się z asystentem AI, żeby to Ty umiał programować", tydzien=0,
    slowa=["asystent", "AI", "prompt", "Claude", "offline", "API", "podpowiedź", "halucynacja", "prywatność", "CLAUDE.md"],
    cel="Po tej lekcji piszesz prompty, które uczą (wskazówka zamiast rozwiązania), wybierasz tryb asystenta w Mentorze (Offline, API, Claude Code), sprawdzasz odpowiedzi AI i chronisz swoje dane.",
    po_co="AI przyspiesza naukę albo ją zastępuje — zależy od pytania. Na rozmowie rekrutacyjnej i w pracy liczy się to, co umiesz wyjaśnić bez AI.",
    wymagania=["Mentor → zakładka Asystent.", "Katalog PRACA (Mój projekt → Utwórz katalog roboczy)."],
    wyjasnienie=(
        "## Trzy tryby asystenta w Mentorze\n"
        "| tryb | koszt | co potrafi |\n|---|---|---|\n"
        "| Offline | 0 zł, bez internetu | słowniczek kursu, wyjaśnienia błędów Pythona, podpowiedzi do zadań |\n"
        "| API | płatność za użycie (klucz z console.anthropic.com) | prawdziwa rozmowa z modelem, pliki przez @nazwa.py |\n"
        "| Claude Code | plan Pro lub wyższy | agent w terminalu w katalogu PRACA |\n"
        "Kurs przejdziesz w trybie Offline. Klucz API wpisujesz wyłącznie w Mentorze (zapis lokalny) — nigdy do pliku w repozytorium.\n"
        "## Prompt, który uczy\n"
        "ŹLE: „Napisz mi program kalkulator”. Dostajesz gotowy kod i niczego się nie uczysz.\n"
        "DOBRZE: „Uczę się if/elif. Mój kalkulator źle dzieli przez zero — oto kod i komunikat błędu. **Nie podawaj rozwiązania**, zadaj mi pytanie naprowadzające.”\n"
        "Schemat: **kontekst** (czego się uczę) + **co zrobiłem** (kod, błąd) + **czego chcę** (wskazówka / wyjaśnienie linii / przegląd) + **ograniczenie** (bez gotowca).\n"
        "## Drabina pomocy\n"
        "1 pytanie naprowadzające → 2 wskazanie fragmentu („zobacz linię 7”) → 3 częściowy przykład → 4 pełne rozwiązanie z omówieniem — dopiero gdy 1–3 nie pomogły.\n"
        "## AI się myli\n"
        "Model potrafi z pewnością podać nieistniejącą funkcję albo bibliotekę (tzw. halucynacja). Zasada: każdą nazwę funkcji sprawdzasz w dokumentacji Pythona, a każdy kod **uruchamiasz i testujesz**.\n"
        "## Prywatność\n"
        "Nie wklejaj do AI haseł, kluczy API, danych osobowych (PESEL, adresy) ani kodu firmy bez zgody. W kursie dane są fikcyjne.\n"
        "## CLAUDE.md — zasady na stałe\n"
        "Plik CLAUDE.md w katalogu projektu czyta Claude Code na początku każdej sesji. Mentor tworzy go przyciskiem (Mój projekt → „Utwórz CLAUDE.md z zasadami”). Wpisz tam np.: „Uczę się Pythona. Nie podawaj gotowych rozwiązań zadań. Tłumacz po polsku.”"),
    przyklad=("Prompt (dobry):\n"
              "Uczę się pętli while w Pythonie (tydzień 2 kursu).\n"
              "Mój program suma.py ma liczyć sumę liczb do wpisania 0, ale kręci się bez końca.\n"
              "Kod:\n"
              "    suma = 0\n"
              "    x = int(input(\"Liczba: \"))\n"
              "    while x != 0:\n"
              "        suma = suma + x\n"
              "    print(suma)\n"
              "Nie podawaj poprawionego kodu. Zadaj mi jedno pytanie, które pomoże znaleźć błąd.\n\n"
              "Odpowiedź asystenta (wskazówka):\n"
              "Co zmienia wartość zmiennej x wewnątrz pętli? Kiedy warunek x != 0 może stać się fałszywy?"),
    demonstracja={"tytul": "Jedna pomoc — cztery poziomy", "kroki": [
        "Kontekst: „Uczę się pętli while (tydzień 2)” — asystent dopasuje poziom wyjaśnienia.",
        "Co zrobiłem: kod i opis objawu („kręci się bez końca”). Bez kodu asystent zgaduje.",
        "Ograniczenie: „Nie podawaj poprawionego kodu” — chronisz swoją naukę.",
        "Odpowiedź to pytanie naprowadzające: x nie zmienia się w pętli, więc warunek zawsze jest prawdziwy. Sam(a) dopisujesz `x = int(input(\"Liczba: \"))` w środku pętli.",
        "Gdyby to nie pomogło: poziom 2 — „wskaż linię”, poziom 3 — „pokaż fragment”, poziom 4 — „pełne rozwiązanie z wyjaśnieniem każdej linii”.",
        "Na koniec: uruchom poprawiony program i przetestuj: 5, 3, 0 → suma 8."],
        "wynik": "Błąd znaleziony przez Ciebie, a w notatki.md zapisana reguła: „w pętli while coś musi zmieniać warunek”."},
    jak_uruchomic=["Mentor → Asystent → tryb Offline → wpisz pytanie, np. „co to jest pętla”.",
                   "Mentor → Prompty: gotowe szablony promptów do skopiowania (Nowy temat, Błąd, Przegląd kodu)."],
    cwiczenia=[
        C("prowadzone",
          "Oceń 3 prompty (dobry / zły): (1) „Zrób zadanie t1z2”; (2) „Uczę się if/elif. Oto mój kod i błąd ZeroDivisionError. Nie dawaj rozwiązania — wskaż, gdzie szukać”; (3) „Wyjaśnij linia po linii, co robi ten kod: …” Czas: 10 minut.",
          "(1) zły — prosi o gotowca; (2) dobry — kontekst, kod, błąd, ograniczenie; (3) dobry — prosi o wyjaśnienie.",
          ["Czy prompt prosi o naukę, czy o wynik?", "Dobry prompt ma kontekst i ograniczenie.", "Wyjaśnienie linia po linii to nauka."],
          "(1) zły; (2) dobry; (3) dobry.",
          [wy("a", "(1) „Zrób zadanie t1z2”", ["dobry", "zły"], "zły"), wy("b", "(2) kontekst + błąd + bez rozwiązania", ["dobry", "zły"], "dobry"),
           wy("c", "(3) wyjaśnij linia po linii", ["dobry", "zły"], "dobry")]),
        C("samodzielne",
          "Asystent napisał: „Użyj funkcji `lista.sum()`, żeby dodać elementy listy”. Uruchamiasz `[1, 2, 3].sum()` i widzisz `AttributeError: 'list' object has no attribute 'sum'`. (1) Czy asystent miał rację? (2) Jak poprawnie dodać elementy listy (wpisz wywołanie dla listy [1, 2, 3])? Czas: 10 minut.",
          "(1) nie — lista nie ma metody sum; (2) sum([1, 2, 3]) (funkcja wbudowana).",
          ["AttributeError mówi, że obiekt nie ma takiej metody.", "W Pythonie sum to funkcja wbudowana, nie metoda listy.", "Sprawdź w dokumentacji: Built-in Functions → sum."],
          "(1) nie — to halucynacja; (2) `sum([1, 2, 3])` zwraca 6. Lekcja: każdą nazwę z odpowiedzi AI sprawdzasz uruchomieniem lub w dokumentacji.",
          [wy("racja", "(1) Asystent miał rację?", ["tak", "nie"], "nie"), tx("wywolanie", "(2) Poprawne wywołanie", "sum([1, 2, 3])")]),
    ],
    typowe_bledy=[
        B("Kod od AI działa, ale nie wiesz dlaczego.", "Poziom 4 drabiny od razu.", "Spróbuj wyjaśnić 3 linie na głos.", "Poproś: „wyjaśnij linia po linii” i przepisz ręcznie."),
        B("AttributeError / ModuleNotFoundError w kodzie od AI.", "Halucynacja: nieistniejąca metoda lub biblioteka.", "Dokumentacja Pythona albo `help(obiekt)`.", "Zapytaj AI: „czy ta funkcja na pewno istnieje? podaj link do dokumentacji” i sprawdź sam."),
    ],
    pulapki=["Wklejanie kodu z kluczem API do czatu — klucz trzeba potem unieważnić.",
             "Wiara w pewny ton AI — pewność to nie dowód; dowodem jest uruchomiony test."],
    zadania=["Utwórz CLAUDE.md przyciskiem w Mój projekt i dopisz 3 własne zasady.", "Zadaj Asystentowi Offline pytanie o zmienną, funkcję i pętlę.", "Zapisz w notatki.md swój szablon dobrego promptu."],
    pytania=[["Jakie 4 elementy ma prompt, który uczy?", "Kontekst, co zrobiłem (kod/błąd), czego chcę, ograniczenie."],
             ["Czym jest halucynacja AI?", "Pewnie podana nieprawda, np. nieistniejąca funkcja."],
             ["Czego nie wklejasz do AI?", "Haseł, kluczy, danych osobowych, cudzego kodu bez zgody."]],
    podsumowanie="Prosisz o wskazówki zamiast gotowców, idziesz po drabinie pomocy, sprawdzasz każdą odpowiedź AI uruchomieniem i nie wysyłasz danych prywatnych.",
    test=[T("Najlepsza pierwsza prośba przy błędzie:", ["napisz poprawny kod", "zadaj mi pytanie naprowadzające", "usuń błąd", "przepisz cały program"], 1, "Poziom 1 drabiny."),
          T("AI podało nieistniejącą funkcję. To:", ["halucynacja", "nowa wersja Pythona", "błąd Windows", "funkcja ukryta"], 0, "Sprawdzaj w dokumentacji."),
          T("Gdzie wpisujesz klucz API?", ["do CLAUDE.md", "do kodu w repozytorium", "tylko w Mentorze (zapis lokalny)", "w README"], 2, "Nigdy do repozytorium."),
          T("Tryb asystenta bez internetu i opłat:", ["API", "Claude Code", "Offline", "żaden"], 2, "Offline w Mentorze.")],
    w_praktyce=["Każda rozmowa z AI kończy się Twoim uruchomieniem kodu i jednym zdaniem w notatki.md.", "Raz w tygodniu poproś asystenta o pytania sprawdzające z tematu tygodnia."],
    zrodla=[Z.CC_BEST, Z.CC_MEM, Z.PY_TUT_PL],
)
