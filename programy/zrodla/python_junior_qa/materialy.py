# -*- coding: utf-8 -*-
"""Generuje paczkę materiałów kursu „Python od zera → Junior QA” (STANDARD_KURSOW.md §5–6) z gotowego python-junior-qa.json:

programy/materialy/python-junior-qa/          (wersja demonstracyjna: programy/materialy/python-junior-qa-demo/, tygodnie 0–3)
├── START_TUTAJ.md, ZRODLA.md, manifest.json, mentor-manifest.json, INTEGRITY.json, kurs_mentor.json, pytest.ini
├── SPRAWDZ_SRODOWISKO.bat, INSTALACJA.bat, URUCHOM_KURS.bat
├── lekcje/tydzien_NN/<id>.md          — pełny tekst lekcji
├── przyklady/tydzien_NN/<id>.py       — programy z demonstracji lekcji (kompletne, działające); przyklady/*.py — pliki startowe zadań
├── cwiczenia/, rozwiazania/           — ćwiczenia z lekcji z 3 podpowiedziami i rozwiązaniem; rozwiazania/kod/ — rozwiązania wzorcowe zadań
├── dane/produkty.csv                  — fikcyjne produkty sklepu „Papierowy Kot”
├── projekty/                          — sklep testowy (Flask, celowe defekty) i cudzy projekt do przeczytania (pełny kurs)
├── WERYFIKATORY/test_tNN.py           — niezależne testy zadań (sumy SHA-256 w INTEGRITY.json i w kursie)
├── pomoc/                             — FAQ, typowe błędy, odzyskiwanie
└── testy/                             — sprawdzenie paczki

Uruchom: python materialy.py [--demo]  (po zbuduj.py [--demo])
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))

from sprawdz_weryfikatory import testy, zloz_test  # noqa: E402

DEMO = "--demo" in sys.argv
ZRODLO = TU.parent.parent / ("python-junior-qa-demo.json" if DEMO else "python-junior-qa.json")
CEL = TU.parent.parent / "materialy" / ("python-junior-qa-demo" if DEMO else "python-junior-qa")
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
          "Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło."]
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

START = """# START TUTAJ — {nazwa}

**Wersja kursu:** {wersja} · stan na: {stan} · format `mentor-program/1`
**Poziom:** {poziom}.
**Czas:** {tygodnie} tygodni, ok. 90 minut dziennie (pn–pt) i do 60 minut w sobotę — razem ok. {godziny} godzin; żaden tydzień nie przekracza 9 godzin (czas policzony z treści lekcji i zadań).
**System:** {system}.
**Potrzebujesz:** {wymagania}.
{demo}
## Co będziesz umieć po kursie
{umiejetnosci}

## Pierwsze 30 minut
Kurs **nie jest wbudowany w Mentora** — to osobna paczka, którą wgrywasz sam(a), kiedy chcesz zacząć.
1. **Zainstaluj Mentora** (2.9.1 lub nowszy, paczka `Mentor-windows.zip`): rozpakuj do zwykłego folderu i uruchom `Mentor.exe`. Windows może zapytać o uruchomienie niepodpisanego programu: „Więcej informacji → Uruchom mimo to”.
2. **Wgraj kurs: Ustawienia → Program nauczania → „📦 Importuj kurs ZIP…”** → wybierz plik `{zip}` (nie musisz go rozpakowywać). Mentor pokaże podgląd — nazwę, wersję, liczbę lekcji, wymagania i listę skryptów, których **nie uruchamia** — a po Twojej zgodzie rozpakuje kurs do swojego katalogu danych i przełączy się na niego.
3. **Sprawdź:** Ustawienia → Program nauczania pokazuje „{nazwa}”, a Plan — {tygodnie} tygodni. (Sam `kurs_mentor.json` przez „Importuj JSON…” nie wystarczy: bez paczki Mentor nie ma testów z `WERYFIKATORY/` i materiałów.)
4. **Mój projekt → „📁 Utwórz katalog roboczy kursu”** → **„📂 Skopiuj materiały kursu tutaj”** (dane, przykłady{projekty}; nic nie nadpisuje).
5. **Środowisko → „Zainstaluj / Napraw”** — Python 3.11–3.13 i biblioteki kursu (pytest, requests, selenium, flask) w osobnym .venv, za Twoją zgodą, bez uprawnień administratora.
6. **Panel → Diagnoza** (10 pytań) → **Lekcje → „Start: jak uczyć się z tego kursu”** → **Plan → Tydzień 0**.

## Jak sprawdzane są zadania
- Pliki zadań tworzysz w katalogu PRACA (przycisk „📝 Utwórz plik ćwiczenia”). „✔ Sprawdź wynik” uruchamia **niezależne testy** z folderu `WERYFIKATORY/` tej paczki — Mentor sprawdza ich sumę SHA-256 (INTEGRITY.json) i uruchamia je w osobnym katalogu. Testy wywołują Twoje funkcje i programy na wielu danych, także błędnych, i mówią po polsku, czego brakuje.
- Część zadań sprawdza wyjście programu („wyjście zawiera…”); zadania z dokumentami — wymagane sekcje i treść; zadania rekrutacyjne — lista kryteriów do samooceny.
- Ćwiczenia w lekcjach mają pola „Twoje odpowiedzi” sprawdzane pole po polu.
- Zielony test to nie wszystko: wyjaśnij własnymi słowami, co i dlaczego działa.

## Bez płatnego konta
Cały kurs przejdziesz za 0 zł: Mentor, Python, Git, GitHub, PyCharm (funkcje darmowe). Asystent AI: tryb Offline w Mentorze albo darmowy czat; Claude Code (płatny plan) jest opcjonalny.

## Gdzie co jest
- `lekcje/` — lekcje (Markdown); `przyklady/tydzien_NN/` — programy z demonstracji; `cwiczenia/` i `rozwiazania/` — ćwiczenia z lekcji z podpowiedziami; `rozwiazania/kod/` — rozwiązania wzorcowe zadań (otwieraj po własnej próbie).
- `przyklady/*.py` — pliki startowe zadań (część celowo z błędami); `dane/produkty.csv` — dane fikcyjne.{projekty_opis}
- `pomoc/` — FAQ, typowe błędy, odzyskiwanie. `pytest.ini` — po skopiowaniu do PRACA `python -m pytest -q` uruchamia tylko Twoje testy.

## Aktualność i źródła
Fakty o narzędziach (Python, pytest, Selenium, Git, GitHub Actions, PyCharm), terminologia ISTQB/SJSI i dane rynku pracy sprawdzono 23.11.2026 — źródła z datą dostępu są przy każdej lekcji i w `ZRODLA.md`.

## Bezpieczeństwo i licencje
Paczka zawiera wyłącznie materiały kursu: dane fikcyjne (sklep „Papierowy Kot”), bez kluczy API, haseł, danych osobowych i programów firm trzecich.
"""


FAQ = """# FAQ — najczęstsze pytania

**„✔ Sprawdź wynik” mówi „Brak pliku …”.** Plik musi leżeć bezpośrednio w katalogu PRACA i mieć dokładnie tę nazwę (włącz widoczne rozszerzenia — `plik.py.txt` to nie `plik.py`).

**„W pliku brakuje funkcji …”.** Nazwy funkcji i parametrów są częścią specyfikacji — skopiuj je dosłownie z zadania.

**Testy „wiszą” albo kończą się po czasie.** W pliku jest `input()` poza blokiem `if __name__ == "__main__":` — test czeka na klawiaturę.

**„pytest nie jest dostępny w środowisku kursu”.** Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.

**Nie mam płatnego planu AI.** Nie jest potrzebny — Asystent Offline w Mentorze, lekcje i podpowiedzi wystarczą.

**Selenium: „Unable to obtain driver”.** Pierwsze uruchomienie wymaga internetu (Selenium Manager pobiera sterownik Edge/Chrome); potem działa z pamięci podręcznej.

**Sklep testowy nie odpowiada (ERR_CONNECTION_REFUSED).** W osobnym oknie terminala Mentora: `cd projekty\\sklep_testowy` → `python app.py`.

**Testy Git mówią „Nie znaleziono programu git”.** Zainstaluj Git for Windows (git-scm.com albo `winget install --id Git.Git -e`) i uruchom Mentora ponownie.

**Asystent proponuje zmienić testy z WERYFIKATORY.** Odmów. Te testy są kopiowane przez Mentora z paczki i sprawdzane sumą SHA-256 — zmiana w Twoim folderze nic nie da, a zasada „nie zmieniaj testów” jest częścią kursu.

**Czy mogę pisać w PyCharm albo VS Code?** Tak — pliki zapisuj w katalogu PRACA i wskaż interpreter środowiska kursu (ścieżka w Mentorze → Środowisko).
"""

ODZYSKIWANIE = """# Odzyskiwanie — gdy coś poszło nie tak

- **Zepsuty plik, bez commita:** `git diff plik.py` (zobacz, co tracisz) → `git restore plik.py`.
- **Zły commit:** `git revert HEAD` (nowy commit odwracający — bezpieczne).
- **Klucz API trafił do repozytorium:** unieważnij klucz w panelu usługi NATYCHMIAST, wygeneruj nowy, ustaw w zmiennej środowiskowej; usunięcie pliku nie usuwa go z historii.
- **Testy zapisały coś do Twoich danych:** w testach zawsze `tmp_path`; dane odtworzysz z `dane/produkty.csv` paczki.
- **Zepsute środowisko Pythona:** Mentor → Środowisko → „Napraw środowisko”.
- **Zagubione materiały kursu:** Mój projekt → „📂 Skopiuj materiały kursu tutaj” (nie nadpisuje Twoich plików) albo rozpakuj ZIP kursu ponownie.
- **Postępy w Mentorze:** zapisane w `mentor_dane.json` w katalogu danych Mentora (`%LOCALAPPDATA%\\Mentor\\`; w trybie przenośnym — obok Mentor.exe) — skopiuj go jako kopię zapasową.
"""


def _pomoc(d):
    if (TU / "pomoc").exists():
        _kopiuj_drzewo(TU / "pomoc", "pomoc")
    _w("pomoc/FAQ.md", FAQ)
    _w("pomoc/ODZYSKIWANIE.md", ODZYSKIWANIE)
    o = ["# Typowe błędy — z każdej lekcji", ""]
    for l in d["lekcje"]:
        o.append(f"## {l['nazwa']} (tydzień {l['tydzien']})")
        for b in l["typowe_bledy"]:
            o.append(f"- **{b['komunikat']}** — {b['przyczyna']} → {b['poprawka']}")
        o.append("")
    o += ["## Komunikaty Pythona i Selenium (Asystent offline)", ""] + [f"- **{k}** — {v}" for k, v in d["bledy"].items()]
    _w("pomoc/BLEDY.md", "\n".join(o) + "\n")


SPRAWDZ_BAT = r"""@echo off
chcp 65001 >nul
echo === Sprawdzenie srodowiska kursu Python Junior QA (niczego nie zmienia) ===
where python >nul 2>nul && (python --version) || echo [!] Python: brak w PATH - Mentor zainstaluje srodowisko kursu sam (zakladka Srodowisko).
where git >nul 2>nul && (git --version) || echo [!] Git: brak - potrzebny od tygodnia 0 (git-scm.com, lekcja Narzedzia).
where claude >nul 2>nul && (claude --version) || echo [i] Claude Code: brak - opcjonalny.
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (echo Edge: jest) else (echo [i] Edge: nie znaleziono - Selenium od tygodnia 8 moze uzyc Chrome.)
echo.
pause
"""

INSTALACJA_BAT = r"""@echo off
chcp 65001 >nul
set CEL=%USERPROFILE%\Documents\Mentor\nauka-python\PRACA
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
echo Nie znaleziono Mentor.exe obok paczki. Uruchom Mentora i wgraj kurs: Ustawienia - Program nauczania - Importuj kurs ZIP - plik ZIP kursu.
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


def manifest_importu(d):
    """mentor-manifest.json (schemat mentor-course/1): Mentor czyta go przy „Importuj kurs ZIP…” — id, wersja, plik kursu, wymagania środowiska."""
    s = d["srodowisko"]
    return {"schema": "mentor-course/1", "course_id": d["id"], "version": d["wersja"], "entrypoint": "kurs_mentor.json", "title": d["nazwa"], "mentor_min": "2.9.1",
            "requirements": {"python": s["python"], "python_packages": list(s["pakiety"]), "required_tools": list(s.get("narzedzia_wymagane") or []),
                             "optional_tools": [{"name": k, "from_week": v} for k, v in s["narzedzia_opcjonalne"].items()]},
            "checks": list(s.get("sprawdzenia") or [])}


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
    uzyte = {(z.get("cwiczenie") or {}).get("sprawdzenie", {}).get("plik_testu", "").split("/")[-1] for w in d["tygodnie"] for z in w["zadania"]}
    for nazwa in testy():
        if nazwa not in uzyte:
            continue
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
    pliki_zadan = {z["cwiczenie"]["plik"] for w in d["tygodnie"] for z in w["zadania"] if z.get("cwiczenie")}
    pliki_zadan |= {p for w in d["tygodnie"] for z in w["zadania"] for p in z.get("pliki", [])}
    for p in sorted((TU / "startowe").glob("*.py")):
        if p.name in pliki_zadan:
            shutil.copyfile(p, CEL / "przyklady" / p.name)
    _kopiuj_drzewo(TU / "startowe" / "dane", "dane")
    for l in d["lekcje"]:
        if l["przyklad"].lstrip().startswith(("PS ", "#!", "python-projekty", "PROJEKTY", "Prompt", "## BUG")) or "import" not in l["przyklad"] and "print(" not in l["przyklad"]:
            continue
        _w(f"przyklady/tydzien_{l['tydzien']:02d}/{l['id']}.py", l["przyklad"])
    for p in sorted((TU / "wzorce").rglob("*")):
        rel = p.relative_to(TU / "wzorce").as_posix()
        if p.is_file() and not (POMIN & set(p.parts)) and (not DEMO or rel in pliki_zadan or rel in ("README.md", "hello.py")):
            c = CEL / "rozwiazania" / "kod" / rel
            c.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, c)
    if not DEMO:
        _kopiuj_drzewo(TU / "projekty", "projekty")
    _w("rozwiazania/kod/README.md", "# Rozwiązania wzorcowe zadań\n\nKażde przechodzi testy z WERYFIKATORY. Otwieraj po własnej próbie — porównaj, nie kopiuj.\n")
    _pomoc(d)
    _w("pytest.ini", PYTEST_INI)
    _w("testy/sprawdz_kurs.py", SPRAWDZ_KURS_PY)
    _w("testy/README.md", "# testy/\n\n`python testy/sprawdz_kurs.py` — sprawdza sumy SHA-256 plików paczki i weryfikatorów.\nTesty zadań są w `WERYFIKATORY/` i uruchamia je Mentor („✔ Sprawdź wynik”).\n")
    _w("SPRAWDZ_SRODOWISKO.bat", SPRAWDZ_BAT)
    _w("INSTALACJA.bat", INSTALACJA_BAT)
    _w("URUCHOM_KURS.bat", URUCHOM_BAT)
    godziny = round(sum(w["czas_min"] for w in d["tygodnie"]) / 60)
    demo = ("\n> **Wersja demonstracyjna:** tygodnie 0–3 z 13 (konfiguracja i podstawy Pythona) — 16 lekcji i 20 zadań z niezależnymi testami. "
            "Pełny kurs (`Python-junior-qa-kurs.zip`) dodaje pliki i Git w zespole, klasy, API, techniki testowania ISTQB, pytest, Selenium z Page Object Model, "
            "raporty błędów, CI, SQLite, Flask i projekt portfolio. Postępy wersji demonstracyjnej są zapisywane osobno.\n") if DEMO else ""
    _w("START_TUTAJ.md", START.format(nazwa=d["nazwa"], wersja=d["wersja"], stan=d["stan_prawny"], poziom=d["poziom"], system=d["system"], godziny=godziny,
                                      tygodnie=len(d["tygodnie"]), demo=demo, zip="Python-junior-qa-demo.zip" if DEMO else "Python-junior-qa-kurs.zip",
                                      projekty="" if DEMO else ", sklep testowy", projekty_opis="" if DEMO else " `projekty/sklep_testowy/` — lokalny sklep do testów Selenium i raportów błędów (celowe defekty), `projekty/cudzy_projekt/` — projekt do przeczytania (tydzień 6).",
                                      wymagania="; ".join(d["wymagania_wstepne"]), umiejetnosci="\n".join(f"- {u}" for u in d["umiejetnosci_koncowe"])))
    zr = ["# Źródła kursu — sprawdzone materiały", "", "Każda pozycja: tytuł, data dostępu, adres. Materiały zagraniczne streszczono i przetłumaczono w lekcjach.", ""]
    zr += [f"- {z[0]} ({z[2]}) — <{z[1]}>" for z in d["zrodla_kursu"]]
    _w("ZRODLA.md", "\n".join(zr) + "\n")
    shutil.copyfile(ZRODLO, CEL / "kurs_mentor.json")
    if (TU / "RAPORT_CHECKLISTA.md").exists():
        shutil.copyfile(TU / "RAPORT_CHECKLISTA.md", CEL / "RAPORT_CHECKLISTA.md")
    _w("mentor-manifest.json", json.dumps(manifest_importu(d), ensure_ascii=False, indent=1))
    pliki = {p.relative_to(CEL).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(CEL.rglob("*")) if p.is_file() and p.name != "manifest.json"}
    manifest = {"kurs": d["id"], "nazwa": d["nazwa"], "wersja": d["wersja"], "format": d["format"], "stan_prawny": d["stan_prawny"], "mentor_min": "2.9.1",
                "liczby": {"tygodnie": len(d["tygodnie"]), "lekcje": n, "zadania": sum(len(w["zadania"]) for w in d["tygodnie"]), "cwiczenia": licz["cwiczenia"],
                           "quizy": sum(len(v) for v in d["quizy"].values()), "diagnoza": len(d["diagnoza"]), "weryfikatory": len(integ)},
                "struktura": ["START_TUTAJ.md", "ZRODLA.md", "INTEGRITY.json", "kurs_mentor.json", "mentor-manifest.json", "manifest.json", "pytest.ini", "lekcje/", "przyklady/", "cwiczenia/", "rozwiazania/",
                              "dane/", "projekty/", "WERYFIKATORY/", "pomoc/", "testy/"],
                "licencja": "materiały kursu — do użytku z Mentorem; dane fikcyjne; brak plików firm trzecich, kluczy i danych prywatnych",
                "pliki": pliki}
    _w("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=1))
    print(f"Materiały: {CEL} — lekcje {licz['lekcje']}, ćwiczenia {licz['cwiczenia']}, weryfikatory {len(integ)}, plików {len(pliki)}")


if __name__ == "__main__":
    zbuduj_materialy()
