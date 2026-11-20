# -*- coding: utf-8 -*-
"""Etap 2, tygodnie 8–9: testy jako umowa, debugowanie, refaktoryzacja; strona HTML/CSS, JavaScript, GitHub Pages."""

from wspolne import (TN, B, C, L, T, bl, kod, kw, li, tx, wy)

D = "dostęp 20.11.2026"
Z_PYTEST = ["pytest — Get started (oficjalna dokumentacja)", "https://docs.pytest.org/en/stable/getting-started.html", D]
Z_PYTEST_RAISES = ["pytest — How to write and report assertions (pytest.raises)", "https://docs.pytest.org/en/stable/how-to/assert.html", D]
Z_PYTEST_PARAM = ["pytest — Parametrizing tests", "https://docs.pytest.org/en/stable/how-to/parametrize.html", D]
Z_CC_BEST = ["Claude Code — Best practices (test-driven, weryfikacja)", "https://code.claude.com/docs/en/best-practices", "dostęp 19.11.2026"]
Z_PY_PDB = ["Python — pdb i breakpoint() (oficjalna dokumentacja)", "https://docs.python.org/3/library/pdb.html", D]
Z_PY_FAQ_DEF = ["Python FAQ — Why are default values shared between objects? (mutowalne wartości domyślne)", "https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects", D]
Z_FOWLER = ["Martin Fowler — Refactoring (definicja i katalog refaktoryzacji)", "https://refactoring.com/", D]
Z_PEP8 = ["PEP 8 — Style Guide for Python Code", "https://peps.python.org/pep-0008/", D]
Z_MDN_HTML = ["MDN — Podstawy HTML (Learn web development)", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content", D]
Z_MDN_CSS = ["MDN — Podstawy CSS i media queries", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics", D]
Z_MDN_JS = ["MDN — JavaScript: zdarzenia i DOM (Learn web development)", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting", D]
Z_MDN_FORM = ["MDN — Formularze w HTML (label, input)", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms", D]
Z_WCAG = ["W3C — WCAG 2.2 w skrócie (Web Content Accessibility Guidelines)", "https://www.w3.org/WAI/standards-guidelines/wcag/", D]
Z_GH_PAGES = ["GitHub Docs — What is GitHub Pages? / Quickstart", "https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages", D]
Z_GH_PAGES_LIM = ["GitHub Docs — GitHub Pages limits (1 GB, 100 GB/mies., 10 min)", "https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits", "dostęp 19.11.2026"]


# =========================================================================== TYDZIEŃ 8
TESTY = L(
    id="testy_umowa", nazwa="Testy jako umowa z agentem: pytest od zera", tydzien=8,
    slowa=["pytest", "test", "assert", "pytest.raises", "parametrize", "TDD", "mutant", "umowa"],
    cel="Po tej lekcji piszesz testy pytest (assert, pytest.raises, parametrize) dla specyfikacji, uruchamiasz je i używasz ich jako umowy: agent dostaje czerwone testy i ma je zazielenić bez ich zmieniania.",
    po_co="Dokumentacja Claude Code nazywa dawanie agentowi sposobu weryfikacji (testów) najskuteczniejszą praktyką. Testy, które piszesz Ty, to Twoja kontrola nad kodem, którego nie piszesz.",
    wymagania=["Środowisko kursu (pytest jest zainstalowany przez Mentora).", "Lekcja „Specyfikacja” (przykłady wejście → wynik)."],
    wyjasnienie=(
        "## Test w pytest\n"
        "Plik `test_cennik.py`, funkcje zaczynające się od `test_`, w środku `assert warunek`. pytest sam znajduje takie pliki i funkcje:\n"
        "```\nfrom cennik import cena_pokoju\n\ndef test_lipowy_w_lipcu():\n    assert cena_pokoju(\"Lipowy\", 7) == 180\n```\n"
        "Uruchomienie w terminalu Mentora: `python -m pytest -q` (wszystkie testy) albo `python -m pytest -q test_cennik.py -k lipowy` (wybrane). Wynik: kropka = przeszedł, F = nie przeszedł z pokazaniem oczekiwanej i otrzymanej wartości.\n"
        "## Trzy narzędzia na start\n"
        "| narzędzie | do czego | przykład |\n"
        "|---|---|---|\n"
        "| `assert` | wynik równy oczekiwanemu | `assert oplata_klimatyczna(2, 3) == 15.0` |\n"
        "| `pytest.raises` | funkcja ma odmówić | `with pytest.raises(ValueError): cena_pokoju(\"Brzozowy\", 7)` |\n"
        "| `@pytest.mark.parametrize` | ta sama reguła, wiele danych | jedna funkcja testu, tabela 8 przypadków |\n"
        "Liczby z przecinkiem porównuj z tolerancją: `assert wynik == pytest.approx(629.94)`.\n"
        "## Testy przed kodem (TDD w wersji vibe)\n"
        "- Ze specyfikacji piszesz testy (sam albo z agentem w osobnej prośbie: „napisz TYLKO testy do specyfikacji, nie implementuj”).\n"
        "- Uruchamiasz — czerwone (kodu jeszcze nie ma). To dowód, że test cokolwiek sprawdza.\n"
        "- Prośba do agenta: „Zaimplementuj tak, żeby przeszły testy test_cennik.py. Nie zmieniaj testów.”\n"
        "- Zielone → przegląd kodu → commit (kod i testy razem).\n"
        "## Czy test w ogóle coś łapie? (mutanty)\n"
        "Test, który przechodzi zawsze, jest bezwartościowy. Sprawdzian: celowo zepsuj kod (zmień `>=` na `>`, usuń `raise`) — dobry test robi się czerwony. Taki zepsuty wariant nazywa się mutantem. "
        "Zadanie tygodnia sprawdza Twoje testy właśnie tak: uruchamia je na poprawnym cenniku (muszą przejść) i na trzech mutantach (każdy musi zostać złapany).\n"
        "## Co testować\n"
        "- Przykłady ze specyfikacji (szczęśliwa ścieżka).\n"
        "- Granice (pierwszy i ostatni miesiąc sezonu, 0 dzieci).\n"
        "- Odmowy (ValueError dla złych danych).\n"
        "- Jedna rzecz na test, nazwa mówi co: `test_dzieci_nie_placa_oplaty`.\n"
        "## Testy Mentora a Twoje testy\n"
        "Testy z WERYFIKATORY to niezależny egzamin — agent ich nie widzi w Twoim projekcie i nie zmieni. Twoje testy (test_*.py w PRACA) są częścią projektu i trafiają do Gita oraz do CI (tydzień 13)."),
    przyklad=kod("testy_umowa:przyklad",
                 "import pytest\n\n\ndef oplata_klimatyczna(dorosli, noce, dzieci=0):\n    if dorosli < 0 or noce < 1 or dzieci < 0:\n        raise ValueError(\"złe dane\")\n    return round(dorosli * noce * 2.5, 2)\n\n\n"
                 "@pytest.mark.parametrize(\"dorosli, noce, dzieci, oczekiwane\", [\n    (2, 3, 0, 15.0),\n    (1, 1, 0, 2.5),\n    (2, 2, 3, 10.0),   # dzieci nie płacą\n])\n"
                 "def test_oplata(dorosli, noce, dzieci, oczekiwane):\n    assert oplata_klimatyczna(dorosli, noce, dzieci) == oczekiwane\n\n\n"
                 "def test_zero_nocy_odmowa():\n    with pytest.raises(ValueError):\n        oplata_klimatyczna(2, 0)\n\n\n"
                 "if __name__ == \"__main__\":\n    print(oplata_klimatyczna(2, 3), oplata_klimatyczna(2, 2, 3))\n",
                 "15.0 10.0\n"),
    demonstracja={"tytul": "Testy łapią mutanta", "kroki": [
        "Zapisz przykład jako test_oplata.py w PRACA. `python -m pytest -q test_oplata.py` → „4 passed” (3 przypadki parametrize + 1 test odmowy).",
        "Mutant 1: zmień `dorosli * noce * 2.5` na `(dorosli + dzieci) * noce * 2.5`. Uruchom: przypadek (2, 2, 3) czerwony — test złapał, że dzieci zaczęły płacić.",
        "Mutant 2: usuń `noce < 1 or`. test_zero_nocy_odmowa czerwony — „DID NOT RAISE ValueError”.",
        "Mutant 3: zaokrąglanie do 1 miejsca. Testy dalej zielone! Żaden przykład nie ma groszy — to luka w testach. Dopisujesz przypadek (1, 3, 0, 7.5) — wciąż zielono (7.5 ma jedno miejsce). Dopiero stawka 2.35 zł ujawniłaby różnicę — zapisujesz to jako wniosek o doborze danych testowych.",
        "Przywróć kod. Wniosek: testy są tak dobre, jak dane, które w nich wymyślisz."],
        "wynik": "Dwa mutanty złapane, jeden przeżył — wiesz, jak sprawdzić, czy testy naprawdę czegoś pilnują."},
    jak_uruchomic=["Terminal Mentora w PRACA: `python -m pytest -q` albo `python -m pytest -q plik_testu.py -k fragment_nazwy`.", "Zadanie z paskiem → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Wynik pytest: `..F.F` i na końcu `2 failed, 3 passed`. (1) Ile testów uruchomiono? (2) Który z kolei test (numer) pierwszy nie przeszedł? (3) Test sprawdza `cena_pokoju(\"Klonowy\", 12) == 200`, a funkcja zwraca 150. "
          "Co najpewniej jest nie tak w kodzie — miesiąc 12 nie jest traktowany jako sezon wysoki (tak/nie)? Czas: 15 minut.",
          "(1) 5; (2) trzeci; (3) tak — grudzień potraktowany jak sezon niski (150 to cena niska Klonowego).",
          ["Każdy znak to jeden test.", "F na trzeciej pozycji.", "200 to cena wysoka, 150 niska — który sezon policzyła funkcja?"],
          "5 testów, pierwszy F na pozycji 3; 150 = cena sezonu niskiego → w kodzie brakuje 12 na liście sezonu wysokiego.",
          [li("ile", "(1) Liczba testów", 5), li("ktory", "(2) Numer pierwszego czerwonego", 3), wy("sezon", "(3) Grudzień potraktowany jako niski?", TN, "tak")]),
        C("samodzielne",
          "Napisz w myślach test odmowy: funkcja `cena_pokoju(\"Brzozowy\", 7)` ma rzucić ValueError. Która linia otwiera blok sprawdzający wyjątek? Wpisz ją dokładnie (bez dwukropka też zaliczy). "
          "Drugie: mutant zamienia `>=` na `>` w warunku „od 7 nocy rabat”. Jaką liczbę nocy MUSI zawierać test, żeby go złapać? Czas: 15 minut.",
          "`with pytest.raises(ValueError):`; test musi zawierać dokładnie 7 nocy.",
          ["Blok z kontekstem zaczyna się od with.", "Funkcja pomocnicza pytest dla wyjątków ma w nazwie „raises”.", "Różnica >= i > ujawnia się tylko na samej granicy."],
          "`with pytest.raises(ValueError):` + wywołanie w środku; mutant >= → > złapie tylko przypadek 7 nocy.",
          [tx("with", "Linia otwierająca blok", ["with pytest.raises(ValueError):"], zawiera=["pytest.raises(ValueError"]), li("noce", "Liczba nocy w teście", 7)]),
    ],
    typowe_bledy=[
        B("„ModuleNotFoundError: No module named 'cennik'” przy pytest.", "pytest uruchomiony z innego folderu niż plik cennik.py.", "`cd` — czy jesteś w PRACA?", "Uruchamiaj `python -m pytest` w katalogu z plikami (terminal Mentora otwiera się w PRACA)."),
        B("„collected 0 items”.", "Plik albo funkcje nie zaczynają się od test_.", "Nazwy pliku i funkcji.", "test_cennik.py, def test_…()."),
        B("assert 0.30000000000000004 == 0.3 nie przechodzi.", "Liczby zmiennoprzecinkowe.", "Czy porównujesz float?", "`== pytest.approx(0.3)` albo zaokrąglenie w kodzie do groszy."),
    ],
    pulapki=["Testy napisane przez agenta do kodu napisanego przez agenta często sprawdzają to, co kod robi, a nie to, co powinien. Przykłady w testach bierzesz ze SPECYFIKACJI.",
             "Zielone testy po zmianie testów to nie sukces — sprawdź diff plików test_*."],
    zadania=["Napisz test_cennik.py, który łapie 3 mutanty (zadanie tygodnia).", "Przećwicz własnego mutanta na kalkulator_pobytu.py.", "Dopisz do AGENTS.md: „testy piszemy ze specyfikacji; nie zmieniaj test_*.py bez pytania”."],
    pytania=[["Po co sprawdzać testy mutantami?", "Żeby upewnić się, że test wykrywa błąd — test, który zawsze przechodzi, niczego nie pilnuje."],
             ["Jak testujesz, że funkcja rzuca wyjątek?", "with pytest.raises(ValueError): wywołanie."], ["Skąd bierzesz przykłady do testów?", "Ze specyfikacji, nie z zachowania istniejącego kodu."]],
    podsumowanie="Piszesz testy pytest z assert, raises i parametrize, uruchamiasz je, sprawdzasz mutantami i używasz jako umowy z agentem.",
    test=[T("pytest znajduje testy w funkcjach, których nazwa zaczyna się od:", ["check_", "test_", "spr_", "assert_"], 1, "I w plikach test_*.py."),
          T("Mutant to:", ["Nowa funkcja", "Celowo zepsuty wariant kodu do sprawdzenia testów", "Błąd pytest", "Biblioteka"], 1, "Dobry test go łapie."),
          T("Porównanie liczb z przecinkiem w teście:", ["==", "pytest.approx", "is", "str()"], 1, "Tolerancja."),
          T("Prośba do agenta przy TDD:", ["Napisz kod i testy, jak chcesz", "Zaimplementuj tak, żeby przeszły testy; nie zmieniaj testów", "Usuń testy", "Pomiń czerwone"], 1, "Testy to umowa.")],
    w_praktyce=["Każda funkcja w projekcie ma co najmniej jeden test granicy i jeden odmowy.", "Raz na jakiś czas — ręczny mutant."],
    zrodla=[Z_PYTEST, Z_PYTEST_RAISES, Z_PYTEST_PARAM, Z_CC_BEST],
)

DEBUG = L(
    id="debugowanie", nazwa="Debugowanie z AI: odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem", tydzien=8,
    slowa=["debugowanie", "odtworzenie", "hipoteza", "print", "breakpoint", "pdb", "regresja", "minimalny przykład"],
    cel="Po tej lekcji prowadzisz debugowanie metodą 5 kroków (odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem) i używasz AI jako partnera do hipotez — nie jako maszyny do losowych poprawek.",
    po_co="Ankieta Stack Overflow 2025: 45% programistów mówi, że debugowanie kodu wygenerowanego przez AI zajmuje więcej czasu niż się spodziewali. Metoda skraca ten czas.",
    wymagania=["Lekcje „Komunikat błędu”, „Gdy agent się myli”, „Testy jako umowa”."],
    wyjasnienie=(
        "## Pięć kroków\n"
        "| krok | pytanie | narzędzie |\n"
        "|---|---|---|\n"
        "| 1. Odtwórz | czy umiem wywołać błąd na żądanie? | dokładne dane i polecenie |\n"
        "| 2. Zawęź | najmniejszy przykład, który nadal psuje | usuwanie kawałków danych/kodu |\n"
        "| 3. Wyjaśnij | dlaczego dokładnie tak się dzieje? | print, breakpoint(), traceback, AI: hipotezy |\n"
        "| 4. Napraw | jedna zmiana przyczyny | agent lub Ty |\n"
        "| 5. Zabezpiecz | czy błąd nie wróci? | test regresji z przykładem z kroku 2 |\n"
        "## Krok 1–2: błąd, którego nie umiesz powtórzyć, nie jest naprawiony\n"
        "Zgłoszenie „czasem liczy źle” zamieniasz w „dla rezerwacji 20.12–23.12 i 2 osób zwraca 0”. Potem zmniejszasz: czy przy 1 rezerwacji też? czy bez dzieci też? Minimalny przykład to połowa sukcesu — i idealny materiał dla agenta.\n"
        "## Krok 3: patrzenie do środka\n"
        "- `print(f\"{zmienna=}\")` — wypisuje nazwę i wartość (np. `noce=0`). Usuń po naprawie.\n"
        "- `breakpoint()` — zatrzymuje program w tym miejscu (debugger pdb): `p zmienna` wypisuje, `n` następna linia, `c` dalej, `q` koniec.\n"
        "- Agent w trybie diagnozy: „Nie zmieniaj plików. Dla tego minimalnego przykładu wyjaśnij krok po kroku, co dzieje się w funkcji, i wskaż linię, w której wartość staje się zła.”\n"
        "## Dwa podstępne błędy, które AI lubi popełniać\n"
        "- Mutowalna wartość domyślna: `def dodaj(r, lista=[])` — lista tworzy się RAZ i jest wspólna dla wszystkich wywołań (oficjalne FAQ Pythona). Objaw: dane „przeciekają” między wywołaniami. Poprawka: `lista=None` i w środku `if lista is None: lista = []`.\n"
        "- Format daty: `\"%m.%d.%Y\"` zamiast `\"%d.%m.%Y\"` — dla 05.07.2026 nie ma błędu, tylko zła data (7 maja zamiast 5 lipca). Dla 20.12.2026 — ValueError. Objaw: błąd „tylko dla niektórych dat”.\n"
        "## Krok 5: test regresji\n"
        "Minimalny przykład z kroku 2 zamieniasz w test: `def test_dwa_wywolania_nie_dziela_listy(): …`. Jeśli kiedyś agent przywróci błąd, test go złapie. Regresja = powrót naprawionego błędu."),
    przyklad=kod("debugowanie:przyklad",
                 "def dodaj_rezerwacje(r, lista=[]):\n    lista.append(r)\n    return lista\n\n"
                 "print(dodaj_rezerwacje(\"Anna\"))\nprint(dodaj_rezerwacje(\"Piotr\"))   # oczekujesz ['Piotr']…\n",
                 "['Anna']\n['Anna', 'Piotr']\n"),
    demonstracja={"tytul": "Błąd „tylko w grudniu” — od zgłoszenia do testu regresji", "kroki": [
        "Zgłoszenie klientki: „import rezerwacji wywala się przy grudniowych”. Odtwarzasz: wczytaj_rezerwacje([\"Anna;Lipowy;20.12.2026;23.12.2026\"]) → ValueError: time data '20.12.2026' does not match format '%m.%d.%Y'.",
        "Zawężasz: \"05.07.2026\" nie wywołuje błędu. Sprawdzasz wynik: 2026-05-07 — maj zamiast lipca! Błąd był zawsze, wybuchał tylko dla dni > 12.",
        "Wyjaśnienie: format ma miesiąc i dzień zamienione. To nie „błąd grudnia”, tylko cichy błąd każdej daty.",
        "Naprawa: \"%d.%m.%Y\". Test regresji: wczytanie \"05.07.2026\" daje date(2026, 7, 5) oraz \"20.12.2026\" działa.",
        "Wniosek: ciche złe dane są groźniejsze niż wyjątek — dlatego testy sprawdzają WYNIK, nie tylko brak błędu."],
        "wynik": "Błąd zdiagnozowany jako zamiana dnia z miesiącem, naprawiony jedną zmianą i zabezpieczony testem dla dnia ≤ 12 i > 12."},
    jak_uruchomic=["Zadanie tygodnia „debug_rezerwacje.py” → „📄 Otwórz przykład” → 5 kroków → „✔ Sprawdź wynik”.", "`breakpoint()` działa po uruchomieniu w terminalu Mentora (`python plik.py`)."],
    cwiczenia=[
        C("prowadzone",
          "Co wypisze przykład lekcji (dwie linie)? Wpisz drugą linię dokładnie. Ile elementów będzie miała lista po trzecim wywołaniu `dodaj_rezerwacje(\"Ewa\")`? Czas: 15 minut.",
          "Druga linia: ['Anna', 'Piotr']; po trzecim wywołaniu 3 elementy.",
          ["Lista domyślna tworzy się raz, przy definicji funkcji.", "Każde wywołanie bez listy dopisuje do tej samej.", "Anna, Piotr, Ewa."],
          "Wspólna lista: ['Anna'], potem ['Anna', 'Piotr'], potem 3 elementy.",
          [tx("l2", "Druga linia", ["['Anna', 'Piotr']"], bledy=[bl("['Piotr']", "lista domyślna jest wspólna dla wywołań — Anna nadal w niej jest")]), li("ile", "Elementy po 3. wywołaniu", 3)]),
        C("samodzielne",
          "Funkcja parsuje datę formatem \"%m.%d.%Y\". Dla wejścia \"05.07.2026\": (1) czy będzie wyjątek (tak/nie)? (2) Jaki miesiąc (numer) wyjdzie w dacie? (3) Dla \"20.12.2026\" — jaki wyjątek? Czas: 15 minut.",
          "(1) nie; (2) 5 (maj); (3) ValueError.",
          ["%m to miesiąc, %d dzień — tu na odwrót.", "05 trafia jako miesiąc.", "Miesiąc 20 nie istnieje."],
          "Bez wyjątku, ale miesiąc 5 zamiast 7 (cichy błąd); dla 20.12 — ValueError (miesiąc 20).",
          [wy("w", "(1) Wyjątek dla 05.07.2026?", TN, "nie"), li("mies", "(2) Miesiąc w wyniku", 5, bledy=[bl(7, "format ma %m na pierwszym miejscu — 05 staje się miesiącem")]),
           tx("wyj", "(3) Wyjątek dla 20.12.2026", ["ValueError"])]),
    ],
    typowe_bledy=[
        B("Dane z poprzedniego wywołania „pojawiają się” w nowym.", "Mutowalna wartość domyślna (lista=[] / słownik={}).", "Szukaj `=[]` i `={}` w linii def.", "`lista=None` + `if lista is None: lista = []`."),
        B("Błąd „tylko czasem”.", "Zależność od danych (dzień > 12, pusty wiersz, polski znak).", "Zbierz 2 przykłady: działający i psujący — czym się różnią?", "Minimalny przykład → hipoteza → test."),
        B("Program zatrzymał się z (Pdb) i nie reaguje.", "breakpoint() został w kodzie.", "Szukaj breakpoint( w plikach.", "`c` kontynuuje, `q` kończy; usuń breakpoint przed commitem."),
    ],
    pulapki=["„Napraw” bez odtworzenia to zgadywanie — także dla agenta.", "Tymczasowe print i breakpoint nie trafiają do commita — sprawdź diff."],
    zadania=["Napraw debug_rezerwacje.py metodą 5 kroków (zadanie tygodnia).", "Dopisz 2 testy regresji do własnego test_*.py.", "W dzienniku: minimalny przykład każdego błędu."],
    pytania=[["Jakie jest 5 kroków debugowania?", "Odtwórz, zawęź, wyjaśnij, napraw, zabezpiecz testem."], ["Dlaczego lista=[] jako wartość domyślna jest groźna?", "Tworzy się raz i jest współdzielona między wywołaniami."],
             ["Co to jest test regresji?", "Test, który pilnuje, żeby naprawiony błąd nie wrócił."]],
    podsumowanie="Debugujesz metodą 5 kroków, używasz print/breakpoint i AI do hipotez, znasz pułapki mutowalnych wartości domyślnych i formatów dat, zabezpieczasz naprawę testem.",
    test=[T("Pierwszy krok debugowania:", ["Napraw", "Odtwórz błąd na żądanie", "Zmień model AI", "Usuń test"], 1, "Bez odtworzenia nie wiesz, czy naprawiłeś."),
          T("`print(f\"{noce=}\")` wypisze dla noce = 3:", ["3", "noce=3", "{noce=}", "Błąd"], 1, "Nazwa i wartość."),
          T("`def f(x, wynik=[])` grozi:", ["Błędem składni", "Współdzieloną listą między wywołaniami", "Wolnym działaniem", "Niczym"], 1, "FAQ Pythona."),
          T("Format daty dzień.miesiąc.rok w strptime:", ["%m.%d.%Y", "%d.%m.%Y", "%Y.%d.%m", "%D.%M.%Y"], 1, "Polski zapis.")],
    w_praktyce=["Każde zgłoszenie błędu od klienta → minimalny przykład → test.", "Agent dostaje minimalny przykład, nie cały log."],
    zrodla=[Z_PY_PDB, Z_PY_FAQ_DEF, ["Python — datetime.strptime: kody formatu (%d, %m, %Y)", "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes", D],
            ["Stack Overflow Developer Survey 2025 — AI (debugowanie kodu AI czasochłonne)", "https://survey.stackoverflow.co/2025/ai", D]],
)

REFAKTOR = L(
    id="refaktoryzacja", nazwa="Refaktoryzacja z agentem: lepszy kod, to samo zachowanie", tydzien=8,
    slowa=["refaktoryzacja", "czytelność", "duplikacja", "funkcja", "nazwa", "docstring", "zachowanie", "testy charakteryzujące"],
    cel="Po tej lekcji zlecasz agentowi refaktoryzację pod osłoną testów: najpierw testy utrwalające obecne zachowanie, potem małe zmiany struktury (nazwy, funkcje, usuwanie powtórzeń) bez zmiany wyników.",
    po_co="Kod od AI szybko rośnie i się powtarza. Refaktoryzacja utrzymuje projekt czytelnym dla Ciebie, klienta i kolejnych sesji agenta (krótszy kod = mniej kontekstu).",
    wymagania=["Lekcja „Testy jako umowa”.", "Plik raport_obroty.py z materiałów (zadanie tygodnia)."],
    wyjasnienie=(
        "## Definicja\n"
        "Martin Fowler: refaktoryzacja to zmiana wewnętrznej struktury kodu, która ułatwia jego zrozumienie i modyfikację, BEZ zmiany zachowania widocznego z zewnątrz. "
        "Jeśli zmienia się wynik — to nie refaktoryzacja, tylko nowa funkcja albo błąd.\n"
        "## Najpierw siatka: testy charakteryzujące\n"
        "Zanim ruszysz brzydki, ale działający kod, utrwal jego zachowanie testami: uruchom funkcje na kilku danych, zapisz wyniki jako asserty. To testy charakteryzujące — opisują, co kod ROBI (nawet jeśli to dziwne). "
        "Po refaktoryzacji muszą przejść bez zmian.\n"
        "## Sygnały, że kod trzeba uporządkować\n"
        "| sygnał | przykład | ruch |\n"
        "|---|---|---|\n"
        "| powtórzony blok | ten sam kod sumowania w 3 miejscach | wydziel funkcję |\n"
        "| długa funkcja | > 25–30 linii, kilka poziomów if/for | podziel na kroki |\n"
        "| tajemnicze nazwy | `x`, `tmp2`, `dane_new` | nazwa mówi, co to jest |\n"
        "| magiczne liczby | `* 0.9`, `if m in (6, 7, 8, 12)` w wielu miejscach | stała z nazwą: `RABAT_DLUGI = 0.10` |\n"
        "| zmienne globalne zmieniane w funkcjach | `WYNIKI.append(...)` | parametry i return |\n"
        "| martwy kod | zakomentowane stare wersje, nieużywane funkcje | usuń — historia jest w Gicie |\n"
        "## Prośba do agenta\n"
        "„Refaktoryzacja raport_obroty.py: usuń powtórzenia, podziel funkcje dłuższe niż 25 linii, nadaj czytelne nazwy, dodaj docstringi. Zachowanie BEZ ZMIAN: testy test_raport_obroty.py muszą przejść bez modyfikacji. "
        "Małe kroki: po każdej zmianie uruchom testy. Nie dodawaj zależności.”\n"
        "## Jak sprawdzisz efekt\n"
        "- Testy zielone bez zmian w plikach test_*.\n"
        "- Diff: więcej usuniętych linii niż dodanych to dobry znak (ale nie reguła).\n"
        "- Umiesz każdą funkcję opisać jednym zdaniem — docstring.\n"
        "- PEP 8 (oficjalny przewodnik stylu Pythona): nazwy funkcji małymi literami z podkreśleniami, 4 spacje wcięcia."),
    przyklad=("Przed:\n\n"
              "def r(d):\n    s = 0\n    for x in d:\n        if x['m'] in (6, 7, 8, 12):\n            s = s + x['n'] * 150 * 0.9 if x['n'] >= 7 else s + x['n'] * 150\n        else:\n            s = s + x['n'] * 110 * 0.9 if x['n'] >= 7 else s + x['n'] * 110\n    return s\n\n"
              "Po:\n\n"
              "SEZON_WYSOKI = (6, 7, 8, 12)\nRABAT_DLUGI = 0.10\n\n"
              "def cena_nocy(miesiac):\n    \"\"\"Cena za osobę za noc zależna od sezonu.\"\"\"\n    return 150 if miesiac in SEZON_WYSOKI else 110\n\n"
              "def koszt(rezerwacja):\n    \"\"\"Koszt jednej rezerwacji z rabatem od 7 nocy.\"\"\"\n    k = rezerwacja['n'] * cena_nocy(rezerwacja['m'])\n    return k * (1 - RABAT_DLUGI) if rezerwacja['n'] >= 7 else k\n\n"
              "def przychod(rezerwacje):\n    \"\"\"Suma kosztów wszystkich rezerwacji.\"\"\"\n    return sum(koszt(r) for r in rezerwacje)"),
    demonstracja={"tytul": "Refaktoryzacja pod osłoną testów", "kroki": [
        "Testy charakteryzujące: dla 3 zestawów danych zapisujesz obecne wyniki r(d) w test_przychod.py. Zielone.",
        "Krok 1 (agent): wydziel cena_nocy i stałe. Testy zielone. Commit.",
        "Krok 2: wydziel koszt(rezerwacja). Testy zielone. Commit.",
        "Krok 3: przemianuj r → przychod. Testy czerwone — test woła r! Decyzja: zostawiasz alias `r = przychod` na czas przejścia albo świadomie aktualizujesz test (to Twoja decyzja, nie agenta) i zapisujesz w opisie commita.",
        "Diff całości: −9 / +12 linii, ale każda funkcja ma jedną odpowiedzialność i opis."],
        "wynik": "Ten sam wynik dla wszystkich danych testowych, czytelniejszy kod w 3 commitach, świadoma decyzja o zmianie nazwy."},
    jak_uruchomic=["Zadanie tygodnia „raport_obroty.py” → testy charakteryzujące (w materiałach) → refaktoryzacja z agentem → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Czy to refaktoryzacja (tak/nie)? (1) zmiana nazwy funkcji `r` na `przychod` z zachowaniem wyników, (2) zmiana rabatu z 10% na 15%, (3) wydzielenie powtórzonego bloku do funkcji, (4) „przy okazji” poprawienie błędu zaokrąglenia, który zmienia wynik o 1 grosz. Ile odpowiedzi „tak”? Czas: 15 minut.",
          "Tak: 1 i 3 → 2 odpowiedzi „tak”; 2 i 4 zmieniają zachowanie (to zmiana funkcji / poprawka błędu — osobny commit).",
          ["Pytanie kontrolne: czy zmienił się wynik dla jakichkolwiek danych?", "Zmiana rabatu zmienia wynik.", "Poprawka błędu też zmienia wynik — może być dobra, ale to nie refaktoryzacja."],
          "Refaktoryzacja: 1 i 3 (wyniki bez zmian) = 2. Zmiana rabatu i poprawka zaokrąglenia zmieniają zachowanie — osobne, świadome commity.",
          [li("ile", "Liczba „tak”", 2, bledy=[bl(3, "poprawka błędu zmienia wynik — rób ją osobnym commitem z testem, nie w ramach refaktoryzacji")]),
           wy("r4", "(4) poprawka zaokrąglenia to refaktoryzacja?", TN, "nie")]),
        C("samodzielne",
          "W kodzie liczba `0.9` występuje 4 razy, a `(6, 7, 8, 12)` — 3 razy. Ile stałych z nazwą warto utworzyć? Jaką nazwę według PEP 8 nadasz funkcji „oblicz przychód miesięczny”: `ObliczPrzychod`, `oblicz_przychod_miesieczny`, `OBLICZ`? Czas: 15 minut.",
          "2 stałe (np. RABAT_DLUGI i SEZON_WYSOKI); funkcja: oblicz_przychod_miesieczny.",
          ["Każda powtarzana „magiczna” wartość → jedna stała.", "Stałe wielkimi literami, funkcje małymi z podkreśleniami.", "PEP 8: lowercase_with_underscores dla funkcji."],
          "Dwie stałe; nazwa funkcji oblicz_przychod_miesieczny (PEP 8).",
          [li("stale", "Liczba stałych", 2), wy("nazwa", "Nazwa funkcji", ["ObliczPrzychod", "oblicz_przychod_miesieczny", "OBLICZ"], "oblicz_przychod_miesieczny")]),
    ],
    typowe_bledy=[
        B("Po refaktoryzacji testy czerwone, agent proponuje „zaktualizować testy”.", "Zmieniło się zachowanie albo nazwy publicznych funkcji.", "Który test i dlaczego?", "Cofnij krok; jeśli zmiana nazwy jest celowa — Twoja decyzja i alias albo świadoma aktualizacja testu."),
        B("Agent przepisał plik od nowa „czyściej”, testy zielone, ale diff ma 300 linii.", "Za duży krok.", "git diff --stat.", "Cofnij, prośba o refaktoryzację krok po kroku, commit po każdym."),
    ],
    pulapki=["Refaktoryzacja bez testów to zmiana na ślepo — najpierw testy charakteryzujące.", "Nie łącz refaktoryzacji z nowymi funkcjami w jednym commicie — przegląd staje się niemożliwy."],
    zadania=["Zrefaktoryzuj raport_obroty.py pod osłoną testów (zadanie tygodnia).", "Znajdź w swoim projekcie 2 magiczne liczby i zamień na stałe.", "Dodaj docstringi do 3 funkcji."],
    pytania=[["Czym jest refaktoryzacja?", "Zmianą struktury kodu bez zmiany zachowania widocznego z zewnątrz."], ["Po co testy charakteryzujące?", "Utrwalają obecne zachowanie, żeby refaktoryzacja go nie zmieniła."],
             ["Dlaczego martwy kod usuwasz zamiast komentować?", "Bo historia jest w Gicie, a martwy kod myli ludzi i agentów oraz zużywa kontekst."]],
    podsumowanie="Refaktoryzujesz pod osłoną testów charakteryzujących, małymi krokami, z czytelnymi nazwami, stałymi i docstringami — wynik się nie zmienia.",
    test=[T("Refaktoryzacja zmienia:", ["Wyniki programu", "Strukturę kodu bez zmiany zachowania", "Wymagania klienta", "Testy"], 1, "Fowler."),
          T("Zanim zrefaktoryzujesz kod bez testów:", ["Piszesz testy charakteryzujące", "Usuwasz go", "Zmieniasz język", "Nic"], 0, "Siatka bezpieczeństwa."),
          T("Magiczna liczba to:", ["Liczba losowa", "Wartość bez nazwy powtarzana w kodzie", "Błąd składni", "Liczba pierwsza"], 1, "Zamień na stałą z nazwą."),
          T("Nazwa funkcji zgodna z PEP 8:", ["ObliczKoszt", "oblicz_koszt", "OBLICZKOSZT", "oblicz-koszt"], 1, "lowercase_with_underscores.")],
    w_praktyce=["Raz w tygodniu 30 minut refaktoryzacji z testami.", "Osobne commity: refaktoryzacja / nowa funkcja / poprawka."],
    zrodla=[Z_FOWLER, Z_PEP8, Z_CC_BEST],
)


# =========================================================================== TYDZIEŃ 9
STRONA = L(
    id="strona_html_css", nazwa="Strona internetowa: HTML (treść) i CSS (wygląd), także na telefonie", tydzien=9,
    slowa=["HTML", "CSS", "znacznik", "formularz", "label", "viewport", "media query", "alt", "dostępność"],
    cel="Po tej lekcji czytasz i zlecasz stronę HTML z poprawną strukturą (lang, title, viewport, nagłówki, formularz z etykietami, alt obrazków) i prostym CSS, który działa na telefonie.",
    po_co="Strona to najczęstsze pierwsze zlecenie vibe codera. Agent ją wygeneruje w minutę — Ty sprawdzasz, czy jest poprawna, dostępna i czytelna na telefonie.",
    wymagania=["Przeglądarka (Edge/Chrome/Firefox).", "Edytor (VS Code zalecany).", "Lekcje etapu 1 (agent, Git)."],
    wyjasnienie=(
        "## HTML — szkielet i treść\n"
        "HTML opisuje, CZYM jest każdy fragment strony, za pomocą znaczników: `<h1>Tytuł</h1>`, `<p>akapit</p>`, `<a href=\"…\">link</a>`. Przeglądarka czyta plik index.html i rysuje stronę.\n"
        "```\n<!DOCTYPE html>\n<html lang=\"pl\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n  <title>Pod Lipą — agroturystyka</title>\n  <link rel=\"stylesheet\" href=\"styl.css\">\n</head>\n<body>\n  <h1>Pod Lipą</h1>\n  …\n  <script src=\"kalkulator.js\"></script>\n</body>\n</html>\n```\n"
        "| element | po co | co sprawdzasz u agenta |\n"
        "|---|---|---|\n"
        "| `lang=\"pl\"` | czytniki ekranu czytają po polsku, wyszukiwarki znają język | jest w `<html>` |\n"
        "| `meta charset` | polskie znaki | utf-8 |\n"
        "| `meta viewport` | strona dopasowuje się do telefonu | dokładnie jak wyżej |\n"
        "| `<title>` | nazwa karty i wyniku w wyszukiwarce | konkretna, nie „Document” |\n"
        "| jeden `<h1>`, potem `<h2>` | struktura dokumentu | nagłówki w kolejności |\n"
        "| `<img alt=\"…\">` | opis obrazka dla niewidomych i gdy obrazek się nie wczyta | alt opisuje treść (nie „obrazek”) |\n"
        "| `<label for=\"noce\">` + `<input id=\"noce\">` | kliknięcie w etykietę i czytniki ekranu | for = id |\n"
        "## Formularz kalkulatora\n"
        "`<label for=\"noce\">Liczba nocy</label> <input id=\"noce\" name=\"noce\" type=\"number\" min=\"1\" value=\"2\">` — type=\"number\" daje klawiaturę numeryczną na telefonie, min blokuje 0 w przeglądarce (ale i tak sprawdzasz w kodzie!).\n"
        "## CSS — wygląd\n"
        "CSS w osobnym pliku styl.css: `body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 0 auto; padding: 1rem; }`. "
        "Media query zmienia wygląd na wąskim ekranie: `@media (max-width: 600px) { … }`. Zasada: zaczynasz od wersji na telefon (jedna kolumna), szerszy ekran tylko powiększa odstępy.\n"
        "## Dostępność — minimum, które sprawdzasz\n"
        "Wytyczne WCAG (W3C) są standardem dostępności; w UE od 28.06.2025 obowiązuje Europejski akt w sprawie dostępności dla wielu usług cyfrowych (w Polsce ustawa o zapewnianiu spełniania wymagań dostępności niektórych produktów i usług). "
        "Mała agroturystyka może nie podlegać obowiązkowi (mikroprzedsiębiorcy świadczący usługi są wyłączeni), ale minimum i tak robisz zawsze: alt, label, kontrast tekstu, działanie klawiaturą (Tab).\n"
        "## Jak sprawdzić stronę od agenta\n"
        "- Otwórz index.html w przeglądarce (podwójne kliknięcie).\n"
        "- F12 → narzędzia deweloperskie → ikona telefonu (tryb urządzenia) — jak wygląda na 375 px szerokości?\n"
        "- Przejdź formularz samym Tab i Enter.\n"
        "- Test w zadaniu sprawdza strukturę automatycznie."),
    przyklad=("<form id=\"kalkulator\">\n  <label for=\"noce\">Liczba nocy</label>\n  <input id=\"noce\" name=\"noce\" type=\"number\" min=\"1\" value=\"2\">\n"
              "  <label for=\"osoby\">Liczba osób</label>\n  <input id=\"osoby\" name=\"osoby\" type=\"number\" min=\"1\" value=\"2\">\n"
              "  <button type=\"submit\">Policz koszt</button>\n</form>\n<p id=\"wynik\" aria-live=\"polite\"></p>\n"
              "<img src=\"lipa.jpg\" alt=\"Drewniany dom pod rozłożystą lipą, przed nim ławka\">"),
    demonstracja={"tytul": "Strona od agenta — przegląd w 10 minut", "kroki": [
        "Prośba: „Utwórz index.html i styl.css dla agroturystyki Pod Lipą: nagłówek, 3 sekcje (O nas, Pokoje, Kontakt), formularz kalkulatora z polami noce i osoby (label + input), miejsce na wynik, zdjęcie z opisem alt. lang=pl, viewport, bez frameworków, bez zewnętrznych czcionek.”",
        "Otwierasz index.html: wygląda dobrze. F12 → tryb urządzenia 375 px: formularz wychodzi poza ekran — w CSS jest `width: 600px` na formularzu. Prośba: „formularz max-width: 100%”.",
        "Przegląd kodu: `<img src=\"lipa.jpg\" alt=\"image\">` — alt bezużyteczny. Poprawiasz opis.",
        "Tab po stronie: fokus przechodzi przez pola i przycisk — OK. Kliknięcie w napis „Liczba nocy” zaznacza pole — label działa.",
        "„✔ Sprawdź wynik” — testy struktury zielone. Commit."],
        "wynik": "Strona z poprawną strukturą, działająca na telefonie i z sensownym alt; dwa błędy agenta złapane przeglądem, nie przez klientkę."},
    jak_uruchomic=["Podwójne kliknięcie index.html w PRACA → przeglądarka; F12 → tryb urządzenia.", "Zadanie tygodnia → „✔ Sprawdź wynik” (testy struktury HTML)."],
    cwiczenia=[
        C("prowadzone",
          "Przejrzyj fragment od agenta: `<html>` (bez lang), `<title>Document</title>`, `<img src=\"dom.jpg\">`, `<input id=\"noce\">` bez etykiety, brak meta viewport. Ile problemów z tabeli lekcji tu jest? "
          "Jaką wartość wpiszesz w atrybut lang? Czas: 15 minut.",
          "5 problemów (lang, title, alt, label, viewport); lang=\"pl\".",
          ["Policz po elementach: html, title, img, input, head.", "„Document” to domyślny tytuł z szablonu.", "Język polski — dwuliterowy kod."],
          "Brak lang, tytuł „Document”, brak alt, pole bez label, brak viewport = 5. lang=\"pl\".",
          [li("ile", "Liczba problemów", 5), tx("lang", "Wartość lang", ["pl"])]),
        C("samodzielne",
          "Dopasuj: (1) strona za mała/za szeroka na telefonie, (2) czytnik ekranu nie wie, co jest na zdjęciu, (3) kliknięcie w napis „Liczba osób” nie zaznacza pola, (4) w wyszukiwarce wynik ma nazwę „Document”. "
          "Poprawki: meta viewport / alt / label for=id / title. Czas: 15 minut.",
          "(1) meta viewport; (2) alt; (3) label for=id; (4) title.",
          ["Telefon — viewport.", "Opis obrazka — atrybut alt.", "Powiązanie etykiety z polem — for i id."],
          "(1) viewport, (2) alt, (3) label for=id, (4) title.",
          [wy(f"d{i}", t, ["meta viewport", "alt", "label for=id", "title"], w) for i, t, w in
           ((1, "(1) Telefon", "meta viewport"), (2, "(2) Zdjęcie", "alt"), (3, "(3) Etykieta", "label for=id"), (4, "(4) Wyszukiwarka", "title"))]),
    ],
    typowe_bledy=[
        B("Polskie znaki wyświetlają się jako krzaczki („Ä…”).", "Brak meta charset utf-8 albo plik zapisany w innym kodowaniu.", "Pierwsze linie head; kodowanie w edytorze (VS Code: prawy dolny róg).", "`<meta charset=\"utf-8\">` jako pierwszy element head; zapisz plik w UTF-8."),
        B("CSS nie działa.", "Zła ścieżka w link href (wielkość liter, folder).", "F12 → Console/Network: 404 dla styl.css?", "href=\"styl.css\" i plik obok index.html (albo poprawna ścieżka do folderu)."),
        B("Na telefonie trzeba przewijać w bok.", "Stała szerokość w px albo brak viewport.", "F12 → tryb urządzenia.", "max-width zamiast width, meta viewport."),
    ],
    pulapki=["Agent chętnie dodaje frameworki CSS i czcionki z zewnętrznych serwerów — to wolniej, zależność od obcych serwerów i kwestie RODO (adres IP gościa trafia do dostawcy czcionek). W kursie: czcionki systemowe.",
             "Zdjęcia z internetu „bo agent znalazł” — prawa autorskie. Używaj własnych zdjęć klienta albo z licencją (tydzień 12)."],
    zadania=["Zbuduj index.html i styl.css z agentem (zadanie tygodnia).", "Sprawdź stronę w trybie urządzenia 375 px.", "Przejdź formularz samą klawiaturą."],
    pytania=[["Po co meta viewport?", "Żeby strona dopasowała szerokość do ekranu telefonu."], ["Jak powiązać etykietę z polem?", "label for=\"x\" i input id=\"x\"."],
             ["Co powinien zawierać alt?", "Opis treści obrazka ważnej dla odbiorcy, nie słowo „obrazek”."]],
    podsumowanie="Czytasz i zlecasz poprawną strukturę HTML, prosty CSS z myślą o telefonie i minimum dostępności — i sprawdzasz to w przeglądarce oraz testem.",
    test=[T("Atrybut języka strony:", ["<html lang=\"pl\">", "<body pl>", "<meta lang>", "<title pl>"], 0, "Na elemencie html."),
          T("Pole formularza bez etykiety — poprawka:", ["placeholder wystarczy", "label for=id", "większa czcionka", "kolor"], 1, "Placeholder znika przy pisaniu."),
          T("Strona za szeroka na telefonie — najpierw sprawdzasz:", ["meta viewport i stałe szerokości w px", "kolor tła", "favicon", "title"], 0, "Typowe przyczyny."),
          T("Plik z wyglądem strony to zwykle:", ["index.html", "styl.css", "kalkulator.js", "README.md"], 1, "CSS.")],
    w_praktyce=["Każda strona: lang, title, viewport, alt, label — lista przed oddaniem.", "Test na telefonie przed pokazaniem klientowi."],
    zrodla=[Z_MDN_HTML, Z_MDN_CSS, Z_MDN_FORM, Z_WCAG],
)

JS = L(
    id="javascript_interakcja", nazwa="JavaScript na stronie: formularz liczy koszt bez serwera", tydzien=9,
    slowa=["JavaScript", "zdarzenie", "addEventListener", "DOM", "querySelector", "konsola", "Number", "funkcja"],
    cel="Po tej lekcji czytasz prosty skrypt JS (funkcja, zdarzenie submit, odczyt pól, wypisanie wyniku), sprawdzasz go w konsoli przeglądarki i zlecasz agentowi kalkulator z obsługą złych danych.",
    po_co="Kalkulator ceny na stronie to typowe pierwsze „żywe” zlecenie. JavaScript działa w przeglądarce gościa — błędy widać od razu u klienta.",
    wymagania=["Lekcja „Strona internetowa: HTML i CSS”.", "Przeglądarka z narzędziami deweloperskimi (F12)."],
    wyjasnienie=(
        "## Ten sam pomysł co w Pythonie, inny zapis\n"
        "| Python | JavaScript |\n"
        "|---|---|\n"
        "| `def koszt(noce, osoby):` | `function obliczKoszt(noce, osoby) {` |\n"
        "| wcięcia | nawiasy klamrowe `{ }` i średniki |\n"
        "| `if noce >= 7:` | `if (noce >= 7) {` |\n"
        "| `raise ValueError` | `throw new Error(\"…\")` |\n"
        "| `int(\"3\")` | `Number(\"3\")` (albo `parseInt`) |\n"
        "| `print(x)` | `console.log(x)` (konsola F12) |\n"
        "## DOM — strona jako obiekty\n"
        "`document.querySelector(\"#noce\")` znajduje element o id=\"noce\". `.value` to wpisany tekst (ZAWSZE napis — jak input() w Pythonie!). `document.querySelector(\"#wynik\").textContent = \"…\"` wypisuje wynik na stronie.\n"
        "## Zdarzenia\n"
        "```\ndocument.querySelector(\"#kalkulator\").addEventListener(\"submit\", (e) => {\n  e.preventDefault();               // nie przeładowuj strony\n  const noce = Number(document.querySelector(\"#noce\").value);\n  const osoby = Number(document.querySelector(\"#osoby\").value);\n  try {\n    const koszt = obliczKoszt(noce, osoby);\n    document.querySelector(\"#wynik\").textContent = `Koszt: ${koszt.toFixed(2)} zł`;\n  } catch (err) {\n    document.querySelector(\"#wynik\").textContent = err.message;\n  }\n});\n```\n"
        "`e.preventDefault()` jest kluczowe: bez niego przeglądarka wyśle formularz i przeładuje stronę — wynik mignie i zniknie.\n"
        "## Dwie pułapki JS, które łapiesz u agenta\n"
        "- `\"3\" + 2` daje `\"32\"` (sklejenie), `\"3\" * 2` daje 6. Dlatego Number() na wartościach pól.\n"
        "- `Number(\"\")` daje 0, a `Number(\"abc\")` daje `NaN` (nie-liczba). Walidacja: `if (!Number.isInteger(noce) || noce < 1) throw new Error(\"Podaj liczbę nocy (co najmniej 1)\")`.\n"
        "## Logika osobno, strona osobno\n"
        "Funkcję `obliczKoszt` trzymaj bez odwołań do strony (dostaje liczby, zwraca liczbę albo rzuca błąd). Wtedy da się ją przetestować osobno (np. Node.js) — test zadania tak robi, jeśli masz Node.\n"
        "## Konsola przeglądarki\n"
        "F12 → Console: czerwone błędy (np. „Uncaught TypeError: Cannot read properties of null”) zwykle znaczą, że skrypt szuka elementu o id, którego nie ma, albo wczytał się przed formularzem (dlatego `<script>` na końcu body)."),
    przyklad=("function obliczKoszt(noce, osoby, cenaZaOsobeNoc = 120) {\n"
              "  if (!Number.isInteger(noce) || noce < 1) throw new Error(\"Podaj liczbę nocy (co najmniej 1)\");\n"
              "  if (!Number.isInteger(osoby) || osoby < 1) throw new Error(\"Podaj liczbę osób (co najmniej 1)\");\n"
              "  let koszt = noce * osoby * cenaZaOsobeNoc;\n  if (noce >= 7) koszt = koszt * 0.9;\n  return Math.round(koszt * 100) / 100;\n}"),
    demonstracja={"tytul": "Wynik, który miga i znika — i NaN zł", "kroki": [
        "Agent dodał kalkulator.js. Klikasz „Policz koszt” — wynik mignął, strona się przeładowała. Konsola czysta. Diagnoza: brak e.preventDefault() w obsłudze submit.",
        "Po poprawce: 2 noce, 2 osoby → „Koszt: 480.00 zł”. Czyścisz pole nocy → „Koszt: 0.00 zł”. Number(\"\") = 0, a walidacja w kodzie agenta to `if (noce < 0)`.",
        "Wpisujesz „abc” w polu (type=number to blokuje, ale gdy agent zmieni type na text) → „Koszt: NaN zł”.",
        "Prośba: „W obliczKoszt: noce i osoby muszą być liczbami całkowitymi ≥ 1, inaczej throw new Error z polskim komunikatem; obsługa submit wypisuje komunikat w #wynik”.",
        "Konsola F12: `obliczKoszt(7, 1)` → 756. `obliczKoszt(0, 1)` → Error z komunikatem. Działa."],
        "wynik": "Kalkulator nie przeładowuje strony, liczy poprawnie z rabatem i pokazuje polski komunikat dla pustych i błędnych pól."},
    jak_uruchomic=["Otwórz index.html → F12 → Console: wywołuj obliczKoszt(…) ręcznie.", "Zadanie tygodnia → „✔ Sprawdź wynik” (jeśli masz Node.js, test uruchomi też logikę JS)."],
    cwiczenia=[
        C("prowadzone",
          "Co zwróci JavaScript: (1) `\"3\" + 2`, (2) `\"3\" * 2`, (3) `Number(\"\")`? Wpisz wyniki tak, jak pokazałaby je konsola (napisy bez cudzysłowu). Czas: 15 minut.",
          "(1) 32 (napis \"32\"); (2) 6; (3) 0.",
          ["+ z napisem skleja.", "* zamienia na liczby.", "Pusty napis jako liczba to zero."],
          "\"3\" + 2 → \"32\" (sklejenie), \"3\" * 2 → 6, Number(\"\") → 0 — dlatego sama konwersja nie wystarcza, potrzebna walidacja.",
          [tx("j1", "(1) \"3\" + 2", ["32"], bledy=[bl("5", "z napisem operator + skleja, nie dodaje")]), li("j2", "(2) \"3\" * 2", 6), li("j3", "(3) Number(\"\")", 0)]),
        C("samodzielne",
          "Konsola pokazuje „Uncaught TypeError: Cannot read properties of null (reading 'value')” w linii `document.querySelector(\"#noc\").value`. W HTML pole ma id=\"noce\". (1) Co zwrócił querySelector? (2) Co poprawisz — selektor w JS czy id w HTML (wybierz to, co zgodne ze specyfikacją pól noce/osoby)? "
          "(3) Czego brakuje, gdy wynik miga i znika po kliknięciu? Czas: 15 minut.",
          "(1) null; (2) selektor w JS na \"#noce\"; (3) e.preventDefault().",
          ["„of null” — nie znalazł elementu.", "Specyfikacja mówi: pola noce i osoby.", "Formularz domyślnie przeładowuje stronę."],
          "querySelector zwrócił null (brak #noc) → popraw selektor na #noce; miganie = brak e.preventDefault().",
          [tx("null", "(1) Co zwrócił querySelector?", ["null"]), wy("co", "(2) Co poprawiasz?", ["selektor w JS", "id w HTML"], "selektor w JS"), tx("prev", "(3) Brakujące wywołanie", ["e.preventDefault()", "preventDefault()", "preventDefault"])]),
    ],
    typowe_bledy=[
        B("„Uncaught ReferenceError: obliczKoszt is not defined”.", "Plik JS nie wczytany (zła ścieżka) albo literówka w nazwie.", "F12 → Network: kalkulator.js 404?", "`<script src=\"kalkulator.js\"></script>` przed `</body>`, plik obok index.html."),
        B("Wynik „NaN zł”.", "Wartość pola nie jest liczbą (pusta, tekst).", "console.log(noce, typeof noce).", "Number() + walidacja Number.isInteger i ≥ 1 z komunikatem."),
        B("Wynik pojawia się na ułamek sekundy.", "Brak e.preventDefault() w submit.", "Obsługa zdarzenia.", "Pierwsza linia obsługi: e.preventDefault();"),
    ],
    pulapki=["Walidacja w przeglądarce (min=\"1\") to wygoda gościa, nie bezpieczeństwo — każdy może ją obejść. Serwer (tydzień 10) sprawdza dane ponownie.",
             "Nie wstawiaj tekstu od użytkownika przez innerHTML — używaj textContent (tydzień 12: XSS)."],
    zadania=["Dodaj kalkulator.js z obsługą złych danych (zadanie tygodnia).", "Przetestuj w konsoli 5 wywołań obliczKoszt.", "Commit + push."],
    pytania=[["Po co e.preventDefault() w submit?", "Żeby przeglądarka nie wysłała formularza i nie przeładowała strony."], ["Dlaczego Number() na wartościach pól?", "Bo .value zawsze jest napisem; + z napisem skleja."],
             ["Czym różni się textContent od innerHTML?", "textContent wstawia czysty tekst; innerHTML interpretuje HTML (ryzyko XSS)."]],
    podsumowanie="Czytasz skrypt z funkcją, zdarzeniem i DOM, rozpoznajesz pułapki napisów i NaN, debugujesz w konsoli i trzymasz logikę osobno od strony.",
    test=[T("`\"5\" + 1` w JavaScript:", ["6", "\"51\"", "Błąd", "NaN"], 1, "Sklejenie napisów."),
          T("Funkcja znajdująca element o id=\"wynik\":", ["document.querySelector(\"#wynik\")", "find(wynik)", "getId.wynik", "select(\".wynik\")"], 0, "# = id."),
          T("Bezpieczne wstawienie tekstu na stronę:", ["innerHTML", "textContent", "eval", "document.write"], 1, "Bez interpretacji HTML."),
          T("Gdzie zobaczysz błędy JavaScript?", ["W terminalu Mentora", "F12 → Console", "W Gicie", "W README"], 1, "Konsola przeglądarki.")],
    w_praktyce=["Logika w osobnej funkcji bez DOM — łatwa do testu.", "Przed oddaniem: konsola F12 bez czerwonych błędów."],
    zrodla=[Z_MDN_JS, ["MDN — Event.preventDefault()", "https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault", D],
            ["MDN — Node.textContent (różnica z innerHTML, bezpieczeństwo)", "https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent", D]],
)

PAGES = L(
    id="publikacja_pages", nazwa="Publikacja: GitHub Pages — strona pod własnym adresem", tydzien=9,
    slowa=["GitHub Pages", "publikacja", "hosting", "github.io", "publiczne repo", "deploy", "domena", "limity"],
    cel="Po tej lekcji publikujesz stronę z repozytorium na GitHub Pages (adres nazwa.github.io/repo), znasz limity i ograniczenia usługi oraz sprawdzasz, co jest publiczne.",
    po_co="Działający adres to najmocniejszy argument w portfolio i dla klienta. GitHub Pages jest darmowy, ale ma zasady, które trzeba znać przed publikacją.",
    wymagania=["Lekcje „GitHub” i „Strona internetowa…”.", "Repozytorium publiczne (w planie GitHub Free Pages działa tylko dla publicznych)."],
    wyjasnienie=(
        "## Co to jest GitHub Pages\n"
        "Usługa GitHuba, która publikuje statyczne pliki (HTML, CSS, JS, obrazy) z repozytorium pod adresem `https://NAZWA.github.io/REPO/`. Statyczne = bez Pythona na serwerze: kalkulator w JS zadziała, aplikacja Flask — nie (tydzień 10 pokaże inny hosting).\n"
        "## Limity i zasady (dokumentacja GitHub)\n"
        "| limit | wartość |\n"
        "|---|---|\n"
        "| repozytorium źródłowe | zalecane do 1 GB |\n"
        "| opublikowana strona | najwyżej 1 GB |\n"
        "| transfer | miękki limit 100 GB miesięcznie |\n"
        "| czas publikacji | do 10 minut na wdrożenie |\n"
        "| plan GitHub Free | Pages tylko z repozytoriów publicznych |\n"
        "GitHub Pages nie jest przeznaczony do sklepów internetowych ani usług SaaS, a dokumentacja zabrania używania go do przesyłania wrażliwych danych (haseł, numerów kart). Formularz rezerwacji zbierający dane gości — nie na Pages.\n"
        "## Osobne repozytorium na stronę\n"
        "Twoje główne repo pod-lipa jest prywatne (kod, notatki). Na stronę utwórz OSOBNE publiczne repozytorium, np. `pod-lipa-strona`, z samymi plikami strony: index.html, styl.css, kalkulator.js, obrazy. "
        "Zanim je opublikujesz — przegląd: żadnych notatek, kluczy, danych osobowych, plików .md z prywatnymi uwagami.\n"
        "## Włączenie\n"
        "- Repozytorium → Settings → Pages → Build and deployment → Source: „Deploy from a branch”, Branch: `main`, folder `/ (root)` → Save.\n"
        "- Po 1–10 minutach u góry pojawi się adres „Your site is live at https://NAZWA.github.io/pod-lipa-strona/”. Zakładka Actions pokazuje postęp wdrożenia.\n"
        "- Każdy kolejny push na main publikuje nową wersję.\n"
        "## Sprawdzenie po publikacji\n"
        "- Otwórz adres na komputerze i telefonie (inna sieć — np. dane komórkowe).\n"
        "- Ścieżki plików są wrażliwe na wielkość liter na serwerze: `Lipa.JPG` ≠ `lipa.jpg` (w Windows działało, na Pages — nie).\n"
        "- F12 → Console i Network: brak 404.\n"
        "## Własna domena\n"
        "Możesz podpiąć domenę klienta (np. podlipa.pl) w Settings → Pages → Custom domain + rekord DNS u rejestratora. Klient płaci za domenę u rejestratora; Ty ustawiasz. HTTPS: zaznacz „Enforce HTTPS”."),
    przyklad=("Struktura publicznego repozytorium strony:\n\npod-lipa-strona/\n├── index.html\n├── styl.css\n├── kalkulator.js\n├── img/\n│   └── lipa.jpg\n└── README.md   (1 akapit: co to za strona, dane fikcyjne)\n\n"
              "Adres po publikacji: https://anna-dev.github.io/pod-lipa-strona/"),
    demonstracja={"tytul": "Od plików do adresu w internecie", "kroki": [
        "github.com → New repository: pod-lipa-strona, Public, bez README.",
        "Nowy folder poza PRACA (np. Dokumenty\\pod-lipa-strona), skopiuj tylko index.html, styl.css, kalkulator.js, img/. `git init`, commit, `git remote add origin …`, `git push -u origin main`.",
        "Settings → Pages → Deploy from a branch → main / (root) → Save. Zakładka Actions: zadanie „pages build and deployment” — po chwili zielone.",
        "Adres działa. Na telefonie zdjęcie się nie wyświetla: w HTML `img/Lipa.jpg`, plik `img/lipa.jpg`. Poprawka nazwy, commit, push — po minucie działa.",
        "Zapisujesz adres w PRACA w adres_strony.txt (zadanie tygodnia)."],
        "wynik": "Publiczna strona pod adresem github.io, sprawdzona na telefonie, bez prywatnych plików w repozytorium."},
    jak_uruchomic=["Repo strony → Settings → Pages → Deploy from a branch → main → / (root).", "Postęp: zakładka Actions."],
    cwiczenia=[
        C("prowadzone",
          "Odpowiedz według dokumentacji: (1) maksymalny rozmiar opublikowanej strony (GB), (2) miękki limit transferu miesięcznie (GB), (3) ile minut najwyżej trwa wdrożenie, (4) czy na GitHub Free można publikować Pages z repozytorium prywatnego (tak/nie). Czas: 15 minut.",
          "(1) 1 GB; (2) 100 GB; (3) 10 minut; (4) nie.",
          ["Tabela limitów w lekcji.", "Transfer — 100.", "GitHub Free — tylko publiczne."],
          "1 GB strony, 100 GB transferu (miękko), wdrożenie do 10 min, Free — tylko repozytoria publiczne.",
          [li("gb", "(1) Rozmiar strony (GB)", 1), li("transfer", "(2) Transfer (GB/mies.)", 100), li("min", "(3) Wdrożenie (min)", 10), wy("priv", "(4) Pages z prywatnego repo na Free?", TN, "nie")]),
        C("samodzielne",
          "Które pliki mogą trafić do PUBLICZNEGO repozytorium strony? (1) index.html (2) notatki/o_mnie.md (3) styl.css (4) .env (5) img/lipa.jpg — zdjęcie od klientki z jej zgodą (6) dziennik.md. Podaj numery rosnąco jako ciąg cyfr. "
          "Czy formularz rezerwacji zbierający numery telefonów gości możesz oprzeć na samym GitHub Pages (tak/nie)? Czas: 15 minut.",
          "Mogą: 1, 3, 5 → „135”; nie — Pages nie służy do przesyłania wrażliwych danych.",
          ["Publiczne = cały internet.", "Notatki i dziennik są prywatne, .env to tajemnica.", "Pages to hosting statyczny, dokumentacja wyklucza przesyłanie wrażliwych danych."],
          "Tylko pliki strony: 1, 3, 5 (zdjęcie za zgodą). Formularz z danymi gości — nie na Pages.",
          [tx("pliki", "Numery plików", ["135"], bledy=[bl("1345", ".env to tajemnica — nigdy w publicznym repozytorium")]), wy("form", "Formularz z telefonami na samym Pages?", TN, "nie")]),
    ],
    typowe_bledy=[
        B("404 „There isn't a GitHub Pages site here”.", "Pages nie włączone, wdrożenie trwa albo brak index.html w korzeniu.", "Settings → Pages i zakładka Actions.", "Włącz źródło main / (root), poczekaj do 10 min, index.html w korzeniu repozytorium."),
        B("Obrazek działa lokalnie, na Pages nie.", "Wielkość liter w nazwie pliku.", "F12 → Network: 404 dla obrazka.", "Ujednolić nazwy na małe litery w plikach i HTML."),
        B("Opcja Pages niedostępna dla repozytorium.", "Repozytorium prywatne na GitHub Free.", "Settings → General → visibility.", "Osobne publiczne repo tylko z plikami strony."),
    ],
    pulapki=["Upublicznienie istniejącego repozytorium upublicznia CAŁĄ historię — dlatego osobne repo strony.", "Pages nie jest miejscem na dane osobowe gości ani płatności."],
    zadania=["Opublikuj stronę na Pages i zapisz adres (zadanie tygodnia).", "Sprawdź stronę na telefonie w innej sieci.", "Napisz 1-akapitowy README repozytorium strony."],
    pytania=[["Dlaczego osobne repozytorium na stronę?", "Bo Pages na Free wymaga publicznego repo, a główny projekt z notatkami i historią ma zostać prywatny."],
             ["Czego nie publikujesz na Pages?", "Formularzy zbierających wrażliwe dane, sklepów, haseł, kart, danych osobowych."], ["Gdzie widać postęp wdrożenia?", "Zakładka Actions repozytorium."]],
    podsumowanie="Publikujesz statyczną stronę na GitHub Pages z osobnego publicznego repozytorium, znasz limity i zakazy usługi i sprawdzasz efekt na telefonie.",
    test=[T("GitHub Pages publikuje:", ["Aplikacje Flask", "Pliki statyczne: HTML, CSS, JS", "Bazy danych", "Pliki .exe"], 1, "Bez Pythona po stronie serwera."),
          T("Adres strony Pages ma postać:", ["NAZWA.github.io/REPO", "github.com/pages", "REPO.pl", "localhost"], 0, "Albo własna domena."),
          T("Limit opublikowanej strony:", ["100 MB", "1 GB", "10 GB", "bez limitu"], 1, "Dokumentacja GitHub."),
          T("Plik działa lokalnie, na Pages 404. Pierwsze podejrzenie:", ["Wielkość liter w nazwie", "Zły kolor", "Za długi tytuł", "Brak README"], 0, "Serwer rozróżnia litery.")],
    w_praktyce=["Strona klienta: osobne repo, przegląd treści przed publikacją.", "Po każdym push — szybki test na telefonie."],
    zrodla=[Z_GH_PAGES, Z_GH_PAGES_LIM, ["GitHub Docs — Configuring a publishing source for your GitHub Pages site", "https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site", D]],
)
