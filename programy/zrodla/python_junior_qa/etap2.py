# -*- coding: utf-8 -*-
"""Etap 2, tygodnie 4–6: pliki i CSV, Git w zespole (gałęzie, pull request, cofanie), klasy, moduły, venv i pip, requests i API,
debugowanie, README i refaktoryzacja, powtórka etapu."""

from wspolne import B, C, L, T, bl, kod, kw, li, tx, wy
import zrodla as Z

# =========================================================================== TYDZIEŃ 4
PLIKI = L(
    id="pliki", nazwa="Pliki: open, read, write, with i kodowanie utf-8", tydzien=4,
    slowa=["plik", "open", "read", "write", "with", "tryb", "r", "w", "a", "encoding", "utf-8", "readlines", "Path", "FileNotFoundError"],
    cel="Po tej lekcji zapisujesz i odczytujesz pliki tekstowe (tryby r, w, a) w bloku with z encoding=\"utf-8\", czytasz plik linia po linii i obsługujesz brak pliku.",
    po_co="Dane testowe, logi i raporty to pliki. Tester czyta logi aplikacji, a skrypty testowe zapisują wyniki do plików.",
    wymagania=["Lekcje etapu 1, zwłaszcza „Napisy” (strip, split) i „Obsługa błędów”."],
    wyjasnienie=(
        "## Otwieranie pliku\n"
        "`open(\"produkty.txt\", \"w\", encoding=\"utf-8\")` — nazwa, **tryb** i kodowanie znaków. Tryby: `\"r\"` czytanie (domyślny; brak pliku → FileNotFoundError), `\"w\"` zapis (tworzy plik albo **kasuje** jego zawartość!), `\"a\"` dopisywanie na końcu.\n"
        "## Zawsze with\n"
        "```\nwith open(\"produkty.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"zeszyt\\n\")\n```\n"
        "Blok with sam zamyka plik po wyjściu — także gdy wystąpi błąd. Bez zamknięcia zapis może nie trafić na dysk.\n"
        "## Kodowanie utf-8\n"
        "Polskie litery w Windows bez `encoding=\"utf-8\"` mogą zamienić się w „krzaki” albo dać UnicodeDecodeError. Od Pythona 3.15 utf-8 jest domyślne (PEP 686), ale kurs używa 3.11–3.13 — pisz encoding zawsze; to też dobry nawyk dla czytelności.\n"
        "## Czytanie\n"
        "- `f.read()` — cały plik jako jeden napis;\n"
        "- `for linia in f:` — linia po linii (oszczędza pamięć); każda linia kończy się `\\n`, więc `linia.strip()`;\n"
        "- `f.readlines()` — lista linii.\n"
        "## write nie dodaje nowej linii\n"
        "`f.write(\"a\")` dwa razy da „aa”. Nową linię dopisujesz sam: `f.write(tekst + \"\\n\")`. write przyjmuje tylko str — liczbę zamień `str(liczba)`.\n"
        "## Ścieżki\n"
        "Względna nazwa (`\"produkty.txt\"`) oznacza plik w **katalogu roboczym** (tam, skąd uruchomiono program). `from pathlib import Path` daje wygodne operacje: `Path(\"dane\") / \"produkty.csv\"`, `.exists()`, `.read_text(encoding=\"utf-8\")`."),
    przyklad=kod("pliki", (
        "from pathlib import Path\n\n"
        "produkty = [\"Zeszyt A5\", \"Długopis niebieski\", \"Gumka\"]\n"
        "with open(\"produkty.txt\", \"w\", encoding=\"utf-8\") as f:\n"
        "    for p in produkty:\n"
        "        f.write(p + \"\\n\")\n"
        "with open(\"produkty.txt\", \"a\", encoding=\"utf-8\") as f:\n"
        "    f.write(\"Klej w sztyfcie\\n\")\n"
        "with open(\"produkty.txt\", encoding=\"utf-8\") as f:\n"
        "    for nr, linia in enumerate(f, 1):\n"
        "        print(nr, linia.strip())\n"
        "print(\"Linii:\", len(Path(\"produkty.txt\").read_text(encoding=\"utf-8\").splitlines()))\n"
        "try:\n"
        "    open(\"brak.txt\", encoding=\"utf-8\")\n"
        "except FileNotFoundError:\n"
        "    print(\"Nie ma pliku brak.txt\")\n"
        "Path(\"produkty.txt\").unlink()\n"), "1 Zeszyt A5\n2 Długopis niebieski\n3 Gumka\n4 Klej w sztyfcie\nLinii: 4\nNie ma pliku brak.txt\n"),
    demonstracja={"tytul": "Zapis, dopisanie i odczyt listy produktów", "kroki": [
        "Tryb `\"w\"` tworzy produkty.txt (albo czyści istniejący) i zapisuje 3 linie — `+ \"\\n\"` w każdej.",
        "Tryb `\"a\"` dopisuje czwartą linię na końcu, nie kasując poprzednich.",
        "Odczyt: `for nr, linia in enumerate(f, 1)` — enumerate numeruje od 1; `linia.strip()` usuwa `\\n`.",
        "`Path(...).read_text(...).splitlines()` — cały plik naraz i podział na linie: 4.",
        "`open(\"brak.txt\")` w trybie r → FileNotFoundError, złapany except.",
        "`unlink()` usuwa plik — przykład sprząta po sobie (w zadaniu plik zostaw!).",
        "Zmień `\"a\"` na `\"w\"` w drugim bloku i przewidź wynik: zostanie tylko „Klej w sztyfcie”."],
        "wynik": "4 ponumerowane produkty, „Linii: 4”, „Nie ma pliku brak.txt”."},
    jak_uruchomic=["Zapisz jako pliki_demo.py w PRACA → ▶ Uruchom.", "Usuń ostatnią linię (unlink) i otwórz produkty.txt w Eksploratorze — sprawdź polskie litery."],
    cwiczenia=[
        C("prowadzone",
          "Plik `stan.txt` zawiera 3 linie: „10”, „25”, „5”. Kod: `with open(\"stan.txt\", encoding=\"utf-8\") as f: suma = sum(int(l) for l in f)`. (1) Ile wynosi suma? (2) Co będzie w pliku po `open(\"stan.txt\", \"w\", encoding=\"utf-8\").write(\"7\")`? (3) Ile linii będzie po kolejnym `with open(\"stan.txt\", \"a\", encoding=\"utf-8\") as f: f.write(\"\\n8\")`? Czas: 15 minut.",
          "(1) 40; (2) tylko 7; (3) 2 linie.",
          ["int() radzi sobie z \"10\\n\" — ignoruje końcową nową linię.", "Tryb w kasuje zawartość.", "\\n przed 8 zaczyna nową linię."],
          "(1) 10 + 25 + 5 = 40; (2) tryb w skasował wszystko → „7”; (3) „7\\n8” = 2 linie.",
          [li("a", "(1) Suma", 40), tx("b", "(2) Zawartość pliku", "7", bledy=[bl("10 25 5 7", "tryb \"w\" najpierw CZYŚCI plik")]), li("c", "(3) Liczba linii", 2)]),
        C("samodzielne",
          "Raport zapisuje się tak: `f = open(\"raport.txt\", \"w\")` / `f.write(\"Razem: \" + 123.5)` / (brak close). Wskaż: (1) jaki błąd rzuci druga linia (wybierz), (2) czego brakuje w pierwszej linii, żeby polskie litery zawsze działały (wpisz argument), (3) jak bezpiecznie zamknąć plik — wybierz: f.close() na końcu / blok with. Czas: 15 minut.",
          "(1) TypeError; (2) encoding=\"utf-8\"; (3) blok with.",
          ["write przyjmuje tylko str.", "Argument z nazwą kodowania.", "Co się stanie, gdy błąd wystąpi przed f.close()?"],
          "(1) TypeError: can only concatenate str (not \"float\") — `str(123.5)` albo f-string; (2) `encoding=\"utf-8\"`; (3) `with open(...) as f:` zamyka plik nawet przy błędzie.",
          [wy("a", "(1) Błąd", ["ValueError", "TypeError", "FileNotFoundError", "brak błędu"], "TypeError"), tx("b", "(2) Brakujący argument", "encoding=\"utf-8\"", zawiera=["encoding", "utf-8"]),
           wy("c", "(3) Bezpieczne zamknięcie", ["f.close() na końcu", "blok with"], "blok with")]),
    ],
    typowe_bledy=[
        B("FileNotFoundError: [Errno 2] No such file or directory: 'dane.csv'", "Plik w innym katalogu niż katalog roboczy.", "`import os; print(os.getcwd())` i `ls`.", "Uruchom z katalogu z plikiem albo podaj ścieżkę Path(__file__).parent / \"dane.csv\"."),
        B("UnicodeDecodeError: 'charmap' codec can't decode byte…", "Plik utf-8 czytany domyślnym kodowaniem Windows.", "Czy jest encoding=\"utf-8\"?", "open(…, encoding=\"utf-8\")."),
        B("Plik pusty po uruchomieniu", "Tryb \"w\" przy każdym uruchomieniu kasuje dane / plik nie zamknięty.", "Który tryb? Czy jest with?", "\"a\" do dopisywania; zawsze with."),
    ],
    pulapki=["Tryb w na pliku z danymi — jedno uruchomienie i dane znikają; rób kopię przed eksperymentem.", "Nazwy plików z polskimi znakami i spacjami działają, ale w projektach używaj prostych nazw."],
    zadania=["Zapisz listę produktów do produkty.txt i odczytaj ją z numerami.", "Zrób to samo raz bez with i raz z with — zanotuj różnicę.", "Obsłuż brak pliku komunikatem."],
    pytania=[["Co robi tryb \"w\" z istniejącym plikiem?", "Kasuje jego zawartość i zapisuje od nowa."], ["Dlaczego with?", "Zamyka plik automatycznie, także przy błędzie."], ["Po co encoding=\"utf-8\"?", "Żeby polskie znaki zapisywały się i czytały poprawnie w Windows."]],
    podsumowanie="Zapisujesz, dopisujesz i czytasz pliki w bloku with z utf-8, czytasz linia po linii i obsługujesz brak pliku.",
    test=[T("Tryb dopisywania na końcu pliku:", ["r", "w", "a", "x"], 2, "append."),
          T("f.write(5) rzuci:", ["nic", "TypeError", "ValueError", "IOError"], 1, "write przyjmuje str."),
          T("for linia in f: — każda linia kończy się:", ["spacją", "\\n (oprócz ewentualnie ostatniej)", "przecinkiem", "niczym"], 1, "Stąd strip()."),
          T("Plik względny \"dane.txt\" jest szukany:", ["na pulpicie", "w katalogu roboczym", "w folderze Pythona", "w internecie"], 1, "Katalog, z którego uruchomiono program.")],
    w_praktyce=["Testy zapisujące pliki używają katalogu tymczasowego (tmp_path w pytest, tydzień 7).", "Logi aplikacji czytasz od końca — najnowsze wpisy są na dole."],
    zrodla=[Z.PY_TUT_IO, Z.PY_TUT_ERR],
)

CSV = L(
    id="csv", nazwa="Moduł csv: DictReader, DictWriter i statystyki z pliku", tydzien=4,
    slowa=["csv", "DictReader", "DictWriter", "reader", "writer", "nagłówek", "separator", "delimiter", "newline", "średnia", "filtr"],
    cel="Po tej lekcji czytasz plik CSV jako listę słowników (DictReader), zamieniasz pola na liczby, liczysz statystyki (suma, średnia, maksimum, filtr) i zapisujesz CSV (DictWriter) z newline=\"\".",
    po_co="Eksporty z systemów, dane testowe i raporty to najczęściej CSV. Tester porównuje eksport z oczekiwanym — i sprawdza separator, polskie znaki i puste pola.",
    wymagania=["Lekcje „Pliki” i „Słowniki”.", "Plik dane/produkty.csv z paczki kursu (Mój projekt → „Skopiuj materiały kursu tutaj”)."],
    wyjasnienie=(
        "## Czym jest CSV\n"
        "Tekst, w którym każda linia to wiersz tabeli, a pola rozdziela przecinek (albo średnik — polski Excel często zapisuje średnikiem). Pierwsza linia to zwykle **nagłówek**:\n"
        "```\nid,nazwa,kategoria,cena,ilosc\n1,Zeszyt A5 w kratkę,zeszyty,4.50,120\n```\n"
        "## DictReader — wiersz jako słownik\n"
        "```\nimport csv\nwith open(\"dane/produkty.csv\", encoding=\"utf-8\", newline=\"\") as f:\n    wiersze = list(csv.DictReader(f))\n```\n"
        "Każdy wiersz to słownik `{\"id\": \"1\", \"nazwa\": \"Zeszyt…\", \"cena\": \"4.50\", …}` — **wszystkie wartości są napisami**; liczby zamieniasz `float(w[\"cena\"])`, `int(w[\"ilosc\"])`. "
        "Separator inny niż przecinek: `csv.DictReader(f, delimiter=\";\")`.\n"
        "## Dlaczego csv, a nie split(\",\")\n"
        "Nazwa „Papier, 500 ark.” w cudzysłowie zawiera przecinek — moduł csv rozumie cudzysłowy, split nie.\n"
        "## Zapis — DictWriter\n"
        "```\nwith open(\"raport.csv\", \"w\", encoding=\"utf-8\", newline=\"\") as f:\n    w = csv.DictWriter(f, fieldnames=[\"nazwa\", \"wartosc\"])\n    w.writeheader()\n    w.writerow({\"nazwa\": \"Zeszyt\", \"wartosc\": 540.0})\n```\n"
        "`newline=\"\"` — bez tego w Windows pojawiają się puste linie co drugi wiersz.\n"
        "## Statystyki\n"
        "Suma: akumulator w pętli albo `sum(float(w[\"cena\"]) for w in wiersze)`. Średnia: suma / len (pilnuj pustej listy). Maksimum: `max(wiersze, key=lambda w: float(w[\"cena\"]))`. Filtr: lista składana z warunkiem."),
    przyklad=kod("csv", (
        "import csv\n"
        "import io\n\n"
        "DANE = \"\"\"id,nazwa,kategoria,cena,ilosc\n"
        "1,Zeszyt A5 w kratkę,zeszyty,4.50,120\n"
        "3,Długopis niebieski,pisaki,2.30,300\n"
        "9,\"Papier ksero A4, 500 ark.\",papier,24.99,35\n"
        "17,Zszywki 1000 szt.,biuro,3.90,0\n"
        "\"\"\"\n"
        "wiersze = list(csv.DictReader(io.StringIO(DANE)))\n"
        "print(\"Produktów:\", len(wiersze), \"| pierwszy:\", wiersze[0][\"nazwa\"])\n"
        "ceny = [float(w[\"cena\"]) for w in wiersze]\n"
        "print(f\"Średnia cena: {sum(ceny) / len(ceny):.2f}\")\n"
        "najdrozszy = max(wiersze, key=lambda w: float(w[\"cena\"]))\n"
        "print(\"Najdroższy:\", najdrozszy[\"nazwa\"])\n"
        "brak = [w[\"nazwa\"] for w in wiersze if int(w[\"ilosc\"]) == 0]\n"
        "print(\"Brak na stanie:\", brak)\n"
        "wartosc = sum(float(w[\"cena\"]) * int(w[\"ilosc\"]) for w in wiersze)\n"
        "print(f\"Wartość magazynu: {wartosc:.2f} zł\")\n"
        "wyjscie = io.StringIO()\n"
        "pisarz = csv.DictWriter(wyjscie, fieldnames=[\"nazwa\", \"wartosc\"], lineterminator=\"\\n\")\n"
        "pisarz.writeheader()\n"
        "pisarz.writerow({\"nazwa\": \"Zeszyt A5 w kratkę\", \"wartosc\": 540.0})\n"
        "print(wyjscie.getvalue(), end=\"\")\n"), (
        "Produktów: 4 | pierwszy: Zeszyt A5 w kratkę\nŚrednia cena: 8.92\nNajdroższy: Papier ksero A4, 500 ark.\nBrak na stanie: ['Zszywki 1000 szt.']\n"
        "Wartość magazynu: 2104.65 zł\nnazwa,wartosc\nZeszyt A5 w kratkę,540.0\n")),
    demonstracja={"tytul": "Statystyki magazynu z CSV", "kroki": [
        "`DANE` — fragment pliku dane/produkty.csv wpisany w kod, żeby przykład działał bez pliku; `io.StringIO(DANE)` udaje otwarty plik. W zadaniu użyjesz `open(\"dane/produkty.csv\", encoding=\"utf-8\", newline=\"\")`.",
        "`list(csv.DictReader(...))` — 4 słowniki; klucze z nagłówka.",
        "Wiersz 9 ma nazwę w cudzysłowie z przecinkiem — csv poprawnie czyta „Papier ksero A4, 500 ark.” jako jedno pole.",
        "`[float(w[\"cena\"]) for w in wiersze]` — lista cen jako liczby; średnia (4.50 + 2.30 + 24.99 + 3.90) / 4 = 8.92.",
        "`max(..., key=lambda w: float(w[\"cena\"]))` — porównanie jako liczb. Bez float porównałbyś napisy: „4.50” > „24.99”!",
        "Filtr: produkty z ilością 0.",
        "Wartość magazynu: suma cena × ilość = 4.50×120 + 2.30×300 + 24.99×35 + 3.90×0 = 540 + 690 + 874.65 + 0 = 2104.65 zł.",
        "DictWriter: nagłówek + wiersz; `lineterminator=\"\\n\"` tylko dla StringIO — przy pliku wystarczy newline=\"\"."],
        "wynik": "Liczba produktów, średnia 8.92, najdroższy papier, lista braków, wartość magazynu i 2 linie CSV z DictWriter."},
    jak_uruchomic=["Zapisz jako csv_demo.py → ▶ Uruchom.", "Wersja z plikiem: Mój projekt → „Skopiuj materiały kursu tutaj” → w PRACA jest dane/produkty.csv → zamień StringIO na open(...)."],
    cwiczenia=[
        C("prowadzone",
          "Plik: nagłówek `nazwa,cena,ilosc` i wiersze `Klej,3.40,110`, `Nożyczki,8.90,30`, `Zszywacz,19.90,15`. Na wzór demonstracji policz: (1) liczbę wierszy danych (bez nagłówka), (2) średnią cenę z 2 miejscami, (3) nazwę produktu o najmniejszej ilości, (4) wartość magazynu (cena × ilość, suma). Czas: 20 minut.",
          "(1) 3; (2) 10.73; (3) Zszywacz; (4) 940.50.",
          ["DictReader nie liczy nagłówka jako wiersza.", "(3.40 + 8.90 + 19.90) / 3.", "374 + 267 + 298.50."],
          "(1) 3; (2) 32.20 / 3 = 10.73; (3) Zszywacz (15); (4) 3.40×110 = 374 + 8.90×30 = 267 + 19.90×15 = 298.50 → 940.50.",
          [li("a", "(1) Wiersze danych", 3, bledy=[bl(4, "nagłówek to nie wiersz danych — DictReader go pomija")]), kw("b", "(2) Średnia cena", 10.73), tx("c", "(3) Najmniej sztuk", "Zszywacz"), kw("d", "(4) Wartość magazynu", 940.50)]),
        C("samodzielne",
          "Kolega liczy maksimum: `max(wiersze, key=lambda w: w[\"cena\"])` dla cen „4.50”, „24.99”, „7.50”. (1) Który produkt wskaże (podaj cenę)? (2) Dlaczego (wybierz)? (3) Jak poprawić key (wpisz)? Czas: 15 minut.",
          "(1) 7.50; (2) porównuje napisy znak po znaku; (3) key=lambda w: float(w[\"cena\"]).",
          ["Napisy porównuje się jak w słowniku — od pierwszego znaku.", "„7” > „4” > „2”.", "Zamień na liczbę w key."],
          "(1) „7.50” — jako napis zaczyna się od 7, największego pierwszego znaku; (2) porównanie napisów; (3) `key=lambda w: float(w[\"cena\"])` → 24.99.",
          [tx("a", "(1) Wskazana cena", "7.50", bledy=[bl("24.99", "to poprawna odpowiedź po zamianie na float — napisy porównują się inaczej")]),
           wy("b", "(2) Przyczyna", ["porównuje napisy znak po znaku", "błąd modułu csv", "zaokrąglenie", "kolejność wierszy"], "porównuje napisy znak po znaku"),
           tx("c", "(3) Poprawione key", "key=lambda w: float(w[\"cena\"])", zawiera=["float", "cena"])]),
    ],
    typowe_bledy=[
        B("KeyError: 'cena'", "Separator ; w pliku — DictReader widzi jeden klucz „nazwa;cena;ilosc”; albo literówka/BOM w nagłówku.", "`print(wiersze[0].keys())`.", "`delimiter=\";\"`; plik z Excela zapisuj jako CSV UTF-8 i otwieraj encoding=\"utf-8-sig\"."),
        B("ValueError: could not convert string to float: '4,50'", "Przecinek dziesiętny z polskiego Excela.", "`print(repr(w[\"cena\"]))`.", "`float(w[\"cena\"].replace(\",\", \".\"))`."),
        B("Puste linie między wierszami w zapisanym CSV", "Brak newline=\"\" przy zapisie w Windows.", "Otwórz plik w Notatniku.", "open(…, \"w\", encoding=\"utf-8\", newline=\"\")."),
    ],
    pulapki=["Wartości z CSV to napisy — porównania i sortowanie bez float/int dają złe wyniki.", "Puste pole (`,,`) to pusty napis \"\" — float(\"\") → ValueError; obsłuż je."],
    zadania=["Wczytaj dane/produkty.csv i policz średnią cenę.", "Lista produktów z ilością 0.", "Zapisz raport wartości magazynu do raport.csv."],
    pytania=[["Jakiego typu są wartości z DictReader?", "Napisy (str)."], ["Po co newline=\"\" przy zapisie?", "Żeby w Windows nie było pustych linii."], ["Jak czytać CSV ze średnikami?", "csv.DictReader(f, delimiter=\";\")."]],
    podsumowanie="Czytasz CSV jako listę słowników, zamieniasz pola na liczby, liczysz statystyki i filtry oraz zapisujesz raport DictWriter.",
    test=[T("DictReader zwraca wiersz jako:", ["listę", "słownik", "krotkę", "napis"], 1, "Klucze z nagłówka."),
          T("float(\"4,50\") daje:", ["4.5", "ValueError", "450", "4"], 1, "Python wymaga kropki."),
          T("\"7.50\" > \"24.99\" (napisy):", ["True", "False", "błąd", "None"], 0, "Porównanie znak po znaku."),
          T("Plik z polskiego Excela ze średnikami czytasz z:", ["delimiter=\";\"", "sep=\";\"", "split(\";\")", "nic nie trzeba"], 0, "Argument delimiter.")],
    w_praktyce=["Testując eksport CSV: separator, kodowanie, polskie znaki, liczby z przecinkiem, puste pola.", "Dane testowe w CSV — łatwo dopisać nowy przypadek bez zmiany kodu."],
    zrodla=[Z.PY_CSV, Z.PY_TUT_IO],
)

GIT = L(
    id="git", nazwa="Git w zespole: gałęzie, diff, log, cofanie zmian i pull request", tydzien=4,
    slowa=["gałąź", "branch", "switch", "merge", "diff", "log", "restore", "stash", "revert", "pull request", "PR", "konflikt", "code review"],
    cel="Po tej lekcji pracujesz na gałęzi (git switch -c), przeglądasz zmiany (git diff, git log), cofasz zmiany w pliku (git restore), odkładasz je (git stash), scalasz gałąź i otwierasz pull request na GitHubie.",
    po_co="W zespole nikt nie pracuje bezpośrednio na main. Tester recenzuje pull requesty, uruchamia testy na gałęzi i zgłasza uwagi przed scaleniem.",
    wymagania=["Lekcja „Git i GitHub — pierwszy commit”.", "Repozytorium w PRACA wysłane na GitHub."],
    wyjasnienie=(
        "## Gałąź\n"
        "Gałąź to osobna linia zmian. Na main jest działająca wersja; nową funkcję robisz na gałęzi `feature/csv`, a po sprawdzeniu scalasz. `git switch -c feature/csv` tworzy gałąź i przechodzi na nią; `git switch main` wraca; `git branch` pokazuje listę (gwiazdka = bieżąca).\n"
        "## Co się zmieniło\n"
        "- `git diff` — zmiany niezacommitowane, linia po linii: `-` usunięte, `+` dodane;\n"
        "- `git diff --staged` — zmiany w poczekalni;\n"
        "- `git log --oneline --graph --all` — historia wszystkich gałęzi w skrócie.\n"
        "## Cofanie\n"
        "| sytuacja | polecenie |\n|---|---|\n"
        "| zepsułem plik, nie commitowałem | `git restore plik.py` (wraca do ostatniego commita; zmiany przepadają!) |\n"
        "| dodałem do poczekalni przez pomyłkę | `git restore --staged plik.py` |\n"
        "| muszę na chwilę przełączyć gałąź, zmiany niegotowe | `git stash` → … → `git stash pop` |\n"
        "| zły commit już wysłany | `git revert <sha>` — nowy commit odwracający |\n"
        "Starsze instrukcje używają `git checkout -- plik` — działa tak samo jak restore.\n"
        "## Scalanie i pull request\n"
        "1. Na gałęzi: commity → `git push -u origin feature/csv`. 2. GitHub pokaże „Compare & pull request” → opis: co, dlaczego, jak sprawdzić. 3. Recenzja (Files changed, komentarze). 4. „Merge pull request”. 5. Lokalnie: `git switch main` → `git pull`.\n"
        "Lokalne scalenie bez GitHuba: na main `git merge feature/csv`.\n"
        "## Konflikt\n"
        "Gdy dwie gałęzie zmieniły tę samą linię, Git wstawia znaczniki `<<<<<<<`, `=======`, `>>>>>>>`. Wybierasz właściwą wersję, usuwasz znaczniki, `git add` i `git commit`."),
    przyklad=("PS …\\PRACA> git switch -c feature/csv\n"
              "Switched to a new branch 'feature/csv'\n"
              "PS …\\PRACA> git add csv_odczyt.py\n"
              "PS …\\PRACA> git commit -m \"Dodaj odczyt produktów z CSV\"\n"
              "PS …\\PRACA> git diff HEAD~1 --stat\n"
              " csv_odczyt.py | 18 ++++++++++++++++++\n"
              "PS …\\PRACA> git push -u origin feature/csv\n"
              "remote: Create a pull request for 'feature/csv' on GitHub by visiting: …/pull/new/feature/csv\n"
              "(GitHub: Compare & pull request → opis → Create → Merge pull request)\n"
              "PS …\\PRACA> git switch main\n"
              "PS …\\PRACA> git pull\n"
              "PS …\\PRACA> git log --oneline --graph\n"
              "*   9c1d2e4 Merge pull request #1 from anna-nowak/feature/csv\n"
              "|\\\n| * 5b7a3f0 Dodaj odczyt produktów z CSV\n|/\n* 3f2a1c9 Dodaj pierwszy program hello.py"),
    demonstracja={"tytul": "Funkcja na gałęzi i pull request", "kroki": [
        "`git switch -c feature/csv` — nowa gałąź od bieżącego main; od teraz commity trafiają na nią.",
        "add + commit jak zwykle — main się nie zmienia.",
        "`git diff HEAD~1 --stat` — podsumowanie: który plik i ile linii zmienił ostatni commit (HEAD~1 = commit przed bieżącym).",
        "`git push -u origin feature/csv` — gałąź trafia na GitHub; terminal podaje link do utworzenia PR.",
        "Na GitHubie: tytuł PR jak opis commita, w opisie „Co / Dlaczego / Jak sprawdzić”, zakładka Files changed — recenzja linii.",
        "Merge pull request — GitHub tworzy commit scalający na main.",
        "Lokalnie `git switch main` i `git pull` — Twoje main dogania GitHub.",
        "`git log --oneline --graph` — rozgałęzienie i scalenie widoczne jako „gałązka”."],
        "wynik": "Na GitHubie zamknięty (scalony) PR #1, a w historii main commit „Merge pull request #1…”."},
    jak_uruchomic=["Terminal w PRACA → polecenia z ramki.", "GitHub → zakładka Pull requests → Compare & pull request."],
    cwiczenia=[
        C("prowadzone",
          "Ułóż kroki pracy z gałęzią (numery po przecinku): 1 `git push -u origin feature/raport`, 2 `git switch -c feature/raport`, 3 Merge pull request na GitHubie, 4 `git commit -m \"Dodaj raport\"`, 5 `git switch main` i `git pull`. Czas: 10 minut.",
          "2, 4, 1, 3, 5.",
          ["Najpierw gałąź, potem praca na niej.", "Wysyłasz zacommitowane zmiany.", "Po scaleniu aktualizujesz lokalne main."],
          "2 (gałąź) → 4 (commit) → 1 (push) → 3 (merge PR) → 5 (main + pull).",
          [tx("k", "Kolejność", "2, 4, 1, 3, 5")]),
        C("samodzielne",
          "Dobierz polecenie: (1) zepsułeś(-aś) raport.py, nie było commita od rana, chcesz wrócić do ostatniej zapisanej wersji; (2) w połowie pracy musisz przełączyć gałąź, zmian nie chcesz commitować; (3) zły commit jest już na GitHubie i inni go pobrali; (4) chcesz zobaczyć, co dokładnie zmieniłeś przed commitem. "
          "Opcje: git restore raport.py / git stash / git revert <sha> / git diff. Czas: 15 minut.",
          "(1) git restore raport.py; (2) git stash; (3) git revert <sha>; (4) git diff.",
          ["Restore wraca do stanu z ostatniego commita.", "Stash odkłada zmiany na półkę.", "Revert nie przepisuje historii, którą inni już mają."],
          "(1) `git restore raport.py`; (2) `git stash` (potem `git stash pop`); (3) `git revert <sha>`; (4) `git diff`.",
          [wy("a", "(1) zepsuty plik bez commita", ["git restore raport.py", "git stash", "git revert <sha>", "git diff"], "git restore raport.py"),
           wy("b", "(2) zmiany na półkę", ["git restore raport.py", "git stash", "git revert <sha>", "git diff"], "git stash"),
           wy("c", "(3) zły commit wysłany", ["git restore raport.py", "git stash", "git revert <sha>", "git diff"], "git revert <sha>"),
           wy("d", "(4) podgląd zmian", ["git restore raport.py", "git stash", "git revert <sha>", "git diff"], "git diff")]),
    ],
    typowe_bledy=[
        B("error: Your local changes to the following files would be overwritten by checkout", "Niezacommitowane zmiany przy przełączaniu gałęzi.", "`git status`.", "commit albo `git stash`, potem switch."),
        B("CONFLICT (content): Merge conflict in csv_odczyt.py", "Ta sama linia zmieniona na dwóch gałęziach.", "Otwórz plik, szukaj <<<<<<<.", "Zostaw właściwą wersję, usuń znaczniki, git add, git commit."),
        B("fatal: The current branch feature/csv has no upstream branch", "Pierwszy push gałęzi bez -u.", "Komunikat podaje gotowe polecenie.", "`git push -u origin feature/csv`."),
    ],
    pulapki=["git restore bezpowrotnie kasuje niezacommitowane zmiany w pliku — najpierw git diff.", "Praca tygodniami na jednej gałęzi bez scalania = duże konflikty; scalaj małe zmiany często."],
    zadania=["Gałąź feature/csv → commit → push → PR → merge.", "Celowo zepsuj plik i odzyskaj go git restore; potem przetestuj git stash.", "Opisz w notatki.md różnicę restore / stash / revert."],
    pytania=[["Po co gałęzie?", "Żeby rozwijać zmianę osobno, nie psując działającego main."], ["Czym różni się revert od restore?", "revert tworzy commit odwracający wysłany commit; restore cofa niezacommitowane zmiany w pliku."], ["Co zawiera dobry opis PR?", "Co, dlaczego, jak sprawdzić."]],
    podsumowanie="Pracujesz na gałęziach, przeglądasz diff i log, cofasz zmiany właściwym poleceniem, rozwiązujesz konflikt i przeprowadzasz pull request do scalenia.",
    test=[T("Nowa gałąź i przejście na nią:", ["git branch -d x", "git switch -c x", "git merge x", "git log x"], 1, "-c = create."),
          T("git stash:", ["usuwa commit", "odkłada niezacommitowane zmiany", "wysyła na GitHub", "tworzy gałąź"], 1, "Półka na zmiany."),
          T("Znaczniki <<<<<<< w pliku oznaczają:", ["błąd Pythona", "konflikt scalania", "komentarz", "nową gałąź"], 1, "Do ręcznego rozwiązania."),
          T("Zły commit już pobrany przez innych cofasz:", ["git reset --hard i push --force", "git revert", "usuwając repozytorium", "git stash"], 1, "Bez przepisywania wspólnej historii.")],
    w_praktyce=["Recenzując PR jako tester: uruchom testy na gałęzi, sprawdź opis „jak sprawdzić”, przetestuj przypadki brzegowe.", "Jeden PR = jedna zmiana, którą da się przejrzeć w 15 minut."],
    zrodla=[Z.GIT_PL_GAL, Z.GIT_PL, Z.GIT_DOCS, Z.GH_PR],
)

# =========================================================================== TYDZIEŃ 5
KLASY = L(
    id="klasy", nazwa="Klasy i obiekty: __init__, self, metody, __str__", tydzien=5,
    slowa=["klasa", "obiekt", "instancja", "__init__", "self", "atrybut", "metoda", "__str__", "__repr__", "dataclass", "hermetyzacja"],
    cel="Po tej lekcji definiujesz klasę z __init__ i atrybutami, piszesz metody zmieniające stan obiektu (z walidacją), tworzysz kilka obiektów i czytelnie je wypisujesz przez __str__.",
    po_co="Page Object Model w Selenium (tydzień 8) to klasy; frameworki testowe i biblioteki są zbudowane z klas. Tester musi je czytać i pisać.",
    wymagania=["Lekcje „Funkcje”, „Słowniki”, „Obsługa błędów”."],
    wyjasnienie=(
        "## Klasa i obiekt\n"
        "**Klasa** to wzór (formularz „Produkt”: nazwa, cena, ilość), **obiekt** to wypełniony egzemplarz (Zeszyt A5, 4.50, 120). Z jednej klasy tworzysz wiele obiektów.\n"
        "```\nclass Produkt:\n    def __init__(self, nazwa, cena, ilosc=0):\n        self.nazwa = nazwa\n        self.cena = cena\n        self.ilosc = ilosc\n```\n"
        "`__init__` uruchamia się przy tworzeniu obiektu: `z = Produkt(\"Zeszyt A5\", 4.5, 120)`. **self** to „ten konkretny obiekt” — `self.ilosc` to ilość TEGO produktu, nie wszystkich.\n"
        "## Metody\n"
        "Funkcja w klasie, pierwszym parametrem zawsze `self`: `def wartosc(self): return self.cena * self.ilosc`. Wywołanie: `z.wartosc()` (self przekazuje Python).\n"
        "Metoda może zmieniać stan i pilnować reguł: `def wydaj(self, n): if n > self.ilosc: raise ValueError(...)`, potem `self.ilosc -= n`.\n"
        "## __str__\n"
        "`print(z)` bez `__str__` pokaże `<__main__.Produkt object at 0x…>`. Metoda `__str__(self)` zwraca czytelny napis: „Zeszyt A5 — 4.50 zł, 120 szt.”.\n"
        "## Kiedy klasa, a kiedy słownik\n"
        "Słownik — same dane. Klasa — dane **i** operacje z regułami (wydaj nie zejdzie poniżej zera). W testach łatwiej sprawdzić metodę klasy niż rozproszone funkcje.\n"
        "## dataclass (dla ciekawych)\n"
        "`from dataclasses import dataclass` i `@dataclass` nad klasą generuje __init__ i __repr__ automatycznie. W kursie piszesz __init__ ręcznie — żeby rozumieć, co się dzieje."),
    przyklad=kod("klasy", (
        "class Produkt:\n"
        "    def __init__(self, nazwa, cena, ilosc=0):\n"
        "        self.nazwa = nazwa\n"
        "        self.cena = cena\n"
        "        self.ilosc = ilosc\n\n"
        "    def wartosc(self):\n"
        "        return round(self.cena * self.ilosc, 2)\n\n"
        "    def przyjmij(self, n):\n"
        "        if n <= 0:\n"
        "            raise ValueError(\"ilość musi być dodatnia\")\n"
        "        self.ilosc += n\n\n"
        "    def wydaj(self, n):\n"
        "        if n <= 0 or n > self.ilosc:\n"
        "            raise ValueError(f\"nie można wydać {n} szt. (stan: {self.ilosc})\")\n"
        "        self.ilosc -= n\n\n"
        "    def __str__(self):\n"
        "        return f\"{self.nazwa} — {self.cena:.2f} zł, {self.ilosc} szt.\"\n\n\n"
        "zeszyt = Produkt(\"Zeszyt A5\", 4.5, 120)\n"
        "klej = Produkt(\"Klej w sztyfcie\", 3.4)\n"
        "klej.przyjmij(50)\n"
        "zeszyt.wydaj(20)\n"
        "for p in [zeszyt, klej]:\n"
        "    print(p, \"| wartość:\", p.wartosc())\n"
        "try:\n"
        "    klej.wydaj(80)\n"
        "except ValueError as e:\n"
        "    print(\"Błąd:\", e)\n"), "Zeszyt A5 — 4.50 zł, 100 szt. | wartość: 450.0\nKlej w sztyfcie — 3.40 zł, 50 szt. | wartość: 170.0\nBłąd: nie można wydać 80 szt. (stan: 50)\n"),
    demonstracja={"tytul": "Klasa Produkt z regułami magazynu", "kroki": [
        "`class Produkt:` — definicja wzoru; nazwy klas wielką literą (PEP 8).",
        "`__init__(self, nazwa, cena, ilosc=0)` — zapisuje dane w atrybutach `self.…`; ilość domyślnie 0.",
        "`wartosc(self)` — liczy z atrybutów tego obiektu; round do groszy.",
        "`przyjmij` i `wydaj` zmieniają `self.ilosc`, ale najpierw walidują — wydanie więcej niż stan rzuca ValueError.",
        "`__str__` — co pokaże print(obiekt).",
        "Dwa obiekty z jednej klasy mają osobne ilości: wydanie zeszytów nie zmienia kleju.",
        "Próba wydania 80 sztuk kleju przy stanie 50 → komunikat błędu, stan bez zmian."],
        "wynik": "Dwie linie produktów z wartościami (450.0 i 170.0) i „Błąd: nie można wydać 80 szt. (stan: 50)”."},
    jak_uruchomic=["Zapisz jako produkt.py → ▶ Uruchom.", "Usuń `__str__` i uruchom — zobacz, co wypisuje print bez niego."],
    cwiczenia=[
        C("prowadzone",
          "Dla klasy z demonstracji: `p = Produkt(\"Kredki\", 12.9, 40)`, potem `p.wydaj(15)`, `p.przyjmij(5)`. Podaj: (1) `p.ilosc`, (2) `p.wartosc()`, (3) co zwróci `str(p)`. Czas: 15 minut.",
          "(1) 30; (2) 387.0; (3) Kredki — 12.90 zł, 30 szt.",
          ["40 − 15 + 5.", "12.9 × 30.", "Format z __str__: nazwa — cena z 2 miejscami zł, ilość szt."],
          "(1) 30; (2) 12.9 × 30 = 387.0; (3) „Kredki — 12.90 zł, 30 szt.”.",
          [li("a", "(1) p.ilosc", 30), li("b", "(2) p.wartosc()", 387.0), tx("c", "(3) str(p)", "Kredki — 12.90 zł, 30 szt.")]),
        C("samodzielne",
          "Kolega dopisał metodę `def rabat(procent): return self.cena * (1 - procent / 100)`. Wywołanie `p.rabat(10)` daje błąd. (1) Jaki (wybierz)? (2) Czego brakuje w def (wpisz poprawną pierwszą linię)? (3) Co powinna zwrócić poprawiona metoda dla ceny 12.9 i 10% (z round do 2 miejsc)? Czas: 15 minut.",
          "(1) TypeError; (2) def rabat(self, procent):; (3) 11.61.",
          ["Python przekazuje obiekt jako pierwszy argument.", "Pierwszy parametr metody to zawsze…", "12.9 × 0.9."],
          "(1) TypeError: rabat() takes 1 positional argument but 2 were given; (2) `def rabat(self, procent):`; (3) round(12.9 × 0.9, 2) = 11.61.",
          [wy("a", "(1) Błąd", ["NameError", "TypeError", "ValueError", "AttributeError"], "TypeError"), tx("b", "(2) Pierwsza linia", "def rabat(self, procent):"), kw("c", "(3) Wynik", 11.61)]),
    ],
    typowe_bledy=[
        B("TypeError: wydaj() takes 1 positional argument but 2 were given", "Brak self w definicji metody.", "Pierwszy parametr metody?", "def wydaj(self, n):"),
        B("AttributeError: 'Produkt' object has no attribute 'ilosc'", "W __init__ zabrakło self.ilosc = … (albo literówka).", "Wypisz `vars(obiekt)`.", "Ustaw wszystkie atrybuty w __init__."),
        B("NameError: name 'ilosc' is not defined w metodzie", "Użycie `ilosc` zamiast `self.ilosc`.", "Czy atrybut ma self.?", "Atrybuty obiektu zawsze przez self."),
    ],
    pulapki=["Atrybut klasy (poza __init__) wspólny dla wszystkich obiektów — dane obiektu zawsze w __init__ przez self.", "Metoda zmieniająca stan bez walidacji — ujemne stany w magazynie."],
    zadania=["Klasa Produkt: atrybuty, metoda opis(), 3 obiekty.", "Metody przyjmij/wydaj z ValueError.", "__str__ i wypisanie listy obiektów pętlą."],
    pytania=[["Czym różni się klasa od obiektu?", "Klasa to wzór, obiekt — konkretny egzemplarz."], ["Co oznacza self?", "Obiekt, na którym wywołano metodę."], ["Po co __str__?", "Czytelny napis przy print(obiekt)."]],
    podsumowanie="Definiujesz klasy z __init__, atrybutami i metodami z walidacją, tworzysz wiele obiektów i wypisujesz je czytelnie.",
    test=[T("Co oznacza self w metodzie?", ["Klasę", "Konkretny obiekt, na którym wywołano metodę", "Moduł", "Nic"], 1, "self.ilosc to ilość tego obiektu."),
          T("__init__ uruchamia się:", ["przy imporcie", "przy tworzeniu obiektu", "przy print", "nigdy"], 1, "Konstruktor."),
          T("print(obiekt) bez __str__ wypisze:", ["atrybuty", "<…object at 0x…>", "błąd", "nic"], 1, "Domyślna reprezentacja."),
          T("Nazwa klasy wg PEP 8:", ["produkt", "Produkt", "PRODUKT", "produkt_klasa"], 1, "CamelCase.")],
    w_praktyce=["Klasa strony (Page Object) = lokatory + metody akcji; testy wołają metody, nie lokatory.", "Testujesz metody klasy: poprawne dane, granice, wyjątki."],
    zrodla=[Z.PY_TUT_CLS, Z.PY_PEP8],
)

MODULY = L(
    id="moduly", nazwa="Podział kodu na moduły i import własnych plików", tydzien=5,
    slowa=["moduł", "import", "from", "pakiet", "__init__.py", "odpowiedzialność", "main.py", "struktura projektu", "zależność cykliczna"],
    cel="Po tej lekcji dzielisz program na kilka plików z jedną odpowiedzialnością (dane, logika, interfejs), importujesz własne moduły (import / from … import) i uruchamiasz całość z main.py.",
    po_co="Projekt testowy ma osobno strony (pages/), testy (tests/) i konfigurację. Rekruter po strukturze katalogów widzi, czy umiesz organizować kod.",
    wymagania=["Lekcje „Funkcje” i „Klasy”.", "Menedżer zadań z tygodnia 3 (zadanie t3z5)."],
    wyjasnienie=(
        "## Moduł = plik .py\n"
        "Każdy plik .py jest modułem. Jeśli w PRACA masz `zadania.py` z funkcją `dodaj`, w `main.py` piszesz `import zadania` i wołasz `zadania.dodaj(...)` albo `from zadania import dodaj` i wołasz `dodaj(...)`.\n"
        "## Jedna odpowiedzialność\n"
        "| plik | odpowiada za | nie robi |\n|---|---|---|\n"
        "| `zadania.py` | logika: dodaj, oznacz, usuń, otwarte | input/print, pliki |\n"
        "| `plik.py` | zapis/odczyt listy do pliku | logika zadań |\n"
        "| `main.py` | menu: input/print, wywołuje dwa pozostałe | obliczeń |\n"
        "Zmiana formatu pliku (txt → JSON) dotyka tylko plik.py; testy logiki dotyczą tylko zadania.py.\n"
        "## Gdzie Python szuka modułów\n"
        "Najpierw w katalogu uruchamianego skryptu, potem w bibliotece standardowej i zainstalowanych pakietach. Dlatego **nie nazywaj plików jak moduły standardowe** (random.py, csv.py, json.py) — przykryjesz je.\n"
        "## Import uruchamia moduł\n"
        "Import wykonuje cały plik od góry. Wywołania i input() w modułach trzymasz w `if __name__ == \"__main__\":` — inaczej import (np. w teście) uruchomi menu.\n"
        "## Pakiet\n"
        "Katalog z plikami .py (np. `pages/`) i plikiem `__init__.py` (może być pusty) to pakiet: `from pages.login_page import LoginPage`.\n"
        "## Zapis do pliku: JSON\n"
        "Listę słowników najprościej zapisać modułem json: `json.dump(lista, f, ensure_ascii=False, indent=2)` i odczytać `json.load(f)` — zachowa typy (liczby, True/False)."),
    przyklad=kod("moduly", (
        "import json\n"
        "import tempfile\n"
        "from pathlib import Path\n\n"
        "katalog = Path(tempfile.mkdtemp())\n"
        "(katalog / \"zadania.py\").write_text(\n"
        "    \"def dodaj(lista, tytul):\\n\"\n"
        "    \"    lista.append({'tytul': tytul.strip(), 'zrobione': False})\\n\", encoding=\"utf-8\")\n"
        "(katalog / \"plik.py\").write_text(\n"
        "    \"import json\\n\"\n"
        "    \"def zapisz(lista, sciezka):\\n\"\n"
        "    \"    with open(sciezka, 'w', encoding='utf-8') as f:\\n\"\n"
        "    \"        json.dump(lista, f, ensure_ascii=False)\\n\"\n"
        "    \"def wczytaj(sciezka):\\n\"\n"
        "    \"    with open(sciezka, encoding='utf-8') as f:\\n\"\n"
        "    \"        return json.load(f)\\n\", encoding=\"utf-8\")\n\n"
        "import sys\n"
        "sys.path.insert(0, str(katalog))\n"
        "import zadania\n"
        "from plik import zapisz, wczytaj\n\n"
        "lista = []\n"
        "zadania.dodaj(lista, \" Zamówić zszywki \")\n"
        "zapisz(lista, katalog / \"zadania.json\")\n"
        "print(wczytaj(katalog / \"zadania.json\"))\n"
        "print(sorted(p.name for p in katalog.iterdir() if p.suffix in (\".py\", \".json\")))\n"), (
        "[{'tytul': 'Zamówić zszywki', 'zrobione': False}]\n['plik.py', 'zadania.json', 'zadania.py']\n")),
    demonstracja={"tytul": "Trzy pliki zamiast jednego (zapisane i zaimportowane w locie)", "kroki": [
        "Przykład sam tworzy w katalogu tymczasowym dwa moduły — żeby dało się go uruchomić jednym plikiem. W zadaniu po prostu masz w PRACA trzy pliki: zadania.py, plik.py, main.py.",
        "`zadania.py` — tylko logika (dodaj).",
        "`plik.py` — tylko zapis/odczyt JSON; `ensure_ascii=False` zachowuje polskie litery w pliku.",
        "`sys.path.insert(0, …)` — dodaje katalog do miejsc, gdzie Python szuka modułów (w PRACA niepotrzebne — main.py i moduły są obok siebie).",
        "`import zadania` → wołasz `zadania.dodaj`; `from plik import zapisz, wczytaj` → wołasz bez przedrostka.",
        "Zapis i odczyt: lista wraca z pliku z tymi samymi typami (False zostało bool)."],
        "wynik": "Lista z jednym zadaniem wczytana z pliku JSON i lista trzech plików w katalogu."},
    jak_uruchomic=["W PRACA: zadania.py, plik.py, main.py obok siebie → otwórz main.py → ▶ Uruchom.", "Terminal: `python main.py` w PRACA."],
    cwiczenia=[
        C("prowadzone",
          "W PRACA są: `ceny.py` z funkcją `brutto(netto)` i `main.py`. (1) Jak zaimportować samą funkcję (wpisz linię)? (2) Jak ją wtedy wywołać dla 10 (wpisz)? (3) Jak wywołać po `import ceny` (wpisz)? Czas: 10 minut.",
          "(1) from ceny import brutto; (2) brutto(10); (3) ceny.brutto(10).",
          ["Import konkretnej nazwy: from … import ….", "Zaimportowana nazwa działa bez przedrostka.", "Po import modułu: moduł.funkcja()."],
          "(1) `from ceny import brutto`; (2) `brutto(10)`; (3) `ceny.brutto(10)`.",
          [tx("a", "(1) Import", "from ceny import brutto"), tx("b", "(2) Wywołanie", "brutto(10)"), tx("c", "(3) Wywołanie po import ceny", "ceny.brutto(10)")]),
        C("samodzielne",
          "Rozmieść funkcje w plikach zadania.py / plik.py / main.py: (1) `zapisz_json(lista, sciezka)`, (2) `oznacz(lista, nr)`, (3) pętla `while True` z input(\"Wybór: \"), (4) `wczytaj_json(sciezka)`. Dodatkowo: (5) co się stanie po `import csv` w projekcie, w którym masz własny plik csv.py (wybierz)? Czas: 15 minut.",
          "(1) plik.py; (2) zadania.py; (3) main.py; (4) plik.py; (5) Python zaimportuje Twój csv.py zamiast modułu standardowego.",
          ["Zapis/odczyt to praca z plikiem.", "Operacje na zadaniach to logika.", "input() tylko w interfejsie."],
          "(1) plik.py; (2) zadania.py; (3) main.py; (4) plik.py; (5) Twój csv.py przykryje moduł csv — błędy typu AttributeError: module 'csv' has no attribute 'DictReader'.",
          [wy("a", "(1) zapisz_json", ["zadania.py", "plik.py", "main.py"], "plik.py"), wy("b", "(2) oznacz", ["zadania.py", "plik.py", "main.py"], "zadania.py"),
           wy("c", "(3) pętla z input", ["zadania.py", "plik.py", "main.py"], "main.py"), wy("d", "(4) wczytaj_json", ["zadania.py", "plik.py", "main.py"], "plik.py"),
           wy("e", "(5) własny csv.py", ["nic — Python wybierze standardowy", "Python zaimportuje Twój csv.py zamiast modułu standardowego", "błąd składni"], "Python zaimportuje Twój csv.py zamiast modułu standardowego")]),
    ],
    typowe_bledy=[
        B("ModuleNotFoundError: No module named 'zadania'", "main.py uruchomiony z innego katalogu albo literówka w nazwie pliku.", "`ls` — czy zadania.py leży obok main.py?", "Uruchamiaj z katalogu projektu; nazwa pliku = nazwa w import (bez .py)."),
        B("ImportError: cannot import name 'dodaj' from 'zadania'", "Brak funkcji o tej nazwie (literówka) albo import cykliczny.", "Otwórz zadania.py — czy jest def dodaj?", "Popraw nazwę; moduły nie importują się nawzajem w kółko."),
        B("Import uruchamia menu", "Kod menu poza blokiem __main__ w module.", "Co jest poza funkcjami?", "Przenieś do if __name__ == \"__main__\":."),
    ],
    pulapki=["Plik nazwany jak moduł standardowy (random.py, json.py, test.py) — przykrywa oryginał.", "from modul import * — nie wiesz, skąd pochodzą nazwy; importuj jawnie."],
    zadania=["Menedżer zadań w 3 plikach z jasną odpowiedzialnością.", "Zapis i odczyt listy zadań w JSON.", "Sprawdź, że import zadania nie uruchamia menu."],
    pytania=[["Co jest modułem w Pythonie?", "Każdy plik .py."], ["Dlaczego input() tylko w main.py?", "Logika i zapis mają być testowalne i niezależne od interfejsu."], ["Po co __init__.py?", "Oznacza katalog jako pakiet (import pages.login_page)."]],
    podsumowanie="Dzielisz program na moduły z jedną odpowiedzialnością, importujesz je i unikasz typowych pułapek nazw i importu uruchamiającego kod.",
    test=[T("Po `from zadania import dodaj` wywołujesz:", ["zadania.dodaj()", "dodaj()", "import.dodaj()", "zadania::dodaj()"], 1, "Nazwa zaimportowana bezpośrednio."),
          T("Plik random.py w projekcie:", ["przyspiesza losowanie", "przykrywa moduł standardowy random", "jest wymagany", "nic nie zmienia"], 1, "Python najpierw szuka w katalogu skryptu."),
          T("Gdzie zapisywanie do pliku w menedżerze zadań?", ["main.py", "zadania.py", "plik.py", "wszędzie"], 2, "Jedna odpowiedzialność."),
          T("json.dump(..., ensure_ascii=False):", ["szyfruje plik", "zachowuje polskie litery czytelne w pliku", "usuwa polskie litery", "kompresuje"], 1, "Bez \\u0105 zamiast ą.")],
    w_praktyce=["Projekt testów: pages/ (Page Objects), tests/ (testy), conftest.py (fixtures) — każdy z jedną rolą.", "Czytając cudzy projekt, zaczynasz od struktury katalogów i importów w main."],
    zrodla=[Z.PY_TUT_MOD, Z.PY_JSON, Z.PY_PEP8],
)

VENV = L(
    id="venv", nazwa="venv, pip, requirements.txt i .gitignore", tydzien=5,
    slowa=["venv", "środowisko wirtualne", "pip", "install", "requirements.txt", "pip freeze", ".gitignore", "aktywacja", "Activate.ps1", "ExecutionPolicy"],
    cel="Po tej lekcji tworzysz własne środowisko wirtualne projektu (python -m venv .venv), aktywujesz je, instalujesz pakiety pip i zapisujesz je w requirements.txt oraz wykluczasz .venv i sekrety z Gita plikiem .gitignore.",
    po_co="CI (tydzień 9) i każdy członek zespołu odtwarza Twoje środowisko z requirements.txt. Repozytorium z wrzuconym .venv to pierwsza rzecz, którą rekruter zauważa.",
    wymagania=["Lekcja „Narzędzia” (środowisko kursu).", "Terminal PowerShell w katalogu projektu.", "Internet do pip install (pakiety z PyPI)."],
    wyjasnienie=(
        "## Dlaczego osobne środowisko\n"
        "Projekt A potrzebuje selenium 4.52, projekt B — starszej wersji. Środowisko wirtualne (venv) to katalog z własnym Pythonem i pakietami tylko dla jednego projektu. Mentor robi to za Ciebie dla kursu; teraz zrobisz to sam dla własnego projektu — tak jak w pracy.\n"
        "## Krok po kroku (PowerShell, w katalogu projektu)\n"
        "1. `python -m venv .venv` — tworzy katalog .venv (w terminalu Mentora `python` to Python kursu — może być bazą).\n"
        "2. `.\\.venv\\Scripts\\Activate.ps1` — aktywacja; zachęta zaczyna się od `(.venv)`. W CMD: `.venv\\Scripts\\activate.bat`.\n"
        "   Błąd „running scripts is disabled on this system” → jednorazowo `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (dotyczy tylko Twojego konta).\n"
        "3. `python -m pip install requests` — instalacja z PyPI (oficjalne repozytorium pakietów). `python -m pip` gwarantuje, że pip należy do aktywnego Pythona.\n"
        "4. `python -m pip freeze > requirements.txt` — zapis dokładnych wersji (np. `requests==2.34.2`).\n"
        "5. Na innym komputerze / w CI: `python -m pip install -r requirements.txt`.\n"
        "6. `deactivate` — wyjście ze środowiska.\n"
        "## .gitignore\n"
        "Plik tekstowy w katalogu repozytorium, każda linia to wzorzec plików, których Git ma nie śledzić:\n"
        "```\n.venv/\n__pycache__/\n*.pyc\n.env\n.pytest_cache/\nreport.html\n```\n"
        "`.env` to plik z sekretami (klucze API) — nigdy w repozytorium. Jeśli coś już zacommitowałeś: `git rm -r --cached .venv`, potem commit.\n"
        "## Bezpieczeństwo pakietów\n"
        "Instaluj tylko pakiety o nazwach sprawdzonych w dokumentacji — literówka w nazwie (np. „reqeusts”) może zainstalować złośliwą podróbkę. Mentor dla kursu instaluje z pliku z sumami SHA-256 (lock), dlatego tam to ryzyko nie istnieje."),
    przyklad=("PS C:\\…\\PRACA\\pogoda> python -m venv .venv\n"
              "PS C:\\…\\PRACA\\pogoda> .\\.venv\\Scripts\\Activate.ps1\n"
              "(.venv) PS C:\\…\\pogoda> python -m pip install requests\n"
              "Successfully installed certifi-… charset-normalizer-… idna-… requests-2.34.2 urllib3-…\n"
              "(.venv) PS C:\\…\\pogoda> python -m pip freeze > requirements.txt\n"
              "(.venv) PS C:\\…\\pogoda> Get-Content requirements.txt\n"
              "certifi==2026.10.23\ncharset-normalizer==3.5.2\nidna==3.…\nrequests==2.34.2\nurllib3==2.…\n"
              "(.venv) PS C:\\…\\pogoda> Set-Content .gitignore \".venv/`n__pycache__/`n.env\"\n"
              "(.venv) PS C:\\…\\pogoda> git status --short\n"
              "?? .gitignore\n?? api.py\n?? requirements.txt"),
    demonstracja={"tytul": "Własne środowisko projektu od zera", "kroki": [
        "`python -m venv .venv` — powstaje katalog .venv (kilkadziesiąt MB). Kropka na początku nazwy to konwencja „katalog techniczny”.",
        "`Activate.ps1` — od teraz `python` i `pip` w tym oknie to te z .venv; widać `(.venv)` w zachęcie.",
        "`pip install requests` instaluje też zależności requests (certifi, idna…).",
        "`pip freeze > requirements.txt` — znak `>` przekierowuje wynik do pliku.",
        "`.gitignore` z trzema liniami (w PowerShell `` `n `` to nowa linia; możesz też utworzyć plik w edytorze).",
        "`git status --short` — .venv NIE pojawia się na liście (zignorowany), widać tylko pliki projektu."],
        "wynik": "Projekt z .venv (niewidocznym dla Gita), requirements.txt z dokładnymi wersjami i .gitignore."},
    jak_uruchomic=["PowerShell → `cd` do katalogu projektu → polecenia z ramki.", "Weryfikacja: `python -c \"import sys; print(sys.prefix)\"` — ścieżka powinna kończyć się na .venv."],
    cwiczenia=[
        C("prowadzone",
          "Ułóż kroki (numery po przecinku): 1 `python -m pip freeze > requirements.txt`, 2 `.\\.venv\\Scripts\\Activate.ps1`, 3 `python -m venv .venv`, 4 `python -m pip install requests`, 5 dopisz `.venv/` do .gitignore. Czas: 10 minut.",
          "3, 2, 4, 1, 5.",
          ["Najpierw utwórz środowisko.", "Instalujesz w aktywnym środowisku.", "freeze po instalacji."],
          "3 (venv) → 2 (aktywacja) → 4 (install) → 1 (freeze) → 5 (.gitignore). Krok 5 może być też wcześniej — ważne, żeby przed pierwszym commitem.",
          [tx("k", "Kolejność", "3, 2, 4, 1, 5")]),
        C("samodzielne",
          "Które pliki/katalogi trafiają do repozytorium (tak/nie)? (1) requirements.txt, (2) .venv/, (3) .env z kluczem API, (4) api.py, (5) __pycache__/. Dodatkowo (6): kolega po sklonowaniu repo ma błąd ModuleNotFoundError: requests — jakie polecenie wpisze (wpisz)? Czas: 15 minut.",
          "(1) tak; (2) nie; (3) nie; (4) tak; (5) nie; (6) python -m pip install -r requirements.txt.",
          ["Repozytorium = kod i lista zależności, nie zainstalowane pakiety.", "Sekrety nigdy.", "requirements.txt odtwarza środowisko."],
          "(1) tak; (2) nie (każdy tworzy własne); (3) nie (sekret); (4) tak; (5) nie (pliki tymczasowe); (6) `python -m pip install -r requirements.txt` w aktywnym .venv.",
          [wy("a", "(1) requirements.txt", ["tak", "nie"], "tak"), wy("b", "(2) .venv/", ["tak", "nie"], "nie"), wy("c", "(3) .env", ["tak", "nie"], "nie"),
           wy("d", "(4) api.py", ["tak", "nie"], "tak"), wy("e", "(5) __pycache__/", ["tak", "nie"], "nie"), tx("f", "(6) Polecenie", "python -m pip install -r requirements.txt", zawiera=["install", "-r", "requirements.txt"])]),
    ],
    typowe_bledy=[
        B(".\\.venv\\Scripts\\Activate.ps1 cannot be loaded because running scripts is disabled on this system", "Domyślna polityka PowerShell blokuje skrypty.", "`Get-ExecutionPolicy -Scope CurrentUser`.", "`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` albo aktywacja w CMD (activate.bat)."),
        B("pip install działa, a import nie (ModuleNotFoundError)", "Pakiet zainstalowany do innego Pythona.", "`python -m pip --version` — ścieżka?", "Aktywuj .venv i używaj `python -m pip`."),
        B("Na GitHubie tysiące plików z .venv", ".gitignore dodany po commicie.", "`git ls-files .venv | Measure-Object`.", "`git rm -r --cached .venv`, commit; .gitignore z .venv/."),
    ],
    pulapki=["Literówka w nazwie pakietu (typosquatting) — kopiuj nazwy z oficjalnej dokumentacji.", "pip freeze w środowisku z „wszystkim” (systemowym) — requirements z setką zbędnych pakietów."],
    zadania=["Utwórz .venv w katalogu projektu pogody, zainstaluj requests, zapisz requirements.txt.", "Dodaj .gitignore z .venv/, __pycache__/, .env.", "Sprawdź git status — .venv niewidoczny."],
    pytania=[["Po co venv?", "Osobne pakiety i wersje dla każdego projektu."], ["Co zawiera requirements.txt?", "Listę pakietów z wersjami do odtworzenia środowiska."], ["Co wpisujesz do .gitignore na start?", ".venv/, __pycache__/, .env, pliki raportów."]],
    podsumowanie="Tworzysz i aktywujesz venv, instalujesz pakiety pip, zapisujesz requirements.txt i chronisz repozytorium plikiem .gitignore.",
    test=[T("Tworzenie środowiska wirtualnego:", ["pip venv", "python -m venv .venv", "git venv", "venv install"], 1, "Moduł venv."),
          T("Odtworzenie zależności z pliku:", ["pip freeze", "pip install -r requirements.txt", "pip list", "git pull"], 1, "-r = z pliku."),
          T("Czy .venv commitujesz?", ["tak, zawsze", "nie — każdy tworzy własne z requirements.txt", "tylko na main", "tylko w PR"], 1, ".gitignore."),
          T("Plik .env z kluczem API:", ["do repozytorium", "do .gitignore", "do README", "do requirements.txt"], 1, "Sekrety poza repo.")],
    w_praktyce=["Pierwsze polecenia w nowym projekcie: venv → .gitignore → git init.", "W CI: pip install -r requirements.txt, potem pytest."],
    zrodla=[Z.PY_TUT_VENV, Z.GIT_PL_PODST],
)

REQUESTS = L(
    id="requests", nazwa="Biblioteka requests i API: GET, kody HTTP, JSON", tydzien=5,
    slowa=["API", "HTTP", "GET", "POST", "status_code", "200", "404", "500", "JSON", "requests", "timeout", "endpoint", "parametry"],
    cel="Po tej lekcji pobierasz dane z API biblioteką requests (GET z parametrami i timeout), sprawdzasz kod odpowiedzi HTTP, czytasz JSON jako słowniki i listy oraz obsługujesz brak połączenia — także na lokalnym serwerze bez internetu.",
    po_co="Testy API to codzienność testera: wysyłasz żądanie, sprawdzasz status, pola i czas odpowiedzi. requests to najpopularniejsza biblioteka HTTP w Pythonie.",
    wymagania=["Lekcje „Słowniki”, „Obsługa błędów”, „venv” (requests jest w środowisku kursu).", "Sklep testowy z paczki (projekty/sklep_testowy) — lokalne API bez internetu."],
    wyjasnienie=(
        "## API w jednym zdaniu\n"
        "API to „okienko” programu dla innych programów: wysyłasz **żądanie** (request) pod adres (endpoint), dostajesz **odpowiedź** (response) — zwykle JSON.\n"
        "## HTTP: metoda i kod odpowiedzi\n"
        "GET — pobierz, POST — wyślij/utwórz, PUT/PATCH — zmień, DELETE — usuń. Kod odpowiedzi:\n"
        "| kod | znaczenie |\n|---|---|\n"
        "| 200 OK | sukces |\n| 201 Created | utworzono (po POST) |\n| 400 Bad Request | złe dane od klienta |\n"
        "| 401 / 403 | brak logowania / brak uprawnień |\n| 404 Not Found | nie ma takiego zasobu |\n| 500 Internal Server Error | błąd serwera — zawsze bug do zgłoszenia |\n"
        "## requests\n"
        "```\nimport requests\nodp = requests.get(\"http://127.0.0.1:5001/api/produkty\", params={\"kategoria\": \"biuro\"}, timeout=10)\nodp.status_code   # 200\ndane = odp.json()  # lista słowników\n```\n"
        "`params` dokleja do adresu `?kategoria=biuro`. **Zawsze `timeout`** — bez niego program może czekać w nieskończoność. `odp.raise_for_status()` rzuca wyjątek dla kodów 4xx/5xx.\n"
        "## Błędy sieci\n"
        "Brak internetu / serwer wyłączony → `requests.exceptions.ConnectionError`; za długo → `Timeout`. Obie dziedziczą po `requests.exceptions.RequestException` — łapiesz ją i wypisujesz zrozumiały komunikat.\n"
        "## Lokalne API zamiast internetu\n"
        "Sklep testowy z paczki kursu uruchomisz poleceniem `python app.py` w projekty/sklep_testowy — API działa pod `http://127.0.0.1:5001/api/produkty`. Publiczne API z internetu (np. open-meteo.com — prognozy pogody bez klucza) to opcja dodatkowa.\n"
        "## Co sprawdza tester API\n"
        "Kod odpowiedzi, typ treści (JSON), obecność i typy pól, wartości graniczne parametrów, zachowanie przy złym parametrze (400, nie 500) i czas odpowiedzi."),
    przyklad=kod("requests", (
        "import json\n"
        "import threading\n"
        "from http.server import BaseHTTPRequestHandler, HTTPServer\n\n"
        "import requests\n\n"
        "PRODUKTY = [{\"id\": 1, \"nazwa\": \"Zeszyt A5\", \"cena\": 4.5, \"kategoria\": \"zeszyty\"},\n"
        "            {\"id\": 14, \"nazwa\": \"Segregator A4\", \"cena\": 11.9, \"kategoria\": \"biuro\"}]\n\n\n"
        "class Api(BaseHTTPRequestHandler):\n"
        "    def do_GET(self):\n"
        "        if self.path.startswith(\"/api/produkty\"):\n"
        "            tresc, kod = json.dumps(PRODUKTY).encode(), 200\n"
        "        else:\n"
        "            tresc, kod = b'{\"blad\": \"nie ma\"}', 404\n"
        "        self.send_response(kod)\n"
        "        self.send_header(\"Content-Type\", \"application/json\")\n"
        "        self.end_headers()\n"
        "        self.wfile.write(tresc)\n\n"
        "    def log_message(self, *args):\n"
        "        pass\n\n\n"
        "serwer = HTTPServer((\"127.0.0.1\", 0), Api)\n"
        "threading.Thread(target=serwer.serve_forever, daemon=True).start()\n"
        "adres = f\"http://127.0.0.1:{serwer.server_port}\"\n\n"
        "odp = requests.get(adres + \"/api/produkty\", timeout=5)\n"
        "print(odp.status_code, odp.headers[\"Content-Type\"])\n"
        "for p in odp.json():\n"
        "    print(p[\"id\"], p[\"nazwa\"], p[\"cena\"])\n"
        "print(\"Brak zasobu:\", requests.get(adres + \"/api/koszyk\", timeout=5).status_code)\n"
        "serwer.shutdown()\n"
        "serwer.server_close()\n"
        "try:\n"
        "    requests.get(adres + \"/api/produkty\", timeout=3)\n"
        "except requests.exceptions.RequestException:\n"
        "    print(\"Serwer niedostępny — sprawdź, czy działa i czy adres jest dobry\")\n"), (
        "200 application/json\n1 Zeszyt A5 4.5\n14 Segregator A4 11.9\nBrak zasobu: 404\nSerwer niedostępny — sprawdź, czy działa i czy adres jest dobry\n")),
    demonstracja={"tytul": "Mini-API na Twoim komputerze i klient requests", "kroki": [
        "Górna część to mały serwer HTTP z biblioteki standardowej — tylko po to, żeby przykład działał bez internetu i bez sklepu testowego. Nie musisz go umieć pisać.",
        "`do_GET` — dla adresu /api/produkty odsyła listę produktów jako JSON z kodem 200, dla innych — 404.",
        "`HTTPServer((\"127.0.0.1\", 0), Api)` — port 0 = system wybiera wolny port; wątek (thread) uruchamia serwer w tle.",
        "`requests.get(adres + \"/api/produkty\", timeout=5)` — żądanie GET z limitem 5 sekund.",
        "`odp.status_code` → 200, nagłówek Content-Type → application/json.",
        "`odp.json()` zamienia JSON na listę słowników — dalej zwykły Python: pętla i klucze.",
        "Nieistniejący zasób → 404 (to nie wyjątek w requests — kod sprawdzasz sam).",
        "Po `serwer.shutdown()` i `server_close()` serwer nie odpowiada: requests rzuca ConnectionError (albo Timeout) — oba łapie `RequestException`, a użytkownik dostaje czytelny komunikat. Tak samo zachowa się program bez internetu."],
        "wynik": "200 application/json, dwa produkty, „Brak zasobu: 404” i komunikat „Serwer niedostępny — …”."},
    jak_uruchomic=["Zapisz jako api_demo.py → ▶ Uruchom (działa offline).",
                   "Sklep testowy: terminal Mentora → `cd projekty\\sklep_testowy` (w materiałach kursu) → `python app.py` → w przeglądarce http://127.0.0.1:5001/api/produkty."],
    cwiczenia=[
        C("prowadzone",
          "Dopasuj kod odpowiedzi: (1) GET /api/produkty — lista OK; (2) POST nowego zamówienia — utworzone; (3) GET /api/produkty/999 — brak produktu; (4) serwer rzucił wyjątek przy dzieleniu przez zero; (5) POST z ilością „abc” — serwer odrzucił dane. Opcje: 200, 201, 400, 404, 500. Czas: 10 minut.",
          "(1) 200; (2) 201; (3) 404; (4) 500; (5) 400.",
          ["2xx — sukces, 4xx — błąd klienta, 5xx — błąd serwera.", "Created ma osobny kod.", "Złe dane od klienta to nie błąd serwera."],
          "(1) 200 OK; (2) 201 Created; (3) 404 Not Found; (4) 500 Internal Server Error; (5) 400 Bad Request.",
          [wy("a", "(1) lista OK", ["200", "201", "400", "404", "500"], "200"), wy("b", "(2) utworzono", ["200", "201", "400", "404", "500"], "201"), wy("c", "(3) brak produktu", ["200", "201", "400", "404", "500"], "404"),
           wy("d", "(4) wyjątek serwera", ["200", "201", "400", "404", "500"], "500"), wy("e", "(5) złe dane", ["200", "201", "400", "404", "500"], "400")]),
        C("samodzielne",
          "Testujesz API sklepu: GET /api/produkty?kategoria=xyz (nieistniejąca kategoria) zwraca 500 i stronę z tracebackiem. (1) Czy to błąd do zgłoszenia (tak/nie)? (2) Jaki kod byłby właściwy — wybierz: 200 z pustą listą / 404 / 500. (3) Czego zabrakło w kodzie klienta, który przy wyłączonym serwerze „zawiesił się” na 2 minuty (wpisz nazwę argumentu)? Czas: 15 minut.",
          "(1) tak; (2) 200 z pustą listą (albo 404 — zależnie od specyfikacji; nigdy 500); (3) timeout.",
          ["5xx przy złych danych od klienta to zawsze błąd serwera.", "Filtr bez wyników to poprawna, pusta odpowiedź.", "Argument ograniczający czas czekania."],
          "(1) tak — 500 dla błędnego parametru to bug, a traceback ujawnia szczegóły serwera; (2) 200 z pustą listą `[]` (dopuszczalne też 400/404, jeśli tak mówi specyfikacja); (3) `timeout`.",
          [wy("a", "(1) Zgłosić?", ["tak", "nie"], "tak"), wy("b", "(2) Właściwy kod", ["200 z pustą listą", "404", "500"], "200 z pustą listą"), tx("c", "(3) Argument", "timeout")]),
    ],
    typowe_bledy=[
        B("requests.exceptions.ConnectionError: … Failed to establish a new connection", "Serwer nie działa / brak internetu / zły port.", "Otwórz adres w przeglądarce.", "Uruchom serwer (python app.py) albo sprawdź adres; łap RequestException."),
        B("requests.exceptions.JSONDecodeError: Expecting value", "Odpowiedź nie jest JSON-em (np. strona błędu HTML).", "`print(odp.status_code, odp.text[:200])`.", "Sprawdź status przed .json()."),
        B("KeyError: 'temperature' przy czytaniu JSON", "Inna struktura odpowiedzi niż zakładasz.", "`print(json.dumps(dane, indent=2)[:500])`.", "Dopasuj klucze do prawdziwej odpowiedzi; używaj .get()."),
    ],
    pulapki=["Brak timeout — program może czekać bez końca.", "Klucze API w kodzie — tylko w zmiennych środowiskowych/.env (poza repo)."],
    zadania=["Pobierz produkty z lokalnego API sklepu i wypisz 3 pola.", "Obsłuż wyłączony serwer czytelnym komunikatem.", "Zapisz wybrane dane z API do CSV z datą."],
    pytania=[["Co oznacza 404, a co 500?", "404 — brak zasobu; 500 — błąd serwera."], ["Po co timeout?", "Żeby program nie czekał w nieskończoność."], ["Co zwraca odp.json()?", "Dane JSON zamienione na słowniki/listy Pythona."]],
    podsumowanie="Wysyłasz żądania GET z parametrami i timeout, rozumiesz kody HTTP, czytasz JSON i obsługujesz błędy sieci — także na lokalnym serwerze.",
    test=[T("Kod 201 oznacza:", ["OK", "Created", "Not Found", "Server Error"], 1, "Po POST."),
          T("requests.get(url) bez timeout:", ["kończy się po 1 s", "może czekać bez końca", "nie działa", "zawsze 200"], 1, "Ustawiaj timeout."),
          T("Serwer zwraca 500 przy złym parametrze. To:", ["poprawne", "błąd serwera do zgłoszenia", "błąd klienta", "brak internetu"], 1, "Złe dane → 4xx."),
          T("Wyjątek łapiący błędy sieci w requests:", ["ValueError", "requests.exceptions.RequestException", "KeyError", "OSError tylko"], 1, "Klasa bazowa.")],
    w_praktyce=["Test API: status, Content-Type, pola i typy, przypadek negatywny, czas odpowiedzi.", "W bug raporcie API: metoda, pełny adres z parametrami, treść żądania, kod i treść odpowiedzi."],
    zrodla=[Z.PY_JSON, Z.FLASK, Z.PY_TUT_ERR],
)

# =========================================================================== TYDZIEŃ 6
DEBUG = L(
    id="debug", nazwa="Debugowanie: print, breakpoint() i debugger krok po kroku", tydzien=6,
    slowa=["debugowanie", "debugger", "breakpoint", "pdb", "krok", "step", "next", "continue", "obserwacja zmiennych", "print debugging", "hipoteza"],
    cel="Po tej lekcji szukasz błędów metodą: odtwórz → zawęź → hipoteza → sprawdź; używasz print z repr, breakpoint() (pdb: n, s, p, c, q) i debuggera w PyCharm (punkt przerwania, Step Over/Into, podgląd zmiennych).",
    po_co="Tester, który potrafi wskazać linię i przyczynę, pisze zgłoszenia, które programista naprawia w minuty, a nie w dni.",
    wymagania=["Lekcje etapu 1 (funkcje, pętle, wyjątki).", "Opcjonalnie PyCharm z interpreterem środowiska kursu."],
    wyjasnienie=(
        "## Metoda zamiast zgadywania\n"
        "1. **Odtwórz**: jakie dane dają zły wynik? Zapisz je. 2. **Zawęź**: która funkcja/linia? 3. **Hipoteza**: „suma liczona jest od 1, nie od 0”. 4. **Sprawdź** jedną zmianą, uruchom ponownie. Zmieniaj jedną rzecz naraz.\n"
        "## print z repr\n"
        "`print(\"DEBUG ilosc=\", repr(ilosc), type(ilosc))` — repr pokazuje cudzysłowy i ukryte znaki (`'12\\n'`). Usuń printy po naprawie.\n"
        "## breakpoint() — debugger w terminalu\n"
        "Wstaw `breakpoint()` w linii, przed którą program ma się zatrzymać, uruchom w terminalu (`python plik.py`). Zobaczysz `(Pdb)`. Polecenia:\n"
        "| polecenie | co robi |\n|---|---|\n"
        "| `p zmienna` | pokaż wartość |\n| `n` (next) | wykonaj linię, nie wchodząc do funkcji |\n| `s` (step) | wejdź do wywoływanej funkcji |\n"
        "| `l` (list) | pokaż kod wokół |\n| `c` (continue) | biegnij do następnego breakpointu |\n| `q` (quit) | zakończ |\n"
        "## Debugger w PyCharm\n"
        "Kliknij na marginesie przy numerze linii — czerwona kropka (breakpoint). Prawy klik → Debug. Program zatrzyma się na kropce; panel Variables pokazuje wszystkie zmienne. "
        "**Step Over** (F8) — następna linia, **Step Into** (F7) — do środka funkcji, **Resume** (F9) — dalej. Warunkowy breakpoint (prawy klik na kropce → Condition: `i == 7`) zatrzyma pętlę dopiero przy 7. obrocie.\n"
        "## Typowe źródła błędów logicznych\n"
        "Pomyłka o jeden (`range(1, n)` zamiast `range(1, n + 1)`), zła kolejność warunków, akumulator w pętli, porównanie napisu z liczbą, zmienna nadpisana w pętli, `=` zamiast `+=`."),
    przyklad=kod("debug", (
        "def srednia_ceny(ceny):\n"
        "    suma = 0\n"
        "    for i in range(1, len(ceny)):\n"
        "        suma += ceny[i]\n"
        "    return suma / len(ceny)\n\n\n"
        "def srednia_ceny_poprawiona(ceny):\n"
        "    if not ceny:\n"
        "        return 0\n"
        "    suma = 0\n"
        "    for cena in ceny:\n"
        "        suma += cena\n"
        "    return suma / len(ceny)\n\n\n"
        "ceny = [4.0, 2.0, 6.0]\n"
        "print(\"Oczekiwane 4.0, otrzymane:\", srednia_ceny(ceny))\n"
        "for i in range(1, len(ceny)):\n"
        "    print(\"DEBUG i =\", i, \"cena =\", repr(ceny[i]))\n"
        "print(\"Po poprawce:\", srednia_ceny_poprawiona(ceny), srednia_ceny_poprawiona([]))\n"), (
        "Oczekiwane 4.0, otrzymane: 2.6666666666666665\nDEBUG i = 1 cena = 2.0\nDEBUG i = 2 cena = 6.0\nPo poprawce: 4.0 0\n")),
    demonstracja={"tytul": "Średnia, która „gubi” pierwszy produkt", "kroki": [
        "Odtworzenie: dla [4.0, 2.0, 6.0] oczekujesz 4.0, program daje 2.67. Dane zapisane — błąd jest powtarzalny.",
        "Zawężenie: dzielenie jest dobre (przez 3), więc zła jest suma: 8 zamiast 12.",
        "Hipoteza: pętla pomija jakiś element. Print debugujący wypisuje i = 1 i 2 — brak i = 0!",
        "Przyczyna: `range(1, len(ceny))` zaczyna od 1 — pomyłka o jeden.",
        "To samo w pdb: wstaw `breakpoint()` przed `for`, uruchom w terminalu, `n` kilka razy i `p i` — zobaczysz 1 jako pierwszą wartość.",
        "Poprawka: pętla po elementach (`for cena in ceny`) i obsługa pustej listy (bez niej `[]` dałoby ZeroDivisionError).",
        "Sprawdzenie: 4.0 dla danych z błędu i 0 dla pustej listy. Usuń printy DEBUG."],
        "wynik": "„otrzymane: 2.6666666666666665”, dwie linie DEBUG (i = 1, i = 2) i „Po poprawce: 4.0 0”."},
    jak_uruchomic=["Zapisz jako debug_demo.py → ▶ Uruchom.", "Wersja z pdb: dopisz `breakpoint()` na początku srednia_ceny → terminal Mentora → `python debug_demo.py` → `n`, `p i`, `p suma`, `c`."],
    cwiczenia=[
        C("prowadzone",
          "Funkcja `def razem(koszyk): suma = 0` / `for cena, ilosc in koszyk: suma = cena * ilosc` / `return suma`. Dla koszyka [(2.0, 3), (5.0, 2)] zwraca 10.0 zamiast 16.0. (1) Ile powinna zwrócić? (2) W której instrukcji jest błąd (wpisz poprawioną linię)? (3) Jaką wartość pokazałoby `p suma` w pdb po pierwszym obrocie pętli? Czas: 15 minut.",
          "(1) 16.0; (2) suma += cena * ilosc; (3) 6.0.",
          ["2 × 3 + 5 × 2.", "= nadpisuje, += dodaje.", "Po pierwszym obrocie suma = 2.0 × 3."],
          "(1) 6 + 10 = 16.0; (2) `suma += cena * ilosc` — `=` nadpisywało sumę; (3) po pierwszym obrocie suma = 6.0.",
          [li("a", "(1) Poprawny wynik", 16.0), tx("b", "(2) Poprawiona linia", "suma += cena * ilosc"), li("c", "(3) p suma po 1. obrocie", 6.0)]),
        C("samodzielne",
          "Pętla 1000 zamówień czasem daje zły wynik dla jednego z nich (nr 742). (1) Który sposób jest najszybszy do zbadania: breakpoint w pętli i 742 razy Continue / breakpoint warunkowy `nr == 742` / print wszystkich 1000 zamówień? (2) Jakie polecenie pdb wejdzie do środka wywoływanej funkcji (wpisz literę)? (3) Po znalezieniu błędu — co robisz najpierw: poprawiasz kod / zapisujesz dane, które go wywołują (do testu)? Czas: 15 minut.",
          "(1) breakpoint warunkowy nr == 742; (2) s; (3) zapisujesz dane, które go wywołują.",
          ["Debugger umie zatrzymać się tylko przy spełnionym warunku.", "step = wejdź do środka.", "Dane z błędu to gotowy przypadek testowy na przyszłość."],
          "(1) breakpoint warunkowy (`nr == 742`); (2) `s` (step); (3) najpierw zapisz dane wejściowe (staną się testem regresji w tygodniu 7), potem poprawiaj.",
          [wy("a", "(1) Najszybszy sposób", ["breakpoint i 742 × Continue", "breakpoint warunkowy nr == 742", "print wszystkich 1000"], "breakpoint warunkowy nr == 742"), tx("b", "(2) Polecenie pdb", "s"),
           wy("c", "(3) Najpierw", ["poprawiasz kod", "zapisujesz dane, które go wywołują"], "zapisujesz dane, które go wywołują")]),
    ],
    typowe_bledy=[
        B("breakpoint() nic nie robi w Mentorze", "Przycisk ▶ uruchamia program bez interaktywnej konsoli pdb.", "Gdzie uruchamiasz?", "Uruchom w terminalu (`python plik.py`) albo w debuggerze PyCharm."),
        B("PyCharm: Debug nie zatrzymuje się na kropce", "Linia nigdy nie jest wykonywana albo uruchomiono Run zamiast Debug.", "Czy kod dochodzi do tej linii?", "Debug (ikona robaka); kropka w linii, która na pewno się wykona."),
    ],
    pulapki=["Zmiana kilku rzeczy naraz — nie wiesz, co naprawiło błąd.", "Zostawione printy DEBUG w kodzie oddanym do recenzji."],
    zadania=["Program z 3 ukrytymi błędami z paczki kursu: znajdź każdy debuggerem i zapisz przyczynę.", "Dla każdego błędu zapisz dane, które go wywołują.", "Przećwicz pdb: n, s, p, c, q."],
    pytania=[["Jakie są 4 kroki debugowania?", "Odtwórz, zawęź, hipoteza, sprawdź."], ["Czym różni się step od next?", "step wchodzi do funkcji, next wykonuje linię w całości."], ["Po co repr() w printach?", "Pokazuje typ/ukryte znaki (cudzysłowy, \\n)."]],
    podsumowanie="Szukasz błędów metodą odtwórz–zawęź–hipoteza–sprawdź, używasz print z repr, pdb i debuggera PyCharm (także warunkowego breakpointu).",
    test=[T("Pierwszy krok debugowania:", ["zmienić kod", "odtworzyć błąd na konkretnych danych", "przeinstalować Pythona", "zapytać AI"], 1, "Bez odtworzenia nie sprawdzisz poprawki."),
          T("Polecenie pdb pokazujące wartość zmiennej x:", ["show x", "p x", "x?", "print x()"], 1, "p = print."),
          T("range(1, len(l)) w sumie pomija:", ["ostatni element", "pierwszy element", "nic", "co drugi"], 1, "Indeks 0."),
          T("Warunkowy breakpoint przydaje się, gdy:", ["program jest krótki", "błąd występuje przy konkretnej iteracji", "nie ma błędu", "zawsze"], 1, "Zatrzymuje tylko przy warunku.")],
    w_praktyce=["W bug raporcie: dane wejściowe, które odtwarzają błąd, i (jeśli znasz) linia przyczyny.", "Dane z każdego znalezionego błędu → nowy test regresji."],
    zrodla=[Z.PY_PDB, Z.PYCHARM, Z.ISTQB_SLOWNIK],
)

README = L(
    id="readme", nazwa="README, docstringi, PEP 8 i refaktoryzacja", tydzien=6,
    slowa=["README", "Markdown", "docstring", "PEP 8", "refaktoryzacja", "nazwy", "funkcja", "duplikacja", "magiczna liczba", "czytelność", "portfolio"],
    cel="Po tej lekcji piszesz README projektu (co robi, jak uruchomić, przykład, jak testować) w Markdown, dokumentujesz funkcje docstringami, poprawiasz styl wg PEP 8 i refaktoryzujesz kod (nazwy, wydzielenie funkcji, stałe) bez zmiany działania.",
    po_co="Rekruter otwiera README zanim spojrzy na kod. Czytelny, udokumentowany kod pokazuje, że umiesz pracować w zespole — to waży więcej niż liczba projektów.",
    wymagania=["Projekty z tygodni 1–5 w repozytorium.", "Lekcje „Funkcje” i „Moduły”."],
    wyjasnienie=(
        "## README.md — wizytówka projektu\n"
        "GitHub pokazuje README.md na stronie repozytorium. Markdown: `# Tytuł`, `## Sekcja`, `- lista`, `` `kod` ``, blok kodu w potrójnych odwrotnych apostrofach, `**pogrubienie**`, link `[tekst](adres)`, obraz `![opis](zrzut.png)`.\n"
        "Minimum dla projektu w portfolio:\n"
        "1. **Tytuł i jedno zdanie**: co robi i dla kogo.\n"
        "2. **Jak uruchomić**: kroki od sklonowania (`git clone`, venv, `pip install -r requirements.txt`, `python main.py`).\n"
        "3. **Przykład użycia**: wejście → wynik (blok kodu albo zrzut ekranu).\n"
        "4. **Jak testować**: polecenie `pytest -v` i co jest testowane.\n"
        "5. **Technologie** i ewentualnie „Co dalej” (znane ograniczenia).\n"
        "## Docstring\n"
        "Krótko: pierwsza linia — co robi funkcja (tryb rozkazujący lub opis), potem parametry, wynik, wyjątki. Konwencja PEP 257.\n"
        "## PEP 8 — wspólny styl\n"
        "Wcięcia 4 spacje, linie do ok. 79–100 znaków, nazwy `snake_case` dla funkcji i zmiennych, `CamelCase` dla klas, `WIELKIE_LITERY` dla stałych, spacje wokół operatorów (`a + b`), dwie puste linie między funkcjami. PyCharm podkreśla naruszenia; Code → Reformat Code poprawia formatowanie.\n"
        "## Refaktoryzacja\n"
        "Zmiana budowy kodu **bez zmiany działania**. Przed refaktoryzacją uruchom i zapisz wyniki (albo testy) — po refaktoryzacji muszą być identyczne. Typowe ruchy:\n"
        "- lepsze nazwy (`x` → `cena_brutto`);\n"
        "- wydzielenie funkcji z powtarzanego fragmentu;\n"
        "- **magiczne liczby** w stałe (`0.23` → `VAT = 0.23`);\n"
        "- logika z input()/print() do funkcji z return (testowalność)."),
    przyklad=kod("readme", (
        "VAT = 0.23\n"
        "PROG_DARMOWEJ_DOSTAWY = 100\n"
        "KOSZT_DOSTAWY = 14.99\n\n\n"
        "def brutto(netto):\n"
        "    \"\"\"Zwraca cenę brutto zaokrągloną do groszy.\"\"\"\n"
        "    return round(netto * (1 + VAT), 2)\n\n\n"
        "def do_zaplaty(ceny_netto):\n"
        "    \"\"\"Suma brutto koszyka plus dostawa (darmowa od PROG_DARMOWEJ_DOSTAWY zł).\n\n"
        "    ceny_netto: lista cen netto; pusta lista → 0.\n"
        "    \"\"\"\n"
        "    if not ceny_netto:\n"
        "        return 0\n"
        "    suma = round(sum(brutto(c) for c in ceny_netto), 2)\n"
        "    dostawa = 0 if suma >= PROG_DARMOWEJ_DOSTAWY else KOSZT_DOSTAWY\n"
        "    return round(suma + dostawa, 2)\n\n\n"
        "print(do_zaplaty([10, 20]), do_zaplaty([50, 40]), do_zaplaty([]))\n"
        "print(do_zaplaty.__doc__.splitlines()[0])\n"), "51.89 110.7 0\nSuma brutto koszyka plus dostawa (darmowa od PROG_DARMOWEJ_DOSTAWY zł).\n"),
    demonstracja={"tytul": "Refaktoryzacja: z „x * 1.23 + 14.99” do czytelnych funkcji", "kroki": [
        "Wersja przed (w głowie): `def f(x): s = 0; for i in x: s = s + i * 1.23; if s < 100: s = s + 14.99; return s` — działa, ale nic nie mówi.",
        "Stałe `VAT`, `PROG_DARMOWEJ_DOSTAWY`, `KOSZT_DOSTAWY` zamiast liczb rozsianych po kodzie — zmiana VAT w jednym miejscu.",
        "Wydzielona `brutto(netto)` — mała funkcja, łatwa do przetestowania osobno.",
        "`do_zaplaty` z nazwą mówiącą, co zwraca, i docstringiem z opisem parametru i przypadku pustej listy.",
        "Sprawdzenie, że działanie się nie zmieniło: 10 + 20 netto → 36.90 brutto + 14.99 = 51.89; 90 netto → 110.70 (darmowa dostawa).",
        "`__doc__` — docstring jest dostępny w programie (i w help())."],
        "wynik": "„51.89 110.7 0” i pierwsza linia docstringu."},
    jak_uruchomic=["Zapisz jako koszyk_refaktor.py → ▶ Uruchom.", "README: utwórz README.md w katalogu projektu, wyślij na GitHub i sprawdź podgląd na stronie repozytorium."],
    cwiczenia=[
        C("prowadzone",
          "Na wzór demonstracji policz `do_zaplaty` dla: (1) [50, 31.3] netto, (2) [81.31] netto, (3) [81.30] netto. Czas: 15 minut.",
          "(1) 100.00 (darmowa dostawa); (2) 100.01; (3) 100.00 — po zaokrągleniu brutto do groszy próg 100 zł jest osiągnięty.",
          ["Najpierw brutto każdej ceny (× 1.23, round 2).", "Porównaj sumę brutto z progiem 100.", "81.31 × 1.23 = 100.0113 → 100.01."],
          "(1) 50 × 1.23 = 61.50 i 31.3 × 1.23 = 38.499 → 38.50; suma 100.00 ≥ 100 → dostawa darmowa → 100.00. (2) 81.31 × 1.23 = 100.0113 → 100.01, dostawa darmowa → 100.01. (3) 81.30 × 1.23 = 99.999 → round do groszy daje 100.00 → próg osiągnięty → 100.00. Wniosek testera: zaokrąglenie przed porównaniem z progiem zmienia wynik — to warto opisać w wymaganiach.",
          [kw("a", "(1) [50, 31.3]", 100.00), kw("b", "(2) [81.31]", 100.01), kw("c", "(3) [81.30]", 100.00, bledy=[bl(114.98, "round(99.999, 2) = 100.0 — próg osiągnięty, dostawa darmowa")])]),
        C("samodzielne",
          "Oceń README (tak/nie — czy jest wystarczające): „# kalkulator\\nmój projekt”. Wybierz, czego brakuje najbardziej (jedna odpowiedź): jak uruchomić / kolor tła / lista commitów. Następnie oceń nazwy wg PEP 8 (dobra/zła): (1) `def ObliczRabat(x):`, (2) `MAX_RABAT = 30`, (3) `class kalkulator:`, (4) `def cena_po_rabacie(cena, procent):`. Czas: 15 minut.",
          "README: nie; brakuje: jak uruchomić. (1) zła; (2) dobra; (3) zła; (4) dobra.",
          ["Czy ktoś obcy uruchomi projekt z tego README?", "Funkcje snake_case, klasy CamelCase, stałe WIELKIMI.", "x jako nazwa parametru też niewiele mówi."],
          "README niewystarczające — brak „jak uruchomić” (i opisu, przykładu, testów). (1) zła (funkcja snake_case: oblicz_rabat; i nazwa parametru x); (2) dobra (stała); (3) zła (Kalkulator); (4) dobra.",
          [wy("r", "README wystarczające?", ["tak", "nie"], "nie"), wy("b", "Czego brakuje najbardziej", ["jak uruchomić", "kolor tła", "lista commitów"], "jak uruchomić"),
           wy("n1", "(1) def ObliczRabat(x):", ["dobra", "zła"], "zła"), wy("n2", "(2) MAX_RABAT = 30", ["dobra", "zła"], "dobra"), wy("n3", "(3) class kalkulator:", ["dobra", "zła"], "zła"),
           wy("n4", "(4) def cena_po_rabacie(…)", ["dobra", "zła"], "dobra")]),
    ],
    typowe_bledy=[
        B("Po refaktoryzacji inny wynik", "Zmiana działania przy okazji „porządków”.", "Porównaj wyniki przed/po na tych samych danych.", "Refaktoryzuj małymi krokami, po każdym uruchom testy."),
        B("README na GitHubie bez formatowania", "Plik nazwany README.txt albo brak pustej linii przed listą/nagłówkiem.", "Nazwa pliku i podgląd.", "README.md; puste linie wokół bloków Markdown."),
    ],
    pulapki=["README pisane na końcu „na szybko” — pisz je od początku i aktualizuj z kodem.", "Refaktoryzacja bez testów to zgadywanie — od tygodnia 7 zawsze najpierw testy."],
    zadania=["README dla każdego projektu: opis, jak uruchomić, przykład, jak testować.", "Docstringi do wszystkich funkcji kalkulatora BMI i zgadywanki.", "Refaktoryzacja BMI: funkcje oblicz_bmi i kategoria, stałe progów."],
    pytania=[["Co musi mieć README?", "Co robi, jak uruchomić, przykład, jak testować."], ["Czym jest refaktoryzacja?", "Zmiana budowy kodu bez zmiany działania."], ["Co to magiczna liczba?", "Liczba bez nazwy w kodzie (np. 0.23) — zamieniasz na stałą."]],
    podsumowanie="Piszesz README, które pozwala obcej osobie uruchomić projekt, dokumentujesz funkcje, trzymasz się PEP 8 i refaktoryzujesz kod bez zmiany działania.",
    test=[T("Nazwa funkcji zgodna z PEP 8:", ["LiczSume", "licz_sume", "LICZ_SUME", "liczSume"], 1, "snake_case."),
          T("Refaktoryzacja zmienia:", ["działanie programu", "budowę kodu, nie działanie", "wymagania", "testy na zielono"], 1, "Działanie zostaje."),
          T("Pierwsza sekcja, której szuka obca osoba w README:", ["licencja", "jak uruchomić", "historia", "podziękowania"], 1, "Uruchomienie."),
          T("Docstring umieszczasz:", ["na końcu pliku", "jako pierwszy napis w funkcji", "w README", "w komentarzu #"], 1, "PEP 257.")],
    w_praktyce=["Recenzując kod: nazwy, długość funkcji, duplikacje, magiczne liczby, brak docstringów.", "README każdego projektu w portfolio sprawdź „oczami rekrutera”: 30 sekund i wiesz, co to jest?"],
    zrodla=[Z.PY_PEP8, Z.PY_PEP257, Z.GH_README],
)

POWTORKA2 = L(
    id="powtorka_projekt", nazwa="Powtórka etapu 2: projekt jak w zespole — struktura, Git, środowisko, czytanie cudzego kodu", tydzien=6,
    slowa=["powtórka", "etap 2", "struktura projektu", "czytanie kodu", "cudzy kod", "recenzja", "checklista", "portfolio", "repozytorium"],
    cel="Po tej lekcji porządkujesz repozytorium jak w zespole (struktura, README, .gitignore, requirements.txt, historia commitów), czytasz cudzy projekt metodą „od wejścia do szczegółów” i oceniasz repozytorium listą kontrolną rekrutera.",
    po_co="Pierwsze dni w pracy QA to czytanie cudzego kodu i uruchamianie cudzego projektu. Twoje repozytorium jest pierwszym projektem, który przeczyta rekruter.",
    wymagania=["Lekcje tygodni 4–6.", "Projekt do przeczytania z paczki kursu: projekty/cudzy_projekt/ (Mój projekt → Skopiuj materiały kursu)."],
    wyjasnienie=(
        "## Czytanie cudzego projektu — od wejścia do szczegółów\n"
        "1. README i struktura katalogów (co jest czym?). 2. Plik startowy (main.py / app.py) — od `if __name__ == \"__main__\":`. 3. Importy — mapa zależności między plikami. "
        "4. Nazwy i docstringi funkcji — bez wchodzenia w szczegóły. 5. Uruchom z przykładowymi danymi. 6. Dopiero teraz szczegóły jednej funkcji (debugger krok po kroku).\n"
        "Zapisuj w notatkach: plik → odpowiedzialność → najważniejsze funkcje → pytania.\n"
        "## Mapa etapu 2\n"
        "| temat | umiesz, gdy… |\n|---|---|\n"
        "| pliki, CSV | czytasz CSV do listy słowników i liczysz statystyki z float/int |\n"
        "| Git w zespole | gałąź → PR → merge; restore/stash/revert bez paniki |\n"
        "| klasy | piszesz klasę z walidacją w metodach |\n"
        "| moduły | dzielisz program na pliki z jedną odpowiedzialnością |\n"
        "| venv | odtwarzasz środowisko z requirements.txt |\n"
        "| API | GET z timeout, kody HTTP, JSON, błędy sieci |\n"
        "| debugowanie | odtwórz → zawęź → hipoteza → sprawdź |\n"
        "| README | obca osoba uruchamia projekt bez pytań |\n"
        "## Lista kontrolna rekrutera (repozytorium)\n"
        "- README z opisem, uruchomieniem i przykładem; - .gitignore (brak .venv, __pycache__, .env); - requirements.txt; - czytelna struktura (folder na projekt); - commity z opisami („Dodaj…”, „Popraw…”), nie „asdf”; - brak haseł/kluczy w historii; - kod z funkcjami i docstringami."),
    przyklad=("python-projekty/\n"
              "├── README.md              ← tabela: projekt | co robi | technologie | link\n"
              "├── .gitignore             ← .venv/ __pycache__/ .env\n"
              "├── kalkulator_bmi/\n"
              "│   ├── README.md\n"
              "│   └── bmi.py             ← oblicz_bmi(), kategoria(), blok __main__\n"
              "├── zgadnij_liczbe/\n"
              "│   ├── README.md\n"
              "│   └── zgadnij.py\n"
              "├── menedzer_zadan/\n"
              "│   ├── README.md\n"
              "│   ├── main.py  zadania.py  plik.py\n"
              "└── raport_cen/\n"
              "    ├── README.md  requirements.txt\n"
              "    └── api.py  raport.py\n\n"
              "git log --oneline (fragment):\n"
              "a1b2c3d Dodaj README dla raportu cen\n"
              "9f8e7d6 Popraw obsługę braku połączenia w api.py\n"
              "5c4b3a2 Wydziel zapis CSV do raport.py"),
    demonstracja={"tytul": "Repozytorium portfolio po porządkach", "kroki": [
        "Jedno repozytorium python-projekty z folderem na każdy projekt — rekruter widzi całość w jednym miejscu.",
        "Główny README.md: tabela projektów z linkami do folderów (Markdown: `[menedżer zadań](menedzer_zadan/)`).",
        "Każdy projekt ma własny README z „Jak uruchomić”.",
        ".gitignore w katalogu głównym działa dla wszystkich podfolderów.",
        "Projekty z bibliotekami mają requirements.txt.",
        "Historia commitów opisuje zmiany — widać sposób pracy.",
        "Przeniesienie plików do folderów: `git mv bmi.py kalkulator_bmi/bmi.py` — Git zachowa historię pliku."],
        "wynik": "Repozytorium, które obca osoba uruchamia bez pytań, a rekruter rozumie w 30 sekund."},
    jak_uruchomic=["Terminal w repozytorium: `git mv` dla przenoszenia plików, potem commit i push.", "GitHub → strona repozytorium → sprawdź, jak wygląda README."],
    cwiczenia=[
        C("prowadzone",
          "Czytasz cudzy projekt: pliki app.py (`if __name__ == \"__main__\": uruchom()`), baza.py (funkcje zapisz/wczytaj), raport.py (funkcja raport_miesieczny), README.md. (1) Od którego pliku zaczniesz czytać? (2) Który plik pierwszy otworzysz z kodu? (3) Gdzie szukasz odpowiedzi „skąd biorą się dane”? Opcje: README.md / app.py / baza.py / raport.py. Czas: 10 minut.",
          "(1) README.md; (2) app.py; (3) baza.py.",
          ["Najpierw opis.", "Wejście programu.", "Zapis i odczyt danych."],
          "(1) README.md; (2) app.py — punkt startowy; (3) baza.py — warstwa danych.",
          [wy("a", "(1) Najpierw", ["README.md", "app.py", "baza.py", "raport.py"], "README.md"), wy("b", "(2) Pierwszy kod", ["README.md", "app.py", "baza.py", "raport.py"], "app.py"),
           wy("c", "(3) Skąd dane", ["README.md", "app.py", "baza.py", "raport.py"], "baza.py")]),
        C("samodzielne",
          "Oceń repozytorium listą kontrolną (spełnia: tak/nie): (1) README: „# projekt” i nic więcej; (2) w repozytorium jest folder .venv z 3000 plików; (3) commity: „zmiany”, „asdf”, „final”, „final2”; (4) plik config.py z `API_KEY = \"sk-…\"`; (5) każdy projekt w osobnym folderze. Który problem naprawiasz PIERWSZY (wybierz numer 1–5)? Czas: 15 minut.",
          "(1) nie; (2) nie; (3) nie; (4) nie; (5) tak; pierwszy: 4 (klucz API — natychmiast unieważnić i usunąć).",
          ["Co jest zagrożeniem bezpieczeństwa, a co tylko estetyką?", "Klucz w publicznym repo boty znajdują w minuty.", "Usunięcie pliku nie usuwa klucza z historii."],
          "(1)–(4) nie, (5) tak. Pierwszy: (4) — unieważnij klucz u dostawcy, usuń z kodu, przenieś do .env w .gitignore. Potem .venv (git rm --cached), README, a stare commity zostaw — nowe pisz porządnie.",
          [wy("a", "(1) README", ["tak", "nie"], "nie"), wy("b", "(2) .venv", ["tak", "nie"], "nie"), wy("c", "(3) commity", ["tak", "nie"], "nie"), wy("d", "(4) klucz w config.py", ["tak", "nie"], "nie"),
           wy("e", "(5) foldery projektów", ["tak", "nie"], "tak"), li("pierwszy", "Naprawiasz pierwszy (nr)", 4)]),
    ],
    typowe_bledy=[
        B("Po przeniesieniu plików importy nie działają", "Moduły w różnych folderach, a import zakłada ten sam katalog.", "Uruchom z folderu projektu.", "Każdy projekt uruchamiaj z jego folderu (cd kalkulator_bmi)."),
        B("Historia pliku „zniknęła” po przeniesieniu", "Przeniesienie w Eksploratorze + nowy plik.", "`git log --follow nowa/sciezka.py`.", "Przenoś `git mv` — historia zostaje."),
    ],
    pulapki=["Czytanie cudzego kodu od pierwszej linii najdłuższego pliku — zaczynaj od README i punktu wejścia.", "Ukrywanie słabych projektów — lepiej 4 porządne niż 10 bałaganu."],
    zadania=["Przeczytaj projekty/cudzy_projekt i opisz każdy plik w notatki_projekt.md.", "Uporządkuj repozytorium python-projekty wg listy kontrolnej.", "Popraw README każdego projektu."],
    pytania=[["Od czego zaczynasz czytanie cudzego projektu?", "README i struktura, potem punkt wejścia."], ["Co sprawdza rekruter w repozytorium?", "README, porządek, commity, brak sekretów, czytelny kod."], ["Jak przenieść plik z zachowaniem historii?", "git mv."]],
    podsumowanie="Porządkujesz repozytorium jak w zespole, czytasz cudzy projekt od wejścia do szczegółów i oceniasz kod listą kontrolną rekrutera.",
    test=[T("Klucz API znaleziony w publicznym repo. Pierwszy krok:", ["usunąć plik", "unieważnić klucz u dostawcy", "zmienić nazwę pliku", "nic"], 1, "Klucz z historii i tak wyciekł."),
          T("git mv:", ["kopiuje plik na GitHub", "przenosi plik z zachowaniem historii", "usuwa plik", "scala gałęzie"], 1, "move."),
          T("Punkt wejścia programu najczęściej znajdziesz:", ["w README", "w bloku if __name__ == \"__main__\":", "w .gitignore", "w requirements.txt"], 1, "Start programu."),
          T("Lepsze portfolio:", ["10 projektów bez README", "4 projekty z README i testami", "1 plik na 2000 linii", "same zrzuty ekranu"], 1, "Jakość > ilość.")],
    w_praktyce=["Pierwszy dzień w projekcie: README → uruchom → testy → struktura → pytania do zespołu.", "Przed wysłaniem CV: przejdź listę kontrolną na każdym repo."],
    zrodla=[Z.GH_README, Z.GIT_PL, Z.PY_PEP8],
)
