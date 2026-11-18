# -*- coding: utf-8 -*-
"""Źródła lekcji — sprawdzone materiały polskie i zagraniczne, z których zbudowano lub zaktualizowano treść (audyt 18.11.2026).
Format pozycji: [tytuł, adres, data dostępu]. Lista „zrodla” trafia do lekcji (Mentor pokazuje ją pod lekcją), a ZRODLA_KURSU — do pola programu."""

D = "dostęp 18.11.2026"


def _z(tytul, url, dostep=D):
    return [tytul, url, dostep]


# ---------------------------------------------------------------- akty prawne (Dziennik Ustaw / ELI / EUR-Lex)
KP_TJ = _z("Kodeks pracy — tekst jednolity Dz.U. 2026 poz. 1245", "https://eli.gov.pl/eli/DU/2026/1245/ogl")
JAWNOSC_2025 = _z("Ustawa z 4.06.2025 o zmianie KP — informacja o wynagrodzeniu w rekrutacji (Dz.U. 2025 poz. 807)", "https://eli.gov.pl/eli/DU/2025/807/ogl")
MOBBING_2026 = _z("Ustawa z 19.06.2026 o zmianie KP i KPC — mobbing, równe traktowanie (Dz.U. 2026 poz. 1046)", "https://eli.gov.pl/eli/DU/2026/1046/ogl")
MOBBING_ELI = _z("Tekst ustawy z 19.06.2026 w systemie ELI (art. 94³, 94³ᵃ, 18³ᵈ–18³ᵍ, przepisy przejściowe)", "https://eli.gov.pl/eli/DU/2026/1046/ogl")
PIP_2026 = _z("Ustawa z 11.03.2026 o zmianie ustawy o PIP i innych ustaw — decyzja o ustaleniu stosunku pracy, grzywny, abolicja (Dz.U. 2026 poz. 473)", "https://eli.gov.pl/eli/DU/2026/473/ogl")
L4_2026 = _z("Ustawa z 18.12.2025 o zmianie ustawy zasiłkowej — kontrola zwolnień lekarskich (Dz.U. 2026 poz. 26)", "https://eli.gov.pl/eli/DU/2026/26/ogl")
L4_ROZP = _z("Rozporządzenie z 8.04.2026 w sprawie kontroli zwolnień lekarskich (Dz.U. 2026 poz. 503)", "https://eli.gov.pl/eli/DU/2026/503/ogl")
EKWIWALENT_2026 = _z("Ustawa z 4.12.2025 o zmianie KP — postać elektroniczna dokumentów, ekwiwalent (Dz.U. 2026 poz. 25)", "https://eli.gov.pl/eli/DU/2026/25/ogl")
UKRAINA_2026 = _z("Ustawa z 23.01.2026 o wygaszeniu rozwiązań ustawy o pomocy obywatelom Ukrainy (Dz.U. 2026 poz. 203)", "https://eli.gov.pl/eli/DU/2026/203/ogl")
UKRAINA_ZL = _z("Zielona Linia (MRPiPS): Pobyt i praca obywateli Ukrainy po 4 marca 2026 r. — powiadomienie w 7 dni", "https://zielonalinia.gov.pl/pobyt-i-praca-obywateli-ukrainy-po-4-marca-2026-r/")
MINIMALNE_2027 = _z("Rozporządzenie RM z 14.09.2026 — minimalne wynagrodzenie 4 950 zł i stawka 32,30 zł w 2027 r. (Dz.U. 2026 poz. 1213)", "https://eli.gov.pl/eli/DU/2026/1213/ogl")
UPALY_2026 = _z("Rozporządzenie MRPiPS z 9.07.2026 zmieniające ogólne przepisy BHP — praca w upale, od 11.01.2027 (Dz.U. 2026 poz. 927)", "https://eli.gov.pl/eli/DU/2026/927/ogl")
ODSETKI_MP = _z("Obwieszczenie MF o stawce odsetek za zwłokę od zaległości podatkowych — 10,50% od 5.03.2026 (M.P. 2026 poz. 269)", "https://eli.gov.pl/eli/MP/2026/269/ogl")
NBP_STOPY = _z("NBP — podstawowe stopy procentowe (referencyjna 3,75%, lombardowa 4,25%)", "https://nbp.pl/polityka-pieniezna/decyzje-rpp/podstawowe-stopy-procentowe-nbp/")
GUS_OBWIESZCZENIA = _z("GUS — komunikaty i obwieszczenia (przeciętne wynagrodzenie do ZFŚS 7 848,60 zł, obwieszczenie z 19.02.2026)", "https://stat.gov.pl/sygnalne/komunikaty-i-obwieszczenia/")
LEGISLACJA = _z("Rządowy proces legislacyjny — projekty UC127 (jawność wynagrodzeń), UC160 (praca platformowa), diety 2027", "https://legislacja.gov.pl")
SEJM = _z("Sejm RP — proces legislacyjny (ustawy 2026: mobbing, PIP, PIT 2027)", "https://www.sejm.gov.pl")
PIT_2027_MONEY = _z("money.pl (PAP), 6.11.2026: Senat przyjął bez poprawek ustawę o PIT 2027 (próg 130 000 zł, stawka 24%) — decyzja prezydenta do 27.11.2026", "https://www.money.pl/podatki/zmiany-w-podatkach-senat-zdecydowal-teraz-czas-na-ruch-prezydenta-7348086529518048a.html")
PIT_2027_INFOR = _z("Infor, XI 2026: zmiany w PIT, CIT i ryczałcie od 2027 r. — prezydent ma czas do 27 listopada", "https://ksiegowosc.infor.pl/wiadomosci/7706344,zmiany-w-pit-cit-ryczalcie-od-2027-r-prezydent-nawrocki-do-27-listopada-ma-czas-na-decyzje-przedsiebiorcy-powinni-przeliczyc-dwa-warianty.html")
MOBBING_PIP = _z("PIP: Mobbing i dyskryminacja w miejscu pracy — nowe przepisy (omówienie, podatki.biz)", "https://www.podatki.biz/artykuly/pip-mobbing-i-dyskryminacja-w-miejscu-pracy-nowe-przepisy_10_63151.htm")
MOBBING_DELOITTE = _z("Deloitte Legal, 11.08.2026: nowe przepisy dotyczące mobbingu wchodzą w życie 5 listopada 2026", "https://www.deloitte.com/pl/pl/services/legal/perspectives/strefa-pracodawcy/nowe-przepisy-dotyczace-mobbingu-wchodza-w-zycie-5-listopada-2026.html")
UKRAINA_GT = _z("Grant Thornton, 5.03.2026: zatrudnianie cudzoziemców 2026 — zmiany dla obywateli Ukrainy od 5 marca 2026 (powiadomienie 7 dni)", "https://grantthornton.pl/publikacja/zatrudnianie-cudzoziemcow-2026-rewolucja-w-przepisach-dla-ukraincow-od-5-marca-2026-r/")
ISAP_KP = _z("ISAP — Kodeks pracy (tekst ujednolicony)", "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19740240141")
ISAP_PIP = _z("ISAP — ustawa o Państwowej Inspekcji Pracy (tekst ujednolicony)", "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20070890589")

# ---------------------------------------------------------------- źródła zagraniczne (UE, TSUE, MOP, EU-OSHA, ACAS, CIPD)
EURLEX_883 = _z("Rozporządzenie (WE) 883/2004 w sprawie koordynacji systemów zabezpieczenia społecznego (EUR-Lex, wersja PL)", "https://eur-lex.europa.eu/eli/reg/2004/883/oj/pol")
EURLEX_987 = _z("Rozporządzenie (WE) 987/2009 — wykonanie koordynacji (A1)", "https://eur-lex.europa.eu/eli/reg/2009/987/oj/pol")
EURLEX_9671 = _z("Dyrektywa 96/71/WE o delegowaniu pracowników", "https://eur-lex.europa.eu/eli/dir/1996/71/oj/pol")
EURLEX_2018957 = _z("Dyrektywa (UE) 2018/957 zmieniająca dyrektywę o delegowaniu — równa płaca, 12/18 miesięcy", "https://eur-lex.europa.eu/eli/dir/2018/957/oj/pol")
EURLEX_200388 = _z("Dyrektywa 2003/88/WE o czasie pracy", "https://eur-lex.europa.eu/eli/dir/2003/88/oj/pol")
EURLEX_20191152 = _z("Dyrektywa (UE) 2019/1152 o przejrzystych i przewidywalnych warunkach pracy", "https://eur-lex.europa.eu/eli/dir/2019/1152/oj/pol")
EURLEX_20191158 = _z("Dyrektywa (UE) 2019/1158 o równowadze między życiem zawodowym a prywatnym", "https://eur-lex.europa.eu/eli/dir/2019/1158/oj/pol")
EURLEX_2023970 = _z("Dyrektywa (UE) 2023/970 o przejrzystości wynagrodzeń (termin transpozycji 7.06.2026)", "https://eur-lex.europa.eu/eli/dir/2023/970/oj/pol")
EURLEX_20222041 = _z("Dyrektywa (UE) 2022/2041 o adekwatnych wynagrodzeniach minimalnych", "https://eur-lex.europa.eu/eli/dir/2022/2041/oj/pol")
EURLEX_20242831 = _z("Dyrektywa (UE) 2024/2831 o pracy za pośrednictwem platform (termin 2.12.2026)", "https://eur-lex.europa.eu/eli/dir/2024/2831/oj/pol")
EURLEX_200078 = _z("Dyrektywa 2000/78/WE — równe traktowanie w zatrudnieniu", "https://eur-lex.europa.eu/eli/dir/2000/78/oj/pol")
EURLEX_200654 = _z("Dyrektywa 2006/54/WE — równość kobiet i mężczyzn w zatrudnieniu", "https://eur-lex.europa.eu/eli/dir/2006/54/oj/pol")
EURLEX_RODO = _z("Rozporządzenie (UE) 2016/679 — RODO", "https://eur-lex.europa.eu/eli/reg/2016/679/oj/pol")
EURLEX_20191937 = _z("Dyrektywa (UE) 2019/1937 o ochronie sygnalistów", "https://eur-lex.europa.eu/eli/dir/2019/1937/oj/pol")
CURIA_C1923 = _z("TSUE, wyrok C-19/23 z 11.11.2025 (Dania p. Parlamentowi i Radzie) — dyrektywa o minimalnych wynagrodzeniach", "https://curia.europa.eu/juris/liste.jsf?num=C-19/23")
CURIA_C5518 = _z("TSUE, wyrok C-55/18 CCOO z 14.05.2019 — obowiązek rejestrowania czasu pracy", "https://curia.europa.eu/juris/liste.jsf?num=C-55/18")
CURIA_C68416 = _z("TSUE, wyrok C-684/16 Max-Planck z 6.11.2018 — przepadek urlopu", "https://curia.europa.eu/juris/liste.jsf?num=C-684/16")
CURIA_C51815 = _z("TSUE, wyrok C-518/15 Matzak z 21.02.2018 — dyżur domowy jako czas pracy", "https://curia.europa.eu/juris/liste.jsf?num=C-518/15")
CURIA_C26614 = _z("TSUE, wyrok C-266/14 Tyco z 10.09.2015 — czas dojazdu pracowników mobilnych", "https://curia.europa.eu/juris/liste.jsf?num=C-266/14")
ILO_C081 = _z("MOP, Konwencja nr 81 o inspekcji pracy (NORMLEX)", "https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C081")
ILO_C100 = _z("MOP, Konwencja nr 100 o jednakowym wynagrodzeniu (NORMLEX)", "https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C100")
ILO_C111 = _z("MOP, Konwencja nr 111 o dyskryminacji w zatrudnieniu (NORMLEX)", "https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C111")
ILO_C190 = _z("MOP, Konwencja nr 190 o eliminacji przemocy i molestowania w świecie pracy (NORMLEX — ratyfikacje)", "https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C190")
EUOSHA_HEAT = _z("EU-OSHA, „Heat at work — Guidance for workplaces” (2023; PDF także po polsku)", "https://osha.europa.eu/en/publications/heat-work-guidance-workplaces")
ACAS_CODE = _z("ACAS, Code of Practice on disciplinary and grievance procedures (2015, par. 1–47; tłumaczenie własne w lekcji)", "https://www.acas.org.uk/acas-code-of-practice-on-disciplinary-and-grievance-procedures/html")
ACAS_PERF = _z("ACAS, Performance management — reviews and appraisals (tłumaczenie własne w lekcji)", "https://www.acas.org.uk/performance")
CIPD_INDUCTION = _z("CIPD, Induction factsheet — wdrożenie pracownika (tłumaczenie własne w lekcji)", "https://www.cipd.org/uk/knowledge/factsheets/induction-factsheet/")
CIPD_RETENTION = _z("CIPD, Employee turnover and retention factsheet — exit interviews", "https://www.cipd.org/uk/knowledge/factsheets/turnover-retention-factsheet/")
SHRM_EXIT = _z("SHRM, Exit interview questions (9.04.2025; pełna treść dla członków)", "https://www.shrm.org/topics-tools/tools/forms/exit-interview-questions")

ZRODLA = {
    "zrodla_prawa": [KP_TJ, ISAP_KP, LEGISLACJA, SEJM, EURLEX_883],
    "wskazniki_2026": [MINIMALNE_2027, GUS_OBWIESZCZENIA, NBP_STOPY, ODSETKI_MP, PIT_2027_MONEY, PIT_2027_INFOR],
    "rekrutacja_jawnosc": [JAWNOSC_2025, KP_TJ, EURLEX_2023970, LEGISLACJA],
    "czas_pracy_systemy": [KP_TJ, EURLEX_200388, CURIA_C5518],
    "ewidencja_czasu": [CURIA_C5518, EURLEX_200388, KP_TJ],
    "urlop_wypoczynkowy": [CURIA_C68416, EURLEX_200388, KP_TJ],
    "kontrola_l4_2026": [L4_2026, L4_ROZP],
    "cudzoziemcy_b2b": [UKRAINA_2026, UKRAINA_ZL, UKRAINA_GT, PIP_2026, EURLEX_883],
    "zus_korekty": [ODSETKI_MP, NBP_STOPY],
    "zfss_pfron": [GUS_OBWIESZCZENIA],
    "swiadectwo_rozliczenie": [EKWIWALENT_2026, PIP_2026, KP_TJ],
    "mobbing_dyskryminacja_2026": [MOBBING_2026, MOBBING_ELI, MOBBING_DELOITTE, MOBBING_PIP, EURLEX_200078, EURLEX_200654, ILO_C190],
    "jawnosc_wynagrodzen": [JAWNOSC_2025, EURLEX_2023970, LEGISLACJA, ILO_C100],
    "kontrola_pip_zus": [PIP_2026, ISAP_PIP, ILO_C081, ODSETKI_MP],
    "delegacje": [LEGISLACJA, EURLEX_2018957],
    "praktyki_hr_zagranica": [ACAS_CODE, ACAS_PERF, CIPD_INDUCTION, CIPD_RETENTION, SHRM_EXIT, KP_TJ, EURLEX_RODO],
    "prawo_ue_i_swiat": [EURLEX_883, EURLEX_987, EURLEX_9671, EURLEX_2018957, EURLEX_200388, EURLEX_20191152, EURLEX_20191158, EURLEX_2023970, EURLEX_20222041,
                         EURLEX_20242831, EURLEX_200078, EURLEX_20191937, CURIA_C1923, CURIA_C5518, CURIA_C68416, CURIA_C51815, CURIA_C26614,
                         ILO_C081, ILO_C100, ILO_C111, ILO_C190, EUOSHA_HEAT, UPALY_2026],
}

# rejestr dla całego programu (zakładka Źródła / START_TUTAJ): bez powtórzeń, w kolejności pierwszego użycia
ZRODLA_KURSU = []
for _lid, _lista in ZRODLA.items():
    for _z_ in _lista:
        if _z_ not in ZRODLA_KURSU:
            ZRODLA_KURSU.append(_z_)
