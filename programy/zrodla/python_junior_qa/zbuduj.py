# -*- coding: utf-8 -*-
"""
Składa program „Python → Junior QA” z plików źródłowych (tresc.py, wiedza.py, jak.py, lekcje_extra.py)
w jeden plik JSON, który Mentor wczytuje.

Uruchom:  python zbuduj.py   →  ../../python-junior-qa.json

Wolisz pisać program w Pythonie niż w JSON? Skopiuj ten folder, zmień treści, uruchom zbuduj.py.
"""

import json
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))

import tresc            # noqa: E402
import wiedza           # noqa: E402
from jak import JAK     # noqa: E402
from lekcje_extra import LEKCJE_TYDZIEN_0, TESTY  # noqa: E402
from cele import CELE  # noqa: E402
from cwiczenia import CWICZENIA, SRODOWISKO  # noqa: E402


def zbuduj():
    lekcje = []
    for l in LEKCJE_TYDZIEN_0 + wiedza.TEMATY:
        l = dict(l)
        l.setdefault("test", TESTY.get(l["id"], []))
        l["pytania"] = [list(p) for p in l.get("pytania", [])]
        if l["id"] in CELE:
            l["cel"] = CELE[l["id"]]
        lekcje.append(l)
    brak = [l["id"] for l in lekcje if not l.get("cel")]
    assert not brak, f"lekcje bez celu: {brak}"
    id_lekcji = {l["id"] for l in lekcje}
    lekcje_tygodnia = {}
    for l in lekcje:
        lekcje_tygodnia.setdefault(l["tydzien"], []).append(l["id"])

    tygodnie = []
    for w in tresc.PROGRAM:
        w = dict(w)
        w["rola_asystenta"] = w.pop("rola_claude")
        w["lekcje"] = lekcje_tygodnia.get(w["tydzien"], [])
        zadania = []
        for z in w["zadania"]:
            z = dict(z)
            j = JAK.get(z["id"])
            if not j:
                raise SystemExit(f"Brak instrukcji w jak.py dla zadania {z['id']}")
            z["czas_min"] = j.get("czas", 60)
            z["kroki"] = j["kroki"]
            z["sprawdz"] = j.get("sprawdz", "")
            z["problemy"] = j.get("problemy", [])
            z["tytul"] = z["tytul"].replace("Piątek: ", "", 1)
            if z["id"] in CWICZENIA:
                z["cwiczenie"] = CWICZENIA[z["id"]]
            zadania.append(z)
        w["zadania"] = zadania
        tygodnie.append(w)

    program = {
        "format": "mentor-program/1",
        "id": "python-junior-qa",
        "nazwa": "Python od zera → Junior QA",
        "podtytul": "12 tygodni · Python, Git, pytest, Selenium, projekt portfolio",
        "opis": "Po 12 tygodniach piszesz samodzielnie proste programy w Pythonie, czytasz cudzy kod, pracujesz z Gitem i masz na GitHubie "
                "projekt z testami automatycznymi (pytest + Selenium), który możesz pokazać na rozmowie o pracę Junior QA. "
                "Uczysz się z asystentem AI (Claude Code, API albo tryb offline) na zasadzie 70/30: 70% kodu piszesz sam.",
        "autor": "Łukasz + Claude",
        "wersja": "2.1",
        "jezyk": "pl",
        "katalog_projektu": "nauka-python",
        "srodowisko": SRODOWISKO,
        "stanowisko": "Junior QA",
        "czas_dziennie_min": 90,
        "dni_w_tygodniu": [0, 1, 2, 3, 4],
        "dzien_quizu": 5,
        "dzien_wolny": 6,
        "zasady": [
            "Najpierw próbujesz sam, potem pytasz — minimum 15 minut własnej walki.",
            "Proś o podpowiedź, nie o rozwiązanie.",
            "Każdy fragment kodu od asystenta przepisujesz ręcznie — nie kopiuj.",
            "Tłumacz asystentowi, co robi kod, zanim go uruchomisz.",
            "Kończ dzień 3 pytaniami sprawdzającymi.",
            "Trzymaj zasady w CLAUDE.md w katalogu projektu.",
            "Większe zadanie najpierw planuj (tryb planowania), potem koduj.",
            "Pytaj „dlaczego”, aż odpowiedź będzie oczywista.",
        ],
        "etapy": tresc.ETAPY,
        "tygodnie": tygodnie,
        "lekcje": lekcje,
        "quizy": {str(k): v for k, v in tresc.QUIZ.items()},
        "rytm_dnia": tresc.RYTM_DNIA,
        "prompty": tresc.PROMPTY,
        "claude_md": tresc.CLAUDE_MD,
        "szablony": {"bug_raport": tresc.BUG_RAPORT_SZABLON},
        "checklista": tresc.CHECKLISTA,
        "sciaga": [{"tytul": "Claude Code", "pozycje": [list(x) for x in tresc.SCIAGA]},
                   {"tytul": "Git — codzienne komendy", "pozycje": [list(x) for x in tresc.SCIAGA_GIT]}],
        "linki": [["Dokumentacja Claude Code", "https://code.claude.com/docs"],
                  ["Kurs Claude Code 101 (Anthropic)", "https://anthropic.skilljar.com/claude-code-in-action"],
                  ["Strona do ćwiczeń Selenium: the-internet", "https://the-internet.herokuapp.com"],
                  ["Strona do ćwiczeń Selenium: saucedemo", "https://www.saucedemo.com"],
                  ["Dokumentacja pytest", "https://docs.pytest.org"],
                  ["Dokumentacja Pythona po polsku", "https://docs.python.org/pl/3/tutorial/"]],
        "wskazowki": tresc.WSKAZOWKI,
        "motywacja_powrot": tresc.MOTYWACJA_POWROT,
        "pojecia": wiedza.POJECIA,
        "bledy": wiedza.BLEDY,
        "pytania_rekrutacyjne": [list(p) for p in wiedza.PYTANIA_REKRUTACYJNE],
        "tematy_wpisu": sorted({l["nazwa"] for l in lekcje}),
    }
    # kontrola spójności
    for w in tygodnie:
        for lid in w["lekcje"]:
            assert lid in id_lekcji, lid
    for l in lekcje:
        for q in l["test"]:
            assert 0 <= q["odp"] < len(q["o"]), (l["id"], q["p"])
    return program


if __name__ == "__main__":
    prog = zbuduj()
    cel = TU.parent.parent / "python-junior-qa.json"
    cel.write_text(json.dumps(prog, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Zapisano {cel} — {len(prog['tygodnie'])} tygodni, {sum(len(w['zadania']) for w in prog['tygodnie'])} zadań, "
          f"{len(prog['lekcje'])} lekcji, {sum(len(l['test']) for l in prog['lekcje'])} pytań testowych")
