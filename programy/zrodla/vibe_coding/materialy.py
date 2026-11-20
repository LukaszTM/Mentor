# -*- coding: utf-8 -*-
"""Generuje paczkę materiałów kursu „Vibe coding od podstaw” (STANDARD_KURSOW.md §5–6) z gotowego vibe-coding.json:

programy/materialy/vibe-coding/
├── START_TUTAJ.md, ZRODLA.md, manifest.json, INTEGRITY.json, kurs_mentor.json, pytest.ini
├── SPRAWDZ_SRODOWISKO.bat, INSTALACJA.bat, URUCHOM_KURS.bat
├── lekcje/tydzien_NN/<id>.md          — pełny tekst lekcji
├── przyklady/                         — pliki startowe zadań (z błędami do znalezienia), dane, zapisy pracy agenta (ścieżka bez konta)
├── cwiczenia/tydzien_NN/<id>_<n>.md   — ćwiczenia z lekcji (treść, oczekiwany wynik)
├── rozwiazania/tydzien_NN/<id>_<n>.md — 3 podpowiedzi + rozwiązanie; rozwiazania/kod/ — rozwiązania wzorcowe zadań
├── dane/rezerwacje.csv                — fikcyjne rezerwacje (CSV z polskiego arkusza)
├── WERYFIKATORY/test_tNN.py           — niezależne testy zadań (sumy SHA-256 w INTEGRITY.json i w kursie)
├── pomoc/                             — tracebacki, diff do przeglądu, obce repozytorium, brief klientki, FAQ, błędy, odzyskiwanie
└── testy/                             — sprawdzenie paczki

Uruchom: python materialy.py  (po zbuduj.py)
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))

from sprawdz_weryfikatory import testy, zloz_test  # noqa: E402

ZRODLO = TU.parent.parent / "vibe-coding.json"
CEL = TU.parent.parent / "materialy" / "vibe-coding"
POMIN = {"__pycache__", ".pytest_cache"}


def _w(sciezka, tresc):
    p = CEL / sciezka
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(tresc.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def _kopiuj_drzewo(zrodlo, cel):
    for p in sorted(Path(zrodlo).rglob("*")):
        if p.is_file() and not (POMIN & set(p.parts)) and p.suffix != ".pyc":
            c = CEL / cel / p.relative_to(zrodlo)
            c.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, c)


def _md_lekcja(l, poz, n):
    o = [f"# {l['nazwa']}", f"Tydzień {l['tydzien']} · lekcja {poz} z {n} · ≈ {l.get('czas_min', 20)} min", "",
         f"**Po tej lekcji potrafisz:** {l['cel']}", "", f"**Po co mi to?** {l['po_co']}", "", "## Czego potrzebujesz"] + [f"- {x}" for x in l["wymagania"]] + ["", "## 1 · Wyjaśnienie od podstaw"]
    for a in l["wyjasnienie"].split("\n"):
        o.append(("### " + a[3:]) if a.startswith("## ") else a)
    dem = l["demonstracja"]
    o += ["", "## 2 · Demonstracja — krok po kroku", f"**{dem['tytul']}**", "", "```", l["przyklad"], "```", ""]
    o += [f"{i}. {k}" for i, k in enumerate(dem["kroki"], 1)] + ["", f"✔ **Oczekiwany wynik:** {dem['wynik']}", "", "## 3 · Jak to uruchomić"]
    o += [f"{i}. {x}" for i, x in enumerate(l["jak_uruchomic"], 1)] + [""]
    if l.get("w_praktyce"):
        o += ["## W praktyce"] + [f"- {x}" for x in l["w_praktyce"]] + [""]
    for nr, cw in enumerate(l["cwiczenia"], 4):
        o += [f"## {nr} · Ćwiczenie {cw['rodzaj']}", cw["tresc"], "", f"📄 `{cw['plik']}` · rozwiązanie: `{cw['rozwiazanie_plik']}`",
              "✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole." if cw.get("odpowiedzi") else "", ""]
    o += ["## 6 · Typowe błędy i naprawa"]
    for b in l["typowe_bledy"]:
        o += [f"- ✘ **{b['komunikat']}**", f"  - Przyczyna: {b['przyczyna']}", f"  - Jak sprawdzić: {b['diagnoza']}", f"  - Poprawka: {b['poprawka']}"]
    o += ["", "## Pułapki"] + [f"- {x}" for x in l["pulapki"]] + ["", "## Dodatkowe zadania"] + [f"{i}. {x}" for i, x in enumerate(l["zadania"], 1)]
    o += ["", "## Sprawdzenie — odpowiedz na głos, potem rozwiń"]
    for p, odp in l["pytania"]:
        o += [f"- **{p}**", f"  - {odp}"]
    o += ["", "## Co potrafię teraz bez patrzenia na przykład?", l["podsumowanie"], "", "## Źródła (data dostępu w nawiasie)",
          "Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło."]
    o += [f"- {z[0]} ({z[2]}) — <{z[1]}>" for z in l["zrodla"]]
    o += ["", "## Test (w Mentorze: Lekcje → Sprawdź się)"]
    for q in l["test"]:
        o.append(f"- {q['p']}")
        o += [f"  - {'ABCDE'[i]}) {op}" for i, op in enumerate(q["o"])]
    o += ["", "Odpowiedzi: " + ", ".join("ABCDE"[q["odp"]] for q in l["test"]), ""]
    return "\n".join(o)


def _md_cwiczenie(l, nr, cw):
    o = [f"# Ćwiczenie {nr} ({cw['rodzaj']}) — {l['nazwa']}", f"Tydzień {l['tydzien']} · lekcja `{l['id']}`", "", "## Zadanie", cw["tresc"], "",
         "## Jak sprawdzić", "1. Zrób ćwiczenie (w Mentorze: Lekcje → ta lekcja → pola „Twoje odpowiedzi”; kod uruchamiasz w pliku .py w PRACA).",
         "2. Utknąłeś? Podpowiedzi po kolei w Mentorze albo w pliku rozwiązania — najpierw podpowiedź 1.", f"3. Po własnej próbie: `{cw['rozwiazanie_plik']}`.", "",
         "## Twoja odpowiedź", "", "(pisz tutaj)", ""]
    return "\n".join(o)


def _md_rozwiazanie(l, nr, cw):
    return "\n".join([f"# Rozwiązanie — ćwiczenie {nr} ({cw['rodzaj']}) — {l['nazwa']}", "", "Najpierw własna próba. Podpowiedzi odkrywaj po kolei.", "",
                      "## Podpowiedź 1", cw["wskazowki"][0], "", "## Podpowiedź 2", cw["wskazowki"][1], "", "## Podpowiedź 3", cw["wskazowki"][2], "",
                      "## Rozwiązanie", cw["rozwiazanie"], "", "## Oczekiwany wynik", cw["wynik"], "",
                      "## Wyjaśnij własnymi słowami", "Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?", ""])


PYTEST_INI = """# Ustawienia pytest dla katalogu roboczego kursu: Twoje testy (test_*.py w PRACA) uruchamiasz `python -m pytest -q`.
# Foldery materiałów kursu (weryfikatory, rozwiązania, przykłady) są pomijane — Mentor uruchamia weryfikatory sam, w izolacji.
[pytest]
norecursedirs = WERYFIKATORY rozwiazania przyklady lekcje cwiczenia pomoc testy .venv .git node_modules
"""

START = """# START TUTAJ — Vibe coding od podstaw

**Wersja kursu:** {wersja} · stan na: {stan} · format `mentor-program/1`
**Poziom:** {poziom}.
**Czas:** 16 tygodni, ok. 80 minut dziennie (pn–pt) i do 90 minut w sobotę — razem ok. {godziny} godzin; żaden tydzień nie przekracza 9 godzin (czas policzony z treści lekcji i zadań).
**System:** {system}.
**Potrzebujesz:** {wymagania}.

## Co będziesz umieć po kursie
{umiejetnosci}

## Pierwsze 30 minut
1. **Rozpakuj ZIP** do zwykłego folderu (nie pracuj „w środku” archiwum).
2. **Uruchom Mentora** (`URUCHOM_KURS.bat` albo `Mentor.exe`). Windows może zapytać o uruchomienie niepodpisanego programu: „Więcej informacji → Uruchom mimo to”.
3. **Ustawienia → Program nauczania → „Vibe coding od podstaw”** (kurs jest wbudowany; `kurs_mentor.json` to ten sam plik — „Wgraj program z pliku…” tylko na komputerze bez tego kursu).
4. **Mój projekt → „📁 Utwórz katalog roboczy kursu”** (Dokumenty\\Mentor\\vibe-coding\\PRACA) → **„📂 Skopiuj materiały kursu tutaj”** (nic nie nadpisuje).
5. **Środowisko → „⬇ Zainstaluj brakujące”** — Python i biblioteki kursu (pytest, flask, requests) w osobnym .venv, za Twoją zgodą.
6. **Panel → Diagnoza** (10 pytań) → **Lekcje → „Jak uczyć się z tego kursu”** → **Plan → Tydzień 0**.

## Jak sprawdzane są zadania
- Pliki zadań tworzysz w katalogu PRACA (przycisk „📝 Utwórz plik ćwiczenia”). „✔ Sprawdź wynik” uruchamia **niezależne testy** z folderu `WERYFIKATORY/` tej paczki — Mentor sprawdza ich sumę SHA-256 (INTEGRITY.json), kopiuje do osobnego katalogu tylko do odczytu i dopiero wtedy uruchamia. Agent AI nie może ich zmienić.
- Zadania opisowe (plany, przeglądy, wyceny) mają listę kryteriów do samooceny.
- Ćwiczenia w lekcjach mają pola „Twoje odpowiedzi” sprawdzane pole po polu; w Warsztacie są **Karty przeglądu** — sytuacje z pracy z agentem.

## Bez płatnego konta
Tygodnie 0–3 kosztują 0 zł. Od tygodnia 4 zadania z agentem mają ścieżkę bez konta: `przyklady/odpowiedzi_agenta/<zadanie>.md` — zapis pracy agenta z jednym celowo wstawionym błędem do znalezienia testem i poprawienia.

## Gdzie co jest
- `lekcje/` — 48 lekcji (Markdown); `cwiczenia/` i `rozwiazania/` — ćwiczenia z lekcji z podpowiedziami; `rozwiazania/kod/` — rozwiązania wzorcowe zadań (otwieraj po własnej próbie).
- `przyklady/` — pliki startowe zadań (część celowo z błędami), `przyklady/odpowiedzi_agenta/` — ścieżka bez konta; `dane/rezerwacje.csv` — dane fikcyjne.
- `pomoc/` — materiały do zadań (tracebacki, diff do przeglądu, obce repozytorium, brief klientki), FAQ, typowe błędy, odzyskiwanie.
- `pytest.ini` — po skopiowaniu do PRACA sprawia, że `python -m pytest -q` uruchamia tylko Twoje testy (pomija foldery materiałów).

## Aktualność
Fakty o narzędziach (Claude Code, Codex), cenach planów i prawie (AI Act, RODO, prawo autorskie) sprawdzono 19–20.11.2026 — źródła z datą dostępu są przy każdej lekcji i w `ZRODLA.md`. Kalendarz aktualizacji (Ściąga w Mentorze) mówi, kiedy sprawdzić ceny, wersje narzędzi i terminy.

## Bezpieczeństwo i licencje
Paczka zawiera wyłącznie materiały kursu: dane fikcyjne, bez kluczy API, haseł i programów firm trzecich. Adresy i klucze w przykładach (np. `smsapi_live_…`, `api.pogoda.example`) są zmyślone na potrzeby ćwiczeń.
"""

FAQ = """# FAQ — najczęstsze pytania

**„✔ Sprawdź wynik” mówi „Brak pliku …”.** Plik musi leżeć bezpośrednio w katalogu PRACA i mieć dokładnie tę nazwę (włącz widoczne rozszerzenia — `plik.py.txt` to nie `plik.py`).

**„W pliku brakuje funkcji …”.** Nazwy funkcji i parametrów są częścią specyfikacji — skopiuj je dosłownie z zadania.

**Testy „wiszą” albo kończą się po czasie.** W pliku jest `input()` poza blokiem `if __name__ == "__main__":` — test czeka na klawiaturę.

**„pytest nie jest dostępny w środowisku kursu”.** Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.

**Nie mam płatnego planu.** Każde zadanie z agentem ma plik `przyklady/odpowiedzi_agenta/<id>.md` — zapis pracy agenta z jednym błędem. Ta sama umiejętność: czytasz, sprawdzasz, poprawiasz.

**Testy Git (tydzień 6+) mówią „Nie znaleziono programu git”.** Zainstaluj Git for Windows (`winget install --id Git.Git -e --source winget`) i uruchom Mentora ponownie.

**Agent chce zmienić testy z WERYFIKATORY.** Odmów. Te testy są kopiowane przez Mentora z paczki i sprawdzane sumą SHA-256 — zmiana w Twoim folderze nic nie da, a zasada „nie zmieniaj testów” jest częścią kursu.

**Czy mogę używać innego agenta (Cursor, Copilot, Gemini…)?** Tak — specyfikacje, testy i przegląd działają tak samo. Lekcje pokazują Claude Code i Codex.
"""

ODZYSKIWANIE = """# Odzyskiwanie — gdy coś poszło nie tak

- **Agent popsuł plik, bez commita:** `git diff plik.py` (zobacz, co tracisz) → `git restore plik.py`. W Claude Code także Esc Esc / `/rewind`.
- **Zły commit:** `git revert HEAD` (nowy commit odwracający — bezpieczne).
- **Klucz API trafił do repozytorium:** unieważnij klucz w panelu usługi NATYCHMIAST, wygeneruj nowy, ustaw w zmiennej środowiskowej; usunięcie pliku nie usuwa go z historii.
- **Skrypt porządkujący przeniósł pliki:** log `.porzadki.log` w folderze mówi, skąd dokąd — przenieś z powrotem.
- **Zepsute środowisko Pythona:** Mentor → Środowisko → „Napraw środowisko”.
- **Zagubione materiały kursu:** Mój projekt → „📂 Skopiuj materiały kursu tutaj” (nie nadpisuje Twoich plików) albo rozpakuj ZIP kursu ponownie.
- **Postępy w Mentorze:** zapisane w `mentor_dane.json` w katalogu danych Mentora (`%LOCALAPPDATA%\\Mentor\\`; w trybie przenośnym — obok Mentor.exe) — skopiuj go jako kopię zapasową.
"""


def _pomoc(d):
    _kopiuj_drzewo(TU / "pomoc", "pomoc")
    _w("pomoc/FAQ.md", FAQ)
    _w("pomoc/ODZYSKIWANIE.md", ODZYSKIWANIE)
    o = ["# Typowe błędy — z każdej lekcji", ""]
    for l in d["lekcje"]:
        o.append(f"## {l['nazwa']} (tydzień {l['tydzien']})")
        for b in l["typowe_bledy"]:
            o.append(f"- **{b['komunikat']}** — {b['przyczyna']} → {b['poprawka']}")
        o.append("")
    o += ["## Komunikaty i sytuacje (Asystent offline)", ""] + [f"- **{k}** — {v['co']} {v['pytanie']}" for k, v in d["bledy"].items()]
    _w("pomoc/BLEDY.md", "\n".join(o) + "\n")


SPRAWDZ_BAT = r"""@echo off
chcp 65001 >nul
echo === Sprawdzenie srodowiska kursu Vibe coding (niczego nie zmienia) ===
where python >nul 2>nul && (python --version) || echo [!] Python: brak w PATH - Mentor zainstaluje srodowisko kursu sam (zakladka Srodowisko).
where git >nul 2>nul && (git --version) || echo [i] Git: brak - potrzebny od tygodnia 6.
where claude >nul 2>nul && (claude --version) || echo [i] Claude Code: brak - instalacja w tygodniu 4 (opcjonalnie, albo Codex).
where codex >nul 2>nul && (codex --version) || echo [i] Codex: brak - instalacja w tygodniu 4 (opcjonalnie, albo Claude Code).
where node >nul 2>nul && (node --version) || echo [i] Node.js: brak - opcjonalny (test JavaScript w tygodniu 9).
echo.
pause
"""

INSTALACJA_BAT = r"""@echo off
chcp 65001 >nul
set CEL=%USERPROFILE%\Documents\Mentor\vibe-coding\PRACA
echo Kopiuje materialy kursu do: %CEL%  (istniejace pliki NIE beda nadpisane)
if not exist "%CEL%" mkdir "%CEL%"
robocopy "%~dp0." "%CEL%" /E /XC /XN /XO /XF *.bat /XD testy /NFL /NDL /NJH /NJS >nul
echo Gotowe. Otworz Mentora: Moj projekt -> wskaz ten katalog.
pause
"""

URUCHOM_BAT = r"""@echo off
chcp 65001 >nul
if exist "%~dp0..\Mentor.exe" (start "" "%~dp0..\Mentor.exe" & goto :eof)
if exist "%~dp0Mentor.exe" (start "" "%~dp0Mentor.exe" & goto :eof)
echo Nie znaleziono Mentor.exe obok paczki. Uruchom Mentora recznie i wybierz program „Vibe coding od podstaw”.
pause
"""

SPRAWDZ_KURS_PY = '''# -*- coding: utf-8 -*-
"""Sprawdza paczkę kursu: sumy SHA-256 z manifest.json i INTEGRITY.json, poprawność kurs_mentor.json. Uruchom: python testy/sprawdz_kurs.py"""
import hashlib
import json
import sys
from pathlib import Path

K = Path(__file__).resolve().parent.parent
m = json.loads((K / "manifest.json").read_text(encoding="utf-8"))
zle = [p for p, h in m["pliki"].items() if not (K / p).is_file() or hashlib.sha256((K / p).read_bytes()).hexdigest() != h]
integ = json.loads((K / "INTEGRITY.json").read_text(encoding="utf-8"))
zle += [p for p, h in integ.items() if hashlib.sha256((K / p).read_bytes()).hexdigest() != h]
kurs = json.loads((K / "kurs_mentor.json").read_text(encoding="utf-8"))
for w in kurs["tygodnie"]:
    for z in w["zadania"]:
        s = (z.get("cwiczenie") or {}).get("sprawdzenie") or {}
        if s.get("rodzaj") == "test_zewnetrzny" and integ.get(s["plik_testu"]) != s.get("sha256"):
            zle.append(z["id"] + ": suma weryfikatora niezgodna z INTEGRITY.json")
print(f"Plików w manifeście: {len(m['pliki'])}, weryfikatorów: {len(integ)}, lekcji: {len(kurs['lekcje'])}")
print("OK — paczka kompletna" if not zle else "BŁĘDY:\\n" + "\\n".join(zle))
sys.exit(1 if zle else 0)
'''


def zbuduj_materialy():
    d = json.loads(ZRODLO.read_text(encoding="utf-8"))
    if CEL.exists():
        shutil.rmtree(CEL)
    CEL.mkdir(parents=True)
    n = len(d["lekcje"])
    licz = {"lekcje": 0, "cwiczenia": 0}
    for poz, l in enumerate(d["lekcje"], 1):
        t = f"tydzien_{l['tydzien']:02d}"
        _w(f"lekcje/{t}/{l['id']}.md", _md_lekcja(l, poz, n))
        licz["lekcje"] += 1
        for i, cw in enumerate(l["cwiczenia"], 1):
            _w(cw["plik"], _md_cwiczenie(l, i, cw))
            _w(cw["rozwiazanie_plik"], _md_rozwiazanie(l, i, cw))
            licz["cwiczenia"] += 1
    # weryfikatory: dokładnie te bajty, których sumy są w kursie
    integ = {}
    for nazwa in testy():
        tresc = zloz_test(nazwa)
        p = CEL / "WERYFIKATORY" / nazwa
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(tresc.encode("utf-8"))
        integ[f"WERYFIKATORY/{nazwa}"] = hashlib.sha256(tresc.encode("utf-8")).hexdigest()
    for w in d["tygodnie"]:
        for z in w["zadania"]:
            s = (z.get("cwiczenie") or {}).get("sprawdzenie") or {}
            if s.get("rodzaj") == "test_zewnetrzny":
                assert integ[s["plik_testu"]] == s["sha256"], (z["id"], "suma weryfikatora niezgodna — uruchom zbuduj.py")
    _w("INTEGRITY.json", json.dumps(integ, ensure_ascii=False, indent=1))
    # przykłady, dane, zapisy agenta, rozwiązania wzorcowe zadań
    (CEL / "przyklady").mkdir(parents=True, exist_ok=True)
    for p in sorted((TU / "startowe").glob("*.py")):
        shutil.copyfile(p, CEL / "przyklady" / p.name)
    _kopiuj_drzewo(TU / "startowe" / "dane", "dane")
    _kopiuj_drzewo(TU / "odpowiedzi_agenta", "przyklady/odpowiedzi_agenta")
    _kopiuj_drzewo(TU / "wzorce", "rozwiazania/kod")
    _w("rozwiazania/kod/README.md", "# Rozwiązania wzorcowe zadań\n\nKażde przechodzi testy z WERYFIKATORY. Otwieraj po własnej próbie — porównaj, nie kopiuj. "
                                    "Pliki takie jak instalacja.txt, adres_repo.txt czy dziennik.md są przykładami formatu, nie Twoimi danymi.\n")
    _pomoc(d)
    _w("pytest.ini", PYTEST_INI)
    _w("testy/sprawdz_kurs.py", SPRAWDZ_KURS_PY)
    _w("testy/README.md", "# testy/\n\n`python testy/sprawdz_kurs.py` — sprawdza sumy SHA-256 plików paczki i weryfikatorów.\nTesty zadań są w `WERYFIKATORY/` i uruchamia je Mentor („✔ Sprawdź wynik”).\n")
    _w("SPRAWDZ_SRODOWISKO.bat", SPRAWDZ_BAT)
    _w("INSTALACJA.bat", INSTALACJA_BAT)
    _w("URUCHOM_KURS.bat", URUCHOM_BAT)
    godziny = round(sum(w["czas_min"] for w in d["tygodnie"]) / 60)
    _w("START_TUTAJ.md", START.format(wersja=d["wersja"], stan=d["stan_prawny"], poziom=d["poziom"], system=d["system"], godziny=godziny,
                                      wymagania="; ".join(d["wymagania_wstepne"]), umiejetnosci="\n".join(f"- {u}" for u in d["umiejetnosci_koncowe"])))
    zr = ["# Źródła kursu — sprawdzone materiały", "", "Każda pozycja: tytuł, data dostępu, adres. Materiały zagraniczne streszczono i przetłumaczono w lekcjach.", ""]
    zr += [f"- {z[0]} ({z[2]}) — <{z[1]}>" for z in d["zrodla_kursu"]]
    _w("ZRODLA.md", "\n".join(zr) + "\n")
    shutil.copyfile(ZRODLO, CEL / "kurs_mentor.json")
    shutil.copyfile(TU / "RAPORT_CHECKLISTA.md", CEL / "RAPORT_CHECKLISTA.md")
    pliki = {p.relative_to(CEL).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(CEL.rglob("*")) if p.is_file() and p.name != "manifest.json"}
    manifest = {"kurs": d["id"], "nazwa": d["nazwa"], "wersja": d["wersja"], "format": d["format"], "stan_prawny": d["stan_prawny"], "mentor_min": "2.9.0",
                "liczby": {"tygodnie": len(d["tygodnie"]), "lekcje": n, "zadania": sum(len(w["zadania"]) for w in d["tygodnie"]), "cwiczenia": licz["cwiczenia"],
                           "quizy": sum(len(v) for v in d["quizy"].values()), "diagnoza": len(d["diagnoza"]), "weryfikatory": len(integ)},
                "struktura": ["START_TUTAJ.md", "ZRODLA.md", "INTEGRITY.json", "kurs_mentor.json", "manifest.json", "pytest.ini", "lekcje/", "przyklady/", "cwiczenia/", "rozwiazania/",
                              "dane/", "WERYFIKATORY/", "pomoc/", "testy/"],
                "licencja": "materiały kursu — do użytku z Mentorem; dane fikcyjne; brak plików firm trzecich, kluczy i danych prywatnych",
                "pliki": pliki}
    _w("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=1))
    print(f"Materiały: {CEL} — lekcje {licz['lekcje']}, ćwiczenia {licz['cwiczenia']}, weryfikatory {len(integ)}, plików {len(pliki)}")


if __name__ == "__main__":
    zbuduj_materialy()
