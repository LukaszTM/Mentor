# -*- coding: utf-8 -*-
"""
Silnik obliczeń kadrowo-płacowych Warsztatu (czysty Python, bez GUI): lista płac, zasiłki, urlopy, czas pracy,
potrącenia, PESEL, walidacja dokumentów ZUS. Parametry roku przychodzą z programu nauczania (P.parametry) albo z DOMYSLNE.
Każda funkcja zwraca słownik z wynikiem i listą „kroki” — żeby uczeń widział, skąd wzięła się każda liczba.
"""

import calendar
import datetime as dt
from decimal import Decimal, ROUND_HALF_UP

DOMYSLNE = {
    "rok": 2026, "minimalne": 4806.0, "stawka_godz": 31.40,
    "emerytalna": 9.76, "rentowa_prac": 1.5, "rentowa_pracod": 6.5, "chorobowa": 2.45, "wypadkowa": 1.67,
    "zdrowotna": 9.0, "fp": 2.45, "fgsp": 0.10, "limit_30": 282600.0, "prog": 120000.0, "stawka_1": 12.0, "stawka_2": 32.0,
    "kwota_zmn": 300.0, "kup": 250.0, "kup_podw": 300.0, "ulga_mlodych": 85528.0, "wspolczynnik": 20.92,
    "ppk_prac": 2.0, "ppk_pracod": 1.5, "odpis_zfss": 2943.23, "hip_stawka": 17.0, "hip_kwota_zmn": 43.76,
}


def zl(x):
    """Zaokrąglenie do grosza (matematyczne, jak w ZUS i na liście płac)."""
    return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def pelne(x):
    """Zaokrąglenie do pełnych złotych (podstawa opodatkowania, zaliczka)."""
    return float(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def fmt(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


# ============================================================ LISTA PŁAC
def lista_plac(zasadnicze=0.0, zmienne=0.0, natura=0.0, wyn_chorobowe=0.0, zasilek=0.0, kup=250.0, pit2=300.0,
               ppk_prac=2.0, ppk_pracod=1.5, ulga_mlodych=False, przychod_mlodych_narast=0.0, dochod_narast=0.0,
               podstawa_er_narast=0.0, fp_zwolnienie=False, potracenia=0.0, par=None, pensja_umowna=None):
    """Brutto → netto dla jednego pracownika w jednym miesiącu. Zwraca słownik z wszystkimi krokami.
    pensja_umowna: wynagrodzenie za PEŁNY miesiąc wg umowy — składki na FP/FGŚP są należne, gdy podstawa „w przeliczeniu
    na okres miesiąca” (art. 104 ust. 1 ustawy o promocji zatrudnienia) jest ≥ minimalnemu; obniżka za chorobę/część miesiąca
    nie zwalnia z FP, zwalnia dopiero niepełny etat z pensją poniżej minimalnej (bez innych tytułów)."""
    p = dict(DOMYSLNE, **(par or {}))
    kroki = []
    przychod_oskl = zl(zasadnicze + zmienne + natura)
    kroki.append(("Przychód oskładkowany (zasadnicze + zmienne + świadczenia w naturze)", przychod_oskl))
    wolne_do_limitu = max(0.0, p["limit_30"] - podstawa_er_narast)
    podstawa_er = zl(min(przychod_oskl, wolne_do_limitu))
    if podstawa_er < przychod_oskl:
        kroki.append((f"Podstawa emerytalno-rentowa ograniczona limitem 30-krotności ({fmt(p['limit_30'])})", podstawa_er))
    emer = zl(podstawa_er * p["emerytalna"] / 100)
    rent = zl(podstawa_er * p["rentowa_prac"] / 100)
    chor = zl(przychod_oskl * p["chorobowa"] / 100)
    spol = zl(emer + rent + chor)
    kroki += [(f"Składka emerytalna {p['emerytalna']}%", emer), (f"Składka rentowa {p['rentowa_prac']}%", rent),
              (f"Składka chorobowa {p['chorobowa']}%", chor), ("Składki społeczne pracownika razem", spol)]
    podstawa_zdr = zl(przychod_oskl - spol + wyn_chorobowe)
    zdrowotna = zl(podstawa_zdr * p["zdrowotna"] / 100)
    kroki.append(("Podstawa składki zdrowotnej (przychód − składki społeczne + wynagrodzenie chorobowe)", podstawa_zdr))
    ppk_pracod_kw = zl(przychod_oskl * ppk_pracod / 100)
    ppk_prac_kw = zl(przychod_oskl * ppk_prac / 100)
    przychod_pracy = zl(przychod_oskl + wyn_chorobowe + ppk_pracod_kw)
    kup_zast = kup if przychod_pracy > 0 else 0.0
    # hipotetyczna zaliczka wg zasad z 2021 (ograniczenie składki zdrowotnej, art. 83 ustawy zdrowotnej)
    hip_podst = max(0.0, pelne(przychod_pracy - spol - kup_zast))
    hip = max(0.0, zl(hip_podst * p["hip_stawka"] / 100 - (p["hip_kwota_zmn"] if pit2 else 0)))
    if zdrowotna > hip:
        kroki.append((f"Składka zdrowotna {p['zdrowotna']}% = {fmt(zdrowotna)}, ale obniżona do hipotetycznej zaliczki z 2021 r.", hip))
        zdrowotna = hip
    else:
        kroki.append((f"Składka zdrowotna {p['zdrowotna']}%", zdrowotna))
    # PIT
    zwolnione = 0.0
    if ulga_mlodych:
        zwolnione = zl(min(przychod_pracy, max(0.0, p["ulga_mlodych"] - przychod_mlodych_narast)))
        kroki.append(("Przychód zwolniony — ulga dla młodych (do 26 lat, limit 85 528 zł rocznie)", zwolnione))
    przychod_opod = zl(przychod_pracy - zwolnione)
    kup_eff = kup_zast if przychod_opod > 0 else 0.0
    # składki społeczne od przychodu zwolnionego nie pomniejszają podstawy
    spol_odl = spol if zwolnione == 0 else zl(spol * (przychod_opod / przychod_pracy) if przychod_pracy else 0)
    podstawa_pracy = max(0.0, przychod_opod - spol_odl - kup_eff)
    podstawa_pit = pelne(podstawa_pracy + zasilek)
    kroki.append(("Podstawa opodatkowania = przychód ze stosunku pracy (z PPK pracodawcy) − składki społeczne − KUP + zasiłki, zaokrąglona do zł", podstawa_pit))
    do_progu = max(0.0, p["prog"] - dochod_narast)
    cz1 = min(podstawa_pit, do_progu)
    cz2 = max(0.0, podstawa_pit - cz1)
    podatek = zl(cz1 * p["stawka_1"] / 100 + cz2 * p["stawka_2"] / 100)
    if cz2 > 0:
        kroki.append((f"Podatek: {fmt(cz1)} × {p['stawka_1']}% + {fmt(cz2)} × {p['stawka_2']}% (próg {fmt(p['prog'])} przekroczony)", podatek))
    else:
        kroki.append((f"Podatek {p['stawka_1']}% od podstawy", podatek))
    zaliczka = pelne(max(0.0, podatek - (pit2 or 0)))
    kroki.append((f"Zaliczka = podatek − kwota zmniejszająca {fmt(pit2 or 0)} (PIT-2), zaokrąglona do zł", zaliczka))
    if ppk_prac_kw:
        kroki.append((f"PPK pracownika {ppk_prac}% (potrącane z netto)", ppk_prac_kw))
    if ppk_pracod_kw:
        kroki.append((f"PPK pracodawcy {ppk_pracod}% (przychód do PIT, bez ZUS, nie wypłacane)", ppk_pracod_kw))
    pieniezne = zl(zasadnicze + zmienne + wyn_chorobowe + zasilek)
    netto = zl(pieniezne - spol - zdrowotna - zaliczka - ppk_prac_kw - potracenia)
    kroki.append(("Netto = wypłaty pieniężne − składki społeczne − zdrowotna − zaliczka − PPK pracownika − potrącenia", netto))
    # pracodawca
    emer_p = zl(podstawa_er * p["emerytalna"] / 100)
    rent_p = zl(podstawa_er * p["rentowa_pracod"] / 100)
    wyp = zl(przychod_oskl * p["wypadkowa"] / 100)
    na_miesiac = max(przychod_oskl, pensja_umowna or 0.0)
    bez_fp = fp_zwolnienie or na_miesiac < p["minimalne"] * 0.999
    fp = 0.0 if bez_fp else zl(przychod_oskl * p["fp"] / 100)
    fgsp = 0.0 if bez_fp else zl(przychod_oskl * p["fgsp"] / 100)
    if bez_fp and not fp_zwolnienie:
        kroki.append((f"FP/FGŚP nienależne: podstawa w przeliczeniu na miesiąc ({fmt(na_miesiac)}) poniżej minimalnego {fmt(p['minimalne'])}", 0.0))
    skl_pracod = zl(emer_p + rent_p + wyp + fp + fgsp)
    koszt = zl(przychod_oskl + wyn_chorobowe + skl_pracod + ppk_pracod_kw)
    kroki.append((f"Składki pracodawcy: emerytalna {fmt(emer_p)} + rentowa {fmt(rent_p)} + wypadkowa {fmt(wyp)} + FP {fmt(fp)} + FGŚP {fmt(fgsp)}", skl_pracod))
    kroki.append(("Koszt pracodawcy = brutto + składki pracodawcy + PPK pracodawcy (zasiłek rozlicza się z ZUS)", koszt))
    return {
        "przychod_oskl": przychod_oskl, "podstawa_er": podstawa_er, "emer": emer, "rent": rent, "chor": chor, "spol": spol,
        "podstawa_zdr": podstawa_zdr, "zdrowotna": zdrowotna, "ppk_prac": ppk_prac_kw, "ppk_pracod": ppk_pracod_kw,
        "przychod_pracy": przychod_pracy, "zwolnione": zwolnione, "kup": kup_eff, "podstawa_pit": podstawa_pit,
        "zaliczka": zaliczka, "zasilek": zasilek, "wyn_chorobowe": wyn_chorobowe, "netto": netto, "potracenia": potracenia,
        "emer_p": emer_p, "rent_p": rent_p, "wyp": wyp, "fp": fp, "fgsp": fgsp, "skl_pracod": skl_pracod, "koszt": koszt,
        "dochod_narast_po": zl(dochod_narast + podstawa_pit), "podstawa_er_narast_po": zl(podstawa_er_narast + podstawa_er),
        "kroki": kroki,
    }


def minimalne_netto(kup=250.0, pit2=300.0, ppk_prac=0.0, etat=1.0, par=None):
    """Kwota wolna od potrąceń = minimalne wynagrodzenie netto przy parametrach tego pracownika (proporcjonalnie do etatu)."""
    p = dict(DOMYSLNE, **(par or {}))
    w = lista_plac(zasadnicze=zl(p["minimalne"] * etat), kup=kup, pit2=pit2, ppk_prac=ppk_prac, ppk_pracod=p["ppk_pracod"] if ppk_prac else 0, par=p)
    return w["netto"]


def potracenia(netto, rodzaj="inne", kwota_zajecia=None, kup=250.0, pit2=300.0, ppk_prac=0.0, etat=1.0, par=None):
    """Ile wolno potrącić z netto: rodzaj = alimenty / inne / zaliczka / kara / zgoda_inne / zgoda_pracodawca."""
    wolna_100 = minimalne_netto(kup, pit2, ppk_prac, etat, par)
    reguly = {"alimenty": (3 / 5, 0.0), "inne": (1 / 2, 1.0), "zaliczka": (1 / 2, 0.75), "kara": (1 / 10, 0.9),
              "zgoda_inne": (1.0, 1.0), "zgoda_pracodawca": (1.0, 0.8)}
    ulamek, ul_wolna = reguly[rodzaj]
    granica = zl(netto * ulamek)
    kwota_wolna = zl(wolna_100 * ul_wolna)
    max_potr = zl(max(0.0, min(granica, netto - kwota_wolna)))
    if kwota_zajecia is not None:
        max_potr = min(max_potr, zl(kwota_zajecia))
    return {"granica": granica, "kwota_wolna": kwota_wolna, "max": max_potr, "zostaje": zl(netto - max_potr),
            "kroki": [(f"Granica potrącenia ({rodzaj}): {ulamek:.2f} × netto", granica),
                      (f"Kwota wolna: {int(ul_wolna * 100)}% minimalnego netto dla tego pracownika ({fmt(wolna_100)})", kwota_wolna),
                      ("Potrącenie = min(granica, netto − kwota wolna, kwota zajęcia)", max_potr)]}


# ============================================================ CZAS PRACY
def wielkanoc(rok):
    a, b, c = rok % 19, rok // 100, rok % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mies = (h + l - 7 * m + 114) // 31
    dzien = ((h + l - 7 * m + 114) % 31) + 1
    return dt.date(rok, mies, dzien)


def swieta(rok):
    """Dni ustawowo wolne od pracy w Polsce."""
    w = wielkanoc(rok)
    stale = [(1, 1), (1, 6), (5, 1), (5, 3), (8, 15), (11, 1), (11, 11), (12, 24), (12, 25), (12, 26)]
    s = {dt.date(rok, m, d) for m, d in stale}
    s |= {w, w + dt.timedelta(days=1), w + dt.timedelta(days=49), w + dt.timedelta(days=60)}
    return s


def wymiar(rok, miesiac):
    """Wymiar czasu pracy miesiąca (art. 130 KP) dla pełnego etatu."""
    sw = swieta(rok)
    dni = [dt.date(rok, miesiac, d) for d in range(1, calendar.monthrange(rok, miesiac)[1] + 1)]
    robocze = [d for d in dni if d.weekday() < 5]
    obnizajace = [d for d in dni if d in sw and d.weekday() != 6]
    godziny = len(robocze) * 8 - len(obnizajace) * 8
    dni_pracy = len([d for d in robocze if d not in sw])
    soboty_sw = [d for d in obnizajace if d.weekday() == 5]
    return {"godziny": godziny, "dni_pracy": dni_pracy, "dni_robocze_pn_pt": len(robocze), "swieta_obnizajace": obnizajace,
            "soboty_swiateczne": soboty_sw,
            "kroki": [(f"Dni pon–pt w miesiącu × 8 h", len(robocze) * 8),
                      (f"minus 8 h za każde święto w dniu innym niż niedziela ({len(obnizajace)})", -len(obnizajace) * 8),
                      ("Wymiar czasu pracy", godziny)]}


def wymiar_roczny(rok):
    return sum(wymiar(rok, m)["godziny"] for m in range(1, 13))


def wspolczynnik_ekwiwalentu(rok):
    return round(wymiar_roczny(rok) / 8 / 12, 2)


def dodatek_nocny(rok, miesiac, godziny, par=None):
    p = dict(DOMYSLNE, **(par or {}))
    w = wymiar(rok, miesiac)["godziny"]
    stawka = zl(p["minimalne"] / w)
    dod = zl(stawka * 0.2)
    return {"stawka_godz_min": stawka, "dodatek_godz": dod, "kwota": zl(dod * godziny), "wymiar": w,
            "kroki": [(f"Stawka z minimalnego: {fmt(p['minimalne'])} / {w} h", stawka), ("20% stawki", dod), (f"× {godziny} h nocnych", zl(dod * godziny))]}


def nadgodziny(zasadnicze, wymiar_godz, h50=0.0, h100=0.0, stale_dodatki=0.0):
    stawka = zl((zasadnicze + stale_dodatki) / wymiar_godz)
    normalne = zl(stawka * (h50 + h100))
    dod50 = zl(stawka * 0.5 * h50)
    dod100 = zl(stawka * h100)
    return {"stawka": stawka, "normalne": normalne, "dod50": dod50, "dod100": dod100, "razem": zl(normalne + dod50 + dod100),
            "kroki": [(f"Stawka godzinowa = (zasadnicze + stałe dodatki) / wymiar {wymiar_godz} h", stawka),
                      (f"Normalne wynagrodzenie za {h50 + h100:g} nadgodzin", normalne),
                      (f"Dodatek 50% za {h50:g} h", dod50), (f"Dodatek 100% za {h100:g} h", dod100), ("Razem", zl(normalne + dod50 + dod100))]}


def koniec_wypowiedzenia(data_doreczenia, okres):
    """okres: '3d', '1t', '2t', '1m', '3m'. Tygodniowy kończy się w sobotę, miesięczny — ostatniego dnia miesiąca."""
    d = data_doreczenia
    if okres.endswith("d"):
        n, kon = int(okres[:-1]), d
        while n:
            kon += dt.timedelta(days=1)
            if kon.weekday() < 5 and kon not in swieta(kon.year):
                n -= 1
        return kon
    if okres.endswith("t"):
        n = int(okres[:-1])
        niedziela = d + dt.timedelta(days=(6 - d.weekday()) % 7 or 7)   # pierwsza niedziela PO doręczeniu
        return niedziela + dt.timedelta(days=7 * n - 1)                    # … i sobota po n pełnych tygodniach
    n = int(okres[:-1])
    m = d.month + n
    r = d.year + (m - 1) // 12
    m = (m - 1) % 12 + 1
    return dt.date(r, m, calendar.monthrange(r, m)[1])


def okres_wypowiedzenia(staz_miesiace, rodzaj="nieokreslona", dlugosc_probnej_dni=0):
    if rodzaj == "probna":
        if dlugosc_probnej_dni <= 14:
            return "3d", "3 dni robocze (okres próbny do 2 tygodni)"
        if dlugosc_probnej_dni < 90:
            return "1t", "1 tydzień (okres próbny dłuższy niż 2 tygodnie)"
        return "2t", "2 tygodnie (okres próbny 3 miesiące)"
    if staz_miesiace < 6:
        return "2t", "2 tygodnie (staż poniżej 6 miesięcy)"
    if staz_miesiace < 36:
        return "1m", "1 miesiąc (staż co najmniej 6 miesięcy)"
    return "3m", "3 miesiące (staż co najmniej 3 lata)"


# ============================================================ URLOPY
def wymiar_urlopu(staz_lata, etat=1.0, pierwsza_praca=False, miesiace_w_roku=12, par=None):
    """Dni i godziny urlopu w roku; proporcja do etatu i do okresu zatrudnienia w roku (zaokrąglenie w górę do dnia)."""
    import math
    pelny = 26 if staz_lata >= 10 else 20
    kroki = [(f"Wymiar ze stażu {staz_lata} lat", pelny)]
    dni_etat = math.ceil(pelny * etat - 1e-9)
    if etat != 1.0:
        kroki.append((f"× etat {etat:g}, zaokrąglenie w górę", dni_etat))
    if pierwsza_praca:
        dni = math.floor(dni_etat * miesiace_w_roku / 12 * 100 + 1e-6) / 100
        kroki.append((f"Pierwsza praca: 1/12 × {miesiace_w_roku} przepracowanych miesięcy, bez zaokrąglania w górę", dni))
        return {"dni": dni, "godziny": round(dni * 8, 2), "kroki": kroki}
    if miesiace_w_roku < 12:
        dni = math.ceil(dni_etat * miesiace_w_roku / 12 - 1e-9)
        kroki.append((f"Proporcjonalnie do {miesiace_w_roku}/12 miesięcy, zaokrąglenie w górę", dni))
    else:
        dni = dni_etat
    return {"dni": dni, "godziny": dni * 8, "kroki": kroki}


def ekwiwalent(stale, zmienne_3m=0.0, roczne_12m=0.0, godziny=0.0, rok=2026, etat=1.0, norma=8, wspolczynnik=None):
    w = wspolczynnik or wspolczynnik_ekwiwalentu(rok)
    w_etat = round(w * etat, 2)
    podstawa = zl(stale + zmienne_3m / 3 + roczne_12m / 12)
    dzienna = zl(podstawa / w_etat)
    godzinowa = zl(dzienna / norma)
    kwota = zl(godzinowa * godziny)
    return {"wspolczynnik": w_etat, "podstawa": podstawa, "dzienna": dzienna, "godzinowa": godzinowa, "kwota": kwota,
            "kroki": [("Podstawa = stałe + średnia zmiennych z 3 mies. + 1/12 składników rocznych", podstawa),
                      (f"Stawka dzienna = podstawa / współczynnik {w_etat}", dzienna), (f"Stawka godzinowa = dzienna / {norma}", godzinowa),
                      (f"Ekwiwalent za {godziny:g} h", kwota)]}


def wynagrodzenie_urlopowe(zmienne_3m, godziny_przepracowane_3m, godziny_urlopu):
    stawka = zl(zmienne_3m / godziny_przepracowane_3m) if godziny_przepracowane_3m else 0.0
    return {"stawka": stawka, "kwota": zl(stawka * godziny_urlopu),
            "kroki": [("Stawka = suma składników zmiennych z 3 mies. / godziny przepracowane w tych miesiącach", stawka),
                      (f"× {godziny_urlopu:g} h urlopu (składniki stałe wypłacasz bez zmian)", zl(stawka * godziny_urlopu))]}


def pomniejszenie(pensja, dni_choroby=0, godziny_innej_nieobecnosci=0.0, wymiar_godz=160):
    za_chorobe = zl(pensja / 30 * dni_choroby)
    za_inne = zl(pensja / wymiar_godz * godziny_innej_nieobecnosci)
    return {"za_chorobe": za_chorobe, "za_inne": za_inne, "do_wyplaty": zl(pensja - za_chorobe - za_inne),
            "kroki": [(f"Choroba: pensja / 30 × {dni_choroby} dni", za_chorobe), (f"Inne nieobecności: pensja / {wymiar_godz} h × {godziny_innej_nieobecnosci:g} h", za_inne),
                      ("Wynagrodzenie za przepracowaną część", zl(pensja - za_chorobe - za_inne))]}


# ============================================================ ZASIŁKI
def podstawa_zasilku(miesiace, etat=1.0, par=None):
    """miesiace: lista słowników {nazwa, stale, zmienne, dni_obow, dni_przepr} — 12 (lub mniej) miesięcy przed niezdolnością.
    stale = kwota umowna składników stałych; zmienne = faktycznie wypłacone zmienne (pomniejszane za chorobę)."""
    p = dict(DOMYSLNE, **(par or {}))
    kroki, suma, n = [], 0.0, 0
    for m in miesiace:
        obow, przepr = m.get("dni_obow", 0), m.get("dni_przepr", 0)
        stale, zmienne = float(m.get("stale", 0)), float(m.get("zmienne", 0))
        if obow and przepr < obow / 2:
            kroki.append((f"{m.get('nazwa', '?')}: przepracowano {przepr}/{obow} dni (< 50%) — miesiąc WYŁĄCZONY", 0.0))
            continue
        if obow and przepr < obow:
            zm_uzup = zl(zmienne / przepr * obow) if przepr else 0.0
            brutto = zl(stale + zm_uzup)
            kroki.append((f"{m.get('nazwa', '?')}: {przepr}/{obow} dni — UZUPEŁNIENIE: stałe {fmt(stale)} w pełnej kwocie, zmienne {fmt(zmienne)}/{przepr}×{obow}", brutto))
        else:
            brutto = zl(stale + zmienne)
            kroki.append((f"{m.get('nazwa', '?')}: pełny miesiąc", brutto))
        po = zl(brutto * (1 - 0.1371))
        suma += po
        n += 1
    if not n:
        return {"podstawa": 0.0, "dzienna": 0.0, "n": 0, "kroki": kroki + [("Brak miesięcy do uwzględnienia", 0.0)]}
    podst = zl(suma / n)
    kroki.append((f"Średnia z {n} miesięcy po odliczeniu 13,71%", podst))
    minimum = zl(p["minimalne"] * etat * (1 - 0.1371))
    if podst < minimum:
        kroki.append((f"Podniesienie do minimalnej podstawy ({fmt(p['minimalne'])} × etat {etat:g} − 13,71%)", minimum))
        podst = minimum
    dzienna = zl(podst / 30)
    kroki.append(("Stawka dzienna = podstawa / 30", dzienna))
    return {"podstawa": podst, "dzienna": dzienna, "n": n, "kroki": kroki}


def pula_chorobowa(nieobecnosci, wiek_50_plus=False, rok=2026):
    """nieobecnosci: lista {od: date, do: date, rodzaj: 'choroba'|'opieka'|'wypadek_praca'|'ciaza'|'wypadek_droga'}.
    Zwraca dla każdej: dni, ile z wynagrodzenia chorobowego (33/14), ile zasiłku, procent, okres zasiłkowy."""
    limit = 14 if wiek_50_plus else 33
    uzyte = 0
    okres_dni, ostatni_koniec = 0, None
    wynik = []
    for nb in sorted(nieobecnosci, key=lambda x: x["od"]):
        dni = (nb["do"] - nb["od"]).days + 1
        rodzaj = nb.get("rodzaj", "choroba")
        proc = 100 if rodzaj in ("ciaza", "wypadek_droga", "wypadek_praca") else 80
        if rodzaj == "opieka":
            wynik.append({**nb, "dni": dni, "chorobowe": 0, "zasilek": dni, "proc": 80, "uwaga": "zasiłek opiekuńczy od 1. dnia (nie wlicza się do 33/14)"})
            continue
        if ostatni_koniec and (nb["od"] - ostatni_koniec).days - 1 > 60:
            okres_dni = 0
        if rodzaj == "wypadek_praca":
            chor, zas = 0, dni
            uwaga = "zasiłek 100% z ubezpieczenia wypadkowego od 1. dnia"
        else:
            if nb["od"].year != rok:
                uzyte = 0
            chor = max(0, min(dni, limit - uzyte))
            zas = dni - chor
            uzyte += chor
            uwaga = f"wynagrodzenie chorobowe {chor} dni (pula {limit}: wykorzystano {uzyte}), zasiłek {zas} dni"
        okres_dni += dni
        ostatni_koniec = nb["do"]
        limit_okresu = 270 if rodzaj == "ciaza" else 182
        if okres_dni > limit_okresu:
            uwaga += f"; UWAGA: okres zasiłkowy {limit_okresu} dni przekroczony ({okres_dni}) — świadczenie rehabilitacyjne"
        wynik.append({**nb, "dni": dni, "chorobowe": chor, "zasilek": zas, "proc": proc, "okres": okres_dni, "uwaga": uwaga})
    return {"limit": limit, "uzyte": uzyte, "pozycje": wynik}


# ============================================================ PESEL i ZUS
def pesel_suma(p10):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    s = sum(int(c) * w for c, w in zip(p10, wagi))
    return (10 - s % 10) % 10


def pesel_poprawny(pesel):
    return len(pesel) == 11 and pesel.isdigit() and pesel_suma(pesel[:10]) == int(pesel[10])


def pesel_z_daty(data, plec="K", seria=0):
    """Fikcyjny, ale poprawny formalnie PESEL (do ćwiczeń)."""
    r, m, d = data.year, data.month, data.day
    if 2000 <= r < 2100:
        m += 20
    kol = 1000 + seria * 2 + (1 if plec == "M" else 0)
    p10 = f"{r % 100:02d}{m:02d}{d:02d}{kol % 10000:04d}"
    return p10 + str(pesel_suma(p10))


def pesel_data(pesel):
    rr, mm, dd = int(pesel[:2]), int(pesel[2:4]), int(pesel[4:6])
    wiek_m = {0: 1900, 20: 2000, 40: 2100, 60: 2200, 80: 1800}
    for k, stulecie in wiek_m.items():
        if k < mm <= k + 12:
            return dt.date(stulecie + rr, mm - k, dd)
    return None


KODY_TYTULU = {
    "0110": "pracownik", "0120": "pracownik młodociany", "0411": "zleceniobiorca / umowa o świadczenie usług", "0430": "osoba współpracująca ze zleceniobiorcą",
    "0510": "osoba prowadząca pozarolniczą działalność", "0540": "działalność — ulga na start (tylko zdrowotne)", "0570": "działalność — składki preferencyjne (30% minimalnego)",
    "0590": "mały ZUS plus", "1211": "osoba na urlopie wychowawczym", "1240": "osoba pobierająca zasiłek macierzyński", "3000": "osoba bez tytułu — rozliczenie po ustaniu",
}
KODY_PRZERW = {
    "111": "urlop bezpłatny", "121": "urlop wychowawczy", "151": "usprawiedliwiona nieobecność bez prawa do wynagrodzenia/zasiłku",
    "152": "nieusprawiedliwiona nieobecność", "155": "niezdolność bez prawa do wynagrodzenia (okres wyczekiwania)",
    "312": "zasiłek opiekuńczy", "313": "zasiłek chorobowy z ubezpieczenia chorobowego", "314": "zasiłek chorobowy z ubezpieczenia wypadkowego",
    "319": "zasiłek macierzyński za okres urlopu rodzicielskiego", "321": "świadczenie rehabilitacyjne", "325": "zasiłek macierzyński za okres urlopu ojcowskiego",
    "327": "zasiłek macierzyński za okres urlopu macierzyńskiego", "331": "wynagrodzenie za czas niezdolności finansowane przez pracodawcę",
}
KODY_WYREJ = {"100": "ustanie tytułu do ubezpieczeń", "500": "zgon", "600": "inna przyczyna"}
TRYBY_ROZW = {"1": "porozumienie stron (art. 30 §1 pkt 1 KP)", "2": "wypowiedzenie przez pracownika (art. 30 §1 pkt 2)", "3": "wypowiedzenie przez pracodawcę (art. 30 §1 pkt 2)",
              "4": "bez wypowiedzenia z winy pracownika (art. 52)", "5": "bez wypowiedzenia bez winy pracownika (art. 53)", "6": "bez wypowiedzenia przez pracownika (art. 55)",
              "7": "upływ czasu, na który była zawarta (art. 30 §1 pkt 4)", "8": "wygaśnięcie (art. 63 i n.)"}


def sprawdz_zgloszenie(dok, osoba, ubezpieczeni, dzis=None):
    """Walidacja jak w Płatniku: zwraca (bledy, ostrzezenia). dok: {typ, kod, data, kod_wyrej, tryb, chorobowe}."""
    dzis = dzis or dt.date.today()
    bledy, ostrz = [], []
    typ = dok.get("typ")
    pesel = osoba.get("pesel", "")
    if not pesel_poprawny(pesel):
        bledy.append("Niepoprawny PESEL (błąd sumy kontrolnej lub długości).")
    data = dok.get("data")
    if not data:
        bledy.append("Brak daty (powstania/ustania obowiązku ubezpieczenia).")
        return bledy, ostrz
    zgl = [d for d in osoba.get("dokumenty", []) if d["typ"] in ("ZUA", "ZZA") and d.get("status") == "przyjęty"]
    wyr = [d for d in osoba.get("dokumenty", []) if d["typ"] == "ZWUA" and d.get("status") == "przyjęty"]
    aktywne = len(zgl) > len(wyr)
    kod = (dok.get("kod") or "").replace(" ", "")
    if typ in ("ZUA", "ZZA"):
        if len(kod) != 6 or kod[:4] not in KODY_TYTULU:
            bledy.append(f"Kod tytułu „{dok.get('kod')}” nie istnieje (4 cyfry tytułu + emerytura/renta + niepełnosprawność).")
        else:
            if kod[4] not in "012":
                bledy.append("5. znak kodu: 0 — brak, 1 — emerytura, 2 — renta.")
            if kod[5] not in "0123":
                bledy.append("6. znak kodu: stopień niepełnosprawności 0–3.")
        if aktywne:
            bledy.append("Osoba jest już zgłoszona z tym tytułem — najpierw ZWUA (lub ZUA w trybie korekty).")
        if osoba.get("student") and kod[:4] == "0411":
            bledy.append("Uczeń/student do 26 lat na zleceniu nie podlega ubezpieczeniom — nie zgłaszasz go wcale.")
        if typ == "ZZA" and kod[:4] == "0110":
            bledy.append("Pracownik (01 10) podlega ubezpieczeniom społecznym — ZZA (tylko zdrowotne) jest błędne; użyj ZUA.")
        if osoba.get("data_zatrudnienia") and data != osoba["data_zatrudnienia"] and kod[:4] == "0110":
            ostrz.append(f"Data powstania obowiązku ({data}) różni się od daty rozpoczęcia pracy ({osoba['data_zatrudnienia']}).")
        if (dzis - data).days > 7:
            ostrz.append(f"Zgłoszenie po terminie 7 dni (termin minął {data + dt.timedelta(days=7)}).")
        if dok.get("chorobowe") and typ == "ZUA" and kod[:4] == "0110":
            ostrz.append("Pracownik ma chorobowe obowiązkowe — pola „dobrowolne” nie zaznaczasz.")
    elif typ == "ZWUA":
        if not aktywne:
            bledy.append("Nie można wyrejestrować osoby, która nie jest zgłoszona.")
        ost = max((d["data"] for d in zgl), default=None)
        if ost and data <= ost:
            bledy.append("Data wyrejestrowania musi być późniejsza niż data zgłoszenia (dzień PO ustaniu tytułu).")
        if osoba.get("data_ustania") and data != osoba["data_ustania"] + dt.timedelta(days=1):
            ostrz.append(f"Umowa ustała {osoba['data_ustania']} — data wyrejestrowania to dzień następny ({osoba['data_ustania'] + dt.timedelta(days=1)}).")
        if (dok.get("kod_wyrej") or "") not in KODY_WYREJ:
            bledy.append("Brak lub zły kod przyczyny wyrejestrowania (100 / 500 / 600).")
        if osoba.get("rodzaj") == "pracownik" and not dok.get("tryb"):
            bledy.append("Dla pracownika podaj tryb i podstawę prawną rozwiązania stosunku pracy.")
        if (dzis - data).days > 7:
            ostrz.append("Wyrejestrowanie po terminie 7 dni.")
    elif typ == "ZCNA":
        if not aktywne:
            bledy.append("Członka rodziny zgłasza się do osoby, która sama jest zgłoszona (ZUA/ZZA).")
        if not dok.get("czlonek_pesel") or not pesel_poprawny(dok["czlonek_pesel"]):
            bledy.append("Niepoprawny PESEL członka rodziny.")
        if dok.get("stopien") not in ("01", "11", "21", "30", "31", "32"):
            ostrz.append("Kod stopnia pokrewieństwa: 01 małżonek, 11 dziecko własne, 21 wnuk/dziecko obce, 30–32 wstępni.")
    elif typ == "ZIUA":
        if not aktywne:
            ostrz.append("Zmiana danych identyfikacyjnych osoby, która nie jest aktualnie zgłoszona.")
    return bledy, ostrz


def sprawdz_komplet(rca, rsa, ubezpieczeni, miesiac, rok, identyfikator="01", wczesniejsze_identyfikatory=()):
    """Weryfikacja kompletu DRA/RCA/RSA: rca: lista {pesel, kod, podstawa_er, podstawa_ch, podstawa_zdr, emer, rent, chor, wyp, zdr};
    rsa: lista {pesel, kod_przerwy, od, do, kwota}."""
    bledy, ostrz = [], []
    if identyfikator in wczesniejsze_identyfikatory:
        bledy.append(f"Identyfikator {identyfikator} {miesiac:02d} {rok} został już użyty — korekta wymaga kolejnego numeru (02, 03…).")
    if identyfikator != "01" and "01" not in wczesniejsze_identyfikatory:
        bledy.append("Korekta (02+) bez wcześniejszego kompletu pierwotnego (01).")
    osoby = {u["pesel"]: u for u in ubezpieczeni}
    for r in rca:
        u = osoby.get(r["pesel"])
        if not u:
            bledy.append(f"RCA {r['pesel']}: osoba nie figuruje w rejestrze ubezpieczonych (brak ZUA/ZZA).")
            continue
        zgl = [d for d in u.get("dokumenty", []) if d["typ"] in ("ZUA", "ZZA") and d.get("status") == "przyjęty"]
        if not zgl:
            bledy.append(f"RCA {u.get('nazwisko', r['pesel'])}: brak przyjętego zgłoszenia ZUA/ZZA.")
        kod = (r.get("kod") or "").replace(" ", "")
        if kod[:4] not in KODY_TYTULU:
            bledy.append(f"RCA {u.get('nazwisko', '')}: kod tytułu {r.get('kod')} nie istnieje.")
        if r.get("podstawa_er", 0) > 0 and zl(r.get("emer", 0)) != zl(r["podstawa_er"] * 0.0976):
            bledy.append(f"RCA {u.get('nazwisko', '')}: składka emerytalna {fmt(r.get('emer', 0))} ≠ 9,76% × {fmt(r['podstawa_er'])} = {fmt(r['podstawa_er'] * 0.0976)}.")
        if r.get("podstawa_zdr", 0) > 0 and zl(r.get("zdr", 0)) > zl(r["podstawa_zdr"] * 0.09) + 0.01:
            bledy.append(f"RCA {u.get('nazwisko', '')}: składka zdrowotna wyższa niż 9% podstawy.")
        if r.get("podstawa_er", 0) > r.get("podstawa_ch", 0) + 0.01:
            ostrz.append(f"RCA {u.get('nazwisko', '')}: podstawa emerytalno-rentowa wyższa niż chorobowa — tak bywa tylko przy 30-krotności odwrotnie (sprawdź).")
    for s in rsa:
        if s["pesel"] not in osoby:
            bledy.append(f"RSA {s['pesel']}: osoba nieznana.")
        if s.get("kod_przerwy") not in KODY_PRZERW:
            bledy.append(f"RSA: kod przerwy {s.get('kod_przerwy')} nie istnieje.")
        if s.get("od") and s.get("do") and s["od"] > s["do"]:
            bledy.append("RSA: data „od” późniejsza niż „do”.")
        if s.get("od") and (s["od"].month != miesiac or s["od"].year != rok):
            if str(s.get("kod_przerwy", ""))[:1] == "3":
                ostrz.append(f"RSA {s.get('kod_przerwy')}: świadczenie za okres z innego miesiąca ({s['od']}) — poprawne tylko, jeśli WYPŁACONO je w miesiącu raportu (zasada kasowa).")
            else:
                ostrz.append(f"RSA {s.get('kod_przerwy')}: przerwa z innego miesiąca niż raport ({s['od']}) — przerwy bez świadczeń wykazuje się za miesiąc, w którym wystąpiły.")
        if s.get("kod_przerwy", "")[0] == "3" and not s.get("kwota"):
            ostrz.append(f"RSA {s['kod_przerwy']}: świadczenie bez kwoty (płatnik zasiłków wykazuje kwotę).")
    return bledy, ostrz


def dra_sumy(rca, rsa, par=None):
    p = dict(DOMYSLNE, **(par or {}))
    s = {"liczba": len(rca), "emer": 0.0, "rent": 0.0, "chor": 0.0, "wyp": 0.0, "zdr": 0.0, "fp": 0.0, "fgsp": 0.0, "zasilki": 0.0}
    for r in rca:
        s["emer"] += r.get("emer", 0) + r.get("emer_p", 0)
        s["rent"] += r.get("rent", 0) + r.get("rent_p", 0)
        s["chor"] += r.get("chor", 0)
        s["wyp"] += r.get("wyp", 0)
        s["zdr"] += r.get("zdr", 0)
        s["fp"] += r.get("fp", 0)
        s["fgsp"] += r.get("fgsp", 0)
    for x in rsa:
        if str(x.get("kod_przerwy", ""))[:1] == "3" and x.get("kod_przerwy") != "331":
            s["zasilki"] += x.get("kwota", 0) or 0
    for k in list(s):
        if k != "liczba":
            s[k] = zl(s[k])
    s["spoleczne"] = zl(s["emer"] + s["rent"] + s["chor"] + s["wyp"])
    s["do_zaplaty"] = zl(s["spoleczne"] + s["zdr"] + s["fp"] + s["fgsp"] - s["zasilki"])
    return s
