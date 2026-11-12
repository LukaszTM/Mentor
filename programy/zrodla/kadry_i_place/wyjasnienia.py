# -*- coding: utf-8 -*-
"""Wyjaśnienia lekcji przepisane ręcznie wg zasady „jedna reguła — jedno zdanie”: nagłówki „## ”, krótkie zdania, punkty „- ”,
tabele Markdown „| a | b |” dla porównań. Treść merytoryczna i liczby identyczne z wersją źródłową w lekcje_*.py (zbuduj.py
sprawdza, czy żadna liczba ani odwołanie do przepisu nie zginęły). Stan prawny: XI 2026."""

WYJASNIENIA = {}

WYJASNIENIA["zrodla_prawa"] = """## Czego uczy się kadrowiec
Kadrowiec nie uczy się przepisów na pamięć. Uczy się, gdzie przepisy są i jak je czytać.

## Hierarchia źródeł — co jest ważniejsze
| Poziom | Przykłady | Zasada |
|---|---|---|
| Konstytucja | — | najwyżej |
| Ustawy | Kodeks pracy, ustawa o systemie ubezpieczeń społecznych, zasiłkowa, PIT, ZFŚS, PPK, o zwolnieniach grupowych | podstawa wszystkiego |
| Rozporządzenia wykonawcze | o dokumentacji pracowniczej, o wynagrodzeniu urlopowym, o minimalnym wynagrodzeniu, składkowe | uszczegóławiają ustawę |
| Akty wewnątrzzakładowe | układ zbiorowy, regulamin pracy, regulamin wynagradzania | nie mogą być mniej korzystne niż ustawa |
| Umowa o pracę | — | nie może być mniej korzystna niż regulamin |

Zasada uprzywilejowania pracownika (art. 18 KP): postanowienie mniej korzystne niż przepis jest nieważne. W jego miejsce wchodzi przepis.

## Gdzie czytać
| Źródło | Co tam znajdziesz |
|---|---|
| ISAP (isap.sejm.gov.pl) | teksty ujednolicone z polem „stan prawny na dzień” |
| Dziennik Ustaw (dziennikustaw.gov.pl) | ogłoszone akty, w tym nowelizacje |
| Monitor Polski | obwieszczenia: limit 30-krotności, kwoty ZFŚS |
| zus.pl, podatki.gov.pl | wskaźniki, formularze, objaśnienia MF |
| PIP (pip.gov.pl) | poradniki i stanowiska |
| orzecznictwo SN (sn.pl) | gdy przepis jest nieostry (np. „ciężkie naruszenie”) |
| portale Infor, Gofin, Lex | komentarze — pomagają, ale źródłem jest akt |

## Trzy nawyki
- Każdą liczbę sprawdzasz u źródła raz w roku i po każdej nowelizacji.
- Czytając przepis, patrzysz na datę wejścia w życie i na przepisy przejściowe.
- Rozróżniasz „obowiązuje” od „projekt”. W tym kursie każda taka informacja ma oznaczenie.

## Dlaczego daty są ważne — zmiany 2025/2026
| Zmiana | Od kiedy |
|---|---|
| jawność wynagrodzeń w rekrutacji | 24.12.2025 |
| staż pracy z umów zlecenia — sektor publiczny | 1.01.2026 |
| staż pracy z umów zlecenia — sektor prywatny | 1.05.2026 |
| kontrola zwolnień lekarskich (L4) | 13.04.2026 |
| mobbing i dyskryminacja — nowe przepisy | 5.11.2026 |
| procedury antymobbingowe w firmach | do 5.05.2027 |"""

WYJASNIENIA["narzedzia_kadrowca"] = """## Cztery systemy, bez których nie da się pracować
| System | Do czego służy | Kto ma dostęp |
|---|---|---|
| eZUS (dawniej PUE ZUS) | portal ZUS: ubezpieczeni, e-ZLA pracowników, saldo składek, wnioski (Z-3, US-3 → A1, zaświadczenie o niezaleganiu), pisma z ZUS | pracownik kadr z pełnomocnictwem PEL podpisanym przez zarząd |
| Płatnik | program ZUS do dokumentów zgłoszeniowych (ZUA, ZZA, ZWUA, ZCNA) i rozliczeniowych (DRA, RCA, RSA, RPA); weryfikacja i wysyłka z certyfikatem kwalifikowanym | małe firmy mogą użyć ePłatnika w eZUS |
| e-Urząd Skarbowy / e-Deklaracje | PIT-4R, PIT-11, PIT-8AR, IFT składasz elektronicznie | osoba z pełnomocnictwem UPL-1 zgłoszonym do US |
| program kadrowo-płacowy (Symfonia, Optima, enova, Gratyfikant…) | generuje listy płac, dokumenty ZUS (eksport do Płatnika — plik KEDU) i PIT-11 | kadry i płace |

Program liczy, ale Ty odpowiadasz za błędy. Dlatego musisz rozumieć, co jest w środku każdego dokumentu.
Zaliczki PIT wpłacasz na mikrorachunek podatkowy firmy (NIP).
PIT-11 to tylko suma kartoteki przychodów. Kartotekę prowadzisz poprawnie przez cały rok.

## Pozostałe portale
- praca.gov.pl — powiadomienia o cudzoziemcach, PUP.
- e-PFRON2 — DEK, Wn-D.
- portal sprawozdawczy GUS.
- platforma PPK instytucji finansowej — zapisy, wpłaty (plik).
- e-Doręczenia — od 2025 obowiązkowe dla firm; tu przychodzą pisma urzędowe.

## Bezpieczeństwo dostępów
- Każda osoba ma oddzielne konto i własne uprawnienia.
- Prowadzisz rejestr pełnomocnictw.
- Gdy pracownik kadr odchodzi, odwołujesz jego pełnomocnictwa tego samego dnia.

## W tym kursie: Warsztat zamiast kont
Żadnego z tych systemów nie musisz zakładać ani instalować. Zakładka Warsztat w Mentorze ma ich symulatory.
| Narzędzie Warsztatu | Co odpowiada prawdziwemu systemowi |
|---|---|
| eZUS / Płatnik | rejestr ubezpieczonych, dokumenty zgłoszeniowe z weryfikacją jak w Płatniku, komplety DRA/RCA/RSA, skrzynka e-ZLA, rejestr z numerami UPP |
| e-Urząd: PIT | PIT-11 i PIT-4R z Twojej kartoteki, UPO |
| kalkulatory | lista płac, zasiłki, urlopy, czas pracy, potrącenia, delegacje |
| Przepisy | biblioteka przepisów offline |
Ekrany i komunikaty odpowiadają prawdziwym. Po kursie przesiadka na eZUS i Płatnika to kwestia logowania, nie nauki od nowa."""

WYJASNIENIA["wskazniki_2026"] = """## Minimalne wynagrodzenie
| Rok | Minimalne (pełny etat) | Stawka godzinowa (zlecenia, usługi) | Podstawa |
|---|---|---|---|
| 2026 | 4 806 zł brutto | 31,40 zł | rozporządzenie RM z 11.09.2025 |
| 2027 | 4 950 zł | 32,30 zł | rozporządzenie z 14.09.2026, Dz.U. 2026 poz. 1213 |

Od minimalnej zależą inne kwoty:
- dodatek nocny — 20% stawki godzinowej z minimalnej,
- kwoty wolne od potrąceń — minimalne netto,
- maksymalna odprawa — 15× minimalnej = 72 090 zł,
- odszkodowanie za mobbing — 6× minimalnej = 28 836 zł,
- wynagrodzenie za przestój,
- minimalna podstawa zasiłku,
- obniżona wpłata PPK — przy wynagrodzeniu ≤ 120% minimalnej = 5 767,20 zł.

## Składki ZUS (stopy od lat niezmienne)
| Składka | Pracownik | Pracodawca | Razem |
|---|---|---|---|
| emerytalna | 9,76% | 9,76% | 19,52% |
| rentowa | 1,5% | 6,5% | 8% |
| chorobowa | 2,45% | — | 2,45% |
| wypadkowa | — | 1,67% do 9 ubezpieczonych; inaczej wg PKD (0,67–3,33%) | — |
| zdrowotna | 9% od podstawy po składkach społecznych | — | 9% |
| FP (w tym FS 1,45%) | — | 2,45% | 2,45% |
| FGŚP | — | 0,10% | 0,10% |
| FEP (prace szczególne) | — | 1,5% | 1,5% |

Pracownik oddaje 13,71% brutto na składki społeczne. Pracodawca dokłada ok. 20,48% (przy wypadkowej 1,67%).
Roczny limit podstawy emerytalno-rentowej 2026: 282 600 zł (30 × prognozowane 9 420 zł).

## PIT 2026
| Element | Wartość |
|---|---|
| skala | 12% do 120 000 zł dochodu, 32% od nadwyżki |
| kwota wolna | 30 000 zł → kwota zmniejszająca 3 600 zł rocznie = 300 zł miesięcznie (PIT-2) |
| KUP | 250 zł (300 zł dojeżdżający); 20% zlecenia; 50% autorskie |
| ulga dla młodych (do 26 lat) | do 85 528 zł przychodu |
| danina solidarnościowa | 4% ponad 1 mln |
Projekt od 2027: próg 130 000 zł, stawka 24% do 150 000 zł. Uchwalony przez Sejm w X 2026, w Senacie. To projekt — sprawdzaj.

## Inne wskaźniki
| Wskaźnik | 2026 |
|---|---|
| współczynnik ekwiwalentu | 20,92 (251 dni roboczych) |
| odpis ZFŚS | 2 943,23 zł (37,5% × 7 848,60) |
| PPK | 2% pracownik + 1,5% pracodawca (+250 zł powitalna, +240 zł rocznie) |
| zasiłek chorobowy | 80% (100% ciąża, wypadek w drodze) |
| wynagrodzenie chorobowe | 33 dni (14 dla 50+) — nadal od pracodawcy (XI 2026) |
| okres zasiłkowy | 182/270 dni |
| urlop wypoczynkowy | 20/26 dni |
| urlop opiekuńczy | 5 dni |
| siła wyższa | 2 dni / 16 h |"""

WYJASNIENIA["rekrutacja_jawnosc"] = """## Jakich danych możesz żądać od kandydata (art. 22¹ §1 KP)
Zawsze: imię i nazwisko, data urodzenia, dane kontaktowe.
Tylko gdy są niezbędne do pracy na stanowisku: wykształcenie, kwalifikacje, przebieg zatrudnienia.
Inne dane (np. niekaralność) — tylko gdy przepis szczególny tego wymaga.
Dane „wrażliwe” (zdrowie, związki) — nie. Wyjątek: orzeczenie o niepełnosprawności kandydat podaje sam, na wniosek pracodawcy, jeśli chce.

## Zakaz pytania o wynagrodzenie (od 24.12.2025, Dz.U. 2025 poz. 807)
Nie wolno żądać informacji o wynagrodzeniu w obecnej i poprzednich pracach (art. 22¹ §1 pkt 6). Ani pytaniem, ani przez dokumenty.

## Jawność wynagrodzeń w rekrutacji (art. 18³ᶜᵃ KP, od 24.12.2025)
Kandydat dostaje dwie informacje: o początkowym wynagrodzeniu lub jego przedziale oraz o postanowieniach układu/regulaminu wynagradzania, jeśli mają zastosowanie.
Przedział ustalasz obiektywnie i neutralnie płciowo. Ogłoszenia mają być neutralne płciowo.

| Sytuacja | Kiedy najpóźniej kandydat dostaje informację |
|---|---|
| jest ogłoszenie | w ogłoszeniu |
| nie było ogłoszenia albo nie podano w nim wynagrodzenia | przed pierwszą rozmową |
| rozmów nie ma | przed nawiązaniem stosunku pracy |
Forma: papierowa lub elektroniczna, z wyprzedzeniem.

Sankcje: grzywna 1 000–30 000 zł (art. 281) i odszkodowanie za dyskryminację — nie mniej niż minimalne wynagrodzenie (art. 18³ᵈ).
Pełne wdrożenie dyrektywy 2023/970 (prawo do informacji o średnich płacach, raport luki) to projekt UC127. W XI 2026 jeszcze nieuchwalony.

## RODO w rekrutacji
| Element | Zasada |
|---|---|
| podstawa przetwarzania | art. 22¹ KP (obowiązek prawny) i działania przed zawarciem umowy |
| dane ponadstandardowe w CV | zgoda przez samo ich podanie; nie wolno ich żądać |
| klauzula informacyjna | w ogłoszeniu lub przy pierwszym kontakcie |
| retencja | do zakończenia rekrutacji (+ okres ewentualnych roszczeń, ale UODO: niezwłocznie); do 12 miesięcy na przyszłe rekrutacje — za zgodą |
| testy, referencje | tylko w zakresie art. 22¹ i za zgodą kandydata na kontakt z referentem |"""

WYJASNIENIA["umowa_o_prace"] = """## Trzy rodzaje umów (art. 25)
| Rodzaj | Najważniejsze zasady |
|---|---|
| na okres próbny | maksymalnie 3 miesiące; ponowna próbna z tym samym pracownikiem — tylko na inny rodzaj pracy |
| na czas określony | łączny limit 33 miesiące i 3 umowy (art. 25¹) |
| na czas nieokreślony | bez limitów |

## Umowa na okres próbny — długość zależy od planów
| Planowana kolejna umowa na czas określony | Maksymalna próbna |
|---|---|
| krótsza niż 6 miesięcy | 1 miesiąc |
| od 6 do 12 miesięcy | 2 miesiące |
| dłuższa albo nieokreślona | 3 miesiące |
Planowany okres kolejnej umowy wpisujesz do umowy próbnej.
Próbną można przedłużyć o urlop i usprawiedliwioną nieobecność, jeśli umowa to przewiduje.

## Umowa na czas określony — limit 33/3
Czwarta umowa albo przekroczenie 33 miesięcy przekształca umowę z mocy prawa w nieokreśloną.
Wyjątki od limitu: zastępstwo, praca dorywcza lub sezonowa, kadencja, obiektywne przyczyny po stronie pracodawcy.
Przy obiektywnych przyczynach: zapis w umowie i zawiadomienie PIP w 5 dni roboczych.
Od 26.04.2023 wypowiedzenie umowy na czas określony wymaga uzasadnienia i konsultacji związkowej — jak przy nieokreślonej.

## Treść umowy (art. 29 §1)
- strony, adres siedziby lub miejsce zamieszkania pracodawcy,
- rodzaj umowy, data zawarcia,
- rodzaj pracy, miejsce lub miejsca wykonywania pracy,
- wynagrodzenie ze wskazaniem składników,
- wymiar czasu pracy, dzień rozpoczęcia pracy,
- przy próbnej — czas trwania, ewentualne przedłużenie o nieobecności, planowana kolejna umowa,
- przy określonej — czas trwania lub termin.

## Forma
Umowę zawierasz na piśmie. Jeśli nie — przed dopuszczeniem do pracy potwierdzasz pisemnie strony, rodzaj i warunki (art. 29 §2).
Brak umowy na piśmie przed dopuszczeniem = wykroczenie.

## Praktyka
- Wynagrodzenie na pełny etat ≥ 4 806 zł; na część etatu proporcjonalnie.
- Premia uznaniowa nie może „uzupełniać” do minimalnej w sposób niepewny. Od 2027 projekt UC62 ma wyłączyć dodatki z minimalnej.
- Miejsce pracy: konkretne — zakład albo obszar dla mobilnych. Zapis „terytorium RP” PIP kwestionuje.
- Zmiana warunków: porozumienie (aneks) albo wypowiedzenie zmieniające.
- Umowa w języku polskim; dla cudzoziemca — tłumaczenie."""

WYJASNIENIA["onboarding_akta"] = """## Przed dopuszczeniem do pracy
| Krok | Szczegóły |
|---|---|
| wstępne badania lekarskie | skierowanie ze wskazaniem czynników szkodliwych; orzeczenie do akt A |
| kto jest zwolniony z badań wstępnych | ponownie przyjmowani do tej samej pracy w 30 dni; osoby z aktualnym orzeczeniem od innego pracodawcy na te same warunki — poza pracami szczególnie niebezpiecznymi |
| umowa o pracę | na piśmie, przed dopuszczeniem |
| szkolenie BHP wstępne | instruktaż ogólny i stanowiskowy; karta do akt B |
| BHP dla administracyjno-biurowych | wstępne zawsze; okresowe można pominąć przy niskim ryzyku |
| zapoznanie | regulamin pracy, ocena ryzyka, informacja o monitoringu |

## Do 7 dni od dopuszczenia
- Informacja o warunkach zatrudnienia (art. 29 §3). Od 2023 rozszerzona: normy czasu pracy, przerwy, odpoczynki, nadgodziny i rekompensata, zasady zmian, składniki wynagrodzenia i świadczenia, urlop, procedura rozwiązania umowy, szkolenia, układ, ZUS.
- Zgłoszenie ZUS ZUA — 7 dni od powstania obowiązku ubezpieczenia, czyli od dnia rozpoczęcia pracy.
- Oświadczenia: PIT-2, KUP, PPK, numer konta, dane kontaktowe.
Do 3 miesięcy: umowa o prowadzenie PPK.

## Akta osobowe A–E (rozporządzenie z 10.12.2018)
| Część | Co zawiera |
|---|---|
| A — ubieganie się o zatrudnienie | kwestionariusz kandydata, skierowanie i orzeczenie wstępne, kwalifikacje |
| B — nawiązanie i przebieg | umowa, kwestionariusz pracownika, informacja art. 29 §3, BHP, potwierdzenia zapoznania, PIT-2/PPK/RODO, aneksy, badania okresowe, uprawnienia rodzicielskie, wnioski o zmianę etatu, oświadczenia o stażu i zaświadczenie ZUS o stażu |
| C — ustanie | wypowiedzenie, świadectwo, dokumenty rozliczenia, wniosek o sprostowanie |
| D — kary porządkowe | usuwane po roku nienagannej pracy |
| E — kontrola trzeźwości | przechowywana rok |
Każda część: chronologia, numeracja, wykaz.
Odrębnie prowadzisz: dokumentację czasu pracy, urlopową, listy płac i karty wynagrodzeń, ewidencję odzieży.

## Przechowywanie
| Zatrudnieni | Okres |
|---|---|
| od 1.01.2019 | 10 lat od końca roku ustania zatrudnienia |
| wcześniej | 50 lat, chyba że złożono ZUS OSW i RIA |

## Postać papierowa albo elektroniczna
Obie są równoważne.
Przejście na e-akta: skan z podpisem kwalifikowanym lub pieczęcią, informacja dla pracowników, 30 dni na odbiór papieru.
Wymogi e-akt: integralność, metadane, kopie, możliwość wydruku.
Pracownik ma prawo do kopii całości lub części akt — na wniosek."""

WYJASNIENIA["czas_pracy_systemy"] = """## Normy (art. 129)
8 godzin na dobę. Przeciętnie 40 godzin w przeciętnie 5-dniowym tygodniu. Liczysz w okresie rozliczeniowym do 4 miesięcy.
Okres do 12 miesięcy — tylko z obiektywnych przyczyn, w układzie lub porozumieniu i z zawiadomieniem PIP.

## Wymiar czasu pracy (art. 130)
Wymiar = pełne tygodnie × 40 h + dni od poniedziałku do piątku poza tygodniami × 8 h − 8 h za każde święto w dniu innym niż niedziela.
Święto w sobotę też obniża wymiar.

## Doba pracownicza
Doba to 24 godziny od rozpoczęcia pracy. Drugie rozpoczęcie pracy w tej samej dobie to nadgodzina. Wyjątek: ruchomy czas pracy z art. 140¹.

## Odpoczynek
| Odpoczynek | Wymiar | Uwagi |
|---|---|---|
| dobowy | 11 h | wyjątki: zarządzający, akcje ratownicze — z równoważnym odpoczynkiem |
| tygodniowy | 35 h | 24 h przy zmianie pory w pracy zmianowej; obejmuje niedzielę (lub inny dzień, gdy praca w niedziele jest dozwolona) |

## Systemy czasu pracy
| System | Dobowy wymiar | Zasady |
|---|---|---|
| podstawowy | 8 h | — |
| równoważny | do 12 h | dozór urządzeń, pogotowie — do 16 h; pilnowanie — do 24 h; okres 1 miesiąc, wyjątkowo 3–4 |
| zadaniowy | — | bez ewidencji godzin; wymiar zadań musi być realny w normach |
| przerywany | — | jedna przerwa do 5 h, 60% wynagrodzenia za przerwę; tylko w układzie lub porozumieniu |
| skrócony tydzień, weekendowy | do 12 h | na wniosek pracownika |
| ruchomy | — | przedziały rozpoczynania albo różne godziny |
| ruch ciągły | — | do 43 h średnio |
| indywidualny rozkład | — | na wniosek |
System i okres rozliczeniowy ustala regulamin, układ albo obwieszczenie.
Harmonogram (grafik) sporządzasz na co najmniej 1 miesiąc. Przekazujesz go 1 tydzień przed (art. 129 §3). Wyjątek: rozkład wynika z regulaminu lub umowy.

## Niedziele i święta
Praca dozwolona tylko w przypadkach z art. 151¹⁰: ruch ciągły, praca zmianowa, handel w ograniczonym zakresie, usługi i inne wymienione.
| Praca w | Rekompensata |
|---|---|
| niedzielę | dzień wolny w 6 dniach przed lub po; inaczej dodatek 100% |
| święto | dzień wolny w okresie rozliczeniowym; inaczej dodatek 100% |
Raz na 4 tygodnie pracownik ma wolną niedzielę.

## Przerwy
| Dobowy czas pracy | Przerwa wliczana do czasu pracy |
|---|---|
| co najmniej 6 h | 15 min |
| ponad 9 h | 30 min (drugie 15 min) |
| ponad 16 h | 45 min (od 2023) |
Przerwa niewliczana do czasu pracy (lunch): do 60 min, zapisana w regulaminie.

## Pracownicy z niepełnosprawnością
Stopień umiarkowany i znaczny: 7 h na dobę, 35 h tygodniowo. Dodatkowe 15 min przerwy. Zakaz pracy nocnej i nadgodzin bez zgody lekarza."""

WYJASNIENIA["nadgodziny_noc"] = """## Kiedy wolno zlecić nadgodziny (art. 151)
Tylko z dwóch powodów: akcja ratownicza albo szczególne potrzeby pracodawcy.
Limit: 150 h rocznie. Regulamin lub umowa może go podnieść — do 416 h, przy zachowaniu średnio 48 h tygodniowo.
| Kto | Nadgodziny |
|---|---|
| ciężarne, młodociani | zakaz |
| pracownicy z niepełnosprawnością | zakaz bez zgody lekarza |
| opiekun dziecka do 8 lat | tylko za zgodą pracownika |

## Dwa rodzaje nadgodzin
| Rodzaj | Kiedy powstaje | Kiedy rozliczasz |
|---|---|---|
| dobowe | przekroczenie 8 h albo przedłużonego wymiaru z grafiku w danym dniu | co miesiąc |
| średniotygodniowe | przepracowane − wymiar − nadgodziny dobowe już policzone | po zakończeniu okresu rozliczeniowego |

## Rekompensata
Za każdą nadgodzinę: normalne wynagrodzenie + dodatek.
Stawka godzinowa = (wynagrodzenie zasadnicze + stałe składniki) / wymiar miesiąca.
| Dodatek | Za nadgodziny |
|---|---|
| 100% | w nocy; w niedziele i święta niebędące dniami pracy wg rozkładu; w dniu wolnym udzielonym za niedzielę lub święto; za przekroczenie normy średniotygodniowej |
| 50% | pozostałe — dobowe w dzień roboczy |

## Praca w dniu wolnym z 5-dniowego tygodnia (sobota)
Najpierw dajesz inny dzień wolny do końca okresu rozliczeniowego (art. 151³).
Jeśli dnia wolnego nie udzieliłeś — to nadgodziny średniotygodniowe z dodatkiem 100%.

## Czas wolny zamiast dodatku
| Na czyj wniosek | Przelicznik | Kiedy |
|---|---|---|
| pracownika | 1:1 | także w kolejnym okresie rozliczeniowym |
| bez wniosku (decyzja pracodawcy) | 1:1,5 | w tym samym okresie, bez obniżenia wynagrodzenia |

## Wyjątki
- Ryczałt za nadgodziny — tylko dla stale pracujących poza zakładem; odpowiada przewidywanemu wymiarowi.
- Kadra zarządzająca i kierownicy komórek — bez prawa do dodatku. Wyjątek dla kierowników: niedziela lub święto bez dnia wolnego.

## Pora nocna
8 godzin między 21:00 a 7:00 — wskazuje regulamin.
Dodatek nocny: 20% stawki godzinowej z minimalnego wynagrodzenia (4 806 / wymiar miesiąca) za każdą godzinę.
Pracujący w nocy (≥ 3 h nocne na dobę albo ≥ 1/4 czasu w okresie) — przy pracach niebezpiecznych maksymalnie 8 h na dobę.

## Dyżur (art. 151⁵)
Dyżur jest poza godzinami pracy, w zakładzie albo w domu.
Dyżur w zakładzie bez wykonywania pracy: czas wolny albo wynagrodzenie. Za dyżur domowy — nie.
Dyżur nie może naruszać odpoczynków."""

WYJASNIENIA["ewidencja_czasu"] = """## Co zawiera ewidencja (art. 149, §6 rozporządzenia o dokumentacji)
Prowadzisz ją dla każdego pracownika odrębnie, papierowo albo elektronicznie.
- liczba przepracowanych godzin z godziną rozpoczęcia i zakończenia,
- nadgodziny, praca w porze nocnej, w niedziele i święta (z tytułem),
- dyżury — miejsce i godziny,
- dni wolne z oznaczeniem tytułu: W5, WN, WŚ, wolne za nadgodziny,
- rodzaj i wymiar zwolnień od pracy i innych usprawiedliwionych nieobecności,
- nieobecności nieusprawiedliwione,
- czas pracy młodocianego przy pracach wzbronionych.

## Dokumenty towarzyszące
Wnioski o wyjścia prywatne. Wnioski i polecenia nadgodzin. Zgody opiekunów dzieci do 8 lat i ciężarnych na delegację. Wnioski o czas wolny. Harmonogramy. Rozkłady ruchome.
Dla zadaniowego czasu pracy i kierowników komórek nie ewidencjonujesz godzin — tylko nieobecności i dni wolne.

## Lista obecności to nie ewidencja
Lista obecności jest narzędziem dyscypliny. Nie jest obowiązkowa.
Ewidencja musi pozwolić policzyć wynagrodzenie. To pierwszy dokument, o który prosi PIP.
Brak ewidencji w sądzie (sprawy o nadgodziny) daje domniemanie na korzyść pracownika.
Przechowywanie: jak akta — 10 lat po ustaniu zatrudnienia (dokumentacja z 2019+). Pracownik ma prawo wglądu i kopii.

## Kody nieobecności w praktyce
| Kod | Nieobecność | Wymiar / płatność |
|---|---|---|
| UW | urlop wypoczynkowy | — |
| UŻ | urlop na żądanie | — |
| UO | urlop opiekuńczy (art. 173¹) | 5 dni, bezpłatny |
| SW | siła wyższa (art. 148¹) | 2 dni / 16 h, 50% |
| — | opieka nad dzieckiem do 14 lat (art. 188) | 2 dni / 16 h, 100% |
| CH | choroba | — |
| OP | opieka zasiłkowa | — |
| UB | urlop bezpłatny | — |
| UOk | urlop okolicznościowy | — |
| D | delegacja | — |
| NN | nieobecność nieusprawiedliwiona | — |
Każdy rodzaj inaczej wpływa na wynagrodzenie (tydzień 6) i składki (RSA, tydzień 10).

## Trzy zasady
- Wyjście prywatne odpracowane nie jest nadgodziną (art. 151 §2¹). Odpracowanie nie może naruszać odpoczynku.
- Praca zdalna: ewidencja nadal obowiązuje.
- Praca zdalna okazjonalna (24 dni) — ewidencjonujesz osobno."""

WYJASNIENIA["urlop_wypoczynkowy"] = """## Wymiar (art. 154)
| Staż pracy | Wymiar |
|---|---|
| mniej niż 10 lat | 20 dni |
| co najmniej 10 lat | 26 dni |

## Co wlicza się do stażu urlopowego
Okresy zatrudnienia u wszystkich pracodawców. Od 2026 także zlecenia i działalność (lekcja o stażu).
Okresy nauki — bez sumowania, liczysz korzystniejszy:
| Szkoła | Lata do stażu |
|---|---|
| zasadnicza zawodowa | 3 |
| średnia zawodowa | 5 |
| średnia ogólnokształcąca | 4 |
| policealna | 6 |
| wyższa | 8 |
Nauka równoległa z pracą — liczysz korzystniejszy z okresów.

## Dni i godziny
Urlopu udzielasz w dni robocze pracownika, w godzinach. 1 dzień = 8 h (7 h przy umiarkowanej lub znacznej niepełnosprawności).
Godzinowo rozliczasz tylko część dnia — gdy pozostała część urlopu jest mniejsza niż dobowy wymiar.
Niepełny etat: wymiar proporcjonalny, zaokrąglany w górę do pełnego dnia. Przykłady: 1/2 × 26 = 13; 3/4 × 20 = 15.

## Pierwsza praca w życiu (art. 153)
W pierwszym roku: z dołu, 1/12 wymiaru za każdy przepracowany miesiąc, bez zaokrąglania w górę.
Od następnego roku kalendarzowego: z góry, cały wymiar 1 stycznia.

## Urlop proporcjonalny (art. 155¹)
- Zmiana pracodawcy w roku: u dotychczasowego za okres do ustania, u nowego za resztę.
- Niepełny miesiąc u pierwszego pracodawcy liczy się za pełny.
- Powrót po urlopie bezpłatnym dłuższym niż 1 miesiąc, po wychowawczym albo służbie — proporcja.
- Dni zaokrąglasz w górę.

## Urlop na żądanie
4 dni w roku, w puli 20/26. Zgłoszenie najpóźniej w dniu urlopu, przed rozpoczęciem pracy.
Odmowa tylko wyjątkowo — interes pracodawcy (SN).
Niewykorzystany urlop na żądanie przechodzi na rok następny jako zwykły zaległy.

## Zasady udzielania
| Zasada | Podstawa |
|---|---|
| plan urlopów albo uzgodnienie indywidualne (gdy brak związków i tak uzgodniono) | — |
| co najmniej jedna część to 14 kolejnych dni kalendarzowych | art. 162 |
| zaległy do 30 września następnego roku | — |
| zaległy w okresie wypowiedzenia można narzucić | art. 167¹ |
| polecenie wykorzystania zaległego po 30.09 | SN dopuszcza |
| przesunięcie i odwołanie z urlopu — zwrot kosztów | art. 164–167 |
| choroba przerywa urlop | — |
| ekwiwalent tylko przy ustaniu zatrudnienia | art. 171 |
Przedawnienie roszczeń: 3 lata od końca roku, w którym urlop stał się wymagalny (od 1.10 następnego roku)."""

WYJASNIENIA["staz_pracy_2026"] = """## Co się zmieniło (art. 302¹ i n. KP)
Do stażu pracy wlicza się teraz okresy pracy poza umową o pracę. Od stażu zależą: wymiar urlopu, okres wypowiedzenia u tego samego pracodawcy, odprawy, dodatki stażowe i nagrody jubileuszowe wg regulaminów.

| Wlicza się | Nie wlicza się |
|---|---|
| umowy zlecenia i o świadczenie usług objęte ubezpieczeniem emerytalno-rentowym | umowy o dzieło |
| umowy studentów do 26 lat bez ubezpieczenia — na podstawie umowy | praktyki, wolontariat |
| umowy agencyjne | działalność nierejestrowana |
| pozarolnicza działalność gospodarcza z opłaconymi składkami (także ulga na start) | zawieszenie działalności (poza opieką nad dzieckiem) |
| współpraca z przedsiębiorcą | — |
| zasiłki pobierane z tych tytułów | — |
| członkostwo w spółdzielniach rolniczych | — |
| praca za granicą w innych formach niż umowa o pracę | — |
Okresy nakładające się liczysz raz — korzystniejszy.

## Od kiedy
| Pracodawca | Wejście w życie |
|---|---|
| sektor finansów publicznych | 1.01.2026 |
| pozostali | 1.05.2026 |

## Jak pracownik dokumentuje staż
- Zaświadczenie ZUS o okresach ubezpieczenia — wniosek elektroniczny przez eZUS, bez załączników. Może obejmować wszystkie tytuły albo wybrany.
- Gdy ZUS nie ma danych — decyzja odmowna i postępowanie wyjaśniające z dowodami: umowy, faktury, zaświadczenia.
- Zleceniodawca nie ma obowiązku wystawiać potwierdzeń. Może.
- Dokumenty zagraniczne — z tłumaczeniem.

## Terminy i skutki
Pracownicy już zatrudnieni mają 24 miesiące (od 1.01 albo 1.05.2026) na dostarczenie dokumentów.
Uprawnienia nabywa się od dnia przedstawienia dokumentów, nie wcześniej niż od wejścia w życie.
Przykład: wymiar urlopu rośnie z 20 na 26 dni → w roku bieżącym przysługuje różnica (urlop uzupełniający) od dnia przedstawienia zaświadczenia.
Spory rozstrzyga sąd pracy.

## Co robi dział kadr
- Komunikat do pracowników i wzór wniosku.
- Dokumenty do akt — część B.
- Aktualizacja w programie: staż ogólny i staż zakładowy osobno.
- Przeliczenie urlopu i — jeśli regulamin przewiduje — dodatków stażowych.
- Okres wypowiedzenia wydłuża tylko zlecenie u TEGO pracodawcy.
- Limity umów na czas określony nie zmieniają się — dotyczą tylko umów o pracę."""

WYJASNIENIA["urlopy_rodzicielskie"] = """## Urlop macierzyński
| Element | Zasada |
|---|---|
| wymiar | 20 tygodni (1 dziecko); 31/33/35/37 przy porodzie mnogim |
| przed porodem | do 6 tygodni |
| obowiązkowe dla matki | 14 tygodni; resztę może przejąć ojciec |
| zasiłek | 100% |
Wcześniaki i hospitalizacja noworodka (od 19.03.2025): dodatkowy urlop macierzyński — tydzień za każdy tydzień pobytu dziecka w szpitalu, do 8 lub 15 tygodni (zależnie od tygodnia ciąży i masy). Zasiłek 100%.

## Urlop rodzicielski (art. 182¹ᵃ)
| Element | Zasada |
|---|---|
| wymiar | 41 tygodni (43 przy porodzie mnogim) łącznie dla obojga |
| część nieprzenoszalna | 9 tygodni wyłącznie dla każdego z rodziców — niewykorzystane przepadają |
| do kiedy | do końca roku kalendarzowego, w którym dziecko kończy 6 lat |
| części | do 5 |
| łączenie z pracą | do 1/2 etatu; urlop wydłuża się proporcjonalnie, maksymalnie 82 tygodnie |
| zasiłek | 70% |
| zasiłek 81,5% | gdy matka złoży wniosek o cały rodzicielski (bez 9 tygodni ojca) w 21 dni po porodzie — 81,5% za macierzyński i rodzicielski; 9 tygodni ojca zawsze 70% |
| dziecko z zaświadczeniem „Za życiem” | 65/67 tygodni |

## Urlop ojcowski
2 tygodnie, do ukończenia przez dziecko 12 miesięcy. Maksymalnie 2 części po tygodniu. Wniosek 7 dni wcześniej. Zasiłek 100%.

## Urlop wychowawczy (art. 186)
| Element | Zasada |
|---|---|
| wymiar | do 36 miesięcy; jeden rodzic maksymalnie 35, 1 miesiąc dla drugiego |
| do kiedy | do końca roku, w którym dziecko kończy 6 lat (18 — dziecko z niepełnosprawnością) |
| warunek | staż co najmniej 6 miesięcy |
| płatność | bezpłatny; wlicza się do stażu |
| części | do 5 |
| wniosek | 21 dni wcześniej, elektronicznie |
| składki | emerytalno-rentowe i zdrowotna z budżetu — ZUS RCA kod 12 11, RSA 121 |
Zamiast wychowawczego: obniżenie etatu do maksymalnie 1/2 na okres do 12 miesięcy, z ochroną.
Elastyczna organizacja pracy dla rodzica dziecka do 8 lat (art. 188¹): wniosek 21 dni wcześniej, odpowiedź w 7 dni.

## Ochrona
- Od zgłoszenia ciąży i przez urlopy macierzyński, rodzicielski i ojcowski — zakaz wypowiedzenia i rozwiązania. Wyjątki: upadłość lub likwidacja oraz art. 52 za zgodą związku.
- Umowa na czas określony albo próbna dłuższa niż 1 miesiąc, która rozwiązałaby się po 3. miesiącu ciąży — przedłuża się do porodu. Nie dotyczy zastępstwa.
- Ochrona zaczyna się 14 dni przed terminem urlopu wskazanym we wniosku (ojcowski, rodzicielski).
- Ciąża: zakaz pracy nocnej, nadgodzin i delegacji bez zgody. Przy pracach wzbronionych — zmiana warunków pracy z zachowaniem wynagrodzenia.

## Dokumenty
Wnioski w postaci papierowej lub elektronicznej (od 2023). Oświadczenia o korzystaniu z urlopu przez drugiego rodzica. Akt urodzenia. Wszystko do akt — część B."""

WYJASNIENIA["nieobecnosci_inne"] = """## Nieobecności z dyrektywy work-life balance (od 26.04.2023)
| Nieobecność | Wymiar | Płatność | Wniosek |
|---|---|---|---|
| urlop opiekuńczy (art. 173¹) — opieka lub wsparcie członka rodziny (dziecko, rodzic, małżonek) albo domownika z poważnych względów medycznych | 5 dni w roku | bezpłatny; wlicza się do stażu | najpóźniej 1 dzień przed |
| siła wyższa (art. 148¹) — pilne sprawy rodzinne: choroba, wypadek | 2 dni lub 16 h w roku | 50% wynagrodzenia liczonego jak urlopowe | najpóźniej w dniu, forma dowolna |
| opieka nad dzieckiem do 14 lat (art. 188) | 2 dni lub 16 h w roku | 100% | dla jednego z rodziców — oświadczenie |
Siła wyższa: pierwszy wniosek w roku decyduje, czy liczysz w dniach, czy w godzinach. Niepełny etat — proporcjonalnie.

## Zwolnienia okolicznościowe (rozporządzenie o usprawiedliwianiu nieobecności)
| Wymiar | Zdarzenie |
|---|---|
| 2 dni | ślub pracownika; urodzenie dziecka; zgon i pogrzeb małżonka, dziecka, ojca, matki, ojczyma, macochy |
| 1 dzień | ślub dziecka; zgon i pogrzeb siostry, brata, teściowej, teścia, babki, dziadka, innej osoby na utrzymaniu |
Wynagrodzenie jak urlopowe.

## Inne zwolnienia
| Zwolnienie | Zasada |
|---|---|
| krwiodawstwo | dzień oddania krwi |
| wezwanie do sądu, urzędu, wojska | bez wynagrodzenia od pracodawcy; zaświadczenie dla organu, który rekompensuje |
| badania ciężarnej | 100% |
| poszukiwanie pracy w wypowiedzeniu przez pracodawcę | 2 dni przy 2 tygodniach lub 1 miesiącu; 3 dni przy 3 miesiącach — 100% |
| urlop szkoleniowy | 6 dni na egzaminy; 21 dni na pracę dyplomową — 100%, gdy pracodawca kieruje lub się zgadza |
| szkolenia BHP | czas pracy |

## Urlop bezpłatny (art. 174)
- Na pisemny (od 2026 także elektroniczny) wniosek pracownika.
- Nie wlicza się do stażu. Wyjątek: urlop na pracę u innego pracodawcy za zgodą (art. 174¹).
- Dłuższy niż 3 miesiące — strony mogą przewidzieć odwołanie.
- W czasie bezpłatnego nie ma składek ani zasiłków (RSA 111).
- Bezpłatny trwający co najmniej 1 miesiąc proporcjonalnie obniża urlop wypoczynkowy po powrocie.

## Elastyczna organizacja pracy (art. 188¹)
Rodzic dziecka do 8 lat wnioskuje 21 dni wcześniej o: pracę zdalną, system przerywany, skrócony tydzień, weekendowy, ruchomy, indywidualny rozkład albo obniżenie etatu.
Pracodawca odpowiada w 7 dni. Odmowa — z uzasadnieniem (organizacja lub rodzaj pracy). Powrót — na wniosek.

## Niestawienie się bez usprawiedliwienia
Kara porządkowa. Przy nieobecności trwającej — rozważ art. 52.
„Porzucenie pracy” nie istnieje jako tryb. Rozwiązujesz umowę z art. 52 §1 pkt 1."""

WYJASNIENIA["lista_plac_krok"] = """## Osiem kroków w stałej kolejności
| Krok | Co liczysz | Jak |
|---|---|---|
| 1 | przychód brutto | wszystkie składniki wypłacone w miesiącu: zasadnicze, nadgodziny, nocne, premie, świadczenia w naturze, wpłata pracodawcy na PPK (jako przychód) |
| 2 | podstawa i składki społeczne | podstawa = przychód bez wyłączeń z rozporządzenia składkowego; składki pracownika: emerytalna 9,76%, rentowa 1,5%, chorobowa 2,45% — każda zaokrąglona do grosza; limit 30-krotności dla emerytalnej i rentowej |
| 3 | podstawa i składka zdrowotna | podstawa = podstawa społecznych − składki społeczne pracownika + wynagrodzenie chorobowe; składka 9%, nie wyższa niż hipotetyczna zaliczka wg zasad z 2021 |
| 4 | podstawa opodatkowania | przychód − składki społeczne pracownika − KUP (250/300) + PPK pracodawcy (już w przychodzie) − przychody zwolnione; zaokrąglona do pełnych złotych |
| 5 | zaliczka | 12% (lub 32% po przekroczeniu 120 000 zł dochodu narastająco) − kwota zmniejszająca (300/150/100 wg PIT-2); zaokrąglenie do pełnych złotych |
| 6 | PPK pracownika | 2% (0,5–2%) od podstawy składek — potrącane z netto |
| 7 | potrącenia | komornik, dobrowolne |
| 8 | netto | brutto − społeczne − zdrowotna − zaliczka − PPK pracownika − potrącenia |

## Co jest wyłączone ze składek (rozporządzenie składkowe)
Odprawy. Nagrody jubileuszowe co 5 lat. Ekwiwalenty za pranie. Diety do limitu. ZFŚS z kryterium socjalnym. PPK pracodawcy.
Ograniczenie zdrowotnej do hipotetycznej zaliczki jest ważne przy niskich przychodach i uldze dla młodych.
Przychody zwolnione z PIT to m.in. ulga dla młodych i ZFŚS do 1 000 zł.

## Zaokrąglenia
| Co | Jak |
|---|---|
| składki | do 1 grosza, matematycznie |
| zdrowotna | do grosza |
| podstawa opodatkowania i zaliczka | do pełnego złotego: do 49 gr w dół, od 50 gr w górę |

## Trzy składniki specjalne
| Składnik | Składki społeczne | Zdrowotna | PIT |
|---|---|---|---|
| wynagrodzenie chorobowe | nie | tak | tak |
| zasiłek | nie | nie | zaliczka 12% bez KUP, z kwotą zmniejszającą, jeśli PIT-2 |
| świadczenie w naturze (auto) | tak — dodajesz do podstaw | tak | tak; nie wypłacasz |

## Kontrola listy
- Bilans: brutto = netto + wszystkie obciążenia pracownika.
- Porównanie z poprzednim miesiącem; odchylenia powyżej 10% wyjaśniasz.
- Zgodność z ewidencją czasu pracy.
- Progi narastająco: 120 000 dochodu, 85 528 ulga dla młodych, 282 600 składki.
- Zgodność oświadczeń z kartoteką.

## Termin wypłaty (art. 85)
Stały, z dołu, do 10. dnia następnego miesiąca. Gdy to dzień wolny — poprzedni dzień roboczy.
Co najmniej raz w miesiącu. Przelew na konto; gotówka tylko na wniosek."""

WYJASNIENIA["zaliczka_pit"] = """## PIT-2 — jeden formularz od 2023
PIT-2 zbiera oświadczenia i wnioski pracownika:
| Oświadczenie / wniosek | Skutek |
|---|---|
| kwota zmniejszająca | 1/12 (300 zł), 1/24 (150 zł) lub 1/36 (100 zł) — pracownik dzieli ją między płatników |
| podwyższone KUP 300 zł | miejsce zamieszkania poza miejscowością zakładu, bez dodatku za rozłąkę |
| zamiar wspólnego rozliczenia | 12% mimo przekroczenia progu |
| ulga dla młodych | wniosek o NIEstosowanie |
| ulga na powrót | 4 lata od powrotu, do 85 528 zł |
| ulga dla rodzin 4+ | do 85 528 zł |
| ulga dla pracujących seniorów | kobiety 60+, mężczyźni 65+ bez emerytury — do 85 528 zł |
| rezygnacja z KUP | np. przy wielu etatach |
| niepobieranie zaliczek | dochód roczny do 30 000 zł |
Stosujesz od następnego miesiąca po złożeniu (albo od razu). Obowiązują do odwołania.

## Po ustaniu stosunku pracy (art. 31a ust. 7 PIT)
Przy późniejszych wypłatach płatnik POMIJA złożone oświadczenia i wnioski: bez kwoty zmniejszającej, bez podwyższonych KUP, bez ulg na oświadczenie.
Nadal stosuje tylko wnioski o niestosowanie KUP, o rezygnację z 50% KUP i o niestosowanie ulgi dla młodych.
KUP 250 i ulga dla młodych działają z mocy ustawy.

## Próg podatkowy
12% do 120 000 zł DOCHODU narastająco od początku roku. Dochód = przychód − składki społeczne − KUP.
| Moment | Stawka |
|---|---|
| miesiąc przekroczenia | 12% od części do progu, 32% od nadwyżki |
| następne miesiące | 32% |
Pracownik może wnioskować o 32% wcześniej — unika dopłaty. Kwotę zmniejszającą stosujesz także przy 32%.

## Ulga dla młodych
Przychody ze stosunku pracy, zlecenia, praktyk i zasiłku macierzyńskiego — do 85 528 zł rocznie zwolnione, do dnia 26. urodzin.
Składki ZUS normalnie. Zdrowotna ograniczona do hipotetycznej zaliczki liczonej jak bez ulgi. W praktyce przy minimalnej to ograniczenie działa.

## Zasiłki i danina
Zasiłki (chorobowy, macierzyński, opiekuńczy) to przychód z innych źródeł. Zaliczka 12% bez KUP; kwota zmniejszająca — gdy PIT-2 u tego płatnika.
Danina solidarnościowa 4% ponad 1 mln — rozlicza podatnik.

## Zmiany 2027 — projekt
Projekt uchwalony przez Sejm 22.10.2026, w Senacie z poprawkami: próg 130 000 zł, stawka 24% do 150 000 zł.
Sprawdź status przed listą za styczeń 2027."""

WYJASNIENIA["koszt_pracodawcy"] = """## Składki finansowane przez pracodawcę
| Składka | Stopa |
|---|---|
| emerytalna | 9,76% |
| rentowa | 6,5% |
| wypadkowa | 0,67–3,33% |
| FP (w tym FS 1,45%) | 2,45% |
| FGŚP | 0,10% |
| FEP — praca w szczególnych warunkach lub charakterze (wykaz) | 1,5% |
| PPK | 1,5% (do 4%) |

## Zwolnienia z FP i FGŚP
- Kobiety od 55 lat i mężczyźni od 60 lat.
- 12 miesięcy po powrocie z urlopu macierzyńskiego, rodzicielskiego lub wychowawczego.
- 36 miesięcy za osoby 50+ zatrudnione z PUP (bezrobotne); 12 miesięcy za skierowanych do 30 lat.
- Wynagrodzenie niższe niż minimalne w przeliczeniu na miesiąc (np. niepełny etat poniżej 4 806) — brak FP/FGŚP, jeśli łączna podstawa ze wszystkich tytułów jest niższa niż minimalna.

## Składka wypadkowa — skąd się bierze stopa
| Płatnik | Stopa |
|---|---|
| zgłasza do 9 ubezpieczonych | 1,67% (50% najwyższej stopy) |
| zgłasza 10 i więcej | stopa dla grupy PKD z załącznika do rozporządzenia; dla działu 10 „produkcja artykułów spożywczych” sprawdź aktualną |
| po 3 latach składania IWA | ZUS ustala indywidualnie (zawiadomienie do 20 kwietnia), korekta ±50% wg wskaźnika częstości wypadków |
Stopa obowiązuje od 1 kwietnia do 31 marca.
IWA składasz do 31 stycznia, gdy: średnio co najmniej 10 ubezpieczonych, płatnik zgłoszony cały rok, wpis w REGON.

## Pełny koszt etatu
Koszt = brutto × (1 + 9,76 + 6,5 + wypadkowa + 2,45 + 0,10)% + PPK + ZFŚS + koszty dodatkowe.
- ZFŚS: 2 943,23 zł rocznie na etat, gdy fundusz działa.
- Koszty dodatkowe: badania, BHP, odzież, szkolenia, sprzęt.
- Koszt nieobecności: wynagrodzenie chorobowe 33 dni, urlop — wynagrodzenie bez pracy.
Przykład dla 4 806 zł: 4 806 × 1,2048 = 5 790,28 zł miesięcznie (bez PPK i ZFŚS).
Zarząd pyta „ile kosztuje pracownik”. Odpowiedź: ok. 1,21–1,25 × brutto + koszty stałe.

## Porównanie form zatrudnienia
| Forma | Koszt ZUS firmy | Ryzyko |
|---|---|---|
| umowa o pracę | pełne składki | — |
| zlecenie z pełnymi składkami | tyle samo w ZUS; bez FP/FGŚP przy zbiegu; bez urlopu i 33 dni chorobowego | — |
| B2B | brak kosztów ZUS po stronie firmy | art. 22 §1¹ KP — ustalenie stosunku pracy: składki 5 lat wstecz z odsetkami, których nie potrącisz pracownikowi, urlopy, nadgodziny, PIP |
Limit 30-krotności obniża koszt w końcówce roku dla wysokich pensji — brak emerytalnej i rentowej po 282 600 zł podstawy."""

WYJASNIENIA["wynagrodzenie_urlopowe"] = """## Zasada (rozporządzenie urlopowe z 8.01.1997)
Wynagrodzenie za urlop to tyle, ile pracownik dostałby, gdyby pracował.

## Które składniki i jak
| Składnik | Jak liczysz |
|---|---|
| stałe miesięczne | w wysokości z miesiąca urlopu — nie przeliczasz; wypłacasz pensję bez zmian |
| zmienne za okresy nie dłuższe niż miesiąc (nadgodziny, nocne, premie miesięczne, prowizje) | średnia z 3 miesięcy poprzedzających miesiąc urlopu (do 12 przy znacznych wahaniach): suma składników / godziny przepracowane w tych miesiącach = stawka godzinowa; × godziny urlopu |
| za okresy dłuższe niż miesiąc (kwartalne, roczne) | nie wchodzą do urlopowego |
Zmiana stawek w okresie 3 miesięcy — przeliczasz składniki wg nowych.

## Co jest wyłączone (§6)
Jednorazowe i nieperiodyczne. Nagrody jubileuszowe. Ekwiwalenty. Odprawy. Wynagrodzenie za czas choroby i zasiłki.
Uwaga: nadgodziny WCHODZĄ — dodatek i normalne wynagrodzenie. Wyłączone jest tylko wynagrodzenie za czas gotowości i przestoju.

## Ekwiwalent (art. 171, §14–19)
Tylko przy niewykorzystaniu urlopu z powodu rozwiązania lub wygaśnięcia umowy.
| Krok | Jak |
|---|---|
| podstawa | stałe z miesiąca nabycia prawa + zmienne miesięczne (średnia z 3 miesięcy) + zmienne za okresy dłuższe niż miesiąc (średnia z 12 miesięcy) |
| stawka dzienna | podstawa / współczynnik; 2026: 20,92 = (365 − 52 niedziele − 52 soboty − 10 świąt) / 12 |
| niepełny etat | współczynnik proporcjonalnie: 1/2 → 10,46 |
| stawka godzinowa | dzienna / 8 (7 dla pracowników z niepełnosprawnością) |
| ekwiwalent | stawka godzinowa × godziny urlopu |
Termin wypłaty (od 27.01.2026, ustawa z 4.12.2025): w terminie wypłaty wynagrodzenia; gdy ten termin przypada przed ustaniem zatrudnienia — w 10 dni od ustania.
Ekwiwalent: składki i PIT jak wynagrodzenie.

## Wynagrodzenie za część miesiąca (rozporządzenie o wynagrodzeniu z 29.05.1996)
| Powód | Jak pomniejszasz pensję stałą |
|---|---|
| choroba, zasiłek (§11) | pensja / 30 × dni kalendarzowe nieobecności |
| inne nieobecności bez prawa do wynagrodzenia — bezpłatny, nieusprawiedliwiona (§12) | pensja / wymiar godzin miesiąca × godziny nieobecności |
| zatrudnienie lub zwolnienie w trakcie miesiąca | pensja / wymiar × godziny przepracowane |
Składników zmiennych (nadgodziny) nie pomniejszasz — są za faktyczną pracę."""

WYJASNIENIA["potracenia"] = """## Bez zgody pracownika (art. 87 §1) — kolejność
1. Sumy egzekwowane na alimenty.
2. Inne tytuły wykonawcze (komornik).
3. Zaliczki pieniężne udzielone pracownikowi.
4. Kary pieniężne z art. 108.

## Granice i kwoty wolne
Granice liczysz po odliczeniu składek ZUS, zaliczki PIT i wpłat PPK pracownika.
| Potrącenie | Maksymalnie | Kwota wolna (art. 87¹) |
|---|---|---|
| alimenty | 3/5 | brak |
| inne tytuły wykonawcze | 1/2 | 100% minimalnego netto |
| alimenty + inne łącznie | 3/5 | — |
| zaliczki pieniężne | — | 75% minimalnego netto |
| kary pieniężne | 1/10 wynagrodzenia po innych potrąceniach | 90% minimalnego netto |
Minimalne netto liczysz dla danego pracownika — po odliczeniu jego składek, PIT i PPK. Dla różnych osób jest różne.
Niepełny etat: kwoty wolne proporcjonalnie.
Nagroda z ZFŚS, trzynastka, nagroda jubileuszowa — na alimenty do 100%.

## Procedura przy zajęciu komorniczym
- Komornik doręcza zajęcie. Od tej chwili potrącasz i przekazujesz.
- W 7 dni odpowiadasz (art. 882 KPC): wynagrodzenie za 3 miesiące, inne zajęcia, przeszkody.
- Zbieg egzekucji: informujesz obu komorników, przekazujesz temu, który pierwszy zajął.
- Ustanie zatrudnienia: zawiadamiasz komornika, wpisujesz zajęcie w świadectwie (komornik, sygnatura, kwota).
- Za nieprzekazanie: grzywna do 5 000 zł od komornika i odpowiedzialność za szkodę.
Zajęcie zasiłków z ZUS, gdy płatnik je wypłaca — limity z ustawy emerytalnej: alimenty 60%, inne 25%, kwota wolna jak w emeryturach.

## Za zgodą pracownika (art. 91)
Tylko pisemna zgoda z konkretną kwotą lub tytułem: pożyczka z ZFŚS, składka związkowa, ubezpieczenie grupowe.
| Na czyją rzecz | Kwota wolna |
|---|---|
| inne podmioty | 100% minimalnego netto |
| pracodawca | 80% minimalnego netto |

## Co nie jest potrąceniem
Nadpłacone wynagrodzenie za okres nieobecności odliczasz w najbliższym terminie wypłaty (art. 87 §7). Tylko za okres nieobecności, nie za „pomyłkę”.
Zwykłą nadpłatę odzyskujesz za zgodą pracownika albo sądownie."""

WYJASNIENIA["swiadczenia_pozaplacowe"] = """## Zasada
Przychód ze stosunku pracy (art. 12 PIT) to także świadczenia w naturze i nieodpłatne.
Składki ZUS od nich są — chyba że rozporządzenie składkowe je wyłącza (§2 ust. 1).

## Wyłączenia ze składek (§2 ust. 1 rozporządzenia składkowego)
- nagrody jubileuszowe nie częściej niż co 5 lat,
- odprawy,
- ekwiwalenty za narzędzia, pranie, używanie własnej odzieży,
- diety i zwrot kosztów podróży do limitów,
- ryczałt za auto prywatne do limitu kilometrówki,
- świadczenia z ZFŚS zgodne z ustawą,
- korzyści materialne z układu lub regulaminu polegające na zakupie po cenie niższej niż detaliczna — np. współfinansowane karty sportowe i pakiety medyczne.
Współfinansowanie: pracownik dopłaca choć 1 zł — składek brak, PIT jest.

## Wycena świadczeń
| Świadczenie | Wartość do przychodu | ZUS | PIT |
|---|---|---|---|
| pakiet, karta | cena zakupu (minus dopłata pracownika) | nie, gdy współfinansowanie wg regulaminu | tak |
| auto służbowe do celów prywatnych | ryczałt 250 zł (≤ 60 kW lub elektryczny/wodorowy) albo 400 zł (pozostałe); za dzień 1/30; obejmuje paliwo (NSA) | tak | tak |
| auto bez używania prywatnego | nie jest przychodem przy właściwej ewidencji i regulaminie | — | — |
| ubezpieczenie grupowe opłacane przez pracodawcę; pakiet medyczny poza medycyną pracy | wartość | tak, chyba że współfinansowanie wg regulaminu | tak |
| ubezpieczenie OC/NNW w interesie pracodawcy | nie jest przychodem | — | — |

## Zwolnienia z PIT
| Świadczenie | Limit |
|---|---|
| posiłki, bony (art. 21 ust. 1 pkt 11b) | do 450 zł miesięcznie |
| ekwiwalent za pranie, narzędzia | — |
| ryczałt za pracę zdalną | odpowiadający kosztom |
| dokształcanie z inicjatywy pracodawcy | — |
| świadczenia z ZFŚS — pieniężne i rzeczowe, bez bonów | do 1 000 zł rocznie |
| zapomogi losowe | z ZFŚS bez limitu; z innych źródeł do 6 000 |

## ZFŚS na liście płac
Świadczenie przyznajesz tylko z kryterium socjalnym: sytuacja życiowa, rodzinna, materialna — oświadczenie o dochodach na osobę.
Wtedy: bez ZUS; bez PIT do 1 000 zł; nadwyżka — PIT, bez ZUS.
„Po równo” albo według stanowiska lub stażu — ZUS doliczy składki w kontroli. To najczęstsze ustalenie kontroli.
| Wiersz na liście | Co zmienia |
|---|---|
| świadczenie ZFŚS | podstawę PIT ponad limit; składek nie |
| świadczenie w naturze z firmy | zwiększa podstawy ZUS i PIT; nie jest wypłacane — netto maleje o obciążenia |"""

WYJASNIENIA["chorobowe_podstawy"] = """## Dwa źródła pieniędzy za chorobę
| Świadczenie | Kto płaci | Za jaki okres | Wysokość |
|---|---|---|---|
| wynagrodzenie chorobowe (art. 92 KP) | pracodawca | pierwsze 33 dni niezdolności w roku kalendarzowym; 14 dni dla osób po 50. roku życia (od roku następnego po 50. urodzinach) | 80% podstawy; 100%: choroba w ciąży, wypadek w drodze do lub z pracy, badania i zabiegi dawcy |
| zasiłek chorobowy (ustawa zasiłkowa z 25.06.1999) | ubezpieczenie chorobowe | od 34. (15.) dnia | 80%; 100% — ciąża, wypadek w drodze, dawca; 80% za pobyt w szpitalu (od 2022) |
| zasiłek z ubezpieczenia wypadkowego | ubezpieczenie wypadkowe | od 1. dnia — wypadek przy pracy, choroba zawodowa | 100%; bez wynagrodzenia chorobowego, bez wyczekiwania |
Dni liczysz KALENDARZOWE — także soboty i święta — ze wszystkich zwolnień w roku. Wliczasz też zwolnienia u poprzedniego pracodawcy w tym samym roku (dane ze świadectwa pracy).
Reforma „ZUS płaci od 1. dnia” to nadal projekt (XI 2026). Pracodawca płaci 33/14 dni.

## Kto wypłaca zasiłek
| Płatnik | Warunek |
|---|---|
| pracodawca (płatnik składek) | na 30 listopada poprzedniego roku zgłaszał do chorobowego ponad 20 osób; ustalasz raz na rok; nowi płatnicy — wg stanu w pierwszym miesiącu |
| ZUS | pozostali — na podstawie Z-3 (pracownik) lub Z-3a (zleceniobiorca) wysłanego przez płatnika w eZUS |
Płatnik wypłaca w terminach wypłaty wynagrodzeń, nie później niż 30 dni od złożenia dokumentów. Wypłacone zasiłki rozliczasz w DRA — pomniejszają składki do zapłaty.

## Okres wyczekiwania
| Ubezpieczenie | Wyczekiwanie |
|---|---|
| obowiązkowe | 30 dni nieprzerwanego ubezpieczenia |
| dobrowolne (zlecenie) | 90 dni |
| bez wyczekiwania | absolwenci w 90 dni od ukończenia szkoły; 10 lat obowiązkowego ubezpieczenia; posłowie; wypadek w drodze |

## Okres zasiłkowy
182 dni; 270 dni — ciąża, gruźlica.
Do jednego okresu wliczasz wszystkie niezdolności bez przerwy oraz z przerwą do 60 dni. Od 2022 — niezależnie od tego, czy to ta sama choroba. Wyjątek: ciąża po innej chorobie liczy się od nowa.
Po wyczerpaniu: świadczenie rehabilitacyjne albo renta.
Świadczenie rehabilitacyjne: do 12 miesięcy; 90% przez 3 miesiące, potem 75%; 100% w ciąży. Wniosek ZNp-7 składasz 6 tygodni przed końcem 182 dni. Orzeka lekarz orzecznik ZUS.

## e-ZLA i kody
Lekarz wystawia zwolnienie elektronicznie. Płatnik widzi je w eZUS (zakładka Zaświadczenia lekarskie). Pracownik nie musi nic dostarczać.
| Kod | Znaczenie |
|---|---|
| A | niezdolność po przerwie do 60 dni — ta sama choroba |
| B | ciąża |
| C | nadużycie alkoholu — brak zasiłku za 5 pierwszych dni |
| D | gruźlica |
| E | choroba po ustaniu tytułu |
Nieobecność 1–3 dni bez e-ZLA to nieobecność nieusprawiedliwiona. Lekarz może wystawić zwolnienie do 3 dni wstecz — z uzasadnieniem medycznym.

## Zasiłek po ustaniu zatrudnienia
Przysługuje, gdy niezdolność powstała w czasie ubezpieczenia i trwa po nim, albo powstała do 14 dni po ustaniu i trwa co najmniej 30 dni. Wypłaca ZUS.
Nie przysługuje, gdy osoba ma inny tytuł, zasiłek dla bezrobotnych, emeryturę, rentę albo działalność.

## Obliczanie i ujęcie na liście
Stawka dzienna = podstawa / 30. Świadczenie = stawka dzienna × % × dni kalendarzowe niezdolności.
| Świadczenie | Charakter | Składki społeczne | Zdrowotna | PIT |
|---|---|---|---|---|
| wynagrodzenie chorobowe | przychód ze stosunku pracy | nie | tak | tak |
| zasiłek | inne źródła | nie | nie | tak |
Oba pomniejszają pensję przez 1/30."""

WYJASNIENIA["podstawa_zasilku"] = """## Z czego liczysz podstawę (art. 36 ustawy zasiłkowej)
Podstawa = przeciętne miesięczne wynagrodzenie WYPŁACONE za 12 miesięcy kalendarzowych poprzedzających miesiąc powstania niezdolności.
| Sytuacja | Okres |
|---|---|
| zatrudnienie krótsze niż 12 miesięcy | pełne miesiące kalendarzowe |
| niezdolność w pierwszym miesiącu | wynagrodzenie, które pracownik by osiągnął: stałe — z umowy; zmienne — średnia innych pracowników na takim stanowisku |
| zmiana wymiaru etatu w okresie 12 miesięcy | tylko wynagrodzenie po zmianie |
„Wynagrodzenie” = przychód stanowiący podstawę składki chorobowej po odliczeniu składek finansowanych przez pracownika (13,71%). Przy podstawie ponad 30-krotność w danym miesiącu odliczasz tylko faktyczne składki.
Minimum dla pełnego etatu: minimalne wynagrodzenie po odliczeniu 13,71% — 2026: 4 806 × 86,29% = 4 147,10 zł. Niepełny etat — proporcjonalnie.
Nowej podstawy nie ustalasz, jeśli między okresami pobierania zasiłków (dowolnego rodzaju) nie było przerwy albo przerwa była krótsza niż miesiąc kalendarzowy (art. 43). To ważne przy chorobie po macierzyńskim.

## Które składniki wchodzą (art. 41)
Wliczasz składniki, które są POMNIEJSZANE za okres choroby.
| Zapis w regulaminie lub umowie | Wliczasz? |
|---|---|
| pomniejszany proporcjonalnie | tak |
| „zachowuje prawo w pełnej wysokości” | nie |
| brak zapisu | tak — z mocy prawa składnik za czas choroby nie przysługuje |
Nie wliczasz:
- składników, do których pracownik zachowuje prawo w okresie choroby (dodatek stażowy wypłacany w całości),
- składników przysługujących tylko do określonego terminu, zakończonych przed niezdolnością,
- premii i nagród uznaniowych wypłacanych w pełnej wysokości mimo choroby (brak reguły pomniejszania i faktyczna wypłata — ZUS: nie wliczasz),
- nagród jubileuszowych, ekwiwalentów, odpraw — nie są podstawą składki chorobowej.

| Składnik | Jak wchodzi do podstawy |
|---|---|
| nadgodziny, dodatki nocne, premie miesięczne | w miesiącu wypłaty |
| premie kwartalne | 1/12 sumy wypłaconej za 4 kwartały poprzedzające miesiąc |
| premie roczne | 1/12 kwoty za rok poprzedzający |
| wypłacone zaliczkowo | w wysokości zaliczki |

## Uzupełnianie i wyłączanie miesięcy (art. 37–38)
| Miesiąc, w którym pracownik przepracował… | Co robisz |
|---|---|
| mniej niż połowę obowiązującego czasu pracy z przyczyn usprawiedliwionych (choroba, urlop bezpłatny, opieka) | WYŁĄCZASZ z 12 miesięcy |
| co najmniej połowę | UZUPEŁNIASZ |
Jak uzupełniasz: składniki stałe — do pełnej miesięcznej kwoty z umowy (po 13,71%); zmienne (godzinowe, akord) — faktyczne / dni przepracowane × dni obowiązujące.
Nieobecności nieusprawiedliwione — nie uzupełniasz. Urlop wypoczynkowy i inne płatne nieobecności traktujesz jak dni przepracowane.
Jeśli wszystkie miesiące są wyłączone — bierzesz wynagrodzenie z miesięcy niepełnych, uzupełnione.

## Zleceniobiorcy i inne zasiłki
- Zleceniobiorca: 12 miesięcy przychodu, bez uzupełniania; minimalna podstawa 31,40 × godziny; zbieg tytułów z wyłączeniem.
- Dobrowolne chorobowe: podstawa miesięczna maksymalnie 250% prognozowanego przeciętnego wynagrodzenia — 2026: 23 550 zł.
- Świadczenie rehabilitacyjne i zasiłek macierzyński: te same zasady. Rehabilitacyjne — waloryzacja wskaźnikiem kwartalnym, gdy przekracza 100%."""

WYJASNIENIA["zasilki_inne"] = """## Zasiłek opiekuńczy (art. 32–35) — 80% podstawy
| Nad kim opieka | Limit dni w roku |
|---|---|
| zdrowe dziecko do 8 lat (zamknięcie żłobka lub szkoły, choroba niani lub opiekuna, poród lub choroba małżonka opiekującego się) | 60 |
| chore dziecko do 14 lat | 60 |
| chory inny członek rodziny we wspólnym gospodarstwie (małżonek, rodzice, dziecko powyżej 14 lat, teściowie, dziadkowie, rodzeństwo) | 14 |
| chore dziecko z niepełnosprawnością 14–18 lat; zdrowe dziecko z niepełnosprawnością do 18 lat przy chorobie opiekuna | 30 |
Łącznie nie więcej niż 60 dni w roku na wszystkich uprawnionych — oboje rodziców razem.
Zasiłek nie przysługuje, gdy inny domownik może zapewnić opiekę. Wyjątek: dziecko do 2 lat.
Dokumenty: e-ZLA na opiekę (lekarz wpisuje PESEL dziecka); wniosek Z-15A (dziecko) lub Z-15B (inny członek rodziny) — oświadczenie, kto jeszcze się opiekuje.
Dodatkowy zasiłek opiekuńczy dla ojca: do 8 tygodni, gdy matka jest w szpitalu w okresie macierzyńskiego.

## Zasiłek macierzyński
Wypłaca płatnik zasiłków albo ZUS. Podstawa — jak przy chorobowym. Bez wyczekiwania.
Dokumenty: skrócony akt urodzenia, wniosek o urlop (termin 21 dni dla 81,5%), oświadczenie o wykorzystaniu przez drugiego rodzica.
Przysługuje też po ustaniu zatrudnienia — umowa przedłużona do porodu, likwidacja.

## Wypadek przy pracy
Definicja: zdarzenie nagłe, z przyczyny zewnętrznej, powodujące uraz lub śmierć, w związku z pracą. Także w delegacji i w drodze między zakładami.
| Krok | Termin |
|---|---|
| zespół powypadkowy (BHP + SIP lub przedstawiciel) → protokół | 14 dni |
| karta wypadku dla zleceniobiorców | 14 dni |
| zatwierdzenie protokołu | 5 dni |
| kopia dla ZUS i poszkodowanego; rejestr wypadków; karta GUS Z-KW | — |
| PIP i prokuratura — wypadek śmiertelny, ciężki, zbiorowy | natychmiast |
Świadczenia: zasiłek z ubezpieczenia wypadkowego 100% od 1. dnia (bez wyczekiwania, także zleceniobiorca bez chorobowego); jednorazowe odszkodowanie z ZUS (za % uszczerbku — stawki roczne); renta wypadkowa.
Brak świadczeń: wina umyślna albo rażące niedbalstwo poszkodowanego jako wyłączna przyczyna; nietrzeźwość.
Wypadek w drodze do lub z pracy: karta wypadku w drodze (14 dni); 100% z ubezpieczenia chorobowego — wynagrodzenie chorobowe 100% + zasiłek 100%.
Choroba zawodowa — wykaz, orzeczenie PIS.

## Dokumenty dla ZUS, gdy ZUS wypłaca
| Dokument | Dla kogo |
|---|---|
| Z-3 z informacją o składnikach z 12 miesięcy | pracownik |
| Z-3a | zleceniobiorca |
| Z-3b | działalność |
| ZAS-12 | zaświadczenie płatnika w szczególnych przypadkach |
Wysyłasz w eZUS. ZUS ustala i wypłaca w 30 dni.

## Kody przerw w RSA (wybór)
| Kod | Znaczenie |
|---|---|
| 111 | urlop bezpłatny |
| 121 | urlop wychowawczy |
| 151 | usprawiedliwiona nieobecność bez wynagrodzenia (np. opiekuńczy art. 173¹) |
| 152 | nieusprawiedliwiona nieobecność |
| 155 | niezdolność bez prawa do wynagrodzenia (wyczekiwanie) |
| 311 | zasiłek macierzyński — obecnie rozbity: 327 za urlop macierzyński, 319 rodzicielski, 325 ojcowski |
| 312 | zasiłek opiekuńczy |
| 313 | zasiłek chorobowy z ubezpieczenia chorobowego |
| 314 | zasiłek chorobowy z ubezpieczenia wypadkowego |
| 321 | świadczenie rehabilitacyjne |
| 331 | wynagrodzenie za czas niezdolności finansowane przez pracodawcę |
W RSA podajesz: okres od–do, liczbę dni, kwotę (dla zasiłków wypłaconych przez płatnika).
Aktualny wykaz kodów: zus.pl → „Kody wykorzystywane przy wypełnianiu dokumentów”."""

WYJASNIENIA["kontrola_l4_2026"] = """## Trzy daty reformy (ustawa z 18.12.2025, Dz.U. 2026 poz. 26)
| Data | Co weszło w życie |
|---|---|
| 27.01.2026 | część przepisów |
| 13.04.2026 | zasadnicze zmiany w kontroli |
| 1.01.2027 | oznaczanie tytułu ubezpieczenia na e-ZLA |

## Co się zmieniło
| Pojęcie | Nowa zasada |
|---|---|
| praca zarobkowa | każda aktywność zmierzająca do uzyskania przychodu — także bez wynagrodzenia i w innej formie niż umowa |
| co NIE jest pracą zarobkową | aktywność incydentalna wymuszona okolicznościami (podpisanie dokumentu, którego nie można było odłożyć); czynności niezbędne do zachowania działalności gospodarczej bez aktywnego zarządzania; czynności z pełnienia funkcji społecznych lub publicznych |
| aktywność niezgodna z celem zwolnienia (zamiast „wykorzystywania niezgodnie z celem”) | zachowania mogące wydłużyć niezdolność: remont, wyjazd rekreacyjny, prace fizyczne |
| co jest dozwolone | czynności życia codziennego: zakupy, wizyta lekarska, opieka nad dzieckiem |
| kto ocenia | ZUS i płatnik — czy aktywność jest zgodna z zaleceniami lekarskimi; może ocenić orzecznik |
| praca u drugiego pracodawcy | od 2027 lekarz oznaczy tytuł na e-ZLA; w 2026 praca u drugiego tylko gdy lekarz wystawił zwolnienie wyłącznie na jeden tytuł |

## Kto kontroluje i jak
| Element | Zasada |
|---|---|
| płatnik zgłaszający powyżej 20 ubezpieczonych | kontroluje sam — imienne upoważnienie; osoba kontrolująca może być spoza firmy |
| pozostali płatnicy | kontrolę prowadzi ZUS; ZUS może też kontrolować na wniosek płatnika |
| miejsce | miejsce zamieszkania lub pobytu z e-ZLA albo inne miejsce; także wezwanie do stawienia się |
| obowiązek ubezpieczonego | podaje adres pobytu; zmianę zgłasza w 3 dni |
| wezwanie na badanie przez ZUS | także przez eZUS, telefon, SMS |
| protokół | ubezpieczony wnosi uwagi w 3 dni |
| spór | ZUS rozstrzyga decyzją; odwołanie do sądu w miesiąc |

## Sankcje
- Utrata prawa do zasiłku i wynagrodzenia chorobowego (art. 92 §3 KP odsyła do zasad zasiłkowych) za cały okres zwolnienia, w którym stwierdzono naruszenie.
- Sfałszowane ZLA: zwrot świadczenia i odpowiedzialność karna.
- Pracodawca może rozwiązać umowę z art. 52. SN: praca zarobkowa na L4 może być ciężkim naruszeniem.
Kontrola prawidłowości ORZEKANIA (czy pracownik faktycznie jest chory) — tylko lekarz orzecznik ZUS. Płatnik może wnioskować. Niestawienie się na badanie = utrata zasiłku od dnia badania.

## Procedura w firmie
- Regulamin kontroli: kto, jak, protokół.
- Upoważnienie imienne (wzór ZUS). Dwie osoby. Kontrola bez uprzedzenia.
- Dokumentacja: protokół z opisem zastanej sytuacji, oświadczenie pracownika; zdjęcia tylko za zgodą.
- Nieobecność w domu nie przesądza — pracownik może wyjaśnić (wizyta lekarska, apteka).
- Wynik: brak naruszeń albo naruszenie → wstrzymanie wypłaty i informacja do ZUS; gdy ZUS płaci — wniosek o kontrolę lub decyzję.
- Kadry nie decydują o „chorobie”. Decydują o zachowaniu.
- Dane z kontroli — RODO: minimalizacja, dostęp dla uprawnionych, retencja jak dokumentacja zasiłkowa.
Od 2026 ZUS prowadzi także kontrole formalne e-ZLA — czy nie wystawiono wstecz nieprawidłowo.
Statystyki ZUS: w 2025 r. wstrzymano lub obniżono świadczenia na ponad 200 mln zł. Kontrola jest realna."""

WYJASNIENIA["zlecenie_dzielo"] = """## Zlecenie — jakie składki
Zlecenie (także umowa o świadczenie usług i agencyjna) jest tytułem do ubezpieczeń.
| Ubezpieczenie | Charakter |
|---|---|
| emerytalne, rentowe, wypadkowe | obowiązkowe |
| chorobowe | dobrowolne — na wniosek (kod 04 11) |
| zdrowotne | obowiązkowe |
| FP, FGŚP | tak, gdy podstawa ze wszystkich tytułów ≥ minimalna |
Podstawa = przychód przy wynagrodzeniu kwotowym — jak u pracownika.

## Zbiegi tytułów — sześć sytuacji
| Sytuacja | Składki ze zlecenia |
|---|---|
| uczeń lub student do 26 lat | brak; nie zgłaszasz do ZUS; zaświadczenie lub legitymacja do dokumentacji; po utracie statusu — składki od następnego dnia |
| zlecenie z WŁASNYM pracodawcą (lub na jego rzecz) | jak stosunek pracy: pełne składki, sumowane z etatem (RCA kod 01 10 z łączną podstawą); podstawa zasiłku łączona |
| zlecenie + etat u INNEGO pracodawcy z wynagrodzeniem ≥ minimalne (4 806 w przeliczeniu na miesiąc) | tylko zdrowotna (kod 04 11, oświadczenie zleceniobiorcy); gdy etat < minimalnej — pełne składki |
| kilka zleceń | sumujesz podstawy chronologicznie: dopóki suma wcześniejszych < 4 806 — pełne składki; od zlecenia, przy którym suma poprzednich ≥ 4 806 — tylko zdrowotna; zleceniobiorca może wybrać tytuł |
| emeryt lub rencista | pełne składki |
| własna działalność + zlecenie w zakresie działalności | składki z działalności; zlecenie jako przychód firmy, faktura |
Oświadczenia o innych tytułach i ich aktualizacje to podstawa Twojej decyzji. Za nieprawdę odpowiada zleceniobiorca.

## Zlecenie — PIT
| Element | Zasada |
|---|---|
| źródło | działalność wykonywana osobiście (art. 13 pkt 8) |
| KUP | 20% od (przychód − składki społeczne); 50% przy przeniesieniu praw autorskich (limit 120 000 zł rocznie) |
| zaliczka | 12%; zleceniobiorca może złożyć PIT-2 — kwota zmniejszająca 300 zł, jeśli nie korzysta u innego płatnika; może wnioskować o 32% |
| umowy do 200 zł z osobą niebędącą pracownikiem | ryczałt 12% bez KUP (PIT-8AR); składki normalnie |
| ulga dla młodych | obejmuje zlecenia — do 26 lat zero PIT |
| nierezydent bez certyfikatu | ryczałt 20% (IFT-1R) |
| informacja | PIT-11 do końca lutego |

## Minimalna stawka godzinowa
31,40 zł w 2026 (32,30 zł w 2027). Dotyczy zleceń i usług wykonywanych przez osoby fizyczne, także samozatrudnionych bez pracowników.
- Obowiązek POTWIERDZANIA LICZBY GODZIN — ewidencja w formie ustalonej w umowie. Brak ewidencji to wykroczenie: PIP 1 000–30 000 zł.
- Wypłata co najmniej raz w miesiącu przy umowach dłuższych. Zakaz zrzeczenia się.
- Wyjątki: wynagrodzenie wyłącznie prowizyjne przy samodzielnym ustalaniu czasu i miejsca; opieka domowa w rodzinnych domach pomocy itp.

## Dzieło
Dzieło to REZULTAT — konkretny i weryfikowalny: projekt, tłumaczenie, utwór, raport.
Czynności to nie dzieło: szkolenia, sprzątanie, obsługa, wykłady cykliczne, pilnowanie. ZUS i SN przekwalifikowują je na zlecenie — z 5-letnią zaległością składek.
| Element | Zasada |
|---|---|
| składki | brak; wyjątek: dzieło z własnym pracodawcą — pełne składki jak etat |
| PIT | KUP 20%/50%, zaliczka 12%, ryczałt do 200 zł |
| ZUS RUD | zgłoszenie w 7 dni od zawarcia — dzieło z osobą, która nie jest Twoim pracownikiem; nie dotyczy dzieł w ramach działalności wykonawcy; przez eZUS; brak RUD to wykroczenie |
| dokumentacja rezultatu | rachunek do umowy, protokół odbioru, licencja lub przeniesienie praw |

## Wspólne dla obu umów
RODO (klauzula). BHP — bezpieczne warunki (art. 304 KP). Zakaz zastępowania etatu (art. 22 §1²). PIP sprawdza umowy cywilnoprawne."""

WYJASNIENIA["ppk"] = """## Kogo dotyczy (ustawa z 4.10.2018)
Obowiązek ma każdy podmiot zatrudniający. Wyjątki: mikroprzedsiębiorca, u którego wszyscy zrezygnowali; osoba fizyczna zatrudniająca w celach niezwiązanych z działalnością.
Dwie umowy: o ZARZĄDZANIE z instytucją finansową (wybór w porozumieniu ze związkami lub reprezentacją) i o PROWADZENIE w imieniu osób zatrudnionych.
Osoby zatrudnione: pracownicy, zleceniobiorcy z obowiązkowymi składkami emerytalno-rentowymi, członkowie rad nadzorczych, rolnicze spółdzielnie.

| Wiek | Zapis |
|---|---|
| 18–55 lat | automatycznie — po 3 miesiącach zatrudnienia, do 10. dnia miesiąca następującego po upływie 90 dni; okresy u tego pracodawcy z 12 miesięcy sumujesz |
| 55–70 lat | na wniosek |
| 70+ | nie |

## Rezygnacja i autozapis
- Rezygnacja: pisemna deklaracja (wzór z rozporządzenia) składana pracodawcy. Od następnego miesiąca brak wpłat.
- Autozapis co 4 lata: pracodawca do końca lutego informuje; od 1 kwietnia (2023, 2027, 2031) wznawia wpłaty za każdego, kto nie złożył nowej deklaracji.
- Powrót możliwy w każdej chwili — wniosek.
Sankcje: nakłanianie do rezygnacji — grzywna do 1,5% funduszu wynagrodzeń; brak umowy o zarządzanie — grzywna do 1 mln zł. PFR weryfikuje (wezwania).

## Wpłaty
Podstawa = wynagrodzenie = podstawa składek emerytalno-rentowych, BEZ limitu 30-krotności. Zasiłki nie wchodzą.
| Wpłata | Podstawowa | Dodatkowa |
|---|---|---|
| pracownika | 2%; obniżenie do 0,5%, gdy wynagrodzenie z różnych źródeł w miesiącu ≤ 120% minimalnego = 5 767,20 zł w 2026 (deklaracja) | do 2% |
| pracodawcy | 1,5% | do 2,5%; może różnicować stażem lub regulaminem |
| Wpłata | Skutek |
|---|---|
| pracownika | potrącana z netto (po PIT) |
| pracodawcy | przychód pracownika do PIT w miesiącu przekazania do instytucji; bez składek ZUS; koszt uzyskania dla firmy |
Termin: naliczenie w miesiącu wypłaty, przekazanie do instytucji do 15. dnia miesiąca następnego (plik z systemu kadrowego → portal instytucji).
Państwo dokłada: wpłatę powitalną 250 zł (po 3 miesiącach uczestnictwa) i dopłatę roczną 240 zł — gdy wpłaty w roku ≥ 3,5% × 6 × minimalne; przy obniżonej 0,5% wystarczy 25% tej kwoty.
Zmiana pracy: środki zostają; nowy pracodawca dostaje informację o rachunkach i robi transfer, chyba że pracownik się sprzeciwi.

## Wypłata środków
| Kiedy | Zasady |
|---|---|
| po 60. roku życia | 25% jednorazowo i 75% w co najmniej 120 ratach — bez podatku; mniej rat → 19% od zysków |
| wcześniej — ZWROT | minus 30% wpłat pracodawcy (idzie na konto ZUS), 19% od zysków, bez dopłat państwa |
| wkład własny | do 45 lat, zwrot w 15 lat |
| poważne zachorowanie | 25% bez zwrotu |
| inne | świadczenie małżeńskie, dziedziczenie |

## Obowiązki kadr co miesiąc
- Lista uczestników i stawek.
- Wpłaty w liście płac — 3 wiersze: pracownik, pracodawca, PIT od wpłaty pracodawcy.
- Plik do instytucji.
- Korekty — zwrot nienależnych wpłat (np. po rezygnacji złożonej przed wypłatą).
- Ewidencja deklaracji (akta B).
- Terminy: zapis nowego w 3 miesiące; informacja o autozapisie do końca lutego 2027; wniosek 55+.
PPK ≠ PPE. PPE to pracowniczy program emerytalny, dobrowolny; składka pracodawcy ≥ 3,5% zwalnia z PPK przy 25% uczestnictwie."""

WYJASNIENIA["cudzoziemcy_b2b"] = """## Cudzoziemcy — ustawa z 20.03.2025 (Dz.U. 2025 poz. 621, od 1.06.2025)
| Element | Zasada |
|---|---|
| wnioski | wyłącznie elektronicznie przez praca.gov.pl |
| test rynku pracy (informacja starosty) | zniesiony |
| zezwolenie na pracę | wydaje wojewoda; typy A–E; A — praca u polskiego pracodawcy, do 3 lat |
| odmowa | zaległości ZUS/PIT, karalność za nielegalne zatrudnienie, firma fikcyjna |
| obowiązki pracodawcy | umowa na piśmie z tłumaczeniem na język zrozumiały; kopia zezwolenia dla cudzoziemca; zgłoszenie w 7 dni do urzędu niepodjęcia lub zakończenia pracy |
| zmiana stanowiska lub wymiaru | nowe zezwolenie; wyjątki: obniżenie wymiaru, podwyżka — informacja |
| oświadczenie o powierzeniu pracy (PUP, do 24 miesięcy) | obywatele Armenii, Białorusi, Gruzji, Mołdawii, Ukrainy; wpis w 7 dni roboczych |
Zwolnieni z zezwolenia: obywatele UE/EOG/Szwajcarii, posiadacze zezwolenia na pobyt stały lub rezydenta UE, Karty Polaka, studenci stacjonarni, absolwenci polskich uczelni, małżonkowie obywateli PL.

## Obywatele Ukrainy — specustawa z 12.03.2022
Legalny pobyt (status UKR) przedłużany kolejnymi nowelizacjami — ostatnio do 4.03.2026 z zapowiedzią kolejnego przedłużenia lub przejścia na CUKR. Sprawdź aktualną datę.
Praca na podstawie POWIADOMIENIA PUP w 14 dni od podjęcia (praca.gov.pl). Warunki: wynagrodzenie nie niższe niż w powiadomieniu i co najmniej minimalne; wymiar nie niższy. Od 2025 obowiązek umowy pisemnej i zgłoszenia do ZUS.

## Kary i dokumenty
Nielegalne powierzenie pracy: grzywna 3 000–50 000 zł; przy wielokrotności i wyzysku — przestępstwo.
Pracodawca sprawdza i kopiuje dokument pobytowy (wiza, karta pobytu, paszport). Kopia w aktach przez cały okres zatrudnienia (art. 2 ust. 3 ustawy o skutkach powierzania pracy niezgodnie z przepisami). Monitorujesz terminy ważności.

## ZUS i PIT cudzoziemca
| Element | Zasada |
|---|---|
| ZUS | jak Polacy: ZUA, kod 01 10, obywatelstwo w zgłoszeniu |
| rezydent (centrum interesów lub ponad 183 dni) | PIT jak Polak |
| nierezydent na etacie | zaliczka na zasadach ogólnych; PIT-11 z adresem zagranicznym |
| nierezydent na zleceniu | ryczałt 20% (IFT-1R), chyba że certyfikat rezydencji i umowa o unikaniu podwójnego opodatkowania |
| PESEL | obowiązkowy do rozliczeń (urząd gminy) |

## Delegowanie z Polski i praca zdalna z zagranicy
- A1 z ZUS (przez eZUS US-3/US-4) na okres do 24 miesięcy.
- Zasady państwa przyjmującego (dyrektywa 96/71): płaca minimalna, czas pracy; po 12 miesiącach prawie wszystkie warunki. Diety i noclegi.
- Praca zdalna z zagranicy — ryzyko składek i podatku w państwie wykonywania. Telepraca transgraniczna (porozumienie ramowe 2023): do 50% czasu w państwie zamieszkania bez zmiany ustawodawstwa — wniosek A1.

## B2B i art. 22 KP
Art. 22 §1¹: zatrudnienie w warunkach stosunku pracy jest stosunkiem pracy bez względu na nazwę umowy. Warunki: praca określonego rodzaju na rzecz pracodawcy i pod jego KIEROWNICTWEM, w miejscu i czasie wyznaczonym, osobiście, za wynagrodzeniem, ryzyko gospodarcze po stronie firmy.
Art. 22 §1²: zakaz zastępowania umowy o pracę umową cywilnoprawną.
Kto przekwalifikowuje: sąd na powództwo pracownika lub PIP. Projekt nowelizacji ustawy o PIP 2025/2026 — decyzja administracyjna inspektora przekształcająca umowę; status: projekt.

| Skutek przekwalifikowania | Szczegóły |
|---|---|
| składki ZUS za 5 lat | całość płaci pracodawca; części pracownika nie może potrącić (SN) |
| PIT | zaległy PIT jako płatnik; różnica między liniowym a skalą — po stronie pracownika |
| uprawnienia | urlopy i ekwiwalent, nadgodziny, PPK, ochrona, PFRON/ZFŚS |
| wykroczenie | 1 000–30 000 zł |

## Test bezpiecznego B2B
- Własny sprzęt i miejsce.
- Brak podporządkowania: zlecenia-rezultaty, nie polecenia.
- Możliwość zastępstwa lub podwykonawcy.
- Wielu klientów.
- Własne ryzyko (kary umowne).
- Faktury za rezultat lub okres; bez grafiku i wniosków urlopowych; własne BHP.
Umowa z BYŁYM pracownikiem: liniowy 19% niedostępny w roku rozpoczęcia, gdy te same czynności dla byłego pracodawcy; ryczałt — w roku i następnym; ZUS preferencyjny niedostępny przy tych samych czynnościach dla byłego pracodawcy.

## Składki przedsiębiorcy 2026
| Wariant | Podstawa i kwoty |
|---|---|
| duży ZUS | podstawa 60% × 9 420 = 5 652 zł: emerytalna 1 103,27, rentowa 452,16, wypadkowa 94,39, FP/FS 138,47, dobrowolna chorobowa 138,47 — razem ok. 1 926,76 z chorobową |
| zdrowotna | wg formy opodatkowania: skala 9% dochodu, liniowy 4,9%; minimum 324,41 zł = 9% × 75% minimalnej |
| preferencyjne (24 miesiące) | podstawa 30% minimalnej = 1 441,80 zł |
| ulga na start (6 miesięcy) | tylko zdrowotna |
| mały ZUS plus (przychód ≤ 120 000) | od dochodu |"""

WYJASNIENIA["zus_zgloszenia"] = """## Dokumenty płatnika
| Dokument | Do czego |
|---|---|
| ZPA | zgłoszenie płatnika — osoba prawna lub jednostka |
| ZFA | zgłoszenie płatnika — osoba fizyczna |
| ZBA | rachunki bankowe |
| ZAA | adresy prowadzenia działalności |
| ZIPA | zmiana danych identyfikacyjnych płatnika |
| ZWPA | wyrejestrowanie płatnika |
Dla firm z KRS/CEIDG ZUS tworzy zgłoszenie płatnika automatycznie z danych rejestrowych.

## Dokumenty ubezpieczonego
| Dokument | Do czego |
|---|---|
| ZUA | zgłoszenie do ubezpieczeń społecznych i zdrowotnego: pracownik 01 10, zleceniobiorca 04 11, wychowawczy 12 11… |
| ZZA | tylko zdrowotne: zleceniobiorca ze zbiegiem, osoba na uldze na start 05 40 |
| ZIUA | zmiana danych identyfikacyjnych: PESEL, nazwisko, dokument |
| ZUA/ZZA w trybie ZMIANY | adres, NFZ (od 2019 zmiana adresu przez ZUA zmiana) |
| ZUA/ZZA w trybie KOREKTY | błędny kod lub data — korekta w ZUA z tym samym kodem; zły kod tytułu → ZWUA z datą zgłoszenia + nowe ZUA |
| ZWUA | wyrejestrowanie: data = dzień po ustaniu tytułu; kod przyczyny 100 ustanie tytułu, 500 zgon, 600 inna |
| ZCNA | zgłoszenie lub wyrejestrowanie członka rodziny do zdrowotnego: małżonek, dziecko do 18 lat (do 26 ucząc się), bez własnego tytułu; 7 dni od oświadczenia pracownika; kod stopnia pokrewieństwa, wspólne gospodarstwo |
| ZSWA | praca w szczególnych warunkach — do 31.03 za poprzedni rok (FEP) |
| IWA | do 31.01 (składka wypadkowa) |
ZWUA pracownika od 2019 ma dodatkowo kod trybu rozwiązania lub wygaśnięcia stosunku pracy i kod podstawy prawnej: porozumienie stron art. 30 §1 pkt 1 KP; wypowiedzenie przez pracownika lub pracodawcę art. 30 §1 pkt 2; bez wypowiedzenia art. 52/53/55; upływ czasu art. 30 §1 pkt 4; wygaśnięcie art. 63. Wykaz kodów na zus.pl. ZUS porównuje te dane przy ustalaniu prawa do zasiłku dla bezrobotnych i stażu.

## Terminy — wszystkie 7 dni
| Dokument | Od kiedy liczysz |
|---|---|
| ZUA/ZZA | od powstania obowiązku: dzień rozpoczęcia pracy lub zawarcia zlecenia; zleceniobiorcy-studenta nie zgłaszasz |
| ZWUA | od ustania; data wyrejestrowania = dzień następny po ostatnim dniu umowy |
| ZCNA, zmiany danych, RUD | 7 dni |
Zgłoszenie z opóźnieniem to wykroczenie (do 5 000 zł) i ryzyko przy wypadku. ZUS i tak obejmuje ubezpieczeniem od daty tytułu, ale PIP i ZUS karzą.

## Kod tytułu — 6 cyfr
4 cyfry tytułu + 1 cyfra prawa do emerytury lub renty (0 nie, 1 emerytura, 2 renta) + 1 cyfra niepełnosprawności (0 nie, 1 lekki, 2 umiarkowany, 3 znaczny).
Przykład: 01 10 2 2 = pracownik z rentą i umiarkowanym stopniem.
| Kod | Tytuł |
|---|---|
| 01 10 | pracownik |
| 01 20 | młodociany |
| 04 11 | zleceniobiorca |
| 04 30 | osoba współpracująca ze zleceniobiorcą |
| 05 10 | działalność |
| 05 70 | działalność — preferencyjne |
| 05 40 | działalność — ulga na start |
| 05 90 | mały ZUS plus |
| 12 11 | urlop wychowawczy |
| 12 40 | zasiłek macierzyński — osoba na macierzyńskim po ustaniu, zleceniobiorca |
| 30 00 | osoba bez tytułu, dla której rozliczasz składki lub świadczenia po ustaniu (wypłata po zwolnieniu) |

## Dane w ZUA
PESEL (obcokrajowiec bez PESEL — paszport; PESEL obowiązkowy do PIT). Nazwisko, data urodzenia, obywatelstwo. Adresy: zameldowania, zamieszkania, korespondencji. NFZ — oddział wg zamieszkania. Daty powstania obowiązku dla każdego ubezpieczenia. Wniosek o dobrowolne chorobowe — zleceniobiorca od dnia wniosku, nie wstecz.

## Praktyka
Program kadrowy generuje KEDU → Płatnik: weryfikacja z danymi ZUS (czerwone błędy blokują, zielone ostrzeżenia sprawdź) → wysyłka z podpisem → potwierdzenie UPP (zachowaj).
W eZUS sprawdzaj „Ubezpieczeni” (czy zgłoszenie dotarło) i „Dokumenty i wiadomości”. Na zawiadomienia ZUS o błędach odpowiadasz w 7 dni.
Najczęstsze błędy: zły kod (01 10 zamiast 04 11); zła data (zawarcie umowy zamiast rozpoczęcia pracy); brak ZWUA; nieaktualny adres (korespondencja ZUS do pracownika); ZCNA zapomniane po ślubie lub urodzeniu dziecka; zgłoszenie studenta."""

WYJASNIENIA["zus_rozliczenia"] = """## Komplet miesięczny
| Dokument | Co zawiera |
|---|---|
| DRA | deklaracja zbiorcza: liczba ubezpieczonych, sumy składek wg funduszy, kwoty zasiłków wypłaconych przez płatnika do rozliczenia z ZUS, kwota do zapłaty, stopa wypadkowa |
| RCA | raport imienny: za każdego ubezpieczonego kod tytułu, wymiar etatu, podstawy i składki emerytalna, rentowa, chorobowa, wypadkowa, zdrowotna; od 2022 informacyjnie kwota wpłaty na PPK finansowanej przez płatnika |
| RSA | raport o przerwach i świadczeniach: kody przerw, okresy, dni, kwoty zasiłków wypłaconych przez płatnika |
| RPA | raport o przychodach dla celów emerytalnych — składasz TYLKO, gdy wystąpiło: przychód należny za INNY rok wypłacony w tym miesiącu (trzynastka, premia roczna, wyrównanie); składnik wypłacony OBOK wynagrodzenia chorobowego lub zasiłku, od którego nie było składek, a stanowi podstawę do emerytury (dodatek stażowy w pełnej wysokości w czasie choroby); praca nauczycielska; praca w szczególnych warunkach przed 2009 |
Za pracowników i zleceniobiorców składasz jeden komplet. Identyfikator dokumentu: 01 MM RRRR — pierwotny; 02–39 — kolejne korekty. Przy przekroczeniu 30-krotności — informacja ZUS i korekty.

## Zasada kasowa
W raportach za dany miesiąc wykazujesz przychody WYPŁACONE lub postawione do dyspozycji w tym miesiącu.
| Przykład | Gdzie |
|---|---|
| wynagrodzenie za listopad wypłacone 10 grudnia | DRA/RCA za grudzień (12/2026) |
| wypłata do końca miesiąca | za ten miesiąc |
| nieobecność listopadowa (pensja w grudniu) | RSA za listopad (11/2026) |
Rozjazd okresów RCA i RSA jest normalny.

## Terminy złożenia i zapłaty
| Płatnik | Do |
|---|---|
| jednostki budżetowe | 5. dnia następnego miesiąca |
| osoby prawne: sp. z o.o., S.A., spółdzielnie, fundacje | 15. |
| pozostali: osoby fizyczne, spółki osobowe | 20. |
Dzień wolny → następny roboczy.
Wpłata: jeden przelew na indywidualny NRS (numer rachunku składkowego z zaświadczenia ZUS); w tytule nic nie trzeba. ZUS rozdziela na fundusze proporcjonalnie i zalicza najpierw najstarsze zaległości — opóźnienie jednej wpłaty „przesuwa” kolejne.
Składki zdrowotne — tym samym przelewem na NRS (od 2018).

## Odsetki i sankcje
- Odsetki za zwłokę — stawka jak od zaległości podatkowych (stopa na podatki.gov.pl). Nie nalicza się, gdy ich kwota nie przekracza 1% minimalnego wynagrodzenia (48,06 zł w 2026).
- Opłata dodatkowa do 100% nieopłaconych składek — przy uporczywym niepłaceniu.
- Zaległości blokują zaświadczenie o niezaleganiu (przetargi, kredyty) i ulgi. Układ ratalny — wniosek RSR.
Płatnik zasiłków: wypłacone zasiłki (nie wynagrodzenie chorobowe!) odejmujesz w DRA od składek do zapłaty. Gdy zasiłki > składki — ZUS zwraca na wniosek.

## Obowiązki wobec ubezpieczonego
Roczna informacja IMIR (dawniej RMUA) — do końca lutego za rok poprzedni. Miesięczna — na żądanie ubezpieczonego, nie częściej niż raz na miesiąc. W praktyce generujesz z programu. Pracownik sam weryfikuje dane w eZUS.

## Kontrola spójności przed wysyłką
- Liczba ubezpieczonych w DRA = liczba RCA. Sumy RCA = DRA.
- Podstawy RCA = lista płac (brutto − wyłączenia).
- Okresy RSA = ewidencja nieobecności.
- Zdrowotna 9% od (podstawa − składki społeczne).
- Zleceniobiorcy ze zbiegiem: podstawa społecznych 0, zdrowotna pełna.
- Kody RCA z informacją o etacie (np. 1/1, 1/2).
- Wychowawczy: RCA 12 11 z podstawą 60% prognozowanego (5 652 zł w 2026, minimum 75% minimalnej) finansowaną z budżetu — w DRA w osobnym bloku; zdrowotna od podstawy równej kwocie specjalnego zasiłku opiekuńczego (620 zł).
- PPK — poza ZUS.
Korekta po terminie — lekcja o korektach. Dokumenty rozliczeniowe (kopie DRA/RCA/RSA i potwierdzenia) przechowujesz 5 lat."""

WYJASNIENIA["zus_korekty"] = """## Kiedy i jak korygujesz
| Element | Zasada |
|---|---|
| termin | 7 dni od stwierdzenia błędu albo od zawiadomienia ZUS; po kontroli — 30 dni od protokołu lub decyzji |
| forma | nowy komplet za miesiąc z identyfikatorem 02 MM RRRR (03, 04… kolejne) |
| co składasz | DRA zawsze + tylko te RCA/RSA, które się zmieniają; RCA korygujący zastępuje pierwotny dla danej osoby; RSA — pełny zestaw przerw osoby |
| dokumenty zgłoszeniowe | ZUA/ZZA w trybie korekty; ZWUA + ZUA przy złym kodzie lub dacie; ZIUA przy danych identyfikacyjnych |
| granica czasu | nie korygujesz po upływie 5 lat od terminu wymagalności składek (od 2022; ZUS też nie wszczyna postępowań) — wyjątki: po wyroku sądu, decyzji |
ZUS sam koryguje drobne błędy (od 2022 — składki pracownika do określonej kwoty) i wysyła informację. Weryfikuj ją z własnymi danymi.

## 30-krotność (282 600 zł w 2026)
Gdy podstawa emerytalno-rentowa narastająco przekracza limit, od nadwyżki nie naliczasz emerytalnej i rentowej. Chorobowa, wypadkowa, zdrowotna, FP/FGŚP — dalej.
Pracownik z kilkoma płatnikami pilnuje sam — oświadczenie o przekroczeniu u innego płatnika. ZUS powiadamia o przekroczeniu u kilku płatników i wskazuje, który koryguje.
Gdy naliczyłeś za dużo:
- korekta RCA — podstawa do limitu,
- nadpłata emerytalnej i rentowej: część pracodawcy do zaliczenia, część pracownika do zwrotu pracownikowi,
- skutki uboczne: rośnie podstawa zdrowotnej (mniej odliczonych składek) i podatek — niedopłatę zdrowotnej i PIT potrącasz ze zwracanej kwoty,
- zwrócone składki społeczne to przychód ze stosunku pracy w miesiącu zwrotu — doliczasz do listy, zaliczka,
- różnicę zdrowotnej wykazujesz w RCA korekcie.

## Typowe korekty
| Błąd | Co robisz |
|---|---|
| zleceniobiorca-student zgłoszony z pełnymi składkami | ZWUA, korekty RCA, zwrot |
| zbieg: pełne składki zamiast tylko zdrowotnej (lub odwrotnie — po zmianie etatu u innego pracodawcy) | NIEDOPŁATA 5 lat wstecz z odsetkami; część pracownika można potrącić za zgodą lub dochodzić |
| nieuwzględnione świadczenie (benefit, ZFŚS bez kryterium) | dopłata |
| wynagrodzenie chorobowe zamiast zasiłku (błędna pula 33 dni) | RSA i rozliczenie zasiłku z ZUS |
| wypłata po ustaniu zatrudnienia bez kodu 30 00 | korekta kodu |
| zły kod przerwy | korekta RSA |

## Nadpłata, niedopłata, płynność
- Nadpłata: ZUS zalicza na przyszłe składki albo zwraca w 30 dni na wniosek RZS-P (eZUS).
- Niedopłata: wpłata z odsetkami (nalicz kalkulatorem ZUS).
- Problemy z płynnością: wniosek o układ ratalny (RSR) albo odroczenie — po zawarciu nie ma odsetek, jest opłata prolongacyjna.

## PIT po korekcie składek
| Sytuacja | Skutek |
|---|---|
| zwrot składek społecznych pracownikowi | przychód w roku zwrotu — PIT-11 za ten rok, pozycja składki pomniejszona |
| zwrot zdrowotnej | od 2022 nie wpływa na podatek (nieodliczalna) |
| zwrot składek byłemu pracownikowi (brak wypłat) | PIT-11 z przychodem ze stosunku pracy; zaliczka potrącona ze zwrotu |
Dokumentuj każdą korektę: uzasadnienie, obliczenia, pisma do pracownika. ZUS może pytać po latach."""

WYJASNIENIA["pit_roczny"] = """## Co składasz po zamknięciu roku — wyłącznie elektronicznie
Składasz przez e-Deklaracje lub e-Urząd Skarbowy, z podpisem kwalifikowanym osoby z UPL-1 zgłoszonym do US.
| Termin | Dokument | Co zawiera |
|---|---|---|
| 31 stycznia | PIT-4R | deklaracja roczna o pobranych zaliczkach: kwoty należnych zaliczek za każdy miesiąc, liczba podatników; wpłaty muszą się zgadzać z historią mikrorachunku |
| 31 stycznia | PIT-8AR | zryczałtowany podatek: umowy do 200 zł, nierezydenci 20%, nagrody w konkursach, wygrane |
| 31 stycznia | PIT-11 do urzędu skarbowego | informacja o przychodach, kosztach, zaliczkach i składkach — za każdego, komu wypłacono cokolwiek w roku: pracownicy, zleceniobiorcy, osoby z zasiłkami, byli pracownicy; adresat: US wg miejsca zamieszkania podatnika (system wysyła zbiorczo) |
| koniec lutego | PIT-11 dla podatnika | papierowo albo elektronicznie: e-mail z podpisem kwalifikowanym lub portal pracowniczy — za zgodą, z potwierdzeniem doręczenia; wydrukuj potwierdzenia |
| koniec lutego | IFT-1R | dla nierezydentów — i do US |
| koniec lutego | ZUS IMIR | roczna informacja dla ubezpieczonego |
Po ustaniu zatrudnienia w trakcie roku PIT-11 składasz w standardowym terminie. Na WNIOSEK podatnika — w 14 dni (art. 39 ust. 2 PIT).
Płatnik nie rozlicza już podatnika (PIT-40 zniesiony). Podatnik korzysta z Twój e-PIT, zasilonego Twoimi PIT-11. Błąd w PIT-11 = błąd w zeznaniu pracownika.

## Treść PIT-11
Sprawdź numer formularza na podatki.gov.pl — od 2024 obowiązuje wersja 29 lub nowsza.
| Sekcja | Co wpisujesz |
|---|---|
| dane | płatnik i podatnik: PESEL/NIP, adres (zagraniczny dla nierezydentów) |
| przychody wg źródeł | stosunek pracy (osobno przychody z 50% KUP); zlecenia (działalność wykonywana osobiście); zasiłki z ubezpieczenia społecznego wypłacone przez zakład pracy (inne źródła) |
| czego tu nie ma | należności z art. 30 ust. 1 pkt 5a (ryczałt) — w PIT-8AR |
| KUP | faktycznie zastosowane: 250/300, 20%, 50% |
| dochód i zaliczki | zaliczki pobrane |
| składki społeczne | podlegające odliczeniu; składki od przychodów zwolnionych — osobno |
| składka zdrowotna | od 2022 BRAK pola — nie wykazujesz |
| przychody ZWOLNIONE | ulga dla młodych (stosunek pracy i zlecenia osobno, zasiłek macierzyński osobno), na powrót, 4+, dla seniorów — z zaznaczeniem, które zwolnienie i czy stosowane na wniosek |
| zwolnienia przedmiotowe (ZFŚS do 1 000 zł, posiłki) | nie wykazujesz |
| wpłaty pracodawcy na PPK | w przychodzie ze stosunku pracy |
Zgodność: suma zaliczek z PIT-11 = PIT-4R = wpłaty na mikrorachunek. Suma przychodów = kartoteka płacowa.
Zasada kasowa: wypłaty w roku, nie „za rok”. Pensja za grudzień wypłacona 10.01 → PIT-11 za następny rok!

## Korekta PIT-11
Korygujesz zawsze, gdy jest błąd — także po latach, do przedawnienia 5 lat.
Składasz nowy PIT-11 z zaznaczeniem „korekta” i uzasadnieniem (ORD-ZU już niewymagany; dobrą praktyką jest pismo). Przekazujesz podatnikowi.
Typowe przyczyny: zwrot składek, błędne KUP, nieujęta wypłata po ustaniu, świadczenie w naturze, przekwalifikowanie umowy.

## Odpowiedzialność płatnika
- Za niepobrany lub niewpłacony podatek — art. 30 Ordynacji; chyba że wina podatnika, np. fałszywe oświadczenie.
- KKS art. 77 — niewpłacenie w terminie (grzywna); art. 80 — niezłożenie informacji.

## Harmonogram zamknięcia roku w kadrach
| Miesiąc | Co robisz |
|---|---|
| grudzień | weryfikacja kartotek (adresy, PESEL, urzędy); oświadczenia PIT-2 na kolejny rok obowiązują nadal — nie zbierasz ponownie; KUP |
| styczeń | uzgodnienie zaliczek z mikrorachunkiem; PIT-4R, PIT-8AR, PIT-11 do US |
| luty | PIT-11 pracownikom, IFT, IMIR; informacja o PPK (autozapis w roku autozapisu) |
Przechowywanie: 5 lat od końca roku, w którym upłynął termin płatności podatku."""

WYJASNIENIA["zfss_pfron"] = """## ZFŚS — kto musi (ustawa z 4.03.1994)
| Pracodawca (stan na 1 stycznia, pełne etaty) | Obowiązek |
|---|---|
| co najmniej 50 etatów | obowiązkowy; rezygnacja tylko w układzie lub regulaminie wynagradzania |
| budżetówka | zawsze |
| 20–49,99 etatu | na wniosek zakładowej organizacji związkowej |
| poniżej 50 | dobrowolnie; jeśli nie tworzy — wypłaca ŚWIADCZENIE URLOPOWE, chyba że do 31 stycznia poinformuje pracowników o nietworzeniu funduszu i niewypłacaniu świadczenia |
Świadczenie urlopowe: raz w roku, przy urlopie co najmniej 14 dni kalendarzowych, do wysokości odpisu, proporcjonalnie do etatu; bez ZUS, z PIT.

## Odpis 2026
Podstawa: 7 848,60 zł — przeciętne wynagrodzenie w II półroczu 2025 (obwieszczenie GUS).
| Odpis | Stawka | Kwota |
|---|---|---|
| podstawowy — na etat | 37,5% | 2 943,23 zł |
| prace szczególnie uciążliwe | 50% | 3 924,30 zł |
| młodociani | 5/6/7% (I/II/III rok) | — |
| zwiększenie: niepełnosprawni (umiarkowany, znaczny) | +6,25% | 490,54 zł |
| zwiększenie: emeryci — byli pracownicy | +6,25% | 490,54 zł |
| zwiększenie: żłobek lub klub dziecięcy | +7,5% | — |
Liczysz od przeciętnej planowanej liczby zatrudnionych w przeliczeniu na etaty; korekta na 31.12 wg faktycznej.
Przelewy na odrębny rachunek: 75% do 31 maja, reszta do 30 września; korekta do 31 grudnia.

## Na co i jak wydajesz
- Regulamin ZFŚS uzgodniony ze związkami (lub przedstawicielem załogi). Komisja socjalna.
- Kryterium socjalne: sytuacja życiowa, rodzinna, materialna — oświadczenie o dochodzie na osobę w rodzinie; prawo żądania dokumentów.
| Przeznaczenie | Uwagi |
|---|---|
| wypoczynek: wczasy pod gruszą, kolonie dzieci | kolonie dzieci do 18 lat przy zorganizowanym wypoczynku — zwolnione z PIT bez limitu |
| kultura i sport | — |
| opieka nad dziećmi (żłobki) | — |
| pomoc materialna | zapomogi losowe zwolnione bez limitu; inne do 1 000 zł łącznie ze świadczeniami |
| pożyczki mieszkaniowe | umowa, poręczenie, potrącenie za zgodą (art. 91) |
Nie z ZFŚS: szkolenia, benefity dla wszystkich „po równo”, imprezy bez kryterium (integracyjne dla wszystkich dopuszcza MRPiPS, ale ZUS bywa sceptyczny), medycyna, premie.
RODO: oświadczenia o dochodach — przegląd corocznie, dostęp tylko dla komisji, retencja do czasu dochodzenia roszczeń.

## PFRON — wpłaty (ustawa z 27.08.1997 o rehabilitacji)
Pracodawca z co najmniej 25 etatami (przeciętnie w miesiącu) i wskaźnikiem zatrudnienia osób z niepełnosprawnością poniżej 6% płaci co miesiąc.
Wpłata = 40,65% przeciętnego wynagrodzenia (GUS, poprzedni kwartał) × (6% × etaty − etaty osób z niepełnosprawnością).
| Dokument | Termin |
|---|---|
| DEK-I-0 i wpłata | do 20. dnia następnego miesiąca (e-PFRON2) |
| DEK-R roczna | do 20 stycznia |
| INF-1 (zwolnieni — wskaźnik co najmniej 6%) | do 20. |
Placówki edukacyjne — próg 2%.
Obniżenie wpłaty: zakup usług lub produkcji od firm uprawnionych (informacja o kwocie obniżenia na fakturze; do 50% wpłaty); zatrudnianie osób ze schorzeniami szczególnymi (obniżony wskaźnik).

## PFRON — dofinansowanie do wynagrodzeń (SOD)
Warunki: pracodawca z co najmniej 25 etatami musi mieć co najmniej 6% (mniejsi — bez warunku); efekt zachęty (wzrost zatrudnienia lub zwolnione miejsce); bez zaległości PFRON powyżej 100 zł; wynagrodzenie wypłacone na konto i koszty płacy w terminie (ZUS do 14 dni po terminie — dopuszczalne).
| Stopień | Kwota miesięczna (od 2025) | Dodatkowo przy schorzeniach szczególnych |
|---|---|---|
| znaczny | 2 760 zł | +1 380 zł |
| umiarkowany | 1 550 zł | +1 035 zł |
| lekki | 575 zł | +690 zł |
Schorzenia szczególne: epilepsja, choroba psychiczna, niepełnosprawność intelektualna, całościowe zaburzenia rozwojowe, niewidomi.
Limit: nie więcej niż 75% kosztów płacy (otwarty rynek) albo 90%.
Wniosek Wn-D + INF-D-P do 25. dnia następnego miesiąca przez SODiR. Orzeczenie w aktach (B); w ZUS — kod niepełnosprawności.

## Uprawnienia pracownika z niepełnosprawnością
| Uprawnienie | Umiarkowany i znaczny | Lekki |
|---|---|---|
| czas pracy | 7 h / 35 h bez obniżenia wynagrodzenia; na wniosek i za zgodą lekarza — normalny | 8 h / 40 h |
| praca nocna i nadgodziny | zakaz; wyjątki: pilnowanie mienia, zgoda lekarza na wniosek pracownika | zakaz — te same wyjątki |
| dodatkowa przerwa | 15 min | — |
| dodatkowy urlop | 10 dni (po roku od zaliczenia do stopnia) | — |
| turnus rehabilitacyjny | do 21 dni raz w roku, z wynagrodzeniem jak ekwiwalent | — |
| badania i zabiegi | zwolnienie 100% | — |
Każdy stopień: pracodawca zapewnia niezbędne racjonalne usprawnienia (refundacja z PFRON)."""

WYJASNIENIA["kalendarz_roczny"] = """## Co miesiąc (spółka z o.o., wypłata do 10.)
| Termin | Zadanie |
|---|---|
| do 5. | zamknięcie ewidencji czasu pracy i nieobecności, pobranie e-ZLA, wnioski urlopowe |
| do 8. | lista płac, kontrola, zatwierdzenie |
| 10. | wypłata (przelew dzień wcześniej, gdy 10. jest wolny) |
| do 15. | DRA/RCA/RSA/RPA + przelew na NRS; plik PPK + przelew do instytucji; ewentualne korekty ZUS |
| do 20. | zaliczka PIT na mikrorachunek; DEK-I-0 lub INF-1 PFRON |
| do 25. | Wn-D (SOD) |
| w 7 dni | ZUA, ZWUA, ZCNA, RUD, zmiany danych |
| w 14 dni | powiadomienia PUP (Ukraina), protokoły powypadkowe |
Bieżąco: zajęcia komornicze (odpowiedź 7 dni), wnioski o urlopy rodzicielskie (21 dni), badania okresowe (terminy z orzeczeń), kończące się umowy (ZWUA, świadectwo, ekwiwalent), limity 33/3, okresy próbne, wygasające dokumenty cudzoziemców, kary porządkowe (rok), dokumenty do akt.

## W roku
| Miesiąc | Zadania |
|---|---|
| styczeń | wymiar czasu pracy i harmonogramy na rok; minimalne wynagrodzenie (aneksy dla pensji poniżej, kwoty wolne od potrąceń, dodatek nocny); nowe wskaźniki (limit 30-krotności, współczynnik ekwiwalentu, odpis ZFŚS wstępny, PPK obniżona wpłata); ustalenie płatnika zasiłków (stan na 30.11); 20.01 DEK-R; 31.01: PIT-4R, PIT-8AR, PIT-11 do US, ZUS IWA, informacja o nietworzeniu ZFŚS (< 50); GUS Z-06 (termin wg portalu sprawozdawczego, zwykle początek lutego) |
| luty | PIT-11 pracownikom, IFT-1R, IMIR (koniec lutego); informacja o autozapisie PPK (w roku autozapisu — do końca lutego); plan urlopów, jeśli nie ustalony wcześniej |
| marzec | ZUS ZSWA (31.03); decyzja ZUS o stopie wypadkowej (do 20.04, obowiązuje od 1.04); przegląd regulaminów po zmianach prawa |
| kwiecień | nowa stopa wypadkowa w DRA za kwiecień; autozapis PPK (2027); Z-03 kwartalne GUS (10 dni po kwartale) |
| maj | 31.05 przelew 75% ZFŚS |
| czerwiec | kontrola urlopów (plan 14 dni); przegląd oświadczeń o dochodach ZFŚS |
| wrzesień | 15.09 ogłoszenie minimalnego wynagrodzenia na kolejny rok → budżet; 30.09 reszta odpisu ZFŚS i termin urlopów zaległych |
| październik–listopad | budżet wynagrodzeń; przegląd składników (dodatki od minimalnej); 30.11 liczba ubezpieczonych do chorobowego (płatnik zasiłków na kolejny rok); szkolenia BHP okresowe i badania zaplanowane |
| grudzień | korekta ZFŚS (31.12); limit nadgodzin (150 h); rozliczenie okresu rozliczeniowego; wnioski o 32% i PIT-2 na kolejny rok (jeśli zmiany); inwentaryzacja akt (kary do usunięcia, dokumenty do zniszczenia po 10 latach); plan urlopów; harmonogramy styczniowe; weryfikacja uprawnień (dostępy eZUS/PEL, UPL-1) |

## Cyklicznie
| Obowiązek | Częstotliwość |
|---|---|
| badania okresowe | wg orzeczenia: zwykle 2–4 lata, biurowe do 5; kontrolne po chorobie dłuższej niż 30 dni — przed dopuszczeniem!; końcowe przy narażeniu na czynniki rakotwórcze |
| szkolenia BHP okresowe — stanowiska robotnicze | co 3 lata; co rok przy pracach szczególnie niebezpiecznych |
| szkolenia BHP — kierownicy, inżynierowie, technolodzy | co 5 lat |
| szkolenia BHP — administracyjno-biurowi | co 6 lat; zwolnieni przy ryzyku do 3. kategorii i braku wypadków — decyzja pracodawcy |
| pierwsze szkolenie okresowe | do 12 miesięcy; kierownicy — 6 |
| ocena ryzyka zawodowego | przegląd przy zmianach |
| regulamin pracy i wynagradzania | obowiązek od 50 pracowników (20–49 na wniosek związków); od 5.11.2026 zasady przeciwdziałania mobbingowi (do 5.05.2027) |
| przeglądy | kary porządkowe (rok); dokumenty cudzoziemców (ważność); umowy terminowe (33/3); uprawnienia rodzicielskie (wiek dziecka); staż — nowe zaświadczenia (do 1.05.2028 dla prywatnych); PPK (wnioski 55+, 70 lat); PFRON (efekt zachęty) |
| GUS Z-12 | co 2 lata — struktura wynagrodzeń, październik |
| e-Doręczenia | skrzynka firmy — pisma ZUS, PIP, US |

## Jak prowadzić kalendarz
Rejestr terminów z alertami 7 dni przed (w kursie: plik kalendarza w projekcie, w firmie: program kadrowy). Każdy termin ma właściciela i zastępcę. Odhaczasz z datą wykonania. To Twoja ochrona przy kontroli."""

WYJASNIENIA["rozwiazanie_umowy"] = """## Tryby rozwiązania (art. 30 §1)
| Tryb | Kto | Zasady |
|---|---|---|
| porozumienie stron | obie strony | dowolny termin, bez przyczyny; przy przyczynach po stronie pracodawcy odprawa z ustawy o zwolnieniach grupowych i tak przysługuje |
| wypowiedzenie | każda ze stron | z okresem wypowiedzenia |
| bez wypowiedzenia — art. 52 (z winy pracownika) | pracodawca | ciężkie naruszenie podstawowych obowiązków; przestępstwo oczywiste lub stwierdzone wyrokiem; zawiniona utrata uprawnień — w 1 MIESIĄC od uzyskania wiadomości przez osobę uprawnioną |
| bez wypowiedzenia — art. 53 (bez winy) | pracodawca | niezdolność z powodu choroby dłuższa niż 3 miesiące (staż poniżej 6 miesięcy) albo dłuższa niż okres zasiłkowy + 3 miesiące świadczenia rehabilitacyjnego (staż co najmniej 6 miesięcy lub wypadek, choroba zawodowa); inna usprawiedliwiona nieobecność dłuższa niż 1 miesiąc; nie po stawieniu się do pracy po ustaniu przyczyny |
| bez wypowiedzenia — art. 55 | pracownik | orzeczenie lekarskie bez przeniesienia (7 dni) albo ciężkie naruszenie przez pracodawcę — z odszkodowaniem za okres wypowiedzenia |
| upływ czasu | — | umowa terminowa |
| wygaśnięcie | — | śmierć pracownika lub pracodawcy-osoby fizycznej; tymczasowe aresztowanie dłuższe niż 3 miesiące |
Ciężkie naruszenie (art. 52) = wina umyślna lub rażące niedbalstwo + zagrożenie interesów. Przykłady: nietrzeźwość, kradzież, nieusprawiedliwiona kilkudniowa nieobecność, praca zarobkowa na L4, naruszenie tajemnicy.

## Okresy wypowiedzenia
| Umowa | Staż u tego pracodawcy | Okres |
|---|---|---|
| określona i nieokreślona (art. 36) | poniżej 6 miesięcy | 2 tygodnie |
| określona i nieokreślona | co najmniej 6 miesięcy | 1 miesiąc |
| określona i nieokreślona | co najmniej 3 lata | 3 miesiące |
| próbna (art. 34) | do 2 tygodni | 3 dni robocze |
| próbna | ponad 2 tygodnie | 1 tydzień |
| próbna | 3 miesiące | 2 tygodnie |
Staż zakładowy liczysz także z art. 23¹ i — od 2026 — ze zlecenia u tego pracodawcy.
Liczenie: tygodniowy kończy się w sobotę; miesięczny — w ostatnim dniu miesiąca. Wypowiedzenie 12.11 z 1-miesięcznym okresem → umowa trwa do 31.12.
- Skrócenie 3-miesięcznego do 1 (art. 36¹) przy upadłości, likwidacji lub przyczynach niedotyczących pracownika — odszkodowanie za resztę (bez ZUS, z PIT; okres wliczany do stażu).
- Strony mogą po wypowiedzeniu ustalić wcześniejszy termin (art. 36 §6) — tryb się nie zmienia.
- Zwolnienie z obowiązku świadczenia pracy (art. 36²) — jednostronne, z wynagrodzeniem jak urlopowe.
- Urlop zaległy i bieżący w wypowiedzeniu — pracodawca może narzucić (art. 167¹).
- Dni wolne na poszukiwanie pracy przy wypowiedzeniu przez pracodawcę: 2 — przy 2 tygodniach lub 1 miesiącu; 3 — przy 3 miesiącach.

## Wymogi formalne (art. 30 §3–5)
| Wymóg | Zasada |
|---|---|
| pismo | podpis osoby uprawnionej (KRS, pełnomocnictwo); e-mail tylko z podpisem kwalifikowanym |
| przyczyna | przy wypowiedzeniu umowy na czas nieokreślony i — od 26.04.2023 — określony oraz przy art. 52/53: konkretna, prawdziwa, zrozumiała, istniejąca w dacie |
| przykłady przyczyn | likwidacja stanowiska — rzeczywista; utrata zaufania — z faktami; nieosiąganie wyników — z porównaniem; redukcja — ze wskazanymi kryteriami doboru |
| pouczenie | o odwołaniu do sądu pracy w 21 dni |
| konsultacja związkowa (art. 38) | zamiar na piśmie; 5 dni na zastrzeżenia (3 dni — art. 52); tylko dla członków i objętych obroną; brak związku — brak konsultacji |
| doręczenie | osobiście (notatka ze świadkiem; odmowa przyjęcia nie wpływa); listem poleconym (skuteczne z chwilą możliwości zapoznania się — awizo); kurierem; nie przez SMS |

## Ochrona przed wypowiedzeniem
| Podstawa | Kogo chroni |
|---|---|
| art. 41 | w czasie urlopu i innej usprawiedliwionej nieobecności — chyba że upłynął okres z art. 53; art. 52 możliwy; zwolnienie w dniu, gdy pracownik był w pracy, a potem poszedł na L4 — skuteczne |
| art. 39 | 4 lata przed emeryturą przy wystarczającym stażu |
| art. 177 | ciąża, urlopy rodzicielskie — także od wniosku |
| inni | ojcowie na urlopach, działacze związkowi (uchwała zarządu), SIP, radni, członkowie rad pracowników, żołnierze rezerwy |
| wiek przedemerytalny przy zwolnieniach grupowych | tylko wypowiedzenie zmieniające z dodatkiem wyrównawczym |
Od 2023: ochrona przed niekorzystnym traktowaniem za skorzystanie z uprawnień — ciężar dowodu na pracodawcy przy roszczeniach.

## Roszczenia pracownika (art. 45, 56)
- Przywrócenie do pracy albo odszkodowanie — do 3-miesięcznego wynagrodzenia; przy bezprawnym art. 52 — za okres wypowiedzenia.
- Od 2023 sąd może nakazać dalsze zatrudnianie chronionych do prawomocności (zabezpieczenie).
- Umowa na czas określony rozwiązana bezprawnie — odszkodowanie do końca umowy, maksymalnie 3 miesiące."""

WYJASNIENIA["odprawy_grupowe"] = """## Ustawa z 13.03.2003 — dla pracodawców z co najmniej 20 pracownikami
Dotyczy rozwiązań z przyczyn niedotyczących pracowników: ekonomicznych, organizacyjnych, technologicznych, likwidacji.

## Kiedy zwolnienie jest grupowe
W okresie do 30 dni rozwiązujesz umowy z:
| Zatrudnienie | Próg |
|---|---|
| 20–99 | co najmniej 10 pracowników |
| 100–299 | 10% |
| 300 i więcej | 30 |
Wliczasz porozumienia stron z inicjatywy pracodawcy, jeśli dotyczą co najmniej 5 osób.

## Procedura zwolnienia grupowego
1. Zawiadomienie związków (lub przedstawicieli) na piśmie: przyczyny, liczba zatrudnionych i zwalnianych, grupy, okres, kryteria doboru, kolejność, propozycje świadczeń.
2. Kopia do PUP.
3. Konsultacje → POROZUMIENIE w 20 dni. Brak porozumienia — REGULAMIN zwolnień po konsultacji.
4. Zawiadomienie PUP o porozumieniu lub regulaminie.
5. Wypowiedzenia nie wcześniej niż po zawiadomieniu PUP. Rozwiązanie nie wcześniej niż 30 dni od zawiadomienia.
- Indywidualna konsultacja z art. 38 jest zbędna przy porozumieniu.
- Chronieni szczególnie (art. 39, ciąża, działacze) — tylko wypowiedzenie zmieniające z DODATKIEM WYRÓWNAWCZYM do końca ochrony.
- Art. 41 nie stoi na przeszkodzie przy likwidacji i upadłości. Przy zwolnieniach grupowych: urlop co najmniej 3 miesiące, choroba po upływie okresu z art. 53.

## Zwolnienie indywidualne (art. 10)
U pracodawcy z co najmniej 20 pracownikami, gdy przyczyny niedotyczące pracownika są WYŁĄCZNĄ przyczyną. Odprawa przysługuje, bez procedury grupowej. Chronieni — tylko za zgodą związku, z ograniczeniami.
Ponowne zatrudnienie (art. 9): pracownik zgłosi zamiar w roku → pracodawca zatrudniający w tej samej grupie zawodowej w 15 miesięcy ma obowiązek go zatrudnić.

## Odprawa (art. 8)
| Staż u tego pracodawcy | Odprawa |
|---|---|
| poniżej 2 lat | 1-miesięczne wynagrodzenie |
| 2–8 lat | 2-miesięczne |
| ponad 8 lat | 3-miesięczne |
Liczysz jak ekwiwalent za urlop. Limit: 15 × minimalne = 72 090 zł (2026), 74 250 zł (2027).
Bez składek ZUS (§2 ust. 1 pkt 3 rozporządzenia składkowego), z PIT (bez zwolnienia).
Staż = u tego pracodawcy, w tym z art. 23¹ i (od 2026) ze zlecenia u niego.
Przy porozumieniu stron z przyczyn pracodawcy odprawa przysługuje (SN) — wpisz przyczynę w porozumieniu.

## Inne odprawy i odszkodowania
| Świadczenie | Zasady | ZUS | PIT |
|---|---|---|---|
| odprawa emerytalno-rentowa (art. 92¹ KP) | 1-miesięczna, raz w życiu; warunek: ustanie w związku z przejściem na emeryturę lub rentę (też po art. 53); układ może podwyższyć | nie | tak |
| odprawa pośmiertna (art. 93) | dla rodziny (małżonek, dzieci uprawnione do renty rodzinnej): 1-miesięczna (poniżej 10 lat), 3-miesięczna (co najmniej 10), 6-miesięczna (co najmniej 15); dzielona równo; połowa, gdy jeden uprawniony; nie wypłacasz, jeśli pracodawca ubezpieczył pracownika na życie i świadczenie ≥ odprawa | nie | zwolniona |
| odszkodowanie za skrócony okres wypowiedzenia (art. 36¹) | — | nie | tak |
| odszkodowania z art. 55 §1¹ i z art. 45/56 | zasądzone | nie | zwolnione przy wyroku lub ugodzie sądowej; ugoda pozasądowa — PIT |
| odszkodowanie z zakazu konkurencji po ustaniu (art. 101²) | minimum 25% wynagrodzenia za okres zakazu | nie | tak |
| odszkodowanie za niewydanie świadectwa | do 6 tygodni | — | — |
| nagroda jubileuszowa | wg regulaminu | nie, gdy nie częściej niż co 5 lat | tak |

## Przejście zakładu lub jego części (art. 23¹)
Dotyczy outsourcingu, sprzedaży, fuzji, przejęcia działu.
- Nowy pracodawca staje się stroną z mocy prawa: umowy, staż, urlopy, warunki — co najmniej rok przy układzie.
- Zawiadomienie pracowników na piśmie 30 dni przed: termin, przyczyny, skutki, zamierzone działania — gdy brak związków. Ze związkami — informacja i negocjacje.
- Pracownik może w 2 MIESIĄCE od przejścia rozwiązać umowę za 7-dniowym uprzedzeniem. Skutki jak wypowiedzenie przez pracodawcę, ale bez odprawy (SN).
- Zakaz wypowiedzenia z powodu przejścia.
- Umowy cywilnoprawne nie przechodzą automatycznie. Dokumentacja (akta) przechodzi.
- ZUS: wyrejestrowanie u dotychczasowego płatnika (ZWUA z kodem przyczyny właściwym dla przejęcia — z listy w Płatniku) i zgłoszenie u nowego od dnia przejścia.
- PIT-11 za okres u każdego pracodawcy; przy następstwie prawnym — jeden.
Outsourcing pozorny (ta sama praca, ten sam nadzór) — ZUS i PIP uznają za fikcję."""

WYJASNIENIA["swiadectwo_rozliczenie"] = """## Świadectwo pracy — kiedy i jak (art. 97, rozporządzenie z 30.12.2016 ze zm.)
Wydajesz w DNIU ustania stosunku pracy, bez wniosku. Gdy to niemożliwe — w 7 dni pocztą lub w inny sposób.
Postać papierowa. Elektroniczna z podpisem kwalifikowanym — tylko za zgodą pracownika; w praktyce papier.
Jeśli w 7 dni zawierasz kolejną umowę — świadectwo tylko na wniosek.

## Treść (wzór pomocniczy MRPiPS)
| Pozycja | Co wpisujesz |
|---|---|
| zatrudnienie | okres, wymiar etatu, stanowiska lub rodzaj pracy |
| tryb i podstawa rozwiązania | art. 30 §1 pkt …; art. 52; art. 53; upływ czasu; wygaśnięcie; przy zwolnieniach grupowych — „art. 1/art. 10 ustawy z 13.03.2003” (ważne dla zasiłku dla bezrobotnych) |
| skrócenie okresu wypowiedzenia | art. 36¹ |
| urlop wypoczynkowy wykorzystany w roku ustania | dni i godziny, w tym na żądanie; obejmuje urlop, za który wypłacono ekwiwalent |
| urlopy i zwolnienia | bezpłatny (podstawa); ojcowski, rodzicielski, wychowawczy (wymiar, części, podstawa); opiekuńczy (173¹); siła wyższa (148¹); art. 188; praca zdalna okazjonalna; zwolnienie z obowiązku świadczenia pracy (36²) |
| niezdolność do pracy w roku | dni z 33/14 (art. 92) |
| okresy nieskładkowe | choroba — wszystkie w okresie zatrudnienia |
| zajęcia komornicze | komornik, sygnatura, kwota |
| na wniosek pracownika | wysokość i składniki wynagrodzenia, kwalifikacje, wyrok sądu |
NIE wpisujesz: przyczyny rozwiązania, oceny, kar.

## Sprostowanie i sankcje
| Krok | Termin |
|---|---|
| wniosek pracownika o sprostowanie (papierowo lub elektronicznie) | 14 dni |
| odpowiedź pracodawcy | 7 dni |
| odmowa (albo brak odpowiedzi) → sąd pracy | 14 dni |
| nowe świadectwo po wyroku | 7 dni |
Kopia w aktach C.
Odszkodowanie za niewydanie lub wadliwe świadectwo — do 6 tygodni wynagrodzenia, gdy pracownik nie mógł podjąć pracy. Niewydanie to wykroczenie (1 000–30 000).
Zmiana podstawy po wyroku (np. art. 52 → art. 30 §1 pkt 2) — nowe świadectwo.
Śmierć pracownika — świadectwo do akt; rodzina może wnioskować.
Świadectwo podpisuje osoba upoważniona. E-doręczenie oryginału z podpisem kwalifikowanym — dopuszczalne za zgodą; praktyka ostrożna: papier.

## Rozliczenie końcowe — checklista
| Obszar | Co robisz |
|---|---|
| wynagrodzenie | za część miesiąca (stałe / wymiar × przepracowane); zmienne (nadgodziny, nocne, premie) |
| ekwiwalent za urlop | współczynnik; wypłata w terminie wypłaty albo w 10 dni od ustania (od 27.01.2026) |
| inne wypłaty | odszkodowanie za skrócony okres; odprawa (72 090); zakaz konkurencji (odszkodowanie w ratach); rozliczenie zaliczek i pożyczek (potrącenie za zgodą); nadpłaty; karta i pasek |
| ZUS | ZWUA w 7 dni (data następna); ZCNA dla rodziny; RSA za nieobecności; RCA za wypłaty po ustaniu (kod 30 00) |
| PIT | oświadczenia pomijane po ustaniu — zaliczki od późniejszych wypłat bez 300 zł i bez podwyższonych KUP; PIT-11 w terminie lub w 14 dni na wniosek |
| PPK | środki zostają na rachunku; informację o rachunkach nowemu pracodawcy przekazuje pracownik |
| komornik | zawiadomienie o ustaniu i wpis w świadectwie |
| dokumentacja | informacja o okresie przechowywania (10 lat od końca roku ustania) i możliwości odbioru do końca miesiąca po upływie okresu; kopia akt na wniosek |
| zaświadczenia | o zatrudnieniu i wynagrodzeniu (ZUS ERP-7 — na wniosek, bez terminu ustawowego, w praktyce 7–14 dni); potwierdzenie okresów pracy w szczególnych warunkach |
| mienie i dostępy | zwrot sprzętu, odzieży, kluczy, kart — protokół; odwołanie uprawnień (eZUS, poczta, systemy, pełnomocnictwa) tego samego dnia |
| RODO | zakończenie przetwarzania w systemach poza aktami |
| exit interview | dobrowolny |

## Śmierć pracownika
Wynagrodzenie i odprawa pośmiertna dla rodziny (art. 63¹). Prawa majątkowe przechodzą na małżonka i osoby uprawnione do renty rodzinnej w równych częściach — bez postępowania spadkowego.
Świadczenia wypłacone po śmierci to dla członków rodziny przychody z praw majątkowych: PIT-11 na uprawnionych, zaliczka 12% bez KUP, bez składek ZUS."""

WYJASNIENIA["mobbing_dyskryminacja_2026"] = """## Mobbing — nowa definicja (ustawa z 19.06.2026, Dz.U. 2026 poz. 1046, od 5.11.2026)
Mobbing to uporczywe nękanie pracownika (art. 94³ §2). Zachowanie — działanie lub zaniechanie — które w szczególności:
- poniża lub ośmiesza,
- izoluje lub eliminuje z zespołu,
- narusza godność,
- zastrasza,
- polega na nieuzasadnionej krytyce, utrudnianiu wykonywania pracy, bezpodstawnym obciążaniu lub odbieraniu zadań.
| Element definicji | Nowa zasada |
|---|---|
| uporczywość | powtarzalność lub długotrwałość — bez sztywnego minimum czasowego (SN wcześniej wymagał miesięcy) |
| zamiar (wina umyślna) | nie jest wymagany |
| skutek „zaniżonej oceny przydatności zawodowej” | nie jest wymagany |
| kto może mobbować | przełożony, współpracownik, podwładny |
| jednorazowe ciężkie zdarzenie | to nie mobbing; może być dyskryminacją albo naruszeniem dóbr |

## Obowiązki pracodawcy (art. 94³ §1)
Pracodawca PRZECIWDZIAŁA mobbingowi: prewencja (szkolenia, zasady), wykrywanie (kanał zgłoszeń), reagowanie (postępowanie wyjaśniające), wsparcie ofiary.
Zasady przeciwdziałania określa regulamin pracy; u pracodawców bez regulaminu — obwieszczenie.
Pracodawcy objęci obowiązkiem (zgodnie z ustawą — zatrudniający co najmniej 10 pracowników) mają czas do 5.05.2027.

## Roszczenia pracownika
| Roszczenie | Zasady |
|---|---|
| zadośćuczynienie za rozstrój zdrowia | wymaga udowodnienia rozstroju |
| odszkodowanie | nie niższe niż 6-krotność minimalnego wynagrodzenia: 28 836 zł w 2026, 29 700 zł w 2027 |
Nowość: odszkodowanie bez konieczności rozwiązania umowy przez pracownika. Dotąd warunkiem było rozwiązanie umowy z powodu mobbingu.
Pracodawca odpowiada za własne zaniechania w przeciwdziałaniu — także gdy mobberem jest współpracownik.
Zwolnienie z odpowiedzialności za odszkodowanie: mobbingu nie dopuścił się pracodawca ani osoba zarządzająca, a pracodawca WYKAŻE, że realizował obowiązek przeciwdziałania (rzeczywista procedura, szkolenia, reakcja). To główny powód, by wdrożyć procedurę.
Ciężar dowodu: pracownik uprawdopodabnia. Dokumentacja po stronie pracodawcy decyduje.

## Dyskryminacja (art. 11³, 18³ᵃ–18³ᵉ)
Zakaz jakiejkolwiek dyskryminacji — bezpośredniej i pośredniej.
Cechy (katalog otwarty): płeć, wiek, niepełnosprawność, rasa, religia, narodowość, przekonania polityczne, przynależność związkowa, pochodzenie etniczne, wyznanie, orientacja seksualna, zatrudnienie na czas określony lub nieokreślony, pełny lub niepełny etat. SN: także np. wygląd, poglądy, światopogląd — o ile cecha jest „społecznie doniosła”.
| Forma | Przykłady |
|---|---|
| nierówne traktowanie | odmowa zatrudnienia, rozwiązanie, niekorzystne wynagrodzenie lub warunki, pominięcie w awansie lub szkoleniach |
| molestowanie | niepożądane zachowanie naruszające godność |
| molestowanie seksualne | — |
| inne | zachęcanie i nakazywanie dyskryminacji; działania odwetowe za skorzystanie z uprawnień |
Dozwolone różnicowanie (art. 18³ᵇ §2): obiektywne powody — staż, kwalifikacje, jakość pracy, rzeczywiste wymagania zawodowe, wiek przy ochronie, programy wyrównawcze.
Równe wynagrodzenie (art. 18³ᶜ): za jednakową pracę LUB pracę jednakowej wartości (porównywalne kwalifikacje, odpowiedzialność, wysiłek) — wszystkie składniki i świadczenia.
Ciężar dowodu: pracownik uprawdopodabnia (wskazuje cechę i gorsze traktowanie); pracodawca udowadnia obiektywne kryteria.
Odszkodowanie (art. 18³ᵈ): nie niższe niż minimalne wynagrodzenie (4 806), bez górnej granicy, niezależnie od szkody.
Nierówne traktowanie z innych przyczyn (art. 11² — „równe prawa za jednakowe obowiązki”) — roszczenia na zasadach ogólnych.

## Procedura wewnętrzna (do 5.05.2027)
| Element | Co zawiera |
|---|---|
| polityka | definicje, przykłady, zakaz odwetu — antymobbingowa i antydyskryminacyjna |
| kanały zgłoszeń | osoba zaufana lub komisja; pisemnie i ustnie; poufnie |
| postępowanie wyjaśniające | komisja 3 osoby, w tym spoza działu/HR; osoba zewnętrzna przy zgłoszeniu na zarząd; wysłuchanie stron i świadków; protokoły; termin (np. 30 dni, przedłużenie); raport z rekomendacją |
| środki | upomnienie lub nagana, przeniesienie, art. 52 wobec mobbera, mediacja, wsparcie psychologiczne |
| informacja zwrotna | dla zgłaszającego |
| rejestr spraw | RODO — dostęp ograniczony; retencja do przedawnienia 3 lata |
| szkolenia | wszyscy przy zatrudnieniu i co 2 lata; kadra kierownicza osobno |
| inne | ankiety klimatu; zapisy w regulaminie pracy (uzgodnienie ze związkami, 2 tygodnie od podania do wiadomości); potwierdzenie zapoznania (akta B) |
Kadry dokumentują KAŻDE zgłoszenie i reakcję. Brak reakcji to odpowiedzialność pracodawcy — nawet przy dobrej procedurze."""

WYJASNIENIA["jawnosc_wynagrodzen"] = """## Co obowiązuje od 24.12.2025 (Dz.U. 2025 poz. 807)
- Informacja o wynagrodzeniu lub przedziale dla kandydata (art. 18³ᶜᵃ).
- Zakaz pytania o historię wynagrodzeń (art. 22¹ §1 pkt 6).
- Neutralne płciowo ogłoszenia.
- Obowiązek informowania o postanowieniach układu lub regulaminu wynagradzania dotyczących stanowiska.
Sankcja: 1 000–30 000 zł.

## Co nadchodzi — dyrektywa (UE) 2023/970
Termin transpozycji: 7.06.2026 — Polska spóźniona. Projekt UC127 (zmiana KP i innych ustaw) jest w procesie rządowo-parlamentarnym, nieuchwalony na XI 2026. Sprawdź status na legislacja.gov.pl lub sejm.gov.pl.
| Element dyrektywy | Zasada |
|---|---|
| prawo do informacji | pracownik może żądać informacji o swoim indywidualnym wynagrodzeniu oraz o ŚREDNIM poziomie wynagrodzeń (w podziale na płeć) dla kategorii pracowników wykonujących tę samą pracę lub pracę tej samej wartości; odpowiedź w 2 miesiące; pracodawca co roku przypomina o tym prawie |
| zakaz klauzul poufności | pracownik może ujawniać swoje wynagrodzenie w celu egzekwowania równości; klauzule w umowach stają się bezskuteczne |
| przejrzyste kryteria | ustalania wynagrodzeń, poziomów i progresji — obiektywne, neutralne płciowo, łatwo dostępne; pracodawcy z co najmniej 50 pracownikami udostępniają obowiązkowo |
| wspólna ocena wynagrodzeń | z przedstawicielami pracowników, gdy luka w jakiejkolwiek kategorii ≥ 5%, nieuzasadniona obiektywnie i nieusunięta w 6 miesięcy |
| spory | ciężar dowodu na pracodawcy; pełne odszkodowanie (zaległe wynagrodzenie, premie, świadczenia, odsetki, zadośćuczynienie); sankcje administracyjne; wykluczenie z zamówień publicznych |
| „praca tej samej wartości” | kryteria: umiejętności, wysiłek, odpowiedzialność, warunki pracy (wartościowanie stanowisk) |

## Raportowanie luki płacowej
| Zatrudnienie | Częstotliwość |
|---|---|
| 250 i więcej | co roku; pierwszy raport wg dyrektywy w 2027 za 2026 |
| 150–249 | co 3 lata, od 2027 |
| 100–149 | co 3 lata, od 2031 |
Zakres raportu: luka w wynagrodzeniu średnim i medianie; luka w składnikach zmiennych; odsetek kobiet i mężczyzn otrzymujących składniki zmienne; luka w kwartylach; luka wg kategorii pracowników (podstawowe + zmienne).
Raport trafia do organu monitorującego (w projekcie: PIP) i do wiadomości pracowników.

## Co robić teraz — przygotowanie 12–18 miesięcy
| Krok | Co robisz |
|---|---|
| a) inwentaryzacja stanowisk i KATEGORIE | grupy pracy tej samej wartości; wartościowanie metodą punktową (np. 4 kryteria × wagi; narzędzia: Hay, własna metoda, metodyki z poradników PIP/MRPiPS); zapis kategorii w kartotece programu kadrowego |
| b) SIATKA PŁAC | widełki min–max dla kategorii; zasady progresji (staż, kompetencje, wyniki); polityka premiowania — na piśmie, w regulaminie wynagradzania |
| c) AUDYT LUKI | dla każdej kategorii średnia i mediana wynagrodzeń K i M (podstawowe i zmienne, w przeliczeniu na pełny etat lub godzinę); luka = (M − K)/M × 100%; każda różnica wyjaśniona obiektywnym czynnikiem (staż, dodatki za warunki) albo plan korekty |
| d) umowy i rekrutacja | usunięcie klauzul poufności (aneksy lub informacja o bezskuteczności); przegląd ogłoszeń i procesu rekrutacji (widełki, zakaz pytań) |
| e) komunikacja | informacja dla pracowników o kryteriach (gdy co najmniej 50); przeszkolenie menedżerów — rozmowy o wynagrodzeniach, uzasadnianie decyzji płacowych na piśmie |
| f) dane | raport z systemu kadrowo-płacowego w strukturze dyrektywy — test na danych za 2026 |
Z perspektywy kadr: każdy awans i podwyżka z uzasadnieniem w aktach (B); zmiany stawek zgodne z siatką; odstępstwa — decyzja zarządu z uzasadnieniem."""

WYJASNIENIA["sygnalisci_zdalna_rodo"] = """## Sygnaliści (ustawa z 14.06.2024, Dz.U. 2024 poz. 928)
Obowiązuje od 25.09.2024; zgłoszenia zewnętrzne od 25.12.2024.
Procedurę zgłoszeń wewnętrznych MUSI mieć podmiot, na rzecz którego pracę zarobkową wykonuje co najmniej 50 osób — stan na 1 stycznia lub 1 lipca. Liczysz osoby, nie etaty: pracowników, zleceniobiorców, B2B, praktykantów, stażystów.
| Element procedury | Zasada |
|---|---|
| wdrożenie | konsultacje ze związkami lub przedstawicielami 5–10 dni; wejście w życie 7 dni po podaniu do wiadomości |
| kanały | pisemny i ustny; anonimowe — jeśli procedura dopuszcza |
| kto przyjmuje | bezstronna osoba lub komórka (może być zewnętrzna) |
| potwierdzenie przyjęcia | 7 dni |
| informacja zwrotna | 3 miesiące |
| rejestr zgłoszeń | numer, przedmiot, dane, data, działania — 3 lata po zakończeniu roku |
Zakres naruszeń: korupcja, zamówienia publiczne, usługi i rynki finansowe, AML, bezpieczeństwo produktów i transportu, środowisko, żywność, zdrowie publiczne, ochrona konsumentów, prywatność i dane, systemy IT, interesy finansowe UE, rynek wewnętrzny, konstytucyjne wolności.
PRAWO PRACY NIE jest objęte. Pracodawca może rozszerzyć procedurę na regulacje wewnętrzne i etykę — zalecane, by objąć mobbing i dyskryminację.
Ochrona sygnalisty (dobra wiara, uzasadnione podstawy): zakaz działań odwetowych (wypowiedzenie, obniżka, pominięcie w awansie, mobbing, zła opinia); ciężar dowodu na pracodawcy; odszkodowanie nie niższe niż przeciętne miesięczne wynagrodzenie w gospodarce (obwieszczenie GUS za poprzedni rok); roszczenia także dla osób pomagających.
Sankcje karne: utrudnianie zgłoszeń, odwet, naruszenie poufności, brak procedury (grzywna), świadomie fałszywe zgłoszenie.
Zgłoszenia zewnętrzne — RPO i organy publiczne. Ujawnienie publiczne — ostateczność.
Kadry: procedura sygnalistów ≠ polityka antymobbingowa, ale można je zintegrować. Dane sygnalisty — poufne, poza aktami.

## Praca zdalna (art. 67¹⁸–67³³ KP, od 7.04.2023)
Trzy rodzaje: całkowita, hybrydowa, okazjonalna.
| Element | Zasada |
|---|---|
| uzgodnienie | przy zawarciu umowy albo w trakcie — wniosek papierowy lub elektroniczny |
| wniosek WIĄŻĄCY | ciężarna; rodzic dziecka do 4 lat; rodzic dziecka z niepełnosprawnością; opiekun osoby z niepełnosprawnością — odmowa tylko, gdy niemożliwe ze względu na organizację lub rodzaj pracy; odpowiedź 7 dni |
| polecenie pracodawcy | tylko w stanie nadzwyczajnym lub epidemii albo gdy zapewnienie BHP w zakładzie jest czasowo niemożliwe; oświadczenie pracownika o warunkach |
| zasady | porozumienie ze związkami, regulamin (po konsultacji), porozumienie indywidualne lub polecenie: grupy, kontrola, koszty, BHP, komunikacja |
| obowiązki pracodawcy | materiały, narzędzia (lub ekwiwalent za własne), instalacja, serwis, szkolenia; POKRYCIE KOSZTÓW energii i usług telekomunikacyjnych — ryczałt lub ekwiwalent odpowiadający przewidywanym kosztom, bez PIT i ZUS; ocena ryzyka i informacja BHP; oświadczenie pracownika o bezpiecznych warunkach lokalowych i technicznych; zakaz prac niebezpiecznych |
| kontrola | praca, BHP, bezpieczeństwo informacji — w uzgodnieniu z pracownikiem, w godzinach pracy, bez naruszania prywatności |
| cofnięcie | na wniosek każdej strony w 30 dni; nie dla grup z wnioskiem wiążącym bez przyczyny |
| wypadek przy pracy zdalnej | oględziny miejsca za zgodą |
| OKAZJONALNA | do 24 dni w roku na wniosek; bez obowiązku kosztów i ekwiwalentu (można); bez regulaminu; ewidencja dni, oświadczenie BHP; nieproporcjonalna do etatu |
| praca zdalna z zagranicy | ryzyko podatkowe i ZUS (A1, 183 dni) — uzgodnij miejsce |

## RODO w kadrach — podstawy
| Przepis | Zasada |
|---|---|
| art. 22¹ KP | dane obowiązkowe |
| art. 22¹ᵃ | zgoda na inne dane — nie może być warunkiem |
| art. 22¹ᵇ | biometria tylko do kontroli dostępu do pomieszczeń lub informacji szczególnie ważnych |
| art. 22¹ᶜ–22¹ʰ — KONTROLA TRZEŹWOŚCI i na środki odurzające (od 21.02.2023) | w regulaminie lub obwieszczeniu: grupy, metoda, częstotliwość; informacja 2 tygodnie przed; alkomat z dokumentem kalibracji; wynik ≥ 0,2‰ (0,1 mg/dm³) = niedopuszczenie; wynik w aktach E tylko gdy niezbędny — rok albo do zakończenia postępowania; badanie przez policję na żądanie |
| art. 22² — MONITORING wizyjny | cele: bezpieczeństwo pracowników, ochrona mienia, kontrola produkcji, tajemnica; nie w pomieszczeniach związkowych, sanitarnych, szatniach, stołówkach — chyba że konieczne, bez naruszania godności, za zgodą związków; nagrania 3 miesiące (dłużej — jako dowód); regulamin + informacja 2 tygodnie przed; oznaczenie; informacja na piśmie przed dopuszczeniem |
| art. 22³ — monitoring poczty i inne formy (GPS, systemy IT) | bez naruszania tajemnicy korespondencji i dóbr |

## RODO w kadrach — organizacja
- Upoważnienia do przetwarzania: kadry, kierownicy — z zakresem.
- Rejestr czynności (RCPD). Umowy powierzenia: biuro rachunkowe, dostawca benefitów, systemy chmurowe. Medycyna pracy i ZUS — odrębni administratorzy. IOD — gdy wymagany.
| Dane | Retencja |
|---|---|
| akta | 10 lat |
| rekrutacja | do końca procesu |
| ZFŚS | niezbędność; przegląd co rok |
| monitoring | 3 miesiące |
| listy obecności, wnioski | jak dokumentacja |
- Prawa pracownika: dostęp i kopia — 1 miesiąc; sprostowanie.
- Naruszenia: ocena ryzyka; zgłoszenie do UODO w 72 h; informacja dla osób przy wysokim ryzyku — np. wysłanie listy płac do niewłaściwego odbiorcy.
- Zasady: minimalizacja (nie kopiujesz dowodu osobistego — tylko dane; PESEL tak), szyfrowanie, czyste biurko, kontrola dostępu do akt."""

WYJASNIENIA["kontrola_pip_zus"] = """## PIP (ustawa z 13.04.2007)
Inspektor kontroluje BEZ UPRZEDZENIA — nie stosuje się zawiadomienia z Prawa przedsiębiorców (Konwencja MOP nr 81). O każdej porze, po okazaniu legitymacji; upoważnienie doręcza najpóźniej w 7 dni.
Uprawnienia: wstęp na teren; wgląd w dokumenty (akta, ewidencja czasu pracy, listy płac, regulaminy, umowy cywilnoprawne, dokumenty cudzoziemców, BHP, ZFŚS); kopie; przesłuchanie pracodawcy i pracowników, także byłych; oględziny; nagrania; wezwanie do siedziby PIP.
Przedmiot kontroli: legalność zatrudnienia (umowy, cudzoziemcy, zgłoszenia ZUS), wynagrodzenia i terminy, czas pracy, urlopy, BHP, umowy cywilnoprawne (art. 22), minimalna stawka godzinowa, równe traktowanie, jawność w rekrutacji, sygnaliści, mobbing (od 2026).

| Środek PIP | Co oznacza |
|---|---|
| NAKAZ (BHP) | usunięcie uchybień w terminie lub natychmiast; wstrzymanie prac; skierowanie do innych prac |
| NAKAZ PŁACOWY | wypłata należnego wynagrodzenia lub świadczenia — natychmiast wykonalny |
| WYSTĄPIENIE | usunięcie naruszeń prawa — odpowiedź w 30 dni z informacją o realizacji |
| POLECENIE | ustne |
| MANDAT | 1 000–2 000 zł; do 5 000 przy ponownym wykroczeniu w 2 lata |
| WNIOSEK DO SĄDU o ukaranie | grzywna 1 000–30 000 zł (art. 281–283 KP); za cudzoziemców 3 000–50 000 |
| ZAWIADOMIENIE PROKURATURY | art. 218 KK — złośliwe lub uporczywe naruszanie praw pracownika; art. 219 — niezgłoszenie do ZUS; art. 220 — narażenie życia |
| POWÓDZTWO o ustalenie stosunku pracy | projekt 2025/2026: decyzja administracyjna inspektora przekształcająca umowę cywilnoprawną w umowę o pracę — status: projekt, śledź |
| wpis do rejestru | — |
Protokół: podpisujesz z możliwością ZASTRZEŻEŃ w 7 dni (inspektor rozpatruje, uzupełnia). Odwołanie od nakazu (decyzji) — do okręgowego inspektora pracy w 14 dni (KPA), dalej skarga do WSA.
Najczęstsze ustalenia (sprawozdania GIP): nieterminowe lub zaniżone wynagrodzenia i nadgodziny; braki w ewidencji czasu pracy; umowy cywilnoprawne w warunkach etatu; brak badań i szkoleń BHP; niewydanie świadectw; nieudzielenie zaległych urlopów; ewidencja godzin zleceniobiorców; brak potwierdzenia umowy przed dopuszczeniem; jawność w rekrutacji (od 2026).

## ZUS (art. 86–97 ustawy systemowej)
| Element | Zasada |
|---|---|
| zawiadomienie o zamiarze kontroli | kontrola nie wcześniej niż 7 i nie później niż 30 dni od doręczenia (Prawo przedsiębiorców); upoważnienie |
| zakres | zgłaszanie, obliczanie i opłacanie składek; uprawnienia do świadczeń i ich wypłata; dokumentacja; zgłoszenia wypadków |
| limit czasu kontroli w roku | mikro 12 dni roboczych; mały 18; średni 24; duży 48 |
| protokół | zastrzeżenia w 14 dni |
| decyzja | odwołanie do sądu okręgowego (pracy i ubezpieczeń) w miesiąc; korekty w 30 dni |
| sankcje | grzywna do 5 000 zł (art. 98 — niezgłoszenie, nieprowadzenie dokumentacji, nieopłacanie); opłata dodatkowa do 100% składek; odsetki; przedawnienie 5 lat |
| po kontroli | wniosek o interpretację (art. 83d) na przyszłość |
Typowe ustalenia: składki od benefitów i ZFŚS bez kryterium; umowy o dzieło = zlecenia; zbiegi tytułów; podstawa zasiłków (uzupełnianie, składniki); wypłaty po ustaniu; zaniżone kody; zdrowotna przedsiębiorców.

## Urząd skarbowy i UODO
| Organ | Zakres | Sankcje |
|---|---|---|
| US | kontrola podatkowa lub celno-skarbowa płatnika: zaliczki, PIT-11, świadczenia nieodpłatne, ryczałt zdalny, 50% KUP; czynności sprawdzające | KKS: art. 77 — niewpłacenie zaliczki, do 720 stawek dziennych; art. 78–80 — niepobranie, niezłożenie informacji; czynny żal (art. 16 KKS) przed wszczęciem — złóż korektę i wpłać |
| UODO | kontrola z zawiadomieniem lub bez | kary do 20 mln € / 4% obrotu (praktyka polska: od kilku do setek tysięcy zł — np. brak zabezpieczeń, wyciek danych kadrowych); upomnienia; nakazy |
Typowe ustalenia UODO: nadmiarowe dane w rekrutacji, kopie dowodów, brak upoważnień, monitoring bez regulaminu, brak zgłoszenia naruszenia w 72 h.

## Przygotowanie firmy
1. KSIĄŻKA KONTROLI (obowiązek przedsiębiorcy) + rejestr upoważnień.
2. „TECZKA KONTROLNA” aktualizowana co kwartał: KRS/CEIDG; regulaminy (pracy, wynagradzania, ZFŚS, pracy zdalnej, kontroli trzeźwości, antymobbingowy, sygnaliści) z datami i potwierdzeniami zapoznania; układ i porozumienia; obwieszczenie o czasie pracy i okresach rozliczeniowych; oceny ryzyka; rejestry wypadków i chorób zawodowych; pomiary czynników; wykaz prac wzbronionych; PEL/UPL-1; umowy powierzenia; RCPD; upoważnienia RODO; ewidencja czasu pracy i urlopów za 3 lata w zasięgu ręki; listy płac i potwierdzenia przelewów; kopie DRA i potwierdzenia ZUS; PIT-4R/11; dokumenty cudzoziemców.
3. AUDYT WEWNĘTRZNY raz w roku checklistą (60 pytań z tygodnia 15) — wyniki, plan naprawczy z terminami i właścicielami.
4. Podczas kontroli: osoba kontaktowa (kadry) + pełnomocnictwo; udostępniasz to, o co proszą (kopie potwierdzone); notatki z przebiegu; nie podpisujesz oświadczeń „na szybko”; pytasz o zakres i podstawę; termin na dokumenty niedostępne na miejscu; uprzejmość; prawnik przy dużych ustaleniach.
5. Po kontroli: analiza protokołu (zastrzeżenia w terminie!); realizacja nakazów i wystąpień z dowodami; odpowiedź w 30 dni; korekty ZUS/PIT; poprawa procedur; informacja dla zarządu o ryzykach i kosztach."""
