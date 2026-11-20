# -*- coding: utf-8 -*-
"""Etap 0, tygodnie 2–3: czytanie kodu 2, traceback, rozmowa z AI, specyfikacja, pierwszy program z AI, powtórka."""

from wspolne import (TN, B, C, L, T, bl, kod, kw, li, tx, wy)
from etap0 import D, Z_ANTH_PROMPT, Z_CC_BEST, Z_PY_ERR, Z_PY_TUT

Z_PY_FUN = ["Python tutorial — 4.8 Defining Functions (def, return)", "https://docs.python.org/3/tutorial/controlflow.html#defining-functions", D]
Z_PY_DS = ["Python tutorial — 5. Data Structures (listy, słowniki)", "https://docs.python.org/3/tutorial/datastructures.html", D]
Z_PY_EXC = ["Python — Built-in Exceptions (lista wyjątków i ich znaczenie)", "https://docs.python.org/3/library/exceptions.html", D]
Z_OAI_PROMPT = ["OpenAI — Prompt engineering guide (dokumentacja platformy)", "https://platform.openai.com/docs/guides/prompt-engineering", D]
Z_ANTH_CLEAR = ["Anthropic — Be clear, direct, and detailed (dokumentacja Claude)", "https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct", D]
Z_ANTH_EX = ["Anthropic — Use examples (multishot prompting) (dokumentacja Claude)", "https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting", D]


# =========================================================================== TYDZIEŃ 2
CZYTANIE_2 = L(
    id="czytanie_kodu_2", nazwa="Czytanie kodu 2: listy, pętle, słowniki i funkcje", tydzien=2,
    slowa=["lista", "pętla", "for", "słownik", "dict", "funkcja", "def", "return", "raise"],
    cel="Po tej lekcji czytasz funkcję z parametrami i return, pętlę for po liście, słownik i rzucanie wyjątku — i umiesz powiedzieć, co funkcja zwróci dla podanych danych.",
    po_co="Prawie każdy kod od AI to funkcje działające na listach i słownikach. Testy w tym kursie wywołują Twoje funkcje — musisz rozumieć, co znaczy „funkcja zwraca”.",
    wymagania=["Lekcja „Czytanie kodu 1”.", "Plik do eksperymentów w PRACA (np. proby.py)."],
    wyjasnienie=(
        "## Lista — wiele wartości pod jedną nazwą\n"
        "`goscie = [\"Anna\", \"Piotr\", \"Ewa\"]` — lista w nawiasach kwadratowych. Numeracja od ZERA: `goscie[0]` to \"Anna\", `goscie[-1]` to ostatni element. "
        "`len(goscie)` → 3, `goscie.append(\"Jan\")` dopisuje na końcu, `\"Ewa\" in goscie` → True.\n"
        "## Pętla for — zrób coś dla każdego elementu\n"
        "`for g in goscie:` + wcięty blok wykonuje się raz dla każdego elementu; w kolejnych obrotach `g` to kolejne imiona. "
        "`for i in range(3):` daje i = 0, 1, 2 (bez 3!). Typowy wzór „zbierz sumę”: przed pętlą `suma = 0`, w pętli `suma = suma + x` (krócej `suma += x`).\n"
        "## Słownik — wartości pod nazwami (kluczami)\n"
        "`rezerwacja = {\"gosc\": \"Anna\", \"noce\": 3, \"pokoj\": \"Lipowy\"}` — klucz: wartość. `rezerwacja[\"noce\"]` → 3. Brak klucza → błąd KeyError; bezpiecznie: `rezerwacja.get(\"rabat\", 0)` (0, gdy brak). "
        "Dane z plików CSV i JSON, odpowiedzi z internetu (API) — to prawie zawsze listy słowników.\n"
        "## Funkcja — nazwany kawałek pracy\n"
        "```\ndef koszt_pobytu(noce, osoby, cena=120):\n    return noce * osoby * cena\n```\n"
        "- `def` definiuje funkcję; `noce, osoby` to parametry, `cena=120` — parametr z wartością domyślną.\n"
        "- `return` ODDAJE wynik temu, kto wywołał funkcję, i kończy funkcję. `print` tylko wypisuje na ekran — testy sprawdzają to, co funkcja ZWRACA. "
        "Funkcja bez return zwraca `None` — to najczęstsza przyczyna, gdy test mówi „oczekiwano 480.0, otrzymano None”.\n"
        "- Wywołanie: `koszt_pobytu(2, 2)` → 480; z inną ceną: `koszt_pobytu(2, 2, cena=150)` → 600.\n"
        "## raise — funkcja odmawia złych danych\n"
        "`if noce < 1: raise ValueError(\"noce muszą być ≥ 1\")` przerywa funkcję z błędem. To dobrze: lepiej głośny błąd niż cicha zła cena. "
        "Test może sprawdzić, że dla złych danych funkcja rzuca ValueError.\n"
        "## if __name__ == \"__main__\":\n"
        "Agent często dopisuje na końcu pliku ten blok. Kod w nim wykonuje się tylko, gdy uruchamiasz plik bezpośrednio (▶ Uruchom), a NIE wtedy, gdy test importuje funkcję. "
        "Dzięki temu input() w tym bloku nie blokuje testów.\n"
        "## Jak czytać funkcję od AI w 4 pytaniach\n"
        "| pytanie | gdzie patrzysz |\n"
        "|---|---|\n"
        "| co przyjmuje? | parametry w linii def |\n"
        "| co zwraca? | każda linia return (może być kilka!) |\n"
        "| kiedy odmawia? | raise i warunki przed nim |\n"
        "| co zmienia poza sobą? | zapisy do plików, print, zmiany list przekazanych z zewnątrz |"),
    przyklad=kod("czytanie_kodu_2:przyklad",
                 "def koszt_pobytu(noce, osoby, cena=120):\n    if noce < 1 or osoby < 1:\n        raise ValueError(\"noce i osoby muszą być co najmniej 1\")\n"
                 "    koszt = noce * osoby * cena\n    if noce >= 7:\n        koszt = koszt * 0.9\n    return round(koszt, 2)\n\n\n"
                 "rezerwacje = [{\"gosc\": \"Anna\", \"noce\": 2, \"osoby\": 2}, {\"gosc\": \"Piotr\", \"noce\": 7, \"osoby\": 1}]\n"
                 "suma = 0\nfor r in rezerwacje:\n    k = koszt_pobytu(r[\"noce\"], r[\"osoby\"])\n    print(r[\"gosc\"], k)\n    suma += k\nprint(\"Razem:\", suma)\n",
                 "Anna 480\nPiotr 756.0\nRazem: 1236.0\n"),
    demonstracja={"tytul": "Śledzenie pętli po liście słowników", "kroki": [
        "Najpierw definicja funkcji — Python ją tylko zapamiętuje, nic nie liczy.",
        "rezerwacje to lista dwóch słowników. suma = 0.",
        "Obrót 1: r = słownik Anny. koszt_pobytu(2, 2): warunek raise nie zachodzi, koszt = 2*2*120 = 480, 2 >= 7 to False, return round(480, 2) → 480 (int, bo nic nie mnożyło przez 0.9). Wypisuje „Anna 480”, suma = 480.",
        "Obrót 2: Piotr: 7*1*120 = 840, 7 >= 7 → koszt = 756.0 (float). Wypisuje „Piotr 756.0”, suma = 1236.0.",
        "Po pętli: „Razem: 1236.0”. Zauważ: raz 480, raz 756.0 — typ wyniku zależy od ścieżki. Testy porównują liczby (480 == 480.0 to True), więc to nie błąd, ale na fakturze formatujesz {k:.2f}.",
        "Spróbuj: dopisz rezerwację z noce = 0 — program kończy się ValueError z Twoim komunikatem. Tak ma być."],
        "wynik": "Anna 480 / Piotr 756.0 / Razem: 1236.0; dla noce = 0 — ValueError z czytelnym komunikatem."},
    jak_uruchomic=["Wklej przykład do proby.py w PRACA i uruchom (zadanie z paskiem albo `python proby.py`)."],
    cwiczenia=[
        C("prowadzone",
          "Co zwróci funkcja i co wypisze program?\n\n" + kod("czytanie_kodu_2:c1",
                                                             "def policz_dorosłych(goscie):\n    n = 0\n    for g in goscie:\n        if g[\"wiek\"] >= 18:\n            n += 1\n    return n\n\n"
                                                             "lista = [{\"imie\": \"Ola\", \"wiek\": 34}, {\"imie\": \"Kuba\", \"wiek\": 12}, {\"imie\": \"Ewa\", \"wiek\": 18}]\n"
                                                             "print(policz_dorosłych(lista))\nprint(lista[1][\"imie\"])\nprint(len(lista))\n",
                                                             "2\nKuba\n3\n") +
          "\nWpisz trzy linie wyniku. Czas: 20 minut.",
          "2 / Kuba / 3",
          ["Przejdź pętlą: Ola 34 (≥18), Kuba 12, Ewa 18 — czy 18 >= 18?", "lista[1] to DRUGI element (numeracja od 0).", "len liczy elementy listy."],
          "Dorośli: Ola i Ewa (18 >= 18 to True) → 2. lista[1] → Kuba. len(lista) → 3.",
          [li("l1", "Linia 1 (dorośli)", 2, bledy=[bl(1, "Ewa ma dokładnie 18 lat, a warunek to >= 18 — granica wchodzi")]),
           tx("l2", "Linia 2", ["Kuba"], bledy=[bl("Ola", "numeracja list zaczyna się od 0 — lista[1] to drugi element")]), li("l3", "Linia 3", 3)]),
        C("samodzielne",
          "AI napisało funkcję, a test mówi: „assert None == 480”. Znajdź błąd:\n\n" + kod("czytanie_kodu_2:c2",
                                                                                        "def koszt(noce, osoby):\n    wynik = noce * osoby * 120\n    print(wynik)\n",
                                                                                        None) +
          "\nCo zwraca ta funkcja? Jakie słowo trzeba wstawić zamiast print, żeby test przeszedł? Czas: 15 minut.",
          "Funkcja zwraca None (nie ma return; print tylko wypisuje). Zamiast `print(wynik)` → `return wynik`.",
          ["Szukaj w funkcji słowa return.", "Funkcja bez return zwraca specjalną wartość None.", "Test porównuje wartość zwróconą, a nie tekst na ekranie."],
          "Brak return → funkcja zwraca None; print tylko wyświetla 480. Poprawka: `return wynik`.",
          [tx("zwraca", "Co zwraca funkcja?", ["None"], bledy=[bl("480", "480 pojawia się na ekranie (print), ale funkcja niczego nie ZWRACA")]),
           tx("slowo", "Słowo zamiast print", ["return"])]),
    ],
    typowe_bledy=[
        B("„IndexError: list index out of range”.", "Sięgasz po element o numerze, którego nie ma (np. lista[3] w liście 3-elementowej).", "len(lista) i numer, którego używasz.", "Pamiętaj: ostatni element to lista[len(lista) - 1] albo lista[-1]."),
        B("„KeyError: 'nocy'”.", "Klucz w słowniku nazywa się inaczej (literówka, wielkość liter).", "print(slownik.keys()) — jakie są klucze?", "Popraw nazwę klucza albo użyj .get(\"klucz\", domyślna)."),
        B("Test: „assert None == …”.", "Funkcja nie ma return (albo return jest w złym miejscu, np. w pętli).", "Czy każda ścieżka funkcji kończy się return?", "Dodaj return z wynikiem; nie zastępuj return przez print."),
    ],
    pulapki=["return w środku pętli kończy funkcję po pierwszym obrocie — częsty błąd AI przy „zsumuj wszystkie”.",
             "Lista przekazana do funkcji to ta sama lista — jeśli funkcja ją zmienia (append, sort), zmienia się też na zewnątrz."],
    zadania=["Napisz w proby.py listę 4 cen i pętlę liczącą sumę i średnią.", "Zmień przykład tak, żeby funkcja dawała 5% rabatu dla 4+ osób i przewidź wyniki.", "Zapytaj czat AI: „wyjaśnij różnicę między print a return na przykładzie” i oceń odpowiedź."],
    pytania=[["Czym różni się return od print?", "return oddaje wartość wywołującemu (np. testowi), print tylko wypisuje tekst na ekran."],
             ["Jaki numer ma pierwszy element listy?", "0."],
             ["Po co funkcji raise ValueError?", "Żeby głośno odmówić błędnych danych zamiast policzyć złą wartość."]],
    podsumowanie="Czytasz listy, pętle, słowniki i funkcje; rozróżniasz return i print; rozumiesz raise i blok __main__.",
    test=[T("Co zwraca funkcja bez return?", ["0", "None", "Pusty napis", "Błąd"], 1, "Domyślnie None."),
          T("`for i in range(3)` daje kolejno:", ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"], 1, "range(3) — od 0, bez 3."),
          T("`d = {\"noce\": 3}`; `d.get(\"osoby\", 1)` zwraca:", ["KeyError", "None", "1", "3"], 2, ".get z wartością domyślną."),
          T("Kod pod `if __name__ == \"__main__\":` wykonuje się:", ["Zawsze", "Gdy plik uruchamiasz bezpośrednio, nie przy imporcie przez test", "Tylko w testach", "Nigdy"], 1,
            "Dlatego input() umieszczamy właśnie tam.")],
    w_praktyce=["Przy każdej funkcji od AI: co przyjmuje, co zwraca, kiedy odmawia.", "Szukaj return w pętlach."],
    zrodla=[Z_PY_FUN, Z_PY_DS, Z_PY_TUT],
)

TRACEBACK = L(
    id="bledy_traceback", nazwa="Komunikat błędu (traceback) — czytanie od dołu", tydzien=2,
    slowa=["traceback", "błąd", "wyjątek", "NameError", "TypeError", "ValueError", "linia", "debug"],
    cel="Po tej lekcji czytasz traceback od dołu: nazwa wyjątku, komunikat, plik i linia — i umiesz przekazać AI błąd tak, żeby poprawiło przyczynę, a nie objaw.",
    po_co="Błędy to codzienność — także w kodzie od AI. Kto czyta traceback, naprawia w minutę; kto wkleja „nie działa”, kręci się w kółko godzinę.",
    wymagania=["Lekcja „Czytanie kodu 2”.", "Plik napraw_mnie.py z materiałów kursu (przyklady/napraw_mnie.py) — do zadania tygodnia."],
    wyjasnienie=(
        "## Anatomia tracebacku\n"
        "Gdy Python trafia na błąd, którego nikt nie obsłużył, wypisuje „Traceback (most recent call last):” i ścieżkę wywołań. Czytaj OD DOŁU:\n"
        "```\nTraceback (most recent call last):\n  File \"C:\\...\\PRACA\\raport.py\", line 9, in <module>\n    print(srednia(ceny))\n"
        "  File \"C:\\...\\PRACA\\raport.py\", line 4, in srednia\n    return suma / len(lista)\nZeroDivisionError: division by zero\n```\n"
        "- Ostatnia linia: typ wyjątku (ZeroDivisionError) i komunikat (division by zero) — CO się stało.\n"
        "- Linia nad nią: plik, numer linii i funkcja (line 4, in srednia) — GDZIE się stało.\n"
        "- Wyższe linie: KTO wywołał (line 9 wywołał srednia). Przyczyna bywa wyżej niż miejsce wybuchu: tu lista była pusta.\n"
        "## Najczęstsze wyjątki\n"
        "| wyjątek | co znaczy | typowa przyczyna w kodzie od AI |\n"
        "|---|---|---|\n"
        "| SyntaxError | kod jest niepoprawnie zapisany | ucięta odpowiedź, wklejony fragment bez nawiasu |\n"
        "| IndentationError | złe wcięcie | mieszane spacje/tabulatory po wklejeniu |\n"
        "| NameError: name 'x' is not defined | nazwa nie istnieje | literówka, brak importu, zmienna z innej funkcji |\n"
        "| TypeError | zła operacja dla typu | napis + liczba, wywołanie z złą liczbą argumentów |\n"
        "| ValueError | dobry typ, zła wartość | int(\"abc\"), Twoje raise dla złych danych |\n"
        "| KeyError / IndexError | brak klucza / indeksu | inne nazwy kolumn w CSV niż założyło AI |\n"
        "| FileNotFoundError | brak pliku | zła ścieżka, uruchomienie z innego folderu |\n"
        "| ModuleNotFoundError | brak biblioteki | nieinstalowana paczka (sprawdź, czy istnieje! — lekcja o halucynacjach) |\n"
        "| AssertionError | test nie przeszedł | wynik różny od oczekiwanego |\n"
        "## Metoda 4 kroków\n"
        "- Przeczytaj ostatnią linię i przetłumacz ją na zdanie („dzielę przez zero”).\n"
        "- Otwórz plik w linii z przedostatniego wpisu. Co tam jest? Jakie wartości mają zmienne? (wstaw tymczasowo `print(lista)` przed linią).\n"
        "- Postaw hipotezę przyczyny („lista jest pusta, bo plik CSV nie miał wierszy”).\n"
        "- Popraw przyczynę i uruchom ponownie. Jedna zmiana naraz.\n"
        "## Jak zgłaszać błąd AI (szablon)\n"
        "„Uruchamiam `python raport.py` w Windows. Oczekuję: średnia cen. Dostaję traceback (cały poniżej). Moja hipoteza: lista ceny jest pusta, gdy plik nie ma danych. "
        "Popraw tak, żeby dla pustej listy funkcja zwracała 0 i nie zmieniaj niczego innego.” + pełny traceback.\n"
        "Pełny traceback, polecenie, którego użyłeś, i oczekiwany wynik — to trzy rzeczy, bez których AI zgaduje.\n"
        "## Mentor pomaga\n"
        "Okno wyniku „▶ Uruchom” tłumaczy najczęstsze wyjątki po polsku i pokazuje linię. Zakładka Asystent ma tryb „wyjaśnij błąd”."),
    przyklad=("Ten sam błąd zgłoszony źle i dobrze:\n\n"
              "Źle: „nie działa, popraw”.\n\n"
              "Dobrze: „Polecenie: python lista_gosci.py. Oczekiwane: 3 gości. Wynik: KeyError: 'imie' w linii 12 (funkcja raport). "
              "W słownikach klucz nazywa się 'imię' (z ogonkiem) — ujednolić na 'imie' w całym pliku, nic więcej nie zmieniaj.”"),
    demonstracja={"tytul": "Naprawa błędu z przyczyną wyżej niż wybuch", "kroki": [
        "Program raport.py liczy średnią cenę z listy. Uruchamiasz i dostajesz traceback z ZeroDivisionError w line 4, in srednia.",
        "Ostatnia linia: dzielenie przez zero. Line 4: return suma / len(lista) — dzielimy przez len(lista), więc len(lista) = 0: lista jest pusta.",
        "Wyżej: line 9 wywołuje srednia(ceny). Wstawiasz przed nią print(ceny) → []. Hipoteza: filtr „ceny powyżej 1000” niczego nie znalazł.",
        "Decyzja: co ma się dziać dla pustej listy? Specyfikacja mówi: zwróć 0. Dopisujesz w srednia: if not lista: return 0.",
        "Uruchamiasz ponownie — działa. Usuwasz tymczasowy print. W dzienniku: „ZeroDivisionError — pusta lista; dodałem przypadek brzegowy”."],
        "wynik": "Błąd naprawiony u przyczyny (pusta lista), a nie przez „łatanie” miejsca wybuchu; masz zapis przypadku brzegowego do testów (tydzień 8)."},
    jak_uruchomic=["Zadanie tygodnia „Napraw mnie” → „📄 Otwórz przykład” → przepisz do napraw_mnie.py → „▶ Uruchom” i czytaj traceback od dołu."],
    cwiczenia=[
        C("prowadzone",
          "Przeczytaj traceback:\n\n"
          "Traceback (most recent call last):\n  File \"C:\\PRACA\\lista_gosci.py\", line 15, in <module>\n    raport(goscie)\n"
          "  File \"C:\\PRACA\\lista_gosci.py\", line 8, in raport\n    print(\"Gość: \" + g[\"imie\"] + \", noce: \" + g[\"noce\"])\n"
          "TypeError: can only concatenate str (not \"int\") to str\n\n"
          "Podaj: typ wyjątku, numer linii, w której wybuchło, nazwę funkcji i który klucz słownika jest liczbą. Czas: 15 minut.",
          "TypeError; linia 8; funkcja raport; klucz noce (liczba) — sklejanie napisu z int.",
          ["Ostatnia linia: nazwa przed dwukropkiem.", "Przedostatni wpis File…: line i in …", "Który z dwóch kluczy w tej linii może być liczbą nocy?"],
          "TypeError w line 8, in raport: napis + g[\"noce\"] (int). Poprawka: f-string f\"Gość: {g['imie']}, noce: {g['noce']}\".",
          [tx("typ", "Typ wyjątku", ["TypeError"]), li("linia", "Linia wybuchu", 8, bledy=[bl(15, "line 15 to miejsce WYWOŁANIA; wybuch jest niżej w tracebacku — line 8")]),
           tx("fun", "Funkcja", ["raport"]), tx("klucz", "Klucz z liczbą", ["noce"])]),
        C("samodzielne",
          "Dopasuj wyjątek do sytuacji: (1) `int(\"dwa\")`, (2) `open(\"dane\\\\brak.csv\")` gdy pliku nie ma, (3) `import pandass` (literówka), (4) `print(cena_kocowa)` przy zmiennej cena_koncowa. Czas: 15 minut.",
          "(1) ValueError, (2) FileNotFoundError, (3) ModuleNotFoundError, (4) NameError.",
          ["int() dostał napis, ale nie liczbę — dobry typ, zła wartość.", "Brak pliku ma własny wyjątek z „File” w nazwie.", "Nieznana nazwa zmiennej → „is not defined”."],
          "(1) ValueError: invalid literal for int(); (2) FileNotFoundError; (3) ModuleNotFoundError: No module named 'pandass'; (4) NameError: name 'cena_kocowa' is not defined.",
          [wy("w1", "(1) int(\"dwa\")", ["ValueError", "TypeError", "NameError", "FileNotFoundError", "ModuleNotFoundError"], "ValueError",
              bledy=[bl("TypeError", "typ (napis) jest akceptowany przez int(), zła jest WARTOŚĆ „dwa” — to ValueError")]),
           wy("w2", "(2) open brakującego pliku", ["ValueError", "TypeError", "NameError", "FileNotFoundError", "ModuleNotFoundError"], "FileNotFoundError"),
           wy("w3", "(3) import pandass", ["ValueError", "TypeError", "NameError", "FileNotFoundError", "ModuleNotFoundError"], "ModuleNotFoundError"),
           wy("w4", "(4) literówka w nazwie zmiennej", ["ValueError", "TypeError", "NameError", "FileNotFoundError", "ModuleNotFoundError"], "NameError")]),
    ],
    typowe_bledy=[
        B("AI „poprawia” błąd, a pojawia się nowy, potem stary wraca.", "Zgłoszenie bez tracebacku i bez hipotezy — model zgaduje i łata objawy.", "Czy podałeś pełny traceback, polecenie i oczekiwany wynik?", "Szablon zgłoszenia z lekcji; po 2 nieudanych poprawkach — nowa rozmowa z podsumowaniem."),
        B("Poprawiłeś linię z tracebacku, ale wynik nadal jest zły.", "Przyczyna leży wyżej (złe dane wejściowe).", "print zmiennych przed linią błędu.", "Szukaj, skąd wzięła się zła wartość — idź w górę tracebacku."),
        B("„ModuleNotFoundError: No module named 'requests'” w terminalu, a w Mentorze działa.", "Terminal używa innego Pythona niż środowisko kursu.", "`where python` w CMD.", "Otwieraj terminal przyciskiem Mentora (Python kursu jest pierwszy w PATH)."),
    ],
    pulapki=["Nie owijaj wszystkiego w `try: … except: pass` — AI czasem tak „naprawia” błędy. Błąd znika z ekranu, a program liczy źle po cichu.",
             "Traceback może zawierać ścieżki z Twoim imieniem (C:\\Users\\Imie) — przy wklejaniu do publicznych miejsc (forum, GitHub) zamaskuj je."],
    zadania=["Celowo wywołaj 3 różne wyjątki z tabeli w proby.py i przeczytaj każdy traceback od dołu.", "Zgłoś jeden błąd czatowi AI według szablonu i porównaj z „nie działa, popraw”.", "Zapisz w dzienniku swoją listę 3 najczęstszych błędów."],
    pytania=[["Dlaczego traceback czytamy od dołu?", "Na dole jest typ i opis błędu oraz miejsce wybuchu; wyżej — kto to wywołał."],
             ["Co musi zawierać dobre zgłoszenie błędu do AI?", "Polecenie, oczekiwany wynik, pełny traceback, hipotezę i granice zmiany."],
             ["Dlaczego except: pass jest groźne?", "Ukrywa błąd — program działa dalej z błędnymi danymi i nikt o tym nie wie."]],
    podsumowanie="Czytasz traceback od dołu, rozpoznajesz najczęstsze wyjątki, szukasz przyczyny wyżej niż wybuch i zgłaszasz błąd AI według szablonu.",
    test=[T("Ostatnia linia tracebacku zawiera:", ["Pierwszą linię programu", "Typ wyjątku i komunikat", "Nazwę autora", "Wersję Pythona"], 1, "Tam jest „co się stało”."),
          T("`NameError: name 'sume' is not defined` najczęściej oznacza:", ["Brak internetu", "Literówkę lub niezdefiniowaną zmienną", "Błąd dysku", "Zły system"], 1, "Nazwa nie istnieje."),
          T("Co NIE jest dobrym sposobem naprawy błędu od AI?", ["Pełny traceback i hipoteza", "Owinięcie kodu w try/except: pass", "Jedna zmiana naraz", "Sprawdzenie danych wejściowych"], 1, "Ukrywa błąd."),
          T("ZeroDivisionError w funkcji średniej zwykle oznacza:", ["Zbyt duże liczby", "Pustą listę", "Złe wcięcie", "Brak modułu"], 1, "len(lista) == 0.")],
    w_praktyce=["Zawsze wklejaj pełny traceback, nie streszczenie.", "Po naprawie zapisz przypadek, który wywołał błąd — to przyszły test."],
    zrodla=[Z_PY_ERR, Z_PY_EXC, Z_CC_BEST],
)

ROZMOWA = L(
    id="rozmowa_z_ai", nazwa="Rozmowa z AI: kontekst, przykłady, ograniczenia, format", tydzien=2,
    slowa=["prompt", "kontekst", "przykłady", "ograniczenia", "format", "iteracja", "rola"],
    cel="Po tej lekcji piszesz prośbę do AI z pięciu części (cel, kontekst, przykłady, ograniczenia, format odpowiedzi) i prowadzisz rozmowę iteracyjnie zamiast jednym wielkim promptem.",
    po_co="Jakość kodu od AI zależy najbardziej od jakości prośby — to Twoja główna „klawiatura” jako vibe codera.",
    wymagania=["Darmowy czat AI (claude.ai lub chatgpt.com).", "Lekcja „Komunikat błędu”."],
    wyjasnienie=(
        "## Model wie tylko to, co mu powiesz\n"
        "Dokumentacja Anthropic radzi traktować model jak bardzo zdolnego nowego pracownika bez kontekstu firmy: im dokładniej wyjaśnisz, czego chcesz i po co, tym lepszy wynik. "
        "Wytyczne OpenAI mówią to samo: jasne instrukcje, przykłady, podział złożonych zadań na kroki.\n"
        "## Pięć części dobrej prośby\n"
        "| część | pytanie | przykład |\n"
        "|---|---|---|\n"
        "| cel | co ma powstać? | funkcja lista_gosci.py: dodawanie gości i raport |\n"
        "| kontekst | dla kogo, w czym, co już jest? | Python 3.12, Windows, początkujący; plik ma być prosty, bez bibliotek |\n"
        "| przykłady | jakie wejście → jaki wynik? | dodaj_goscia(lista, \"Anna\", 2) → lista ma 1 element |\n"
        "| ograniczenia | czego nie robić? | bez input() w funkcjach, bez zmiany nazw funkcji, polskie komunikaty |\n"
        "| format | jak ma wyglądać odpowiedź? | cały plik w jednym bloku kodu + 3 zdania, jak go sprawdzić |\n"
        "## Przykłady są najważniejsze\n"
        "Dokumentacja Anthropic nazywa to „multishot prompting”: kilka przykładów wejście → wynik mówi modelowi więcej niż akapit opisu. "
        "Dla Ciebie mają drugi plus — przykłady to gotowe testy: po odpowiedzi sprawdzasz, czy program daje dokładnie te wyniki.\n"
        "## Iteracja zamiast „promptu idealnego”\n"
        "- Najpierw poproś o plan albo pytania: „Zanim napiszesz kod, zadaj mi do 5 pytań o niejasności”.\n"
        "- Potem mały kawałek (jedna funkcja), uruchomienie, poprawka.\n"
        "- Każda poprawka konkretna: „dla (7, 1) wychodzi 840, a ma być 756 — rabat nie działa na granicy 7 nocy”.\n"
        "- Gdy rozmowa się „rozjeżdża” (model miesza wersje), zaczynasz nową z krótkim podsumowaniem ustaleń.\n"
        "## Rola i poziom\n"
        "„Jesteś cierpliwym mentorem Pythona; wyjaśniaj prosto, bo jestem początkujący” zmienia styl wyjaśnień. Rola nie zastąpi jednak konkretów z tabeli.\n"
        "## Poproś o sprawdzalność\n"
        "Dodawaj do każdej prośby: „podaj, jak mam sprawdzić, że działa (polecenie i oczekiwany wynik)” oraz „wypisz założenia, które przyjąłeś”. "
        "Założenia to miejsca, w których model zgadywał — tam szukasz błędów.\n"
        "## Czego nie wklejać\n"
        "Haseł, kluczy API, danych osobowych prawdziwych klientów, poufnych dokumentów firmy. Dane w kursie są fikcyjne — w pracy zastępujesz prawdziwe dane przykładowymi."),
    przyklad=("Prośba z pięciu części (wklej do czatu w zadaniu tygodnia):\n\n"
              "Cel: napisz plik lista_gosci.py z funkcjami dodaj_goscia(lista, imie, noce), liczba_gosci(lista) i raport(lista).\n"
              "Kontekst: Python 3.12, Windows, uczę się — kod ma być prosty, bez bibliotek, z komentarzami po polsku.\n"
              "Przykłady: po dodaj_goscia(l, \"Anna\", 2) lista ma element {\"imie\": \"Anna\", \"noce\": 2}; liczba_gosci(l) → 1; raport zwraca napis „Anna: 2 noce”.\n"
              "Ograniczenia: bez input() w funkcjach; noce < 1 → ValueError; puste imię → ValueError.\n"
              "Format: cały plik w jednym bloku kodu, potem lista założeń i polecenie do sprawdzenia."),
    demonstracja={"tytul": "Ta sama prośba w trzech iteracjach", "kroki": [
        "Iteracja 0 (zła): „zrób listę gości”. Model daje program z input() w pętli, który pyta o gości bez końca — nie da się go przetestować.",
        "Iteracja 1: wklejasz prośbę z pięciu części, ale najpierw dopisujesz: „zadaj do 5 pytań, zanim napiszesz kod”. Model pyta np., czy imiona mogą się powtarzać i jak liczyć gości — odpowiadasz.",
        "Iteracja 2: model daje plik. Sprawdzasz przykłady (Uruchom + własne wywołania). Jeden nie działa: raport zwraca „Anna: 2 nocy”.",
        "Iteracja 3: konkretna poprawka: „raport dla 2 nocy zwraca ‚2 nocy’, ma być ‚2 noce’; dla 1 — ‚1 noc’, dla 5 — ‚5 nocy’. Popraw tylko funkcję raport”. Działa.",
        "Wnioski do dziennika: pytania modelu ujawniły luki w specyfikacji; przykłady złapały błąd odmiany."],
        "wynik": "Działający plik po 3 krótkich iteracjach i lista założeń, z których jedna (odmiana „noc/noce/nocy”) wymagała decyzji człowieka."},
    jak_uruchomic=["Czat AI → nowa rozmowa → wklej prośbę z przykładu.", "Odpowiedź → skopiuj kod do pliku w PRACA → ▶ Uruchom."],
    cwiczenia=[
        C("prowadzone",
          "Oceń prośbę: „Napisz w Pythonie funkcję, która liczy cenę pobytu. Ma być dobra.” Których z pięciu części brakuje? Zaznacz dla każdej: jest / brak. Czas: 15 minut.",
          "Cel — jest (ogólnie); kontekst — brak; przykłady — brak; ograniczenia — brak; format — brak.",
          ["Cel: czy wiadomo, CO ma powstać? (ogólnie tak — funkcja ceny).", "Przykłady: czy są liczby wejście → wynik?", "„Ma być dobra” to nie ograniczenie — nie mówi, czego nie robić."],
          "Jest tylko ogólny cel; brakuje kontekstu (wersja, kto, gdzie), przykładów (wejście → wynik), ograniczeń (np. rabat, złe dane) i formatu odpowiedzi.",
          [wy("cel", "Cel", ["jest", "brak"], "jest"), wy("kontekst", "Kontekst", ["jest", "brak"], "brak"), wy("przyklady", "Przykłady", ["jest", "brak"], "brak"),
           wy("ogr", "Ograniczenia", ["jest", "brak"], "brak", bledy=[bl("jest", "„ma być dobra” nie mówi modelowi, czego NIE robić ani jak traktować złe dane")]),
           wy("format", "Format odpowiedzi", ["jest", "brak"], "brak")]),
        C("samodzielne",
          "Model odpowiedział kodem, ale dla Twojego przykładu (7 nocy, 1 osoba) program wypisuje 840.0 zamiast 756.0. Która wiadomość jest najlepszą następną prośbą? "
          "(A) „Nie działa, popraw.” (B) „Dla (7, 1) jest 840.0, ma być 756.0 — rabat 10% od 7 nocy nie działa; popraw tylko warunek rabatu i pokaż zmienioną linię.” "
          "(C) „Napisz wszystko od nowa lepiej.” Ile założeń warto poprosić model wypisać po każdej odpowiedzi — zero czy wszystkie? Czas: 15 minut.",
          "B; wszystkie założenia.",
          ["Która wiadomość ma konkretne wejście, wynik i oczekiwanie?", "Która ogranicza zakres zmiany?", "Założenia to miejsca, w których model zgadywał."],
          "B — konkretny przypadek, oczekiwany wynik, hipoteza i granica zmiany. Założenia: prosisz o wszystkie, bo tam ukrywają się błędy.",
          [wy("najlepsza", "Najlepsza następna wiadomość", ["A", "B", "C"], "B", bledy=[bl("C", "pisanie od nowa często wprowadza nowe błędy i gubi to, co już działało")]),
           wy("zal", "Założenia", ["zero", "wszystkie"], "wszystkie")]),
    ],
    typowe_bledy=[
        B("Model pisze dużo więcej, niż prosiłeś (GUI, baza, logowanie).", "Brak ograniczeń zakresu.", "Czy prośba mówi, czego nie robić?", "Dopisz „tylko X; bez interfejsu graficznego, bez bibliotek, maks. 40 linii”."),
        B("Każda poprawka psuje coś innego.", "Za długa rozmowa, model miesza wersje plików.", "Ile wersji kodu jest w rozmowie?", "Nowa rozmowa: wklej aktualny plik + 3 zdania ustaleń + jedną prośbę."),
        B("Kod nie pasuje do Twojego Pythona/systemu (ścieżki /home/…, komendy Linuksa).", "Brak kontekstu systemu.", "Czy podałeś Windows i wersję Pythona?", "Kontekst: „Windows 11, CMD, Python 3.12”."),
    ],
    pulapki=["Grzeczność nie szkodzi, ale nie zastępuje konkretów — „proszę, zrób to dobrze” nic nie mówi modelowi.",
             "Model chętnie się zgadza („Masz rację!”) nawet z błędną uwagą. Jeśli kwestionujesz wynik, poproś o sprawdzenie na przykładzie, a nie o przyznanie racji."],
    zadania=["Przepisz jedną swoją wcześniejszą prośbę do AI na wersję z pięciu części i porównaj wyniki.", "Poproś model o 5 pytań przed kodem w zadaniu tygodnia.", "Zapisz w dzienniku 3 założenia, które model przyjął bez pytania."],
    pytania=[["Jakie jest pięć części dobrej prośby?", "Cel, kontekst, przykłady wejście → wynik, ograniczenia, format odpowiedzi."],
             ["Dlaczego przykłady są tak ważne?", "Mówią modelowi najwięcej i jednocześnie są gotowymi testami do sprawdzenia odpowiedzi."],
             ["Co robisz, gdy rozmowa się rozjeżdża?", "Zaczynam nową rozmowę z aktualnym plikiem i krótkim podsumowaniem ustaleń."]],
    podsumowanie="Piszesz prośby z pięciu części, prosisz o pytania i założenia, poprawiasz iteracyjnie konkretnymi przypadkami i wiesz, czego nie wklejać.",
    test=[T("Co najbardziej poprawia trafność kodu od AI?", ["Dłuższe podziękowania", "Przykłady wejście → oczekiwany wynik", "Wielkie litery", "Prośba „zrób dobrze”"], 1, "Multishot prompting."),
          T("Model po poprawce psuje inne rzeczy. Co robisz?", ["Piszę „źle!”", "Nowa rozmowa z aktualnym plikiem i podsumowaniem", "Kupuję droższy plan", "Wyłączam komputer"], 1, "Krótki, czysty kontekst."),
          T("Po co prosić o listę założeń?", ["Żeby było dłużej", "Bo pokazują, gdzie model zgadywał", "Bo tak każe prawo", "Nie warto"], 1, "Tam szukasz błędów."),
          T("Co nie powinno trafić do czatu AI?", ["Fikcyjne dane z kursu", "Prawdziwy klucz API", "Opis funkcji", "Traceback z kursu"], 1, "Tajemnice zostają u Ciebie.")],
    w_praktyce=["Szablon 5 części trzymaj w Ściądze → Prompty.", "„Zadaj pytania, zanim napiszesz kod” — najtańsza poprawa jakości."],
    zrodla=[Z_ANTH_PROMPT, Z_ANTH_CLEAR, Z_ANTH_EX, Z_OAI_PROMPT],
)


# =========================================================================== TYDZIEŃ 3
SPECYFIKACJA = L(
    id="specyfikacja", nazwa="Specyfikacja: „Gotowe, gdy…” — zamówienie, które da się sprawdzić", tydzien=3,
    slowa=["specyfikacja", "wymagania", "kryteria akceptacji", "przypadek brzegowy", "gotowe gdy", "zakres"],
    cel="Po tej lekcji piszesz jednostronicową specyfikację (cel, wejście, wynik, przykłady, przypadki brzegowe, poza zakresem, gotowe gdy) — taką, z której agent zbuduje kod, a Ty test.",
    po_co="Agent zrobi dokładnie to, co opiszesz — a czego nie opiszesz, wymyśli. Specyfikacja to Twoja najważniejsza praca w vibe codingu.",
    wymagania=["Lekcja „Rozmowa z AI”.", "Edytor lub Notatnik (plik specyfikacja.md w PRACA)."],
    wyjasnienie=(
        "## Po co spisywać, skoro można powiedzieć?\n"
        "Rozmowa znika, plik zostaje. Specyfikację dasz agentowi dziś, przeczytasz za miesiąc przy poprawce i pokażesz klientowi przy odbiorze. "
        "Dokumentacja Claude Code (Best practices) radzi wprost: daj agentowi sposób na zweryfikowanie pracy — testy, przykłady, oczekiwane wyniki — i najpierw planuj, potem koduj.\n"
        "## Siedem sekcji specyfikacji\n"
        "| sekcja | co wpisujesz | przykład (walidacja e-maila) |\n"
        "|---|---|---|\n"
        "| Cel | jedno zdanie: co i dla kogo | funkcja sprawdzająca adres e-mail gościa w formularzu rezerwacji |\n"
        "| Wejście | jakie dane, jakiego typu | napis (str) |\n"
        "| Wynik | co zwraca / co robi | True albo False |\n"
        "| Przykłady | 4–8 par wejście → wynik | \"anna@pod-lipa.pl\" → True; \"anna@\" → False |\n"
        "| Przypadki brzegowe | puste, za długie, dziwne znaki, granice | \"\" → False; spacje na końcu → usuń i sprawdź |\n"
        "| Poza zakresem | czego NIE robić | nie wysyłamy maili, nie sprawdzamy, czy skrzynka istnieje |\n"
        "| Gotowe, gdy | jak sprawdzisz | przechodzą testy Mentora; przykłady dają dokładnie te wyniki |\n"
        "## Przypadki brzegowe — gdzie mieszkają błędy\n"
        "- Puste dane: pusta lista, pusty napis, 0.\n"
        "- Granice: dokładnie 7 nocy, dokładnie 18 lat, ostatni dzień miesiąca.\n"
        "- Złe typy i wartości: \"abc\" zamiast liczby, liczba ujemna.\n"
        "- Polskie znaki i spacje: \"Łódź \", \"Żaneta\".\n"
        "- Duże dane: 10 000 wierszy zamiast 3.\n"
        "## Poza zakresem — hamulec dla agenta\n"
        "Agenci lubią „pomagać więcej”: dodają bibliotekę, przepisują sąsiedni plik, zmieniają nazwy. Sekcja „Poza zakresem” i lista plików, których nie wolno ruszać, to najprostsza ochrona.\n"
        "## Gotowe, gdy — kryteria akceptacji\n"
        "Kryterium musi dać odpowiedź tak/nie. „Działa szybko” — nie; „raport dla 10 000 wierszy powstaje w mniej niż 2 sekundy” — tak. "
        "„Ładny” — nie; „ma nagłówek h1, formularz z polami noce i osoby i działa na telefonie (meta viewport)” — tak.\n"
        "## Format pliku: Markdown\n"
        "Specyfikację piszesz w .md: `# Tytuł`, `## Sekcja`, listy `- `. Agenci czytają Markdown świetnie, GitHub pokazuje go ładnie."),
    przyklad=("# Specyfikacja: walidacja.py\n\n## Cel\nFunkcje sprawdzające e-mail i telefon gościa w formularzu rezerwacji „Pod Lipą”.\n\n"
              "## Wejście\nNapis (str).\n\n## Wynik\nczy_email(tekst) → True/False; czy_telefon(tekst) → True/False.\n\n"
              "## Przykłady\n- czy_email(\"anna@pod-lipa.pl\") → True\n- czy_email(\"anna@\") → False\n- czy_telefon(\"600 700 800\") → True\n- czy_telefon(\"+48 600-700-800\") → True\n- czy_telefon(\"12345\") → False\n\n"
              "## Przypadki brzegowe\n- \"\" → False dla obu\n- spacje na początku/końcu ignorujemy\n\n"
              "## Poza zakresem\n- nie sprawdzamy, czy skrzynka istnieje; bez bibliotek spoza Pythona\n\n## Gotowe, gdy\n- przechodzą testy Mentora (zadanie tygodnia 3)"),
    demonstracja={"tytul": "Od mglistej prośby do specyfikacji w 15 minut", "kroki": [
        "Klientka „Pod Lipą” pisze: „Chciałabym, żeby formularz nie przyjmował złych telefonów”.",
        "Cel: funkcja czy_telefon(tekst). Pytasz siebie: co to jest „dobry telefon”? Decyzja: polski numer, 9 cyfr, opcjonalnie +48 na początku, spacje i myślniki dozwolone.",
        "Przykłady: \"600700800\" → True; \"600 700 800\" → True; \"+48 600-700-800\" → True; \"48600700800\" → False (bez plusa niejednoznaczne — decyzja!); \"12345\" → False; \"\" → False.",
        "Poza zakresem: numery zagraniczne (zapisujesz jako pytanie do klientki), sprawdzanie, czy numer istnieje.",
        "Gotowe, gdy: wszystkie przykłady dają wynik z listy; testy Mentora przechodzą. Każdy przykład to linia testu — spisałeś test, zanim powstał kod."],
        "wynik": "Specyfikacja z 6 przykładami, jedną świadomą decyzją (48 bez plusa = False) i jednym pytaniem do klientki — agent nie musi niczego zgadywać."},
    jak_uruchomic=["Utwórz specyfikacja.md w PRACA (zadanie tygodnia — „📝 Utwórz plik ćwiczenia” wstawi szablon sekcji).", "„✔ Sprawdź wynik” sprawdzi, czy są wszystkie sekcje i co najmniej 4 przykłady."],
    cwiczenia=[
        C("prowadzone",
          "Specyfikacja funkcji cena_sniadan(osoby, noce): 35 zł za osobę za dzień; dzieci nie są liczone osobno. Uzupełnij wyniki przykładów: (1) cena_sniadan(2, 3), (2) cena_sniadan(1, 1), "
          "(3) cena_sniadan(4, 7). Do której sekcji wpiszesz „osoby = 0 → ValueError”? Czas: 15 minut.",
          "(1) 210; (2) 35; (3) 980; „osoby = 0 → ValueError” → Przypadki brzegowe.",
          ["2 osoby × 3 dni × 35 zł.", "4 × 7 × 35.", "Zero osób to wartość na granicy dopuszczalnych danych."],
          "2·3·35 = 210; 1·1·35 = 35; 4·7·35 = 980. Osoby = 0 to przypadek brzegowy (sekcja „Przypadki brzegowe”).",
          [kw("p1", "cena_sniadan(2, 3) (zł)", 210), kw("p2", "cena_sniadan(1, 1) (zł)", 35), kw("p3", "cena_sniadan(4, 7) (zł)", 980),
           wy("sekcja", "Sekcja dla „osoby = 0 → ValueError”", ["Cel", "Przykłady", "Przypadki brzegowe", "Poza zakresem"], "Przypadki brzegowe")]),
        C("samodzielne",
          "Które kryteria „Gotowe, gdy” są sprawdzalne (tak/nie)? (1) „Strona ładnie wygląda” (2) „Raport dla 10 000 wierszy powstaje w < 2 s” (3) „Kod jest dobry” "
          "(4) „Funkcja dla (7, 1) zwraca 756.0” (5) „Formularz ma pola noce i osoby”. Ile jest sprawdzalnych? Czas: 15 minut.",
          "Sprawdzalne: 2, 4, 5 → 3 kryteria.",
          ["Zadaj pytanie: czy dwie osoby, sprawdzając, dadzą tę samą odpowiedź?", "„Ładnie” i „dobry” zależą od opinii.", "Liczby, czasy i konkretne elementy da się sprawdzić."],
          "Sprawdzalne są (2) czas z progiem, (4) konkretny wynik, (5) konkretne pola — razem 3. (1) i (3) to opinie.",
          [li("ile", "Liczba sprawdzalnych kryteriów", 3), wy("k1", "(1) Strona ładnie wygląda", ["sprawdzalne", "niesprawdzalne"], "niesprawdzalne"),
           wy("k4", "(4) Dla (7, 1) zwraca 756.0", ["sprawdzalne", "niesprawdzalne"], "sprawdzalne")]),
    ],
    typowe_bledy=[
        B("Agent zrobił „coś innego”, niż chciałeś.", "Specyfikacja bez przykładów — model zinterpretował słowa po swojemu.", "Ile przykładów wejście → wynik ma specyfikacja?", "Minimum 4 przykłady, w tym 2 brzegowe."),
        B("Agent dodał bibliotekę i przerobił 5 plików.", "Brak sekcji „Poza zakresem”.", "Czy napisałeś, czego nie ruszać?", "Dopisz listę plików i rzeczy zakazanych; w Claude Code użyj trybu planu (tydzień 5)."),
        B("Klient przy odbiorze: „miało być inaczej”.", "Decyzje podjęte po cichu zamiast zapisane i potwierdzone.", "Czy decyzje są w specyfikacji?", "Sekcja „Decyzje i pytania do klienta” — wysyłasz ją przed budową."),
    ],
    pulapki=["Specyfikacja nie musi być długa — jedna strona wystarczy. Długie specyfikacje agent czyta gorzej i drożej.",
             "Nie wpisuj w specyfikację rozwiązania („użyj wyrażeń regularnych”), jeśli nie masz powodu — opisuj CO, a nie JAK."],
    zadania=["Napisz specyfikację dla funkcji czy_telefon z demonstracji (zadanie tygodnia).", "Dla jednej codziennej rzeczy (np. lista zakupów) wypisz 5 przypadków brzegowych.", "Przerób 2 niesprawdzalne kryteria z ćwiczenia na sprawdzalne."],
    pytania=[["Jakie sekcje ma specyfikacja?", "Cel, wejście, wynik, przykłady, przypadki brzegowe, poza zakresem, gotowe gdy."],
             ["Czym jest kryterium akceptacji?", "Warunkiem z odpowiedzią tak/nie, który mówi, kiedy praca jest skończona."],
             ["Dlaczego przykłady w specyfikacji to „testy przed kodem”?", "Bo każdy przykład wejście → wynik można od razu zamienić na test."]],
    podsumowanie="Piszesz specyfikację z 7 sekcji, wymyślasz przypadki brzegowe, ograniczasz agenta sekcją „Poza zakresem” i formułujesz sprawdzalne kryteria „Gotowe, gdy”.",
    test=[T("Które kryterium jest sprawdzalne?", ["Kod jest czytelny", "Funkcja dla \"\" zwraca False", "Program jest nowoczesny", "Strona jest ładna"], 1, "Ma odpowiedź tak/nie."),
          T("Po co sekcja „Poza zakresem”?", ["Żeby było dłużej", "Żeby agent nie robił rzeczy, o które nie prosiłeś", "Dla prawnika", "Nie ma sensu"], 1, "Hamulec dla nadgorliwego agenta."),
          T("Który przykład jest przypadkiem brzegowym dla „rabat od 7 nocy”?", ["3 noce", "Dokładnie 7 nocy", "100 nocy", "Każdy"], 1, "Granica."),
          T("W jakim formacie piszemy specyfikację?", ["Markdown (.md)", ".exe", ".zip", "Zdjęcie kartki"], 0, "Czytelny dla ludzi, agentów i GitHuba.")],
    w_praktyce=["Każde zlecenie dla agenta = plik specyfikacji w repozytorium.", "Decyzje zapisuj w specyfikacji, nie w głowie."],
    zrodla=[Z_CC_BEST, Z_ANTH_CLEAR, ["Atlassian — Acceptance criteria: definicja i przykłady (tłumaczenie robocze)", "https://www.atlassian.com/work-management/project-management/acceptance-criteria", D]],
)

PIERWSZY = L(
    id="pierwszy_program_z_ai", nazwa="Pierwszy program z AI: od specyfikacji do zielonego testu", tydzien=3,
    slowa=["pętla pracy", "generowanie", "weryfikacja", "test", "poprawka", "kod od AI", "kopiuj"],
    cel="Po tej lekcji przechodzisz pełną pętlę: specyfikacja → prośba do czatu AI → plik w PRACA → uruchomienie → testy Mentora → konkretna poprawka → zapis w dzienniku.",
    po_co="To dokładnie ta sama pętla, którą od tygodnia 4 wykonasz z agentem — tylko wolniej i ręcznie, żebyś widział każdy krok.",
    wymagania=["Lekcje „Specyfikacja” i „Rozmowa z AI”.", "Darmowy czat AI.", "Środowisko kursu (zakładka Środowisko — zielone)."],
    wyjasnienie=(
        "## Pętla pracy vibe codera\n"
        "| krok | kto | co powstaje |\n"
        "|---|---|---|\n"
        "| 1. Specyfikacja | Ty | specyfikacja.md z przykładami |\n"
        "| 2. Prośba | Ty | wiadomość z 5 części + specyfikacja |\n"
        "| 3. Kod | AI | plik .py |\n"
        "| 4. Uruchomienie | Ty | wynik albo traceback |\n"
        "| 5. Sprawdzenie | testy Mentora | ✔ albo lista przypadków, które nie przechodzą |\n"
        "| 6. Poprawka | AI na Twoje konkretne zgłoszenie | nowa wersja |\n"
        "| 7. Zapis | Ty | dziennik: co sprawdziłem, czego nie rozumiem |\n"
        "## Kopiowanie kodu z czatu — bez pułapek\n"
        "- Używaj przycisku „Copy/Kopiuj” bloku kodu (nie zaznaczaj myszą — łatwo uciąć linię).\n"
        "- Wklejaj CAŁY plik, jeśli model dał cały plik; jeśli dał fragment — zapytaj, gdzie dokładnie go wstawić, albo poproś o cały plik.\n"
        "- Zapisz z rozszerzeniem .py (nie .txt). Nazwa pliku musi być taka, jak w zadaniu — testy szukają konkretnej nazwy.\n"
        "- Sprawdź wcięcia po wklejeniu (IndentationError = coś się przesunęło).\n"
        "## Jak testy Mentora sprawdzają Twój plik\n"
        "„✔ Sprawdź wynik” uruchamia niezależne testy z paczki kursu (folder WERYFIKATORY). Testy importują Twój plik i wywołują funkcje z różnymi danymi — także takimi, których nie było w przykładach. "
        "Wynik: zielony (zaliczone) albo lista nieprzechodzących przypadków, np. „koszt_pobytu(7, 1): oczekiwano 756.0, otrzymano 840.0”. "
        "Testów nie da się „przekonać”: suma kontrolna SHA-256 pilnuje, że nikt (także agent) ich nie zmienił.\n"
        "## Czytaj kod, zanim zaliczysz\n"
        "Zielony test to warunek konieczny, ale nie jedyny. Zanim zamkniesz zadanie, przeczytaj kod z pytaniami z lekcji „Czytanie kodu 2”: co przyjmuje, co zwraca, kiedy odmawia, co zmienia poza sobą. "
        "Jeśli jakiejś linii nie rozumiesz — zapytaj model „wyjaśnij linię 7 jak początkującemu”.\n"
        "## Ile poprawek to za dużo?\n"
        "Reguła trzech: jeśli po 3 konkretnych poprawkach błąd wraca — zatrzymaj się. Zwykle specyfikacja jest niejasna albo rozmowa za długa. Popraw specyfikację i zacznij nową rozmowę."),
    przyklad=("Fragment dziennika po zadaniu:\n\n"
              "## 2026-12-02 — kalkulator_pobytu.py\n- Specyfikacja: 6 przykładów, 2 brzegowe (7 nocy, 0 nocy).\n"
              "- Iteracje: 2 (pierwsza wersja liczyła rabat od 8 nocy — warunek > zamiast >=).\n"
              "- Sprawdzenie: testy Mentora ✔, przeczytałem kod: rozumiem wszystkie linie poza round(x, 2) — doczytałem.\n"
              "- Pytanie: czy cena 120 zł ma być parametrem? (zapisane do specyfikacji v2)."),
    demonstracja={"tytul": "Kalkulator pobytu — pełna pętla", "kroki": [
        "Specyfikacja (z lekcji start_vibe): koszt_pobytu(noce, osoby, cena_za_osobe_noc=120), rabat 10% od 7 nocy, < 1 → ValueError, wynik zaokrąglony do groszy.",
        "Prośba do czatu: specyfikacja + „cały plik w jednym bloku, bez input() w funkcji, blok if __name__ == '__main__' z przykładowym wywołaniem”.",
        "Kopiujesz przyciskiem Copy, zapisujesz jako kalkulator_pobytu.py w PRACA (zadanie tygodnia → „📝 Utwórz plik ćwiczenia”, potem wklej pod nagłówkiem).",
        "▶ Uruchom: blok __main__ wypisuje przykład. ✔ Sprawdź wynik: 1 przypadek nie przechodzi — „koszt_pobytu(2, 2, cena_za_osobe_noc=150): TypeError: unexpected keyword argument” — model nazwał parametr „cena”.",
        "Zgłoszenie: „Parametr ma się nazywać dokładnie cena_za_osobe_noc (tak jest w specyfikacji) — zmień tylko nazwę”. Nowa wersja → ✔ zielony.",
        "Czytasz kod 4 pytaniami i zapisujesz dziennik."],
        "wynik": "Zadanie zaliczone automatycznie; wiesz, że nazwy z specyfikacji są częścią „umowy” z testami, a przeczytany kod rozumiesz linia po linii."},
    jak_uruchomic=["Zadanie tygodnia → „📝 Utwórz plik ćwiczenia” → wklej kod → „▶ Uruchom” → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Test Mentora pokazał: „koszt_pobytu(7, 2): oczekiwano 1512.0, otrzymano 1680”. Specyfikacja: 120 zł/os./noc, rabat 10% od 7 nocy. "
          "Ile wynosi koszt bez rabatu? Czy rabat został naliczony (tak/nie)? Jaki znak porównania najpewniej jest w warunku zamiast >=? Czas: 15 minut.",
          "Bez rabatu: 7·2·120 = 1680 (to otrzymano) → rabat nie został naliczony; warunek najpewniej `noce > 7` zamiast `noce >= 7`.",
          ["Policz 7 × 2 × 120.", "Porównaj z „otrzymano”.", "Dla 7 nocy rabat nie działa, a od 8 pewnie tak — który znak wyklucza samą granicę?"],
          "1680 = cena bez rabatu, czyli warunek nie objął 7 nocy → zamiast >= jest >. 1680·0,9 = 1512.0.",
          [kw("bez", "Koszt bez rabatu (zł)", 1680), wy("rabat", "Czy rabat naliczono?", TN, "nie"), wy("znak", "Znak w warunku", [">", "<", "==", "<="], ">")]),
        C("samodzielne",
          "Uporządkuj pętlę pracy: wpisz numery kroków w kolejności dla: A) testy Mentora, B) specyfikacja, C) zapis w dzienniku, D) prośba do AI, E) uruchomienie. Podaj kolejność jako ciąg liter (np. ABCDE). "
          "Druga sprawa: po ilu nieudanych konkretnych poprawkach zatrzymujesz się i poprawiasz specyfikację? Czas: 15 minut.",
          "BDEAC; po 3 poprawkach.",
          ["Najpierw zawsze to, co robisz Ty, zanim cokolwiek powstanie.", "Testy uruchamiasz po uruchomieniu programu.", "Reguła z lekcji ma nazwę z liczbą."],
          "Specyfikacja (B) → prośba (D) → uruchomienie (E) → testy (A) → dziennik (C) = BDEAC. Reguła trzech poprawek.",
          [tx("kolejnosc", "Kolejność liter", ["BDEAC"]), li("ile", "Po ilu nieudanych poprawkach się zatrzymujesz?", 3)]),
    ],
    typowe_bledy=[
        B("Mentor: „Brak pliku kalkulator_pobytu.py”.", "Plik zapisany pod inną nazwą lub w innym folderze (albo jako .py.txt).", "Mój projekt → Otwórz folder; rozszerzenia widoczne?", "Nazwa dokładnie jak w zadaniu, w katalogu PRACA."),
        B("„AssertionError: Brak funkcji koszt_pobytu”.", "Model nazwał funkcję inaczej (np. oblicz_koszt).", "Szukaj `def` w pliku.", "Zmień nazwę na tę ze specyfikacji — nazwy to umowa z testem."),
        B("Testy „wiszą” i kończą się po czasie.", "W kodzie jest input() poza blokiem __main__ — test czeka na klawiaturę.", "Szukaj input( w pliku.", "Przenieś input() do bloku if __name__ == \"__main__\":."),
    ],
    pulapki=["Nie dopasowuj specyfikacji do kodu, który „prawie działa”. To kod ma spełnić specyfikację.",
             "Zielony test ≠ rozumiem kod. Zadanie kończy się, gdy umiesz wyjaśnić każdą linię."],
    zadania=["Przejdź pełną pętlę dla walidacja.py (zadanie tygodnia).", "Zapisz w dzienniku liczbę iteracji i co je spowodowało.", "Poproś model o wyjaśnienie jednej linii, której nie rozumiesz."],
    pytania=[["Jakie są kroki pętli pracy?", "Specyfikacja → prośba → kod → uruchomienie → testy → poprawka → zapis."],
             ["Dlaczego nazwa funkcji musi być dokładnie taka jak w zadaniu?", "Testy importują ją po nazwie — inna nazwa to „Brak funkcji”."],
             ["Kiedy zadanie jest naprawdę skończone?", "Gdy testy są zielone i rozumiesz każdą linię kodu."]],
    podsumowanie="Przeszedłeś pełną pętlę ze zwykłym czatem: specyfikacja, kod, uruchomienie, testy, konkretna poprawka i dziennik — ta sama pętla czeka Cię z agentem.",
    test=[T("Co robisz po zielonym teście?", ["Nic", "Czytam kod 4 pytaniami i zapisuję dziennik", "Usuwam plik", "Proszę o nowy kod"], 1, "Zielony test to warunek konieczny."),
          T("Testy Mentora „wiszą”. Najczęstsza przyczyna:", ["Za wolny komputer", "input() poza blokiem __main__", "Zła wersja Windows", "Brak internetu"], 1, "Test czeka na klawiaturę."),
          T("Model nazwał funkcję inaczej niż w zadaniu. Co robisz?", ["Zmieniam zadanie", "Zmieniam nazwę na tę ze specyfikacji", "Usuwam test", "Ignoruję"], 1, "Nazwa to umowa."),
          T("Reguła trzech poprawek mówi:", ["Zawsze 3 iteracje", "Po 3 nieudanych poprawkach popraw specyfikację i zacznij nową rozmowę", "3 pliki naraz", "3 testy"], 1, "Problem jest zwykle wyżej.")],
    w_praktyce=["Jedno zadanie = jedna rozmowa = jeden wpis w dzienniku.", "Nazwy z zadania kopiuj, nie przepisuj."],
    zrodla=[Z_CC_BEST, Z_ANTH_PROMPT, Z_PY_FUN],
)

POWTORKA_0 = L(
    id="powtorka_etap_0", nazwa="Powtórka etapu 0 i mini-projekt: rabaty sezonowe", tydzien=3,
    slowa=["powtórka", "mini-projekt", "rabat", "sezon", "samodzielnie", "etap 0"],
    cel="Po tej lekcji samodzielnie (z czatem AI) budujesz mały moduł rabaty.py od specyfikacji do zielonego testu i oceniasz, czy jesteś gotowy na agenta.",
    po_co="Etap 1 daje Ci agenta, który zmienia pliki sam. Bez pewnych podstaw z etapu 0 nie odróżnisz dobrej zmiany od złej.",
    wymagania=["Wszystkie lekcje tygodni 0–3.", "Quiz tygodnia 3 (sobota)."],
    wyjasnienie=(
        "## Co już umiesz (lista kontrolna)\n"
        "| umiejętność | sprawdzian |\n"
        "|---|---|\n"
        "| pliki i ścieżki | wiesz, gdzie jest PRACA, widzisz rozszerzenia |\n"
        "| terminal | cd, dir, mkdir, type, python plik.py, Ctrl + C |\n"
        "| czytanie kodu | przewidujesz wynik funkcji z if, for, listą i słownikiem |\n"
        "| błędy | czytasz traceback od dołu, znasz 8 wyjątków |\n"
        "| rozmowa z AI | 5 części prośby, iteracje, reguła trzech |\n"
        "| specyfikacja | 7 sekcji, przypadki brzegowe, kryteria tak/nie |\n"
        "## Mini-projekt: rabaty.py\n"
        "Gospodarstwo „Pod Lipą” ma cennik sezonowy. Specyfikacja (pełna w zadaniu tygodnia):\n"
        "- `sezon(miesiac)` → \"wysoki\" dla 6, 7, 8 i 12; \"niski\" dla pozostałych 1–12; inna liczba → ValueError.\n"
        "- `cena_nocy(miesiac)` → 150 zł w sezonie wysokim, 110 zł w niskim (za osobę).\n"
        "- `rabat(noce, osoby)` → procent rabatu: 10 od 7 nocy, 5 dla 4+ osób, rabaty SUMUJĄ SIĘ (7 nocy i 4 osoby → 15), maksymalnie 15.\n"
        "- `do_zaplaty(miesiac, noce, osoby)` → kwota po rabacie, zaokrąglona do groszy.\n"
        "## Jak się ocenić\n"
        "- Ile iteracji z AI potrzebowałeś? (1–3 dobrze, 4+ — wróć do lekcji „Specyfikacja”).\n"
        "- Czy umiesz wyjaśnić każdą linię? (jeśli nie — lekcje „Czytanie kodu” 1–2).\n"
        "- Czy czytasz traceback bez pomocy? (jeśli nie — „Komunikat błędu”).\n"
        "- Quiz tygodnia 3 ≥ 70%? Jeśli nie, Mentor wskaże lekcje do powtórki.\n"
        "## Co dalej\n"
        "Tydzień 4: decyzja o planie (koszty), instalacja Claude Code i Codex. Jeśli nie kupujesz planu — przechodzisz kurs ścieżką z zapisami pracy agenta; umiejętności są te same: czytanie, sprawdzanie, poprawianie."),
    przyklad=kod("powtorka_etap_0:przyklad",
                 "def sezon(miesiac):\n    if miesiac not in range(1, 13):\n        raise ValueError(\"miesiąc 1–12\")\n    return \"wysoki\" if miesiac in (6, 7, 8, 12) else \"niski\"\n\n"
                 "print(sezon(7), sezon(3), sezon(12))\n",
                 "wysoki niski wysoki\n"),
    demonstracja={"tytul": "Specyfikacja → test w głowie dla rabat()", "kroki": [
        "Wypisujesz przykłady z reguł: (3, 2) → 0; (7, 2) → 10; (3, 4) → 5; (7, 4) → 15; (14, 6) → 15 (maks.).",
        "Brzegowe: (6, 3) → 0 (tuż przed obiema granicami); (7, 3) → 10; (6, 4) → 5.",
        "Prosisz czat o rabaty.py z tymi przykładami. Dostajesz funkcję rabat z if/elif: if noce >= 7: return 10 / elif osoby >= 4: return 5.",
        "Twój przykład (7, 4) → oczekujesz 15, kod daje 10: elif nie pozwala zsumować rabatów — to dokładnie błąd, który złapałby test.",
        "Konkretna poprawka: „rabaty się sumują: dwa niezależne if dodające do zmiennej, na końcu min(wynik, 15)”. Test w głowie: (7, 4) → 10 + 5 = 15 ✔."],
        "wynik": "Złapałeś błąd logiczny (elif zamiast sumowania) jeszcze przed uruchomieniem — dzięki przykładom ze specyfikacji."},
    jak_uruchomic=["Zadanie tygodnia „Mini-projekt: rabaty.py” → „📝 Utwórz plik ćwiczenia” → czat AI → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Policz według specyfikacji mini-projektu: (1) rabat(7, 4), (2) rabat(10, 2), (3) do_zaplaty(7, 7, 2) — lipiec, 7 nocy, 2 osoby (150 zł/os./noc, rabat 10%). Czas: 15 minut.",
          "(1) 15; (2) 10; (3) 7·2·150 = 2100 → −10% = 1890,00 zł.",
          ["7 nocy daje 10, 4 osoby dają 5 — sumują się.", "10 nocy, 2 osoby — tylko rabat za noce.", "Lipiec to sezon wysoki: 150 zł."],
          "rabat(7, 4) = 15; rabat(10, 2) = 10; do_zaplaty(7, 7, 2) = 2100 · 0,9 = 1890,00 zł.",
          [li("r1", "rabat(7, 4) (%)", 15, bledy=[bl(10, "rabaty się sumują — 10 za noce + 5 za osoby")]), li("r2", "rabat(10, 2) (%)", 10),
           kw("kw", "do_zaplaty(7, 7, 2) (zł)", 1890, bledy=[bl(2100, "to kwota przed rabatem 10% za 7 nocy"), bl(1386, "lipiec to sezon wysoki — 150 zł, nie 110")])]),
        C("samodzielne",
          "Samoocena gotowości. Odpowiedz uczciwie: (1) czy potrafisz bez pomocy przeczytać traceback i wskazać linię? (2) ile iteracji potrzebowałeś w kalkulator_pobytu? "
          "Następnie policz: miesiąc 13 w sezon() — co powinno się stać (nazwa wyjątku)? I ile wynosi do_zaplaty(3, 2, 1) (marzec, 2 noce, 1 osoba)? Czas: 20 minut.",
          "Wyjątek: ValueError; do_zaplaty(3, 2, 1) = 2·1·110 = 220,00 zł. (Samoocena — dowolna, zapisz w dzienniku.)",
          ["Miesiąc spoza 1–12 to zła wartość dobrego typu.", "Marzec — sezon niski.", "2 noce i 1 osoba — bez rabatu."],
          "ValueError dla 13; 2 × 1 × 110 = 220,00 zł bez rabatu.",
          [tx("wyj", "Wyjątek dla miesiąca 13", ["ValueError"]), kw("kw", "do_zaplaty(3, 2, 1) (zł)", 220)]),
    ],
    typowe_bledy=[
        B("Rabat 7 nocy + 4 osoby wychodzi 10 zamiast 15.", "elif zamiast niezależnych if — rabaty się nie sumują.", "Przykład (7, 4).", "Dwa osobne if dodające do zmiennej, potem min(…, 15)."),
        B("sezon(\"7\") zwraca „niski”.", "Napis \"7\" to nie liczba 7 — `\"7\" in (6, 7, 8, 12)` to False.", "Skąd przychodzi miesiąc (input? CSV?)", "Zamień na int przy wczytywaniu danych; w specyfikacji zapisz typ wejścia."),
    ],
    pulapki=["Mini-projekt to nie egzamin — jeśli utknąłeś, rozwiązanie wzorcowe jest w materiałach (rozwiazania/), ale najpierw 3 konkretne iteracje z AI.",
             "Nie przechodź do etapu 1 z poczuciem „kopiuję, ale nie wiem co” — to sygnał, by powtórzyć lekcje czytania kodu."],
    zadania=["Zbuduj rabaty.py i zalicz test.", "Wypełnij samoocenę w dzienniku.", "Zrób quiz tygodnia 3."],
    pytania=[["Dlaczego elif psuje sumowanie rabatów?", "Bo wykonuje tylko pierwszy pasujący blok — drugi rabat jest pomijany."],
             ["Jakie przykłady wpiszesz dla granic rabatu?", "6 i 7 nocy, 3 i 4 osoby, oraz kombinację 7 nocy i 4 osób."],
             ["Kiedy jesteś gotowy na agenta?", "Gdy czytasz traceback i kod samodzielnie, piszesz specyfikację z przykładami i zaliczasz mini-projekt w 1–3 iteracjach."]],
    podsumowanie="Zbudowałeś mini-projekt od specyfikacji do testu, oceniłeś gotowość i wiesz, które lekcje powtórzyć przed etapem z agentem.",
    test=[T("rabat(7, 4) według specyfikacji to:", ["10", "5", "15", "20"], 2, "Sumują się do maks. 15."),
          T("Miesiąc 12 to sezon:", ["wysoki", "niski", "błąd", "zależy od roku"], 0, "6, 7, 8 i 12."),
          T("Jaki jest dobry wynik samooceny przed etapem 1?", ["Kopiuję kod bez czytania", "Czytam traceback i kod sam, mini-projekt w 1–3 iteracjach", "Nie potrzebuję testów", "Mam dwa plany AI"], 1,
            "Agent przyspiesza tylko tego, kto umie sprawdzać.")],
    w_praktyce=["Przed każdym etapem — lista kontrolna umiejętności.", "Przykłady kombinacji (7 nocy + 4 osoby) łapią błędy logiki."],
    zrodla=[Z_CC_BEST, Z_PY_TUT, Z_ANTH_EX],
)

