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
import reszta                                     # noqa: E402


def zbuduj():
    lekcje = []
    for l in LEKCJE_1 + LEKCJE_2 + LEKCJE_3:
        l = dict(l)
        l["pytania"] = [list(p) for p in l.get("pytania", [])]
        l.setdefault("test", [])
        lekcje.append(l)
    id_lekcji = {l["id"] for l in lekcje}
    assert len(id_lekcji) == len(lekcje), "powtórzone id lekcji"

    tygodnie = []
    id_zadan = set()
    for w in TYGODNIE_1 + TYGODNIE_2 + TYGODNIE_3:
        w = dict(w)
        w.setdefault("rola_asystenta", "")
        for lid in w["lekcje"]:
            assert lid in id_lekcji, f"tydzień {w['tydzien']}: brak lekcji {lid}"
        zadania = []
        for z in w["zadania"]:
            z = dict(z)
            assert z["id"] not in id_zadan, f"powtórzone id zadania {z['id']}"
            id_zadan.add(z["id"])
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

    program = {
        "format": "mentor-program/1",
        "id": "kadry-i-place",
        "nazwa": "Kadry i płace — kurs zaawansowany (praktyka 2026)",
        "podtytul": "12 tygodni · prawo pracy, lista płac, zasiłki, ZUS, PIT, ZFŚS/PFRON, ustanie zatrudnienia, compliance 2026",
        "opis": "Po 12 tygodniach samodzielnie prowadzisz kadry i płace firmy zatrudniającej kilkadziesiąt osób: zawierasz i rozwiązujesz umowy, "
                "rozliczasz czas pracy i urlopy, liczysz listę płac od brutto do netto, zasiłki, ekwiwalenty i potrącenia, składasz dokumenty do ZUS, US, PFRON, "
                "prowadzisz ZFŚS i PPK, wdrażasz procedury wymagane w 2026 r. (staż z zleceń, kontrola L4, mobbing, jawność wynagrodzeń, sygnaliści) "
                "i przygotowujesz firmę do kontroli PIP/ZUS. Wszystko na fikcyjnej firmie AGRO-MLEKO RADZYŃ, z liczbami obowiązującymi w 2026 r. "
                "i podstawą prawną przy każdej liczbie. Uczysz się z asystentem AI (Claude Code, API albo tryb offline): kazusy rozwiązujesz sam, asystent pyta i wskazuje przepisy.",
        "autor": "Łukasz + Claude",
        "wersja": "1.0",
        "jezyk": "pl",
        "katalog_projektu": "kadry-praktyka",
        "stanowisko": "Specjalista ds. kadr i płac",
        "czas_dziennie_min": 90,
        "dni_w_tygodniu": [0, 1, 2, 3, 4],
        "dzien_quizu": 5,
        "dzien_wolny": 6,
        "zasady": [
            "Każda liczba ma podstawę prawną i rok obowiązywania — zapisujesz źródło obok wyniku.",
            "Najpierw liczysz i rozstrzygasz sam (minimum 15 minut), potem pytasz asystenta o podpowiedź, nie o wynik.",
            "Rozróżniasz: obowiązuje / projekt / nie wiem — i tak samo wymagasz od asystenta.",
            "Pracujesz wyłącznie na fikcyjnej firmie z FIRMA.md — nigdy na prawdziwych danych osobowych.",
            "Każdy kazus kończysz notatką: stan faktyczny, pytanie, podstawa, rozstrzygnięcie, ryzyka.",
            "Wynik sprawdzasz drugą metodą (kalkulator ZUS/MF, arkusz, przepis) zanim uznasz go za gotowy.",
            "Kończysz dzień 3 pytaniami sprawdzającymi i wpisem w dziennik.md (commit).",
            "Raz w tygodniu wracasz do ściągi wskaźników i terminów — liczby mają być w głowie, nie tylko w pliku.",
        ],
        "firma": FIRMA,
        "etapy": ETAPY,
        "tygodnie": tygodnie,
        "lekcje": lekcje,
        "quizy": {str(k): v for k, v in reszta.QUIZY.items()},
        "rytm_dnia": reszta.RYTM_DNIA,
        "prompty": reszta.PROMPTY,
        "claude_md": reszta.CLAUDE_MD,
        "szablony": reszta.SZABLONY,
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
          f"{sum(len(v) for v in prog['quizy'].values())} pytań quizowych, {len(prog['pojecia'])} pojęć")
