# -*- coding: utf-8 -*-
"""
Składa program „Python od zera → Junior QA” z plików źródłowych (etap*.py, zadania*.py, reszta.py, weryfikatory/)
w jeden plik JSON, który Mentor wczytuje:  python zbuduj.py  →  ../../python-junior-qa.json
Wersja demonstracyjna (tygodnie 0–3):  python zbuduj.py --demo  →  ../../python-junior-qa-demo.json

Pilnuje standardu (STANDARD_KURSOW.md): komplet bloków lekcji, klucze odpowiedzi zgodne z rozwiązaniami, czas tygodnia ≤ 9 h,
sumy SHA-256 weryfikatorów wpisane do zadań, quizy wskazujące istniejące lekcje.
"""

import hashlib
import json
import math
import re
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))
sys.path.insert(0, str(TU.parent.parent.parent))      # katalog Mentora (odpowiedzi.py)

import etap0, etap1, etap2, etap3, etap4  # noqa: E402,E401
import reszta  # noqa: E402
import odpowiedzi as _odp  # noqa: E402
from sprawdz_weryfikatory import zloz_test  # noqa: E402
from zadania_wszystkie import QUIZY, TYGODNIE  # noqa: E402

CEL = TU.parent.parent / "python-junior-qa.json"
CEL_DEMO = TU.parent.parent / "python-junior-qa-demo.json"
TYGODNIE_DEMO = 4
LIMIT_TYGODNIA_MIN = 540


def wszystkie_lekcje():
    out = {}
    for m in (etap0, etap1, etap2, etap3, etap4):
        for v in vars(m).values():
            if isinstance(v, dict) and "cwiczenia" in v and "wyjasnienie" in v:
                assert v["id"] not in out, f"powtórzone id lekcji {v['id']}"
                out[v["id"]] = v
    return out


def _slowa(x):
    if isinstance(x, str):
        return len(x.split())
    if isinstance(x, list):
        return sum(_slowa(i) for i in x)
    if isinstance(x, dict):
        return sum(_slowa(v) for v in x.values())
    return 0


def czas_lekcji(l):
    """Czas z objętości treści: czytanie 140 słów/min, demonstracja 70 słów/min, ćwiczenia wg „Czas: N” (domyślnie 20), test 10 min; w górę do 5 min."""
    czytanie = _slowa([l.get(k, "") for k in ("wyjasnienie", "przyklad", "po_co", "podsumowanie", "pulapki", "wymagania", "jak_uruchomic", "typowe_bledy")])
    demo = _slowa(l.get("demonstracja", {}))
    cw = 0
    for c in l.get("cwiczenia", []):
        m = re.search(r"Czas:\s*(\d+)", c.get("tresc", ""))
        cw += int(m.group(1)) if m else 20
    return int(math.ceil((czytanie / 140 + demo / 70 + cw + 10) / 5) * 5)


def klucz_w_tekscie(pole, tekst):
    """Czy wartość z klucza odpowiedzi występuje w treści/wyniku/rozwiązaniu ćwiczenia (klucz nie może się rozjechać z rozwiązaniem)."""
    import datetime as _dt
    t = tekst.replace(" ", " ").replace(" ", " ")
    typ = pole.get("typ", "kwota")
    if typ in ("kwota", "liczba"):
        if pole.get("tol", 0) and float(pole["tol"]) >= float(pole["wartosc"]):
            return True                                   # samoocena (każda wartość w zakresie jest poprawna)
        w = float(pole["wartosc"])
        war = set()
        if w == int(w):
            i = int(w)
            war |= {f"{i:,}".replace(",", " "), str(i)}
        s = f"{w:,.2f}".replace(",", " ").replace(".", ",")
        war |= {s, s.replace(" ", ""), f"{w:.2f}", f"{w:.1f}"}
        if w != int(w):
            war |= {str(w).replace(".", ","), str(w)}
        return any(re.search(r"(?<![\d,.])" + re.escape(v) + r"(?![\d])", t) for v in war)
    if typ == "data":
        d = _dt.date.fromisoformat(pole["wartosc"])
        war = {d.isoformat(), f"{d.day}.{d.month:02d}.{d.year}", f"{d.day:02d}.{d.month:02d}.{d.year}", f"{d.day}.{d.month:02d}", f"{d.day:02d}.{d.month:02d}"}
        return any(v in t for v in war)
    if typ == "tekst":
        w = pole.get("wartosc")
        war = list(w) if isinstance(w, (list, tuple)) else ([w] if w else [])
        war += list(pole.get("zawiera") or [])
        n = _odp.tekst_norm(t)
        return any(str(v).lower() in t.lower() or _odp.tekst_norm(v) in n for v in war)
    if typ == "wybor":
        return pole["wartosc"] in pole.get("opcje", [])
    return True


def sha_weryfikatora(nazwa):
    return hashlib.sha256(zloz_test(nazwa).encode("utf-8")).hexdigest()


def zbuduj(demo=False):
    lekcje = wszystkie_lekcje()
    tyg = [w for w in TYGODNIE if not demo or w["tydzien"] < TYGODNIE_DEMO]
    if demo:
        lekcje = {k: v for k, v in lekcje.items() if v["tydzien"] < TYGODNIE_DEMO}
    bledy = []
    uzyte = []
    for w in tyg:
        for lid in w["lekcje"]:
            assert lid in lekcje, f"tydzień {w['tydzien']}: brak lekcji {lid}"
            assert lekcje[lid]["tydzien"] == w["tydzien"], f"lekcja {lid}: tydzien {lekcje[lid]['tydzien']} ≠ {w['tydzien']}"
            uzyte.append(lid)
    assert sorted(uzyte) == sorted(lekcje), f"lekcje poza planem: {sorted(set(lekcje) - set(uzyte))}"

    lista_lekcji = []
    for lid in uzyte:
        l = json.loads(json.dumps(lekcje[lid], ensure_ascii=False))
        l["czas_min"] = czas_lekcji(l)
        t = f"tydzien_{l['tydzien']:02d}"
        for i, cw in enumerate(l["cwiczenia"], 1):
            cw["plik"] = f"cwiczenia/{t}/{l['id']}_{i}.md"
            cw["rozwiazanie_plik"] = f"rozwiazania/{t}/{l['id']}_{i}.md"
            if cw.get("odpowiedzi"):
                bledy += _odp.waliduj_pola(cw["odpowiedzi"], f"{lid}:{i}")
                tekst = " ".join([cw["tresc"], cw["wynik"], cw["rozwiazanie"]])
                bledy += [f"{lid}:{i} pole „{p['id']}” = {p['wartosc']!r} nie występuje w treści/wyniku/rozwiązaniu" for p in cw["odpowiedzi"] if not klucz_w_tekscie(p, tekst)]
        lista_lekcji.append(l)
    po_id = {l["id"]: l for l in lista_lekcji}

    tygodnie = []
    ids_zadan = set()
    sumy = {}
    for w in tyg:
        w = json.loads(json.dumps(w, ensure_ascii=False))
        for z in w["zadania"]:
            assert z["id"] not in ids_zadan, f"powtórzone id zadania {z['id']}"
            ids_zadan.add(z["id"])
            c = z.get("cwiczenie")
            assert c, f"zadanie {z['id']} bez paska ćwiczenia"
            assert "/" not in c["plik"], (z["id"], c["plik"])
            spr = c["sprawdzenie"]
            if spr["rodzaj"] == "test_zewnetrzny":
                nazwa = spr["plik_testu"].split("/")[-1]
                sumy.setdefault(spr["plik_testu"], sha_weryfikatora(nazwa))
                spr["sha256"] = sumy[spr["plik_testu"]]
        razem = sum(po_id[lid]["czas_min"] for lid in w["lekcje"]) + sum(z["czas_min"] for z in w["zadania"])
        w["czas_min"] = razem
        if razem > LIMIT_TYGODNIA_MIN:
            bledy.append(f"tydzień {w['tydzien']}: {razem} min > {LIMIT_TYGODNIA_MIN} (lekcje {[po_id[l]['czas_min'] for l in w['lekcje']]}, zadania {[z['czas_min'] for z in w['zadania']]})")
        tygodnie.append(w)

    quizy = {}
    for k, qs in QUIZY.items():
        if int(k) >= len(tyg) and demo:
            continue
        for q in qs:
            assert q["lekcja"] in po_id, f"quiz {k}: nieznana lekcja {q['lekcja']}"
            assert po_id[q["lekcja"]]["tydzien"] <= int(k), f"quiz {k}: pytanie o lekcję z przyszłości {q['lekcja']}"
        quizy[k] = qs
    assert sorted(quizy, key=int) == [str(w["tydzien"]) for w in tygodnie]
    for q in reszta.DIAGNOZA:
        assert q["lekcja"] in po_id, q
    zrodla, widziane = [], set()
    for l in lista_lekcji:
        for z in l["zrodla"]:
            if z[1] not in widziane:
                widziane.add(z[1])
                zrodla.append(z)
    for z in reszta.ZRODLA_DODATKOWE:
        if z[1] not in widziane:
            zrodla.append(z)

    prog = json.loads(json.dumps(reszta.META, ensure_ascii=False))
    if demo:
        prog["id"] = "python-junior-qa-demo"
        prog["nazwa"] = "Python od zera → Junior QA (wersja demonstracyjna)"
        prog["podtytul"] = "Tygodnie 0–3 z 13 · konfiguracja i podstawy Pythona — pełny kurs: 13 tygodni z pytest, Selenium, SQL, Flask, CI i projektem portfolio"
        prog["wersja"] = prog["wersja"] + "-demo"
        prog["materialy"] = "materialy/python-junior-qa-demo"
        prog["etapy"] = [e for e in reszta.ETAPY if max(e["tygodnie"]) < TYGODNIE_DEMO]
    prog.update({
        "etapy": prog.get("etapy") or reszta.ETAPY, "tygodnie": tygodnie, "lekcje": lista_lekcji, "quizy": quizy, "diagnoza": reszta.DIAGNOZA,
        "pytania_dziennika": reszta.PYTANIA_DZIENNIKA, "rytm_dnia": reszta.RYTM_DNIA, "prompty": reszta.PROMPTY, "claude_md": reszta.CLAUDE_MD,
        "szablony": reszta.SZABLONY, "checklista": reszta.CHECKLISTA, "sciaga": reszta.SCIAGA, "linki": reszta.LINKI, "pojecia": reszta.POJECIA,
        "bledy": reszta.BLEDY, "pytania_rekrutacyjne": reszta.PYTANIA_REKRUTACYJNE, "tematy_wpisu": reszta.TEMATY_WPISU, "wskazowki": reszta.WSKAZOWKI,
        "motywacja_powrot": reszta.MOTYWACJA_POWROT, "zrodla_kursu": zrodla,
    })
    if bledy:
        print("BŁĘDY BUDOWANIA:")
        for b in bledy:
            print("  - " + b)
        raise SystemExit(1)
    (CEL_DEMO if demo else CEL).write_text(json.dumps(prog, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Zapisano {(CEL_DEMO if demo else CEL).name}: tygodnie {len(tygodnie)}, lekcje {len(lista_lekcji)}, zadania {len(ids_zadan)}, quizy {sum(len(v) for v in quizy.values())}, "
          f"źródła {len(zrodla)}, weryfikatory {len(sumy)}")
    for w in tygodnie:
        print(f"  T{w['tydzien']:>2} {w['czas_min']:>4} min = {w['czas_min'] / 60:>4.1f} h  lekcje {[po_id[l]['czas_min'] for l in w['lekcje']]} zadania {sum(z['czas_min'] for z in w['zadania'])}  {w['tytul'][:55]}")
    print(f"  razem {sum(w['czas_min'] for w in tygodnie) / 60:.1f} h")
    return prog


if __name__ == "__main__":
    zbuduj(demo="--demo" in sys.argv)
