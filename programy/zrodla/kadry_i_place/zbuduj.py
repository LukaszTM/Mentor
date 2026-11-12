# -*- coding: utf-8 -*-
"""
Składa program „Kadry i płace — kurs zaawansowany (praktyka 2026)” z plików źródłowych
(tygodnie_1/2/3.py, lekcje_1/2/3.py, reszta.py) w jeden plik JSON, który Mentor wczytuje.

Uruchom:  python zbuduj.py   →  ../../kadry-i-place.json
"""

import json
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))

from tygodnie_1 import FIRMA, ETAPY, TYGODNIE_1   # noqa: E402
from tygodnie_2 import TYGODNIE_2                 # noqa: E402
from tygodnie_3 import TYGODNIE_3                 # noqa: E402
from lekcje_1 import LEKCJE_1                     # noqa: E402
from lekcje_2 import LEKCJE_2                     # noqa: E402
from lekcje_3 import LEKCJE_3                     # noqa: E402
from lekcja_start import LEKCJA_START             # noqa: E402
from cele import CELE                             # noqa: E402
from czytelnosc import uczytelnij                 # noqa: E402
from firma import FIRMA_OSOBY, FIRMA_REGULAMINY, PARAMETRY, NARZEDZIA  # noqa: E402
from przepisy import PRZEPISY                     # noqa: E402
from zadania_warsztat import NADPISZ, DOPISZ_KROK  # noqa: E402
from standard_1 import STANDARD_1                 # noqa: E402
from standard_2 import STANDARD_2                 # noqa: E402
from standard_3 import STANDARD_3                 # noqa: E402
from standard_4 import STANDARD_4                 # noqa: E402
from standard_5 import STANDARD_5                 # noqa: E402
from powtorki import POWTORKI                     # noqa: E402
from diagnoza import DIAGNOZA, PYTANIA_DZIENNIKA, QUIZ_LEKCJE  # noqa: E402
from szablony import SZABLONY_DODATKOWE           # noqa: E402
import reszta                                     # noqa: E402

STANDARD = {}
for _m in (STANDARD_1, STANDARD_2, STANDARD_3, STANDARD_4, STANDARD_5):
    STANDARD.update(_m)

# pola, które standard nadpisuje w lekcji (zadania/w_praktyce — gdy stara wersja odsyłała poza Mentora)
NADPISZ_W_PRAKTYCE = {
    "narzedzia_kadrowca": ["Rozpisz kalendarz miesiąca: 5. ewidencja, 8. lista, 10. wypłata, 15. ZUS/PPK, 20. PIT/PFRON, 25. Wn-D — z właścicielem każdego terminu.",
                           "Ustal, kto w firmie ma PEL (ZUS) i UPL-1 (US) i kto je podpisuje; wpisz do dostepy.md.",
                           "Przejdź w symulatorze eZUS/Płatnik pełną ścieżkę dokumentu: przygotuj → weryfikuj → wyślij → UPP w Rejestrze.",
                           "Wygeneruj w e-Urząd: PIT jeden PIT-11 i zapisz go do projektu — zobacz, które pola rozumiesz."],
}


def _sciezka_cw(lekcja_id, tydzien, nr):
    return f"cwiczenia/tydzien_{tydzien:02d}/{lekcja_id}_{nr}.md"


def _zastosuj_standard(l):
    """Dokłada bloki standardu (po_co, wymagania, demonstracja, jak_uruchomic, cwiczenia, typowe_bledy, podsumowanie)."""
    st = STANDARD.get(l["id"])
    if not st:
        return l
    for k, v in st.items():
        l[k] = v
    cw = []
    for i, c in enumerate(l.get("cwiczenia", []), 1):
        c = dict(c)
        c["plik"] = _sciezka_cw(l["id"], l["tydzien"], i)
        c["rozwiazanie_plik"] = c["plik"].replace("cwiczenia/", "rozwiazania/")
        cw.append(c)
    l["cwiczenia"] = cw
    if l["id"] in NADPISZ_W_PRAKTYCE:
        l["w_praktyce"] = NADPISZ_W_PRAKTYCE[l["id"]]
    return l


def _dopasuj_lekcje_quizu(tydzien, idx, q, lekcje_tyg, lekcje_po_id):
    """Przypisuje pytaniu quizu lekcję (do powtórki po błędnej odpowiedzi): ręcznie (QUIZ_LEKCJE) albo po słowach kluczowych."""
    import re
    if (tydzien, idx) in QUIZ_LEKCJE:
        return QUIZ_LEKCJE[(tydzien, idx)]
    txt = (q["p"] + " " + " ".join(q["o"]) + " " + q.get("w", "")).lower()
    rdz = {w[:6] for w in re.findall(r"[0-9a-ząćęłńóśźż]+", txt)}
    best, bp = None, 0
    for lid in lekcje_tyg:
        l = lekcje_po_id[lid]
        if l["id"].startswith("powtorka_"):
            continue
        p = 0
        for s in l.get("slowa", []):
            if s.lower() in txt:
                p += 2
            elif all(c[:6] in rdz for c in re.findall(r"[0-9a-ząćęłńóśźż]+", s.lower())):
                p += 1
        for s in {w[:6] for w in re.findall(r"[0-9a-ząćęłńóśźż]+", l["nazwa"].lower())}:
            if len(s) >= 5 and s in rdz:
                p += 1
        if p > bp:
            best, bp = lid, p
    return best or lekcje_tyg[0]


def zbuduj():
    lekcje = []
    for l in [LEKCJA_START] + LEKCJE_1 + LEKCJE_2 + LEKCJE_3:
        l = dict(l)
        l["pytania"] = [list(p) for p in l.get("pytania", [])]
        l.setdefault("test", [])
        if l["id"] in CELE:
            l.update(CELE[l["id"]])
        l["wyjasnienie"] = uczytelnij(l["wyjasnienie"])
        assert l.get("cel"), f"lekcja {l['id']} bez celu"
        l = _zastosuj_standard(l)
        assert l.get("cwiczenia") and l.get("demonstracja"), f"lekcja {l['id']} bez bloków standardu"
        lekcje.append(l)
    assert set(CELE) <= {l["id"] for l in lekcje}, set(CELE) - {l["id"] for l in lekcje}
    assert set(STANDARD) == {l["id"] for l in lekcje}, set(STANDARD) ^ {l["id"] for l in lekcje}
    # powtórki — po lekcjach etapu, dołączone do ostatniego tygodnia etapu
    for pw in POWTORKI:
        pw = dict(pw)
        pw["pytania"] = [list(p) for p in pw.get("pytania", [])]
        pw.setdefault("przyklad", "")
        cw = []
        for i, c in enumerate(pw.get("cwiczenia", []), 1):
            c = dict(c)
            c["plik"] = _sciezka_cw(pw["id"], pw["tydzien"], i)
            c["rozwiazanie_plik"] = c["plik"].replace("cwiczenia/", "rozwiazania/")
            cw.append(c)
        pw["cwiczenia"] = cw
        # wstaw po ostatniej lekcji tego tygodnia (nawigacja „następna lekcja” prowadzi do powtórki na końcu etapu)
        poz = max(i for i, l in enumerate(lekcje) if l["tydzien"] == pw["tydzien"]) + 1
        lekcje.insert(poz, pw)
    id_lekcji = {l["id"] for l in lekcje}
    assert len(id_lekcji) == len(lekcje), "powtórzone id lekcji"

    tygodnie = []
    id_zadan = set()
    for w in TYGODNIE_1 + TYGODNIE_2 + TYGODNIE_3:
        w = dict(w)
        w.setdefault("rola_asystenta", "")
        w["lekcje"] = list(w["lekcje"]) + [pw["id"] for pw in POWTORKI if pw["tydzien"] == w["tydzien"]]
        for lid in w["lekcje"]:
            assert lid in id_lekcji, f"tydzień {w['tydzien']}: brak lekcji {lid}"
        zadania = []
        for z in w["zadania"]:
            z = dict(z)
            assert z["id"] not in id_zadan, f"powtórzone id zadania {z['id']}"
            id_zadan.add(z["id"])
            z.update(NADPISZ.get(z["id"], {}))        # wersja „wszystko w Mentorze” (Warsztat zamiast kont zewnętrznych)
            if z["id"] in DOPISZ_KROK:
                z["kroki"] = list(z.get("kroki", [])) + [DOPISZ_KROK[z["id"]]]
            # pliki: żadnych arkuszy — wyniki w .md/.csv z Warsztatu
            pl = []
            for f in z.get("pliki", []):
                f = f.replace(".xlsx", ".md")
                if f not in pl:
                    pl.append(f)
            z["pliki"] = pl
            for klucz in ("opis", "sprawdz"):
                z[klucz] = (z.get(klucz) or "").replace("Arkusz terminów", "Rejestr terminów").replace("Jeden arkusz/strona", "Jedna strona").replace("Excel/LibreOffice: ", "")
            z.setdefault("kroki", [])
            z.setdefault("sprawdz", "")
            z.setdefault("problemy", [])
            z.setdefault("pliki", [])
            z.setdefault("xp", 10)
            z.setdefault("czas_min", 60)
            zadania.append(z)
        w["zadania"] = zadania
        tygodnie.append(w)
    tygodnie.sort(key=lambda w: w["tydzien"])
    assert set(NADPISZ) <= id_zadan, set(NADPISZ) - id_zadan
    assert set(DOPISZ_KROK) <= id_zadan, set(DOPISZ_KROK) - id_zadan

    # quizy: każde pytanie wskazuje lekcję do powtórki
    lekcje_po_id = {l["id"]: l for l in lekcje}
    tyg_lekcje = {w["tydzien"]: w["lekcje"] for w in tygodnie}
    quizy = {}
    for t, qs in reszta.QUIZY.items():
        quizy[str(t)] = [dict(q, lekcja=_dopasuj_lekcje_quizu(t, i, q, tyg_lekcje[t], lekcje_po_id)) for i, q in enumerate(qs)]
    for q in DIAGNOZA:
        assert q["lekcja"] in lekcje_po_id, q["lekcja"]
    szablony = dict(reszta.SZABLONY)
    szablony.update(SZABLONY_DODATKOWE)

    program = {
        "format": "mentor-program/1",
        "id": "kadry-i-place",
        "nazwa": "Kadry i płace — kurs zaawansowany (praktyka 2026)",
        "podtytul": "12 tygodni · prawo pracy, lista płac, zasiłki, ZUS, PIT, ZFŚS/PFRON, ustanie zatrudnienia, compliance 2026",
        "opis": "Po 12 tygodniach samodzielnie prowadzisz kadry i płace firmy zatrudniającej kilkadziesiąt osób: zawierasz i rozwiązujesz umowy, "
                "rozliczasz czas pracy i urlopy, liczysz listę płac od brutto do netto, zasiłki, ekwiwalenty i potrącenia, składasz dokumenty do ZUS, US, PFRON, "
                "prowadzisz ZFŚS i PPK, wdrażasz procedury wymagane w 2026 r. (staż z zleceń, kontrola L4, mobbing, jawność wynagrodzeń, sygnaliści) "
                "i przygotowujesz firmę do kontroli PIP/ZUS. Wszystko na fikcyjnej firmie AGRO-MLEKO, z liczbami obowiązującymi w 2026 r. "
                "i podstawą prawną przy każdej liczbie. Uczysz się z asystentem AI (Claude Code, API albo tryb offline): kazusy rozwiązujesz sam, asystent pyta i wskazuje przepisy.",
        "autor": "Mentor — kurs otwarty (treść wygenerowana z Claude, stan prawny XI 2026)",
        "wersja": "2.0",
        "jezyk": "pl",
        "katalog_projektu": "kadry-praktyka",
        "stanowisko": "Specjalista ds. kadr i płac",
        "czas_dziennie_min": 90,
        "dni_w_tygodniu": [0, 1, 2, 3, 4],
        "dzien_quizu": 5,
        "dzien_wolny": 6,
        "poziom": "od podstaw — bez znajomości prawa pracy, księgowości i arkuszy kalkulacyjnych",
        "system": "Windows 10/11 (Mentor.exe); działa też z Pythonem 3.10+ na innych systemach",
        "wymagania_wstepne": ["60–90 minut dziennie przez 12 tygodni", "jeden folder na dysku na pliki ćwiczeń", "Mentor (ten program) — nic więcej: żadnych kont, instalacji ani arkuszy; internet niepotrzebny"],
        "umiejetnosci_koncowe": ["zawrzeć i rozwiązać umowę o pracę z kompletem dokumentów i w terminach", "policzyć wymiar czasu pracy, nadgodziny, nocne, urlop i pensję za część miesiąca",
                                 "sporządzić i skontrolować listę płac od brutto do netto (PPK, chorobowe, zasiłek, benefity, potrącenia)", "ustalić podstawę zasiłku, rozliczyć zleceniobiorcę, przygotować komplet DRA/RCA/RSA i korektę",
                                 "zamknąć rok (PIT-4R, PIT-11, ZFŚS, PFRON) i przygotować firmę do kontroli PIP/ZUS z procedurami 2026/2027"],
        "zasady": [
            "Każda liczba ma podstawę prawną i rok obowiązywania — zapisujesz źródło obok wyniku.",
            "Najpierw liczysz i rozstrzygasz sam, korzystając z podpowiedzi w lekcji po kolei; o wskazówkę (nie o wynik) pytasz asystenta, gdy nie wiesz, jak zacząć — bez obowiązku „walczenia” przez określony czas.",
            "Rozróżniasz: obowiązuje / projekt / nie wiem — i tak samo wymagasz od asystenta.",
            "Pracujesz wyłącznie na fikcyjnej firmie z FIRMA.md — nigdy na prawdziwych danych osobowych.",
            "Każdy kazus kończysz notatką: stan faktyczny, pytanie, podstawa, rozstrzygnięcie, ryzyka.",
            "Wynik sprawdzasz drugą metodą (Warsztat, przepis, rozwiązanie w paczce) zanim uznasz go za gotowy — i potrafisz go wyjaśnić własnymi słowami.",
            "Kończysz dzień 3 pytaniami sprawdzającymi i wpisem w dziennik.md (commit).",
            "Raz w tygodniu wracasz do ściągi wskaźników i terminów — liczby mają być w głowie, nie tylko w pliku.",
        ],
        "firma": FIRMA,
        "firma_osoby": FIRMA_OSOBY,
        "firma_regulaminy": FIRMA_REGULAMINY,
        "parametry": PARAMETRY,
        "narzedzia": NARZEDZIA,
        "przepisy": PRZEPISY,
        "etapy": ETAPY,
        "tygodnie": tygodnie,
        "lekcje": lekcje,
        "quizy": quizy,
        "diagnoza": DIAGNOZA,
        "pytania_dziennika": PYTANIA_DZIENNIKA,
        "materialy": "materialy/kadry-i-place",
        "rytm_dnia": reszta.RYTM_DNIA,
        "prompty": reszta.PROMPTY,
        "claude_md": reszta.CLAUDE_MD,
        "szablony": szablony,
        "checklista": reszta.CHECKLISTA,
        "sciaga": [{"tytul": "Wskaźniki 2026", "pozycje": [list(x) for x in reszta.SCIAGA_WSKAZNIKI]},
                   {"tytul": "Terminy", "pozycje": [list(x) for x in reszta.SCIAGA_TERMINY]},
                   {"tytul": "Dokumenty i kody ZUS / US / PFRON", "pozycje": [list(x) for x in reszta.SCIAGA_ZUS]}],
        "linki": reszta.LINKI,
        "wskazowki": reszta.WSKAZOWKI,
        "motywacja_powrot": reszta.MOTYWACJA_POWROT,
        "pojecia": reszta.POJECIA,
        "bledy": reszta.BLEDY,
        "pytania_rekrutacyjne": [list(p) for p in reszta.PYTANIA_REKRUTACYJNE],
        "tematy_wpisu": sorted({l["nazwa"] for l in lekcje}),
        "stan_prawny": "listopad 2026",
    }
    # kontrola spójności
    for l in lekcje:
        assert l["id"] and l["nazwa"] and l["wyjasnienie"], l.get("id")
        assert len(l["test"]) >= 3, f"lekcja {l['id']} ma za mało pytań testowych"
        for q in l["test"]:
            assert 0 <= q["odp"] < len(q["o"]), (l["id"], q["p"])
        # standard §3: 12 elementów
        for k in ("po_co", "cel", "wymagania", "wyjasnienie", "demonstracja", "jak_uruchomic", "cwiczenia", "typowe_bledy", "pytania", "podsumowanie", "test"):
            assert l.get(k), f"lekcja {l['id']}: brak {k}"
        assert l["demonstracja"].get("kroki") and l["demonstracja"].get("wynik"), l["id"]
        assert [c["rodzaj"] for c in l["cwiczenia"]] == ["prowadzone", "samodzielne"], l["id"]
        for c in l["cwiczenia"]:
            assert len(c["wskazowki"]) == 3 and c["rozwiazanie"] and c["wynik"] and c["plik"], (l["id"], c["rodzaj"])
        for b in l["typowe_bledy"]:
            assert all(b.get(k) for k in ("komunikat", "przyczyna", "diagnoza", "poprawka")), l["id"]
    assert len(program["diagnoza"]) >= 8
    for t, qs in program["quizy"].items():
        for q in qs:
            assert q["lekcja"] in {l["id"] for l in lekcje}, (t, q["p"])
    for k, qs in reszta.QUIZY.items():
        assert any(w["tydzien"] == k for w in tygodnie), f"quiz dla nieistniejącego tygodnia {k}"
        for q in qs:
            assert 0 <= q["odp"] < len(q["o"]), (k, q["p"])
    for w in tygodnie:
        assert str(w["tydzien"]) in program["quizy"], f"brak quizu dla tygodnia {w['tydzien']}"
        assert w["lekcje"], f"tydzień {w['tydzien']} bez lekcji"
        assert any(e["nr"] == w["etap"] for e in ETAPY), f"tydzień {w['tydzien']}: etap {w['etap']} nie istnieje"
    for e in ETAPY:
        for t in e["tygodnie"]:
            assert any(w["tydzien"] == t for w in tygodnie), f"etap {e['nr']}: brak tygodnia {t}"
    return program


if __name__ == "__main__":
    prog = zbuduj()
    cel = TU.parent.parent / "kadry-i-place.json"
    cel.write_text(json.dumps(prog, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Zapisano {cel} — {len(prog['tygodnie'])} tygodni, {sum(len(w['zadania']) for w in prog['tygodnie'])} zadań, "
          f"{len(prog['lekcje'])} lekcji, {sum(len(l['test']) for l in prog['lekcje'])} pytań testowych, "
          f"{sum(len(v) for v in prog['quizy'].values())} pytań quizowych, {len(prog['pojecia'])} pojęć, {len(prog['przepisy'])} przepisów, {len(prog['firma_osoby'])} osób w firmie")
