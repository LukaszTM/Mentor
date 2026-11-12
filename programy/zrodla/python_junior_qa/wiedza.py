# -*- coding: utf-8 -*-
"""
Baza wiedzy trybu OFFLINE Asystenta — tematy z 12 tygodni, błędy Pythona, pojęcia.

Każdy temat: słowa kluczowe (do rozpoznania w promptach), wyjaśnienie z przykładami z gospodarstwa,
3 zadania rosnącej trudności (bez rozwiązań), pytania sprawdzające, pułapki.
To nie jest model językowy — to podręcznik, który Asystent czyta za Ciebie. Możesz go rozbudować.
"""

TEMATY = [
    {"id": "zmienne", "tydzien": 1, "nazwa": "Zmienne i typy danych",
     "slowa": ["zmienn", "typ", "int", "float", "str", "bool", "type("],
     "wyjasnienie":
         "Zmienna to etykieta na pudełku z wartością. W oborze masz tabliczkę „Krasula — 612 kg”: tabliczka to nazwa "
         "zmiennej, 612 to wartość. Możesz tabliczkę przepiąć na inną wartość (waga = 620), a Python pamięta ostatnią.\n"
         "Każda wartość ma typ: int (liczba całkowita: 14 krów), float (z przecinkiem: 612.5 kg), str (napis: \"Krasula\"), "
         "bool (prawda/fałsz: czy_szczepiona = True). Typ sprawdzasz funkcją type(). Python nie pozwala dodać napisu do liczby: "
         "\"612\" + 8 to błąd — \"612\" to tekst, nie liczba. Zamieniasz typ funkcjami int(), float(), str().",
     "przyklad":
         "imie = \"Krasula\"        # str\n"
         "waga_kg = 612.5          # float\n"
         "liczba_cielat = 3        # int\n"
         "szczepiona = True        # bool\n"
         "print(imie, type(imie))\n"
         "print(waga_kg + 10)      # 622.5\n"
         "print(\"Waga: \" + str(waga_kg))  # bez str() byłby błąd",
     "zadania": [
         "Utwórz 5 zmiennych opisujących jedno zwierzę (imię, waga, wiek w latach, rasa, czy zdrowe) i wypisz każdą z jej type().",
         "Zapisz w zmiennych liczbę krów, cen mleka za litr i wydajność dzienną na krowę; policz i wypisz dzienny przychód.",
         "Wczytaj wagę z input(), zamień na float, dodaj 25 i wypisz zdanie „Po tuczu: X kg” — sklejając napis z liczbą poprawnie."],
     "pytania": [("Co zwróci type(\"14\")?", "str — bo jest w cudzysłowie, to napis mimo cyfr."),
                 ("Jak zamienić napis \"612\" na liczbę całkowitą?", "int(\"612\")"),
                 ("Dlaczego \"Waga: \" + 612 to błąd?", "Nie można skleić napisu z liczbą; trzeba str(612).")],
     "pulapki": ["input() ZAWSZE zwraca str — nawet gdy użytkownik wpisze liczbę.",
                 "Nazwy zmiennych: waga_kg mówi więcej niż w. Małe litery, podkreślenia, bez polskich znaków."]},

    {"id": "input_print", "tydzien": 1, "nazwa": "print i input",
     "slowa": ["input", "print", "wypisz", "wczyt"],
     "wyjasnienie":
         "print() wypisuje na ekran, input() pyta użytkownika i zwraca to, co wpisał — zawsze jako napis. "
         "To jak zapisanie na kartce odpowiedzi sąsiada: nawet gdy powie „sześćset”, na kartce masz tekst, nie liczbę do liczenia. "
         "Żeby liczyć, zamieniasz: int(input(\"Ile krów? \")). print przyjmuje wiele argumentów oddzielonych przecinkiem "
         "i sam wstawia spacje; f-string (f\"Waga: {waga} kg\") pozwala wstawić zmienną w środek napisu.",
     "przyklad":
         "ile = int(input(\"Ile krów masz w oborze? \"))\n"
         "print(\"Masz\", ile, \"krów\")\n"
         "print(f\"Za rok możesz mieć {ile * 2} krów\")",
     "zadania": ["Zapytaj o imię i wiek zwierzęcia, wypisz zdanie z f-stringa.",
                 "Zapytaj o litry mleka dziennie i cenę skupu; wypisz miesięczny przychód z dwoma miejscami po przecinku (f\"{x:.2f}\").",
                 "Zapytaj o trzy wagi, policz średnią i wypisz ją — pamiętaj o zamianie typów."],
     "pytania": [("Jakiego typu jest wynik input()?", "Zawsze str."),
                 ("Co wypisze print(\"a\", \"b\")?", "a b — print wstawia spację między argumentami."),
                 ("Jak wstawić zmienną w środek napisu?", "f\"...{zmienna}...\"")],
     "pulapki": ["int(input()) wywali się, gdy użytkownik wpisze litery — tydzień 3 (try/except) to naprawia."]},

    {"id": "warunki", "tydzien": 1, "nazwa": "Instrukcje warunkowe if / elif / else",
     "slowa": ["if", "elif", "else", "warun", "porówn", "==", "progi"],
     "wyjasnienie":
         "if to rozwidlenie drogi: jeśli warunek prawdziwy — idziesz jedną ścieżką, w przeciwnym razie (else) drugą. "
         "elif to kolejne rozwidlenia po drodze. Przykład z gospodarstwa: jeśli temperatura < 0 — włącz ogrzewanie w kurniku; "
         "elif temperatura > 30 — włącz wentylację; else — nic nie rób. Skup mleka z progami cenowymi: jeśli tłuszcz > 4.0 — "
         "cena 2.10; elif > 3.5 — 1.90; else — 1.70.\n"
         "Porównania: == (równe), != (różne), <, >, <=, >=. Warunki łączysz przez and, or, not. "
         "Blok pod if wcinasz czterema spacjami — wcięcie mówi Pythonowi, co należy do warunku.",
     "przyklad":
         "tluszcz = float(input(\"Zawartość tłuszczu (%): \"))\n"
         "if tluszcz > 4.0:\n"
         "    cena = 2.10\n"
         "elif tluszcz > 3.5:\n"
         "    cena = 1.90\n"
         "else:\n"
         "    cena = 1.70\n"
         "print(f\"Cena skupu: {cena} zł/l\")",
     "zadania": ["Program pyta o wiek krowy i wypisuje: cielę (<1), jałówka (1–2), krowa (>2).",
                 "Kalkulator z dzieleniem: zanim podzielisz, sprawdź if-em, czy dzielnik to zero, i wypisz komunikat zamiast błędu.",
                 "Trzy progi cenowe za mleko + dopłata 0.10 zł, gdy dostawa > 500 l (dwa warunki połączone and)."],
     "pytania": [("Czym różni się = od ==?", "= przypisuje wartość, == porównuje."),
                 ("Ile bloków może wykonać się w łańcuchu if/elif/else?", "Dokładnie jeden — pierwszy, którego warunek jest prawdziwy."),
                 ("Co znaczy: if not szczepiona:?", "Wykona się, gdy szczepiona jest False.")],
     "pulapki": ["Zapomniany dwukropek po warunku — SyntaxError.", "Mieszanie tabulatorów i spacji we wcięciach — IndentationError."]},

    {"id": "petle", "tydzien": 2, "nazwa": "Pętle for i while",
     "slowa": ["pętl", "petl", "for ", "while", "range", "break", "continue", "iterac"],
     "wyjasnienie":
         "Pętla powtarza czynność. for przechodzi po kolekcji: „dla każdej krowy w stadzie: zważ ją” — wiesz z góry, ile obrotów. "
         "while powtarza, dopóki warunek jest prawdziwy: „dopóki zbiornik nie pełny: dolewaj” — liczba obrotów zależy od sytuacji.\n"
         "range(5) daje 0,1,2,3,4 (od zera, do pięciu wyłącznie); range(1, 11) daje 1..10. "
         "break wychodzi z pętli natychmiast (znalazłeś chore zwierzę — przerwij obchód), continue pomija resztę bieżącego obrotu "
         "i idzie do następnego (ta krowa zdrowa — następna). Pętla while bez zmiany warunku kręci się w nieskończoność.",
     "przyklad":
         "stado = [\"Krasula\", \"Mućka\", \"Łaciata\"]\n"
         "for krowa in stado:\n"
         "    print(\"Ważę:\", krowa)\n\n"
         "suma = 0\n"
         "while True:\n"
         "    litry = int(input(\"Litry (0 = koniec): \"))\n"
         "    if litry == 0:\n"
         "        break\n"
         "    suma += litry\n"
         "print(\"Razem:\", suma)",
     "zadania": ["Tabliczka mnożenia 1–10 pętlą for (potem spróbuj dwóch zagnieżdżonych pętli).",
                 "Pętla while sumuje wpisywane liczby aż do 0; na końcu wypisz sumę, średnią i maksimum.",
                 "Gra „zgadnij liczbę” 1–100 z podpowiedziami „za mało/za dużo” i licznikiem prób (random.randint)."],
     "pytania": [("Co wypisze for i in range(3): print(i)?", "0, 1, 2."),
                 ("Czym różni się break od continue?", "break kończy pętlę; continue przeskakuje do następnego obrotu."),
                 ("Kiedy użyć while zamiast for?", "Gdy nie wiesz z góry, ile razy powtarzać — np. do wpisania 0.")],
     "pulapki": ["range kończy PRZED ostatnią liczbą.", "W while pamiętaj o zmianie warunku — inaczej pętla nieskończona (Ctrl+C przerywa)."]},

    {"id": "listy", "tydzien": 2, "nazwa": "Listy",
     "slowa": ["list", "append", "remove", "len(", "indeks", "sort"],
     "wyjasnienie":
         "Lista to uporządkowany ciąg wartości w nawiasach kwadratowych: stado = [\"Krasula\", \"Mućka\"]. "
         "Jak rząd stanowisk w oborze: każde ma numer (indeks) od 0. stado[0] to pierwsza krowa, stado[-1] ostatnia. "
         "Dodajesz na koniec append(), wstawiasz insert(i, x), usuwasz remove(x) lub pop(i), liczysz len(), sortujesz sort(). "
         "Listę można zmieniać po utworzeniu (w odróżnieniu od krotki). Sprawdzasz obecność: if \"Mućka\" in stado.",
     "przyklad":
         "wagi = [612, 580, 640]\n"
         "wagi.append(595)\n"
         "print(len(wagi), max(wagi), sum(wagi) / len(wagi))\n"
         "wagi.sort()\n"
         "print(wagi[0], wagi[-1])   # najlżejsza, najcięższa\n"
         "for nr, w in enumerate(wagi, start=1):\n"
         "    print(nr, w)",
     "zadania": ["Lista 5 produktów do zakupu: dodaj, usuń, wypisz z numerami (enumerate).",
                 "Lista wag zwierząt: wypisz najcięższe, najlżejsze i te powyżej średniej.",
                 "Ranking najlepszych wyników w grze: dodawaj wynik, sortuj, trzymaj tylko 5 najlepszych."],
     "pytania": [("Jaki indeks ma pierwszy element?", "0."),
                 ("Jak dodać element na koniec?", "lista.append(x)"),
                 ("Co zwróci [1,2,3][-1]?", "3 — ujemny indeks liczy od końca.")],
     "pulapki": ["lista[len(lista)] to IndexError — ostatni element ma indeks len-1.", "sort() sortuje w miejscu i zwraca None."]},

    {"id": "napisy", "tydzien": 2, "nazwa": "Napisy i ich metody",
     "slowa": ["napis", "string", "upper", "lower", "split", "strip", "samogłos", "od tyłu", "[::-1]"],
     "wyjasnienie":
         "Napis (str) to ciąg znaków; możesz go traktować jak listę liter: tekst[0], tekst[-1], tekst[::-1] (od tyłu), len(tekst). "
         "Metody: upper()/lower() (wielkość liter), strip() (obcina spacje z brzegów — ważne po input()), split() (dzieli na listę słów), "
         "replace(a, b), count(x), startswith(). Napisy są niezmienne — metody zwracają NOWY napis, oryginał zostaje. "
         "Przykład: etykieta z mleczarni „  kRASULA ” → .strip().capitalize() daje „Krasula”.",
     "przyklad":
         "tekst = input(\"Wpisz zdanie: \").strip()\n"
         "print(tekst.upper())\n"
         "print(tekst[::-1])\n"
         "samogloski = 0\n"
         "for litera in tekst.lower():\n"
         "    if litera in \"aeiouyąęó\":\n"
         "        samogloski += 1\n"
         "print(\"Samogłosek:\", samogloski)",
     "zadania": ["Podany tekst wypisz wielkimi literami, od tyłu i policz samogłoski.",
                 "Policz słowa w zdaniu (split) i wypisz najdłuższe.",
                 "Sprawdź, czy słowo jest palindromem (kajak) — ignorując wielkość liter."],
     "pytania": [("Co zwraca \"abc\".upper()?", "\"ABC\""),
                 ("Czy tekst.upper() zmienia tekst?", "Nie — zwraca nowy napis; trzeba przypisać wynik."),
                 ("Jak odwrócić napis?", "tekst[::-1]")],
     "pulapki": ["\"5\" + \"5\" to \"55\", nie 10.", "Po input() często zostaje spacja na końcu — strip()."]},

    {"id": "funkcje", "tydzien": 3, "nazwa": "Funkcje",
     "slowa": ["funkc", "def ", "return", "argument", "parametr", "docstring"],
     "wyjasnienie":
         "Funkcja to nazwana czynność, którą definiujesz raz i wywołujesz wiele razy. Jak przepis „oblicz dawkę paszy”: "
         "podajesz wagę (argument), dostajesz kilogramy (return). def otwiera definicję, return oddaje wynik. "
         "Funkcja bez return zwraca None. Zmienne tworzone w środku funkcji żyją tylko w niej. "
         "Docstring — opis w potrójnych cudzysłowach tuż pod def — mówi, co funkcja robi; czyta go help() i PyCharm. "
         "Dobra funkcja robi jedną rzecz i ma nazwę-czasownik: policz_dawke, czy_parzysta.",
     "przyklad":
         "def dawka_paszy(waga_kg, procent=2.5):\n"
         "    \"\"\"Zwraca dzienną dawkę paszy w kg jako procent masy ciała.\"\"\"\n"
         "    return waga_kg * procent / 100\n\n"
         "print(dawka_paszy(600))        # 15.0\n"
         "print(dawka_paszy(600, 3))     # 18.0",
     "zadania": ["5 funkcji z docstringami: pole prostokąta, czy parzysta, maksimum z listy (bez max()), odwróć napis, silnia.",
                 "Przepisz kalkulator BMI tak, by liczenie i kategoria były osobnymi funkcjami.",
                 "Menedżer zadań: menu w pętli, każda operacja (dodaj/usuń/wypisz) osobną funkcją."],
     "pytania": [("Co zwraca funkcja bez return?", "None."),
                 ("Czym różni się parametr od argumentu?", "Parametr to nazwa w def; argument to wartość przekazana przy wywołaniu."),
                 ("Gdzie pisze się docstring?", "W pierwszej linii ciała funkcji, w \"\"\" \"\"\".")],
     "pulapki": ["print w funkcji to nie return — wynik nie wraca do wywołującego.", "Zmienna z wnętrza funkcji nie istnieje na zewnątrz."]},

    {"id": "slowniki", "tydzien": 3, "nazwa": "Słowniki i krotki",
     "slowa": ["słownik", "slownik", "dict", "klucz", "krotk", "tuple", "items()"],
     "wyjasnienie":
         "Słownik to pary klucz → wartość: wagi = {\"Krasula\": 612, \"Mućka\": 580}. Jak kartoteka zwierząt: po imieniu (klucz) "
         "od razu znajdujesz wagę (wartość), bez przeszukiwania listy. Dodajesz/zmieniasz wagi[\"Łaciata\"] = 640, "
         "usuwasz del wagi[\"Mućka\"], sprawdzasz if \"Mućka\" in wagi, przechodzisz for imie, waga in wagi.items(). "
         "wagi.get(\"Nowa\", 0) zwraca domyślną wartość zamiast błędu KeyError.\n"
         "Krotka (tuple) to lista, której nie można zmienić: wspolrzedne = (52.1, 21.0). Używasz, gdy dane mają zostać stałe "
         "lub gdy funkcja zwraca kilka wartości naraz: return srednia, maksimum.",
     "przyklad":
         "wagi = {\"Krasula\": 612, \"Mućka\": 580}\n"
         "wagi[\"Łaciata\"] = 640\n"
         "for imie, waga in sorted(wagi.items(), key=lambda p: p[1]):\n"
         "    print(imie, waga)\n"
         "print(wagi.get(\"Nowa\", \"brak w kartotece\"))",
     "zadania": ["Słownik zwierzę → waga: dodaj, zmień, usuń, wypisz posortowane po wadze.",
                 "Policz, ile razy każde słowo występuje w zdaniu (słownik licznikowy).",
                 "Menedżer zadań jako lista słowników {\"tytul\":..., \"zrobione\": False}; oznaczanie zadania jako zrobione."],
     "pytania": [("Co zwróci d[\"krowa\"] dla d = {\"krowa\": 600}?", "600."),
                 ("Co się stanie przy d[\"byk\"], gdy klucza nie ma?", "KeyError — użyj d.get(\"byk\")."),
                 ("Czym różni się krotka od listy?", "Krotki nie można zmienić po utworzeniu.")],
     "pulapki": ["Klucze muszą być niezmienne (napisy, liczby, krotki) — lista nie może być kluczem."]},

    {"id": "bledy", "tydzien": 3, "nazwa": "Obsługa błędów try / except",
     "slowa": ["try", "except", "wyjąt", "wyjat", "błąd", "blad", "obsług"],
     "wyjasnienie":
         "try/except to siatka zabezpieczająca: próbujesz wykonać coś ryzykownego (int(input())), a gdy pójdzie źle, "
         "łapiesz błąd i reagujesz zamiast wywalać program. Jak przy zakupie zwierzęcia: próbujesz je załadować, "
         "a gdy nie wejdzie na przyczepę — masz plan B, nie odwołujesz całego dnia.\n"
         "Łap konkretny typ: except ValueError — zły format liczby; except ZeroDivisionError — dzielenie przez zero. "
         "Gołe except: łapie wszystko, także literówki w Twoim kodzie, i ukrywa prawdziwy problem — unikaj. "
         "else wykonuje się, gdy błędu nie było; finally — zawsze (np. zamknięcie pliku).",
     "przyklad":
         "while True:\n"
         "    try:\n"
         "        waga = float(input(\"Waga: \"))\n"
         "        break\n"
         "    except ValueError:\n"
         "        print(\"To nie liczba, spróbuj jeszcze raz.\")\n"
         "print(\"Zapisano\", waga)",
     "zadania": ["Pytaj o liczbę w pętli; zły wpis nie przerywa programu (ValueError).",
                 "Kalkulator: obsłuż dzielenie przez zero wyjątkiem zamiast if-em i porównaj oba podejścia.",
                 "Wczytaj plik, którego może nie być — FileNotFoundError z czytelnym komunikatem."],
     "pytania": [("Kiedy wykona się except?", "Gdy w bloku try wystąpi błąd pasującego typu."),
                 ("Dlaczego gołe except: jest złe?", "Łapie wszystko, także błędy w Twoim kodzie, i je ukrywa."),
                 ("Jaki wyjątek rzuca int(\"abc\")?", "ValueError.")],
     "pulapki": ["try nie naprawia błędu — tylko pozwala zareagować.", "Za szeroki try utrudnia znalezienie, która linia zawiodła."]},

    {"id": "moduly_std", "tydzien": 3, "nazwa": "Moduły random i datetime",
     "slowa": ["random", "datetime", "losow", "data", "timedelta", "import"],
     "wyjasnienie":
         "import wnosi do programu gotowe narzędzia. random losuje: random.randint(1, 100) (liczba z zakresu, oba końce włącznie), "
         "random.choice(lista) (jeden element), random.sample(lista, 3) (trzy różne), random.shuffle(lista) (miesza). "
         "datetime liczy czas: datetime.date.today() to dziś, datetime.timedelta(days=7) to „tydzień”, więc "
         "today() + timedelta(days=7) daje datę kontroli za tydzień. Formatowanie: data.strftime(\"%d.%m.%Y\"). "
         "Przykład: losujesz 3 zwierzęta do kontroli weterynaryjnej i wyznaczasz termin za 7 dni.",
     "przyklad":
         "import random\n"
         "import datetime\n\n"
         "stado = [\"Krasula\", \"Mućka\", \"Łaciata\", \"Bystra\"]\n"
         "do_kontroli = random.sample(stado, 3)\n"
         "termin = datetime.date.today() + datetime.timedelta(days=7)\n"
         "print(do_kontroli, termin.strftime(\"%d.%m.%Y\"))",
     "zadania": ["Wylosuj 3 zwierzęta z listy do kontroli i wypisz datę kontroli za 7 dni.",
                 "Rzut dwiema kostkami 1000 razy — policz, ile razy wypadła suma 7.",
                 "Program liczy, ile dni zostało do podanej daty (input w formacie RRRR-MM-DD, datetime.date.fromisoformat)."],
     "pytania": [("Czym różni się random.choice od random.sample?", "choice zwraca jeden element; sample listę n różnych."),
                 ("Jak dodać 7 dni do daty?", "data + datetime.timedelta(days=7)"),
                 ("Czy randint(1, 6) może zwrócić 6?", "Tak — oba końce włącznie.")],
     "pulapki": ["random.random() zwraca float 0–1, nie liczbę całkowitą.", "import datetime vs from datetime import date — różne sposoby odwołania."]},

    {"id": "pliki", "tydzien": 4, "nazwa": "Pliki: open, read, write, with",
     "slowa": ["plik", "open(", "with open", "zapis", "odczyt", "write", "read"],
     "wyjasnienie":
         "Program zapomina wszystko po zamknięciu — plik to zeszyt, do którego zapisujesz na trwałe. open(\"stado.txt\", \"w\") "
         "otwiera do zapisu (w nadpisuje!, a dopisuje), \"r\" do odczytu. with open(...) as f: zamyka plik automatycznie, "
         "nawet gdy w środku wystąpi błąd — zawsze używaj with. f.write() zapisuje napis (sam dodaj \\n), f.read() czyta całość, "
         "for linia in f: czyta po linii. encoding=\"utf-8\" chroni polskie znaki.",
     "przyklad":
         "stado = [\"Krasula\", \"Mućka\"]\n"
         "with open(\"stado.txt\", \"w\", encoding=\"utf-8\") as f:\n"
         "    for krowa in stado:\n"
         "        f.write(krowa + \"\\n\")\n\n"
         "with open(\"stado.txt\", encoding=\"utf-8\") as f:\n"
         "    for linia in f:\n"
         "        print(linia.strip())",
     "zadania": ["Zapisz listę zwierząt do stado.txt, odczytaj i wypisz — najpierw bez with, potem z with; porównaj.",
                 "Dziennik: każde uruchomienie dopisuje (tryb a) linię z datą i wpisanym zdarzeniem.",
                 "Policz linie i słowa w dowolnym pliku tekstowym; obsłuż brak pliku."],
     "pytania": [("Co robi tryb \"w\"?", "Otwiera do zapisu i KASUJE poprzednią zawartość."),
                 ("Po co with?", "Zamyka plik automatycznie, także przy błędzie."),
                 ("Jak dopisać, nie nadpisując?", "Tryb \"a\".")],
     "pulapki": ["Brak \\n w write() skleja wszystko w jedną linię.", "Ścieżka względna liczy się od katalogu, z którego uruchamiasz program."]},

    {"id": "csv", "tydzien": 4, "nazwa": "Moduł csv",
     "slowa": ["csv", "reader", "writer", "dictreader", "średnia wag"],
     "wyjasnienie":
         "CSV to tabela w pliku tekstowym: wartości oddzielone przecinkami, jedna linia = jeden wiersz. Tak eksportuje arkusz "
         "i tak wygląda rejestr stada: nr,imie,rasa,waga. Moduł csv czyta i pisze bezpiecznie (radzi sobie z przecinkami w danych). "
         "csv.reader daje każdy wiersz jako listę napisów, csv.DictReader jako słownik z nagłówkami jako kluczami — "
         "czytelniej: wiersz[\"waga\"]. Liczby wracają jako napisy, więc float(wiersz[\"waga\"]). "
         "Przy zapisie: newline=\"\" w open, inaczej na Windows pojawią się puste linie.",
     "przyklad":
         "import csv\n\n"
         "with open(\"stado.csv\", encoding=\"utf-8\", newline=\"\") as f:\n"
         "    wiersze = list(csv.DictReader(f))\n"
         "wagi = [float(w[\"waga\"]) for w in wiersze]\n"
         "print(\"Średnia waga:\", sum(wagi) / len(wagi))\n\n"
         "with open(\"stado.csv\", \"a\", encoding=\"utf-8\", newline=\"\") as f:\n"
         "    csv.writer(f).writerow([5, \"Bystra\", \"HF\", 598])",
     "zadania": ["Wczytaj stado.csv (nr, imię, rasa, waga) i policz średnią wagę.",
                 "Dziennik stada: dodawanie zwierzęcia do CSV, statystyki (liczba, średnia, najcięższe), wyszukiwanie po rasie.",
                 "Wczytaj CSV i zapisz nowy plik tylko ze zwierzętami powyżej 600 kg."],
     "pytania": [("Co daje csv.reader przy iteracji?", "Listę napisów dla każdego wiersza."),
                 ("Czym różni się DictReader?", "Zwraca słowniki z nagłówkami jako kluczami."),
                 ("Jakiego typu jest w[\"waga\"] z DictReadera?", "str — trzeba float().")],
     "pulapki": ["Pierwsza linia to nagłówek — reader ją też zwraca; DictReader ją zjada.", "Brak newline=\"\" na Windows = puste linie."]},

    {"id": "git", "tydzien": 4, "nazwa": "Git: gałęzie, diff, log, cofanie, pull request",
     "slowa": ["git", "gałą", "gala", "branch", "commit", "diff", "stash", "checkout", "pull request", "merge", "push"],
     "wyjasnienie":
         "Git to dziennik zmian z możliwością cofania. Commit = zdjęcie całego projektu w danej chwili z podpisem. "
         "git status mówi, co zmieniłeś; git diff pokazuje różnice; git log --oneline to historia. "
         "Gałąź (branch) to równoległa linia pracy: git checkout -b feature/csv tworzy ją i przełącza — pracujesz bez psucia main, "
         "a gdy skończysz, scalasz (merge) przez pull request na GitHubie, gdzie można zmiany obejrzeć i skomentować. "
         "Cofanie: git checkout -- plik odrzuca niezacommitowane zmiany w pliku; git stash odkłada zmiany na bok (stash pop przywraca); "
         "git revert tworzy commit odwracający inny commit. Jak w gospodarstwie: gałąź to próba nowej paszy u 3 krów, zanim dasz całemu stadu.",
     "przyklad":
         "git checkout -b feature/csv      # nowa gałąź\n"
         "# ...zmiany w plikach...\n"
         "git status\n"
         "git diff\n"
         "git add .\n"
         "git commit -m \"dzień 18: odczyt CSV\"\n"
         "git push -u origin feature/csv    # potem Pull Request na GitHubie\n"
         "git checkout main && git pull     # po scaleniu",
     "zadania": ["Gałąź feature/csv: zmiany, git diff, git log, scal przez pull request na GitHubie.",
                 "Celowo zepsuj plik; odzyskaj go raz przez git checkout -- plik, drugi raz przez git stash; opisz różnicę.",
                 "Zrób dwa commity, obejrzyj git log, cofnij ostatni przez git revert HEAD."],
     "pytania": [("Co robi git checkout -b nazwa?", "Tworzy gałąź i przełącza na nią."),
                 ("Czym różni się commit od push?", "Commit zapisuje lokalnie; push wysyła na GitHub."),
                 ("Co pokazuje git diff?", "Zmiany w plikach, których jeszcze nie dodałeś do commita.")],
     "pulapki": ["git add . przed commitem — inaczej commit jest pusty.", "git checkout -- plik kasuje zmiany bezpowrotnie."]},

    {"id": "klasy", "tydzien": 5, "nazwa": "Klasy i obiekty",
     "slowa": ["klas", "class", "obiekt", "__init__", "self", "metod", "atrybut"],
     "wyjasnienie":
         "Klasa to szablon, obiekt to konkretny egzemplarz. Klasa Zwierze opisuje, co każde zwierzę ma (atrybuty: imie, waga) "
         "i co umie (metody: opis(), dodaj_wage()). Krasula i Mućka to dwa obiekty tej klasy — ten sam szablon, inne dane. "
         "__init__ wywołuje się przy tworzeniu obiektu i ustawia atrybuty; self to „ten konkretny obiekt” — "
         "self.waga to waga tej krowy, nie wszystkich. Klasy porządkują kod, gdy dane i czynności na nich chodzą razem.",
     "przyklad":
         "class Zwierze:\n"
         "    def __init__(self, imie, waga):\n"
         "        self.imie = imie\n"
         "        self.waga = waga\n\n"
         "    def opis(self):\n"
         "        return f\"{self.imie}: {self.waga} kg\"\n\n"
         "    def przybierz(self, kg):\n"
         "        self.waga += kg\n\n"
         "krasula = Zwierze(\"Krasula\", 612)\n"
         "krasula.przybierz(8)\n"
         "print(krasula.opis())",
     "zadania": ["Klasa Zwierze z atrybutami i metodą opis(); utwórz 3 obiekty i wypisz opisy.",
                 "Dodaj metodę dodaj_zdarzenie(opis) zapisującą do listy w obiekcie i historia() wypisującą ją.",
                 "Klasa Stado przechowująca listę obiektów Zwierze z metodami dodaj(), srednia_waga(), najciezsze()."],
     "pytania": [("Czym jest __init__?", "Konstruktorem — wywołuje się przy tworzeniu obiektu."),
                 ("Co oznacza self?", "Obiekt, na którym wywołano metodę."),
                 ("Jak utworzyć obiekt klasy Zwierze?", "Zwierze(\"Krasula\", 612)")],
     "pulapki": ["Zapomniany self w def — TypeError o liczbie argumentów.", "Atrybut bez self. to zwykła zmienna lokalna, która znika."]},

    {"id": "moduly", "tydzien": 5, "nazwa": "Podział kodu na moduły",
     "slowa": ["moduł", "modul", "import", "main.py", "podziel", "__name__"],
     "wyjasnienie":
         "Gdy plik rośnie ponad 100 linii, dzielisz go: main.py (uruchomienie, menu), zadania.py (logika), plik.py (zapis/odczyt). "
         "Każdy plik .py to moduł; from zadania import dodaj_zadanie wnosi funkcję. "
         "Jak w gospodarstwie: osobny budynek na maszyny, osobny na paszę — każdy ma jedną rolę. "
         "if __name__ == \"__main__\": chroni kod startowy przed uruchomieniem przy imporcie — "
         "moduł zaimportowany wykonuje tylko definicje, nie menu.",
     "przyklad":
         "# zadania.py\n"
         "def dodaj(lista, tytul):\n"
         "    lista.append({\"tytul\": tytul, \"zrobione\": False})\n\n"
         "# main.py\n"
         "from zadania import dodaj\n\n"
         "def main():\n"
         "    zadania = []\n"
         "    dodaj(zadania, \"nakarmić cielęta\")\n"
         "    print(zadania)\n\n"
         "if __name__ == \"__main__\":\n"
         "    main()",
     "zadania": ["Podziel menedżer zadań na main.py, zadania.py, plik.py.",
                 "Przenieś funkcje z tygodnia 3 do modułu narzedzia.py i użyj ich z dwóch różnych skryptów.",
                 "Dodaj if __name__ == \"__main__\": do każdego pliku i sprawdź, co się dzieje przy imporcie."],
     "pytania": [("Po co if __name__ == \"__main__\":?", "Żeby kod startowy nie wykonywał się przy imporcie modułu."),
                 ("Jak zaimportować funkcję dodaj z zadania.py?", "from zadania import dodaj"),
                 ("Co to jest moduł?", "Każdy plik .py, który można zaimportować.")],
     "pulapki": ["Importy kołowe (A importuje B, B importuje A) — ImportError.", "Nazwa pliku jak nazwa biblioteki (random.py) przykrywa bibliotekę."]},

    {"id": "venv", "tydzien": 5, "nazwa": "venv, pip, requirements.txt, .gitignore",
     "slowa": ["venv", "pip", "requirements", "gitignore", "środowisko", "srodowisko", "bibliotek"],
     "wyjasnienie":
         "venv to osobna szafka z narzędziami dla jednego projektu — biblioteki nie mieszają się między projektami. Znasz to już z Mentora: zakładka Środowisko "
         "utworzyła takie środowisko dla kursu (srodowiska/python-junior-qa/.venv) i zainstalowała w nim pytest, requests, selenium i flask — teraz robisz to samo ręcznie dla swojego projektu. "
         "Tworzysz: python -m venv .venv; aktywujesz (Windows: .venv\\Scripts\\activate; Linux/Mac: source .venv/bin/activate); "
         "instalujesz: pip install requests. pip freeze > requirements.txt zapisuje listę bibliotek, "
         "a pip install -r requirements.txt odtwarza ją na innym komputerze (i w CI). "
         ".venv to setki plików — do .gitignore, nie do repozytorium.",
     "przyklad":
         "python -m venv .venv\n"
         ".venv\\Scripts\\activate          # Windows\n"
         "pip install requests\n"
         "pip freeze > requirements.txt\n"
         "echo .venv/ >> .gitignore",
     "zadania": ["Utwórz venv, zainstaluj requests, zapisz requirements.txt, dodaj .venv do .gitignore.",
                 "Usuń venv i odtwórz środowisko z requirements.txt jedną komendą.",
                 "Sprawdź, co pokazuje pip list w venv i poza nim — zapisz różnicę w notatkach."],
     "pytania": [("Po co venv?", "Izoluje biblioteki projektu od reszty systemu."),
                 ("Co zawiera requirements.txt?", "Listę bibliotek z wersjami."),
                 ("Dlaczego .venv w .gitignore?", "To cudze biblioteki — każdy odtworzy je z requirements.txt.")],
     "pulapki": ["PyCharm ma własne venv w ustawieniach interpretera — sprawdź, czy terminal używa tego samego.",
                 "Po pip install zawsze zaktualizuj requirements.txt."]},

    {"id": "requests", "tydzien": 5, "nazwa": "Biblioteka requests i API",
     "slowa": ["request", "api", "json", "pogod", "open-meteo", "http", "get("],
     "wyjasnienie":
         "API to okienko, przez które jeden program pyta drugi o dane. requests.get(url) wysyła pytanie, odpowiedź ma "
         "status (200 = OK, 404 = nie ma) i treść — często JSON, czyli tekst w formacie słowników i list. "
         ".json() zamienia go na struktury Pythona: dane[\"daily\"][\"temperature_2m_min\"][0]. "
         "Przykład: open-meteo.com zwraca prognozę dla współrzędnych Radzynia; wyciągasz temperaturę minimalną "
         "i ostrzegasz o przymrozku. Zawsze sprawdź status i obsłuż brak internetu (requests.exceptions.RequestException).",
     "przyklad":
         "import requests\n\n"
         "url = \"https://api.open-meteo.com/v1/forecast\"\n"
         "param = {\"latitude\": 51.78, \"longitude\": 22.62, \"daily\": \"temperature_2m_min\", \"timezone\": \"Europe/Warsaw\"}\n"
         "odp = requests.get(url, params=param, timeout=10)\n"
         "odp.raise_for_status()\n"
         "dane = odp.json()\n"
         "for dzien, tmin in zip(dane[\"daily\"][\"time\"], dane[\"daily\"][\"temperature_2m_min\"]):\n"
         "    print(dzien, tmin, \"PRZYMROZEK!\" if tmin < 0 else \"\")",
     "zadania": ["Pobierz dane z publicznego API i wypisz 3 pola z odpowiedzi JSON.",
                 "Pogoda dla Radzynia: prognoza na 3 dni zapisana do CSV z datą, ostrzeżenie o przymrozku.",
                 "Obsłuż brak internetu i błędny status — program ma wypisać komunikat, nie traceback."],
     "pytania": [("Co zwraca odp.json()?", "Dane JSON zamienione na słowniki/listy Pythona."),
                 ("Co oznacza status 200?", "Sukces."),
                 ("Po co timeout w get()?", "Żeby program nie wisiał w nieskończoność bez odpowiedzi.")],
     "pulapki": ["Klucze JSON są napisami — dane[\"daily\"], nie dane.daily.", "Bez venv i pip install requests — ModuleNotFoundError."]},

    {"id": "debug", "tydzien": 6, "nazwa": "Debugowanie: print i debugger PyCharm",
     "slowa": ["debug", "breakpoint", "błąd ukryt", "szukaj błęd", "krok po kroku"],
     "wyjasnienie":
         "Debugowanie to tropienie: wiesz, że wynik jest zły, szukasz, gdzie dane skręciły. Najprostsze narzędzie: print(zmienna) "
         "przed i po podejrzanej linii. Debugger PyCharm robi to lepiej: klikasz obok numeru linii (czerwona kropka = breakpoint), "
         "uruchamiasz przez ikonę robaka, program zatrzymuje się i widzisz wartości wszystkich zmiennych; "
         "Step Over (F8) wykonuje linię, Step Into (F7) wchodzi do funkcji. Jak szukanie przecieku w rurociągu: "
         "zakręcasz zawory po kolei, aż znajdziesz odcinek, gdzie ubywa.",
     "przyklad":
         "def srednia(wagi):\n"
         "    suma = 0\n"
         "    for w in wagi:\n"
         "        suma = w          # <- breakpoint tutaj: suma nie rośnie! powinno być suma += w\n"
         "    return suma / len(wagi)",
     "zadania": ["Poproś Asystenta: „daj mi program z 3 ukrytymi błędami” i znajdź je debuggerem.",
                 "Postaw breakpoint w pętli i obejrzyj, jak zmienia się zmienna w każdym obrocie.",
                 "Znajdź błąd w cudzym kodzie z GitHuba, używając wyłącznie printów — opisz w notatki.md, jak szukałeś."],
     "pytania": [("Co robi breakpoint?", "Zatrzymuje program w tej linii, żebyś obejrzał zmienne."),
                 ("Czym różni się Step Over od Step Into?", "Over wykonuje linię w całości; Into wchodzi do wywołanej funkcji."),
                 ("Od którego końca czytać traceback?", "Od dołu — ostatnia linia mówi CO, wyżej GDZIE.")],
     "pulapki": ["Printy do debugowania usuń przed commitem.", "Błąd logiczny (zły wynik) nie daje tracebacku — tylko testy go wykryją."]},

    {"id": "readme", "tydzien": 6, "nazwa": "README, docstringi, refaktoryzacja",
     "slowa": ["readme", "dokument", "refaktor", "czytel", "porządek", "porzadek", "rekruter"],
     "wyjasnienie":
         "README to pierwsza rzecz, którą widzi rekruter: co program robi, jak go uruchomić, co pokazuje (zrzut ekranu). "
         "Trzy akapity wystarczą. Docstring robi to samo dla funkcji. Refaktoryzacja to porządkowanie kodu bez zmiany działania: "
         "wyciąganie powtórzeń do funkcji, lepsze nazwy, krótsze funkcje (jedna rzecz na funkcję). "
         "Jak sprzątanie warsztatu: narzędzia te same, ale każde ma miejsce. Zasada: najpierw testy lub ręczne sprawdzenie, "
         "potem refaktor, potem sprawdzenie ponownie — zachowanie ma zostać identyczne.",
     "przyklad":
         "# README.md\n"
         "# Kalkulator BMI\n"
         "Pyta o wzrost i wagę, wypisuje BMI i kategorię.\n\n"
         "## Uruchomienie\n"
         "python bmi.py\n\n"
         "## Przykład\n"
         "Wzrost (m): 1.80 / Waga (kg): 75 -> BMI 23.1, norma",
     "zadania": ["Napisz README dla każdego z 6 projektów: co robi, jak uruchomić, zrzut z konsoli.",
                 "Zrefaktoryzuj BMI i zgadywankę: funkcje z docstringami, bez powtórzeń.",
                 "Jedno repo python-projekty z folderem na projekt i głównym README z linkami."],
     "pytania": [("Co minimalnie ma README?", "Co robi i jak uruchomić."),
                 ("Czym jest refaktoryzacja?", "Zmianą struktury kodu bez zmiany zachowania."),
                 ("Po co docstring, skoro jest komentarz?", "Docstring czyta help() i edytor; opisuje CO robi funkcja, komentarz — DLACZEGO coś zrobiono.")],
     "pulapki": ["README bez instrukcji uruchomienia = rekruter zamyka kartę.", "Refaktor i nowa funkcja w jednym commicie utrudniają cofnięcie."]},

    {"id": "pytest", "tydzien": 7, "nazwa": "pytest: assert, nazewnictwo, uruchamianie",
     "slowa": ["pytest", "test_", "assert", "test jednostk", "piramid"],
     "wyjasnienie":
         "Test to program sprawdzający inny program. Zamiast ręcznie wpisywać dane i patrzeć, piszesz: assert dawka_paszy(600) == 15.0 — "
         "pytest uruchamia to za Ciebie w sekundę, za każdym razem. Jak próbnik mleka: nie smakujesz każdej bańki, aparat mierzy. "
         "pytest szuka plików test_*.py i funkcji def test_...(); assert warunek — fałsz = test czerwony z czytelnym opisem. "
         "Uruchamiasz pytest -v. Piramida testów: dużo szybkich testów jednostkowych (funkcje), mniej integracyjnych (moduły razem), "
         "najmniej end-to-end (przeglądarka). Dobry test: jedna rzecz, jasna nazwa (test_dawka_dla_600kg), przypadki brzegowe "
         "(pusta lista, zero, zły typ).",
     "przyklad":
         "# test_pasza.py\n"
         "from pasza import dawka_paszy\n\n"
         "def test_dawka_dla_600kg():\n"
         "    assert dawka_paszy(600) == 15.0\n\n"
         "def test_dawka_dla_zera():\n"
         "    assert dawka_paszy(0) == 0\n\n"
         "def test_ujemna_waga_rzuca_blad():\n"
         "    import pytest\n"
         "    with pytest.raises(ValueError):\n"
         "        dawka_paszy(-10)",
     "zadania": ["pip install pytest; test_funkcje.py z 5 testami do funkcji z tygodnia 3; pytest -v.",
                 "15+ testów do menedżera zadań i dziennika stada: pusta lista, zły typ, duplikat.",
                 "Poproś Asystenta o ukryty błąd w pliku i znajdź go testem, który nie przechodzi."],
     "pytania": [("W jakich plikach pytest szuka testów?", "test_*.py lub *_test.py."),
                 ("Co się stanie przy assert 2 + 2 == 5?", "Test nie przejdzie — AssertionError."),
                 ("Co to przypadek brzegowy?", "Skrajne dane: pusta lista, zero, maksimum, zły typ.")],
     "pulapki": ["Test, który nigdy nie był czerwony, może nic nie sprawdzać — zepsuj kod i zobacz, czy test to wykryje.",
                 "Testy nie mogą zależeć od kolejności ani od input()."]},

    {"id": "parametrize_fixture", "tydzien": 7, "nazwa": "parametrize i fixtures",
     "slowa": ["parametrize", "fixture", "conftest", "tmp_path"],
     "wyjasnienie":
         "@pytest.mark.parametrize uruchamia jeden test dla wielu zestawów danych — zamiast 6 kopii testu BMI masz jedną funkcję "
         "i tabelę (wzrost, waga, kategoria). Fixture to przygotowanie sceny: funkcja z @pytest.fixture tworzy np. menedżer "
         "z 3 zadaniami, a każdy test dostaje świeży egzemplarz jako argument. Wbudowana fixture tmp_path daje tymczasowy katalog — "
         "testy zapisu do pliku nie dotykają prawdziwych danych. Fixtures wspólne dla wielu plików trzymasz w conftest.py.",
     "przyklad":
         "import pytest\n"
         "from bmi import kategoria\n\n"
         "@pytest.mark.parametrize(\"wzrost, waga, oczekiwana\", [\n"
         "    (1.80, 50, \"niedowaga\"),\n"
         "    (1.80, 75, \"norma\"),\n"
         "    (1.80, 95, \"nadwaga\"),\n"
         "])\n"
         "def test_kategoria(wzrost, waga, oczekiwana):\n"
         "    assert kategoria(wzrost, waga) == oczekiwana\n\n"
         "@pytest.fixture\n"
         "def menedzer():\n"
         "    m = []\n"
         "    for t in (\"a\", \"b\", \"c\"):\n"
         "        dodaj(m, t)\n"
         "    return m\n\n"
         "def test_usun(menedzer):\n"
         "    usun(menedzer, \"a\")\n"
         "    assert len(menedzer) == 2",
     "zadania": ["Jeden test z parametrize sprawdzający 6 przypadków BMI.",
                 "Fixture tworząca menedżer zadań z 3 zadaniami, użyta w 4 testach.",
                 "Testy dziennika stada zapisujące do tmp_path, nie do prawdziwego CSV."],
     "pytania": [("Po co parametrize?", "Jeden test dla wielu zestawów danych."),
                 ("Czym jest fixture?", "Funkcją przygotowującą dane/obiekty dla testów."),
                 ("Co daje tmp_path?", "Tymczasowy katalog kasowany po teście.")],
     "pulapki": ["Nazwa argumentu testu musi być taka sama jak nazwa fixture.", "Fixture, która zmienia globalny stan, psuje inne testy."]},

    {"id": "selenium", "tydzien": 8, "nazwa": "Selenium WebDriver i lokatory",
     "slowa": ["selenium", "webdriver", "lokator", "xpath", "css_selector", "find_element", "by."],
     "wyjasnienie":
         "Selenium steruje prawdziwą przeglądarką z kodu: otwiera stronę, klika, wpisuje, czyta tekst — tak jak użytkownik. "
         "driver = webdriver.Chrome(); driver.get(url); element = driver.find_element(By.ID, \"login\"); element.send_keys(\"jan\"); "
         "element.click(). Lokator to adres elementu: By.ID (najstabilniejszy), By.CSS_SELECTOR (\"#id\", \".klasa\", \"input[name=user]\"), "
         "By.XPATH (\"//button[text()='Zaloguj']\") — najpotężniejszy, ale kruchy, gdy opiera się na pełnej ścieżce. "
         "Lokatory podglądasz w przeglądarce: F12 → Elements. Ćwicz na saucedemo.com i the-internet.herokuapp.com.",
     "przyklad":
         "from selenium import webdriver\n"
         "from selenium.webdriver.common.by import By\n\n"
         "driver = webdriver.Chrome()\n"
         "driver.get(\"https://www.saucedemo.com\")\n"
         "driver.find_element(By.ID, \"user-name\").send_keys(\"standard_user\")\n"
         "driver.find_element(By.ID, \"password\").send_keys(\"secret_sauce\")\n"
         "driver.find_element(By.CSS_SELECTOR, \"#login-button\").click()\n"
         "driver.save_screenshot(\"po_logowaniu.png\")\n"
         "driver.quit()",
     "zadania": ["pip install selenium; skrypt otwiera saucedemo.com, loguje się, robi zrzut ekranu.",
                 "Znajdź 5 elementów na the-internet.herokuapp.com trzema sposobami: id, CSS, XPath.",
                 "Formularz: wypełnij, wyślij, sprawdź komunikat — z WebDriverWait, bez time.sleep."],
     "pytania": [("Który lokator jest najstabilniejszy?", "id."),
                 ("Co znaczy # w selektorze CSS?", "id; kropka to klasa."),
                 ("Po co driver.quit()?", "Zamyka przeglądarkę i zwalnia zasoby.")],
     "pulapki": ["Selenium 4 pobiera sterownik sam — stary poradnik z chromedriver.exe może mylić.",
                 "XPath po pełnej ścieżce psuje się przy każdej zmianie układu strony."]},

    {"id": "wait_pom", "tydzien": 8, "nazwa": "WebDriverWait i Page Object Model",
     "slowa": ["wait", "webdriverwait", "expected_conditions", "page object", "pom", "loginpage", "sleep"],
     "wyjasnienie":
         "Strona ładuje się chwilę; time.sleep(5) zawsze czeka 5 s — za długo albo za krótko. WebDriverWait czeka tylko tyle, "
         "ile trzeba, aż warunek się spełni (element widoczny, klikalny), maksymalnie N sekund. "
         "Page Object Model: każda strona to klasa z lokatorami i akcjami (LoginPage.login(user, haslo)); testy wywołują metody, "
         "nie szukają elementów same. Gdy zmieni się id przycisku, poprawiasz jedno miejsce, nie 15 testów. "
         "Jak w gospodarstwie: instrukcja „uruchom dojarkę” to jedna karta, a nie powtarzana w każdym planie dnia.",
     "przyklad":
         "from selenium.webdriver.support.ui import WebDriverWait\n"
         "from selenium.webdriver.support import expected_conditions as EC\n"
         "from selenium.webdriver.common.by import By\n\n"
         "class LoginPage:\n"
         "    URL = \"https://www.saucedemo.com\"\n"
         "    USER = (By.ID, \"user-name\")\n"
         "    HASLO = (By.ID, \"password\")\n"
         "    PRZYCISK = (By.ID, \"login-button\")\n"
         "    BLAD = (By.CSS_SELECTOR, \"[data-test='error']\")\n\n"
         "    def __init__(self, driver):\n"
         "        self.driver = driver\n"
         "        self.wait = WebDriverWait(driver, 10)\n\n"
         "    def open(self):\n"
         "        self.driver.get(self.URL)\n\n"
         "    def login(self, user, haslo):\n"
         "        self.driver.find_element(*self.USER).send_keys(user)\n"
         "        self.driver.find_element(*self.HASLO).send_keys(haslo)\n"
         "        self.driver.find_element(*self.PRZYCISK).click()\n\n"
         "    def error_text(self):\n"
         "        return self.wait.until(EC.visibility_of_element_located(self.BLAD)).text",
     "zadania": ["Klasa LoginPage z metodami open(), login(), error_text().",
                 "5 testów end-to-end: logowanie, błędne hasło, przelew, saldo, wylogowanie — każdy w POM.",
                 "Zamień każde time.sleep w swoich skryptach na WebDriverWait z odpowiednim expected_conditions."],
     "pytania": [("Dlaczego Wait zamiast sleep?", "Czeka tylko tyle, ile trzeba, do spełnienia warunku."),
                 ("Na czym polega POM?", "Klasa na stronę: lokatory i akcje w jednym miejscu, testy używają metod."),
                 ("Co zrobić, gdy zmieni się id elementu w POM?", "Poprawić jeden lokator w klasie strony.")],
     "pulapki": ["Lokator jako krotka (By.ID, \"x\") rozpakowujesz gwiazdką: find_element(*self.USER).",
                 "Wait rzuca TimeoutException — to też informacja: element nie pojawił się."]},

    {"id": "bug_raport", "tydzien": 9, "nazwa": "Przypadki testowe i bug raporty",
     "slowa": ["bug", "raport", "przypadek testow", "test case", "kroki", "oczekiwan"],
     "wyjasnienie":
         "Przypadek testowy to przepis, który inny tester wykona bez Ciebie: ID, warunki wstępne (zalogowany, saldo 100), kroki "
         "(1. kliknij Przelew, 2. wpisz 50…), oczekiwany wynik (saldo 50, komunikat „Wysłano”). "
         "Bug raport to zgłoszenie usterki: tytuł (co nie działa, konkretnie), kroki odtworzenia, oczekiwany vs rzeczywisty wynik, "
         "środowisko (system, przeglądarka, wersja), załącznik (zrzut). Test dobrego raportu: programista odtwarza błąd bez zadawania pytań. "
         "Jak zgłoszenie do serwisu maszyny: „nie działa” to za mało; „przy 2000 obr./min po 10 minutach gaśnie, w lipcu, na benzynie 95” — to raport.",
     "przyklad":
         "# BUG-003: Przelew o kwocie 0 zł przechodzi bez komunikatu\n"
         "Środowisko: Windows 11, Chrome 129, MeridianBank v1.2\n"
         "Kroki: 1. Zaloguj jako test_user. 2. Przelew -> kwota 0 -> Wyślij.\n"
         "Oczekiwany: komunikat „Kwota musi być większa od 0”, przelew odrzucony.\n"
         "Rzeczywisty: przelew zapisany w historii z kwotą 0,00 zł.\n"
         "Priorytet: średni. Załącznik: przelew_zero.png",
     "zadania": ["10 przypadków testowych dla MeridianBank w tabeli (ID, warunki wstępne, kroki, oczekiwany wynik).",
                 "3 bug raporty z własnych znalezisk; poproś Asystenta o ocenę, czy programista zrozumie bez pytań.",
                 "Przerób jeden bug raport w test Selenium, który go wykrywa."],
     "pytania": [("Co musi zawierać bug raport?", "Kroki odtworzenia, oczekiwany vs rzeczywisty wynik, środowisko."),
                 ("Czym różni się przypadek testowy od testu automatycznego?", "Przypadek to opis dla człowieka; test automatyczny to kod wykonujący go."),
                 ("Jaki jest test dobrego raportu?", "Programista odtwarza błąd bez pytań.")],
     "pulapki": ["Tytuł „nie działa logowanie” to za mało — „Logowanie z poprawnym hasłem zwraca błąd 500 po 3. próbie”.",
                 "Oczekiwany wynik piszesz z wymagań, nie z własnego domysłu — jeśli brak wymagań, zaznacz to."]},

    {"id": "ci", "tydzien": 9, "nazwa": "GitHub Actions i pytest-html",
     "slowa": ["actions", "workflow", "ci", "yml", "yaml", "pytest-html", "odznak", "badge"],
     "wyjasnienie":
         "CI (ciągła integracja) uruchamia testy automatycznie po każdym pushu na czystej maszynie w chmurze — dowód, że projekt "
         "działa nie tylko u Ciebie. Plik .github/workflows/tests.yml opisuje kroki: pobierz kod, zainstaluj Pythona, pip install -r "
         "requirements.txt, pytest. Zielony znacznik i odznaka w README to pierwsza rzecz, jaką rekruter widzi. "
         "pytest-html (pytest --html=raport.html) tworzy raport z wynikami, który dołączasz jako artefakt CI.",
     "przyklad":
         "# .github/workflows/tests.yml\n"
         "name: tests\n"
         "on: [push, pull_request]\n"
         "jobs:\n"
         "  test:\n"
         "    runs-on: ubuntu-latest\n"
         "    steps:\n"
         "      - uses: actions/checkout@v4\n"
         "      - uses: actions/setup-python@v5\n"
         "        with:\n"
         "          python-version: \"3.12\"\n"
         "      - run: pip install -r requirements.txt\n"
         "      - run: pytest -v --html=raport.html --self-contained-html\n"
         "      - uses: actions/upload-artifact@v4\n"
         "        if: always()\n"
         "        with:\n"
         "          name: raport\n"
         "          path: raport.html",
     "zadania": ["tests.yml uruchamiający pytest przy każdym pushu; zielony znacznik na GitHubie.",
                 "pip install pytest-html; raport HTML jako artefakt CI.",
                 "Odznaka CI w README (Actions → workflow → Create status badge)."],
     "pytania": [("Gdzie leży plik workflow?", ".github/workflows/"),
                 ("Co daje CI?", "Automatyczne testy przy każdym pushu na czystej maszynie."),
                 ("Po co requirements.txt w CI?", "Maszyna w chmurze instaluje z niego biblioteki.")],
     "pulapki": ["YAML wymaga spacji, nie tabulatorów.", "Testy Selenium w CI potrzebują trybu headless (opcja --headless w Chrome)."]},

    {"id": "sqlite", "tydzien": 10, "nazwa": "SQLite i planowanie projektu",
     "slowa": ["sqlite", "baza", "sql", "tabel", "plan.md", "zakres"],
     "wyjasnienie":
         "SQLite to baza danych w jednym pliku, wbudowana w Pythona (import sqlite3) — bez serwera i instalacji. "
         "Tabela to arkusz z kolumnami o typach: zwierzeta(id, imie, rasa, waga), zdarzenia(id, zwierze_id, data, typ, opis). "
         "Mówisz do niej w SQL: CREATE TABLE, INSERT, SELECT ... WHERE, DELETE. Zawsze przekazuj wartości przez ? (parametry), "
         "nigdy sklejaniem napisów. Przed kodowaniem: PLAN.md — zakres (co wchodzi, co nie), struktura plików, kolejność kroków; "
         "ustalasz go w trybie planowania, zanim utoniesz w szczegółach.",
     "przyklad":
         "import sqlite3\n\n"
         "def polacz(sciezka=\"stado.db\"):\n"
         "    con = sqlite3.connect(sciezka)\n"
         "    con.execute(\"CREATE TABLE IF NOT EXISTS zwierzeta (id INTEGER PRIMARY KEY, imie TEXT, rasa TEXT, waga REAL)\")\n"
         "    return con\n\n"
         "def dodaj(con, imie, rasa, waga):\n"
         "    con.execute(\"INSERT INTO zwierzeta (imie, rasa, waga) VALUES (?, ?, ?)\", (imie, rasa, waga))\n"
         "    con.commit()\n\n"
         "def pobierz(con):\n"
         "    return con.execute(\"SELECT id, imie, rasa, waga FROM zwierzeta ORDER BY imie\").fetchall()",
     "zadania": ["PLAN.md: zakres, struktura plików, kolejność kroków.",
                 "baza.py: tabele zwierzeta i zdarzenia, funkcje dodaj/pobierz/usuń; testy z bazą w tmp_path.",
                 "stado.py: rejestracja zwierzęcia, dodanie zdarzenia (szczepienie, wycielenie), lista zdarzeń po dacie."],
     "pytania": [("Czym jest SQLite?", "Bazą w jednym pliku wbudowaną w Pythona."),
                 ("Po co ? w zapytaniach?", "Bezpieczne przekazanie wartości — bez SQL injection."),
                 ("Po co PLAN.md?", "Ustalić zakres i kolejność, zanim zaczniesz kodować.")],
     "pulapki": ["Bez con.commit() dane nie zostaną zapisane.", "Testy na prawdziwym stado.db kasują Twoje dane — tmp_path."]},

    {"id": "flask", "tydzien": 11, "nazwa": "Flask: strony, formularze, walidacja",
     "slowa": ["flask", "route", "render_template", "formularz", "walidac", "app.py", "html"],
     "wyjasnienie":
         "Flask zamienia funkcje Pythona w strony WWW: @app.route(\"/\") łączy adres z funkcją, która zwraca HTML "
         "(render_template z szablonu w folderze templates/). Formularz wysyła dane metodą POST; odczytujesz request.form[\"imie\"]. "
         "Walidacja po stronie serwera jest obowiązkowa: puste pole, waga ujemna, litery zamiast liczby — odrzucasz z komunikatem, "
         "zanim cokolwiek trafi do bazy. Tester (czyli Ty) wpisze wszystko, co się da. python app.py uruchamia serwer na 127.0.0.1:5000.",
     "przyklad":
         "from flask import Flask, render_template, request, redirect\n"
         "import baza\n\n"
         "app = Flask(__name__)\n\n"
         "@app.route(\"/\")\n"
         "def lista():\n"
         "    return render_template(\"lista.html\", zwierzeta=baza.pobierz(baza.polacz()))\n\n"
         "@app.route(\"/dodaj\", methods=[\"GET\", \"POST\"])\n"
         "def dodaj():\n"
         "    blad = None\n"
         "    if request.method == \"POST\":\n"
         "        imie = request.form.get(\"imie\", \"\").strip()\n"
         "        try:\n"
         "            waga = float(request.form.get(\"waga\", \"\"))\n"
         "        except ValueError:\n"
         "            waga = -1\n"
         "        if not imie or waga <= 0:\n"
         "            blad = \"Podaj imię i wagę większą od zera.\"\n"
         "        else:\n"
         "            baza.dodaj(baza.polacz(), imie, request.form.get(\"rasa\", \"\"), waga)\n"
         "            return redirect(\"/\")\n"
         "    return render_template(\"dodaj.html\", blad=blad)\n\n"
         "if __name__ == \"__main__\":\n"
         "    app.run(debug=True)",
     "zadania": ["Strona główna z listą zwierząt z bazy.",
                 "Formularz dodawania z walidacją (puste pole, zła waga) i komunikatem.",
                 "Strona historii zdarzeń dla jednego zwierzęcia; 3 testy Selenium w POM uruchamiane w CI."],
     "pytania": [("Jak zdefiniować stronę główną?", "@app.route(\"/\")"),
                 ("Po co walidacja po stronie serwera?", "Żeby złe dane nie trafiły do bazy, cokolwiek wpisze użytkownik."),
                 ("Co robi python app.py?", "Uruchamia lokalny serwer WWW.")],
     "pulapki": ["Szablony muszą leżeć w folderze templates/.", "debug=True tylko lokalnie — nigdy na produkcji."]},

    {"id": "rekrutacja", "tydzien": 12, "nazwa": "CV, opowieść o projekcie, rozmowa rekrutacyjna",
     "slowa": ["cv", "rekrut", "rozmow", "opowie", "aplikac", "portfolio", "junior qa"],
     "wyjasnienie":
         "Sekcja Projekty w CV: nazwa, co robi, technologie, liczba testów, link do GitHuba i CI — każde słowo potwierdza kod, który "
         "rekruter może kliknąć. Opowieść o projekcie w 2 minuty: problem (ewidencja stada na kartkach) → rozwiązanie (SQLite + Flask) → "
         "jak testuję (pytest, Selenium w POM, CI) → czego się nauczyłem (np. że walidacja formularza to połowa błędów). "
         "Pytania rekrutacyjne na Junior QA krążą wokół: różnica test manualny/automatyczny, piramida testów, co to przypadek brzegowy, "
         "jak napisać bug raport, czym jest fixture, POM, dlaczego Wait zamiast sleep. Twoja przewaga: znasz dziedzinę projektu z 15 lat praktyki.",
     "przyklad":
         "## Projekty\n"
         "**System zarządzania gospodarstwem** — Python, SQLite, Flask, pytest (24 testy), Selenium (POM, 3 testy E2E), GitHub Actions.\n"
         "Ewidencja zwierząt i zdarzeń (szczepienia, wycielenia) z interfejsem WWW. github.com/LukaszTM/gospodarstwo · CI: zielone",
     "zadania": ["Sesja rekrutacyjna: 15 pytań (manual, pytest/Selenium, projekt) — Asystent offline ma pulę pytań: wpisz /rekrutacja.",
                 "Nagraj 2-minutową opowieść o projekcie; zapisz transkrypcję i skróć ją o 30%.",
                 "CV z sekcją Projekty i 5 pierwszych aplikacji."],
     "pytania": [("Co zawiera wpis w sekcji Projekty?", "Co robi, technologie, liczba testów, link do GitHuba i CI."),
                 ("Jak zbudować opowieść o projekcie?", "Problem → rozwiązanie → jak testuję → czego się nauczyłem."),
                 ("Sygnał gotowości do aplikowania?", "Naprawiasz test Selenium sam i tłumaczysz każdy plik koledze bez IT.")],
     "pulapki": ["CV bez linków do kodu to obietnica bez dowodu.", "Na rozmowie „nie wiem, ale sprawdziłbym tak…” jest lepsze niż zmyślanie."]},
]

# ---------------------------------------------------------------------------
# BŁĘDY PYTHONA — co znaczy, pytanie naprowadzające (nie rozwiązanie)
# ---------------------------------------------------------------------------
BLEDY = {
    "SyntaxError": {
        "co": "Python nie rozumie składni — zwykle brak dwukropka po if/for/def, niedomknięty nawias lub cudzysłów, albo literówka w słowie kluczowym.",
        "pytanie": "Spójrz na linię wskazaną w błędzie I NA POPRZEDNIĄ. Czy każdy if/for/def kończy się dwukropkiem? Czy liczba nawiasów otwierających równa się zamykającym?"},
    "IndentationError": {
        "co": "Wcięcia są nierówne albo mieszasz tabulatory ze spacjami. Python wcięciami rozpoznaje, co należy do bloku.",
        "pytanie": "Czy wszystkie linie w tym bloku zaczynają się od tej samej liczby spacji (4)? PyCharm: Edit → Convert Indents → To Spaces."},
    "NameError": {
        "co": "Używasz nazwy, której Python nie zna — literówka, zmienna zdefiniowana później, albo zmienna z wnętrza funkcji użyta na zewnątrz.",
        "pytanie": "Gdzie ta nazwa dostaje wartość po raz pierwszy? Czy to miejsce wykonuje się PRZED linią z błędem — i w tym samym zakresie (funkcja/poza funkcją)?"},
    "TypeError": {
        "co": "Operacja na niepasujących typach: napis + liczba, wywołanie funkcji ze złą liczbą argumentów, indeksowanie liczby.",
        "pytanie": "Jakiego typu są wartości po obu stronach operatora w tej linii? Wypisz je przez print(type(x)). Czy jedna z nich przyszła z input()?"},
    "ValueError": {
        "co": "Typ się zgadza, ale wartość nie — int(\"abc\"), float(\"\"), lista.remove(czegoś, czego nie ma).",
        "pytanie": "Jaka dokładnie wartość trafia do tej funkcji? Czy użytkownik mógł wpisać coś, co nie jest liczbą — i czy try/except by to złapał?"},
    "ZeroDivisionError": {
        "co": "Dzielisz przez zero. Często: średnia z pustej listy (sum / len == 0).",
        "pytanie": "Co jest dzielnikiem w tej linii i w jakiej sytuacji może być zerem? Pusta lista? Wpisane 0? Jaki warunek przed dzieleniem by to wykluczył?"},
    "IndexError": {
        "co": "Indeks poza listą — lista ma 3 elementy (0,1,2), a prosisz o [3]; albo lista jest pusta.",
        "pytanie": "Ile elementów ma lista w chwili błędu (print(len(lista)))? Czy pętla używa range(len(lista)) i sięga o jeden za daleko?"},
    "KeyError": {
        "co": "Słownik nie ma takiego klucza — literówka w kluczu, inna wielkość liter, albo klucz jeszcze nie dodany.",
        "pytanie": "Wypisz słownik.keys() tuż przed tą linią. Czy klucz, którego szukasz, jest tam DOKŁADNIE tak zapisany? Czy .get() z wartością domyślną by pomogło?"},
    "AttributeError": {
        "co": "Obiekt nie ma takiej metody/atrybutu: 'NoneType' object has no attribute — funkcja zwróciła None (brak return); 'list' object has no attribute 'push' — zła nazwa metody.",
        "pytanie": "Co dokładnie jest po lewej stronie kropki i jakiego jest typu? Jeśli NoneType — która funkcja zwróciła None zamiast wartości (sprawdź jej return)?"},
    "ModuleNotFoundError": {
        "co": "Nie ma takiej biblioteki w tym środowisku — nie zainstalowana (pip install), albo zainstalowana w innym venv, albo literówka w nazwie.",
        "pytanie": "Czy venv jest aktywny w terminalu, z którego uruchamiasz (nazwa w nawiasie przed ścieżką)? Co pokazuje pip list? Czy PyCharm używa tego samego interpretera?"},
    "ImportError": {
        "co": "Moduł jest, ale nie ma w nim tej nazwy — literówka w from X import Y, import kołowy, albo własny plik nazwany jak biblioteka.",
        "pytanie": "Czy nazwa po import jest dokładnie taka jak w pliku źródłowym? Czy masz w projekcie plik o nazwie biblioteki (np. random.py, csv.py)?"},
    "FileNotFoundError": {
        "co": "Pliku nie ma tam, gdzie program szuka. Ścieżka względna liczy się od katalogu, z którego uruchomiono program, nie od pliku .py.",
        "pytanie": "Z jakiego katalogu uruchamiasz program (print(os.getcwd()))? Czy plik leży właśnie tam? Czy nazwa i rozszerzenie zgadzają się co do litery?"},
    "UnboundLocalError": {
        "co": "Zmienna w funkcji jest użyta przed przypisaniem — Python uznał ją za lokalną, bo gdzieś w funkcji ją przypisujesz.",
        "pytanie": "Czy w tej funkcji przypisujesz tej zmiennej wartość (x = ...) i jednocześnie czytasz ją wcześniej? Może powinna być argumentem funkcji?"},
    "RecursionError": {
        "co": "Funkcja wywołuje samą siebie bez końca — brak warunku stopu w rekurencji (np. silnia bez if n == 0).",
        "pytanie": "Jaki jest warunek, przy którym funkcja NIE wywołuje siebie? Czy argument na pewno zbliża się do tego warunku w każdym wywołaniu?"},
    "AssertionError": {
        "co": "assert był fałszywy — w teście znaczy: kod zwrócił inny wynik niż oczekiwany. To nie awaria, to informacja.",
        "pytanie": "Jaką wartość zwrócił kod, a jakiej oczekiwał test (pytest pokazuje obie)? Który z nich jest w błędzie — kod czy oczekiwanie w teście?"},
    "TimeoutException": {
        "co": "Selenium: element nie pojawił się w zadanym czasie — zły lokator, strona jeszcze się ładuje, element w innej ramce/karcie.",
        "pytanie": "Czy lokator znajduje element w konsoli przeglądarki (F12 → $(\"#id\") lub $x(\"//...\"))? Czy element pojawia się dopiero po jakiejś akcji?"},
    "NoSuchElementException": {
        "co": "Selenium nie znalazło elementu — lokator nie pasuje albo strona nie zdążyła się załadować (brak WebDriverWait).",
        "pytanie": "Czy szukasz elementu zaraz po get()/click(), bez czekania? Czy ten sam lokator działa w narzędziach deweloperskich przeglądarki?"},
    "KeyboardInterrupt": {
        "co": "Przerwałeś program klawiszem Ctrl+C — zwykle przy pętli nieskończonej.",
        "pytanie": "Który warunek pętli nigdy nie stał się fałszywy? Czy w pętli zmieniasz zmienną, od której zależy warunek?"},
}

# ---------------------------------------------------------------------------
# POJĘCIA — krótkie definicje „jak dziesięciolatkowi”
# ---------------------------------------------------------------------------
POJECIA = {
    "terminal": "Terminal to okno, w którym rozmawiasz z komputerem tekstem zamiast klikania: wpisujesz komendę, Enter, komputer odpowiada. Jak CB-radio do komputera.",
    "katalog roboczy": "Katalog roboczy to folder, w którym terminal „stoi” w tej chwili. Komendy (python plik.py) szukają plików właśnie tam. cd zmienia katalog, pwd/cd (bez argumentu) pokazuje, gdzie jesteś.",
    "plik .py": "Plik .py to zwykły plik tekstowy z kodem Pythona. Python czyta go linia po linii od góry i wykonuje. Uruchamiasz: python nazwa.py.",
    "zmienna": "Zmienna to pudełko z etykietą, w którym trzymasz wartość: na pudełku „waga” leży 612. Możesz zajrzeć, podmienić, policzyć.",
    "funkcja": "Funkcja to zapisany raz przepis z nazwą: „oblicz dawkę paszy dla wagi X”. Wołasz go po nazwie, podajesz dane, dostajesz wynik — bez przepisywania kroków.",
    "pętla": "Pętla to powtarzanie tej samej czynności dla każdego elementu albo dopóki coś trwa: „dla każdej krowy: zważ” / „dopóki zbiornik niepełny: dolewaj”.",
    "git": "Git to dziennik zmian w projekcie: zapisujesz zdjęcia (commity) stanu plików i możesz wrócić do dowolnego. GitHub to miejsce w internecie, gdzie te zdjęcia trzymasz i pokazujesz innym.",
    "commit": "Commit to zapisane zdjęcie wszystkich plików projektu w danej chwili, z podpisem co się zmieniło. Robisz: git add . → git commit -m \"opis\".",
    "repozytorium": "Repozytorium to folder projektu śledzony przez Gita — z całą historią zmian. Lokalne jest na Twoim dysku, zdalne na GitHubie.",
    "claude.md": "CLAUDE.md to plik z zasadami, który Claude Code czyta na starcie sesji w katalogu projektu. Tu wpisujesz: „nie pisz rozwiązań za mnie”.",
    "tryb planowania": "Tryb planowania (Shift+Tab aż zobaczysz „plan”): Claude opisuje podejście i strukturę, ale nie zmienia plików. Ty czytasz, pytasz, dopiero potem kodujesz.",
    "api": "API to okienko, przez które jeden program pyta drugi o dane albo prosi o czynność — bez klikania w stronę. Pogoda z open-meteo to API.",
    "json": "JSON to zapis danych jako tekst w formie słowników i list: {\"imie\": \"Krasula\", \"waga\": 612}. Tak rozmawiają ze sobą programy.",
    "test": "Test to mały program, który sprawdza, czy inny program daje spodziewany wynik: assert dawka(600) == 15. Uruchamiasz pytest i od razu wiesz, co się zepsuło.",
    "fixture": "Fixture to przygotowanie sceny do testu: utworzenie menedżera z 3 zadaniami, bazy tymczasowej — każdy test dostaje świeżą kopię.",
    "selenium": "Selenium steruje prawdziwą przeglądarką z kodu: wchodzi na stronę, klika, wpisuje, czyta — jak użytkownik, tylko automatycznie i powtarzalnie.",
    "page object model": "Page Object Model: każda strona WWW to klasa z lokatorami i akcjami (LoginPage.login()). Testy wołają metody, więc zmiana strony = poprawka w jednym miejscu.",
    "bug raport": "Bug raport to zgłoszenie usterki tak opisane, że programista odtworzy ją bez pytań: kroki, co miało być, co było, środowisko, zrzut.",
    "ci": "CI (ciągła integracja): po każdym pushu chmura pobiera Twój kod na czystą maszynę i uruchamia testy. Zielono = działa nie tylko u Ciebie.",
    "venv": "venv to osobna szafka z bibliotekami dla jednego projektu. Dzięki temu projekty nie kłócą się o wersje.",
    "docstring": "Docstring to opis funkcji w potrójnych cudzysłowach tuż pod def — czyta go help(), PyCharm i każdy, kto otworzy Twój kod.",
    "readme": "README to tablica informacyjna przy wejściu do projektu: co to robi, jak uruchomić, jak wygląda. Rekruter czyta to pierwsze.",
    "refaktoryzacja": "Refaktoryzacja to sprzątanie kodu bez zmiany tego, co robi: lepsze nazwy, krótsze funkcje, bez powtórzeń.",
    "sqlite": "SQLite to baza danych w jednym pliku, wbudowana w Pythona. Tabele jak arkusze, pytania w języku SQL.",
    "flask": "Flask zamienia funkcje Pythona w strony WWW: adres /dodaj → funkcja dodaj() → HTML w przeglądarce.",
}

# Pytania rekrutacyjne na Junior QA (tryb offline: /rekrutacja)
PYTANIA_REKRUTACYJNE = [
    ("manual", "Czym różni się test manualny od automatycznego i kiedy wybrałbyś każdy z nich?",
     "Manualny: człowiek wykonuje kroki — dobry do eksploracji, UX, jednorazowych sprawdzeń. Automatyczny: kod — dobry do powtarzalnych regresji. Oba się uzupełniają."),
    ("manual", "Co to jest przypadek brzegowy? Podaj 3 przykłady dla pola „waga zwierzęcia”.",
     "Skrajne/graniczne dane: 0, wartość ujemna, bardzo duża (99999), puste pole, litery, przecinek zamiast kropki."),
    ("manual", "Co musi zawierać dobry bug raport?",
     "Tytuł, kroki odtworzenia, oczekiwany vs rzeczywisty wynik, środowisko, priorytet, załącznik. Test: programista odtwarza bez pytań."),
    ("manual", "Czym jest piramida testów?",
     "Dużo szybkich testów jednostkowych na dole, mniej integracyjnych, najmniej wolnych E2E na górze."),
    ("manual", "Różnica między błędem (bug), awarią (failure) a defektem?",
     "Defekt/bug — wada w kodzie; awaria — widoczne złe zachowanie wywołane defektem. Jeden defekt może nie dać awarii, dopóki nie trafi na odpowiednie dane."),
    ("auto", "Czym jest fixture w pytest i po co jej używasz?",
     "Funkcją przygotowującą dane/obiekty dla testów (z @pytest.fixture); każdy test dostaje świeży egzemplarz jako argument."),
    ("auto", "Co daje @pytest.mark.parametrize?",
     "Jeden test uruchamiany dla wielu zestawów danych — mniej kopii, czytelna tabela przypadków."),
    ("auto", "Dlaczego WebDriverWait zamiast time.sleep?",
     "Wait czeka tylko tyle, ile trzeba, do spełnienia warunku (max N s); sleep zawsze pełny czas — za długo lub za krótko."),
    ("auto", "Na czym polega Page Object Model i jaki ma sens?",
     "Klasa na stronę z lokatorami i akcjami; testy używają metod. Zmiana strony = poprawka w jednym miejscu."),
    ("auto", "Który lokator Selenium jest najstabilniejszy i dlaczego?",
     "id (albo dedykowany atrybut data-test): unikalny, rzadko się zmienia. XPath po pełnej ścieżce psuje się przy zmianie układu."),
    ("projekt", "Opowiedz o swoim projekcie w 2 minuty.",
     "Problem → rozwiązanie → technologie → jak testujesz → czego się nauczyłeś. Konkretne liczby: ile testów, CI."),
    ("projekt", "Jaki najtrudniejszy błąd znalazłeś w swoim projekcie i jak go wykryłeś?",
     "Konkretna historia: objaw, jak zawęziłeś (test/print/debugger), przyczyna, test, który teraz tego pilnuje."),
    ("projekt", "Co byś przetestował w formularzu dodawania zwierzęcia?",
     "Puste pola, waga 0/ujemna/litery, bardzo długie imię, znaki specjalne, podwójne wysłanie, zapis w bazie, komunikaty błędów."),
    ("projekt", "Jak działa Twoje CI i co się dzieje, gdy test nie przejdzie?",
     "GitHub Actions: checkout → Python → pip install -r → pytest; czerwony status na PR/commicie, raport HTML w artefaktach."),
    ("projekt", "Czego nie zdążyłeś zrobić w projekcie i co zrobiłbyś jako następne?",
     "Szczerze: np. testy wydajności, autoryzacja, więcej E2E. Pokaż, że widzisz braki i masz plan."),
]
