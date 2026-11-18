# -*- coding: utf-8 -*-
"""Kalendarz aktualizacji kursu — daty, po których trzeba sprawdzić przepis (Mentor przypomina na Panelu i pokazuje listę w Ściądze).
Każda pozycja: data (RRRR-MM-DD), temat, co sprawdzić, gdzie, lekcje, których dotyczy. Stan na 18.11.2026."""


def _a(data, temat, co, gdzie, *lekcje):
    return {"data": data, "temat": temat, "co": co, "gdzie": gdzie, "lekcje": list(lekcje)}


AKTUALIZACJE = [
    _a("2026-11-27", "PIT 2027 — podpis albo weto prezydenta",
       "Ustawa uchwalona 5–6.11.2026: próg 12% do 130 000 zł, nowa stawka 24% (130 000–150 000 zł), 32% powyżej. Ogłoszona w Dz.U. — od wypłat styczniowych 2027 zmieniasz próg w rachunku zaliczek; weto — zostaje 120 000 zł.",
       "dziennikustaw.gov.pl, sejm.gov.pl", "zaliczka_pit", "wskazniki_2026"),
    _a("2026-12-02", "Praca platformowa — termin wdrożenia dyrektywy 2024/2831",
       "Sprawdź status projektu UC160 (domniemanie stosunku pracy, zarządzanie algorytmiczne).", "legislacja.gov.pl", "prawo_ue_i_swiat", "cudzoziemcy_b2b"),
    _a("2026-12-20", "Diety i ryczałty za podróże służbowe 2027",
       "Projekt z 21.05.2026: dieta krajowa 60 zł, ryczałt za nocleg 90 zł, dojazdy 12 zł, limit hotelu 1 200 zł, nowe diety zagraniczne — planowo od 1.01.2027. Nowymi stawkami liczysz dopiero po ogłoszeniu w Dz.U.",
       "dziennikustaw.gov.pl", "delegacje"),
    _a("2026-12-31", "Jawność wynagrodzeń — projekt UC127",
       "Rada Ministrów planowała przyjęcie w IV kwartale 2026. Sprawdź: termin odpowiedzi na wniosek pracownika (projekt: 30 dni), kary 2 000–60 000 zł, pierwsze sprawozdania z luki płacowej.",
       "legislacja.gov.pl, sejm.gov.pl", "jawnosc_wynagrodzen", "rekrutacja_jawnosc"),
    _a("2027-01-01", "Nowy rok — wskaźniki 2027",
       "Minimalne 4 950 zł i 32,30 zł/h (aneksy, kwoty wolne od potrąceń, dodatek nocny, minimalna podstawa zasiłku), limit 30-krotności 300 990 zł, limit odprawy 74 250 zł, "
       "minimalne zadośćuczynienie za mobbing 29 700 zł; e-ZLA wystawiane na jeden tytuł ubezpieczenia. Zaktualizuj tabelę wskaźników i parametry programu kadrowego.",
       "Dz.U. 2026 poz. 1213; M.P. 2026 poz. 1098; zus.pl", "wskazniki_2026", "potracenia", "kontrola_l4_2026"),
    _a("2027-01-11", "Praca w upale — nowe przepisy BHP",
       "Od 11.01.2027 obowiązują progi 28/25°C i 35/32°C (Dz.U. 2026 poz. 927): przed latem przygotuj ocenę ryzyka i organizację pracy.", "eli.gov.pl/eli/DU/2026/927/ogl", "prawo_ue_i_swiat"),
    _a("2027-01-15", "PIT-11 tylko na wniosek? — projekt UDER105",
       "Stan na 17.11.2026: po konsultacjach publicznych, nie trafił do Sejmu; wersja z 28.04.2026 miała objąć już informacje za 2026 r. Przed wysyłką sprawdź, czy ustawę ogłoszono — jeśli nie, przekazujesz PIT-11 wszystkim.",
       "legislacja.gov.pl", "pit_roczny"),
    _a("2027-01-20", "Terminy roczne 2027 przesunięte przez niedziele",
       "PIT-4R, PIT-8AR i PIT-11 do urzędu oraz ZUS IWA — do 1.02.2027; PIT-11 i IFT-1R podatnikom oraz IMIR — do 1.03.2027; informację o autozapisie PPK przekaż do piątku 26.02.2027.",
       "podatki.gov.pl, zus.pl, mojeppk.pl", "kalendarz_roczny", "pit_roczny", "ppk"),
    _a("2027-02-20", "GUS — przeciętne wynagrodzenie i odpis na ZFŚS 2027",
       "Obwieszczenie Prezesa GUS (zwykle ok. 20 lutego). Do publikacji stosujesz odpis z 2026 r. (2 943,23 zł) i korygujesz po ogłoszeniu; sprawdź też ustawę okołobudżetową — bywa, że zamraża podstawę odpisu. "
       "Kwartalne przeciętne wynagrodzenie — do wpłat na PFRON.", "stat.gov.pl", "zfss_pfron"),
    _a("2027-03-01", "Kwoty wolne od potrąceń z zasiłków",
       "Od 1 marca nowe kwoty wolne po waloryzacji (komunikat Prezesa ZUS). Do 28.02.2027: 849,42 zł przy alimentach i 1 401,57 zł przy innych egzekucjach.", "zus.pl, Monitor Polski", "potracenia"),
    _a("2027-04-01", "PPK — ponowny autozapis; stopa wypadkowa na nowy rok składkowy",
       "Od 1.04.2027 wznawiasz wpłaty za osoby, które zrezygnowały i nie złożyły nowej deklaracji (pierwsza wypłata w AGRO-MLEKO: 9.04.2027). Stopa wypadkowa od 1.04 — z zawiadomienia ZUS (przychodzi do 20.04).",
       "mojeppk.pl, eZUS", "ppk", "koszt_pracodawcy"),
    _a("2027-05-05", "Mobbing — termin dostosowania regulaminów",
       "Do 5.05.2027 pracodawca zatrudniający co najmniej 10 pracowników ustala reguły, procedury i częstotliwość działań przeciw mobbingowi (art. 94³ᵃ KP) w regulaminie pracy, układzie albo odrębnym regulaminie.",
       "Dz.U. 2026 poz. 1046", "mobbing_dyskryminacja_2026"),
    _a("2027-06-07", "Jawność wynagrodzeń — pierwsze sprawozdania z luki płacowej",
       "Termin z dyrektywy 2023/970 dla pracodawców od 150 pracowników (dane za 2026 r.). Obowiązek w Polsce zależy od uchwalenia ustawy (UC127) — sprawdź stan i narzędzie GUS do sprawozdań.",
       "legislacja.gov.pl, stat.gov.pl", "jawnosc_wynagrodzen"),
    _a("2027-07-08", "PIP — koniec okresu „abolicji”",
       "Do 8.07.2027 pracodawca, który sam zamieni umowę cywilnoprawną na umowę o pracę, korzysta z ulg z reformy PIP. Przejrzyj zlecenia i B2B testem 8 cech stosunku pracy.",
       "Dz.U. 2026 poz. 473", "kontrola_pip_zus", "cudzoziemcy_b2b"),
    _a("2027-09-15", "Minimalne wynagrodzenie 2028",
       "Rada Ministrów wydaje rozporządzenie do 15 września: nowe minimum, stawka godzinowa i wszystkie wskaźniki pochodne (kwoty wolne, dodatek nocny, limity odpraw, minimalna podstawa zasiłku).",
       "dziennikustaw.gov.pl", "wskazniki_2026"),
    _a("2028-03-04", "Obywatele Ukrainy — koniec ochrony czasowej (status UKR)",
       "Ochrona czasowa obowiązuje do 4.03.2028 (decyzja wykonawcza Rady (UE) 2026/1912). Wcześniej ustal dla każdego pracownika podstawę pobytu i pracy po jej wygaśnięciu.",
       "zielonalinia.gov.pl, praca.gov.pl", "cudzoziemcy_b2b"),
    _a("2028-05-01", "Staż pracy ze zleceń i działalności — koniec okresu na dokumenty",
       "Pracownicy pracodawców prywatnych mają 24 miesiące (do 1.05.2028) na dostarczenie dowodów okresów sprzed 1.05.2026 — przypomnij załodze pół roku wcześniej.",
       "Kodeks pracy art. 302¹ i n.", "staz_pracy_2026"),
]
