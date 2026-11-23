# -*- coding: utf-8 -*-
"""Etap 1, tygodnie 1–3: zmienne i typy, print/input, warunki, pętle, listy, napisy, funkcje, słowniki, wyjątki, moduły standardowe, powtórka etapu.
Przykłady z fikcyjnego sklepu papierniczego „Papierowy Kot” (ceny, ilości, rabaty) — ten sam świat aż do projektu końcowego."""

from wspolne import B, C, L, T, bl, kod, kw, li, tx, wy
import zrodla as Z

# =========================================================================== TYDZIEŃ 1
ZMIENNE = L(
    id="zmienne", nazwa="Zmienne i typy danych: int, float, str, bool", tydzien=1,
    slowa=["zmienna", "typ", "int", "float", "str", "bool", "type", "przypisanie", "operator", "rzutowanie", "f-string"],
    cel="Po tej lekcji tworzysz zmienne, rozpoznajesz typy int, float, str i bool funkcją type(), liczysz operatorami + - * / // % ** i zamieniasz typy (int(), float(), str()).",
    po_co="Każdy test porównuje wartości określonego typu: „5” to nie 5. Połowa błędów w aplikacjach (i w zgłoszeniach testerów) to złe typy danych.",
    wymagania=["Lekcja „Terminal i pierwszy program”.", "Środowisko kursu w Mentorze (przycisk ▶ Uruchom)."],
    wyjasnienie=(
        "## Zmienna = pudełko z etykietą\n"
        "`cena = 4.50` — Python tworzy pudełko o nazwie cena i wkłada do niego 4.50. Znak `=` to **przypisanie** („włóż do pudełka”), nie porównanie. Nowe przypisanie podmienia zawartość.\n"
        "Nazwy: małe litery i podkreślenia (`cena_brutto`), bez spacji i polskich znaków, nie zaczynają się cyfrą. Wielkość liter ma znaczenie: `Cena` i `cena` to dwie różne zmienne.\n"
        "## Cztery podstawowe typy\n"
        "| typ | co to | przykład |\n|---|---|---|\n"
        "| `int` | liczba całkowita | `ilosc = 120` |\n"
        "| `float` | liczba z częścią ułamkową (kropka!) | `cena = 4.50` |\n"
        "| `str` | napis (tekst w cudzysłowie) | `nazwa = \"Zeszyt A5\"` |\n"
        "| `bool` | prawda/fałsz | `dostepny = True` |\n"
        "`type(x)` mówi, jakiego typu jest wartość: `type(4.5)` → `<class 'float'>`.\n"
        "## Operatory\n"
        "`+ - *` jak w matematyce; `/` dzielenie zawsze daje float (`7 / 2` → 3.5); `//` dzielenie całkowite (`7 // 2` → 3); `%` reszta (`7 % 2` → 1); `**` potęga (`2 ** 3` → 8). "
        "Na napisach: `+` skleja (`\"ab\" + \"cd\"` → \"abcd\"), `*` powtarza (`\"-\" * 5`).\n"
        "## Zamiana typów (rzutowanie)\n"
        "`int(\"12\")` → 12, `float(\"4.5\")` → 4.5, `str(12)` → \"12\". `int(\"4,5\")` da błąd ValueError — Python używa kropki. `\"5\" + 5` da TypeError: nie dodasz napisu do liczby.\n"
        "## f-string — liczby w tekście\n"
        "`f\"Razem: {razem:.2f} zł\"` wstawia wartość zmiennej w napis; `:.2f` to 2 miejsca po przecinku. Uwaga: float bywa niedokładny (`0.1 + 0.2` → 0.30000000000000004), dlatego kwoty wypisujesz z `:.2f`, a w testach porównujesz z tolerancją."),
    przyklad=kod("zmienne", (
        "nazwa = \"Zeszyt A5 w kratkę\"\n"
        "cena = 4.50\n"
        "ilosc = 3\n"
        "dostepny = True\n\n"
        "razem = cena * ilosc\n"
        "print(nazwa, type(nazwa))\n"
        "print(cena, type(cena))\n"
        "print(ilosc, type(ilosc))\n"
        "print(dostepny, type(dostepny))\n"
        "print(f\"Do zapłaty: {razem:.2f} zł\")\n"
        "print(\"Paczki po 4 szt.:\", 10 // 4, \"reszta:\", 10 % 4)\n"), (
        "Zeszyt A5 w kratkę <class 'str'>\n4.5 <class 'float'>\n3 <class 'int'>\nTrue <class 'bool'>\nDo zapłaty: 13.50 zł\nPaczki po 4 szt.: 2 reszta: 2\n")),
    demonstracja={"tytul": "Paragon za 3 zeszyty — cztery typy w jednym programie", "kroki": [
        "`nazwa = \"Zeszyt A5 w kratkę\"` — napis (str) w cudzysłowie; polskie litery w napisach są w porządku.",
        "`cena = 4.50` — float; Python wypisze go jako 4.5 (zera na końcu znikają).",
        "`ilosc = 3` — int, liczba całkowita.",
        "`dostepny = True` — bool; zawsze z wielkiej litery: True / False.",
        "`razem = cena * ilosc` — wynik mnożenia float × int to float (13.5).",
        "`print(nazwa, type(nazwa))` — wypisuje wartość i jej typ: `<class 'str'>`.",
        "`f\"Do zapłaty: {razem:.2f} zł\"` — f-string: w klamrach wartość zmiennej, `:.2f` = dwa miejsca po przecinku → 13.50.",
        "`10 // 4` → 2 pełne paczki, `10 % 4` → 2 sztuki reszty. Zmień 10 na 13 i przewidź wynik (3 i 1)."],
        "wynik": "Sześć linii: cztery wartości z typami, „Do zapłaty: 13.50 zł” i „Paczki po 4 szt.: 2 reszta: 2”."},
    jak_uruchomic=["Mentor → zadanie t1z1 → „Utwórz plik ćwiczenia” → przepisz przykład (nie kopiuj — ręka uczy się składni) → Ctrl+S → ▶ Uruchom.",
                   "Albo terminal Mentora w PRACA: `python zmienne.py`."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji: długopis kosztuje 2.30 zł, kupujesz 7 sztuk. (1) Ile wynosi razem (z f-stringiem :.2f)? (2) Jaki typ ma `7`? (3) Ile pełnych opakowań po 5 szt. i ile sztuk reszty? Czas: 15 minut.",
          "(1) 16.10 zł; (2) int; (3) 1 opakowanie, reszta 2.",
          ["razem = 2.30 * 7.", "Liczba bez kropki to int.", "Opakowania: 7 // 5; reszta: 7 % 5."],
          "2.30 × 7 = 16.1 → f\"{16.1:.2f}\" = 16.10; type(7) → int; 7 // 5 = 1, 7 % 5 = 2.",
          [kw("razem", "(1) Razem (zł)", 16.10), wy("typ", "(2) Typ 7", ["int", "float", "str", "bool"], "int"),
           li("opak", "(3) Pełne opakowania", 1), li("reszta", "(3) Reszta (szt.)", 2, bledy=[bl(1.4, "to wynik dzielenia / — reszta z dzielenia to operator %")])]),
        C("samodzielne",
          "Przewidź wynik (bez uruchamiania), potem sprawdź w Mentorze: (1) `7 / 2`; (2) `7 // 2`; (3) `\"2\" * 3`; (4) `int(\"12\") + 3`; (5) co da `\"5\" + 5` — wybierz: 10 / 55 / TypeError. Czas: 15 minut.",
          "(1) 3.5; (2) 3; (3) 222; (4) 15; (5) TypeError.",
          ["`/` zawsze daje float.", "`*` na napisie powtarza go.", "Napis + liczba — Python nie zgaduje, co miałeś na myśli."],
          "(1) 3.5; (2) 3; (3) \"222\"; (4) 15; (5) TypeError: can only concatenate str (not \"int\") to str.",
          [li("a", "(1) 7 / 2", 3.5), li("b", "(2) 7 // 2", 3, bledy=[bl(3.5, "to wynik / — // obcina część ułamkową")]), tx("c", "(3) \"2\" * 3", "222", bledy=[bl("6", "\"2\" to napis — * powtarza go 3 razy")]),
           li("d", "(4) int(\"12\") + 3", 15), wy("e", "(5) \"5\" + 5", ["10", "55", "TypeError"], "TypeError")]),
    ],
    typowe_bledy=[
        B("TypeError: can only concatenate str (not \"int\") to str", "Sklejanie napisu z liczbą: `\"Ilość: \" + 3`.", "Sprawdź typy: `type(...)` obu stron +.", "`\"Ilość: \" + str(3)` albo f-string `f\"Ilość: {3}\"`."),
        B("ValueError: invalid literal for int() with base 10: '4,5'", "Przecinek zamiast kropki albo tekst w int().", "Wypisz wartość przed zamianą: `print(repr(x))`.", "`float(x.replace(\",\", \".\"))` — albo wpisuj z kropką."),
        B("NameError: name 'Cena' is not defined", "Literówka lub wielkość liter w nazwie zmiennej.", "Porównaj nazwę w linii błędu z miejscem przypisania.", "Ujednolić nazwę: `cena` wszędzie małymi literami."),
    ],
    pulapki=["`=` to przypisanie, `==` porównanie (tydzień 1, warunki).", "Kwoty na float: 0.1 + 0.2 ≠ 0.3 dokładnie — wypisuj z :.2f, a w testach porównuj z tolerancją (pytest.approx)."],
    zadania=["Zapisz 5 zmiennych różnych typów o produkcie ze sklepu i wypisz je z type().", "Policz cenę 3 produktów razem z f-stringiem :.2f.", "Sprawdź w Mentorze, co dają 13 // 4 i 13 % 4."],
    pytania=[["Co robi znak = w Pythonie?", "Przypisuje wartość zmiennej (nie porównuje)."],
             ["Jaki typ ma wynik 6 / 3?", "float (2.0) — dzielenie / zawsze daje float."],
             ["Jak wstawić liczbę w tekst?", "f-string: f\"Cena: {cena:.2f} zł\" albo str(liczba)."]],
    podsumowanie="Tworzysz zmienne, rozpoznajesz 4 typy, liczysz operatorami (w tym // i %), zamieniasz typy i wypisujesz kwoty f-stringiem.",
    test=[T("type(4.5) zwraca:", ["int", "float", "str", "bool"], 1, "Liczba z kropką."),
          T("Wynik 9 % 4:", ["2.25", "2", "1", "0"], 2, "Reszta z dzielenia 9 przez 4."),
          T("Co da \"3\" + \"4\"?", ["7", "\"34\"", "TypeError", "12"], 1, "Napisy się sklejają."),
          T("f\"{2.5:.2f}\" daje:", ["2.5", "2.50", "3", "2,50"], 1, "Dwa miejsca po kropce.")],
    w_praktyce=["Testując formularz: wpisz liczbę z przecinkiem i z kropką — to klasyczne źródło błędów.", "W zgłoszeniu błędu podawaj typ: „pole przyjmuje tekst zamiast liczby”."],
    zrodla=[Z.PY_TUT_INTRO, Z.PY_STDTYPES, Z.PY_TUT_IO],
)

INPUT_PRINT = L(
    id="input_print", nazwa="print i input — rozmowa programu z użytkownikiem", tydzien=1,
    slowa=["print", "input", "sep", "end", "wczytywanie", "napis", "int(input())", "float(input())", "strip"],
    cel="Po tej lekcji wypisujesz dane czytelnie (print z sep i end, f-string) i wczytujesz je od użytkownika input(), zamieniając na liczby int()/float() — wiedząc, że input() zawsze zwraca napis.",
    po_co="Każdy program z formularzem przyjmuje tekst od człowieka. Tester sprawdza, co się dzieje, gdy człowiek wpisze coś innego niż oczekiwano.",
    wymagania=["Lekcja „Zmienne i typy”.", "W Mentorze dane dla input() wpisujesz w polu nad wynikiem — jedna linia = jedna odpowiedź."],
    wyjasnienie=(
        "## print — wypisywanie\n"
        "`print(\"a\", \"b\", 3)` wypisuje `a b 3` — argumenty rozdziela spacją. `sep=\";\"` zmienia separator, `end=\"\"` usuwa przejście do nowej linii. Pusty `print()` wstawia pustą linię.\n"
        "## input — wczytywanie\n"
        "`imie = input(\"Jak masz na imię? \")` — program wyświetla pytanie i czeka, aż użytkownik wpisze tekst i naciśnie Enter. **input() zawsze zwraca str**, nawet gdy wpiszesz 12.\n"
        "Liczbę trzeba zamienić: `ilosc = int(input(\"Ilość: \"))`, `cena = float(input(\"Cena: \"))`. Kolejność: najpierw input (napis), potem int (liczba).\n"
        "## Spacje i wielkość liter\n"
        "Użytkownicy dopisują spacje. `.strip()` usuwa je z początku i końca: `input().strip()`. `.lower()` zamienia na małe litery — przydatne przy porównaniach „TAK”/„tak”.\n"
        "## Program, który można przetestować\n"
        "Mentor uruchamia Twój program z danymi wpisanymi w polu nad wynikiem — każda linia to kolejna odpowiedź dla input(). Weryfikatory robią to samo automatycznie z wieloma zestawami danych, także błędnymi."),
    przyklad=kod("input_print", (
        "nazwa = \"Długopis niebieski\"\n"
        "cena = 2.3\n"
        "ilosc = 4\n"
        "print(\"Produkt:\", nazwa)\n"
        "print(\"Cena\", \"Ilość\", \"Razem\", sep=\" | \")\n"
        "print(cena, ilosc, cena * ilosc, sep=\" | \")\n"
        "print(\"Wczytuję\", end=\"\")\n"
        "print(\"...\", end=\"\")\n"
        "print(\" gotowe\")\n"
        "print(f\"{nazwa}: {ilosc} szt. × {cena:.2f} zł = {cena * ilosc:.2f} zł\")\n"), (
        "Produkt: Długopis niebieski\nCena | Ilość | Razem\n2.3 | 4 | 9.2\nWczytuję... gotowe\nDługopis niebieski: 4 szt. × 2.30 zł = 9.20 zł\n")),
    demonstracja={"tytul": "Tabelka z print i wersja z input()", "kroki": [
        "`print(\"Produkt:\", nazwa)` — dwa argumenty, spacja między nimi.",
        "`sep=\" | \"` — zamiast spacji wstawia „ | ” między argumentami: powstaje tabelka.",
        "`end=\"\"` — print nie przechodzi do nowej linii; trzy printy dają jedną linię „Wczytuję... gotowe”.",
        "Ostatni print: f-string z trzema wstawkami; `{cena:.2f}` → 2.30.",
        "Wersja interaktywna: zamień linie 2–3 na `cena = float(input(\"Cena: \"))` i `ilosc = int(input(\"Ilość: \"))`. W Mentorze w polu danych wpisz dwie linie: `2.3` i `4`.",
        "Wpisz `cztery` zamiast 4 → ValueError. To jest dokładnie to, co tester sprawdza: co robi program przy złych danych? (Obsługę błędów poznasz w tygodniu 3.)"],
        "wynik": "Pięć linii; ostatnia: „Długopis niebieski: 4 szt. × 2.30 zł = 9.20 zł”."},
    jak_uruchomic=["Zapisz jako paragon.py → ▶ Uruchom.", "Wersja z input(): pole „Dane dla input()” nad wynikiem → wpisz 2.3 (Enter) 4 → ▶ Uruchom."],
    cwiczenia=[
        C("prowadzone",
          "Program: `a = input(\"Pierwsza: \")`, `b = input(\"Druga: \")`, `print(a + b)`. Użytkownik wpisuje 12 i 5. (1) Co wypisze program? (2) Jak poprawić pierwszą linię, żeby dodawał liczby (wpisz linię)? (3) Co wtedy wypisze? Czas: 15 minut.",
          "(1) 125; (2) a = int(input(\"Pierwsza: \")) (i tak samo b); (3) 17.",
          ["input() zwraca napis.", "Napis + napis = sklejenie.", "Zamień wynik input() na liczbę int(...)."],
          "(1) \"12\" + \"5\" = \"125\"; (2) `a = int(input(\"Pierwsza: \"))` oraz `b = int(input(\"Druga: \"))`; (3) 12 + 5 = 17.",
          [tx("w1", "(1) Wynik bez poprawki", "125", bledy=[bl("17", "input() zwraca napisy — \"12\" + \"5\" się skleja")]), tx("linia", "(2) Poprawiona linia", "a = int(input(\"Pierwsza: \"))"),
           li("w3", "(3) Wynik po poprawce", 17)]),
        C("samodzielne",
          "Napisz w głowie (potem w Mentorze) program: pyta o nazwę produktu i ilość, wypisuje „Dodano: <ilość> × <nazwa>”. Użytkownik wpisuje „  zeszyt A5 ” (ze spacjami) i 3. "
          "(1) Jak wczytać nazwę bez spacji na brzegach (wpisz wyrażenie)? (2) Co wypisze program? Czas: 15 minut.",
          "(1) input(\"Produkt: \").strip(); (2) Dodano: 3 × zeszyt A5.",
          ["Metoda usuwająca spacje z brzegów napisu.", "Ilość zamień na int, nazwę zostaw jako str.", "f\"Dodano: {ilosc} × {nazwa}\"."],
          "`nazwa = input(\"Produkt: \").strip()`, `ilosc = int(input(\"Ilość: \"))`, `print(f\"Dodano: {ilosc} × {nazwa}\")` → „Dodano: 3 × zeszyt A5”.",
          [tx("strip", "(1) Wczytanie nazwy", "input(\"Produkt: \").strip()", zawiera=["input", "strip()"]), tx("wynik", "(2) Wynik", "Dodano: 3 × zeszyt A5")]),
    ],
    typowe_bledy=[
        B("TypeError: unsupported operand type(s) for *: 'float' and 'str'", "Liczba z input() nie została zamieniona: `cena * input()`.", "`print(type(ilosc))`.", "`ilosc = int(input(...))`."),
        B("EOFError: EOF when reading a line", "Program czeka na dane, a nikt ich nie podał (pole danych w Mentorze puste).", "Ile razy wywołujesz input()? Tyle linii danych potrzeba.", "Wpisz dane w polu nad wynikiem — po jednej linii na każde input()."),
    ],
    pulapki=["int(input()) przy wpisie „3.5” → ValueError; dla kwot używaj float().", "Komunikat w input() bez spacji na końcu: „Ilość:3” — dodaj spację po dwukropku."],
    zadania=["Program pyta o cenę i ilość, wypisuje razem z :.2f.", "Wypisz tabelkę 3 produktów z sep=\" | \".", "Sprawdź, co robi program przy wpisie „abc” — zapisz komunikat błędu."],
    pytania=[["Jakiego typu jest wynik input()?", "Zawsze str."], ["Co robi end=\"\" w print?", "Nie przechodzi do nowej linii."], ["Po co .strip()?", "Usuwa spacje z początku i końca napisu."]],
    podsumowanie="Wypisujesz czytelnie (sep, end, f-string), wczytujesz dane input() i zamieniasz je na liczby; wiesz, co dzieje się przy złym wpisie.",
    test=[T("x = input() — użytkownik wpisał 7. type(x)?", ["int", "str", "float", "zależy"], 1, "input() zawsze daje napis."),
          T("print(1, 2, sep=\"-\") wypisze:", ["1 2", "1-2", "12", "-1-2-"], 1, "sep zastępuje spację."),
          T("Brak danych dla input() w Mentorze kończy się:", ["ValueError", "EOFError", "TypeError", "niczym"], 1, "Koniec danych wejściowych."),
          T("\"  abc \".strip() to:", ["\"abc\"", "\"  abc\"", "\"abc \"", "\"ABC\""], 0, "Usuwa spacje z obu brzegów.")],
    w_praktyce=["Testując pole liczbowe: liczba, liczba z przecinkiem, tekst, puste pole, spacje — 5 przypadków na start.", "Komunikaty w input() piszesz tak, by człowiek wiedział, co wpisać (jednostka, format)."],
    zrodla=[Z.PY_TUT_IO, Z.PY_TUT_INTRO],
)

WARUNKI = L(
    id="warunki", nazwa="Instrukcje warunkowe if / elif / else", tydzien=1,
    slowa=["if", "elif", "else", "warunek", "porównanie", "==", "!=", "and", "or", "not", "wcięcie", "próg"],
    cel="Po tej lekcji piszesz decyzje if/elif/else z porównaniami (== != < <= > >=) i łączysz warunki and/or/not, dbając o wcięcia i kolejność progów.",
    po_co="Reguły biznesowe (rabaty, progi, walidacja) to warunki — a tester sprawdza właśnie ich granice: co dla 99 zł, 100 zł i 100,01 zł?",
    wymagania=["Lekcje „Zmienne” i „print i input”."],
    wyjasnienie=(
        "## if — jeśli\n"
        "```\nif razem >= 100:\n    print(\"Darmowa dostawa\")\n```\n"
        "Dwukropek kończy warunek, a wcięcie (4 spacje) pokazuje, co należy do if. Bez wcięcia: IndentationError.\n"
        "## Porównania\n"
        "`==` równe, `!=` różne, `<` `<=` `>` `>=`. Wynik porównania to bool: `5 > 3` → True. Napisy porównujesz dokładnie: `\"Tak\" == \"tak\"` → False (użyj `.lower()`).\n"
        "## elif i else\n"
        "`elif` = „w przeciwnym razie, jeśli…”, `else` = „we wszystkich pozostałych przypadkach”. Python sprawdza warunki **od góry** i wykonuje **tylko pierwszy prawdziwy**. Dlatego progi układasz od największego:\n"
        "```\nif razem >= 300:\n    rabat = 10\nelif razem >= 100:\n    rabat = 5\nelse:\n    rabat = 0\n```\n"
        "Gdybyś zaczął od `>= 100`, kwota 350 dostałaby 5% — klasyczny błąd kolejności.\n"
        "## and, or, not\n"
        "`and` — oba warunki prawdziwe; `or` — co najmniej jeden; `not` — odwrócenie. `if ilosc > 0 and ilosc <= 50:` można zapisać krócej `if 0 < ilosc <= 50:`.\n"
        "## Wartości brzegowe\n"
        "Dla reguły „od 100 zł darmowa dostawa” testujesz 99.99, 100 i 100.01. To technika z sylabusa ISTQB (analiza wartości brzegowych) — wrócisz do niej w tygodniu 7."),
    przyklad=kod("warunki", (
        "def koszt_dostawy(razem):\n"
        "    if razem >= 100:\n"
        "        return 0\n"
        "    elif razem >= 50:\n"
        "        return 9.99\n"
        "    else:\n"
        "        return 14.99\n\n\n"
        "for kwota in [49.99, 50, 99.99, 100, 250]:\n"
        "    print(kwota, \"->\", koszt_dostawy(kwota))\n"), "49.99 -> 14.99\n50 -> 9.99\n99.99 -> 9.99\n100 -> 0\n250 -> 0\n"),
    demonstracja={"tytul": "Koszt dostawy w sklepie — trzy progi i ich granice", "kroki": [
        "`def koszt_dostawy(razem):` — zamknięcie reguły w funkcji (funkcje poznasz w tygodniu 3; tu: „przepis z nazwą, który dostaje kwotę i zwraca koszt”).",
        "`if razem >= 100: return 0` — najwyższy próg pierwszy; `return` oddaje wynik i kończy funkcję.",
        "`elif razem >= 50: return 9.99` — sprawdzany tylko, gdy pierwszy warunek był fałszywy, czyli dla kwot poniżej 100.",
        "`else: return 14.99` — wszystko poniżej 50.",
        "Pętla `for kwota in [...]` sprawdza 5 kwot — w tym granice 50 i 100 oraz wartości tuż pod nimi (49.99, 99.99).",
        "Zamień kolejność warunków (najpierw `>= 50`) i uruchom — 100 i 250 dostaną 9.99. Tak wygląda błąd, który łapie test wartości brzegowych."],
        "wynik": "49.99 → 14.99, 50 → 9.99, 99.99 → 9.99, 100 → 0, 250 → 0."},
    jak_uruchomic=["Zapisz jako dostawa.py → ▶ Uruchom.", "Eksperyment: zmień kolejność warunków, uruchom, porównaj wynik i przywróć poprawną wersję."],
    cwiczenia=[
        C("prowadzone",
          "Reguła rabatu: od 300 zł — 10%, od 100 zł — 5%, poniżej — 0%. Jaki rabat (w %) dostaną kwoty: (1) 99.99, (2) 100, (3) 299.99, (4) 300? Czas: 10 minut.",
          "(1) 0; (2) 5; (3) 5; (4) 10.",
          ["„Od 100” znaczy razem >= 100.", "Sprawdzaj progi od największego.", "300 spełnia już warunek najwyższego progu."],
          "99.99 < 100 → 0%; 100 ≥ 100 → 5%; 299.99 < 300 → 5%; 300 ≥ 300 → 10%.",
          [li("r1", "(1) 99.99 zł", 0), li("r2", "(2) 100 zł", 5, bledy=[bl(0, "„od 100 zł” obejmuje 100 — warunek >=")]), li("r3", "(3) 299.99 zł", 5), li("r4", "(4) 300 zł", 10)]),
        C("samodzielne",
          "Kolega napisał: `if razem >= 100: rabat = 5` / `elif razem >= 300: rabat = 10` / `else: rabat = 0`. (1) Jaki rabat dostanie 500 zł? (2) Czy kiedykolwiek ktoś dostanie 10%? (3) Ile minimum przypadków testowych (kwot) sprawdza granice obu progów, jeśli dla każdej granicy bierzesz wartość tuż pod i dokładnie na granicy? Czas: 15 minut.",
          "(1) 5; (2) nie; (3) 4 (99.99, 100, 299.99, 300).",
          ["Python wykonuje tylko pierwszy prawdziwy warunek.", "500 >= 100 jest prawdziwe — dalej nie sprawdza.", "Dwie granice × dwie wartości."],
          "(1) 5% — pierwszy warunek prawdziwy, elif pominięty; (2) nie — elif >= 300 jest nieosiągalny; (3) 4 kwoty: 99.99, 100, 299.99, 300.",
          [li("a", "(1) Rabat dla 500 zł (%)", 5, bledy=[bl(10, "Python zatrzymuje się na PIERWSZYM prawdziwym warunku")]), wy("b", "(2) Czy ktoś dostanie 10%?", ["tak", "nie"], "nie"), li("c", "(3) Liczba kwot", 4)]),
    ],
    typowe_bledy=[
        B("IndentationError: expected an indented block after 'if' statement", "Brak wcięcia po dwukropku.", "Linia po if musi zaczynać się 4 spacjami.", "Wcięcie 4 spacje (Tab w edytorze Mentora wstawia 4 spacje)."),
        B("SyntaxError: invalid syntax przy `if x = 5:`", "Przypisanie = zamiast porównania ==.", "Szukaj pojedynczego = w warunku.", "`if x == 5:`."),
        B("Zła kategoria dla dużych kwot (bez komunikatu błędu)", "Progi w złej kolejności.", "Przetestuj wartości brzegowe każdego progu.", "Ułóż warunki od największego progu."),
    ],
    pulapki=["Porównywanie float z == (0.1 + 0.2 == 0.3 → False) — dla kwot używaj progów >= lub zaokrąglenia.", "else łapie WSZYSTKO, także wartości ujemne — sprawdzaj dane wejściowe osobnym if."],
    zadania=["Napisz regułę rabatu z 3 progami i sprawdź 4 wartości brzegowe.", "Program pyta „Czy masz kartę stałego klienta? (tak/nie)” i działa dla „TAK”, „ tak ”.", "Zapisz w notatki.md, dlaczego kolejność elif ma znaczenie."],
    pytania=[["Ile gałęzi if/elif/else się wykona?", "Dokładnie jedna — pierwsza z prawdziwym warunkiem (albo else)."],
             ["Dlaczego progi układa się od największego?", "Bo większa kwota spełnia też niższe progi — wygrałby niższy."],
             ["Jakie wartości testujesz dla „od 100 zł”?", "99.99, 100, 100.01 — wartości brzegowe."]],
    podsumowanie="Piszesz decyzje if/elif/else, łączysz warunki and/or/not, pilnujesz wcięć i kolejności progów oraz testujesz wartości brzegowe.",
    test=[T("Co wypisze: x = 100; if x > 100: print(\"A\") elif x >= 100: print(\"B\") else: print(\"C\")", ["A", "B", "C", "A i B"], 1, "100 > 100 fałsz, 100 >= 100 prawda."),
          T("Operator „różne od”:", ["<>", "!=", "=!", "not="], 1, "!= ."),
          T("True and False daje:", ["True", "False", "None", "błąd"], 1, "and wymaga obu prawd."),
          T("Granice reguły „od 50 zł” do testu:", ["0 i 1000", "49.99 i 50", "tylko 50", "100"], 1, "Tuż pod granicą i na granicy.")],
    w_praktyce=["Każdy próg w wymaganiach = co najmniej 2 przypadki testowe (pod i na granicy).", "W bug raporcie podajesz dokładną kwotę, dla której reguła działa źle."],
    zrodla=[Z.PY_TUT_CTRL, Z.SJSI_CTFL_PL, Z.ISTQB_SLOWNIK],
)

# =========================================================================== TYDZIEŃ 2
PETLE = L(
    id="petle", nazwa="Pętle for i while, range, break i continue", tydzien=2,
    slowa=["pętla", "for", "while", "range", "break", "continue", "licznik", "akumulator", "nieskończona pętla", "zagnieżdżona pętla"],
    cel="Po tej lekcji powtarzasz czynności pętlą for (po liście i range) i while (dopóki warunek), liczysz sumy i liczniki, przerywasz pętlę break i pomijasz obrót continue — bez pętli nieskończonej.",
    po_co="Testy przechodzą po listach danych (dziesiątki kwot, loginów, produktów). Pętla zamienia 50 linii kopiuj-wklej w 3.",
    wymagania=["Lekcja „Warunki”."],
    wyjasnienie=(
        "## for — dla każdego elementu\n"
        "```\nfor cena in [4.5, 2.3, 7.5]:\n    print(cena)\n```\n"
        "Zmienna `cena` przyjmuje po kolei każdą wartość z listy; wcięty blok wykonuje się raz dla każdej. Liczba obrotów jest znana z góry.\n"
        "## range — liczby po kolei\n"
        "`range(5)` → 0, 1, 2, 3, 4 (bez 5!). `range(1, 11)` → 1…10. `range(0, 20, 5)` → 0, 5, 10, 15 (krok 5).\n"
        "## Akumulator i licznik\n"
        "`suma = 0` przed pętlą, `suma = suma + x` (krócej `suma += x`) w pętli. Licznik: `ile = 0`, `ile += 1` gdy warunek spełniony. Zmienną startową ustawiasz ZAWSZE przed pętlą.\n"
        "## while — dopóki\n"
        "`while warunek:` powtarza blok, dopóki warunek jest prawdziwy. Coś w środku musi go w końcu zmienić — inaczej pętla nieskończona (zatrzymasz ją przyciskiem ■ w Mentorze albo Ctrl+C w terminalu).\n"
        "## break i continue\n"
        "`break` kończy pętlę natychmiast (np. użytkownik wpisał 0). `continue` pomija resztę bloku i przechodzi do następnego obrotu (np. pomiń produkty z ilością 0).\n"
        "## Pętla w pętli\n"
        "Zagnieżdżona pętla wykonuje wewnętrzną w całości dla każdego obrotu zewnętrznej: 10 × 10 = 100 obrotów (tabliczka mnożenia)."),
    przyklad=kod("petle", (
        "ceny = [4.5, 2.3, 0, 7.5, 24.99]\n"
        "suma = 0\n"
        "ile_drogich = 0\n"
        "for cena in ceny:\n"
        "    if cena == 0:\n"
        "        continue\n"
        "    suma += cena\n"
        "    if cena > 5:\n"
        "        ile_drogich += 1\n"
        "print(f\"Suma: {suma:.2f}, droższe niż 5 zł: {ile_drogich}\")\n\n"
        "for n in range(1, 4):\n"
        "    print(n, \"x 7 =\", n * 7)\n\n"
        "stan = 10\n"
        "while stan > 0:\n"
        "    stan -= 4\n"
        "    print(\"Zostało:\", stan)\n"), "Suma: 39.29, droższe niż 5 zł: 2\n1 x 7 = 7\n2 x 7 = 14\n3 x 7 = 21\nZostało: 6\nZostało: 2\nZostało: -2\n"),
    demonstracja={"tytul": "Suma koszyka, tabliczka i wydawanie z magazynu", "kroki": [
        "`suma = 0` i `ile_drogich = 0` — akumulator i licznik ustawione PRZED pętlą.",
        "`for cena in ceny:` — 5 obrotów, `cena` to kolejno 4.5, 2.3, 0, 7.5, 24.99.",
        "`if cena == 0: continue` — pozycja z ceną 0 jest pomijana (nie dodaje się i nie liczy).",
        "`suma += cena` — dopisanie do sumy; `if cena > 5: ile_drogich += 1` — 7.5 i 24.99.",
        "`for n in range(1, 4)` — n = 1, 2, 3 (4 nie wchodzi).",
        "`while stan > 0:` — dopóki jest towar: odejmij 4 i wypisz. 10 → 6 → 2 → -2 i koniec (warunek fałszywy).",
        "Zwróć uwagę: stan zszedł do -2 — w prawdziwym magazynie to błąd. W zadaniu z menu sprawdzisz warunek PRZED wydaniem."],
        "wynik": "„Suma: 39.29, droższe niż 5 zł: 2”, trzy linie tabliczki 7 i trzy linie „Zostało: 6 / 2 / -2”."},
    jak_uruchomic=["Zapisz jako petle.py → ▶ Uruchom.", "Pętla się nie kończy? Przycisk ■ Zatrzymaj w Mentorze (w terminalu Ctrl+C)."],
    cwiczenia=[
        C("prowadzone",
          "Lista ilości w magazynie: [120, 0, 80, 0, 35]. Na wzór demonstracji policz pętlą for: (1) sumę sztuk, (2) ile produktów ma ilość 0, (3) ile obrotów wykona `for i in range(2, 10, 3)`. Czas: 15 minut.",
          "(1) 235; (2) 2; (3) 3 obroty (2, 5, 8).",
          ["Akumulator suma = 0 przed pętlą.", "Licznik zer: if ilosc == 0: zera += 1.", "range(start, stop, krok) — stop nie wchodzi."],
          "120 + 0 + 80 + 0 + 35 = 235; zera: 2; range(2, 10, 3) → 2, 5, 8 = 3 obroty.",
          [li("suma", "(1) Suma sztuk", 235), li("zera", "(2) Produkty z ilością 0", 2), li("obroty", "(3) Obroty range(2, 10, 3)", 3, bledy=[bl(4, "10 nie wchodzi do range — po 8 następna byłaby 11")])]),
        C("samodzielne",
          "Pętla `x = 5` / `while x != 0:` / `    x -= 2` / `    print(x)`. (1) Czy się zakończy? (2) Jak minimalnie poprawić warunek, żeby kończyła się dla każdej dodatniej wartości startowej (wpisz nowy warunek)? (3) Co wypisze poprawiona pętla dla x = 5? Czas: 15 minut.",
          "(1) nie — x: 3, 1, -1, -3… nigdy nie równa się 0; (2) while x > 0:; (3) 3, 1, -1.",
          ["Wypisz kolejne wartości x na kartce.", "Warunek != 0 omija zero przy kroku 2.", "Porównanie > działa dla każdej liczby."],
          "(1) nie — pętla nieskończona; (2) `while x > 0:`; (3) wypisze 3, 1, -1 (po -1 warunek fałszywy).",
          [wy("a", "(1) Zakończy się?", ["tak", "nie"], "nie"), tx("b", "(2) Nowy warunek", "while x > 0:", zawiera=["x > 0"]), tx("c", "(3) Wypisane wartości", "3, 1, -1")]),
    ],
    typowe_bledy=[
        B("Program „wisi”, brak wyniku", "Pętla while bez zmiany warunku.", "Dodaj print(x) w pętli — czy x się zmienia?", "Zmieniaj zmienną warunku w środku pętli albo użyj break."),
        B("Suma za duża przy drugim uruchomieniu funkcji", "Akumulator ustawiony poza funkcją/pętlą raz na zawsze.", "Gdzie jest `suma = 0`?", "Zeruj akumulator tuż przed pętlą, w tym samym bloku."),
        B("Brakuje ostatniej liczby (np. 10 w tabliczce)", "range(1, 10) kończy się na 9.", "Wypisz list(range(1, 10)).", "range(1, 11)."),
    ],
    pulapki=["Zmiana listy w trakcie pętli po niej (usuwanie elementów) — pomija elementy; twórz nową listę.", "while True bez break = pętla nieskończona."],
    zadania=["Tabliczka mnożenia 1–10 pętlą zagnieżdżoną.", "Suma i średnia cen z listy (pomiń zera continue).", "Pętla while pytająca o liczby do wpisania 0 (break)."],
    pytania=[["Kiedy for, a kiedy while?", "for — znana kolekcja/liczba obrotów; while — dopóki warunek (np. do wpisania 0)."],
             ["Co robi continue?", "Pomija resztę bloku i przechodzi do następnego obrotu."],
             ["Ile liczb daje range(3, 8)?", "5: 3, 4, 5, 6, 7."]],
    podsumowanie="Używasz for z listą i range, while z warunkiem, akumulatorów i liczników oraz break/continue; rozpoznajesz i naprawiasz pętlę nieskończoną.",
    test=[T("list(range(4)) to:", ["[1, 2, 3, 4]", "[0, 1, 2, 3]", "[0, 1, 2, 3, 4]", "[4]"], 1, "Od 0, bez 4."),
          T("break w pętli:", ["pomija obrót", "kończy pętlę", "restartuje pętlę", "nic nie robi"], 1, "Natychmiastowe wyjście."),
          T("Gdzie ustawiasz suma = 0?", ["w pętli", "przed pętlą", "po pętli", "nigdzie"], 1, "Inaczej zerujesz co obrót."),
          T("Zagnieżdżone pętle 3 × 4 wykonają wewnętrzny blok:", ["7 razy", "12 razy", "3 razy", "4 razy"], 1, "3 × 4.")],
    w_praktyce=["Dane testowe trzymasz w liście i przechodzisz pętlą — w tygodniu 7 zrobi to za Ciebie parametrize.", "Każdą pętlę while sprawdź: co ją zakończy?"],
    zrodla=[Z.PY_TUT_CTRL, Z.PY_TUT_INTRO],
)

LISTY = L(
    id="listy", nazwa="Listy: indeksy, append, remove, sortowanie, len, sum, max", tydzien=2,
    slowa=["lista", "indeks", "append", "remove", "pop", "insert", "len", "sum", "max", "min", "sort", "sorted", "in", "wycinek"],
    cel="Po tej lekcji tworzysz listy, czytasz elementy po indeksie (także ujemnym i wycinkiem), dodajesz i usuwasz elementy, sortujesz i liczysz len/sum/max/min oraz sprawdzasz `in`.",
    po_co="Koszyk, lista zamówień, wyniki testów — wszystko to listy. Tester sprawdza też skrajności: pusta lista, jeden element, duplikaty.",
    wymagania=["Lekcja „Pętle”."],
    wyjasnienie=(
        "## Lista\n"
        "`koszyk = [\"zeszyt\", \"długopis\", \"klej\"]` — uporządkowany ciąg elementów w nawiasach kwadratowych. Elementy mogą być dowolnego typu.\n"
        "## Indeksy\n"
        "Numeracja od **0**: `koszyk[0]` → \"zeszyt\", `koszyk[2]` → \"klej\". Ujemne od końca: `koszyk[-1]` → ostatni. Indeks poza listą → IndexError.\n"
        "Wycinek: `koszyk[0:2]` → elementy 0 i 1 (bez 2). `koszyk[:2]` — od początku, `koszyk[1:]` — do końca.\n"
        "## Zmiany\n"
        "| operacja | co robi |\n|---|---|\n"
        "| `koszyk.append(\"gumka\")` | dodaje na koniec |\n"
        "| `koszyk.insert(0, \"blok\")` | wstawia na pozycję 0 |\n"
        "| `koszyk.remove(\"klej\")` | usuwa pierwsze wystąpienie wartości (brak → ValueError) |\n"
        "| `koszyk.pop()` | usuwa i zwraca ostatni (`pop(0)` — pierwszy) |\n"
        "| `koszyk[1] = \"ołówek\"` | podmienia element |\n"
        "## Liczenie i sortowanie\n"
        "`len(lista)` — liczba elementów; `sum`, `max`, `min` — dla liczb. `lista.sort()` sortuje **tę listę** (zwraca None!), `sorted(lista)` zwraca **nową** posortowaną. `reverse=True` — malejąco.\n"
        "## Sprawdzanie\n"
        "`\"klej\" in koszyk` → True/False. Pusta lista `[]` ma len 0 — `max([])` da ValueError, więc sprawdzaj `if lista:` przed max/średnią."),
    przyklad=kod("listy", (
        "koszyk = [\"zeszyt\", \"długopis\", \"klej\"]\n"
        "ceny = [4.5, 2.3, 3.4]\n"
        "koszyk.append(\"gumka\")\n"
        "ceny.append(1.5)\n"
        "print(koszyk[0], koszyk[-1], len(koszyk))\n"
        "print(koszyk[1:3])\n"
        "koszyk.remove(\"klej\")\n"
        "print(koszyk, \"klej\" in koszyk)\n"
        "print(\"Suma:\", sum(ceny), \"max:\", max(ceny), \"min:\", min(ceny))\n"
        "print(sorted(ceny), sorted(ceny, reverse=True)[0])\n"
        "print(f\"Średnia: {sum(ceny) / len(ceny):.2f}\")\n"), (
        "zeszyt gumka 4\n['długopis', 'klej']\n['zeszyt', 'długopis', 'gumka'] False\nSuma: 11.7 max: 4.5 min: 1.5\n[1.5, 2.3, 3.4, 4.5] 4.5\nŚrednia: 2.92\n")),
    demonstracja={"tytul": "Koszyk w sklepie: dodaj, usuń, policz", "kroki": [
        "`koszyk = [...]`, `ceny = [...]` — dwie listy; pozycja 0 w obu dotyczy tego samego produktu.",
        "`append` — gumka i jej cena trafiają na koniec obu list.",
        "`koszyk[0]` → zeszyt, `koszyk[-1]` → gumka, `len` → 4.",
        "`koszyk[1:3]` → elementy 1 i 2: długopis, klej.",
        "`remove(\"klej\")` — usunięcie po wartości; `\"klej\" in koszyk` → False.",
        "`sum`, `max`, `min` na liście liczb. Uwaga: lista ceny wciąż ma 4 pozycje — usunęliśmy klej tylko z koszyka! To błąd danych równoległych list; w tygodniu 3 zastąpi je słownik.",
        "`sorted(ceny)` nowa lista rosnąco; `sorted(..., reverse=True)[0]` — największa.",
        "Średnia = suma / liczba elementów, z :.2f."],
        "wynik": "Sześć linii — od „zeszyt gumka 4” do „Średnia: 2.92”."},
    jak_uruchomic=["Zapisz jako koszyk.py → ▶ Uruchom.", "Dopisz `print(max([]))` i zobacz ValueError — potem usuń tę linię."],
    cwiczenia=[
        C("prowadzone",
          "Lista `stany = [120, 80, 300, 0, 45]`. Podaj: (1) `stany[2]`, (2) `stany[-2]`, (3) `stany[1:4]`, (4) `len(stany)` po `stany.append(10)`, (5) `max(stany)`. Czas: 15 minut.",
          "(1) 300; (2) 0; (3) [80, 300, 0]; (4) 6; (5) 300.",
          ["Indeksy od 0.", "-1 to ostatni, -2 przedostatni.", "Wycinek [1:4] bierze indeksy 1, 2, 3."],
          "(1) 300; (2) 0; (3) [80, 300, 0]; (4) 6; (5) 300.",
          [li("a", "(1) stany[2]", 300, bledy=[bl(80, "indeksy liczysz od 0 — stany[2] to trzeci element")]), li("b", "(2) stany[-2]", 0), tx("c", "(3) stany[1:4]", "[80, 300, 0]"),
           li("d", "(4) len po append", 6), li("e", "(5) max", 300)]),
        C("samodzielne",
          "Kod: `ceny = [7.5, 2.3, 4.5]` / `wynik = ceny.sort()` / `print(wynik)`. (1) Co wypisze? (2) Jak dostać nową posortowaną listę w zmiennej wynik (wpisz wyrażenie)? (3) Co zwróci `sum([])` i czy `max([])` zadziała (tak/nie)? Czas: 15 minut.",
          "(1) None; (2) sorted(ceny); (3) 0; nie — ValueError.",
          ["Metoda sort zmienia listę w miejscu.", "Funkcja wbudowana zwraca nową listę.", "Suma pustej listy to 0, a maksimum nie istnieje."],
          "(1) None — sort() zwraca None; (2) `wynik = sorted(ceny)`; (3) sum([]) = 0, max([]) → ValueError: max() iterable argument is empty.",
          [tx("a", "(1) Wypisze", "None", bledy=[bl("[2.3, 4.5, 7.5]", "sort() sortuje listę w miejscu i zwraca None")]), tx("b", "(2) Wyrażenie", "sorted(ceny)"),
           li("c", "(3) sum([])", 0), wy("d", "(3) max([]) zadziała?", ["tak", "nie"], "nie")]),
    ],
    typowe_bledy=[
        B("IndexError: list index out of range", "Indeks ≥ len(lista) (np. lista[3] dla 3 elementów).", "Wypisz len(lista) i indeks.", "Ostatni element to lista[-1] albo lista[len(lista) - 1]."),
        B("ValueError: list.remove(x): x not in list", "Usuwasz wartość, której nie ma.", "`print(x in lista)`.", "`if x in lista: lista.remove(x)`."),
        B("TypeError: 'NoneType' object is not subscriptable", "Wynik lista.sort() (None) użyty jak lista.", "Gdzie przypisujesz wynik sort()?", "sorted(lista) albo samo lista.sort() bez przypisania."),
    ],
    pulapki=["Dwie równoległe listy (nazwy i ceny) łatwo rozjechać — w tygodniu 3 słownik/lista słowników.", "lista2 = lista1 nie kopiuje — obie nazwy wskazują tę samą listę; kopia: lista1.copy()."],
    zadania=["Lista zakupów: dodaj 5 produktów, usuń jeden, wypisz z numerami od 1.", "Średnia i maksimum cen z obsługą pustej listy.", "Sprawdź `in` dla produktu, którego nie ma."],
    pytania=[["Jaki indeks ma pierwszy element?", "0."], ["Różnica sort() i sorted()?", "sort() zmienia listę i zwraca None; sorted() zwraca nową."], ["Jak sprawdzić, czy lista jest pusta?", "if not lista: albo len(lista) == 0."]],
    podsumowanie="Tworzysz i zmieniasz listy, indeksujesz (także -1 i wycinki), sortujesz, liczysz len/sum/max/min i pilnujesz pustej listy.",
    test=[T("[10, 20, 30][-1] to:", ["10", "20", "30", "błąd"], 2, "-1 = ostatni."),
          T("Co zwraca lista.sort()?", ["posortowaną listę", "None", "True", "długość"], 1, "Sortuje w miejscu."),
          T("len([]) to:", ["0", "1", "None", "błąd"], 0, "Pusta lista."),
          T("[1, 2, 3, 4][1:3] to:", ["[1, 2]", "[2, 3]", "[2, 3, 4]", "[1, 2, 3]"], 1, "Indeksy 1 i 2.")],
    w_praktyce=["Test każdej funkcji na liście: pusta, jeden element, kilka, duplikaty.", "W raporcie błędu podaj dokładne dane wejściowe (całą listę)."],
    zrodla=[Z.PY_TUT_DS, Z.PY_TUT_INTRO, Z.PY_STDTYPES],
)

NAPISY = L(
    id="napisy", nazwa="Napisy i ich metody: upper, lower, strip, split, replace, len, wycinki", tydzien=2,
    slowa=["napis", "str", "upper", "lower", "strip", "split", "join", "replace", "find", "startswith", "len", "wycinek", "[::-1]", "count"],
    cel="Po tej lekcji przetwarzasz tekst metodami napisów (upper, lower, strip, split, join, replace, count, startswith), liczysz znaki i słowa, odwracasz napis wycinkiem i wiesz, że metody zwracają NOWY napis.",
    po_co="Dane od użytkowników to tekst z literówkami i spacjami; wyszukiwarka sklepu, walidacja e-maila i porównania w testach opierają się na tych metodach.",
    wymagania=["Lekcje „Listy” i „Pętle”."],
    wyjasnienie=(
        "## Napis to ciąg znaków\n"
        "Napis indeksujesz jak listę: `\"Zeszyt\"[0]` → \"Z\", `[-1]` → \"t\", `[0:3]` → \"Zes\". `len(\"Zeszyt\")` → 6. `[::-1]` odwraca napis.\n"
        "## Napisy są niezmienne\n"
        "`nazwa.upper()` NIE zmienia `nazwa` — zwraca nowy napis. Zapisz wynik: `nazwa = nazwa.upper()` albo od razu wypisz.\n"
        "## Najważniejsze metody\n"
        "| metoda | przykład | wynik |\n|---|---|---|\n"
        "| `upper()` / `lower()` | `\"Klej\".upper()` | \"KLEJ\" |\n"
        "| `strip()` | `\"  klej \".strip()` | \"klej\" |\n"
        "| `split()` | `\"zeszyt długopis klej\".split()` | ['zeszyt', 'długopis', 'klej'] |\n"
        "| `split(\";\")` | `\"a;b\".split(\";\")` | ['a', 'b'] |\n"
        "| `\", \".join(lista)` | `\", \".join([\"a\", \"b\"])` | \"a, b\" |\n"
        "| `replace(stare, nowe)` | `\"4,50\".replace(\",\", \".\")` | \"4.50\" |\n"
        "| `count(x)` | `\"banan\".count(\"a\")` | 2 |\n"
        "| `startswith(x)` | `\"PL123\".startswith(\"PL\")` | True |\n"
        "| `find(x)` | `\"a@b.pl\".find(\"@\")` | 1 (brak → -1) |\n"
        "## Wyszukiwanie bez względu na wielkość liter\n"
        "`fraza.lower() in nazwa.lower()` — „DŁUGOPIS” znajdzie „Długopis niebieski”. Brak `.lower()` w wyszukiwarce to częsty błąd, który zgłasza tester (sklep testowy w tygodniu 8 ma taki celowo).\n"
        "## Liczenie samogłosek\n"
        "Pętla po napisie: `for znak in tekst.lower(): if znak in \"aąeęioóuy\": ile += 1`."),
    przyklad=kod("napisy", (
        "zdanie = \"  Ala ma kota i psa  \"\n"
        "czyste = zdanie.strip()\n"
        "print(czyste.upper())\n"
        "print(czyste[::-1])\n"
        "print(len(czyste), \"znaków\")\n"
        "slowa = czyste.split()\n"
        "print(len(slowa), \"słów:\", \", \".join(slowa))\n"
        "samogloski = 0\n"
        "for znak in czyste.lower():\n"
        "    if znak in \"aąeęioóuy\":\n"
        "        samogloski += 1\n"
        "print(\"Samogłoski:\", samogloski)\n"
        "najdluzsze = max(slowa, key=len)\n"
        "print(\"Najdłuższe:\", najdluzsze)\n"
        "print(\"4,50 zł\".replace(\",\", \".\"), \"Długopis\".lower().startswith(\"dług\"))\n"), (
        "ALA MA KOTA I PSA\nasp i atok am alA\n17 znaków\n5 słów: Ala, ma, kota, i, psa\nSamogłoski: 7\nNajdłuższe: kota\n4.50 zł True\n")),
    demonstracja={"tytul": "Analiza zdania: wielkie litery, od tyłu, słowa, samogłoski", "kroki": [
        "`strip()` — usuwa spacje z brzegów; `czyste` ma 17 znaków (spacje w środku się liczą).",
        "`upper()` zwraca nowy napis wielkimi literami — `czyste` się nie zmienia.",
        "`[::-1]` — wycinek z krokiem -1: napis od tyłu.",
        "`split()` bez argumentu dzieli po spacjach → lista 5 słów; `\", \".join(slowa)` skleja je z przecinkiem.",
        "Pętla po znakach: `lower()` zamienia „A” na „a”, `in \"aąeęioóuy\"` sprawdza samogłoskę → 7 (a, a, a, o, a, i, a).",
        "`max(slowa, key=len)` — najdłuższe słowo według długości; przy remisie pierwsze (kota, 4 litery).",
        "`replace` zamienia przecinek na kropkę (przyda się przy float), `lower().startswith` — wyszukiwanie po początku."],
        "wynik": "Siedem linii, m.in. „5 słów: Ala, ma, kota, i, psa” i „Samogłoski: 7”."},
    jak_uruchomic=["Zapisz jako tekst.py → ▶ Uruchom.", "Zmień zdanie na własne i przewidź liczbę samogłosek przed uruchomieniem."],
    cwiczenia=[
        C("prowadzone",
          "Dla napisu `t = \"Zeszyt A5 w kratkę\"` podaj: (1) `len(t)`, (2) `t.split()` — ile elementów, (3) `t.lower().count(\"z\")`, (4) `t.replace(\"A5\", \"A4\")`. Czas: 15 minut.",
          "(1) 18; (2) 4; (3) 2; (4) Zeszyt A4 w kratkę.",
          ["Licz także spacje.", "split() dzieli po spacjach.", "lower() zamienia Z na z, potem licz."],
          "(1) 18 znaków; (2) ['Zeszyt', 'A5', 'w', 'kratkę'] = 4; (3) „zeszyt” ma 2 litery z; (4) „Zeszyt A4 w kratkę”.",
          [li("a", "(1) len(t)", 18), li("b", "(2) Liczba słów", 4), li("c", "(3) Liczba „z”", 2, bledy=[bl(1, "bez lower() nie policzysz wielkiego Z")]), tx("d", "(4) Po replace", "Zeszyt A4 w kratkę")]),
        C("samodzielne",
          "Wyszukiwarka sklepu: `def pasuje(fraza, nazwa): return fraza in nazwa`. (1) Co zwróci `pasuje(\"długopis\", \"Długopis niebieski\")`? (2) Popraw treść return (wpisz nowe wyrażenie), żeby nie zależała od wielkości liter i spacji na brzegach frazy. (3) Co wtedy zwróci `pasuje(\"  DŁUGOPIS \", \"Długopis niebieski\")`? Czas: 15 minut.",
          "(1) False; (2) fraza.strip().lower() in nazwa.lower(); (3) True.",
          ["„d” i „D” to różne znaki.", "Sprowadź oba napisy do małych liter.", "strip() usuwa spacje z frazy."],
          "(1) False — wielkość liter; (2) `return fraza.strip().lower() in nazwa.lower()`; (3) True.",
          [wy("a", "(1) Wynik", ["True", "False"], "False"), tx("b", "(2) Wyrażenie", "fraza.strip().lower() in nazwa.lower()", zawiera=["strip", "lower", "in", "nazwa.lower"]), wy("c", "(3) Wynik po poprawce", ["True", "False"], "True")]),
    ],
    typowe_bledy=[
        B("Napis się „nie zmienia” po .upper()", "Wynik metody nie został zapisany.", "Czy jest `x = x.upper()`?", "Przypisz wynik albo użyj go od razu."),
        B("AttributeError: 'list' object has no attribute 'lower'", "Metoda napisu wywołana na liście (np. po split()).", "`print(type(x))`.", "Wywołaj na każdym elemencie w pętli albo przed split()."),
        B("TypeError: 'str' object does not support item assignment", "Próba zmiany znaku: `t[0] = \"z\"`.", "Napisy są niezmienne.", "Zbuduj nowy napis: `t = \"z\" + t[1:]`."),
    ],
    pulapki=["Polskie litery: „Ą”.lower() działa poprawnie, ale porównania z ogonkami i bez to różne napisy („zolty” ≠ „żółty”).", "split(\",\") nie usuwa spacji: \"a, b\".split(\",\") → ['a', ' b']."],
    zadania=["Program: wpisz zdanie → wielkie litery, od tyłu, liczba znaków, samogłosek, słów, najdłuższe słowo.", "Wyszukiwarka produktów bez względu na wielkość liter.", "Zamiana „4,50” na liczbę 4.5."],
    pytania=[["Dlaczego t.upper() nie zmienia t?", "Napisy są niezmienne — metoda zwraca nowy napis."], ["Co robi \"-\".join([\"a\", \"b\"])?", "Zwraca \"a-b\"."], ["Jak odwrócić napis?", "t[::-1]."]],
    podsumowanie="Przetwarzasz tekst metodami napisów, liczysz znaki/słowa/samogłoski, odwracasz napis i budujesz wyszukiwanie niezależne od wielkości liter.",
    test=[T("\"Klej\".lower() zwraca:", ["\"KLEJ\"", "\"klej\"", "None", "zmienia oryginał"], 1, "Nowy napis małymi literami."),
          T("\"a b  c\".split() daje:", ["['a', 'b', '', 'c']", "['a', 'b', 'c']", "['a b  c']", "błąd"], 1, "split() bez argumentu łączy wiele spacji."),
          T("\"abc\"[::-1] to:", ["\"abc\"", "\"cba\"", "\"c\"", "błąd"], 1, "Krok -1."),
          T("\"PL\" in \"pl-123\" daje:", ["True", "False", "błąd", "None"], 1, "Wielkość liter ma znaczenie.")],
    w_praktyce=["Testując wyszukiwarkę: wielkie/małe litery, spacje, polskie znaki, pusta fraza.", "Porównania w testach: najpierw strip(), potem porównuj."],
    zrodla=[Z.PY_STDTYPES, Z.PY_TUT_INTRO],
)

# =========================================================================== TYDZIEŃ 3
FUNKCJE = L(
    id="funkcje", nazwa="Funkcje: def, parametry, return, docstring, if __name__ == \"__main__\"", tydzien=3,
    slowa=["funkcja", "def", "parametr", "argument", "return", "None", "docstring", "zasięg", "wartość domyślna", "__main__", "wywołanie"],
    cel="Po tej lekcji piszesz funkcje z parametrami i return, dokumentujesz je docstringiem, odróżniasz return od print, używasz wartości domyślnych i chronisz kod bloku `if __name__ == \"__main__\":` — żeby funkcje dało się testować.",
    po_co="Testy jednostkowe (tydzień 7) wywołują funkcje i sprawdzają, co zwracają. Kod bez funkcji jest prawie nietestowalny — tester to od razu widzi.",
    wymagania=["Lekcje tygodni 1–2 (warunki, pętle, listy)."],
    wyjasnienie=(
        "## Funkcja = przepis z nazwą\n"
        "```\ndef brutto(netto, vat=23):\n    \"\"\"Zwraca cenę brutto z netto i stawki VAT w procentach.\"\"\"\n    return round(netto * (1 + vat / 100), 2)\n```\n"
        "`def` definiuje funkcję, w nawiasie **parametry** (wejście), `return` oddaje **wynik** i kończy funkcję. Wywołanie: `brutto(10)` → 12.3. Wartości w wywołaniu to **argumenty**.\n"
        "## Wartość domyślna\n"
        "`vat=23` — gdy nie podasz drugiego argumentu, użyje 23. `brutto(10, 8)` → 10.8. Można nazwać argument: `brutto(netto=10, vat=5)`.\n"
        "## return a print\n"
        "`print` tylko pokazuje tekst na ekranie; `return` oddaje wartość, którą można zapisać, porównać i przetestować. Funkcja bez return zwraca `None` — klasyczny błąd: `wynik = funkcja_z_printem()` → None.\n"
        "## Docstring\n"
        "Pierwszy napis w potrójnym cudzysłowie w funkcji opisuje, co robi, co przyjmuje i co zwraca (konwencja PEP 257). `help(brutto)` go wyświetli.\n"
        "## Zasięg zmiennych\n"
        "Zmienne utworzone w funkcji istnieją tylko w niej. Dane przekazuj parametrami, wynik — return (nie zmiennymi globalnymi).\n"
        "## if __name__ == \"__main__\":\n"
        "Kod w tym bloku wykonuje się tylko przy uruchomieniu pliku (▶ Uruchom), a NIE przy imporcie. Test importuje Twój plik, żeby wywołać funkcje — gdyby input() był poza tym blokiem, test zatrzymałby się w oczekiwaniu na dane. "
        "Dlatego w zadaniach od tygodnia 3: funkcje na górze, rozmowa z użytkownikiem (input/print) w bloku main."),
    przyklad=kod("funkcje", (
        "def brutto(netto, vat=23):\n"
        "    \"\"\"Zwraca cenę brutto (2 miejsca po przecinku) z ceny netto i stawki VAT w %.\"\"\"\n"
        "    return round(netto * (1 + vat / 100), 2)\n\n\n"
        "def czy_parzysta(n):\n"
        "    \"\"\"True, gdy n jest parzyste.\"\"\"\n"
        "    return n % 2 == 0\n\n\n"
        "def wypisz_brutto(netto):\n"
        "    print(\"Brutto:\", brutto(netto))\n\n\n"
        "if __name__ == \"__main__\":\n"
        "    print(brutto(10), brutto(10, 8), brutto(netto=100, vat=5))\n"
        "    print(czy_parzysta(4), czy_parzysta(7))\n"
        "    wynik = wypisz_brutto(20)\n"
        "    print(\"Funkcja bez return zwraca:\", wynik)\n"), "12.3 10.8 105.0\nTrue False\nBrutto: 24.6\nFunkcja bez return zwraca: None\n"),
    demonstracja={"tytul": "Ceny brutto w sklepie — trzy funkcje i blok main", "kroki": [
        "`def brutto(netto, vat=23):` — dwa parametry, drugi z wartością domyślną 23.",
        "Docstring w potrójnym cudzysłowie — opis dla ludzi i dla `help(brutto)`.",
        "`return round(netto * (1 + vat / 100), 2)` — 10 × 1.23 = 12.3; `round(…, 2)` zaokrągla do groszy.",
        "`czy_parzysta` zwraca bool: wynik porównania `n % 2 == 0`.",
        "`wypisz_brutto` używa print i NIE ma return — dlatego `wynik` to None. Do testów nadaje się `brutto`, nie `wypisz_brutto`.",
        "`if __name__ == \"__main__\":` — wywołania i print tylko przy uruchomieniu. Test zaimportuje plik i wywoła `brutto(10)` bez wypisywania czegokolwiek.",
        "Eksperyment: wywołaj `brutto()` bez argumentu → TypeError: missing 1 required positional argument: 'netto'."],
        "wynik": "„12.3 10.8 105.0”, „True False”, „Brutto: 24.6”, „Funkcja bez return zwraca: None”."},
    jak_uruchomic=["Zapisz jako ceny.py → ▶ Uruchom.", "W terminalu Mentora: `python -c \"import ceny; print(ceny.brutto(50))\"` — import NIE uruchamia bloku main."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór `brutto` napisz `def netto(brutto, vat=23): return round(brutto / (1 + vat / 100), 2)`. Podaj wyniki: (1) `netto(12.3)`, (2) `netto(10.8, 8)`, (3) `netto(123)`. Czas: 15 minut.",
          "(1) 10.0; (2) 10.0; (3) 100.0.",
          ["Odwrotność mnożenia przez 1.23 to dzielenie przez 1.23.", "Drugi argument zastępuje domyślne 23.", "123 / 1.23 = 100."],
          "12.3 / 1.23 = 10.0; 10.8 / 1.08 = 10.0; 123 / 1.23 = 100.0.",
          [li("a", "(1) netto(12.3)", 10.0), li("b", "(2) netto(10.8, 8)", 10.0, bledy=[bl(8.78, "podałeś vat=8 — dzielisz przez 1.08, nie przez 1.23")]), li("c", "(3) netto(123)", 100.0)]),
        C("samodzielne",
          "Funkcja: `def rabat(razem):` / `    if razem >= 100:` / `        print(razem * 0.95)` / `    else:` / `        print(razem)`. Test: `assert rabat(200) == 190`. (1) Co zwraca `rabat(200)`? (2) Czy test przejdzie (tak/nie)? (3) Którą instrukcję zamieniasz w obu gałęziach (wpisz słowo)? Czas: 15 minut.",
          "(1) None; (2) nie; (3) return.",
          ["print tylko wyświetla.", "Funkcja bez return zwraca None.", "Wynik dla testu oddaje się słowem…"],
          "(1) None — funkcja tylko wypisuje 190.0; (2) nie — None == 190 to False; (3) `return razem * 0.95` i `return razem`.",
          [tx("a", "(1) Zwraca", "None", bledy=[bl("190", "190.0 tylko się WYPISUJE — funkcja nic nie zwraca")]), wy("b", "(2) Test przejdzie?", ["tak", "nie"], "nie"), tx("c", "(3) Instrukcja", "return")]),
    ],
    typowe_bledy=[
        B("TypeError: brutto() missing 1 required positional argument: 'netto'", "Wywołanie bez wymaganego argumentu.", "Porównaj wywołanie z def.", "Podaj argument albo dodaj wartość domyślną."),
        B("Wynik funkcji to None", "Brak return (jest tylko print) albo return w złym miejscu.", "Dodaj `print(repr(wynik))`.", "return w każdej gałęzi, która ma oddać wynik."),
        B("Test „wisi” albo EOFError przy imporcie", "input() poza blokiem `if __name__ == \"__main__\":`.", "Czy coś poza funkcjami pyta użytkownika?", "Przenieś input()/print() programu do bloku main."),
    ],
    pulapki=["Kod po return w tej samej gałęzi nigdy się nie wykona.", "Lista jako wartość domyślna (def f(x=[])) jest wspólna dla wywołań — używaj None."],
    zadania=["5 funkcji z docstringami: pole prostokąta, czy parzysta, maksimum listy bez max(), odwróć napis, silnia.", "Każda funkcja zwraca wynik (return), wywołania w bloku main.", "Sprawdź help() jednej funkcji."],
    pytania=[["Czym różni się return od print?", "return oddaje wartość do dalszego użycia i testów; print tylko pokazuje."],
             ["Co zwraca funkcja bez return?", "None."], ["Po co if __name__ == \"__main__\"?", "Żeby kod programu nie wykonywał się przy imporcie (np. przez testy)."]],
    podsumowanie="Piszesz funkcje z parametrami, wartościami domyślnymi, return i docstringiem; oddzielasz logikę (funkcje) od rozmowy z użytkownikiem (blok main) — kod staje się testowalny.",
    test=[T("def f(x): x * 2 — co zwraca f(3)?", ["6", "None", "3", "błąd"], 1, "Brak return."),
          T("def f(a, b=2): return a * b — f(5) to:", ["5", "10", "7", "błąd"], 1, "b domyślnie 2."),
          T("Kod w if __name__ == \"__main__\": wykonuje się:", ["zawsze", "tylko przy uruchomieniu pliku", "tylko przy imporcie", "nigdy"], 1, "Import go pomija."),
          T("Docstring to:", ["komentarz #", "napis z opisem na początku funkcji", "nazwa funkcji", "typ zwracany"], 1, "PEP 257.")],
    w_praktyce=["Każda reguła biznesowa = osobna funkcja z return — łatwa do przetestowania.", "Czytając cudzy kod, zaczynasz od docstringów i nazw funkcji."],
    zrodla=[Z.PY_TUT_CTRL, Z.PY_PEP257, Z.PY_TUT_MOD],
)

SLOWNIKI = L(
    id="slowniki", nazwa="Słowniki i krotki: klucz → wartość", tydzien=3,
    slowa=["słownik", "dict", "klucz", "wartość", "items", "keys", "values", "get", "del", "krotka", "tuple", "lista słowników", "sorted key"],
    cel="Po tej lekcji przechowujesz dane jako klucz → wartość w słowniku (dodaj, zmień, usuń, get, in), przechodzisz po items(), sortujesz po wartości, używasz krotek i listy słowników jako prostej „tabeli”.",
    po_co="Dane z API, plików JSON i baz przychodzą jako słowniki. Tester porównuje oczekiwany słownik z otrzymanym w każdym teście API.",
    wymagania=["Lekcje „Listy” i „Funkcje”."],
    wyjasnienie=(
        "## Słownik\n"
        "`stany = {\"zeszyt\": 120, \"klej\": 110}` — pary **klucz: wartość** w nawiasach klamrowych. Klucz (najczęściej napis) jest unikalny, po nim szybko znajdujesz wartość: `stany[\"zeszyt\"]` → 120.\n"
        "## Operacje\n"
        "| operacja | co robi |\n|---|---|\n"
        "| `stany[\"gumka\"] = 150` | dodaje albo podmienia |\n"
        "| `del stany[\"klej\"]` | usuwa (brak klucza → KeyError) |\n"
        "| `stany.get(\"farby\", 0)` | wartość albo 0, gdy brak klucza — bez błędu |\n"
        "| `\"klej\" in stany` | czy jest taki KLUCZ |\n"
        "| `len(stany)` | liczba par |\n"
        "| `for nazwa, ilosc in stany.items():` | pętla po parach |\n"
        "`keys()` — same klucze, `values()` — same wartości (`sum(stany.values())`).\n"
        "## Sortowanie po wartości\n"
        "`sorted(stany.items(), key=lambda p: p[1])` — lista par (krotek) posortowana po drugim elemencie, czyli po ilości. `lambda p: p[1]` to mała funkcja „weź element 1 pary”.\n"
        "## Krotka\n"
        "`para = (\"zeszyt\", 120)` — jak lista, ale niezmienna, w nawiasach okrągłych. Rozpakowanie: `nazwa, ilosc = para`. items() zwraca właśnie krotki.\n"
        "## Lista słowników — prosta tabela\n"
        "`produkty = [{\"nazwa\": \"zeszyt\", \"cena\": 4.5}, {\"nazwa\": \"klej\", \"cena\": 3.4}]` — każdy słownik to wiersz, klucze to kolumny. Tak wyglądają dane z API i z csv.DictReader (tydzień 4)."),
    przyklad=kod("slowniki", (
        "stany = {\"zeszyt\": 120, \"klej\": 110, \"zszywki\": 0}\n"
        "stany[\"gumka\"] = 150\n"
        "stany[\"klej\"] = 100\n"
        "del stany[\"zszywki\"]\n"
        "print(stany)\n"
        "print(stany.get(\"farby\", 0), \"klej\" in stany, len(stany))\n"
        "for nazwa, ilosc in sorted(stany.items(), key=lambda p: p[1]):\n"
        "    print(f\"{nazwa:<8}{ilosc:>5}\")\n"
        "print(\"Razem sztuk:\", sum(stany.values()))\n"
        "produkty = [{\"nazwa\": \"zeszyt\", \"cena\": 4.5}, {\"nazwa\": \"klej\", \"cena\": 3.4}]\n"
        "najtanszy = min(produkty, key=lambda p: p[\"cena\"])\n"
        "print(\"Najtańszy:\", najtanszy[\"nazwa\"])\n"), (
        "{'zeszyt': 120, 'klej': 100, 'gumka': 150}\n0 True 3\nklej      100\nzeszyt    120\ngumka     150\nRazem sztuk: 370\nNajtańszy: klej\n")),
    demonstracja={"tytul": "Stany magazynowe w słowniku", "kroki": [
        "Słownik z 3 parami; `stany[\"gumka\"] = 150` dodaje nową parę, `stany[\"klej\"] = 100` podmienia wartość.",
        "`del stany[\"zszywki\"]` — usunięcie pary.",
        "`get(\"farby\", 0)` — brak klucza, więc 0 (bez KeyError); `\"klej\" in stany` → True; 3 pary.",
        "`sorted(stany.items(), key=lambda p: p[1])` — pary rosnąco po ilości: klej 100, zeszyt 120, gumka 150.",
        "`f\"{nazwa:<8}{ilosc:>5}\"` — wyrównanie: nazwa do lewej na 8 znakach, ilość do prawej na 5 — czytelna tabelka.",
        "`sum(stany.values())` — suma samych wartości.",
        "Lista słowników: `min(..., key=lambda p: p[\"cena\"])` wybiera słownik z najniższą ceną."],
        "wynik": "Słownik po zmianach, „0 True 3”, tabelka posortowana po ilości, „Razem sztuk: 370”, „Najtańszy: klej”."},
    jak_uruchomic=["Zapisz jako magazyn_demo.py → ▶ Uruchom.", "Dopisz `print(stany[\"farby\"])` → KeyError; zamień na get."],
    cwiczenia=[
        C("prowadzone",
          "`c = {\"zeszyt\": 4.5, \"długopis\": 2.3}`. Po kolei: `c[\"klej\"] = 3.4`, `c[\"zeszyt\"] = 4.9`, `del c[\"długopis\"]`. Podaj: (1) `len(c)`, (2) `c[\"zeszyt\"]`, (3) `c.get(\"długopis\", 0)`, (4) `round(sum(c.values()), 2)`. Czas: 15 minut.",
          "(1) 2; (2) 4.9; (3) 0; (4) 8.3.",
          ["Przypisanie istniejącego klucza podmienia wartość.", "Po del klucza nie ma.", "Zostały zeszyt 4.9 i klej 3.4."],
          "Po zmianach: {\"zeszyt\": 4.9, \"klej\": 3.4} → len 2, zeszyt 4.9, get → 0, suma 8.3.",
          [li("a", "(1) len(c)", 2), li("b", "(2) c[\"zeszyt\"]", 4.9, bledy=[bl(4.5, "drugie przypisanie podmieniło wartość")]), li("c", "(3) get", 0), li("d", "(4) suma wartości", 8.3)]),
        C("samodzielne",
          "Lista `zamowienia = [{\"nr\": 1, \"kwota\": 45.0}, {\"nr\": 2, \"kwota\": 120.5}, {\"nr\": 3, \"kwota\": 99.99}]`. (1) Suma kwot (wyrażenie lub wynik)? (2) Numer zamówienia z największą kwotą? (3) Ile zamówień ma kwotę ≥ 100? (4) Co da `zamowienia[0][\"klient\"]` — wybierz: None / KeyError / pusty napis. Czas: 15 minut.",
          "(1) 265.49; (2) 2; (3) 1; (4) KeyError.",
          ["Pętla po liście, z każdego słownika z[\"kwota\"].", "max(zamowienia, key=lambda z: z[\"kwota\"]).", "Brakujący klucz w [] daje błąd; get() — nie."],
          "(1) 45.0 + 120.5 + 99.99 = 265.49; (2) nr 2; (3) tylko 120.5 → 1; (4) KeyError: 'klient' — bezpiecznie: z.get(\"klient\").",
          [kw("a", "(1) Suma kwot", 265.49), li("b", "(2) Nr największego", 2), li("c", "(3) Kwota ≥ 100", 1), wy("d", "(4) Brakujący klucz", ["None", "KeyError", "pusty napis"], "KeyError")]),
    ],
    typowe_bledy=[
        B("KeyError: 'farby'", "Odczyt nieistniejącego klucza nawiasem [].", "`print(stany.keys())`.", "`stany.get(\"farby\", 0)` albo `if \"farby\" in stany:`."),
        B("RuntimeError: dictionary changed size during iteration", "Usuwanie kluczy w pętli po tym samym słowniku.", "Czy w pętli jest del?", "Pętla po `list(stany.keys())` albo zbuduj nowy słownik."),
        B("TypeError: unhashable type: 'list'", "Lista jako klucz słownika.", "Jakiego typu jest klucz?", "Kluczem może być napis, liczba albo krotka."),
    ],
    pulapki=["`in` na słowniku sprawdza klucze, nie wartości (`120 in stany` → False).", "Kolejność kluczy = kolejność dodania; do raportu sortuj jawnie."],
    zadania=["Słownik produkt → ilość: dodaj, zmień, usuń, wypisz posortowane po ilości.", "Lista 3 słowników zamówień: suma, największe, filtr ≥ 100.", "Zamień dwie równoległe listy z lekcji „Listy” na słownik."],
    pytania=[["Co zwraca d.get(\"x\", 0), gdy klucza x nie ma?", "0."], ["Jak przejść po parach słownika?", "for k, v in d.items():"], ["Czym krotka różni się od listy?", "Jest niezmienna; nawiasy okrągłe."]],
    podsumowanie="Przechowujesz dane klucz → wartość, bezpiecznie je odczytujesz (get, in), sortujesz po wartości i budujesz prostą tabelę z listy słowników.",
    test=[T("d = {\"a\": 1}; d[\"a\"] = 5; d[\"a\"] to:", ["1", "5", "[1, 5]", "błąd"], 1, "Podmiana wartości."),
          T("\"b\" in {\"a\": \"b\"} daje:", ["True", "False", "błąd", "None"], 1, "in sprawdza klucze."),
          T("Bezpieczny odczyt klucza, którego może nie być:", ["d[k]", "d.get(k)", "d.k", "del d[k]"], 1, "get zwraca None/domyślną."),
          T("d.items() zwraca:", ["same klucze", "same wartości", "pary (klucz, wartość)", "długość"], 2, "Krotki par.")],
    w_praktyce=["W testach API porównujesz słowniki: assert odpowiedz[\"status\"] == \"ok\".", "Brakujące pole w danych — test na KeyError lub get z wartością domyślną."],
    zrodla=[Z.PY_TUT_DS, Z.PY_STDTYPES],
)

BLEDY = L(
    id="bledy", nazwa="Obsługa błędów: try / except / else / finally i raise", tydzien=3,
    slowa=["wyjątek", "exception", "try", "except", "ValueError", "ZeroDivisionError", "KeyError", "TypeError", "raise", "finally", "traceback", "walidacja"],
    cel="Po tej lekcji czytasz traceback (typ błędu, plik, linia), łapiesz konkretne wyjątki try/except, ponawiasz pytanie w pętli przy złym wpisie i sam zgłaszasz błąd raise ValueError przy niepoprawnych danych.",
    po_co="Program sklepu nie może paść, gdy klient wpisze „dwa” zamiast 2. Tester celowo wpisuje złe dane — i ocenia, czy komunikat jest zrozumiały.",
    wymagania=["Lekcja „Funkcje”."],
    wyjasnienie=(
        "## Traceback — czytaj od dołu\n"
        "```\nTraceback (most recent call last):\n  File \"kalk.py\", line 3, in <module>\n    ilosc = int(wpis)\nValueError: invalid literal for int() with base 10: 'dwa'\n```\n"
        "Ostatnia linia: **typ błędu** i opis. Wyżej: plik i **numer linii**. To pierwsze, co wklejasz do zgłoszenia lub asystentowi.\n"
        "## try / except\n"
        "```\ntry:\n    ilosc = int(wpis)\nexcept ValueError:\n    print(\"Podaj liczbę całkowitą\")\n```\n"
        "Python próbuje wykonać blok try; jeśli wystąpi ValueError, przechodzi do except zamiast kończyć program. Łap **konkretne** wyjątki — samo `except:` ukrywa też Twoje literówki.\n"
        "## Najczęstsze wyjątki\n"
        "| wyjątek | kiedy |\n|---|---|\n"
        "| `ValueError` | zła wartość: int(\"dwa\") |\n"
        "| `ZeroDivisionError` | dzielenie przez zero |\n"
        "| `KeyError` | brak klucza w słowniku |\n"
        "| `IndexError` | indeks poza listą |\n"
        "| `TypeError` | zły typ: \"a\" + 1 |\n"
        "| `FileNotFoundError` | brak pliku (tydzień 4) |\n"
        "## else i finally\n"
        "`else:` wykonuje się, gdy w try NIE było błędu; `finally:` — zawsze (np. komunikat „koniec”).\n"
        "## Pętla do skutku\n"
        "`while True: try: return int(input(...)) except ValueError: print(\"To nie liczba\")` — pyta, aż dostanie poprawny wpis.\n"
        "## raise — zgłaszasz błąd sam\n"
        "Funkcja nie powinna po cichu liczyć bzdur: `if ilosc <= 0: raise ValueError(\"ilość musi być dodatnia\")`. Wywołujący (albo test) dostaje jasny sygnał. W tygodniu 7 sprawdzisz to `pytest.raises(ValueError)`."),
    przyklad=kod("bledy", (
        "def wydaj(stan, ilosc):\n"
        "    \"\"\"Zwraca nowy stan po wydaniu towaru; zła ilość → ValueError.\"\"\"\n"
        "    if ilosc <= 0:\n"
        "        raise ValueError(\"ilość musi być dodatnia\")\n"
        "    if ilosc > stan:\n"
        "        raise ValueError(f\"brak towaru: na stanie {stan}\")\n"
        "    return stan - ilosc\n\n\n"
        "for wpis in [\"5\", \"dwa\", \"0\", \"200\"]:\n"
        "    try:\n"
        "        ilosc = int(wpis)\n"
        "        nowy = wydaj(120, ilosc)\n"
        "    except ValueError as e:\n"
        "        print(f\"{wpis!r}: błąd — {e}\")\n"
        "    else:\n"
        "        print(f\"{wpis!r}: wydano, zostało {nowy}\")\n"
        "    finally:\n"
        "        print(\"---\")\n"), (
        "'5': wydano, zostało 115\n---\n'dwa': błąd — invalid literal for int() with base 10: 'dwa'\n---\n'0': błąd — ilość musi być dodatnia\n---\n'200': błąd — brak towaru: na stanie 120\n---\n")),
    demonstracja={"tytul": "Wydawanie towaru: trzy rodzaje złych danych", "kroki": [
        "`wydaj(stan, ilosc)` — sama logika: dwie reguły walidacji z `raise ValueError(\"…\")` i return nowego stanu.",
        "Pętla po 4 wpisach — jak 4 przypadki testowe: poprawny, tekst, zero, za dużo.",
        "`int(wpis)` dla „dwa” rzuca ValueError od Pythona; `wydaj` dla 0 i 200 rzuca ValueError z naszym komunikatem.",
        "`except ValueError as e:` — `e` to obiekt błędu, `{e}` wypisuje jego opis.",
        "`else:` — tylko dla „5”: wydano, zostało 115.",
        "`finally:` — linia „---” po każdym wpisie, z błędem i bez.",
        "`{wpis!r}` — wypisuje wartość z cudzysłowem ('5'), widać, że to napis."],
        "wynik": "Cztery bloki: '5' wydano (115), 'dwa' błąd int(), '0' ilość musi być dodatnia, '200' brak towaru — każdy zakończony „---”."},
    jak_uruchomic=["Zapisz jako wydawanie.py → ▶ Uruchom.", "Usuń try/except i uruchom — zobaczysz pełny traceback i zatrzymanie programu na „dwa”."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji: `def podziel(a, b): return a / b`, wywołania w try z `except ZeroDivisionError: print(\"Nie dzielimy przez zero\")`. Co wypisze dla: (1) podziel(10, 4), (2) podziel(5, 0)? (3) Jaki wyjątek rzuci podziel(\"10\", 2)? Czas: 15 minut.",
          "(1) 2.5; (2) Nie dzielimy przez zero; (3) TypeError.",
          ["10 / 4 w Pythonie.", "Dzielenie przez 0 → ZeroDivisionError → except.", "Napis podzielony przez liczbę to zły typ."],
          "(1) 2.5; (2) „Nie dzielimy przez zero”; (3) TypeError: unsupported operand type(s) for /: 'str' and 'int' — tego except nie złapie.",
          [li("a", "(1) podziel(10, 4)", 2.5), tx("b", "(2) Komunikat", "Nie dzielimy przez zero"), wy("c", "(3) Wyjątek dla \"10\" / 2", ["ValueError", "ZeroDivisionError", "TypeError", "KeyError"], "TypeError")]),
        C("samodzielne",
          "Traceback: `File \"sklep.py\", line 14, in cena_koszyka` / `return suma / len(koszyk)` / `ZeroDivisionError: division by zero`. (1) W której linii jest błąd? (2) W jakiej funkcji? (3) Jaki stan danych go wywołał (wybierz)? (4) Co jest lepszą poprawką: except: pass / sprawdzenie pustego koszyka przed dzieleniem? Czas: 15 minut.",
          "(1) 14; (2) cena_koszyka; (3) pusty koszyk; (4) sprawdzenie pustego koszyka.",
          ["Numer linii jest w linii File.", "Nazwa po „in”.", "len(koszyk) == 0 oznacza…"],
          "(1) linia 14; (2) cena_koszyka; (3) pusty koszyk (len = 0); (4) `if not koszyk: return 0` (albo jasny komunikat) — except: pass ukryłby problem.",
          [li("a", "(1) Linia", 14), tx("b", "(2) Funkcja", "cena_koszyka"), wy("c", "(3) Przyczyna", ["pusty koszyk", "za duża kwota", "brak internetu", "zły plik"], "pusty koszyk"),
           wy("d", "(4) Lepsza poprawka", ["except: pass", "sprawdzenie pustego koszyka"], "sprawdzenie pustego koszyka")]),
    ],
    typowe_bledy=[
        B("Program „działa”, ale wynik bez sensu i bez komunikatu", "`except:` albo `except Exception: pass` połknęło błąd.", "Usuń tymczasowo try i zobacz traceback.", "Łap konkretny wyjątek i reaguj komunikatem."),
        B("UnboundLocalError / NameError po bloku try", "Zmienna przypisana w try, który się nie udał, użyta dalej.", "Czy zmienna ma wartość, gdy był wyjątek?", "Użyj zmiennej w else albo nadaj wartość przed try."),
    ],
    pulapki=["Zbyt szeroki try (cała funkcja) — nie wiesz, która linia rzuciła błąd. Obejmuj tylko ryzykowną linię.", "raise bez komunikatu — zawsze pisz, CO jest nie tak i jakie są dozwolone wartości."],
    zadania=["Funkcja wczytaj_liczbe() pytająca do skutku.", "Kalkulator z obsługą ValueError i ZeroDivisionError.", "Funkcja z raise ValueError dla ilości ≤ 0."],
    pytania=[["Gdzie w tracebacku jest typ błędu?", "W ostatniej linii."], ["Dlaczego nie except: pass?", "Ukrywa błędy, także Twoje literówki."], ["Kiedy wykonuje się else w try?", "Gdy w try nie było wyjątku."]],
    podsumowanie="Czytasz traceback, łapiesz konkretne wyjątki, ponawiasz pytanie przy złym wpisie i zgłaszasz błędy raise z jasnym komunikatem.",
    test=[T("int(\"3.5\") rzuci:", ["TypeError", "ValueError", "nic — da 3", "ZeroDivisionError"], 1, "Napis z kropką to nie int."),
          T("Gdzie szukasz numeru linii w tracebacku?", ["w pierwszej linii", "w linii File \"…\", line N", "w ostatniej linii", "nigdzie"], 1, "File … line N."),
          T("finally wykonuje się:", ["tylko przy błędzie", "tylko bez błędu", "zawsze", "nigdy"], 2, "Zawsze."),
          T("Funkcja dostała ilość -3. Najlepiej:", ["zwrócić 0 po cichu", "raise ValueError z opisem", "print i dalej liczyć", "zakończyć Pythona"], 1, "Jasny sygnał dla wywołującego i testu.")],
    w_praktyce=["W bug raporcie zawsze ostatnia linia tracebacku i numer linii.", "Test negatywny = sprawdzenie, że zła dana daje czytelny błąd, nie awarię."],
    zrodla=[Z.PY_TUT_ERR, Z.SJSI_CTFL_PL],
)

MODULY_STD = L(
    id="moduly_std", nazwa="Moduły standardowe: random i datetime", tydzien=3,
    slowa=["moduł", "import", "from", "random", "randint", "choice", "sample", "seed", "datetime", "date", "timedelta", "strftime", "strptime"],
    cel="Po tej lekcji importujesz moduły standardowe, losujesz (randint, choice, sample) — także powtarzalnie z seed — i liczysz na datach (date, timedelta, strftime, strptime).",
    po_co="Losowe dane testowe i daty (terminy, ważność, „za 7 dni”) są w każdym systemie. Testy z losowością bez seed są niepowtarzalne — a test musi dać ten sam wynik za każdym razem.",
    wymagania=["Lekcje „Funkcje” i „Listy”."],
    wyjasnienie=(
        "## import\n"
        "`import random` — cały moduł, używasz `random.randint(...)`. `from datetime import date, timedelta` — konkretne nazwy, używasz `date.today()`. Moduły standardowe są w każdym Pythonie, bez instalacji.\n"
        "## random\n"
        "- `random.randint(1, 100)` — liczba całkowita od 1 do 100 **włącznie**;\n"
        "- `random.choice(lista)` — jeden losowy element;\n"
        "- `random.sample(lista, 3)` — 3 różne elementy (bez powtórzeń);\n"
        "- `random.shuffle(lista)` — tasuje listę w miejscu;\n"
        "- `random.seed(42)` — ustawia ziarno: od tej chwili losowania są **powtarzalne** (ważne w testach i przy odtwarzaniu błędu).\n"
        "## datetime\n"
        "- `date.today()` — dzisiejsza data; `date(2026, 12, 24)` — konkretna;\n"
        "- `timedelta(days=7)` — odcinek czasu: `dzis + timedelta(days=7)` to data za tydzień; różnica dwóch dat to timedelta, `.days` — liczba dni;\n"
        "- `strftime(\"%d.%m.%Y\")` — data → napis po polsku (23.11.2026); `%A` — nazwa dnia (po angielsku w domyślnych ustawieniach);\n"
        "- `datetime.strptime(\"24.12.2026\", \"%d.%m.%Y\").date()` — napis → data.\n"
        "## Funkcja testowalna z datą\n"
        "Zamiast `date.today()` w środku funkcji przekaż datę parametrem: `def termin(od, dni=7): return od + timedelta(days=dni)`. Test poda stałą datę i zawsze dostanie ten sam wynik."),
    przyklad=kod("moduly_std", (
        "import random\n"
        "from datetime import date, datetime, timedelta\n\n"
        "random.seed(7)\n"
        "produkty = [\"zeszyt\", \"długopis\", \"klej\", \"gumka\", \"blok\", \"kredki\"]\n"
        "print(\"Do inwentaryzacji:\", random.sample(produkty, 3))\n"
        "print(\"Kostka:\", random.randint(1, 6))\n\n"
        "def termin(od, dni=7):\n"
        "    return od + timedelta(days=dni)\n\n"
        "start = date(2026, 11, 23)\n"
        "print(\"Termin:\", termin(start).strftime(\"%d.%m.%Y\"))\n"
        "wigilia = datetime.strptime(\"24.12.2026\", \"%d.%m.%Y\").date()\n"
        "print(\"Dni do Wigilii:\", (wigilia - start).days)\n"), None),
    demonstracja={"tytul": "Losowanie produktów do inwentaryzacji i termin za 7 dni", "kroki": [
        "`import random` i `from datetime import date, datetime, timedelta` — dwa sposoby importu.",
        "`random.seed(7)` — ziarno: przy każdym uruchomieniu wylosujesz te same 3 produkty. Usuń tę linię, uruchom 3 razy — wyniki będą różne.",
        "`random.sample(produkty, 3)` — 3 RÓŻNE produkty (choice mógłby się powtórzyć).",
        "`random.randint(1, 6)` — obie granice wchodzą.",
        "`termin(od, dni=7)` — data przekazana parametrem, więc wynik jest przewidywalny: 23.11.2026 + 7 dni = 30.11.2026.",
        "`strftime(\"%d.%m.%Y\")` — format polski.",
        "`strptime` zamienia napis na datę; różnica dat `.days` → 31."],
        "wynik": "Trzy wylosowane produkty (te same przy każdym uruchomieniu z seed), liczba z kostki, „Termin: 30.11.2026”, „Dni do Wigilii: 31”."},
    jak_uruchomic=["Zapisz jako losowanie_demo.py → ▶ Uruchom dwa razy — porównaj wyniki z seed i bez seed."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór `termin`: start = date(2026, 1, 28). Podaj datę w formacie DD.MM.RRRR dla: (1) termin(start) (7 dni), (2) termin(start, 30), (3) liczbę dni między date(2026, 3, 1) a date(2026, 2, 1). Czas: 15 minut.",
          "(1) 04.02.2026; (2) 27.02.2026; (3) 28.",
          ["Styczeń ma 31 dni.", "28.01 + 30 dni: 3 dni do końca stycznia + 27.", "Luty 2026 nie jest przestępny."],
          "(1) 28.01 + 7 = 04.02.2026; (2) 28.01 + 30 = 27.02.2026; (3) luty 2026 ma 28 dni → 28.",
          [tx("a", "(1) termin(start)", "04.02.2026"), tx("b", "(2) termin(start, 30)", "27.02.2026"), li("c", "(3) Liczba dni", 28)]),
        C("samodzielne",
          "Test: `def test_losowanie(): assert wybierz_3(produkty) == [\"klej\", \"blok\", \"zeszyt\"]` — raz przechodzi, raz nie. (1) Dlaczego (wybierz)? (2) Jaką linię dodasz w teście przed losowaniem, żeby wynik był powtarzalny (wpisz z dowolną liczbą, np. 1)? (3) Które losowanie gwarantuje brak powtórzeń: choice 3 razy / sample(…, 3)? Czas: 15 minut.",
          "(1) losowanie bez ziarna; (2) random.seed(1); (3) sample.",
          ["Co sprawia, że random daje te same wyniki?", "Ziarno ustawiasz przed losowaniem.", "choice może trafić dwa razy w to samo."],
          "(1) losowość bez seed — test niepowtarzalny (flaky); (2) `random.seed(1)` (wartość dowolna, byle stała) i oczekiwany wynik dopasowany do tego ziarna; (3) sample.",
          [wy("a", "(1) Przyczyna", ["losowanie bez ziarna", "błąd Pythona", "zła lista", "wolny komputer"], "losowanie bez ziarna"), tx("b", "(2) Linia", "random.seed(1)", zawiera=["random.seed("]),
           wy("c", "(3) Bez powtórzeń", ["choice 3 razy", "sample(…, 3)"], "sample(…, 3)")]),
    ],
    typowe_bledy=[
        B("AttributeError: module 'datetime' has no attribute 'today'", "`import datetime`, a potem `datetime.today()` (moduł, nie klasa).", "Jak zaimportowałeś?", "`datetime.date.today()` albo `from datetime import date` → `date.today()`."),
        B("ValueError: time data '2026-12-24' does not match format '%d.%m.%Y'", "Format w strptime nie pasuje do napisu.", "Porównaj znak po znaku.", "Dopasuj format: \"%Y-%m-%d\" dla 2026-12-24."),
        B("Test raz zielony, raz czerwony (flaky)", "Losowość albo date.today() w testowanej funkcji.", "Uruchom test 5 razy.", "random.seed(...) albo data przekazana parametrem."),
    ],
    pulapki=["Nazwanie własnego pliku random.py albo datetime.py — import weźmie Twój plik zamiast modułu.", "randint(1, 6) włącza 6, a range(1, 6) — nie."],
    zadania=["Wylosuj 3 produkty do inwentaryzacji i wypisz datę kontroli za 7 dni.", "Funkcja dni_do(data_docelowa, od) z testowalną datą.", "Sprawdź, czy wynik losowania z seed jest stały."],
    pytania=[["Po co random.seed?", "Żeby losowanie było powtarzalne (testy, odtwarzanie błędu)."], ["Jak dodać 7 dni do daty?", "data + timedelta(days=7)."], ["Jak zamienić datę na napis 23.11.2026?", "data.strftime(\"%d.%m.%Y\")."]],
    podsumowanie="Importujesz moduły, losujesz powtarzalnie (seed), liczysz terminy na datach i piszesz funkcje z datą w parametrze — testowalne.",
    test=[T("random.randint(1, 3) może zwrócić:", ["tylko 1 lub 2", "1, 2 lub 3", "0–3", "liczbę z kropką"], 1, "Obie granice włącznie."),
          T("date(2026, 1, 31) + timedelta(days=1):", ["2026-01-32", "2026-02-01", "błąd", "2026-01-30"], 1, "Przejście na luty."),
          T("Powtarzalne losowanie zapewnia:", ["random.repeat()", "random.seed(stała)", "import random dwa razy", "sample"], 1, "Ziarno."),
          T("sample(lista, 2):", ["może powtórzyć element", "2 różne elementy", "sortuje", "usuwa 2 elementy"], 1, "Bez powtórzeń.")],
    w_praktyce=["Dane losowe w testach zawsze z seed, a seed zapisany w raporcie.", "Daty graniczne do testów: 28/29 lutego, 31 grudnia, przejście czasu letniego."],
    zrodla=[Z.PY_RANDOM, Z.PY_DATETIME, Z.PY_TUT_MOD],
)

POWTORKA1 = L(
    id="powtorka_podstawy", nazwa="Powtórka etapu 1: podstawy Pythona w jednym programie", tydzien=3,
    slowa=["powtórka", "etap 1", "menu", "program konsolowy", "lista słowników", "funkcje", "walidacja", "plan programu"],
    cel="Po tej lekcji łączysz wszystkie podstawy (typy, warunki, pętle, listy, słowniki, funkcje, wyjątki) w program z menu, rozbijasz go na funkcje i sprawdzasz, które tematy etapu 1 musisz powtórzyć.",
    po_co="Na rozmowie Junior QA dostaniesz małe zadanie z kodem: przeczytaj, znajdź błąd, dopisz warunek. To są dokładnie podstawy z tego etapu — połączone.",
    wymagania=["Wszystkie lekcje tygodni 1–3.", "Wyniki quizów tygodni 1–3 (Statystyki)."],
    wyjasnienie=(
        "## Mapa etapu 1\n"
        "| temat | kluczowa umiejętność | typowy błąd |\n|---|---|---|\n"
        "| zmienne, typy | int/float/str/bool, rzutowanie | \"5\" + 5 |\n"
        "| input/print | input zawsze str | brak int() |\n"
        "| warunki | kolejność progów, granice | >= vs > |\n"
        "| pętle | akumulator przed pętlą | pętla nieskończona |\n"
        "| listy | indeks od 0, pusta lista | IndexError |\n"
        "| napisy | metody zwracają nowy napis | brak przypisania |\n"
        "| funkcje | return, blok main | None zamiast wyniku |\n"
        "| słowniki | get, items, lista słowników | KeyError |\n"
        "| wyjątki | konkretne except, raise | except: pass |\n"
        "| random/datetime | seed, timedelta | test flaky |\n"
        "## Jak zaplanować program z menu\n"
        "1. Dane: jak je trzymasz? (lista słowników `{\"tytul\": …, \"zrobione\": False}`).\n"
        "2. Operacje: każda jako funkcja **bez input()** — dostaje dane parametrami, zwraca wynik (dodaj, oznacz, usuń, lista otwartych).\n"
        "3. Menu: pętla `while True` w bloku main — tylko tu input() i print().\n"
        "4. Złe dane: nieznana opcja, numer spoza listy, pusty tytuł — każda funkcja rzuca ValueError, menu łapie i wypisuje komunikat.\n"
        "## Samoocena\n"
        "Napisz z pamięci (bez patrzenia w lekcje) funkcję, która z listy słowników zwraca te z ceną poniżej progu. Jeśli w 15 minut nie dasz rady — wróć do lekcji „Słowniki” i „Funkcje”."),
    przyklad=kod("powtorka_podstawy", (
        "def dodaj(zadania, tytul):\n"
        "    tytul = tytul.strip()\n"
        "    if not tytul:\n"
        "        raise ValueError(\"tytuł nie może być pusty\")\n"
        "    zadania.append({\"tytul\": tytul, \"zrobione\": False})\n\n\n"
        "def oznacz(zadania, nr):\n"
        "    if not 1 <= nr <= len(zadania):\n"
        "        raise ValueError(f\"nie ma zadania nr {nr}\")\n"
        "    zadania[nr - 1][\"zrobione\"] = True\n\n\n"
        "def otwarte(zadania):\n"
        "    return [z[\"tytul\"] for z in zadania if not z[\"zrobione\"]]\n\n\n"
        "lista = []\n"
        "dodaj(lista, \"Zamówić papier\")\n"
        "dodaj(lista, \"  Policzyć zeszyty \")\n"
        "oznacz(lista, 1)\n"
        "print(otwarte(lista))\n"
        "for blad in [lambda: dodaj(lista, \"   \"), lambda: oznacz(lista, 5)]:\n"
        "    try:\n"
        "        blad()\n"
        "    except ValueError as e:\n"
        "        print(\"Błąd:\", e)\n"), "['Policzyć zeszyty']\nBłąd: tytuł nie może być pusty\nBłąd: nie ma zadania nr 5\n"),
    demonstracja={"tytul": "Szkielet menedżera zadań: funkcje bez input()", "kroki": [
        "`dodaj` — strip() i walidacja pustego tytułu (raise), dopisanie słownika do listy.",
        "`oznacz` — numer dla człowieka od 1, indeks od 0: stąd `nr - 1`; zakres sprawdzony `1 <= nr <= len(zadania)`.",
        "`otwarte` — lista tytułów niezrobionych zadań. Zapis `[z[\"tytul\"] for z in zadania if not z[\"zrobione\"]]` to **lista składana**: krótsza wersja pętli for z append.",
        "Wywołania: dwa zadania, pierwsze oznaczone → otwarte: ['Policzyć zeszyty'] (spacje usunięte).",
        "Dwa przypadki negatywne w try/except — dokładnie tak sprawdza je weryfikator zadania t3z5.",
        "`lambda: …` — mała funkcja bez nazwy; tu tylko po to, żeby wywołać błąd w pętli. Nie musisz jej jeszcze używać sam."],
        "wynik": "„['Policzyć zeszyty']” i dwa komunikaty błędów."},
    jak_uruchomic=["Zapisz jako szkielet.py → ▶ Uruchom.", "Dopisz menu w bloku `if __name__ == \"__main__\":` z pętlą while True i opcjami 1–4, 0 = koniec."],
    cwiczenia=[
        C("prowadzone",
          "Dla `lista` z demonstracji po wywołaniach: (1) ile elementów ma lista? (2) jaka jest wartość `lista[0][\"zrobione\"]`? (3) co zwróci `otwarte(lista)` po dodatkowym `oznacz(lista, 2)`? (4) jaki wyjątek rzuci `oznacz(lista, 0)`? Czas: 15 minut.",
          "(1) 2; (2) True; (3) []; (4) ValueError.",
          ["Pusty tytuł nie został dodany (raise przed append).", "Zadanie 1 oznaczone.", "Zakres 1…len — 0 jest poza."],
          "(1) 2 zadania; (2) True; (3) [] — oba zrobione; (4) ValueError: nie ma zadania nr 0.",
          [li("a", "(1) Liczba zadań", 2, bledy=[bl(3, "pusty tytuł rzucił ValueError PRZED append — nie trafił do listy")]), wy("b", "(2) lista[0][\"zrobione\"]", ["True", "False"], "True"), tx("c", "(3) otwarte()", "[]"),
           wy("d", "(4) oznacz(lista, 0)", ["IndexError", "ValueError", "nic", "KeyError"], "ValueError")]),
        C("samodzielne",
          "Napisz funkcję `def usun(zadania, nr):` (bez input), która usuwa zadanie o numerze nr (od 1) i zwraca jego tytuł; dla złego numeru — ValueError. Dla listy [\"A\", \"B\", \"C\"] (jako słowniki) podaj: (1) co zwróci usun(…, 2), (2) ile zostanie zadań, (3) jaki tytuł ma teraz zadanie nr 2. Czas: 20 minut.",
          "(1) B; (2) 2; (3) C.",
          ["Indeks = nr - 1.", "pop(indeks) usuwa i zwraca element.", "Po usunięciu elementy się przesuwają."],
          "`if not 1 <= nr <= len(zadania): raise ValueError(...)`; `return zadania.pop(nr - 1)[\"tytul\"]`. Wynik: (1) „B”; (2) 2; (3) „C” — elementy przesunęły się w lewo.",
          [tx("a", "(1) Zwrócony tytuł", "B"), li("b", "(2) Zostało zadań", 2), tx("c", "(3) Tytuł nr 2", "C", bledy=[bl("B", "po usunięciu B lista przesuwa się — nr 2 to teraz C")])]),
    ],
    typowe_bledy=[
        B("IndexError przy oznaczaniu ostatniego zadania", "Numer od 1 użyty jako indeks od 0.", "Wypisz nr i len(lista).", "Indeks = nr - 1, zakres 1 ≤ nr ≤ len."),
        B("Menu kończy się po pierwszym błędnym wpisie", "Brak try/except wokół int(input()).", "Wpisz „x” jako opcję.", "try/except ValueError w pętli menu."),
    ],
    pulapki=["Funkcje z input() w środku — nie da się ich przetestować; input tylko w menu.", "Jedna wielka funkcja main na 100 linii — dziel na funkcje po 5–15 linii."],
    zadania=["Menedżer zadań w konsoli: menu w pętli, każda operacja funkcją, lista słowników.", "Powtórz lekcje z czerwonymi quizami.", "Napisz z pamięci filtr produktów poniżej progu ceny."],
    pytania=[["Dlaczego funkcje menedżera nie używają input()?", "Żeby dało się je testować i używać w innym interfejsie (np. web)."],
             ["Jak zamienić numer zadania na indeks?", "indeks = nr - 1."], ["Co robi lista składana [x for x in l if w]?", "Buduje nową listę z elementów spełniających warunek."]],
    podsumowanie="Łączysz podstawy w program z menu, rozdzielasz logikę od rozmowy z użytkownikiem, walidujesz dane wyjątkami i wiesz, co powtórzyć przed etapem 2.",
    test=[T("Numer zadania 3 to indeks:", ["3", "2", "4", "-3"], 1, "Od zera."),
          T("Gdzie input() w programie z menu?", ["w każdej funkcji", "tylko w pętli menu (blok main)", "w testach", "nigdzie"], 1, "Logika bez input()."),
          T("[x * 2 for x in [1, 2, 3]] to:", ["[1, 2, 3]", "[2, 4, 6]", "6", "12"], 1, "Lista składana."),
          T("lista.pop(0) zwraca:", ["None", "pierwszy element (i go usuwa)", "długość", "ostatni element"], 1, "Usuwa i zwraca.")],
    w_praktyce=["Przed kodowaniem: na kartce dane + lista funkcji + przypadki złych danych.", "Zadanie rekrutacyjne: najpierw przeczytaj kod na głos, potem zmieniaj."],
    zrodla=[Z.PY_TUT_DS, Z.PY_TUT_CTRL, Z.PY_TUT_ERR],
)
