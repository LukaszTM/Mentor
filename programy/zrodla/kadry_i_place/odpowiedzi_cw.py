# -*- coding: utf-8 -*-
"""Klucze odpowiedzi do ćwiczeń w lekcjach — sprawdzane automatycznie w Mentorze (pole „odpowiedzi” ćwiczenia; moduł odpowiedzi.py).

ODPOWIEDZI[id_lekcji][numer_ćwiczenia] = lista pól. Każda wartość MUSI występować w „wynik” albo „rozwiazanie” ćwiczenia —
pilnuje tego zbuduj.py i test testy/test_odpowiedzi.py (klucz nie może się rozjechać z rozwiązaniem).
Pole „bledy” = typowa pomyłka + podpowiedź, skąd się wzięła (Mentor pokazuje ją zamiast suchego „nie zgadza się”)."""

TN = ["tak", "nie"]
LEG = ["zgodne z prawem", "niezgodne z prawem"]
PYT = ["dozwolone", "zakazane", "dozwolone pod warunkiem"]
PRZER = ["zgodne z prawem", "do przerobienia", "zakazane"]


def kw(i, et, w, **k):
    return dict(id=i, etykieta=et, typ="kwota", wartosc=w, **k)


def li(i, et, w, **k):
    return dict(id=i, etykieta=et, typ="liczba", wartosc=w, **k)


def da(i, et, w, **k):
    return dict(id=i, etykieta=et, typ="data", wartosc=w, **k)


def tx(i, et, w=None, **k):
    d = dict(id=i, etykieta=et, typ="tekst", **k)
    if w is not None:
        d["wartosc"] = w
    return d


def wy(i, et, opcje, w, **k):
    return dict(id=i, etykieta=et, typ="wybor", opcje=list(opcje), wartosc=w, **k)


def bl(w, kom):
    return {"wartosc": w, "komunikat": kom}


ODPOWIEDZI = {
    # ------------------------------------------------------------------ etap 0
    "zrodla_prawa": {
        1: [kw("stawka", "Minimalna stawka godzinowa w 2026 r. (zł)", 31.40, bledy=[bl(32.30, "to stawka na 2027 r. — pytanie dotyczy 2026")]),
            li("poz", "Pozycja w Dz.U. 2025 (rozporządzenie RM z 11.09.2025)", 1242)],
        2: [wy("mozna", "Czy stały dodatek nocny 5,50 zł/h jest dopuszczalny?", TN, "nie"),
            kw("ustawowy", "Ustawowy dodatek nocny za 1 h w listopadzie 2026 (zł)", 6.01)],
    },
    "narzedzia_kadrowca": {
        2: [da("zus10", "ZUS za październik 2026 — ostatni dzień", "2026-11-16", bledy=[bl("2026-11-15", "15.11.2026 to niedziela — termin przesuwa się na następny dzień roboczy")]),
            da("zus11", "ZUS za listopad 2026 — ostatni dzień", "2026-12-15"),
            da("pit11", "Zaliczki PIT za listopad 2026 — ostatni dzień", "2026-12-21", bledy=[bl("2026-12-20", "20.12.2026 to niedziela — termin przesuwa się na poniedziałek")])],
    },
    "wskazniki_2026": {
        1: [kw("spol", "Składki społeczne pracownika razem (zł)", 740.34),
            kw("zdr", "Składka zdrowotna (zł)", 419.37, bledy=[bl(486.00, "9% liczysz od podstawy PO odjęciu składek społecznych, nie od brutto")]),
            kw("podst", "Podstawa zaliczki PIT (pełne zł)", 4491, bledy=[bl(4410, "wpłata pracodawcy do PPK (81,00) jest przychodem pracownika — dolicz ją do podstawy")]),
            kw("zal", "Zaliczka PIT (pełne zł)", 239, bledy=[bl(229, "zabrakło wpłaty pracodawcy do PPK w przychodzie"), bl(539, "zapomniałeś o kwocie zmniejszającej 300 zł (PIT-2)")]),
            kw("netto", "Netto do wypłaty (zł)", 3893.29, bledy=[bl(4011.29, "to netto bez PPK — Marek jest uczestnikiem (2% i 1,5%)"), bl(3593.29, "to netto bez PIT-2 — Marek złożył PIT-2 (300 zł)")])],
        2: [kw("spol", "Składki społeczne (zł)", 671.79), kw("zdr", "Składka zdrowotna (zł)", 380.54),
            kw("zal", "Zaliczka PIT (zł)", 0, bledy=[bl(186, "ulga dla młodych zeruje zaliczkę — przychód do 85 528 zł rocznie jest zwolniony")]),
            kw("netto", "Netto do wypłaty (zł)", 3749.67)],
    },
    "powtorka_etap_0": {
        1: [kw("nocne", "Dodatek nocny za 24 h (zł)", 144.24), kw("brutto", "Brutto razem (zł)", 4950.24), kw("spol", "Składki społeczne pracownika (zł)", 678.67),
            kw("zdr", "Składka zdrowotna (zł)", 384.44), kw("zal", "Zaliczka PIT (pełne zł)", 192), kw("netto", "Netto do wypłaty (zł)", 3596.13),
            kw("koszt", "Całkowity koszt pracodawcy (zł)", 6015.03)],
        2: [wy("premia", "Czy premia „do 10%” wystarczy, by zostawić pensje 4 806 zł w 2027 r.?", TN, "nie"),
            li("aneksy", "Ile osób z FIRMA.md wymaga aneksu od 1.01.2027?", 2),
            kw("pol", "Minimalne wynagrodzenie na 1/2 etatu w 2027 r. (zł)", 2475)],
    },
    # ------------------------------------------------------------------ etap 1
    "rekrutacja_jawnosc": {
        2: [wy("p1", "(1) „Czy planuje pani dzieci?”", PYT, "zakazane"), wy("p2", "(2) „Ile pani zarabiała u poprzedniego pracodawcy?”", PYT, "zakazane"),
            wy("p5", "(5) „Jakie ma pani uprawnienia na wózki?”", PYT, "dozwolone"), wy("p6", "(6) „Jakie są pani oczekiwania finansowe?”", PYT, "dozwolone")],
    },
    "umowa_o_prace": {
        1: [wy("a", "(a) Czy umowa próbna mogła trwać 3 miesiące?", TN, "tak"), li("mies", "(b) Wykorzystane miesiące z limitu 33", 12),
            li("umowy", "(b) Wykorzystane umowy z limitu 3", 1), da("max", "(c) Druga umowa na czas określony — najpóźniej do", "2029-09-30")],
        2: [li("licznik", "Która to umowa w limicie 3 (po aneksie)?", 2), li("mies", "Łączna liczba miesięcy po aneksie", 34),
            da("bezterm", "Od kiedy umowa jest z mocy prawa bezterminowa", "2027-12-01"), da("max", "Najpóźniejszy legalny koniec umowy określonej", "2027-11-30")],
    },
    "onboarding_akta": {
        1: [da("zua", "ZUA — ostatni dzień", "2026-10-08"), da("info", "Informacja o warunkach zatrudnienia (art. 29 §3) — ostatni dzień", "2026-10-08"),
            wy("orz", "Część akt: orzeczenie lekarskie z badań wstępnych", ["A", "B", "C", "D", "E"], "A"),
            wy("um", "Część akt: umowa o pracę", ["A", "B", "C", "D", "E"], "B"),
            da("ppk", "Ustawowy termin zawarcia umowy o prowadzenie PPK", "2027-01-10")],
    },
    "czas_pracy_systemy": {
        1: [li("sty", "Wymiar czasu pracy — styczeń 2027 (h)", 152, bledy=[bl(160, "odjąłeś tylko jedno święto — w styczniu 2027 są dwa w dni robocze (1.01 i 6.01)")]),
            li("kwi", "Wymiar — kwiecień 2027 (h)", 176, bledy=[bl(168, "Poniedziałek Wielkanocny 2027 wypada 29 marca, nie w kwietniu")]),
            li("maj", "Wymiar — maj 2027 (h)", 144, bledy=[bl(152, "święto w sobotę (1.05) też obniża wymiar o 8 h — art. 130 §2 KP")])],
        2: [wy("a", "(a) Czy 6 dni × 10 h tygodniowo jest dopuszczalne?", TN, "nie"), li("dob", "(c) Minimalny odpoczynek dobowy (h)", 11),
            li("tyg", "(c) Minimalny odpoczynek tygodniowy (h)", 35), li("limit", "Roczny limit nadgodzin z Kodeksu pracy (h)", 150)],
    },
    "nadgodziny_noc": {
        1: [kw("stawka", "Stawka godzinowa (zł)", 33.75, bledy=[bl(32.14, "dzielisz przez wymiar listopada 2026 (160 h), nie przez 168")]),
            kw("norm", "Normalne wynagrodzenie za 10 nadgodzin (zł)", 337.50), kw("d50", "Dodatek 50% (zł)", 101.25), kw("d100", "Dodatek 100% (zł)", 135.00),
            kw("razem", "Razem za nadgodziny (zł)", 573.75)],
        2: [kw("nocny", "(a) Dodatek nocny za 64 h (zł)", 384.64), kw("g13", "(b) Normalne wynagrodzenie + dodatek 100% za 13. godzinę (zł)", 67.50),
            li("wolne", "(c) Czas wolny za 1 nadgodzinę udzielany bez wniosku pracownika (h)", 1.5, bledy=[bl(1, "1:1 jest tylko NA WNIOSEK pracownika; bez wniosku — w wymiarze o połowę wyższym")]),
            li("odp", "(d) Wymagany odpoczynek dobowy (h)", 11)],
    },
    "praktyki_hr_zagranica": {
        2: [wy("a", "(a) „Trzy ostrzeżenia = zwolnienie”", PRZER, "do przerobienia"), wy("b", "(b) Zawieszenie bez wynagrodzenia", PRZER, "zakazane"),
            wy("c", "(c) Kara 200 zł za spóźnienie", PRZER, "zakazane"), wy("d", "(d) Obowiązkowe exit interview z przełożonym", PRZER, "do przerobienia"),
            wy("e", "(e) Ocena 1–5 bez kryteriów decydująca o premii", PRZER, "do przerobienia")],
    },
    "urlop_wypoczynkowy": {
        1: [li("nowak_d", "Nowak — urlop (dni)", 13), li("nowak_h", "Nowak — urlop (godziny)", 104),
            li("kowal", "Kowalczyk — urlop u Ciebie w 2026 (dni)", 6, bledy=[bl(7, "sama proporcja to za mało — sprawdź limit roczny i urlop wykorzystany u poprzedniego pracodawcy (art. 155³ §2)")]),
            li("krawczyk", "Krawczyk — urlop nabyty do końca 2026 (dni)", 10)],
        2: [da("termin", "(a) Zaległy urlop za 2024 należało udzielić do", "2025-09-30"), wy("b", "(b) Czy pracodawca może udzielić zaległego urlopu bez zgody pracownika?", TN, "tak"),
            da("przed", "(c) Roszczenie o urlop za 2024 przedawnia się", "2028-09-30")],
    },
    "staz_pracy_2026": {
        1: [li("przed", "Wymiar urlopu przed doliczeniem nowych okresów (dni)", 26), li("po", "Wymiar urlopu po doliczeniu (dni)", 26),
            li("zlec", "Lata doliczone ze zleceń", 2, bledy=[bl(3, "okresy równoległe (drugie zlecenie 2017–2018) nie liczą się podwójnie")]),
            li("dzial", "Lata doliczone z działalności", 3), da("od", "Od kiedy stosujesz nowy staż", "2026-05-01", bledy=[bl("2026-11-01", "liczy się dzień stosowania ustawy u prywatnego pracodawcy, nie dzień wpływu zaświadczenia")])],
        2: [da("od", "(a) Prawo do 26 dni urlopu od", "2026-05-01"), li("uzup", "(a) Urlop uzupełniający za 2026 (dni)", 6),
            wy("b", "(b) Czy wydłuża się okres wypowiedzenia?", TN, "nie"), wy("c", "(c) Czy wyrównujesz urlop za 2025 r.?", TN, "nie")],
    },
    "urlopy_rodzicielskie": {
        1: [da("mac", "Ostatni dzień urlopu macierzyńskiego", "2027-04-21"), da("obow", "Ostatni dzień 14 obowiązkowych tygodni", "2027-03-10"),
            da("wniosek", "Wniosek o 81,5% — ostatni dzień", "2026-12-24"), da("rodz", "Ostatni dzień urlopu rodzicielskiego matki (32 tyg.)", "2027-12-01"),
            tx("k311", "Kod RSA — zasiłek za urlop macierzyński", "311"), tx("k338", "Kod RSA — 9 nieprzenoszalnych tygodni ojca", "338"),
            li("proc", "Zasiłek ojca za 9 tygodni (% podstawy)", 70)],
        2: [wy("a", "(a) Czy umowa próbna rozwiąże się 31.12?", TN, "nie"), wy("b", "(b) Czy pracodawca może ją wypowiedzieć w ciąży (poza art. 52 i likwidacją)?", TN, "nie"),
            wy("c", "(c) Czy po przedstawieniu zaświadczenia może dalej pracować w nocy?", TN, "nie"),
            wy("d", "(d) Kto wypłaca zasiłek macierzyński po ustaniu umowy?", ["pracodawca", "ZUS"], "ZUS")],
    },
    "nieobecnosci_inne": {
        1: [kw("sila", "Pomniejszenie za 4 h siły wyższej (zł)", 65, bledy=[bl(130, "za czas zwolnienia z powodu siły wyższej przysługuje POŁOWA wynagrodzenia — potrącasz 50%")]),
            kw("opiek", "Pomniejszenie za 16 h urlopu opiekuńczego (zł)", 520), kw("wyn", "Wynagrodzenie za miesiąc (zł)", 4615),
            tx("kod", "Kod przerwy RSA dla urlopu opiekuńczego", "131")],
        2: [li("h", "(a) Za ile godzin potrącasz 50%?", 12, bledy=[bl(8, "dzień zwolnienia to cała zaplanowana zmiana — tutaj 12 h")]),
            wy("b", "(b) Czy drugi wniosek w tym roku może być „w godzinach”?", TN, "nie"), li("zost", "(c) Ile godzin zostaje w trybie godzinowym po 12 h?", 4)],
    },
    "powtorka_etap_1": {
        1: [li("staz", "Staż urlopowy (lata)", 14), li("urlop", "Urlop u Ciebie w roku zatrudnienia (dni)", 22, bledy=[bl(21, "niepełny dzień urlopu zaokrąglasz w górę (art. 155³ §1)")]),
            kw("stawka", "Stawka godzinowa (zł)", 32.50), kw("nadg", "Wynagrodzenie za 6 nadgodzin z dodatkiem 50% (zł)", 292.50),
            kw("opiek", "Pomniejszenie za 16 h urlopu opiekuńczego (zł)", 520)],
        2: [wy("p1", "(1) Próbna 3 mies., potem określona na 4 mies.", LEG, "niezgodne z prawem"), wy("p2", "(2) Grafik w czwartek na następny tydzień", LEG, "niezgodne z prawem"),
            wy("p3", "(3) Ryczałt nocny 150 zł dla wszystkich operatorów", LEG, "niezgodne z prawem"), wy("p4", "(4) Urlop w równoważnym zawsze po 8 h", LEG, "niezgodne z prawem")],
    },
}

MIES = ["lipiec", "sierpień", "wrzesień", "październik", "listopad"]
ZUSPIT = ["tak", "nie"]
L4 = ["utrata świadczenia", "brak sankcji", "najpierw wezwanie do wyjaśnień"]
DZ = ["dzieło", "zlecenie"]
B2B = ["bezpieczne B2B", "ryzyko uznania za stosunek pracy"]

# ---------------------------------------------------------------------- etap 2: płace
ODPOWIEDZI.update({
    "lista_plac_krok": {
        1: [kw("brutto", "Brutto razem (zł)", 5773.75), kw("spol", "Składki społeczne pracownika (zł)", 791.59), kw("zdr", "Składka zdrowotna (zł)", 448.39),
            kw("podst", "Podstawa zaliczki PIT (pełne zł)", 4819), kw("zal", "Zaliczka PIT (pełne zł)", 278), kw("ppk", "PPK pracownika (zł)", 115.48),
            kw("netto", "Netto do wypłaty (zł)", 4140.29)],
        2: [kw("pensja", "Pensja za część miesiąca (zł)", 3600),
            kw("spol", "Składki społeczne (zł)", 493.56, bledy=[bl(676.53, "wynagrodzenie chorobowe nie jest podstawą składek społecznych — liczysz je tylko od 3 600")]),
            kw("zdr", "Składka zdrowotna (zł)", 399.69, bledy=[bl(279.58, "wynagrodzenie chorobowe WCHODZI do podstawy składki zdrowotnej")]),
            kw("zal", "Zaliczka PIT (pełne zł)", 209), kw("netto", "Netto do wypłaty (zł)", 3760.35)],
    },
    "zaliczka_pit": {
        1: [kw("mazur", "(1) Mazur — zaliczka z PIT-2 i KUP 300 (zł)", 472), kw("mazur_bez", "(1) Mazur — zaliczka bez PIT-2 (zł)", 772),
            kw("nowak", "(2) Nowak — zaliczka u Ciebie, bez PIT-2 (zł)", 229), kw("krol", "(3) Król — zaliczka z PIT-2 (zł)", 0),
            kw("krol_bez", "(3) Król — zaliczka bez PIT-2 (zł)", 295)],
        2: [kw("czerwiec", "(a) Dochód narastająco po czerwcu (zł)", 89804), wy("mies", "(a) Miesiąc przekroczenia progu 120 000 zł", MIES, "wrzesień"),
            kw("zal", "(b) Zaliczka za wrzesień (pełne zł)", 2330, bledy=[bl(3553, "32% stosujesz tylko do nadwyżki ponad próg — część do progu nadal po 12%")]),
            wy("limit", "(c) Czy w tym roku przekroczy limit 30-krotności?", TN, "nie")],
    },
    "koszt_pracodawcy": {
        1: [kw("mazur_skl", "Mazur — składki pracodawcy miesięcznie (zł)", 1560.78), kw("mazur_rok", "Mazur — koszt roczny z odpisem ZFŚS (zł)", 115272.59),
            kw("lis_mies", "Lis — koszt miesięczny z PPK (zł)", 17011.40), kw("lis_rok", "Lis — koszt roczny z odpisem ZFŚS (zł)", 207080.03),
            kw("nowak_skl", "Nowak — składki pracodawcy miesięcznie (zł)", 439.00, bledy=[bl(500.25, "FP nie płacisz, gdy łączna podstawa ze wszystkich tytułów (3 800) jest niższa od minimalnego wynagrodzenia")]),
            kw("nowak_rok", "Nowak — koszt roczny z odpisem ZFŚS (zł)", 36739.62)],
        2: [kw("etat", "(a) Miesięczny koszt etatu 10 000 zł z PPK (zł)", 12151), kw("zlec", "(a) Miesięczny koszt zlecenia 10 000 zł (zł)", 12001),
            wy("c", "(c) Czy B2B z podporządkowaniem, wyznaczonym miejscem i czasem jest bezpieczne?", TN, "nie")],
    },
    "wynagrodzenie_urlopowe": {
        1: [kw("stawka", "(1) Stawka godzinowa ze składników zmiennych (zł)", 3.02), kw("url", "(1) Wynagrodzenie urlopowe ze zmiennych za 16 h (zł)", 48.32),
            kw("dzien", "(2) Ekwiwalent za 1 dzień (zł)", 272.47, bledy=[bl(271.43, "dzielisz przez współczynnik 20,92, nie przez 21 dni")]),
            kw("godz", "(2) Ekwiwalent za 1 godzinę (zł)", 34.06), kw("ekw", "(2) Ekwiwalent za 40 h (zł)", 1362.40)],
        2: [kw("chor", "Pomniejszenie za 6 dni choroby (zł)", 1080), kw("bezpl", "Pomniejszenie za 24 h urlopu bezpłatnego (zł)", 810,
                                                                    bledy=[bl(4320, "za urlop bezpłatny dzielisz przez wymiar godzin miesiąca (160) i mnożysz przez godziny nieobecności")]),
            kw("pensja", "Pensja za przepracowaną część miesiąca (zł)", 3510)],
    },
    "potracenia": {
        1: [kw("gran", "Granica potrącenia — 1/2 netto (zł)", 1946.65), kw("wolna", "Kwota wolna od potrąceń (zł)", 3501.73,
                                                                         bledy=[bl(3605.85, "to minimalne netto BEZ PPK — Marek jest uczestnikiem PPK, więc kwota wolna jest niższa")]),
            kw("potr", "Kwota potrącenia w tym miesiącu (zł)", 391.56, bledy=[bl(1200, "zajęcie na 1 200 zł nie oznacza potrącenia 1 200 — pracownikowi musi zostać kwota wolna"),
                                                                             bl(1946.65, "to granica 1/2, ale silniejsza jest kwota wolna: potrącasz tylko nadwyżkę netto ponad nią")])],
        2: [kw("gran", "Łączna granica przy zbiegu z alimentami — 3/5 netto (zł)", 5741.01), kw("alim", "Potrącenie alimentów (zł)", 2500),
            kw("inne", "Potrącenie na inne egzekucje (zł)", 3000), wy("zgoda", "Czy ratę za laptop można potrącić bez pisemnej zgody pracownika?", TN, "nie"),
            kw("laptop", "Najwyższa rata za laptop w tym miesiącu przy zgodzie (zł)", 566.62)],
    },
    "ppk": {
        1: [kw("kow_xi", "Kowalczyk — wpłata pracownika w listopadzie (zł)", 0, bledy=[bl(120, "umowy o prowadzenie jeszcze nie ma — wpłaty zaczynasz od wypłaty po jej zawarciu")]),
            kw("kow_prac", "Kowalczyk — docelowa wpłata pracownika (zł)", 120), kw("kow_firma", "Kowalczyk — docelowa wpłata pracodawcy (zł)", 90),
            kw("nowak_prac", "Nowak — wpłata pracownika 0,5% (zł)", 12.50), kw("nowak_firma", "Nowak — wpłata pracodawcy (zł)", 37.50,
                                                                              bledy=[bl(12.50, "obniżyć wpłatę może tylko uczestnik — pracodawca zawsze płaci co najmniej 1,5%")]),
            kw("krol_prac", "Król — wpłata pracownika (zł)", 70.00), kw("krol_firma", "Król — wpłata pracodawcy (zł)", 52.50)],
        2: [da("info", "(a) Informacja o autozapisie — ustawowy termin", "2027-02-28"), da("wyplata", "(c) Pierwsza wypłata z wpłatami PPK w AGRO-MLEKO", "2027-04-09"),
            da("przekaz", "(a) Termin przekazania tych wpłat do instytucji", "2027-05-17", bledy=[bl("2027-05-15", "15.05.2027 to sobota — termin przesuwa się na poniedziałek")]),
            wy("d", "(d) Czy osobie, która zrezygnowała 5.04, naliczasz wpłaty z wypłaty 9.04?", TN, "nie")],
    },
    "swiadczenia_pozaplacowe": {
        1: [wy("karta_zus", "Karta sportowa za 1 zł — składki ZUS?", ZUSPIT, "nie"), wy("karta_pit", "Karta sportowa za 1 zł — PIT?", ZUSPIT, "tak"),
            wy("posilek_zus", "Posiłek 300 zł/mies. — składki ZUS?", ZUSPIT, "nie"), wy("posilek_pit", "Posiłek 300 zł/mies. — PIT?", ZUSPIT, "tak"),
            wy("jub_zus", "Nagroda jubileuszowa co 5 lat — składki ZUS?", ZUSPIT, "nie"), wy("jub_pit", "Nagroda jubileuszowa — PIT?", ZUSPIT, "tak"),
            wy("szkol", "Szkolenie z Excela — ZUS lub PIT?", ZUSPIT, "nie"), wy("auto", "Auto służbowe do celów prywatnych — ZUS i PIT?", ZUSPIT, "tak")],
        2: [wy("paczki", "Czy paczki „po równo” korzystają z wyłączenia ze składek?", TN, "nie"), kw("paczki_wart", "Wartość paczek do oskładkowania (zł)", 18600),
            kw("karty", "Roczna wartość kart bez współfinansowania 1 zł (zł)", 72000)],
    },
    "delegacje": {
        1: [kw("diety", "Diety po pomniejszeniu za obiady (zł)", 45.00, bledy=[bl(90.00, "za każdy zapewniony obiad odejmujesz 50% diety (22,50 zł)")]),
            kw("km", "Kilometrówka (zł)", 713.00), kw("razem", "Razem należności (zł)", 1178.00), kw("wyplata", "Do wypłaty po zaliczce (zł)", 778.00)],
        2: [kw("diety", "Diety zagraniczne po pomniejszeniu (EUR)", 132.30), kw("razem", "Razem należności zagraniczne (EUR)", 496.00),
            kw("pln", "Do wypłaty po zaliczce (zł)", 1268.36), kw("kraj", "Dieta za odcinki krajowe (zł)", 22.50, bledy=[bl(45.00, "łącznie 8,5 h odcinków krajowych — od 8 do 12 h przysługuje połowa diety")])],
    },
    "chorobowe_podstawy": {
        1: [kw("marzec", "Marzec — wynagrodzenie chorobowe za 12 dni (zł)", 1601.52), li("pula", "Ile dni z puli 33 zostaje po lipcu?", 9),
            li("xi_dni", "Listopad — dni wynagrodzenia chorobowego", 9), kw("xi_chor", "Listopad — wynagrodzenie chorobowe (zł)", 1201.14),
            kw("xi_zas", "Listopad — zasiłek chorobowy (zł)", 800.76), tx("k_chor", "Kod RSA wynagrodzenia chorobowego", "331"), tx("k_zas", "Kod RSA zasiłku chorobowego", "313")],
        2: [li("dni", "(a) Luty — dni wynagrodzenia chorobowego", 14, bledy=[bl(26, "pracownik po 50. roku życia ma 14 dni wynagrodzenia chorobowego w roku, potem zasiłek"),
                                                                           bl(33, "33 dni dotyczy pracowników do 50 lat — tu limit to 14")]),
            kw("chor", "(a) Luty — wynagrodzenie chorobowe (zł)", 2512.72), kw("zas_ii", "(a) Luty — zasiłek (zł)", 2153.76), kw("zas_xi", "(a) Listopad — zasiłek (zł)", 3410.12),
            wy("c", "(c) Czy listopadowe zwolnienie otwiera nowy okres zasiłkowy?", TN, "tak"),
            wy("d", "(d) Kto wypłaca zasiłek?", ["pracodawca (płatnik zasiłków)", "ZUS"], "pracodawca (płatnik zasiłków)")],
    },
    "podstawa_zasilku": {
        1: [li("mies", "Z ilu miesięcy liczysz podstawę?", 11, bledy=[bl(12, "miesiąc, w którym przepracowano mniej niż połowę dni, wyłączasz")]),
            kw("marzec", "Marzec po uzupełnieniu (zł)", 5800), kw("podst", "Podstawa wymiaru (zł)", 5004.82), kw("dzien", "Stawka dzienna 100% (zł)", 166.83),
            kw("st80", "Stawka dzienna 80% (zł)", 133.46)],
        2: [wy("a", "(a) Czy ma prawo do świadczenia bez okresu wyczekiwania?", TN, "tak"), kw("podst", "(b) Podstawa wymiaru (zł)", 5177.40),
            kw("dzien", "(b) Stawka dzienna 100% (zł)", 172.58), kw("swiad", "(b) Świadczenie za 7 dni (zł)", 966.42),
            kw("min", "(c) Minimalna podstawa wymiaru w 2026 r. (zł)", 4147.10), kw("wojcik", "(c) Wójcik — stawka dzienna 80% (zł)", 110.59)],
    },
    "zasilki_inne": {
        1: [kw("st80", "Stawka dzienna zasiłku opiekuńczego 80% (zł)", 119.66), kw("zas", "Zasiłek za 5 dni (zł)", 598.30), kw("pensja", "Pensja za listopad (zł)", 4333.33),
            tx("kod", "Kod RSA zasiłku opiekuńczego", "312"), li("limit", "Ile dni opieki zostaje w roku obojgu rodzicom?", 35)],
        2: [da("prot", "(a) Protokół powypadkowy — najpóźniej", "2026-12-07"), li("proc", "(b) Zasiłek z ubezpieczenia wypadkowego (% podstawy)", 100),
            kw("dzien", "(b) Stawka dzienna (zł)", 140.94), kw("zas", "(b) Zasiłek za 23–30.11 (zł)", 1127.52), kw("pensja", "(b) Pensja za listopad (zł)", 3593.33),
            tx("kod", "(d) Kod RSA", "314")],
    },
    "kontrola_l4_2026": {
        1: [wy("s1", "(1) Sklep internetowy — wysyła paczki", L4, "utrata świadczenia"), wy("s2", "(2) Po operacji kolana jedzie na narty", L4, "utrata świadczenia"),
            wy("s3", "(3) Z depresją wyjeżdża do rodziny na wsi", L4, "brak sankcji"), wy("s4", "(4) Z grypą idzie do apteki i na zakupy", L4, "brak sankcji"),
            wy("s5", "(5) Na L4 ciążowym prowadzi płatne zajęcia jogi", L4, "utrata świadczenia"), wy("s6", "(6) Nie zastano go pod adresem z e-ZLA", L4, "najpierw wezwanie do wyjaśnień")],
        2: [wy("kier", "Czy kierownik bez imiennego upoważnienia może kontrolować?", TN, "nie"), wy("tel", "Czy telefon do pracownika jest kontrolą?", TN, "nie"),
            wy("dysc", "Czy naruszenie zwolnienia oznacza automatycznie art. 52?", TN, "nie"), li("zastrz", "Termin na zastrzeżenia do protokołu (dni)", 7)],
    },
    "zlecenie_dzielo": {
        1: [kw("p_min", "Pawlak — minimalna należność za 120 h (zł)", 3768), kw("p_zdr", "Pawlak — składka zdrowotna (zł)", 270.00), kw("p_zal", "Pawlak — zaliczka PIT (zł)", 288),
            kw("p_netto", "Pawlak — netto (zł)", 2442.00), kw("k_spol", "Król — składki społeczne (zł)", 479.85), kw("k_zdr", "Król — składka zdrowotna (zł)", 271.81),
            kw("k_netto", "Król — netto (zł)", 2678.34), kw("d_netto", "Dąbrowski (student do 26 lat) — netto (zł)", 2000)],
        2: [wy("u1", "(1) Projekt nowych etykiet", DZ, "dzieło"), wy("u2", "(2) Comiesięczne szkolenia BHP", DZ, "zlecenie"), wy("u3", "(3) Namalowanie muralu", DZ, "dzieło"),
            wy("u4", "(4) Sprzątanie biura 3 razy w tygodniu", DZ, "zlecenie"), wy("u5", "(5) Napisanie regulaminu ZFŚS", DZ, "dzieło"),
            wy("u6", "(6) Obsługa stoiska na targach", DZ, "zlecenie"), kw("n20", "(1) Netto przy KUP 20% (zł)", 2260), kw("n50", "(1) Netto przy KUP 50% (zł)", 2350),
            da("rud", "Termin zgłoszenia RUD", "2026-11-09")],
    },
    "cudzoziemcy_b2b": {
        1: [da("pup", "Powiadomienie PUP o podjęciu pracy — ostatni dzień", "2027-01-11"), da("zua", "ZUA — ostatni dzień", "2027-01-11"),
            kw("oplata", "Opłata za oświadczenie o powierzeniu pracy (zł)", 400), li("mies", "Maksymalny okres pracy na oświadczeniu (miesiące)", 24),
            wy("gruzja", "Czy obywatel Gruzji może dziś pracować na oświadczeniu?", TN, "nie")],
        2: [wy("a", "(A) informatyk", B2B, "ryzyko uznania za stosunek pracy"), wy("b", "(B) doradca podatkowy z własną kancelarią", B2B, "bezpieczne B2B"), wy("c", "(C) kierowca z własnym busem", B2B, "ryzyko uznania za stosunek pracy"),
            kw("skl", "(A) Zaległe składki w części pracownika za 36 miesięcy (zł)", 49356)],
    },
})

DOP = ["dopuszczalny", "niedopuszczalny", "dopuszczalny pod warunkiem"]
KWAL = ["mobbing", "dyskryminacja", "nierówne traktowanie bez kryterium dyskryminacyjnego", "jednorazowe naruszenie dóbr osobistych"]
KRAJ = ["Polska (ZUS)", "Czechy"]

# ---------------------------------------------------------------------- powtórka etapu 2, etap 3 i 4
ODPOWIEDZI.update({
    "powtorka_etap_2": {
        1: [kw("pensja", "Pensja po urlopie opiekuńczym (zł)", 4940), kw("oskl", "Przychód oskładkowany (zł)", 5740), kw("spol", "Składki społeczne (zł)", 786.95),
            kw("zdr", "Składka zdrowotna (zł)", 445.77), kw("zal", "Zaliczka PIT (pełne zł)", 275),
            kw("netto", "Netto do wypłaty (zł)", 3717.48, bledy=[bl(4117.48, "auto służbowe to świadczenie w naturze — zwiększa podstawy, ale nie jest wypłacane")]),
            tx("kod", "Kod przerwy RSA za dzień urlopu opiekuńczego", "131")],
        2: [kw("pensja", "Pensja za część miesiąca (zł)", 11666.67), kw("spol", "Składki społeczne (zł)", 5712.50), kw("zas", "Zasiłek chorobowy za 5 dni (zł)", 1610.75),
            kw("zdr", "Składka zdrowotna (zł)", 3235.88), kw("zal", "Zaliczka PIT 32% (pełne zł)", 11841), kw("netto", "Netto przed potrąceniem (zł)", 21654.71),
            kw("wypl", "Do wypłaty po alimentach (zł)", 18654.71)],
    },
    "zus_zgloszenia": {
        1: [li("zua", "Ile dokumentów ZUA składasz?", 3), li("zza", "Ile dokumentów ZZA?", 1), tx("kod", "Kod tytułu ubezpieczenia Ewy Sobczak (6 cyfr)", "011002"),
            da("rud", "RUD dla umowy o dzieło z 2.11 — ostatni dzień", "2026-11-09")],
        2: [wy("b", "(b) Dokumenty po powstaniu zbiegu od 1.09.2026", ["ZUA", "ZZA", "ZWUA + ZZA", "ZIUA"], "ZWUA + ZZA"),
            kw("prac", "(c) Nadpłata w części zleceniobiorcy (zł)", 1439.55), kw("firma", "(c) Nadpłata zleceniodawcy z FGŚP (zł)", 1843.80),
            kw("zdr", "(c) O ile rośnie składka zdrowotna miesięcznie (zł)", 43.19)],
    },
    "zus_rozliczenia": {
        1: [li("rca", "Ile wierszy RCA?", 8), kw("z313", "RSA 313 — zasiłek chorobowy (zł)", 800.76), kw("z312", "RSA 312 — zasiłek opiekuńczy (zł)", 598.30),
            tx("kod", "Kod RSA urlopu bezpłatnego 2–3.12", "111"), tx("ident", "Identyfikator kompletu", "01 12 2026"), da("termin", "Termin kompletu i składek", "2027-01-15")],
        2: [li("kompl", "(a) Ile kompletów za styczeń 2027?", 1), tx("ident", "(a) Identyfikator kompletu", "01 01 2027"),
            wy("rpa", "(b) Czy pensja za grudzień wypłacona 8.01 wymaga RPA?", TN, "nie"), da("termin", "(c) Termin kompletu", "2027-02-15"),
            kw("ods", "(c) Odsetki za 1 dzień zwłoki po zaokrągleniu (zł)", 52), wy("pobr", "(c) Czy ZUS pobierze te odsetki?", TN, "tak")],
    },
    "zus_korekty": {
        1: [da("od", "Data powstania obowiązku w ZUA", "2026-09-16"), kw("prac", "Niedopłata w części zleceniobiorcy (zł)", 337.80,
                                                                         bledy=[bl(411.30, "dobrowolne chorobowe (2,45%) nie działa wstecz — liczysz 11,26%")]),
            kw("firma", "Niedopłata zleceniodawcy z FGŚP (zł)", 526.80), kw("zdr", "Składka zdrowotna (zł)", 239.60), kw("pit", "Zaliczka PIT (zł)", 0)],
        2: [kw("prac", "(b) Składki w części ubezpieczonej (zł)", 844.50), kw("firma", "(b) Składki zleceniodawcy bez FGŚP (zł)", 1309.50), kw("zdr", "(b) Składka zdrowotna (zł)", 599.00),
            kw("razem", "(b) Razem do dopłaty bez odsetek (zł)", 2760.50), li("lata", "(d) Przedawnienie składek (lata)", 5)],
    },
    "pit_roczny": {
        1: [kw("przych", "Przychód w PIT-11 za 2026 (zł)", 12000, bledy=[bl(18000, "zasada kasowa: pensja za grudzień wypłacona 8.01.2027 to przychód roku 2027"),
                                                                          bl(12180, "w 2026 r. Anna nie ma jeszcze wpłat PPK — pierwsze będą w 2027")]),
            kw("kup", "Koszty uzyskania (zł)", 500), kw("skl", "Składki społeczne (zł)", 1645.20), kw("doch", "Dochód w PIT-11 — przychód minus koszty (zł)", 11500, bledy=[bl(9854.80, "w PIT-11 składek społecznych nie odejmujesz od dochodu — wykazujesz je osobno w poz. 95")]), kw("zal", "Zaliczki pobrane (zł)", 582),
            li("rok", "W PIT-11 za który rok trafi pensja za grudzień?", 2027)],
        2: [kw("p1", "(1) Niedopłata zaliczki od zasiłku (zł)", 30), kw("p2", "(2) Ryczałt od umowy 180 zł (zł)", 22),
            wy("dekl", "(2) Deklaracja dla tego ryczałtu", ["PIT-4R", "PIT-8AR", "PIT-11"], "PIT-8AR"), kw("p3", "(3) Brakująca zaliczka od zwrotu składek (zł)", 915),
            kw("razem", "Suma niedopłat (1) + (3) (zł)", 945)],
    },
    "prawo_ue_i_swiat": {
        1: [wy("b", "(B) Delegowanie na 30 miesięcy bez porozumienia wyjątkowego — ubezpieczenie", KRAJ, "Czechy"),
            wy("c", "(C) Praca w kilku państwach, ≥ 25% w państwie zamieszkania — ubezpieczenie", KRAJ, "Polska (ZUS)"),
            li("mies", "Najdłuższe delegowanie z A1 na podstawie art. 12 (miesiące)", 24), li("proc", "Próg „znacznej części pracy” w państwie zamieszkania (%)", 25)],
        2: [tx("wn", "Wniosek o A1 dla pracownika delegowanego (symbol formularza ZUS)", ["US-3", "US3"]), kw("podst", "Minimalna podstawa składek w 2027 r. (zł)", 10033),
            wy("pit", "PIT od pierwszego dnia pracy w Czechach — gdzie?", ["Polska", "Czechy"], "Czechy"),
            wy("diety", "Czy przy oddelegowaniu wypłacasz diety z rozporządzenia o podróżach służbowych?", TN, "nie")],
    },
    "zfss_pfron": {
        1: [kw("odpis", "Odpis na ZFŚS razem (zł)", 186387.50, bledy=[bl(186581.25, "zwiększenie 6,25% należy się tylko za stopień umiarkowany i znaczny — za 2 osoby, nie 3")]),
            kw("rata", "Rata 75% do 31 maja (zł)", 139790.63), kw("reszta", "Reszta do 30 września (zł)", 46596.87),
            kw("pfron", "Miesięczna wpłata na PFRON (zł)", 2243.88), kw("sod", "Dofinansowanie SOD (zł)", 0)],
        2: [wy("p1", "(1) Wczasy 1 500 zł „dla każdego, kto złoży wniosek”", DOP, "dopuszczalny pod warunkiem"), wy("p2", "(2) Karty 500 zł po równo dla wszystkich", DOP, "niedopuszczalny"),
            wy("p3", "(3) Pożyczka remontowa dla dyrektora", DOP, "dopuszczalny"), wy("p4", "(4) Nagroda za wyniki z funduszu", DOP, "niedopuszczalny")],
    },
    "kalendarz_roczny": {
        1: [da("wypl", "Wypłata pensji za grudzień 2026", "2027-01-08", bledy=[bl("2027-01-11", "wynagrodzenie wypłacasz dzień WCZEŚNIEJ, gdy termin wypada w dzień wolny (art. 85 §3) — odwrotnie niż w ZUS i PIT")]),
            da("zus", "Komplet ZUS i składki", "2027-01-15"), tx("ident", "Identyfikator tego kompletu", "01 12 2026"),
            da("pit", "PIT-4R, PIT-8AR i PIT-11 do urzędu", "2027-02-01", bledy=[bl("2027-01-31", "31.01.2027 to niedziela — termin przesuwa się na poniedziałek")])],
        2: [li("zus", "Osoba fizyczna z pracownikami — dzień miesiąca na ZUS", 20), wy("zfss", "14 etatów — ZFŚS obowiązkowy?", TN, "nie"), wy("pfron", "14 etatów — wpłaty na PFRON?", TN, "nie"),
            wy("sygn", "18 osób — procedura sygnalistów obowiązkowa?", TN, "nie"), wy("zas", "18 ubezpieczonych — kto wypłaca zasiłki?", ["pracodawca", "ZUS"], "ZUS"),
            wy("iwa", "18 ubezpieczonych — ZUS IWA?", TN, "tak")],
    },
    "powtorka_etap_3": {
        1: [da("zua", "ZUA nowego zleceniobiorcy — ostatni dzień", "2027-02-22"), da("zwua_d", "ZWUA Kowalczyk — data wyrejestrowania", "2027-03-01"),
            da("zwua_t", "ZWUA Kowalczyk — ostatni dzień", "2027-03-08", bledy=[bl("2027-03-07", "7.03.2027 to niedziela — termin przesuwa się na poniedziałek")]),
            da("kompl", "Komplet 01 02 2027 — termin", "2027-03-15"), da("pit", "Zaliczki PIT za wypłaty lutowe — termin", "2027-03-22"),
            tx("rsa", "W komplecie za który miesiąc wykażesz RSA 312 (zasiłek wypłacony 10.03)?", ["03 2027", "01 03 2027", "marzec 2027", "marzec", "03.2027", "03/2027", "3 2027", "03"])],
        2: [kw("skl", "(1) Składki do dopłaty bez odsetek (zł)", 2760.50), kw("sod", "(2) Nadpłacone dofinansowanie do zwrotu (zł)", 3100), kw("odpis", "(3) Korekta odpisu ZFŚS (zł)", 8241.04)],
    },
    "rozwiazanie_umowy": {
        1: [da("mazur", "Mazur — dzień rozwiązania umowy", "2027-02-28"), da("ziel", "Zieliński — dzień rozwiązania umowy", "2026-12-31"),
            da("kowal", "Kowalczyk — dzień rozwiązania umowy", "2026-12-05"), wy("probna", "Czy przy umowie próbnej podajesz przyczynę wypowiedzenia?", TN, "nie"),
            wy("l4", "Czy Krawczykowi przebywającemu na L4 można teraz wręczyć wypowiedzenie?", TN, "nie")],
        2: [da("koniec", "Poprawny koniec okresu wypowiedzenia", "2027-03-31", bledy=[bl("2027-01-31", "staż 6 lat daje 3-miesięczny okres wypowiedzenia, nie miesięczny")]),
            da("zwua_d", "ZWUA — data wyrejestrowania", "2027-04-01"), da("zwua_t", "ZWUA — ostatni dzień", "2027-04-07"), tx("tryb", "ZWUA — kod trybu", "23R"),
            tx("podst", "ZWUA — kod podstawy prawnej", "403"), da("ekw", "Ekwiwalent za urlop — najpóźniej", "2027-04-09")],
    },
    "odprawy_grupowe": {
        1: [da("dzien", "Mazur — dzień rozwiązania umowy", "2027-04-30"), kw("mazur", "Mazur — odprawa (zł)", 23400), kw("mazur_e", "Mazur — ekwiwalent za 80 h (zł)", 3728.80),
            kw("lis", "Lis — odprawa (zł)", 42000), kw("nowak", "Nowak — odprawa (zł)", 5000, bledy=[bl(7500, "7 lat i 8 miesięcy to przedział od 2 do 8 lat — dwie pensje, nie trzy")]),
            kw("ziel", "Zieliński — odprawa (zł)", 0, bledy=[bl(5400, "umowa wygasa z upływem czasu — to nie jest rozwiązanie z przyczyn niedotyczących pracownika"),
                                                          bl(10800, "tyle byłoby po wypowiedzeniu — ale umowy terminowej, która i tak wygasa, nie wypowiadasz")]),
            kw("limit", "Limit odprawy w 2027 r. (zł)", 74250)],
        2: [wy("a", "(a) Czy to zwolnienie grupowe?", TN, "nie"), li("prog", "(a) Ile osób liczysz do progu?", 9, bledy=[bl(13, "porozumienia stron liczysz dopiero, gdy jest ich co najmniej 5")]),
            wy("b", "(b) Czy ciężarnej wolno wręczyć wypowiedzenie definitywne?", TN, "nie"), li("dni", "(c) Po ilu dniach od zawiadomienia PUP najwcześniej rozwiążą się umowy?", 30)],
    },
    "swiadectwo_rozliczenie": {
        1: [li("urlop", "Urlop należny za 2026 r. (dni)", 19), kw("ekw", "Ekwiwalent za 5 dni (zł)", 1290.80), kw("pensja", "Pensja za przepracowaną część listopada (zł)", 1890),
            kw("zal", "Zaliczka PIT (pełne zł)", 1193, bledy=[bl(893, "po ustaniu zatrudnienia pomijasz PIT-2 — bez kwoty zmniejszającej 300 zł")]),
            kw("netto", "Netto przed potrąceniem (zł)", 8534.86), kw("kom", "Potrącenie komornicze razem (zł)", 4115.29), kw("wypl", "Do wypłaty (zł)", 4419.57),
            tx("tryb", "ZWUA — kod trybu", "46R"), tx("podst", "ZWUA — kod podstawy prawnej", "402")],
        2: [li("prac", "(a) Termin pracownika na wniosek o sprostowanie (dni)", 14), li("firma", "(a) Termin pracodawcy na odpowiedź (dni)", 7),
            wy("b", "(b) Czy zwykły PDF bez podpisu kwalifikowanego jest świadectwem pracy?", TN, "nie"),
            li("pkt", "(c) Numer punktu w ust. 6 wzoru dla pracy w szczególnych warunkach", 14), da("ekw", "(d) Ekwiwalent za urlop — najpóźniej", "2026-12-10")],
    },
    "mobbing_dyskryminacja_2026": {
        1: [wy("k1", "(1) Codzienne publiczne wyśmiewanie od 2 miesięcy", KWAL, "mobbing"), wy("k2", "(2) Odmowa awansu „bo zajdzie w ciążę”", KWAL, "dyskryminacja"),
            wy("k3", "(3) Różne premie bez uzasadnienia", KWAL, "nierówne traktowanie bez kryterium dyskryminacyjnego"),
            wy("k4", "(4) Jednorazowe „leń” i przeprosiny", KWAL, "jednorazowe naruszenie dóbr osobistych"), wy("k5", "(5) Brak szkoleń dla 58-latka", KWAL, "dyskryminacja"),
            kw("min", "Minimalne zadośćuczynienie za mobbing w 2026 r. (zł)", 28836)],
        2: [li("potw", "Potwierdzenie przyjęcia zgłoszenia (dni)", 3), li("post", "Postępowanie wyjaśniające — najdłużej (dni)", 21), li("dec", "Decyzja po raporcie (dni)", 7),
            li("ret", "Retencja dokumentów postępowania (lata)", 3)],
    },
    "jawnosc_wynagrodzen": {
        1: [kw("m_sr", "Mężczyźni — średnia (zł)", 5230), kw("m_med", "Mężczyźni — mediana (zł)", 5200), kw("k_sr", "Kobiety — średnia (zł)", 5010),
            kw("k_med", "Kobiety — mediana (zł)", 5000), li("luka", "Luka wg średniej (%)", 4.2, tol=0.05), li("luka_m", "Luka wg mediany (%)", 3.8, tol=0.05),
            kw("po", "Różnica po odjęciu stażu i nocnych (zł)", 10)],
        2: [wy("p1", "(1) Klauzula poufności wynagrodzenia z karą umowną — dopuszczalna?", TN, "nie"), wy("p3", "(3) Samo „do uzgodnienia” w ogłoszeniu — wystarczy?", TN, "nie"),
            li("mies", "Termin odpowiedzi na wniosek wg dyrektywy (miesiące)", 2)],
    },
    "sygnalisci_zdalna_rodo": {
        1: [da("odp", "Odpowiedź na wniosek o pracę zdalną — najpóźniej", "2026-11-24"), kw("energia", "Koszt energii miesięcznie (zł)", 6.25), kw("ryczalt", "Ryczałt miesięczny po zaokrągleniu (zł)", 27),
            li("powrot", "Powrót z pracy zdalnej po wiążącym wniosku — najpóźniej (dni)", 30)],
        2: [li("uodo", "Zgłoszenie naruszenia ochrony danych do UODO (godziny)", 72), li("sygn", "Wejście w życie procedury sygnalistów po ogłoszeniu (dni)", 7),
            li("trzezw", "Informacja o kontroli trzeźwości przed jej rozpoczęciem (tygodnie)", 2), wy("obow", "Czy firma 62-osobowa musi mieć procedurę zgłoszeń wewnętrznych?", TN, "tak")],
    },
    "kontrola_pip_zus": {
        1: [wy("termin", "Czy kontrola 1.12 po zawiadomieniu z 20.11 mieści się w terminie?", TN, "tak"), li("zastrz", "Zastrzeżenia do protokołu ZUS (dni)", 14),
            li("kor", "Korekty po uprawomocnieniu decyzji (dni)", 7), wy("mandat", "Czy inspektor ZUS nakłada mandaty?", TN, "nie")],
        2: [wy("b", "(b) Czy odwołanie wstrzymuje wykonanie nakazu wypłaty?", TN, "nie"), li("zastrz", "(c) Zastrzeżenia do protokołu PIP (dni)", 7),
            kw("ods", "(d) Odsetki za opóźnienie (zł)", 337.63), kw("razem", "(d) Zaległość z odsetkami (zł)", 4717.63), kw("grzywna", "(a) Górna granica grzywny sądowej (zł)", 60000)],
    },
    "powtorka_etap_4": {
        2: [kw("mobb", "Minimalne zadośćuczynienie za mobbing (zł)", 28836), kw("pawlak", "Niedopłata na zleceniu Pawlak miesięcznie (zł)", 768),
            kw("zfss", "Kwota paczek narażona na oskładkowanie (zł)", 18600), kw("pfron", "Wpłata na PFRON miesięcznie (zł)", 5524)],
    },
})
