# -*- coding: utf-8 -*-
"""Kadry i płace — lekcje tygodni 0–5. Każda: wyjasnienie, przyklad, zadania, pytania, pulapki, test (3 pytania A–D)."""

LEKCJE_1 = [
    # ================================================================ TYDZIEŃ 0
    {"id": "zrodla_prawa", "tydzien": 0, "nazwa": "Źródła prawa pracy i gdzie sprawdzać stan prawny",
     "slowa": ["źródła prawa", "zrodla prawa", "kodeks pracy", "isap", "dziennik ustaw", "tekst jednolity", "rozporządzenie", "hierarchia"],
     "wyjasnienie":
         "Kadrowiec nie uczy się przepisów na pamięć — uczy się, gdzie są i jak je czytać. Hierarchia: Konstytucja → ustawy (Kodeks pracy, ustawa o systemie ubezpieczeń społecznych, zasiłkowa, PIT, ZFŚS, PPK, o zwolnieniach grupowych) → rozporządzenia (wykonawcze: o dokumentacji pracowniczej, o wynagrodzeniu urlopowym, o minimalnym wynagrodzeniu, składkowe) → akty wewnątrzzakładowe (układ zbiorowy, regulamin pracy i wynagradzania — nie mogą być mniej korzystne niż ustawa) → umowa o pracę (nie może być mniej korzystna niż regulamin). Zasada uprzywilejowania pracownika (art. 18 KP): postanowienie mniej korzystne jest nieważne, w jego miejsce wchodzi przepis.\n"
         "Gdzie czytać: ISAP (isap.sejm.gov.pl) — teksty ujednolicone z polem „stan prawny na dzień”; Dziennik Ustaw (dziennikustaw.gov.pl) — ogłoszone akty, w tym nowelizacje; Monitor Polski — obwieszczenia (limit 30-krotności, kwoty ZFŚS); zus.pl i podatki.gov.pl — wskaźniki, formularze, objaśnienia MF; PIP (pip.gov.pl) — poradniki i stanowiska; orzecznictwo SN (sn.pl) — gdy przepis jest nieostry (np. „ciężkie naruszenie”). Portale (Infor, Gofin, Lex) to komentarze — pomagają, ale źródłem jest akt.\n"
         "Nawyki: (1) każdą liczbę sprawdzasz u źródła raz w roku i po nowelizacji; (2) czytając przepis, patrzysz na datę wejścia w życie i przepisy przejściowe — w 2026 wiele zmian działa od różnych dat (staż: 1.01 publiczny / 1.05 prywatny; mobbing: 5.11.2026 z procedurami do 5.05.2027; jawność w rekrutacji: 24.12.2025; kontrola L4: 13.04.2026); (3) rozróżniasz „obowiązuje” od „projekt” — w tym kursie każda taka informacja ma oznaczenie.",
     "przyklad":
         "Pytanie: ile wynosi dodatek za pracę w nocy?\n"
         "1. Art. 151⁸ KP: 20% stawki godzinowej wynikającej z minimalnego wynagrodzenia.\n"
         "2. Minimalne 2026: rozporządzenie RM z 11.09.2025 (Dz.U. 2025 poz. 1242) → 4 806 zł.\n"
         "3. Wymiar listopada 2026 (art. 130 KP): 20 dni × 8 h = 160 h.\n"
         "4. 4 806 / 160 = 30,04 zł → 20% = 6,01 zł za godzinę nocną w listopadzie.\n"
         "Każdy krok ma źródło — tak odpowiadasz zarządowi i inspektorowi.",
     "zadania": ["Znajdź w ISAP tekst ujednolicony KP i zapisz datę stanu prawnego oraz trzy ostatnie nowelizacje.",
                 "Sprawdź w M.P. obwieszczenie o limicie 30-krotności na 2026 i zapisz kwotę ze źródłem.",
                 "Znajdź na podatki.gov.pl aktualny wzór PIT-2 i numer wersji."],
     "pytania": [["Co jest ważniejsze: regulamin wynagradzania czy umowa o pracę, gdy umowa daje mniej?", "Regulamin — umowa nie może być mniej korzystna (art. 18 KP); postanowienie umowy jest nieważne."],
                 ["Czym różni się tekst ujednolicony od Dziennika Ustaw?", "Dz.U. ogłasza akty i nowelizacje; tekst ujednolicony to scalona wersja z naniesionymi zmianami (ISAP), do codziennej pracy."],
                 ["Gdzie szukasz kwoty odpisu na ZFŚS?", "Obwieszczenie GUS o przeciętnym wynagrodzeniu w II półroczu roku poprzedniego (37,5% tej kwoty)."]],
     "pulapki": ["Portal podaje kwotę z poprzedniego roku — sprawdź datę artykułu.", "„Projekt ustawy” w nagłówku ≠ obowiązujące prawo."],
     "test": [
         {"p": "Umowa o pracę przewiduje 18 dni urlopu dla pracownika ze stażem 12 lat. Co obowiązuje?", "o": ["18 dni — strony tak ustaliły", "26 dni — postanowienie mniej korzystne jest nieważne (art. 18 KP)", "20 dni", "Zależy od regulaminu"], "odp": 1, "w": "Zasada uprzywilejowania pracownika."},
         {"p": "Gdzie znajdziesz tekst ujednolicony Kodeksu pracy ze stanem prawnym na dzień?", "o": ["Na portalu Infor", "W ISAP (isap.sejm.gov.pl)", "W Monitorze Polskim", "Na stronie PIP"], "odp": 1, "w": "ISAP = Internetowy System Aktów Prawnych Sejmu."},
         {"p": "Od kiedy obowiązuje nowa definicja mobbingu?", "o": ["24.12.2025", "1.01.2026", "5.11.2026", "5.05.2027"], "odp": 2, "w": "Ustawa z 19.06.2026 (Dz.U. 2026 poz. 1046); procedury pracodawców do 5.05.2027."},
     ]},

    {"id": "narzedzia_kadrowca", "tydzien": 0, "nazwa": "Narzędzia: eZUS/PUE, Płatnik, e-Urząd Skarbowy, program kadrowy",
     "slowa": ["narzędzi", "narzedzi", "ezus", "pue", "płatnik", "platnik", "e-urząd", "e-deklaracje", "pel", "upl-1", "program kadrowy"],
     "wyjasnienie":
         "Cztery systemy, bez których nie da się pracować. eZUS (dawniej PUE ZUS) — portal ZUS: jako płatnik widzisz ubezpieczonych, e-ZLA pracowników, saldo składek, składasz wnioski (Z-3, US-3 → A1, zaświadczenie o niezaleganiu), odbierasz pisma. Dostęp dla pracownika kadr daje pełnomocnictwo PEL podpisane przez zarząd. Płatnik — program desktopowy ZUS do dokumentów zgłoszeniowych (ZUA, ZZA, ZWUA, ZCNA) i rozliczeniowych (DRA, RCA, RSA, RPA), z weryfikacją i wysyłką z certyfikatem kwalifikowanym; małe firmy mogą użyć ePłatnika w eZUS. W praktyce dokumenty generuje program kadrowo-płacowy (Symfonia, Optima, enova, Gratyfikant…) i eksportuje do Płatnika (plik KEDU) — ale rozumieć musisz, co jest w środku, bo to Ty odpowiadasz za błędy.\n"
         "e-Urząd Skarbowy / e-Deklaracje — PIT-4R, PIT-11, PIT-8AR, IFT składasz elektronicznie; podpisuje osoba z pełnomocnictwem UPL-1 (zgłoszonym do US). Zaliczki PIT wpłacasz na mikrorachunek podatkowy firmy (NIP). Program kadrowy generuje PIT-11, ale kartoteka przychodów musi być prowadzona poprawnie przez cały rok — PIT-11 to tylko jej suma.\n"
         "Pozostałe: praca.gov.pl (powiadomienia o cudzoziemcach, PUP), e-PFRON2 (DEK, Wn-D), portal sprawozdawczy GUS, platforma PPK instytucji finansowej (zapisy, wpłaty — plik), e-Doręczenia (od 2025 obowiązkowe dla firm — pisma urzędowe). Zasada bezpieczeństwa: oddzielne konto i uprawnienia dla każdej osoby, rejestr pełnomocnictw, odwołanie przy odejściu pracownika kadr tego samego dnia.\n"
         "## W tym kursie: Warsztat zamiast kont\n"
         "Żadnego z tych systemów nie musisz zakładać ani instalować. Zakładka Warsztat w Mentorze ma ich symulatory: „eZUS / Płatnik” (rejestr ubezpieczonych, dokumenty zgłoszeniowe z weryfikacją jak w Płatniku, komplety DRA/RCA/RSA, skrzynka e-ZLA, rejestr z numerami UPP), „e-Urząd: PIT” (PIT-11 i PIT-4R z Twojej kartoteki, UPO) oraz kalkulatory (lista płac, zasiłki, urlopy, czas pracy, potrącenia) i bibliotekę przepisów. Ekrany i komunikaty odpowiadają prawdziwym, więc po kursie przesiadka na eZUS i Płatnika to kwestia logowania, nie nauki od nowa.",
     "przyklad":
         "Miesięczny obieg w firmie 62-osobowej:\n"
         "1. do 5. — zamknięcie ewidencji czasu pracy, e-ZLA z eZUS\n"
         "2. do 8. — lista płac w programie, kontrola, przelewy na 10.\n"
         "3. do 15. — eksport KEDU → Płatnik → weryfikacja → wysyłka DRA/RCA/RSA; przelew składek na NRS; plik PPK do instytucji\n"
         "4. do 20. — zaliczka PIT na mikrorachunek; DEK-I-0 PFRON\n"
         "5. do 25. — Wn-D (dofinansowanie niepełnosprawnych, jeśli dotyczy)",
     "zadania": ["Zaloguj się do eZUS i znajdź w panelu Ubezpieczonego swoje zwolnienia e-ZLA oraz informację o stanie konta.",
                 "Zainstaluj Płatnika, utwórz bazę ćwiczeniową i dodaj płatnika z testowym NIP.",
                 "Wypisz, jakie pełnomocnictwa (PEL, UPL-1) musiałby mieć nowy pracownik kadr i kto je podpisuje."],
     "pytania": [["Kto wysyła DRA, gdy firma zatrudnia 62 osoby?", "Płatnik (pracodawca) — przez program Płatnik z certyfikatem lub ePłatnik; w praktyce kadry z pełnomocnictwem PEL."],
                 ["Czym różni się UPL-1 od PEL?", "UPL-1 — pełnomocnictwo do podpisywania e-deklaracji podatkowych (US); PEL — pełnomocnictwo do ZUS."],
                 ["Co to jest KEDU?", "Plik z dokumentami ZUS (format XML) eksportowany z programu kadrowego do Płatnika."]],
     "pulapki": ["Jedno hasło do Płatnika dla całego działu — po odejściu pracownika nikt go nie zmienia.", "Program kadrowy „liczy sam” — ale źle wprowadzony kod tytułu lub oświadczenie daje błędne DRA/PIT przez cały rok."],
     "test": [
         {"p": "Jakim dokumentem zarząd upoważnia kadrową do działania w ZUS przez eZUS?", "o": ["UPL-1", "PEL", "ZUS ZUA", "ZUS PEL-K"], "odp": 1, "w": "PEL = pełnomocnictwo ZUS; PEL-K to jego odwołanie; UPL-1 dotyczy podatków."},
         {"p": "Gdzie wpłacasz zaliczki na PIT od wynagrodzeń?", "o": ["Na rachunek ZUS (NRS)", "Na mikrorachunek podatkowy firmy (NIP)", "Na konto pracownika", "Na rachunek PFR"], "odp": 1, "w": "NRS jest dla składek ZUS; podatki — mikrorachunek."},
         {"p": "Kto składa raporty miesięczne RCA/RSA?", "o": ["Pracownik przez eZUS", "Płatnik składek (pracodawca)", "Urząd skarbowy", "Instytucja PPK"], "odp": 1, "w": "To dokumenty rozliczeniowe płatnika."},
     ]},

    {"id": "wskazniki_2026", "tydzien": 0, "nazwa": "Wskaźniki 2026 — liczby, które musisz znać",
     "slowa": ["wskaźnik", "wskaznik", "minimalne wynagrodzenie", "4806", "stawki", "limit 30", "kwota wolna", "próg", "prog"],
     "wyjasnienie":
         "Minimalne wynagrodzenie 2026: 4 806 zł brutto (pełny etat), minimalna stawka godzinowa 31,40 zł (zlecenia, usługi) — rozporządzenie RM z 11.09.2025. Na 2027: 4 950 zł i 32,30 zł (rozporządzenie z 14.09.2026, Dz.U. 2026 poz. 1213). Od minimalnej zależą: dodatek nocny (20% stawki godzinowej z minimalnej), kwoty wolne od potrąceń (minimalne netto), maksymalna odprawa (15× = 72 090 zł), odszkodowanie za mobbing (6× = 28 836 zł), wynagrodzenie za przestój, minimalna podstawa zasiłku, obniżona wpłata PPK (≤ 120% = 5 767,20 zł).\n"
         "Składki ZUS (stopy od lat niezmienne): emerytalna 19,52% (9,76 pracownik + 9,76 pracodawca), rentowa 8% (1,5 + 6,5), chorobowa 2,45% (pracownik), wypadkowa 1,67% dla płatników do 9 ubezpieczonych, inaczej wg PKD (0,67–3,33%), zdrowotna 9% (pracownik, od podstawy po składkach społecznych), FP 2,45% (w tym FS 1,45%) i FGŚP 0,10% (pracodawca), FEP 1,5% (prace szczególne). Pracownik oddaje 13,71% brutto na społeczne; pracodawca dokłada ~20,48% (przy wypadkowej 1,67). Roczny limit podstawy emerytalno-rentowej 2026: 282 600 zł (30 × prognozowane 9 420 zł).\n"
         "PIT 2026: skala 12% do 120 000 zł dochodu, 32% od nadwyżki; kwota wolna 30 000 zł → kwota zmniejszająca 3 600 zł rocznie = 300 zł miesięcznie (PIT-2); KUP 250 zł (300 zł dojeżdżający), 20% zlecenia, 50% autorskie; ulga dla młodych (do 26 lat) do 85 528 zł przychodu; danina solidarnościowa 4% ponad 1 mln. Projekt od 2027: próg 130 000, stawka 24% do 150 000 — uchwalony przez Sejm X 2026, w Senacie; sprawdzaj.\n"
         "Inne: współczynnik ekwiwalentu 2026 — 20,92 (251 dni roboczych); odpis ZFŚS 2 943,23 zł (37,5% × 7 848,60); PPK 2% + 1,5% (+250 powitalna, +240 rocznie); zasiłek chorobowy 80% (100% ciąża/wypadek w drodze), wynagrodzenie chorobowe 33 dni (14 dla 50+) nadal od pracodawcy (XI 2026); okres zasiłkowy 182/270 dni; urlop 20/26 dni, opiekuńczy 5, siła wyższa 2 dni/16 h.",
     "przyklad":
         "Pensja 4 806 zł brutto (KUP 250, PIT-2, bez PPK):\n"
         "społeczne 469,07 + 72,09 + 117,75 = 658,91 → podstawa zdrowotnej 4 147,09 → zdrowotna 373,24\n"
         "podstawa PIT = 4 806 − 658,91 − 250 = 3 897 → 12% = 467,64 − 300 = 167,64 → 168\n"
         "netto = 4 806 − 658,91 − 373,24 − 168 = 3 605,85 zł\n"
         "koszt pracodawcy = 4 806 + składki pracodawcy (469,07 + 312,39 + 80,26 + 117,75 + 4,81) = 5 790,28 zł (≈ 4 806 × 1,2048)",
     "zadania": ["Zbuduj tabelę 25 wskaźników z linkami do źródeł (zadanie tygodnia 0).",
                 "Policz dodatek nocny za 1 h dla każdego miesiąca 2026 (zmienia się z wymiarem).",
                 "Policz, od którego miesiąca pracownik z pensją 14 000 zł przekroczy próg 120 000 zł dochodu."],
     "pytania": [["Ile wynosi suma składek społecznych finansowanych przez pracownika?", "13,71% (9,76 + 1,5 + 2,45)."],
                 ["Jaki jest limit 30-krotności w 2026 i czego dotyczy?", "282 600 zł; po przekroczeniu nie nalicza się składek emerytalnej i rentowej (chorobowa, wypadkowa, zdrowotna — dalej)."],
                 ["Ile wynosi kwota zmniejszająca podatek miesięcznie i co ją uruchamia?", "300 zł; oświadczenie PIT-2 (1/12), 150 zł (1/24), 100 zł (1/36)."]],
     "pulapki": ["Kwota wolna 30 000 zł to nie „pierwsze 30 000 bez podatku” w liście płac — to 300 zł miesięcznie odejmowane od zaliczki.", "Składka wypadkowa 1,67% tylko dla małych płatników — firma 62-osobowa ma stopę z PKD."],
     "test": [
         {"p": "Minimalna stawka godzinowa dla zleceniobiorcy w 2026 r.?", "o": ["30,50 zł", "31,40 zł", "32,30 zł", "28,10 zł"], "odp": 1, "w": "32,30 zł będzie w 2027."},
         {"p": "Jaka część składki emerytalnej obciąża pracownika?", "o": ["19,52%", "9,76%", "6,5%", "1,5%"], "odp": 1, "w": "Połowa 19,52%; drugą połowę płaci pracodawca."},
         {"p": "Ile wynosi roczny limit podstawy składek emerytalno-rentowych w 2026?", "o": ["234 720 zł", "260 190 zł", "282 600 zł", "300 000 zł"], "odp": 2, "w": "30 × 9 420 zł."},
     ]},

    # ================================================================ TYDZIEŃ 1
    {"id": "rekrutacja_jawnosc", "tydzien": 1, "nazwa": "Rekrutacja: dane kandydata, jawność wynagrodzeń, RODO",
     "slowa": ["rekrutac", "ogłoszen", "ogloszen", "kandydat", "jawność", "jawnosc", "widełki", "widelki", "art. 221", "rodo w rekrutacji"],
     "wyjasnienie":
         "Od kandydata możesz żądać tylko danych z art. 22¹ §1 KP: imię i nazwisko, data urodzenia, dane kontaktowe, a gdy są niezbędne do pracy na stanowisku — wykształcenie, kwalifikacje, przebieg zatrudnienia. Od 24.12.2025 (Dz.U. 2025 poz. 807) wprost zakazane jest żądanie informacji o wynagrodzeniu w obecnej i poprzednich pracach (art. 22¹ §1 pkt 6) — ani pytaniem, ani przez dokumenty. Inne dane (np. niekaralność) — tylko gdy przepis szczególny tego wymaga. Dane „wrażliwe” (zdrowie, związki) — nie; wyjątek: na wniosek pracodawcy orzeczenie o niepełnosprawności podaje sam kandydat, jeśli chce.\n"
         "Jawność wynagrodzeń w rekrutacji (art. 18³ᶜᵃ KP, od 24.12.2025): kandydat musi dostać informację o początkowym wynagrodzeniu lub jego przedziale (ustalonym obiektywnie, neutralnie płciowo) oraz o postanowieniach układu/regulaminu wynagradzania, jeśli mają zastosowanie — najpóźniej w ogłoszeniu, a jeśli nie było ogłoszenia lub go tam nie podano, przed pierwszą rozmową; gdy rozmów nie ma — przed nawiązaniem stosunku pracy. Forma: papierowa lub elektroniczna, z wyprzedzeniem. Ogłoszenia mają być neutralne płciowo. Sankcja: grzywna 1 000–30 000 zł (art. 281) i odszkodowanie za dyskryminację (nie mniej niż minimalne wynagrodzenie, art. 18³ᵈ). Pełne wdrożenie dyrektywy 2023/970 (prawo do informacji o średnich płacach, raport luki) to projekt UC127 — jeszcze nieuchwalony (XI 2026).\n"
         "RODO: podstawa to art. 22¹ KP (obowiązek prawny) i działania przed zawarciem umowy; na dane ponadstandardowe w CV — zgoda przez samo ich podanie (ale nie wolno ich żądać); klauzula informacyjna w ogłoszeniu lub przy pierwszym kontakcie; retencja: do zakończenia rekrutacji (+ okres ewentualnych roszczeń, ale UODO: niezwłocznie), do 12 miesięcy na przyszłe rekrutacje za zgodą. Testy, sprawdzanie referencji — tylko w zakresie art. 22¹ i za zgodą kandydata na kontakt z referentem.",
     "przyklad":
         "Fragment ogłoszenia 2026:\n"
         "Stanowisko: osoba na stanowisko operatora linii produkcyjnej (praca 3-zmianowa, system równoważny do 12 h)\n"
         "Wynagrodzenie: 5 200–6 100 zł brutto (zasadnicze, zależnie od doświadczenia) + dodatek za pracę w nocy (20% stawki godz. z minimalnej) + premia regulaminowa do 10% wg regulaminu wynagradzania z 1.03.2025\n"
         "Klauzula: Administratorem danych jest AGRO-MLEKO sp. z o.o. … podstawa: art. 22¹ KP i art. 6 ust. 1 lit. b, c RODO … dane przechowujemy do zakończenia rekrutacji, a za Twoją zgodą 12 miesięcy …",
     "zadania": ["Przepisz 3 pytania zakazane na rozmowie na wersje dozwolone.",
                 "Napisz klauzulę RODO dla rekrutacji z retencją 12 miesięcy za zgodą.",
                 "Sprawdź 3 ogłoszenia z pracuj.pl pod kątem widełek i neutralności — zapisz wnioski."],
     "pytania": [["Czy można zapytać kandydata o oczekiwania finansowe?", "Tak — zakaz dotyczy pytania o DOTYCHCZASOWE zarobki, nie o oczekiwania."],
                 ["Kiedy najpóźniej kandydat musi poznać widełki?", "W ogłoszeniu, a jeśli nie — przed pierwszą rozmową; bez rozmów — przed nawiązaniem stosunku pracy."],
                 ["Jak długo trzymasz CV odrzuconego kandydata?", "Do zakończenia rekrutacji; dłużej (do 12 mies.) tylko za zgodą na przyszłe rekrutacje."]],
     "pulapki": ["„Widełki od 4 806 do 20 000” — formalnie przedział, ale nieobiektywny; PIP i sąd ocenią jako obejście.", "Prośba o „ostatni pasek wynagrodzeń” = naruszenie art. 22¹ §1 pkt 6."],
     "test": [
         {"p": "Które pytanie jest zakazane od 24.12.2025?", "o": ["Jakie są Pani oczekiwania finansowe?", "Ile Pani zarabiała u poprzedniego pracodawcy?", "Czy ma Pani uprawnienia na wózek?", "Od kiedy może Pani zacząć?"], "odp": 1, "w": "Art. 22¹ §1 pkt 6 KP."},
         {"p": "Jaka jest grzywna za brak informacji o wynagrodzeniu w rekrutacji?", "o": ["Do 5 000 zł", "1 000–30 000 zł", "Do 90 000 zł", "Brak sankcji"], "odp": 1, "w": "Art. 281 KP; plus ryzyko odszkodowania za dyskryminację."},
         {"p": "Na jakiej podstawie przetwarzasz dane z art. 22¹ KP?", "o": ["Zgoda kandydata", "Obowiązek prawny / działania przed zawarciem umowy (art. 6 ust. 1 lit. c, b RODO)", "Uzasadniony interes", "Umowa powierzenia"], "odp": 1, "w": "Zgoda jest tylko dla danych dodatkowych, których nie wolno żądać."},
     ]},

    {"id": "umowa_o_prace", "tydzien": 1, "nazwa": "Umowa o pracę: rodzaje, limity 33/3, treść art. 29",
     "slowa": ["umow", "okres próbny", "okres probny", "czas określony", "czas okreslony", "nieokreślony", "33 miesi", "art. 29", "art. 25"],
     "wyjasnienie":
         "Trzy rodzaje: na okres próbny, na czas określony, na czas nieokreślony (art. 25). Próbna: maksymalnie 3 miesiące; jeśli po niej planujesz umowę na czas określony krótszą niż 6 miesięcy — próbna max 1 miesiąc, 6–12 miesięcy — max 2 miesiące (i musisz w umowie wpisać planowany okres kolejnej umowy); można przedłużyć o urlop/usprawiedliwioną nieobecność, jeśli umowa to przewiduje; ponowna próbna z tym samym pracownikiem — tylko na inny rodzaj pracy. Umowa na czas określony: łączny limit 33 miesiące i 3 umowy (art. 25¹) — czwarta umowa lub przekroczenie 33 miesięcy przekształca ją z mocy prawa w nieokreśloną; wyjątki: zastępstwo, praca dorywcza/sezonowa, kadencja, obiektywne przyczyny leżące po stronie pracodawcy (wtedy zapis w umowie + zawiadomienie PIP w 5 dni roboczych). Od 26.04.2023 wypowiedzenie umowy na czas określony wymaga uzasadnienia i konsultacji związkowej jak nieokreślonej.\n"
         "Treść (art. 29 §1): strony, adres siedziby/miejsce zamieszkania pracodawcy, rodzaj umowy, data zawarcia, rodzaj pracy, miejsce lub miejsca wykonywania pracy, wynagrodzenie ze wskazaniem składników, wymiar czasu pracy, dzień rozpoczęcia pracy; przy próbnej — czas trwania (i ewentualne przedłużenie o nieobecności, planowana kolejna umowa); przy określonej — czas trwania/termin. Umowę zawierasz na piśmie; jeśli nie — przed dopuszczeniem do pracy potwierdzasz pisemnie strony, rodzaj i warunki (art. 29 §2). Brak umowy na piśmie przed dopuszczeniem = wykroczenie.\n"
         "Praktyka: wynagrodzenie na pełny etat ≥ 4 806 zł (proporcjonalnie na część), premia uznaniowa nie może „uzupełniać” do minimalnej w sposób niepewny — od 2027 projekt UC62 ma wyłączyć dodatki z minimalnej; miejsce pracy: konkretne (zakład, obszar dla mobilnych — „terytorium RP” PIP kwestionuje); zmiana warunków: porozumienie (aneks) albo wypowiedzenie zmieniające; umowa w języku polskim (cudzoziemiec — tłumaczenie).",
     "przyklad":
         "Pracownik: umowa próbna 1.02–30.04.2024 (3 mies.), potem określona 1.05.2024–30.04.2026 (24 mies.), potem określona 1.05.2026–31.01.2027 (9 mies. → razem 33).\n"
         "Trzecia umowa kończy się 31.01.2027 — czwarta musiałaby być już nieokreślona; przedłużenie trzeciej choćby o dzień → przekształcenie. Próbna nie liczy się do 33/3.",
     "zadania": ["Dla 3 pracowników z FIRMA.md ustal, która umowa z kolei i ile miesięcy do limitu.",
                 "Napisz umowę próbną z zapisem o planowanej umowie na czas określony 8 miesięcy (ile może trwać próbna?).",
                 "Sprawdź, czy wynagrodzenie niepełnoetatowca (1/2 etatu, 2 300 zł) spełnia minimum."],
     "pytania": [["Ile może trwać okres próbny, gdy planujesz potem umowę na 8 miesięcy?", "Maksymalnie 2 miesiące (plan 6–12 mies.); zapis o planie w umowie próbnej."],
                 ["Co się dzieje po 33 miesiącach umów na czas określony?", "Od następnego dnia umowa jest umową na czas nieokreślony z mocy prawa."],
                 ["Czy umowa na zastępstwo liczy się do limitu 33/3?", "Nie — jest wyłączona (art. 25¹ §4 pkt 1)."]],
     "pulapki": ["Aneks wydłużający umowę określoną = nowa umowa do limitu 3 (art. 25¹ §2).", "Próbna na 3 miesiące, a potem określona na 5 miesięcy → próbna mogła trwać max 1 miesiąc; naruszenie."],
     "test": [
         {"p": "Maksymalny łączny czas umów na czas określony u jednego pracodawcy?", "o": ["24 miesiące", "33 miesiące i 3 umowy", "36 miesięcy", "Bez limitu"], "odp": 1, "w": "Art. 25¹ KP."},
         {"p": "Kiedy najpóźniej pracownik musi dostać umowę na piśmie?", "o": ["W ciągu 7 dni od rozpoczęcia pracy", "Przed dopuszczeniem do pracy", "Do końca miesiąca", "Po okresie próbnym"], "odp": 1, "w": "Art. 29 §2 — przed dopuszczeniem (lub pisemne potwierdzenie warunków)."},
         {"p": "Czy wypowiedzenie umowy na czas określony wymaga uzasadnienia?", "o": ["Nie", "Tak, od 26.04.2023", "Tylko powyżej 6 miesięcy", "Tylko przy konsultacji związkowej"], "odp": 1, "w": "Zrównanie z umową na czas nieokreślony."},
     ]},

    {"id": "onboarding_akta", "tydzien": 1, "nazwa": "Onboarding i akta osobowe: badania, BHP, ZUS, informacja art. 29 §3, dokumentacja A–E",
     "slowa": ["onboarding", "akta osobow", "dokumentacja pracownicz", "badania wstępne", "badania wstepne", "bhp wstępne", "informacja o warunkach", "29 §3", "część b", "czesc b"],
     "wyjasnienie":
         "Przed dopuszczeniem do pracy: wstępne badania lekarskie (skierowanie ze wskazaniem czynników szkodliwych; orzeczenie do akt A; zwolnieni: ponownie przyjmowani do tej samej pracy w 30 dni oraz osoby z aktualnym orzeczeniem od innego pracodawcy na te same warunki — poza pracami szczególnie niebezpiecznymi), umowa, szkolenie BHP wstępne (instruktaż ogólny i stanowiskowy — karta do akt B; dla administracyjno-biurowych wstępne zawsze, okresowe można pominąć przy niskim ryzyku), zapoznanie z regulaminem pracy i oceną ryzyka, informacja o monitoringu. Do 7 dni od dopuszczenia: informacja o warunkach zatrudnienia (art. 29 §3 — od 2023 rozszerzona: normy czasu pracy, przerwy, odpoczynki, nadgodziny i rekompensata, zasady zmian, składniki wynagrodzenia i świadczenia, urlop, procedura rozwiązania umowy, szkolenia, układ, ZUS), zgłoszenie ZUS ZUA (7 dni od powstania obowiązku ubezpieczenia = dzień rozpoczęcia pracy), oświadczenia: PIT-2, KUP, PPK, numer konta, dane kontaktowe. Do 3 miesięcy: umowa o prowadzenie PPK.\n"
         "Akta osobowe (rozporządzenie z 10.12.2018): A — ubieganie się o zatrudnienie (kwestionariusz kandydata, skierowanie i orzeczenie wstępne, kwalifikacje), B — nawiązanie i przebieg (umowa, kwestionariusz pracownika, informacja 29 §3, BHP, potwierdzenia zapoznania, PIT-2/PPK/RODO, aneksy, badania okresowe, uprawnienia rodzicielskie, wnioski o zmianę etatu, oświadczenia o stażu i zaświadczenie ZUS o stażu), C — ustanie (wypowiedzenie, świadectwo, dokumenty rozliczenia, wniosek o sprostowanie), D — kary porządkowe (usuwane po roku nienagannej pracy), E — kontrola trzeźwości (rok). Każda część: chronologia, numeracja, wykaz. Odrębnie: dokumentacja czasu pracy, urlopowa, lista płac/karty wynagrodzeń, odzież.\n"
         "Przechowywanie: 10 lat od końca roku ustania zatrudnienia (zatrudnieni od 1.01.2019; starsi — 50 lat, chyba że ZUS OSW + RIA). Postać papierowa lub elektroniczna (równoważne); przejście na e-akta: skan z podpisem kwalifikowanym/pieczęcią, informacja dla pracowników, 30 dni na odbiór papieru; wymogi: integralność, metadane, kopie, możliwość wydruku. Pracownik ma prawo do kopii całości lub części akt (wniosek).",
     "przyklad":
         "Nowy operator, start 1.12.2026:\n"
         "25.11 skierowanie → 27.11 orzeczenie (akta A) → 28.11 umowa (B) → 1.12 BHP wstępne (B), regulamin, PIT-2, PPK-info, RODO (B) → do 8.12 ZUA i informacja 29 §3 (B) → do 10.03.2027 umowa o prowadzenie PPK (B) → badania okresowe wg orzeczenia (B) → … → 2031 ustanie: świadectwo (C) → archiwum do 31.12.2041.",
     "zadania": ["Ułóż checklistę onboardingu z 15 pozycjami: termin, dokument, część akt, podstawa.",
                 "Posortuj 20 dokumentów do części A/B/C/D/E (lista w zadaniu tygodnia).",
                 "Policz datę końca przechowywania akt dla pracownika zwolnionego 15.03.2026."],
     "pytania": [["Gdzie trafia karta szkolenia BHP wstępnego?", "Część B akt osobowych."],
                 ["Ile masz dni na zgłoszenie pracownika do ZUS?", "7 dni od powstania obowiązku ubezpieczenia (dzień rozpoczęcia pracy)."],
                 ["Kiedy kara porządkowa znika z akt?", "Po roku nienagannej pracy (wcześniej na wniosek pracownika za zgodą pracodawcy lub związku)."]],
     "pulapki": ["Dopuszczenie do pracy przed orzeczeniem lekarskim — wykroczenie i utrata ochrony ubezpieczeniowej przy wypadku.", "Informacja 29 §3 „odsyłająca do regulaminu”, którego nie ma w firmie < 50 osób — musisz wpisać treść."],
     "test": [
         {"p": "W jakiej części akt przechowujesz oświadczenie PIT-2?", "o": ["A", "B", "C", "Poza aktami, w dokumentacji płacowej"], "odp": 1, "w": "Dokument z przebiegu zatrudnienia → B."},
         {"p": "Ile wynosi okres przechowywania akt pracownika zatrudnionego w 2020 r.?", "o": ["5 lat", "10 lat od końca roku ustania zatrudnienia", "50 lat", "3 lata"], "odp": 1, "w": "Dla stosunków pracy nawiązanych od 1.01.2019."},
         {"p": "Termin na przekazanie informacji o warunkach zatrudnienia (art. 29 §3)?", "o": ["W dniu zawarcia umowy", "7 dni od dopuszczenia do pracy", "30 dni", "Do końca okresu próbnego"], "odp": 1, "w": "Zmiana warunków — najpóźniej w dniu zmiany."},
     ]},

    # ================================================================ TYDZIEŃ 2
    {"id": "czas_pracy_systemy", "tydzien": 2, "nazwa": "Czas pracy: normy, systemy, okresy rozliczeniowe, odpoczynek",
     "slowa": ["czas pracy", "system czasu", "równoważny", "rownowazny", "okres rozliczeniowy", "wymiar czasu", "odpoczynek", "doba pracownicza", "art. 130", "harmonogram", "grafik"],
     "wyjasnienie":
         "Normy: 8 h na dobę i przeciętnie 40 h w przeciętnie 5-dniowym tygodniu w okresie rozliczeniowym do 4 miesięcy (art. 129); wydłużenie do 12 miesięcy — z obiektywnych przyczyn, w układzie/porozumieniu i z zawiadomieniem PIP. Wymiar (art. 130): tygodnie × 40 + dni pon–pt × 8 − 8 za święto w dniu innym niż niedziela (także sobotnie święto obniża wymiar). Doba pracownicza: 24 h od rozpoczęcia pracy — drugie rozpoczęcie w tej samej dobie to nadgodzina (chyba że ruchomy czas pracy z art. 140¹). Odpoczynek: 11 h dobowy (wyjątki: zarządzający, akcje ratownicze — z równoważnym odpoczynkiem), 35 h tygodniowy (24 h przy zmianie pory w zmianowym), obejmujący niedzielę (lub inny dzień w pracy dozwolonej w niedziele).\n"
         "Systemy: podstawowy (8 h), równoważny (do 12 h — a przy dozorze urządzeń/pogotowiu do 16 h, przy pilnowaniu do 24 h; okres 1 mies., wyjątkowo 3–4), zadaniowy (bez ewidencji godzin, ale wymiar zadań realny w normach), przerywany (jedna przerwa do 5 h, 60% wynagrodzenia za przerwę — tylko w układzie/porozumieniu), skrócony tydzień i weekendowy (na wniosek, do 12 h), ruchomy (przedziały rozpoczynania lub różne godziny), praca w ruchu ciągłym (do 43 h średnio), indywidualny rozkład na wniosek. System i okres ustala regulamin/układ/obwieszczenie; harmonogram (grafik) na co najmniej 1 miesiąc, przekazany 1 tydzień przed (art. 129 §3), chyba że rozkład wynika z regulaminu/umowy.\n"
         "Praca w niedziele i święta dozwolona tylko w przypadkach z art. 151¹⁰ (ruch ciągły, zmianowa, handel ograniczony, usługi…); rekompensata: dzień wolny w 6 dniach przed/po (niedziela) lub w okresie (święto), inaczej 100%; raz na 4 tygodnie wolna niedziela. Przerwy: 15 min przy ≥ 6 h, 30 min (drugie 15) przy > 9 h, 45 min przy > 16 h (od 2023) — wliczane do czasu pracy; przerwa niewliczana do 60 min (lunch) — w regulaminie. Niepełnosprawni: 7 h/35 h (umiarkowany/znaczny), dodatkowe 15 min, zakaz nocnej i nadgodzin bez zgody lekarza.",
     "przyklad":
         "Wymiar grudnia 2026: 4 pełne tygodnie (1–28.12) × 40 = 160 h; pozostałe dni pon–pt: 29, 30, 31.12 = 3 × 8 = 24 h → 184 h; święta w dniu innym niż niedziela: 24.12 (czw), 25.12 (pt), 26.12 (sb) = 3 × 8 = 24 h → wymiar 160 h, 20 dni pracy.\n"
         "Operator 12-godzinny: 160 h = 13 zmian 12 h + 1 zmiana 4 h (lub 13 zmian i 4 h „do przodu” w 3-mies. okresie).",
     "zadania": ["Policz wymiar dla każdego miesiąca 2027.",
                 "Ułóż 2-tygodniowy grafik 3-zmianowy dla 4 osób z zachowaniem 11/35 h i wolnej niedzieli.",
                 "Wskaż, który system wybrać dla kierowcy dostaw (dowóz 6 dni w tygodniu po 10 h)."],
     "pytania": [["Czym jest doba pracownicza?", "24 kolejne godziny od rozpoczęcia pracy wg rozkładu; ponowne rozpoczęcie w tej dobie = nadgodziny (poza ruchomym czasem pracy)."],
                 ["Ile wynosi minimalny odpoczynek tygodniowy i kiedy może być krótszy?", "35 h nieprzerwane (w tym 11 h dobowe); 24 h przy zmianie pory wykonywania pracy w zmianowym i dla zarządzających."],
                 ["Czy święto w sobotę obniża wymiar czasu pracy?", "Tak — o 8 h; pracodawca wyznacza inny dzień wolny."]],
     "pulapki": ["Grafik „na tydzień” przekazany w piątek → minimum 1 tydzień przed i na co najmniej miesiąc.", "W równoważnym 12 h dalej obowiązuje 11 h odpoczynku — zmiana 18–6 i potem 6–18 jest niedopuszczalna."],
     "test": [
         {"p": "Wymiar czasu pracy w sierpniu 2026 (15.08 w sobotę)?", "o": ["168 h", "160 h", "176 h", "152 h"], "odp": 1, "w": "21 dni roboczych × 8 = 168 − 8 za sobotnie święto = 160 h (20 dni)."},
         {"p": "Maksymalny dobowy wymiar w systemie równoważnym przy dozorze urządzeń?", "o": ["12 h", "16 h", "24 h", "10 h"], "odp": 1, "w": "Art. 136; 24 h przy pilnowaniu mienia/ochronie (art. 137)."},
         {"p": "Jak często pracownik pracujący w niedziele musi mieć wolną niedzielę?", "o": ["Co 2 tygodnie", "Raz na 4 tygodnie", "Raz w miesiącu kalendarzowym", "Raz na 6 tygodni"], "odp": 1, "w": "Art. 151¹² §3 (nie dotyczy weekendowego)."},
     ]},

    {"id": "nadgodziny_noc", "tydzien": 2, "nazwa": "Nadgodziny, dyżur, praca w nocy — rozliczenie",
     "slowa": ["nadgodzin", "godziny nadliczbowe", "dodatek 50", "dodatek 100", "czas wolny", "praca w nocy", "dodatek nocny", "dyżur", "dyzur", "151"],
     "wyjasnienie":
         "Nadgodziny (art. 151) tylko z konieczności akcji ratowniczej lub szczególnych potrzeb pracodawcy; limit 150 h rocznie (regulamin/umowa może podnieść — do 416 h przy zachowaniu 48 h tygodniowo średnio), zakaz dla ciężarnych, młodocianych, niepełnosprawnych (bez zgody lekarza), a opiekun dziecka do 8 lat — tylko za zgodą. Rodzaje: dobowe (przekroczenie 8 h lub przedłużonego wymiaru z grafiku w danym dniu) — rozliczane co miesiąc; średniotygodniowe (po zakończeniu okresu rozliczeniowego: przepracowane − wymiar − nadgodziny dobowe już policzone).\n"
         "Rekompensata: normalne wynagrodzenie za każdą nadgodzinę (stawka godzinowa = wynagrodzenie zasadnicze + stałe składniki / wymiar miesiąca) + dodatek: 100% za nadgodziny w nocy, w niedziele i święta niebędące dniami pracy wg rozkładu, w dniu wolnym udzielonym za niedzielę/święto, oraz za przekroczenie normy średniotygodniowej; 50% w pozostałych (dobowe w dzień roboczy). Praca w dniu wolnym z 5-dniowego tygodnia (sobota) → najpierw inny dzień wolny do końca okresu (art. 151³); jeśli nieudzielony — nadgodziny średniotygodniowe 100%. Zamiast dodatku: czas wolny 1:1 na wniosek pracownika (także w kolejnym okresie), 1:1,5 bez wniosku w tym samym okresie — bez obniżenia wynagrodzenia. Ryczałt za nadgodziny — tylko dla stale pracujących poza zakładem, odpowiadający przewidywanemu wymiarowi. Kadra zarządzająca i kierownicy komórek — bez prawa do dodatku (poza niedzielą/świętem bez dnia wolnego dla kierowników).\n"
         "Pora nocna: 8 h między 21:00 a 7:00 (regulamin); dodatek 20% stawki godzinowej z minimalnego wynagrodzenia (4 806 / wymiar miesiąca) za każdą godzinę; pracujący w nocy (≥ 3 h nocnych na dobę lub ≥ 1/4 czasu w okresie) — max 8 h przy pracach niebezpiecznych. Dyżur (art. 151⁵): poza godzinami, w zakładzie lub domu; czas dyżuru w zakładzie bez pracy — czas wolny lub wynagrodzenie (nie dla domowego); nie może naruszać odpoczynków.",
     "przyklad":
         "Biuro, 6 000 zł, czerwiec 2026 (wymiar 168 h), stawka 35,71 zł/h.\n"
         "Wtorek 8 → 12 h: 4 nadgodziny dobowe: 4 × 35,71 = 142,84 normalne + 4 × 50% × 35,71 = 71,42 dodatek.\n"
         "Sobota 8 h (nie udzielono wolnego do końca czerwca): 8 × 35,71 = 285,68 normalne + 8 × 100% × 35,71 = 285,68.\n"
         "Razem za nadgodziny: 785,62 zł. Wariant: pracownik wnioskuje o czas wolny 12 h → wypłacasz tylko „normalne”? Nie — przy czasie wolnym 1:1 nie wypłacasz dodatku, a godziny wolne pomniejszają czas pracy bez obniżki pensji.",
     "zadania": ["Policz nadgodziny 3 przypadków z zadania tygodnia 2 (stawka z wymiaru miesiąca).",
                 "Policz dodatek nocny dla 64 h w listopadzie 2026.",
                 "Rozlicz pracę w sobotę, gdy dzień wolny udzielono w następnym miesiącu tego samego okresu."],
     "pytania": [["Jaki dodatek za nadgodziny dobowe w dzień roboczy w ciągu dnia?", "50%; w nocy/niedzielę/święto — 100%."],
                 ["Kiedy nadgodziny rozliczasz jako średniotygodniowe?", "Po zakończeniu okresu rozliczeniowego, od przekroczenia wymiaru pomniejszonego o już rozliczone dobowe."],
                 ["Ile wynosi dodatek nocny w listopadzie 2026?", "20% × (4 806 / 160) = 6,01 zł/h."]],
     "pulapki": ["Dzielnik stawki = wymiar DANEGO miesiąca (nie 168 zawsze).", "Czas wolny 1:1,5 z inicjatywy pracodawcy musi być w tym samym okresie rozliczeniowym."],
     "test": [
         {"p": "Pracownik przepracował 10 h w sobotę (dzień wolny z 5-dniowego tygodnia). Co najpierw?", "o": ["Dodatek 100% za 10 h", "Inny dzień wolny do końca okresu rozliczeniowego", "Dodatek 50%", "Nic — sobota jest wolna"], "odp": 1, "w": "Art. 151³; dodatek dopiero gdy wolnego nie udzielono (2 h ponad 8 — dobowe 50%)."},
         {"p": "Czas wolny za nadgodziny bez wniosku pracownika udziela się w proporcji:", "o": ["1:1", "1:1,5", "1:2", "Nie można bez wniosku"], "odp": 1, "w": "Art. 151² §2; w tym samym okresie rozliczeniowym."},
         {"p": "Roczny limit nadgodzin bez zmiany w regulaminie?", "o": ["100 h", "150 h", "260 h", "416 h"], "odp": 1, "w": "Art. 151 §3; regulamin może podnieść do 416 h."},
     ]},

    {"id": "ewidencja_czasu", "tydzien": 2, "nazwa": "Ewidencja czasu pracy i nieobecności",
     "slowa": ["ewidencj", "karta ewidencji", "lista obecności", "lista obecnosci", "nieobecno", "§6", "wyjścia prywatne", "wyjscia prywatne"],
     "wyjasnienie":
         "Ewidencja czasu pracy (art. 149, §6 rozporządzenia o dokumentacji) prowadzona dla każdego pracownika odrębnie, w postaci papierowej lub elektronicznej, zawiera: liczbę przepracowanych godzin z godziną rozpoczęcia i zakończenia, w tym nadgodziny, w porze nocnej, w niedziele i święta (z tytułem), dyżury (miejsce, godziny), dni wolne z oznaczeniem tytułu (W5, WN, WŚ, wolne za nadgodziny), rodzaj i wymiar zwolnień od pracy i innych usprawiedliwionych nieobecności, nieusprawiedliwione, czas pracy młodocianego przy pracach wzbronionych. Towarzyszą jej: wnioski o wyjścia prywatne, wnioski/polecenia nadgodzin, zgody opiekunów dzieci do 8 lat i ciężarnych na delegację, wnioski o czas wolny, harmonogramy, rozkłady ruchome. Dla zadaniowego czasu pracy i kierowników komórek nie ewidencjonujesz godzin (tylko nieobecności i dni wolne).\n"
         "Lista obecności to narzędzie dyscypliny, nie ewidencja; nie jest obowiązkowa. Ewidencja musi pozwolić policzyć wynagrodzenie — to pierwszy dokument, o który prosi PIP i którego brak daje domniemanie na korzyść pracownika w sądzie (sprawy o nadgodziny). Przechowywanie: jak akta — 10 lat po ustaniu zatrudnienia (dokumentacja z 2019+). Pracownik ma prawo wglądu i kopii.\n"
         "Nieobecności i kody w praktyce: urlop wypoczynkowy (UW), na żądanie (UŻ), opiekuńczy art. 173¹ (UO, 5 dni, bezpłatny), siła wyższa art. 148¹ (SW, 2 dni/16 h, 50%), art. 188 (opieka nad dzieckiem do 14 lat, 2 dni/16 h, 100%), choroba (CH), opieka zasiłkowa (OP), bezpłatny (UB), okolicznościowy (UOk), delegacja (D), nieobecność nieusprawiedliwiona (NN). Każdy rodzaj inaczej wpływa na wynagrodzenie (tydzień 5) i składki (RSA, tydzień 8). Wyjście prywatne odpracowane nie jest nadgodziną (art. 151 §2¹) — ale odpracowanie nie może naruszać odpoczynku. Praca zdalna: ewidencja nadal, okazjonalna (24 dni) — osobno.",
     "przyklad":
         "Karta — grudzień 2026, operator (fragment):\n"
         "01.12 | 06:00–18:00 | 12 h | nocne 0 | W: — | zmiana wg grafiku\n"
         "02.12 | — | 0 | W5 (wolne z 5-dn. tygodnia)\n"
         "03.12 | 18:00–06:00 | 12 h | nocne 8 h (22–6)\n"
         "05.12 | — | UW 12 h (urlop = godziny z planu)\n"
         "08–09.12 | — | CH (e-ZLA)\n"
         "12.12 | 06:00–20:00 | 14 h | nadgodziny dobowe 2 h (polecenie nr 7/12)",
     "zadania": ["Zbuduj kartę ewidencji w arkuszu z kolumnami §6 i wypełnij miesiąc z grafiku.",
                 "Wypisz 10 kodów nieobecności z wpływem na wynagrodzenie (100/50/0/zasiłek).",
                 "Opisz, co grozi pracodawcy bez ewidencji w sporze o nadgodziny."],
     "pytania": [["Czy lista obecności zastępuje ewidencję czasu pracy?", "Nie — ewidencja musi zawierać godziny, nadgodziny, nocne, dyżury, nieobecności; lista obecności to tylko potwierdzenie przybycia."],
                 ["Dla kogo nie ewidencjonujesz godzin pracy?", "Zadaniowy czas pracy, kierownicy wyodrębnionych komórek, ryczałt za nadgodziny/nocne — ale nieobecności i dni wolne tak."],
                 ["Czy odpracowanie wyjścia prywatnego jest nadgodziną?", "Nie (art. 151 §2¹), jeśli na pisemny wniosek pracownika i bez naruszenia odpoczynku."]],
     "pulapki": ["Ewidencja w programie bez godzin rozpoczęcia/zakończenia (tylko „8 h”) — niezgodna z §6 od 2019.", "Urlop w równoważnym ewidencjonujesz w godzinach z planu (12 h), nie 8 h."],
     "test": [
         {"p": "Które dane są obowiązkowe w ewidencji od 2019 r.?", "o": ["Tylko liczba godzin dziennie", "Godzina rozpoczęcia i zakończenia pracy, nadgodziny, nocne, dyżury, nieobecności", "Tylko nieobecności", "Tylko nadgodziny"], "odp": 1, "w": "§6 rozporządzenia o dokumentacji pracowniczej."},
         {"p": "Jak długo przechowujesz ewidencję czasu pracy?", "o": ["3 lata", "Jak akta osobowe — 10 lat po ustaniu zatrudnienia", "1 rok", "5 lat"], "odp": 1, "w": "Dokumentacja pracownicza = akta + dokumentacja w sprawach ze stosunku pracy."},
         {"p": "Pracownik na zadaniowym czasie pracy — co ewidencjonujesz?", "o": ["Nic", "Pełne godziny", "Nieobecności i dni wolne", "Tylko nadgodziny"], "odp": 2, "w": "Art. 149 §2 KP."},
     ]},

    # ================================================================ TYDZIEŃ 3
    {"id": "urlop_wypoczynkowy", "tydzien": 3, "nazwa": "Urlop wypoczynkowy w praktyce: wymiar, proporcja, na żądanie, zaległy",
     "slowa": ["urlop wypoczynkow", "wymiar urlopu", "20 dni", "26 dni", "na żądanie", "na zadanie", "proporcjonal", "zaległy", "zalegly", "plan urlop", "pierwsz"],
     "wyjasnienie":
         "Wymiar: 20 dni (staż < 10 lat) lub 26 dni (≥ 10 lat) — art. 154; do stażu wlicza się okresy zatrudnienia (u wszystkich pracodawców) i nauki (ZSZ 3, średnia zawodowa 5, średnia ogólnokształcąca 4, policealna 6, wyższe 8 lat — bez sumowania, korzystniejszy; nauka równoległa z pracą — korzystniejsze), a od 2026 także zlecenia/działalność (lekcja o stażu). Urlop udzielany w dni robocze pracownika, w godzinach: 1 dzień = 8 h (7 h dla umiarkowanej/znacznej niepełnosprawności; godzinowo liczysz tylko część dnia, gdy pozostała część urlopu jest mniejsza niż dobowy wymiar). Niepełny etat: wymiar proporcjonalny, zaokrąglany w górę do pełnego dnia (1/2 × 26 = 13; 3/4 × 20 = 15).\n"
         "Pierwsza praca w życiu (art. 153): z dołu, 1/12 wymiaru za każdy przepracowany miesiąc, bez zaokrąglania w górę; od następnego roku kalendarzowego — z góry, cały wymiar 1 stycznia. Proporcjonalny (art. 155¹): przy zmianie pracodawcy w roku — u dotychczasowego za okres do ustania (po zaokrągleniu miesięcy — niepełny miesiąc u pierwszego pracodawcy liczy się za pełny), u nowego za resztę; przy powrocie po urlopie bezpłatnym > 1 miesiąc, wychowawczym, służbie — proporcja. Zaokrąglenia dni w górę. Urlop na żądanie: 4 dni w roku (w puli 20/26), zgłoszenie najpóźniej w dniu, przed rozpoczęciem pracy; odmowa tylko wyjątkowo (interes pracodawcy — SN); niewykorzystany na żądanie przechodzi na rok następny jako zwykły zaległy.\n"
         "Zasady udzielania: plan urlopów (lub uzgodnienie indywidualne, gdy brak związków i uzgodniono), co najmniej jedna część 14 kolejnych dni kalendarzowych (art. 162), zaległy do 30 września następnego roku (urlop zaległy w okresie wypowiedzenia można narzucić — art. 167¹; poza tym SN dopuszcza polecenie wykorzystania zaległego po 30.09), przesunięcie i odwołanie z urlopu (art. 164–167: zwrot kosztów), przerwanie przez chorobę, ekwiwalent tylko przy ustaniu zatrudnienia (art. 171). Przedawnienie roszczeń: 3 lata od końca roku, w którym stał się wymagalny (od 1.10 następnego roku).",
     "przyklad":
         "Pracownica, 1/2 etatu, staż 11 lat (wliczone 3 lata zlecenia), zatrudniona 15.03.2026 (wcześniej pracowała w 2026 u innego pracodawcy do 28.02):\n"
         "wymiar roczny: 26 × 1/2 = 13 dni; proporcja u Ciebie: 10/12 (marzec–grudzień; marzec liczy się cały, bo poprzedni pracodawca rozliczył do lutego) × 13 = 10,83 → 11 dni = 88 h.\n"
         "Zaległy u Ciebie: brak. Na żądanie: 4 dni w puli 11.",
     "zadania": ["Policz urlop dla 8 pracowników z FIRMA.md (zadanie tygodnia).",
                 "Rozpisz urlop 3/4 etatu w godzinach i ustal, ile dni „na żądanie”.",
                 "Wskaż termin przedawnienia urlopu za 2024 r."],
     "pytania": [["Kiedy pracownik w pierwszej pracy nabywa prawo do urlopu?", "Z upływem każdego miesiąca pracy, 1/12 wymiaru (z dołu), w pierwszym roku kalendarzowym."],
                 ["Jak liczysz urlop niepełnoetatowca?", "Wymiar × część etatu, zaokrąglenie w górę do pełnego dnia; dzień = 8 h."],
                 ["Do kiedy należy udzielić urlopu zaległego?", "Do 30 września następnego roku (PIP karze za brak; roszczenie przedawnia się po 3 latach)."]],
     "pulapki": ["Zaokrąglanie 1/12 w górę przy pierwszej pracy — niedozwolone (tylko proporcjonalny).", "Urlop na żądanie „4 dni dodatkowe” — nie, z puli 20/26."],
     "test": [
         {"p": "Pracownik ze stażem 9 lat i 10 miesięcy nabywa 26 dni:", "o": ["Od 1 stycznia następnego roku", "Z dniem uzyskania 10 lat stażu — urlop uzupełniający w tym roku", "Nigdy w tym roku", "Po 12 miesiącach u obecnego pracodawcy"], "odp": 1, "w": "Art. 158 — urlop uzupełniający (6 dni) od dnia nabycia."},
         {"p": "Ile dni urlopu ma pracownik na 3/4 etatu ze stażem 4 lat?", "o": ["15", "14", "20", "13"], "odp": 0, "w": "3/4 × 20 = 15 (bez zaokrąglania, bo równe)."},
         {"p": "Pracownik zachorował w 3. dniu 10-dniowego urlopu. Co z urlopem?", "o": ["Przepada", "Choroba przerywa urlop; niewykorzystane dni udziela się później", "Pracownik decyduje", "Zamienia się w ekwiwalent"], "odp": 1, "w": "Art. 166 KP."},
     ]},

    {"id": "staz_pracy_2026", "tydzien": 3, "nazwa": "Staż pracy 2026: zlecenia i działalność w stażu, zaświadczenie ZUS",
     "slowa": ["staż pracy", "staz pracy", "zaświadczenie zus", "zaswiadczenie zus", "1 maja 2026", "302", "zlecenie do stażu", "dodatek stażowy", "staz z dzialalnosci"],
     "wyjasnienie":
         "Nowelizacja KP (art. 302¹ i n.): do stażu pracy, od którego zależą uprawnienia pracownicze (wymiar urlopu, okres wypowiedzenia u tego samego pracodawcy, odprawy, dodatki stażowe i nagrody jubileuszowe wg regulaminów), wlicza się okresy: umów zlecenia i o świadczenie usług objętych ubezpieczeniem emerytalno-rentowym (a dla studentów do 26 lat bez ubezpieczenia — na podstawie umowy), umów agencyjnych, pozarolniczej działalności gospodarczej z opłaconymi składkami (także ulga na start; zawieszenie — tylko na opiekę nad dzieckiem), współpracy z przedsiębiorcą, pobierania zasiłków z tych tytułów, członkostwa w spółdzielniach rolniczych, pracy za granicą w innych formach niż umowa o pracę. Nie wlicza się: umów o dzieło, praktyk, wolontariatu, działalności nierejestrowanej, zawieszenia (poza opieką). Okresy nakładające się liczysz raz (korzystniejszy). Wejście w życie: 1.01.2026 — sektor finansów publicznych, 1.05.2026 — pozostali pracodawcy.\n"
         "Dokumentowanie: zaświadczenie ZUS o okresach ubezpieczenia — wniosek elektroniczny przez eZUS (bez załączników), może obejmować wszystkie tytuły lub wybrany; gdy ZUS nie ma danych — decyzja odmowna i postępowanie wyjaśniające z dowodami (umowy, faktury, zaświadczenia); zleceniodawca nie ma obowiązku wystawiać potwierdzeń (może). Dokumenty zagraniczne z tłumaczeniem. Pracownicy już zatrudnieni mają 24 miesiące (od 1.01 lub 1.05.2026) na dostarczenie dokumentów; uprawnienia od dnia nabycia (np. urlop uzupełniający od dnia przedstawienia zaświadczenia — jeśli wymiar rośnie z 20 na 26, przysługuje różnica w roku bieżącym), nie wcześniej niż od wejścia w życie. Spory — sąd pracy.\n"
         "Dla kadr: komunikat do pracowników, wzór wniosku, miejsce w aktach (B), aktualizacja w programie (staż ogólny vs zakładowy), przeliczenie urlopu i — jeśli regulamin przewiduje — dodatków stażowych; okres wypowiedzenia wydłuża tylko zlecenie u TEGO pracodawcy; limity umów na czas określony — nie zmieniają się (dotyczą tylko umów o pracę).",
     "przyklad":
         "Pracownik zatrudniony u Ciebie od 2022 (umowa o pracę), wcześniej: 2016–2019 zlecenie w innej firmie (ubezpieczony), 2019–2021 działalność (składki opłacone), 2020–2021 równolegle dzieło.\n"
         "Staż przed nowelizacją: 4 lata (2022–2026) → 20 dni. Po: + 3 (zlecenie) + 2 (działalność; dzieło nie liczy się, a 2020–2021 i tak nakłada się na działalność) = 9 lat → nadal 20 dni; po 1 roku → 26. Zaświadczenie ZUS dostarczone 10.06.2026 — przelicz staż; okres wypowiedzenia u Ciebie bez zmian (staż zakładowy od 2022).",
     "zadania": ["Napisz komunikat do pracowników o nowych zasadach stażu z terminem 24 miesięcy.",
                 "Przelicz staż i urlop dla 2 pracowników z FIRMA.md po dostarczeniu zaświadczeń.",
                 "Ustal, które okresy z listy (dzieło, wolontariat, zlecenie studenta, ulga na start) wliczasz."],
     "pytania": [["Od kiedy prywatny pracodawca wlicza zlecenia do stażu?", "Od 1 maja 2026 r. (publiczny — od 1 stycznia 2026)."],
                 ["Czy zlecenie u innego podmiotu wydłuża okres wypowiedzenia u Ciebie?", "Nie — okres wypowiedzenia zależy od stażu u danego pracodawcy; tylko zlecenia u Ciebie."],
                 ["Jak pracownik dokumentuje okres zlecenia?", "Zaświadczeniem ZUS (eZUS), a gdy ZUS nie ma danych — dowodami w postępowaniu wyjaśniającym; student bez ubezpieczenia — umową."]],
     "pulapki": ["Umowa o dzieło „bo była długa” — nie wlicza się nigdy.", "Dwa równoległe okresy (etat + zlecenie) liczone podwójnie — tylko jeden."],
     "test": [
         {"p": "Który okres NIE wlicza się do stażu pracy po nowelizacji 2026?", "o": ["Zlecenie z ubezpieczeniem emerytalno-rentowym", "Działalność gospodarcza ze składkami", "Umowa o dzieło", "Współpraca z przedsiębiorcą"], "odp": 2, "w": "Dzieło nie jest tytułem do ubezpieczeń."},
         {"p": "Ile czasu mają obecni pracownicy prywatnej firmy na dostarczenie dokumentów o stażu?", "o": ["Do 31.12.2026", "24 miesiące od 1.05.2026", "12 miesięcy", "Bez limitu"], "odp": 1, "w": "Po terminie okresy nie zostaną wliczone (poza sporem sądowym)."},
         {"p": "Jak składa się wniosek o zaświadczenie ZUS o stażu?", "o": ["Papierowo w oddziale", "Wyłącznie elektronicznie przez eZUS", "Przez pracodawcę", "Telefonicznie"], "odp": 1, "w": "Bez załączników; ZUS wydaje z własnych danych."},
     ]},

    {"id": "urlopy_rodzicielskie", "tydzien": 3, "nazwa": "Urlopy rodzicielskie 2026: macierzyński, rodzicielski, ojcowski, wychowawczy, ochrona",
     "slowa": ["macierzyńsk", "macierzynsk", "rodzicielsk", "ojcowsk", "wychowawcz", "ciąż", "ciaz", "41 tygodni", "9 tygodni", "wcześniak", "wczesniak", "81,5"],
     "wyjasnienie":
         "Macierzyński: 20 tygodni (1 dziecko; 31/33/35/37 przy porodzie mnogim), do 6 tygodni przed porodem, obowiązkowe 14 tygodni dla matki — resztę może przejąć ojciec; zasiłek 100%. Wcześniaki i hospitalizacja noworodka (od 19.03.2025): dodatkowy urlop macierzyński — tydzień za każdy tydzień pobytu dziecka w szpitalu, do 8 lub 15 tygodni (zależnie od tygodnia ciąży/masy), 100%. Rodzicielski (art. 182¹ᵃ): 41 tygodni (43 przy mnogim) łącznie dla obojga, w tym 9 tygodni wyłącznie dla każdego z rodziców (nieprzenoszalne — przepadają); do końca roku kalendarzowego, w którym dziecko kończy 6 lat; do 5 części; można łączyć z pracą do 1/2 etatu (urlop wydłuża się proporcjonalnie, max 82 tygodnie); zasiłek 70%, a jeśli matka złoży wniosek o cały rodzicielski (bez 9 tygodni ojca) w 21 dni po porodzie — 81,5% za macierzyński i rodzicielski; 9 tygodni ojca zawsze 70%. Rodzice dziecka z zaświadczeniem „Za życiem” — 65/67 tygodni.\n"
         "Ojcowski: 2 tygodnie do ukończenia przez dziecko 12 miesięcy (max 2 części po tygodniu), wniosek 7 dni wcześniej, 100%. Wychowawczy (art. 186): do 36 miesięcy (jeden rodzic max 35, 1 miesiąc dla drugiego), do końca roku, w którym dziecko kończy 6 lat (18 — niepełnosprawne), staż ≥ 6 miesięcy, bezpłatny, do 5 części, wniosek 21 dni wcześniej (elektronicznie), składki emerytalno-rentowe i zdrowotna z budżetu (ZUS RCA kod 12 11, RSA 121), wlicza się do stażu; zamiast wychowawczego — obniżenie etatu do max 1/2 na do 12 miesięcy z ochroną. Elastyczna organizacja pracy dla rodzica dziecka do 8 lat (art. 188¹) — wniosek 21 dni, odpowiedź 7 dni.\n"
         "Ochrona: od zgłoszenia ciąży i przez urlopy macierzyński/rodzicielski/ojcowski — zakaz wypowiedzenia i rozwiązania (poza upadłością/likwidacją i art. 52 za zgodą związku); umowa na czas określony/próbny > 1 mies., która rozwiązałaby się po 3. miesiącu ciąży — przedłuża się do porodu (nie zastępstwo); od złożenia wniosku o urlop — ochrona od 14 dni przed terminem (ojcowski/rodzicielski). Ciąża: zakaz nocnej, nadgodzin, delegacji bez zgody; zmiana warunków pracy przy pracach wzbronionych z zachowaniem wynagrodzenia. Dokumenty: wnioski w postaci papierowej lub elektronicznej (od 2023), oświadczenia o korzystaniu przez drugiego rodzica, akt urodzenia — do akt B.",
     "przyklad":
         "Poród 15.09.2026, matka zaczyna macierzyński w dniu porodu:\n"
         "macierzyński 20 tyg.: 15.09.2026–1.02.2027 (100%).\n"
         "Wniosek w 21 dni (do 6.10) o rodzicielski 32 tyg. (41 − 9 ojca): 2.02–13.09.2027 — razem 81,5% od 15.09.2026.\n"
         "Ojciec: ojcowski 2 tyg. do 14.09.2027 (100%); 9 tyg. rodzicielskiego (70%) np. 14.09–15.11.2027 lub później, do końca 2032.",
     "zadania": ["Ułóż kalendarz dla obojga rodziców (zadanie tygodnia).",
                 "Policz zasiłek macierzyński 81,5% vs 100%/70% dla podstawy 5 177,40 zł.",
                 "Napisz odpowiedź odmowną na wniosek o elastyczną organizację pracy (z uzasadnieniem)."],
     "pytania": [["Ile tygodni rodzicielskiego jest nieprzenoszalnych i dla kogo?", "9 tygodni dla każdego z rodziców; niewykorzystane przepadają."],
                 ["Warunek zasiłku 81,5% za cały okres?", "Wniosek matki o pełny rodzicielski (bez części ojca) w 21 dni po porodzie."],
                 ["Do kiedy ojciec może wykorzystać urlop ojcowski?", "Do ukończenia przez dziecko 12. miesiąca życia."]],
     "pulapki": ["Umowa na zastępstwo w ciąży nie przedłuża się do porodu.", "Wniosek o rodzicielski po 21 dniach → 100% + 70%, bez wyrównania."],
     "test": [
         {"p": "Łączny wymiar urlopu rodzicielskiego dla obojga rodziców (1 dziecko)?", "o": ["32 tygodnie", "41 tygodni", "43 tygodnie", "52 tygodnie"], "odp": 1, "w": "W tym po 9 tygodni nieprzenoszalnych."},
         {"p": "Umowa na czas określony pracownicy w 5. miesiącu ciąży kończy się 30.11. Co robisz?", "o": ["Umowa wygasa 30.11", "Umowa przedłuża się do dnia porodu z mocy prawa", "Podpisujesz nową umowę", "Przedłużasz do końca urlopu macierzyńskiego"], "odp": 1, "w": "Art. 177 §3 KP (poza zastępstwem i próbną ≤ 1 mies.)."},
         {"p": "Kto finansuje składki emerytalno-rentowe na urlopie wychowawczym?", "o": ["Pracodawca", "Pracownik", "Budżet państwa (płatnik tylko wykazuje w RCA)", "Nikt — brak składek"], "odp": 2, "w": "Kod 12 11; podstawa 60% prognozowanego przeciętnego wynagrodzenia."},
     ]},

    {"id": "nieobecnosci_inne", "tydzien": 3, "nazwa": "Inne nieobecności i elastyczna organizacja pracy",
     "slowa": ["urlop opiekuńczy", "urlop opiekunczy", "siła wyższa", "sila wyzsza", "art. 188", "okolicznościow", "okolicznosciow", "bezpłatn", "bezplatn", "188¹", "elastyczn"],
     "wyjasnienie":
         "Z dyrektywy work-life balance (26.04.2023): urlop opiekuńczy (art. 173¹) — 5 dni w roku na opiekę lub wsparcie członka rodziny (dziecko, rodzic, małżonek) lub domownika z poważnych względów medycznych, bezpłatny (wlicza się do stażu), wniosek najpóźniej 1 dzień przed; zwolnienie z powodu siły wyższej (art. 148¹) — 2 dni lub 16 h w roku w pilnych sprawach rodzinnych (choroba, wypadek), z 50% wynagrodzenia (liczonego jak urlopowe), wniosek najpóźniej w dniu, forma dowolna (pierwszy wniosek w roku decyduje: dni czy godziny; niepełny etat — proporcjonalnie). Art. 188: rodzic dziecka do 14 lat — 2 dni lub 16 h w roku, 100%, dla jednego z rodziców (oświadczenie).\n"
         "Zwolnienia okolicznościowe (rozporządzenie o usprawiedliwianiu nieobecności): 2 dni — ślub pracownika, urodzenie dziecka, zgon i pogrzeb małżonka, dziecka, ojca, matki, ojczyma, macochy; 1 dzień — ślub dziecka, zgon i pogrzeb siostry, brata, teściowej, teścia, babki, dziadka, innej osoby na utrzymaniu — wynagrodzenie jak urlopowe. Inne: krwiodawstwo (dzień oddania), wezwanie do sądu/urzędu/wojska (bez wynagrodzenia od pracodawcy — zaświadczenie dla organu, który rekompensuje), badania ciężarnej (100%), poszukiwanie pracy w wypowiedzeniu przez pracodawcę (2 dni przy 2 tyg./1 mies., 3 dni przy 3 mies. — 100%), urlop szkoleniowy (6 dni na egzaminy; 21 dni na pracę dyplomową — 100%, gdy pracodawca kieruje lub zgadza się), zwolnienie na szukanie pracy, udział w szkoleniach BHP (czas pracy).\n"
         "Urlop bezpłatny (art. 174): na pisemny (od 2026 także elektroniczny) wniosek pracownika; nie wlicza się do stażu (poza urlopem na pracę u innego pracodawcy za zgodą — art. 174¹); > 3 miesiące — strony mogą przewidzieć odwołanie; w czasie bezpłatnego brak składek i zasiłków (RSA 111); urlop wypoczynkowy proporcjonalnie obniżany po powrocie, gdy bezpłatny trwał ≥ 1 miesiąc. Elastyczna organizacja (art. 188¹): rodzic dziecka do 8 lat wnioskuje (21 dni) o zdalną, przerywany, skrócony tydzień, weekendowy, ruchomy, indywidualny rozkład lub obniżenie etatu; pracodawca odpowiada w 7 dni, odmowa z uzasadnieniem (organizacja/rodzaj pracy); powrót na wniosek. Niestawienie się bez usprawiedliwienia: kara porządkowa, przy nieobecności trwającej — rozważ art. 52 (porzucenie pracy nie istnieje jako tryb — rozwiązujesz z art. 52 §1 pkt 1).",
     "przyklad":
         "Pracownik 6 000 zł, listopad 2026 (wymiar 160 h): siła wyższa 8 h (dziecko w szpitalu), art. 188 — 8 h, urlop opiekuńczy 16 h (matka po operacji).\n"
         "Siła wyższa: 50% × (6 000/160 × 8) = 150 zł zamiast 300 → potrącenie 150.\n"
         "Art. 188: 100% — bez zmian.\n"
         "Opiekuńczy: bezpłatny → 6 000/160 × 16 = 600 zł potrącenia.\n"
         "Wynagrodzenie: 6 000 − 150 − 600 = 5 250 zł (składki i PIT od 5 250).",
     "zadania": ["Zbuduj tabelę 12 nieobecności (zadanie tygodnia).",
                 "Rozlicz miesiąc z trzema krótkimi nieobecnościami (przykład powyżej z innymi liczbami).",
                 "Napisz wzór odpowiedzi na wniosek o elastyczną organizację pracy."],
     "pytania": [["Ile wynosi wynagrodzenie za zwolnienie z powodu siły wyższej?", "50% wynagrodzenia liczonego jak urlopowe (art. 148¹ §4)."],
                 ["Czy urlop opiekuńczy (5 dni) jest płatny?", "Nie — bezpłatny, ale wlicza się do stażu i nie obniża urlopu wypoczynkowego."],
                 ["Ile dni zwolnienia na ślub dziecka?", "1 dzień (ślub własny — 2)."]],
     "pulapki": ["Urlop opiekuńczy mylony z art. 188 (opieka nad zdrowym dzieckiem do 14 lat — płatny).", "Pracownik wybrał „godziny” przy pierwszym wniosku o siłę wyższą — w tym roku nie może już brać dni."],
     "test": [
         {"p": "Wymiar urlopu opiekuńczego (art. 173¹) w roku?", "o": ["2 dni", "5 dni", "10 dni", "14 dni"], "odp": 1, "w": "Bezpłatny; na członka rodziny/domownika."},
         {"p": "Pracownik wnioskuje o zwolnienie z powodu siły wyższej w dniu zdarzenia. Co robisz?", "o": ["Odmawiasz — za późno", "Udzielasz — wniosek może być najpóźniej w dniu korzystania", "Zamieniasz na urlop na żądanie", "Wymagasz zaświadczenia lekarskiego"], "odp": 1, "w": "Art. 148¹ §3; pracodawca jest obowiązany udzielić."},
         {"p": "W jakim terminie pracodawca odpowiada na wniosek o elastyczną organizację pracy?", "o": ["3 dni", "7 dni", "14 dni", "21 dni"], "odp": 1, "w": "Art. 188¹ §5; odmowa z uzasadnieniem."},
     ]},

    # ================================================================ TYDZIEŃ 4
    {"id": "lista_plac_krok", "tydzien": 4, "nazwa": "Lista płac krok po kroku: od brutto do netto",
     "slowa": ["lista płac", "lista plac", "netto", "brutto", "13,71", "składka zdrowotna", "skladka zdrowotna", "podstawa opodatkowania", "zaokrągl", "zaokragl"],
     "wyjasnienie":
         "Kolejność obliczeń dla pracownika: (1) przychód brutto = wszystkie składniki wypłacone w miesiącu (zasadnicze, nadgodziny, nocne, premie, świadczenia w naturze, wpłata pracodawcy na PPK jako przychód); (2) podstawa składek społecznych = przychód bez wyłączeń z rozporządzenia składkowego (odprawy, nagrody jubileuszowe co 5 lat, ekwiwalenty za pranie, diety do limitu, ZFŚS z kryterium, PPK pracodawcy — bez składek); składki pracownika: emerytalna 9,76%, rentowa 1,5%, chorobowa 2,45% — każda zaokrąglona do grosza; limit 30-krotności dla emerytalnej i rentowej; (3) podstawa zdrowotnej = podstawa społecznych − składki społeczne pracownika (+ wynagrodzenie chorobowe, które nie ma społecznych, ale ma zdrowotną); zdrowotna 9%, nie wyższa niż hipotetyczna zaliczka wg zasad z 2021 (ograniczenie — ważne przy niskich przychodach i uldze dla młodych); (4) podstawa opodatkowania = przychód − składki społeczne pracownika − KUP (250/300) + PPK pracodawcy (już w przychodzie) − przychody zwolnione (ulga dla młodych, ZFŚS do 1 000…), zaokrąglona do pełnych złotych; (5) zaliczka = 12% (lub 32% po przekroczeniu 120 000 zł dochodu narastająco) − kwota zmniejszająca (300/150/100 wg PIT-2) → zaokrąglenie do pełnych złotych; (6) PPK pracownika 2% (0,5–2%) od podstawy składek — z netto; (7) potrącenia (komornik, dobrowolne); (8) netto = brutto − społeczne − zdrowotna − zaliczka − PPK pracownika − potrącenia.\n"
         "Zaokrąglenia: składki do 1 grosza (matematycznie), podstawa opodatkowania i zaliczka do pełnego złotego (do 49 gr w dół, od 50 gr w górę), zdrowotna do grosza. Wynagrodzenie chorobowe: podstawa zdrowotnej i PIT, bez społecznych; zasiłki: tylko PIT (zaliczka 12% bez KUP, z kwotą zmniejszającą jeśli PIT-2). Świadczenie w naturze (auto): dodajesz do podstaw, nie wypłacasz.\n"
         "Kontrola listy: bilans (brutto = netto + wszystkie obciążenia pracownika), porównanie z poprzednim miesiącem (odchylenia > 10% wyjaśnij), zgodność z ewidencją czasu pracy, sprawdzenie progów narastająco (120 000 dochodu, 85 528 ulga dla młodych, 282 600 składki), zgodność oświadczeń z kartoteką. Termin wypłaty: stały, z dołu, do 10. dnia następnego miesiąca (art. 85); jeśli dzień wolny — poprzedni dzień roboczy; co najmniej raz w miesiącu; przelew na konto (gotówka tylko na wniosek).",
     "przyklad":
         "Brutto 7 200 zł (6 000 zasadnicze + 800 nadgodziny + 400 premia), KUP 250, PIT-2, PPK 2%/1,5%:\n"
         "społeczne: 702,72 + 108,00 + 176,40 = 987,12 → podst. zdrow. 6 212,88 → zdrowotna 559,16\n"
         "PPK pracodawcy 108,00 (przychód) → podstawa PIT = 7 200 + 108 − 987,12 − 250 = 6 070,88 → 6 071 → 12% = 728,52 − 300 = 428,52 → 429\n"
         "PPK pracownika 144,00 → netto = 7 200 − 987,12 − 559,16 − 429 − 144 = 5 080,72 zł",
     "zadania": ["Policz ręcznie 4 806 zł w 4 wariantach (zadanie tygodnia 4, zad. 1).",
                 "Zbuduj arkusz 8 pracowników z formułami zaokrągleń.",
                 "Sprawdź, co się dzieje ze zdrowotną pracownika 1/2 etatu 2 500 zł bez PIT-2."],
     "pytania": [["Od jakiej podstawy liczysz składkę zdrowotną?", "Od podstawy składek społecznych pomniejszonej o składki społeczne pracownika (13,71%)."],
                 ["Czy wpłata pracodawcy na PPK obniża netto?", "Pośrednio — jest przychodem do PIT (zaliczka rośnie), ale nie potrąca się jej z wynagrodzenia."],
                 ["Do czego zaokrąglasz podstawę opodatkowania?", "Do pełnych złotych (49 gr w dół, 50 gr w górę)."]],
     "pulapki": ["Zaokrąglanie 13,71% jedną kwotą — składki osobno.", "KUP odejmujesz także od wynagrodzenia chorobowego (tak — to przychód ze stosunku pracy), ale nie od zasiłku."],
     "test": [
         {"p": "Ile wynosi netto przy 4 806 zł brutto, KUP 250, PIT-2, bez PPK (2026)?", "o": ["3 505,85", "3 605,85", "3 773,85", "3 305,85"], "odp": 1, "w": "Składki 658,91, zdrowotna 373,24, zaliczka 168."},
         {"p": "Które składki nalicza się od wynagrodzenia chorobowego?", "o": ["Społeczne i zdrowotną", "Tylko zdrowotną", "Żadnych", "Tylko społeczne"], "odp": 1, "w": "Wynagrodzenie chorobowe — bez społecznych, ze zdrowotną i PIT."},
         {"p": "Kwotę zmniejszającą (300 zł) odejmujesz od:", "o": ["Podstawy opodatkowania", "Obliczonej zaliczki (12% podstawy)", "Przychodu", "Składki zdrowotnej"], "odp": 1, "w": "Zaliczka − 300 → zaokrąglenie."},
     ]},

    {"id": "zaliczka_pit", "tydzien": 4, "nazwa": "Zaliczka na PIT: PIT-2, KUP, próg 32%, ulgi i zwolnienia",
     "slowa": ["pit-2", "pit2", "koszty uzyskania", "kup", "32%", "próg podatkowy", "ulga dla młodych", "ulga dla mlodych", "ulga na powrót", "zwolnienie", "kwota zmniejszająca"],
     "wyjasnienie":
         "PIT-2 (jeden formularz od 2023) zbiera oświadczenia i wnioski pracownika: kwota zmniejszająca 1/12 (300 zł), 1/24 (150) lub 1/36 (100) — pracownik dzieli między płatników; podwyższone KUP 300 zł (miejsce zamieszkania poza miejscowością zakładu, bez dodatku za rozłąkę); zamiar wspólnego rozliczenia (12% mimo przekroczenia progu); ulga dla młodych — wniosek o NIEstosowanie; ulga na powrót (4 lata od powrotu, do 85 528 zł), dla rodzin 4+ (do 85 528), dla pracujących seniorów (kobiety 60+/mężczyźni 65+ bez emerytury — do 85 528) — oświadczenia o spełnieniu warunków; rezygnacja z KUP (np. przy wielu etatach); wniosek o niepobieranie zaliczek (dochód roczny ≤ 30 000 zł). Stosujesz od następnego miesiąca po złożeniu (lub od razu); obowiązują do odwołania; po ustaniu stosunku pracy płatnik przy późniejszych wypłatach POMIJA złożone oświadczenia i wnioski (art. 31a ust. 7 PIT) — bez kwoty zmniejszającej, bez podwyższonych KUP, bez ulg na oświadczenie; nadal stosuje tylko wnioski o niestosowanie KUP, o rezygnację z 50% KUP i o niestosowanie ulgi dla młodych (KUP 250 i ulga dla młodych działają z mocy ustawy).\n"
         "Próg: 12% do 120 000 zł DOCHODU (przychód − składki społeczne − KUP) narastająco od początku roku; w miesiącu przekroczenia — 12% od części do progu i 32% od nadwyżki; od następnego miesiąca 32%; pracownik może wnioskować o 32% wcześniej (unika dopłaty). Kwota zmniejszająca stosowana także przy 32%. Ulga dla młodych: przychody ze stosunku pracy, zlecenia, praktyk, zasiłku macierzyńskiego — do 85 528 zł rocznie zwolnione (do dnia 26. urodzin); składki ZUS normalnie; zdrowotna ograniczona do hipotetycznej zaliczki (liczonej jak bez ulgi) — w praktyce przy minimalnej działa.\n"
         "Zasiłki (chorobowy, macierzyński, opiekuńczy): przychód z innych źródeł, zaliczka 12% bez KUP (kwota zmniejszająca — gdy PIT-2 u tego płatnika). Danina solidarnościowa 4% ponad 1 mln — rozlicza podatnik. Zmiany 2027 (projekt uchwalony przez Sejm 22.10.2026, Senat z poprawkami): próg 130 000, stawka 24% do 150 000 — sprawdź status przed listą za styczeń 2027.",
     "przyklad":
         "Pracownik 14 000 zł, KUP 250, PIT-2: dochód miesięczny = 14 000 − 1 919,40 − 250 = 11 830,60 → narastająco: po 10 miesiącach 118 306; w listopadzie przekracza 120 000 (1 694 do progu, 10 136,60 nadwyżki) → zaliczka XI = 12% × 1 694 + 32% × 10 136,60 − 300 = 203,28 + 3 243,71 − 300 = 3 146,99 → 3 147; od grudnia 32% od całości.",
     "zadania": ["Wypełnij PIT-2 dla 3 pracowników z FIRMA.md (różne sytuacje).",
                 "Policz miesiąc przekroczenia progu dla 14 000 zł z premią 10% w czerwcu.",
                 "Rozlicz zasiłek chorobowy 2 000 zł na liście płac (zaliczka, bez składek)."],
     "pytania": [["Co liczysz do progu 120 000 zł?", "Dochód: przychód − składki społeczne pracownika − KUP, narastająco; nie brutto."],
                 ["Jak PIT-2 wpływa na zaliczkę od zasiłku?", "Kwota zmniejszająca 300 zł stosowana jest także do zaliczki od zasiłku wypłacanego przez tego płatnika."],
                 ["Czy osoba do 26 lat płaci składki ZUS?", "Tak — ulga dla młodych dotyczy tylko PIT (student na zleceniu — brak składek z innego tytułu)."]],
     "pulapki": ["Dwa etaty z PIT-2 1/12 u obu → dopłata w zeznaniu; pouczaj.", "KUP 300 bez oświadczenia — nie wolno; z oświadczeniem nawet gdy dojeżdża tylko kilka dni."],
     "test": [
         {"p": "Kiedy stosujesz 32%?", "o": ["Od brutto 10 000 zł miesięcznie", "Od nadwyżki dochodu ponad 120 000 zł narastająco w roku", "Od przychodu ponad 120 000 zł", "Zawsze na wniosek pracodawcy"], "odp": 1, "w": "Dochód = przychód − składki − KUP."},
         {"p": "Limit przychodów zwolnionych w uldze dla młodych?", "o": ["30 000 zł", "85 528 zł", "120 000 zł", "100 000 zł"], "odp": 1, "w": "Łącznie z ulgą na powrót/4+/seniorów."},
         {"p": "Pracownik złożył PIT-2 15 marca. Od kiedy stosujesz kwotę zmniejszającą?", "o": ["Od stycznia (wstecz)", "Najpóźniej od kwietnia (można od marca)", "Od następnego roku", "Nigdy — za późno"], "odp": 1, "w": "Art. 31a ust. 5 PIT — najpóźniej od miesiąca następnego."},
     ]},

    {"id": "koszt_pracodawcy", "tydzien": 4, "nazwa": "Koszt pracodawcy i składka wypadkowa",
     "slowa": ["koszt pracodawcy", "koszt zatrudnienia", "wypadkowa", "pkd", "iwa", "fundusz pracy", "fgśp", "fgsp", "zwolnienie z fp", "budżet wynagrodzeń"],
     "wyjasnienie":
         "Składki finansowane przez pracodawcę: emerytalna 9,76%, rentowa 6,5%, wypadkowa (0,67–3,33%), FP 2,45% (w tym FS 1,45%), FGŚP 0,10%, FEP 1,5% (praca w szczególnych warunkach/charakterze — wykaz), plus PPK 1,5% (do 4%). Zwolnienia z FP i FGŚP: pracownicy — kobiety ≥ 55 lat i mężczyźni ≥ 60 lat; przez 12 miesięcy po powrocie z macierzyńskiego/rodzicielskiego/wychowawczego; przez 36 miesięcy za osoby 50+ zatrudnione z PUP (bezrobotne), 12 miesięcy za skierowanych do 30 lat; wynagrodzenie < minimalne w przeliczeniu na miesiąc (np. niepełny etat poniżej 4 806) — brak FP/FGŚP, jeśli łączna podstawa z wszystkich tytułów < minimalnej. Przy wypadkowej: płatnik zgłaszający do 9 ubezpieczonych — 1,67% (50% najwyższej stopy); ≥ 10 — stopa dla grupy PKD (załącznik do rozporządzenia; dla działu 10 „produkcja artykułów spożywczych” sprawdź aktualną), a po 3 latach składania IWA — ZUS ustala indywidualnie (zawiadomienie do 20 kwietnia) z korektą ±50% wg wskaźnika częstości wypadków; obowiązuje od 1 kwietnia do 31 marca; IWA do 31 stycznia (gdy ≥ 10 ubezpieczonych średnio, zgłoszony cały rok, w REGON).\n"
         "Pełny koszt etatu to brutto × (1 + 9,76 + 6,5 + wypadkowa + 2,45 + 0,10)% + PPK + ZFŚS (2 943,23/rok na etat, gdy fundusz) + badania, BHP, odzież, szkolenia, sprzęt + koszt nieobecności (wynagrodzenie chorobowe 33 dni, urlop — wynagrodzenie bez pracy). Dla 4 806 zł: 4 806 × 1,2048 = 5 790,28 zł miesięcznie (bez PPK i ZFŚS). Zarząd pyta „ile kosztuje pracownik” — odpowiedź: ~1,21–1,25 × brutto + stałe.\n"
         "Porównanie form: zlecenie z pełnymi składkami kosztuje tyle samo w ZUS (bez FP/FGŚP, gdy zbieg; bez urlopu i 33 dni), B2B — bez kosztów ZUS po stronie firmy, ale ryzyko art. 22 §1¹ KP (ustalenie stosunku pracy: składki 5 lat wstecz z odsetkami, których nie potrącisz pracownikowi, urlopy, nadgodziny, PIP). Limit 30-krotności obniża koszt w końcówce roku dla wysokich pensji (brak emerytalnej/rentowej po 282 600 zł podstawy).",
     "przyklad":
         "Pracownica 56 lat, 6 000 zł, wypadkowa firmy 1,20%:\n"
         "emerytalna 585,60 + rentowa 390,00 + wypadkowa 72,00 + FP 0 (zwolnienie 55+) + FGŚP 0 + PPK 90,00 = 1 137,60\n"
         "koszt miesięczny 7 137,60 zł; rocznie + ZFŚS 2 943,23 → 88 594 zł + badania/BHP.",
     "zadania": ["Policz roczny koszt 8 pracowników z rozbiciem na fundusze.",
                 "Ustal stopę wypadkową dla PKD firmy i zapisz źródło.",
                 "Porównaj koszt etat/zlecenie/B2B dla 6 000 zł."],
     "pytania": [["Kiedy nie płacisz FP i FGŚP za pracownika?", "Kobieta 55+/mężczyzna 60+, 12 mies. po urlopach rodzicielskich, 36 mies. za 50+ z PUP, wynagrodzenie poniżej minimalnej ze wszystkich tytułów."],
                 ["Od kiedy obowiązuje nowa stopa wypadkowa?", "Od 1 kwietnia do 31 marca następnego roku."],
                 ["Ile kosztuje pracodawcę pensja minimalna 2026 (bez PPK)?", "5 790,28 zł (4 806 + 984,28 składek pracodawcy przy wypadkowej 1,67%; ≈ × 1,2048)."]],
     "pulapki": ["FP od pełnej kwoty u pracownika na 1/2 etatu z 2 500 zł bez innych tytułów — nie płacisz (poniżej minimalnej).", "IWA nie złożona 3 lata z rzędu — ZUS nie ustali stopy indywidualnie, ale brak IWA to wykroczenie."],
     "test": [
         {"p": "Składka wypadkowa dla płatnika zgłaszającego 62 ubezpieczonych:", "o": ["Zawsze 1,67%", "Wg grupy PKD, a po 3 latach IWA — ustalona przez ZUS", "Wg uznania płatnika", "0,67%"], "odp": 1, "w": "1,67% tylko dla płatników do 9 ubezpieczonych."},
         {"p": "Za którego pracownika nie płacisz Funduszu Pracy?", "o": ["Za 45-letniego kierownika", "Za 61-letniego magazyniera", "Za 30-letnią księgową", "Za nikogo — FP jest zawsze"], "odp": 1, "w": "Mężczyzna ≥ 60 lat."},
         {"p": "Co grozi firmie przy przekwalifikowaniu B2B na etat przez sąd?", "o": ["Nic — umowa jest ważna", "Składki za 5 lat wstecz z odsetkami (bez możliwości potrącenia części pracownika), urlop, nadgodziny", "Tylko grzywna 1 000 zł", "Tylko obowiązek zawarcia umowy na przyszłość"], "odp": 1, "w": "Art. 22 §1¹ KP, art. 281 KP, przedawnienie składek 5 lat."},
     ]},

    # ================================================================ TYDZIEŃ 5
    {"id": "wynagrodzenie_urlopowe", "tydzien": 5, "nazwa": "Wynagrodzenie za urlop i ekwiwalent",
     "slowa": ["wynagrodzenie urlopowe", "za urlop", "ekwiwalent", "współczynnik", "wspolczynnik", "20,92", "składniki zmienne", "skladniki zmienne", "część miesiąca", "czesc miesiaca"],
     "wyjasnienie":
         "Rozporządzenie urlopowe (8.01.1997): wynagrodzenie za urlop = jakie pracownik dostałby, gdyby pracował. Składniki stałe miesięczne — w wysokości z miesiąca urlopu (nie przeliczasz; w praktyce wypłacasz pensję bez zmian). Składniki zmienne za okresy nie dłuższe niż miesiąc (nadgodziny, nocne, premie miesięczne, prowizje) — średnia z 3 miesięcy poprzedzających miesiąc urlopu (do 12 przy znacznych wahaniach): suma składników / godziny przepracowane w tych miesiącach = stawka godzinowa × godziny urlopu. Składniki za okresy dłuższe niż miesiąc (kwartalne, roczne) — nie do urlopowego. Wyłączone (§6): jednorazowe/nieperiodyczne, nagrody jubileuszowe, ekwiwalenty, odprawy, wynagrodzenie za czas choroby i zasiłki, wynagrodzenie za nadgodziny... — uwaga: nadgodziny WCHODZĄ (dodatek i normalne), wyłączone jest tylko wynagrodzenie za „czas gotowości/przestoju”. Zmiana stawek w okresie 3 miesięcy — przeliczasz składniki wg nowych.\n"
         "Ekwiwalent (art. 171, §14–19): tylko przy niewykorzystaniu z powodu rozwiązania/wygaśnięcia umowy; podstawa: stałe z miesiąca nabycia prawa + zmienne miesięczne (średnia z 3 mies.) + zmienne za okresy > 1 mies. (średnia z 12 mies.); stawka dzienna = podstawa / współczynnik (2026: 20,92 = (365 − 52 niedziele − 52 soboty − 10 świąt) / 12; niepełny etat proporcjonalnie: 1/2 → 10,46); stawka godzinowa = dzienna / 8 (7 dla niepełnosprawnych); ekwiwalent = stawka godz. × godziny urlopu. Od 27.01.2026 (ustawa z 4.12.2025) wypłata w terminie wypłaty wynagrodzenia, a gdy termin ten przypada przed ustaniem — w 10 dni od ustania. Ekwiwalent: składki i PIT jak wynagrodzenie.\n"
         "Wynagrodzenie za część miesiąca (rozporządzenie o wynagrodzeniu z 29.05.1996): choroba/zasiłek — pensję stałą dzielisz przez 30 i mnożysz przez dni kalendarzowe nieobecności (§11); inne nieobecności bez prawa do wynagrodzenia (bezpłatny, nieusprawiedliwiona) — dzielisz przez wymiar godzin miesiąca i mnożysz przez godziny nieobecności (§12); zatrudnienie/zwolnienie w trakcie miesiąca — przez wymiar × godziny przepracowane. Składniki zmienne (nadgodziny) — nie pomniejszasz (są za faktyczną pracę).",
     "przyklad":
         "Ekwiwalent 2026, pełny etat, 6 000 zł + zmienne średnio 400 zł, 7 dni (56 h) niewykorzystane:\n"
         "podstawa 6 400 → dzienna 6 400 / 20,92 = 305,93 → godz. 38,24 → 56 × 38,24 = 2 141,44 zł.\n"
         "1/2 etatu, 2 500 zł, 32 h: współczynnik 10,46 → 239,01 → 29,88 → 956,16 zł.\n"
         "Pensja 6 000, L4 10 dni w listopadzie: 6 000 − 6 000/30×10 = 4 000 za pracę (+ chorobowe); urlop bezpłatny 24 h: 6 000 − 6 000/160×24 = 5 100.",
     "zadania": ["Policz urlopowe z zmiennymi (przykład B z zadania tygodnia).",
                 "Policz ekwiwalent dla 3/4 etatu z 5 dniami urlopu.",
                 "Rozlicz pensję za miesiąc z chorobą i bezpłatnym jednocześnie."],
     "pytania": [["Przez co dzielisz zmienne składniki przy urlopowym?", "Przez liczbę godzin faktycznie przepracowanych w miesiącach, z których bierzesz składniki (nie przez wymiar)."],
                 ["Jaki współczynnik ekwiwalentu dla 1/2 etatu w 2026?", "10,46 (20,92 × 1/2)."],
                 ["Do kiedy wypłacasz ekwiwalent przy ustaniu 31.12?", "W terminie wypłaty wynagrodzenia; jeśli ten przypada przed ustaniem — w 10 dni od ustania (zmiana od 27.01.2026)."]],
     "pulapki": ["Premia roczna w urlopowym — nie; w ekwiwalencie — tak (1/12).", "Choroba dzielona przez wymiar godzin — zawsze przez 30."],
     "test": [
         {"p": "Współczynnik ekwiwalentu dla pełnego etatu w 2026 r.?", "o": ["20,83", "20,92", "21,00", "20,58"], "odp": 1, "w": "251 dni roboczych / 12."},
         {"p": "Składniki zmienne do wynagrodzenia urlopowego bierzesz z:", "o": ["Miesiąca urlopu", "3 miesięcy poprzedzających (do 12 przy wahaniach)", "12 miesięcy zawsze", "Ostatniego kwartału kalendarzowego"], "odp": 1, "w": "§8 rozporządzenia urlopowego."},
         {"p": "Pracownik 6 000 zł chorował 10 dni w lutym (28 dni). Pomniejszenie?", "o": ["6 000/28 × 10", "6 000/30 × 10 = 2 000", "6 000/160 × 80", "6 000/20 × 7"], "odp": 1, "w": "§11 — zawsze dzielnik 30."},
     ]},

    {"id": "potracenia", "tydzien": 5, "nazwa": "Potrącenia z wynagrodzenia: art. 87–91 KP",
     "slowa": ["potrącen", "potracen", "komornik", "alimenty", "kwota wolna od potrąceń", "zajęcie", "zajecie", "art. 87", "art. 91", "kara pieniężna"],
     "wyjasnienie":
         "Bez zgody pracownika potrącasz (art. 87 §1) w kolejności: (1) sumy egzekwowane na alimenty, (2) inne tytuły wykonawcze (komornik), (3) zaliczki pieniężne udzielone pracownikowi, (4) kary pieniężne z art. 108. Granice (po odliczeniu składek ZUS, zaliczki PIT i wpłat PPK pracownika): alimenty do 3/5; inne do 1/2; łącznie alimenty + inne do 3/5; kary — do 1/10 wynagrodzenia po innych potrąceniach. Kwoty wolne (art. 87¹): minimalne wynagrodzenie netto (po odliczeniu składek, PIT i PPK dla danego pracownika — różne dla różnych osób!) — przy niealimentacyjnych; 75% minimalnego netto — zaliczki; 90% — kary; alimenty — BEZ kwoty wolnej. Niepełny etat: kwoty wolne proporcjonalnie. Nagroda z ZFŚS, trzynastka, jubileuszowa — na alimenty do 100%.\n"
         "Procedura przy zajęciu: komornik doręcza zajęcie → od tej chwili potrącasz i przekazujesz; w 7 dni odpowiadasz (art. 882 KPC): wynagrodzenie za 3 miesiące, inne zajęcia, przeszkody; zbieg egzekucji — informujesz obu komorników, przekazujesz do tego, który pierwszy zajął; ustanie zatrudnienia — zawiadamiasz, wpisujesz zajęcie w świadectwie (komornik, sygnatura, kwota). Za nieprzekazanie — grzywna do 5 000 zł od komornika i odpowiedzialność za szkodę. Zajęcie zasiłków z ZUS (gdy płatnik wypłaca) — limity z ustawy emerytalnej: alimenty 60%, inne 25%, kwota wolna jak w emeryturach.\n"
         "Za zgodą (art. 91): tylko pisemna zgoda z konkretną kwotą/tytułem (np. pożyczka z ZFŚS, składka związkowa, ubezpieczenie grupowe) — kwota wolna 100% minimalnego netto (inne) lub 80% (na rzecz pracodawcy). Inne pomniejszenia nie są potrąceniami: nadpłacone wynagrodzenie za okres nieobecności może być odliczone w najbliższym terminie (art. 87 §7) — tylko za okres nieobecności, nie „pomyłkę”; zwykłą nadpłatę odzyskujesz za zgodą lub sądownie.",
     "przyklad":
         "Komornik (niealimentacyjne), pracownik 1 etat, KUP 250, PIT-2, bez PPK, netto 4 300 zł:\n"
         "max 1/2 netto = 2 150; kwota wolna = 3 605,85 → możesz potrącić 4 300 − 3 605,85 = 694,15 zł.\n"
         "Gdyby pracownik był w PPK (2% = 96,12 z netto): kwota wolna liczona z uwzględnieniem PPK (minimalne netto z PPK = 3 501,73: zaliczka rośnie do 176 przez wpłatę pracodawcy 72,09, a 96,12 schodzi z netto) — policz i porównaj.",
     "zadania": ["Rozwiąż 5 kazusów potrąceń (zadanie tygodnia).",
                 "Napisz odpowiedź dla komornika w 7 dni (wzór).",
                 "Ustal kwoty wolne dla pracownika 1/2 etatu bez PIT-2."],
     "pytania": [["Jaka jest granica potrącenia na alimenty i czy jest kwota wolna?", "3/5 wynagrodzenia netto; kwoty wolnej nie ma."],
                 ["Co zrobić przy dwóch zajęciach od różnych komorników?", "Potrącać dla pierwszego, zawiadomić obu o zbiegu (art. 773 KPC) i czekać na wskazanie właściwego."],
                 ["Czy można potrącić pożyczkę z ZFŚS bez zgody?", "Nie — tylko pisemna zgoda z kwotą (art. 91), z kwotą wolną 80% minimalnego netto."]],
     "pulapki": ["Kwota wolna „3 605,85 dla wszystkich” — zależy od KUP/PIT-2/PPK pracownika.", "Potrącanie nadpłaty wynagrodzenia „bo pomyliliśmy się” bez zgody — niedopuszczalne poza art. 87 §7."],
     "test": [
         {"p": "Netto 4 000 zł, zajęcie niealimentacyjne, kwota wolna 3 605,85. Potrącasz:", "o": ["2 000 zł", "394,15 zł", "1 000 zł", "0 zł"], "odp": 1, "w": "Min(1/2 netto; netto − kwota wolna)."},
         {"p": "Kolejność potrąceń bez zgody pracownika:", "o": ["Komornik, alimenty, kary, zaliczki", "Alimenty, inne tytuły wykonawcze, zaliczki, kary", "Kary, zaliczki, alimenty, komornik", "Dowolna"], "odp": 1, "w": "Art. 87 §1 KP."},
         {"p": "Termin odpowiedzi pracodawcy na zajęcie komornicze?", "o": ["3 dni", "7 dni", "14 dni", "30 dni"], "odp": 1, "w": "Art. 882 KPC; grzywna do 5 000 zł za brak."},
     ]},

    {"id": "swiadczenia_pozaplacowe", "tydzien": 5, "nazwa": "Świadczenia pozapłacowe i ZFŚS w liście płac",
     "slowa": ["benefit", "świadczenia pozapłacowe", "swiadczenia pozaplacowe", "samochód służbowy", "samochod sluzbowy", "karta sportowa", "pakiet medyczny", "ryczałt", "ryczalt", "nieodpłatne świadczenie"],
     "wyjasnienie":
         "Przychód ze stosunku pracy (art. 12 PIT) to także świadczenia w naturze i nieodpłatne; składki ZUS od nich — chyba że wyłączone rozporządzeniem składkowym (§2 ust. 1: m.in. nagrody jubileuszowe nie częściej niż co 5 lat, odprawy, ekwiwalenty za narzędzia/pranie/używanie własnej odzieży, diety i zwrot kosztów podróży do limitów, ryczałt za auto prywatne do limitu kilometrówki, świadczenia z ZFŚS zgodne z ustawą, korzyści materialne z układu/regulaminu polegające na zakupie po cenie niższej niż detaliczna — np. współfinansowane karty sportowe/pakiety medyczne, gdy pracownik dopłaca choć 1 zł: składek brak, PIT jest). Wycena: cena zakupu (pakiet, karta), ryczałt auta: 250 zł (≤ 60 kW lub elektryczny/wodorowy) / 400 zł (pozostałe), za dzień 1/30 — obejmuje paliwo (NSA), ZUS i PIT; auto bez używania prywatnego — nie jest przychodem przy właściwej ewidencji/regulaminie.\n"
         "Zwolnienia PIT: posiłki/bony do 450 zł miesięcznie (art. 21 ust. 1 pkt 11b), ekwiwalent za pranie, narzędzia, ryczałt za pracę zdalną (odpowiadający kosztom), dokształcanie z inicjatywy pracodawcy, świadczenia z ZFŚS do 1 000 zł rocznie (pieniężne i rzeczowe, bez bonów), zapomogi losowe (z ZFŚS bez limitu, z innych źródeł do 6 000), ubezpieczenie OC/NNW w interesie pracodawcy — nie przychód. Ubezpieczenie grupowe opłacane przez pracodawcę i pakiet medyczny (poza medycyną pracy) — przychód i składki (chyba że współfinansowanie wg regulaminu).\n"
         "ZFŚS: świadczenia tylko z kryterium socjalnym (sytuacja życiowa, rodzinna, materialna — oświadczenie o dochodach na osobę) — wtedy bez ZUS i PIT do 1 000 zł (nadwyżka: PIT, bez ZUS). „Po równo” lub według stanowiska/stażu = ZUS doliczy składki w kontroli (najczęstsze ustalenie). Na liście płac: wiersz „świadczenie ZFŚS” wpływa na podstawę PIT ponad limit, nie na składki; świadczenie w naturze z firmy — wiersz zwiększający podstawy, nie wypłacany (netto maleje o obciążenia).",
     "przyklad":
         "Pracownik 6 000 zł + auto 400 zł ryczałtu + karta sportowa 150 zł (pracownik dopłaca 1 zł wg regulaminu wynagradzania):\n"
         "podstawa ZUS: 6 000 + 400 = 6 400 (karta wyłączona — współfinansowanie); podstawa PIT: 6 000 + 400 + 149 = 6 549 (minus składki i KUP).\n"
         "Netto spada względem 6 000 o składki od 400 i podatek od 549; pracownik nie dostaje tych kwot gotówką.",
     "zadania": ["Zbuduj tabelę 10 świadczeń (zadanie tygodnia).",
                 "Policz listę płac z autem i kartą (jak w przykładzie) dla pracownika z PPK.",
                 "Zaprojektuj regulamin współfinansowania benefitów, żeby uniknąć składek."],
     "pytania": [["Kiedy karta sportowa nie podlega składkom ZUS?", "Gdy z regulaminu/układu wynika współfinansowanie przez pracownika (kupuje poniżej ceny detalicznej) albo gdy z ZFŚS z kryterium socjalnym."],
                 ["Ile wynosi ryczałt za auto służbowe do celów prywatnych?", "250 zł (do 60 kW / elektryczny) lub 400 zł miesięcznie; 1/30 za dzień."],
                 ["Jaki limit zwolnienia PIT dla świadczeń z ZFŚS?", "1 000 zł rocznie (bez bonów/talonów), zapomogi losowe bez limitu."]],
     "pulapki": ["Pakiet medyczny „w pełni od firmy” — przychód i składki; „1 zł od pracownika” wg regulaminu — bez składek.", "Paczka świąteczna z ZFŚS dla każdego po 300 zł — kwestionowana; zróżnicuj wg dochodu."],
     "test": [
         {"p": "Ryczałt za używanie samochodu służbowego 90 kW do celów prywatnych (2026)?", "o": ["250 zł", "400 zł", "500 zł", "Według kilometrówki"], "odp": 1, "w": "Powyżej 60 kW — 400 zł; paliwo wliczone."},
         {"p": "Świadczenie z ZFŚS przyznane „po równo” wszystkim:", "o": ["Zwolnione z PIT do 1 000 zł i bez ZUS", "Podlega ZUS (brak kryterium socjalnego)", "Jest zwolnione z PIT bez limitu", "Nie jest przychodem"], "odp": 1, "w": "ZUS doliczy składki; PIT również (nie jest to działalność socjalna)."},
         {"p": "Do jakiej kwoty miesięcznie zwolnione są posiłki/bony od pracodawcy?", "o": ["190 zł", "300 zł", "450 zł", "Bez limitu"], "odp": 2, "w": "Art. 21 ust. 1 pkt 11b PIT (od 2022)."},
     ]},
]
