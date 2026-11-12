# -*- coding: utf-8 -*-
"""Generuje paczkę materiałów kursu (STANDARD_KURSOW.md §5–6) z gotowego kadry-i-place.json:

programy/materialy/kadry-i-place/
├── START_TUTAJ.md, manifest.json, SPRAWDZ_SRODOWISKO.bat, INSTALACJA.bat, URUCHOM_KURS.bat
├── lekcje/tydzien_NN/<id>.md          — pełny tekst lekcji (offline, do druku)
├── przyklady/tydzien_NN/<id>.md       — demonstracja z omówieniem + pliki danych
├── cwiczenia/tydzien_NN/<id>_<n>.md   — pliki startowe (treść, oczekiwany wynik, miejsce na odpowiedź)
├── rozwiazania/tydzien_NN/<id>_<n>.md — 3 podpowiedzi + pełne rozwiązanie
├── projekty/kadry-praktyka-przyklad/  — przykładowy katalog projektu (FIRMA.md, dziennik.md)
├── testy/                             — sprawdzenie paczki (bat + py)
├── pomoc/                             — FAQ, typowe błędy, komunikaty Warsztatu, odzyskiwanie
└── instalatory/README.md              — co (nie) trzeba instalować

Uruchom: python materialy.py  (po zbuduj.py)
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent
sys.path.insert(0, str(TU))
sys.path.insert(0, str(TU.parent.parent.parent))  # katalog Mentora (kadry.py)

from materialy_dodatkowe import PRZYKLADY, EXTRA_START  # noqa: E402

ZRODLO = TU.parent.parent / "kadry-i-place.json"
CEL = TU.parent.parent / "materialy" / "kadry-i-place"


def _w(sciezka, tresc):
    p = CEL / sciezka
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(tresc.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def _md_lekcja(l, poz, n):
    o = [f"# {l['nazwa']}", f"Tydzień {l['tydzien']} · lekcja {poz} z {n} · ≈ {l.get('czas_min', 20)} min", ""]
    if l.get("cel"):
        o += [f"**Po tej lekcji potrafisz:** {l['cel']}", ""]
    if l.get("po_co"):
        o += [f"**Po co mi to?** {l['po_co']}", ""]
    if l.get("wymagania"):
        o += ["## Czego potrzebujesz"] + [f"- {x}" for x in l["wymagania"]] + [""]
    o += ["## 1 · Wyjaśnienie od podstaw"]
    for a in l["wyjasnienie"].split("\n"):
        a = a.strip()
        if not a:
            continue
        o.append(("### " + a[3:]) if a.startswith("## ") else a)
    o.append("")
    dem = l.get("demonstracja") or {}
    o += ["## 2 · Demonstracja — kompletny przykład omówiony krok po kroku"]
    if dem.get("tytul"):
        o.append(f"**{dem['tytul']}**")
    if l.get("przyklad"):
        o += ["", "```", l["przyklad"], "```", ""]
    for i, k in enumerate(dem.get("kroki", []), 1):
        o.append(f"{i}. {k}")
    if dem.get("wynik"):
        o += ["", f"✔ **Oczekiwany wynik:** {dem['wynik']}"]
    o.append("")
    if l.get("jak_uruchomic"):
        o += ["## 3 · Jak to uruchomić"] + [f"{i}. {x}" for i, x in enumerate(l["jak_uruchomic"], 1)] + [""]
    if l.get("w_praktyce"):
        o += ["## W praktyce — jak to robisz w firmie"] + [f"{i}. {x}" for i, x in enumerate(l["w_praktyce"], 1)] + [""]
    for nr, cw in enumerate(l.get("cwiczenia", []), 4):
        rodzaj = "prowadzone" if cw.get("rodzaj") == "prowadzone" else "samodzielne"
        o += [f"## {nr} · Ćwiczenie {rodzaj}", cw["tresc"], "", f"📄 Plik startowy: `{cw['plik']}` · rozwiązanie: `{cw['rozwiazanie_plik']}`", f"✔ Poprawny wynik wygląda tak: {cw['wynik']}", ""]
    if l.get("typowe_bledy"):
        o += [f"## {4 + len(l.get('cwiczenia', []))} · Typowe błędy i naprawa"]
        for b in l["typowe_bledy"]:
            o += [f"- ✘ **{b['komunikat']}**", f"  - Prawdopodobna przyczyna: {b['przyczyna']}", f"  - Jak sprawdzić: {b['diagnoza']}", f"  - Poprawka: {b['poprawka']}"]
        o.append("")
    if l.get("pulapki"):
        o += ["## Pułapki"] + [f"- {x}" for x in l["pulapki"]] + [""]
    if l.get("zadania"):
        o += ["## Dodatkowe zadania"] + [f"{i}. {x}" for i, x in enumerate(l["zadania"], 1)] + [""]
    if l.get("pytania"):
        o += ["## Sprawdzenie — odpowiedz na głos, potem rozwiń"]
        for p, odp in l["pytania"]:
            o += [f"- **{p}**", f"  - {odp}"]
        o.append("")
    if l.get("podsumowanie"):
        o += ["## Co potrafię teraz zrobić bez patrzenia na przykład?", l["podsumowanie"], ""]
    if l.get("test"):
        o += ["## Test (w Mentorze: Lekcje → Sprawdź się)"]
        for q in l["test"]:
            o.append(f"- {q['p']}")
            for i, op in enumerate(q["o"]):
                o.append(f"  - {'ABCD'[i]}) {op}")
        o += ["", "Odpowiedzi: " + ", ".join("ABCD"[q["odp"]] for q in l["test"]), ""]
    return "\n".join(o)


def _md_przyklad(l):
    dem = l.get("demonstracja") or {}
    o = [f"# Przykład — {l['nazwa']}", f"Tydzień {l['tydzien']}", ""]
    if dem.get("tytul"):
        o += [f"**{dem['tytul']}**", ""]
    if l.get("przyklad"):
        o += ["```", l["przyklad"], "```", ""]
    o += ["## Omówienie — co robi każdy krok i dlaczego"] + [f"{i}. {k}" for i, k in enumerate(dem.get("kroki", []), 1)]
    if dem.get("wynik"):
        o += ["", f"✔ Oczekiwany wynik: {dem['wynik']}"]
    if l.get("jak_uruchomic"):
        o += ["", "## Jak to uruchomić"] + [f"{i}. {x}" for i, x in enumerate(l["jak_uruchomic"], 1)]
    return "\n".join(o) + "\n"


def _md_cwiczenie(l, nr, cw):
    klucz = f"{l['id']}_{nr}"
    o = [f"# Ćwiczenie {nr} ({cw['rodzaj']}) — {l['nazwa']}", f"Tydzień {l['tydzien']} · lekcja `{l['id']}` · plik: `{cw['plik']}`", "",
         "## Zadanie", cw["tresc"], "", "## Oczekiwany wynik (sprawdź, czy Twój wygląda tak samo)", cw["wynik"], "",
         "## Jak sprawdzić", "1. Zrób zadanie poniżej (albo w Warsztacie / w pliku, który wskazuje treść).",
         "2. Porównaj z sekcją „Oczekiwany wynik”.", f"3. Utknąłeś? W Mentorze: Lekcje → ta lekcja → „Podpowiedź 1 z 3” (albo w Asystencie offline wpisz „podpowiedź {nr}”).",
         f"4. Po własnej próbie otwórz rozwiązanie: `{cw['rozwiazanie_plik']}` — i wyjaśnij je własnymi słowami.", ""]
    if klucz in EXTRA_START:
        o += [EXTRA_START[klucz].rstrip(), ""]
    o += ["## Twoja odpowiedź", "", "(pisz tutaj)", "", "## Czego się nauczyłem / co sprawdzić jutro", "", ""]
    return "\n".join(o)


def _md_rozwiazanie(l, nr, cw):
    o = [f"# Rozwiązanie — ćwiczenie {nr} ({cw['rodzaj']}) — {l['nazwa']}", f"Plik startowy: `{cw['plik']}`", "",
         "Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.", "",
         "## Podpowiedź 1 — pytanie naprowadzające", cw["wskazowki"][0], "", "## Podpowiedź 2 — gdzie szukać", cw["wskazowki"][1], "",
         "## Podpowiedź 3 — częściowy przykład", cw["wskazowki"][2], "", "## Pełne rozwiązanie", "```", cw["rozwiazanie"], "```", "",
         "## Oczekiwany wynik", cw["wynik"], "", "## Wyjaśnij własnymi słowami", "Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?", ""]
    return "\n".join(o)


START_TUTAJ = """# START TUTAJ — Kadry i płace: kurs zaawansowany (praktyka 2026)

**Wersja kursu:** {wersja} · stan prawny: {stan_prawny} · format `mentor-program/1`
**Poziom:** {poziom}.
**Czas:** 12 tygodni × 5 dni × 60–90 minut.
**System:** {system}.
**Potrzebujesz:** {wymagania}.
**Nie potrzebujesz:** internetu (kurs i Asystent offline działają bez sieci), kont w eZUS/e-Urzędzie (w Mentorze są symulatory), Excela, Pythona, żadnych instalacji poza samym Mentorem.

## Co będziesz umieć po kursie
{umiejetnosci}

## Pierwsze 30 minut (krok po kroku)
1. **Rozpakuj ZIP** do zwykłego folderu, np. `C:\\Users\\<Ty>\\Mentor` (ścieżka może mieć spacje i polskie znaki). Nie uruchamiaj z wnętrza archiwum.
2. **Sprawdź środowisko (opcjonalnie):** kliknij dwukrotnie `SPRAWDZ_SRODOWISKO.bat` — wypisze po polsku, co wykrył; niczego nie zmienia.
3. **Uruchom Mentora:** `URUCHOM_KURS.bat` albo `Mentor.exe` (Windows może zapytać „Czy chcesz uruchomić?” — plik nie jest podpisany certyfikatem; wybierz „Więcej informacji → Uruchom mimo to”). Alternatywa z Pythonem: `python mentor.py`.
4. **W Mentorze:** Ustawienia → Program nauczania → „Kadry i płace — kurs zaawansowany (praktyka 2026)” (jest wbudowany; `kurs_mentor.json` w tej paczce to ten sam plik — użyj „Wgraj program z pliku…” tylko na innym komputerze z Mentorem bez tego kursu).
5. **Przewodnik „Jak zacząć”** otworzy się sam: wpisz imię, **„Wybierz katalog…”** (utwórz folder `kadry-praktyka` w Dokumentach) i kliknij **„Skopiuj materiały kursu do katalogu projektu”** — to skopiuje do Twojego folderu: START_TUTAJ.md, `cwiczenia/`, `przyklady/`, `rozwiazania/`, `pomoc/`, `lekcje/`. (To samo zrobi `INSTALACJA.bat`, jeśli wolisz poza Mentorem.)
6. **Diagnoza na start** (Panel → Pierwsze kroki → Diagnoza; 10 pytań, 5 minut, nie blokuje nauki) — wynik wskaże lekcje, przy których warto zwolnić.
7. **Lekcje → pierwsza lekcja** „Start: jak uczyć się z tego programu” (15 minut) → test 3 pytań.
8. **Plan → Tydzień 0 → zadanie 1 → „Jak to zrobić”** — pierwsze zadanie: plik FIRMA.md (Warsztat → Firma ćwiczeniowa → „Zapisz FIRMA.md do projektu”).

Pierwsze działające ćwiczenie masz w ciągu 30 minut: Warsztat → Lista płac → Osoba „Katarzyna Wójcik” → „Policz” → netto 3 501,73 zł (a bez PPK: 3 605,85).

## Jak wygląda każda lekcja (zawsze ta sama kolejność)
cel → po co mi to → czego potrzebujesz → **1** wyjaśnienie od podstaw → **2** demonstracja omówiona krok po kroku → **3** jak to uruchomić → **4** ćwiczenie prowadzone → **5** ćwiczenie samodzielne (3 podpowiedzi, potem rozwiązanie) → **6** typowe błędy i naprawa → sprawdzenie (pytania + „co potrafię bez przykładu”) → test (2/3 zalicza).
Każde ćwiczenie ma plik startowy w `cwiczenia/tydzien_NN/` i rozwiązanie w `rozwiazania/tydzien_NN/` — te same treści są w Mentorze (Lekcje), więc możesz pracować w aplikacji albo na plikach.

## Gdzie co jest w paczce
- `kurs_mentor.json` — plik kursu (kopia `programy/kadry-i-place.json`); `manifest.json` — lista plików z sumami kontrolnymi.
- `lekcje/` — pełne lekcje w Markdown (do czytania offline/druku); `przyklady/` — demonstracje i dane do ćwiczeń; `cwiczenia/` — pliki startowe; `rozwiazania/` — podpowiedzi i rozwiązania; `projekty/` — przykładowy katalog projektu; `testy/` — sprawdzenie paczki; `pomoc/` — FAQ, typowe błędy, komunikaty Warsztatu, odzyskiwanie; `instalatory/` — informacja, że nic nie trzeba instalować (i skąd legalnie pobrać Pythona, gdyby ktoś chciał uruchamiać ze źródeł).
- Twoje pliki powstają w **katalogu projektu** (wskazanym w Mentorze), nie w paczce — paczkę możesz skopiować ponownie bez utraty pracy (kopiowanie nie nadpisuje istniejących plików).

## Asystent AI — trzy tryby, zawsze nauczyciel, nie wykonawca
- **Offline** (domyślny, bez konta i opłat): komendy „uczę się [temat]”, „podpowiedź”, „zadaj mi 3 pytania”, „quiz z tygodnia 4”, „odpytaj mnie jak rekruter”, „utknąłem: …”.
- **API** (opcjonalnie, płatne za użycie — klucz z console.anthropic.com; koszt zależy od użycia, kilka–kilkanaście groszy za rozmowę) i **Subskrypcja** (Claude Code — płatny abonament). Żadne zadanie kursu nie wymaga trybu płatnego.
- Zasada: najpierw własna próba i podpowiedzi po kolei; gdy nie wiesz, jak zacząć — pytaj od razu o wskazówkę, nie o wynik. Asystent nie wysyła Twoich plików nigdzie bez Twojej zgody (tryb API wysyła tylko to, co wpiszesz lub wskażesz).

## Powtórki, quizy, postępy
- Po każdym etapie: rozbudowana powtórka (przypomnienie, przykład, typowe błędy, ćwiczenie prowadzone i samodzielne, test).
- Sobota: quiz tygodnia; błędne pytania wracają w powtórce i wskazują lekcję do przeczytania.
- Postępy (XP, odznaki, zaliczone testy) zapisują się w `mentor_dane.json` obok Mentor.exe — **kopia zapasowa:** skopiuj ten plik; przywrócenie: wklej z powrotem. Nowa wersja kursu nie kasuje postępów (id zadań i lekcji są stałe).

## Gdy coś nie działa
`pomoc/FAQ.md` (najczęstsze pytania), `pomoc/ODZYSKIWANIE.md` (reset, kopia, ponowna instalacja), `pomoc/KOMUNIKATY_WARSZTATU.md` (co znaczą komunikaty weryfikacji w symulatorach), `pomoc/BLEDY.md` (typowe błędy merytoryczne z każdej lekcji).

## Licencje i bezpieczeństwo
Wszystkie pliki w paczce są własnymi materiałami kursu (dane firmy i osób fikcyjne, PESEL-e wygenerowane). Paczka nie zawiera programów firm trzecich, kluczy API, haseł ani danych prywatnych. Przepisy w Warsztacie to streszczenia — pełne teksty są publiczne w ISAP (isap.sejm.gov.pl), bez logowania; nie są potrzebne do żadnego ćwiczenia.
"""

SPRAWDZ_BAT = r"""@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
title Mentor - sprawdzenie srodowiska (nic nie zmienia)
echo ================================================================
echo  MENTOR - KADRY I PLACE: sprawdzenie srodowiska
echo  Ten skrypt tylko sprawdza i wypisuje. Niczego nie instaluje.
echo ================================================================
echo.
set "TU=%~dp0"
echo Folder paczki: "%TU%"
echo.
set BRAK=0
rem --- Windows
for /f "tokens=4-5 delims=. " %%i in ('ver') do set WER=%%i.%%j
echo [1] Windows: wersja %WER%  (wymagany Windows 10 lub 11)
rem --- Mentor.exe lub python
if exist "%TU%Mentor.exe" (
    echo [2] Mentor.exe: JEST
) else (
    if exist "%TU%mentor.py" (
        echo [2] Mentor.exe: brak, ale jest mentor.py - sprawdzam Pythona...
        where python >nul 2>nul
        if !errorlevel!==0 (
            for /f "tokens=2" %%v in ('python --version 2^>^&1') do echo     Python %%v  (wymagany 3.10 lub nowszy)
        ) else (
            echo     Python: NIE ZNALEZIONO. Pobierz oficjalnie: https://www.python.org/downloads/windows/  (wersja 3.12, zaznacz "Add python.exe to PATH")
            set BRAK=1
        )
    ) else (
        echo [2] Mentor.exe: BRAK - rozpakuj caly ZIP (nie uruchamiaj z wnetrza archiwum).
        set BRAK=1
    )
)
rem --- kurs
if exist "%TU%programy\kadry-i-place.json" (echo [3] Plik kursu programy\kadry-i-place.json: JEST) else (
    if exist "%TU%kurs_mentor.json" (echo [3] Plik kursu kurs_mentor.json: JEST ^(wgraj w Mentorze: Ustawienia - Wgraj program z pliku^)) else (echo [3] Plik kursu: BRAK & set BRAK=1))
rem --- materialy
set "MAT=%TU%programy\materialy\kadry-i-place"
if not exist "%MAT%\START_TUTAJ.md" set "MAT=%TU%"
if exist "%MAT%\cwiczenia" (echo [4] Materialy ^(cwiczenia, rozwiazania, pomoc^): JEST w "%MAT%") else (echo [4] Materialy: BRAK katalogu cwiczenia & set BRAK=1)
rem --- zapis w folderze
echo test > "%TU%_test_zapisu.tmp" 2>nul
if exist "%TU%_test_zapisu.tmp" (del "%TU%_test_zapisu.tmp" & echo [5] Zapis w folderze paczki: OK ^(Mentor zapisuje tu postepy: mentor_dane.json^)) else (
    echo [5] Zapis w folderze paczki: BRAK UPRAWNIEN - przenies folder np. do Dokumentow. & set BRAK=1)
rem --- miejsce na dysku
for /f "tokens=3" %%a in ('dir /-c "%TU%" ^| find "bajtów wolnych"') do set WOLNE=%%a
if not defined WOLNE for /f "tokens=3" %%a in ('dir /-c "%TU%" ^| find "bytes free"') do set WOLNE=%%a
if defined WOLNE (echo [6] Wolne miejsce na dysku: %WOLNE% bajtow ^(potrzeba ok. 100 MB^)) else (echo [6] Wolne miejsce: nie udalo sie odczytac - sprawdz w Eksploratorze ^(potrzeba ok. 100 MB^))
rem --- Dokumenty
if exist "%USERPROFILE%\Documents" (echo [7] Folder Dokumenty: "%USERPROFILE%\Documents" ^(tu INSTALACJA.bat zaproponuje katalog projektu^)) else (echo [7] Folder Dokumenty: nie znaleziono - katalog projektu wskazesz recznie w Mentorze)
rem --- internet (niewymagany)
echo [8] Internet: NIEWYMAGANY ^(kurs, Warsztat i Asystent offline dzialaja bez sieci^)
echo.
if %BRAK%==0 (
    echo WYNIK: srodowisko gotowe. Nastepny krok: URUCHOM_KURS.bat ^(albo Mentor.exe^), potem w Mentorze "Jak zaczac".
) else (
    echo WYNIK: czegos brakuje - patrz pozycje z napisem BRAK. Po poprawieniu uruchom ten skrypt ponownie.
)
echo.
pause
"""

INSTALACJA_BAT = r"""@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
title Mentor - instalacja materialow kursu (z potwierdzeniem)
set "TU=%~dp0"
set "MAT=%TU%programy\materialy\kadry-i-place"
if not exist "%MAT%\START_TUTAJ.md" set "MAT=%TU%"
set "CEL=%USERPROFILE%\Documents\kadry-praktyka"
echo ================================================================
echo  MENTOR - KADRY I PLACE: instalacja materialow kursu
echo ================================================================
echo.
echo Ten skrypt NIE instaluje zadnych programow (Mentor dziala bez instalacji).
echo Zrobi tylko jedno: skopiuje materialy kursu do Twojego katalogu projektu.
echo.
echo   Zrodlo:  "%MAT%"
echo   Cel:     "%CEL%"
echo.
echo Istniejace pliki o tej samej nazwie NIE zostana nadpisane (Twoja praca jest bezpieczna).
echo Mozesz tez zrobic to samo w Mentorze: Moj projekt - "Skopiuj materialy kursu tutaj".
echo.
set /p ODP="Kontynuowac? [T/N] "
if /i not "%ODP%"=="T" (echo Przerwano - nic nie zmieniono. & pause & exit /b 0)
set /p INNY="Inny katalog docelowy? Wpisz sciezke albo ENTER, zeby uzyc domyslnego: "
if not "%INNY%"=="" set "CEL=%INNY%"
if not exist "%CEL%" (
    mkdir "%CEL%" 2>nul
    if not exist "%CEL%" (echo BLAD: nie mozna utworzyc "%CEL%" - brak uprawnien lub zla sciezka. & pause & exit /b 1)
)
set N=0
for %%D in (lekcje przyklady cwiczenia rozwiazania pomoc projekty testy) do (
    if exist "%MAT%\%%D" (
        xcopy "%MAT%\%%D" "%CEL%\%%D\" /E /I /Q /Y /D >nul 2>nul
        rem /D kopiuje tylko nowsze; dodatkowo nie nadpisujemy zmienionych przez ucznia: robocopy z /XO /XN /XC
        robocopy "%MAT%\%%D" "%CEL%\%%D" /E /XO /XN /XC /NFL /NDL /NJH /NJS /NC /NS /NP >nul 2>nul
        set /a N+=1
    )
)
if exist "%MAT%\START_TUTAJ.md" if not exist "%CEL%\START_TUTAJ.md" copy "%MAT%\START_TUTAJ.md" "%CEL%\" >nul
if not exist "%CEL%\dziennik.md" (
    echo # Dziennik nauki - kadry i place> "%CEL%\dziennik.md"
    echo.>> "%CEL%\dziennik.md"
    echo Dzien 1: >> "%CEL%\dziennik.md"
)
echo.
echo Gotowe. Skopiowano %N% katalogow do "%CEL%".
echo W Mentorze: Ustawienia (lub Moj projekt) - "Wybierz katalog..." - wskaz ten folder.
echo Wycofanie: usun folder "%CEL%" (paczka zostaje nietknieta). Reset jednego cwiczenia: skasuj jego plik i uruchom ten skrypt ponownie.
echo.
pause
"""

URUCHOM_BAT = r"""@echo off
chcp 65001 >nul
title Mentor - Kadry i place
set "TU=%~dp0"
cd /d "%TU%"
if exist "%TU%Mentor.exe" (
    start "" "%TU%Mentor.exe"
    exit /b 0
)
if exist "%TU%mentor.py" (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Nie znaleziono Mentor.exe ani Pythona. Rozpakuj caly ZIP albo zainstaluj Pythona 3.12 z https://www.python.org/downloads/windows/
        pause
        exit /b 1
    )
    python "%TU%mentor.py"
    exit /b %errorlevel%
)
echo Nie znaleziono Mentor.exe w folderze "%TU%". Rozpakuj caly ZIP do jednego folderu.
pause
exit /b 1
"""

SPRAWDZ_KURS_PY = '''# -*- coding: utf-8 -*-
"""Sprawdza paczkę kursu bez Mentora: plik JSON, strukturę mentor-program/1, obecność plików ćwiczeń/rozwiązań
i sumy kontrolne z manifest.json. Uruchom: python testy/sprawdz_kurs.py (z katalogu paczki) — kod wyjścia 0 = OK."""
import hashlib
import json
import sys
from pathlib import Path

TU = Path(__file__).resolve().parent.parent
bledy = []
js = TU / "kurs_mentor.json"
if not js.exists():
    js = TU.parent.parent / "kadry-i-place.json"
if not js.exists():
    print("BRAK pliku kursu (kurs_mentor.json)"); sys.exit(1)
d = json.loads(js.read_text(encoding="utf-8"))
for k in ("nazwa", "etapy", "tygodnie", "lekcje"):
    if k not in d:
        bledy.append(f"brak pola {k}")
ids = {l["id"] for l in d.get("lekcje", [])}
for w in d.get("tygodnie", []):
    for lid in w.get("lekcje", []):
        if lid not in ids:
            bledy.append(f"tydzień {w.get('tydzien')}: lekcja {lid} nie istnieje")
    for z in w.get("zadania", []):
        for k in ("id", "tytul", "opis", "kroki", "sprawdz", "problemy", "pliki", "xp", "czas_min"):
            if k not in z:
                bledy.append(f"zadanie {z.get('id')}: brak {k}")
for l in d.get("lekcje", []):
    for k in ("id", "tydzien", "nazwa", "slowa", "wyjasnienie", "przyklad", "zadania", "pytania", "pulapki", "test", "cwiczenia", "demonstracja", "typowe_bledy", "podsumowanie"):
        if k not in l:
            bledy.append(f"lekcja {l.get('id')}: brak {k}")
    for q in l.get("test", []):
        if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
            bledy.append(f"lekcja {l.get('id')}: zły odp w teście")
    for cw in l.get("cwiczenia", []):
        for k in ("plik", "rozwiazanie_plik"):
            if cw.get(k) and not (TU / cw[k]).exists():
                bledy.append(f"brak pliku {cw[k]}")
for t, qs in d.get("quizy", {}).items():
    for q in qs:
        if not (isinstance(q.get("odp"), int) and 0 <= q["odp"] < len(q.get("o", []))):
            bledy.append(f"quiz {t}: zły odp")
        if q.get("lekcja") and q["lekcja"] not in ids:
            bledy.append(f"quiz {t}: lekcja {q['lekcja']} nie istnieje")
man = TU / "manifest.json"
if man.exists():
    m = json.loads(man.read_text(encoding="utf-8"))
    for sc, h in m.get("pliki", {}).items():
        p = TU / sc
        if not p.exists():
            bledy.append(f"manifest: brak {sc}")
        elif hashlib.sha256(p.read_bytes()).hexdigest() != h:
            bledy.append(f"manifest: zmieniony {sc}")
else:
    bledy.append("brak manifest.json")
print(f"Kurs: {d.get('nazwa')} v{d.get('wersja')} — tygodni {len(d.get('tygodnie', []))}, lekcji {len(d.get('lekcje', []))}, zadań {sum(len(w.get('zadania', [])) for w in d.get('tygodnie', []))}")
if bledy:
    print("DO POPRAWY:"); [print(" -", b) for b in bledy]; sys.exit(1)
print("OK — paczka kompletna, JSON poprawny, sumy kontrolne zgodne.")
'''

SPRAWDZ_KURS_BAT = r"""@echo off
chcp 65001 >nul
set "TU=%~dp0.."
echo Sprawdzanie paczki kursu w "%TU%"
set B=0
for %%F in (START_TUTAJ.md manifest.json kurs_mentor.json) do (if exist "%TU%\%%F" (echo [OK] %%F) else (echo [BRAK] %%F & set B=1))
for %%D in (lekcje przyklady cwiczenia rozwiazania pomoc projekty testy) do (if exist "%TU%\%%D" (echo [OK] %%D\) else (echo [BRAK] %%D\ & set B=1))
for /f %%n in ('dir /b /s "%TU%\cwiczenia\*.md" 2^>nul ^| find /c ".md"') do echo Plikow cwiczen: %%n (oczekiwane: 90)
for /f %%n in ('dir /b /s "%TU%\rozwiazania\*.md" 2^>nul ^| find /c ".md"') do echo Plikow rozwiazan: %%n (oczekiwane: 90)
where python >nul 2>nul && (python "%TU%\testy\sprawdz_kurs.py") || echo (Python niedostepny - pominieto sprawdzenie sum kontrolnych; to nie jest wymagane do nauki)
if %B%==0 (echo WYNIK: struktura paczki kompletna.) else (echo WYNIK: brakuje plikow - rozpakuj ZIP ponownie.)
pause
"""


def _pomoc(d):
    faq = """# FAQ — najczęstsze pytania

**Nie wiem, co dziś robić.** Panel → karta „Dzisiaj”: zadanie dnia, przycisk „Jak to zrobić” i lekcja dnia.

**Gdzie są pliki do ćwiczeń?** W katalogu projektu (który wskazałeś w Mentorze) w `cwiczenia/tydzien_NN/`; rozwiązania w `rozwiazania/`. Jeśli ich nie ma: Mój projekt → „Skopiuj materiały kursu tutaj” (albo INSTALACJA.bat).

**Mentor nie widzi mojego pliku.** Nazwa musi być dokładnie taka jak w zadaniu (Notatnik dopisuje `.txt` — włącz w Eksploratorze „Rozszerzenia nazw plików”); plik może leżeć w dowolnym podkatalogu projektu. Mój projekt → „Odśwież”.

**Czy muszę mieć internet, konto w ZUS, Excel?** Nie. Symulatory eZUS/Płatnika i e-Urzędu, kalkulatory i 48 streszczeń przepisów są w zakładce Warsztat. ISAP (pełne teksty aktów) jest publiczny, ale niepotrzebny do ćwiczeń.

**Czy Asystent jest płatny?** Tryb offline — nie (bez konta). API i Subskrypcja — tak, opcjonalnie; żadne zadanie ich nie wymaga.

**Test lekcji nie zalicza (1/3).** Zalicza 2/3; powtarzaj bez limitu — pytania sprawdzają rozumienie, nie pamięć.

**Jak zresetować ćwiczenie?** Skasuj swój plik w `cwiczenia/` i skopiuj materiały ponownie (nic innego nie zostanie nadpisane).

**Skąd Mentor bierze liczby i czy są aktualne?** Stan prawny: listopad 2026; każdy wskaźnik ma źródło (Warsztat → Przepisy, Firma ćwiczeniowa → Parametry). W styczniu aktualizujesz parametry (lekcja „Wskaźniki”).

**Wynik w Warsztacie różni się od mojego.** Tryb ćwiczenia (Lista płac → „Sprawdź”) podpowie, której kwocie równa się różnica. Najczęściej: składki liczone jedną kwotą, brak zaokrągleń, zły dzielnik.

**Przerwałem na 3 tygodnie.** Panel pokaże, ile dni minęło i od czego zacząć; XP i testy zostają; zacznij od powtórki ostatniego etapu.

**Jak zrobić kopię postępów?** Skopiuj `mentor_dane.json` (obok Mentor.exe). Przywrócenie: wklej plik z powrotem przed uruchomieniem.
"""
    odz = """# Odzyskiwanie, reset, aktualizacja

## Kopia zapasowa i przywrócenie postępów
- Postępy: `mentor_dane.json` obok `Mentor.exe` (lub obok `mentor.py`). Skopiuj go w bezpieczne miejsce (np. raz w tygodniu).
- Przywrócenie: zamknij Mentora, wklej zapisany `mentor_dane.json`, uruchom ponownie.
- Twoje pliki (FIRMA.md, listy płac, pisma) są w katalogu projektu — to zwykłe pliki; kopiuj cały folder.

## Reset
- Jedno ćwiczenie: usuń plik z `cwiczenia/tydzien_NN/` i uruchom INSTALACJA.bat (lub Mój projekt → Skopiuj materiały) — skopiuje tylko brakujące.
- Postępy programu: Ustawienia → eksport postępów (kopia), potem usuń `mentor_dane.json` → Mentor startuje od zera (dla wszystkich programów!).
- Symulator ZUS: Warsztat → eZUS/Płatnik → „Wyczyść wszystkie zgłoszenia (zacznij od nowa)”; lista płac miesiąca: „Wyczyść listę miesiąca”.

## Aktualizacja kursu / Mentora
- Nowa wersja ZIP: rozpakuj do NOWEGO folderu, skopiuj do niego `mentor_dane.json` ze starego. Id zadań i lekcji są stałe — postępy pasują.
- Import nowej wersji kursu plikiem (Ustawienia → Wgraj program z pliku) nie usuwa postępów; stary plik kursu możesz usunąć z `programy/`.

## Odinstalowanie
- Mentor nie instaluje się w systemie: usuń folder paczki. Katalog projektu i kopia `mentor_dane.json` zostają, jeśli chcesz.

## Typowe problemy techniczne
- „Windows chronił komputer” przy Mentor.exe → „Więcej informacji” → „Uruchom mimo to” (plik bez podpisu certyfikatem).
- Antywirus blokuje exe → dodaj folder do wyjątków albo uruchom ze źródeł (`python mentor.py`, Python 3.12 z python.org).
- Okno za duże/za małe → Ustawienia → Czcionki/skala.
- Polskie znaki w ścieżce lub spacje — obsługiwane; nie uruchamiaj z wnętrza ZIP.
- Brak uprawnień do zapisu w folderze (np. Program Files) → przenieś folder do Dokumentów.
"""
    kom = """# Komunikaty weryfikacji w Warsztacie — co znaczą i co zrobić

## eZUS / Płatnik — Dokument zgłoszeniowy (błędy blokują wysyłkę, ostrzeżenia nie)
- „Niepoprawny PESEL (błąd sumy kontrolnej lub długości)” → sprawdź 11 cyfr; nie „dopasowuj” ostatniej cyfry.
- „Brak daty (powstania/ustania obowiązku ubezpieczenia)” → wpisz datę RRRR-MM-DD (rozpoczęcia pracy / dzień po ustaniu).
- „Kod tytułu „…” nie istnieje (4 cyfry tytułu + emerytura/renta + niepełnosprawność)” → 6 znaków, np. 011000, 041100, 011022.
- „5. znak kodu: 0 — brak, 1 — emerytura, 2 — renta.” / „6. znak kodu: stopień niepełnosprawności 0–3.”
- „Osoba jest już zgłoszona z tym tytułem — najpierw ZWUA (lub ZUA w trybie korekty)” → nie duplikuj zgłoszenia.
- „Uczeń/student do 26 lat na zleceniu nie podlega ubezpieczeniom — nie zgłaszasz go wcale.”
- „Pracownik (01 10) podlega ubezpieczeniom społecznym — ZZA (tylko zdrowotne) jest błędne; użyj ZUA.”
- „Nie można wyrejestrować osoby, która nie jest zgłoszona.” / „Data wyrejestrowania musi być późniejsza niż data zgłoszenia (dzień PO ustaniu tytułu).”
- „Brak lub zły kod przyczyny wyrejestrowania (100 / 500 / 600).” / „Dla pracownika podaj tryb i podstawę prawną rozwiązania stosunku pracy.”
- „Członka rodziny zgłasza się do osoby, która sama jest zgłoszona (ZUA/ZZA).” / „Niepoprawny PESEL członka rodziny.”
- Ostrzeżenia: „Zgłoszenie po terminie 7 dni…”, „Data powstania obowiązku różni się od daty rozpoczęcia pracy…”, „Pracownik ma chorobowe obowiązkowe — pola „dobrowolne” nie zaznaczasz.”, „Wyrejestrowanie po terminie 7 dni.”, „Kod stopnia pokrewieństwa: 01 małżonek, 11 dziecko własne…”.

## eZUS / Płatnik — Rozliczenie DRA/RCA/RSA
- „Identyfikator 01 MM RRRR został już użyty — korekta wymaga kolejnego numeru (02, 03…).” / „Korekta (02+) bez wcześniejszego kompletu pierwotnego (01).”
- „RCA …: osoba nie figuruje w rejestrze ubezpieczonych (brak ZUA/ZZA).” / „RCA …: brak przyjętego zgłoszenia ZUA/ZZA.” / „RCA …: kod tytułu … nie istnieje.”
- „RCA …: składka emerytalna … ≠ 9,76% × podstawa” → RCA bierz z listy płac, nie ręcznie. / „RCA …: składka zdrowotna wyższa niż 9% podstawy.”
- Ostrzeżenie „RCA …: podstawa emerytalno-rentowa wyższa niż chorobowa…” → sprawdź 30-krotność.
- „RSA …: osoba nieznana.” / „RSA: kod przerwy … nie istnieje.” / „RSA: data „od” późniejsza niż „do”.”
- Ostrzeżenie „RSA …: świadczenie za okres z innego miesiąca — poprawne tylko, jeśli WYPŁACONO je w miesiącu raportu” / „RSA …: przerwa z innego miesiąca niż raport — przerwy bez świadczeń wykazuje się za miesiąc, w którym wystąpiły.” / „RSA 3xx: świadczenie bez kwoty (płatnik zasiłków wykazuje kwotę).”

## Lista płac — Tryb ćwiczenia („Sprawdź”)
- „✔ Zgadza się” — pełne kroki.
- „✘ Twoje netto … ≠ … Różnica równa się kwocie: …” — Mentor wskazuje krok, którego kwota odpowiada różnicy (np. PPK pracodawcy, zaliczka).
- „Policz jeszcze raz w kolejności: składki osobno → zdrowotna od (brutto − składki) → podstawa PIT zaokrąglona → zaliczka − PIT-2 → PPK.”
- Krok „FP/FGŚP nienależne: podstawa w przeliczeniu na miesiąc … poniżej minimalnego” — wpisz „Pensja wg umowy”, jeśli obniżka wynika z choroby/części miesiąca.

## Zasiłki
- „… — miesiąc WYŁĄCZONY” (< 50% dni), „UZUPEŁNIENIE: …”, „Podniesienie do minimalnej podstawy …”, „Stawka dzienna × …% = … (zaokrąglona do grosza)”.
- Pula: „wynagrodzenie chorobowe … dni (pula 33: wykorzystano …), zasiłek … dni”; „UWAGA: okres zasiłkowy 182 dni przekroczony” → świadczenie rehabilitacyjne.
"""
    bl = ["# Typowe błędy i naprawa — zebrane ze wszystkich lekcji", ""]
    for l in d["lekcje"]:
        if not l.get("typowe_bledy"):
            continue
        bl.append(f"## {l['nazwa']} (tydzień {l['tydzien']})")
        for b in l["typowe_bledy"]:
            bl += [f"- ✘ **{b['komunikat']}**", f"  - przyczyna: {b['przyczyna']}", f"  - jak sprawdzić: {b['diagnoza']}", f"  - poprawka: {b['poprawka']}"]
        bl.append("")
    _w("pomoc/FAQ.md", faq)
    _w("pomoc/ODZYSKIWANIE.md", odz)
    _w("pomoc/KOMUNIKATY_WARSZTATU.md", kom)
    _w("pomoc/BLEDY.md", "\n".join(bl))


def _projekt_przyklad(d):
    firma = ["# AGRO-MLEKO sp. z o.o. — karta firmy ćwiczeniowej (dane fikcyjne)", "", d.get("firma", ""), "", "## Regulaminy i zasady"]
    firma += [f"- {r['nazwa'] if isinstance(r, dict) else r}" for r in d.get("firma_regulaminy", [])]
    firma += ["", "## Osoby", "| Id | Imię i nazwisko | Stanowisko | Umowa | Od | Etat | Zasadnicze | PPK | KUP | PIT-2 | Kod ZUS |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for o in d.get("firma_osoby", []):
        firma.append(f"| {o['id']} | {o['imie']} {o['nazwisko']} | {o['stanowisko']} | {o['umowa']} | {o['od']} | {o['etat']} | {o['zasadnicze']} | {'tak' if o.get('ppk') else 'nie'} | {o['kup']} | {o['pit2']} | {o.get('kod', '—') or '—'} |")
    firma += ["", "## Parametry 2026", "| Parametr | Wartość |", "|---|---|"] + [f"| {k} | {v} |" for k, v in d.get("parametry", {}).items()]
    _w("projekty/kadry-praktyka-przyklad/FIRMA.md", "\n".join(firma) + "\n")
    _w("projekty/kadry-praktyka-przyklad/dziennik.md", "# Dziennik nauki — kadry i płace\n\nDzień 1: utworzyłem katalog i FIRMA.md; nie wiem jeszcze, co to PEL.\n")
    _w("projekty/README.md", "# projekty/\n\nPrzykładowy katalog projektu (`kadry-praktyka-przyklad/`) — tak wygląda Twój folder po tygodniu 0. Sandboxem kursu jest zakładka **Warsztat** w Mentorze (symulatory eZUS/Płatnika i e-Urzędu, kalkulatory) — nie wymaga lokalnego serwera ani bazy.\n")


def _instalatory():
    _w("instalatory/README.md", """# instalatory/ — nic nie trzeba instalować

Kurs działa w całości w Mentorze (Mentor.exe, bez instalacji, bez uprawnień administratora, bez internetu). Nie ma zależności do pobrania.

Opcjonalnie — tylko dla osób, które chcą uruchamiać Mentora ze źródeł (`python mentor.py`) zamiast Mentor.exe:
- Python 3.12.x (64-bit), oficjalne źródło: https://www.python.org/downloads/windows/ — instalator „Windows installer (64-bit)”; przy instalacji zaznacz „Add python.exe to PATH”. Licencja: PSF (wolne oprogramowanie). Tkinter jest w standardowej instalacji. Suma kontrolna instalatora: na stronie python.org przy danej wersji (porównaj po pobraniu).
- Żadne pakiety pip nie są potrzebne (Mentor używa tylko biblioteki standardowej).

Nie dołączamy instalatora Pythona do ZIP, bo nie jest potrzebny do kursu; wskazujemy dokładne oficjalne źródło i wersję — nie jest to „instalacja offline”.
""")


def zbuduj_materialy():
    d = json.loads(ZRODLO.read_text(encoding="utf-8"))
    if CEL.exists():
        shutil.rmtree(CEL)
    CEL.mkdir(parents=True)
    lekcje = d["lekcje"]
    n = len(lekcje)
    licz = {"lekcje": 0, "cwiczenia": 0, "rozwiazania": 0, "przyklady": 0}
    for poz, l in enumerate(lekcje, 1):
        t = f"tydzien_{l['tydzien']:02d}"
        _w(f"lekcje/{t}/{l['id']}.md", _md_lekcja(l, poz, n)); licz["lekcje"] += 1
        _w(f"przyklady/{t}/{l['id']}.md", _md_przyklad(l)); licz["przyklady"] += 1
        for i, cw in enumerate(l.get("cwiczenia", []), 1):
            assert cw["plik"] == f"cwiczenia/{t}/{l['id']}_{i}.md", cw["plik"]
            _w(cw["plik"], _md_cwiczenie(l, i, cw)); licz["cwiczenia"] += 1
            _w(cw["rozwiazanie_plik"], _md_rozwiazanie(l, i, cw)); licz["rozwiazania"] += 1
    for sc, tresc in PRZYKLADY.items():
        _w(sc, tresc)
    _pomoc(d)
    _projekt_przyklad(d)
    _instalatory()
    _w("testy/sprawdz_kurs.py", SPRAWDZ_KURS_PY)
    _w("testy/SPRAWDZ_KURS.bat", SPRAWDZ_KURS_BAT)
    _w("testy/README.md", "# testy/\n\n`SPRAWDZ_KURS.bat` — sprawdza strukturę paczki (dwuklik). `sprawdz_kurs.py` — pełne sprawdzenie JSON i sum kontrolnych (wymaga Pythona; opcjonalne).\nTesty merytoryczne (czy liczysz poprawnie) są w Mentorze: Tryb ćwiczenia w Liście płac, testy lekcji, quizy — i w plikach `rozwiazania/`.\n")
    _w("SPRAWDZ_SRODOWISKO.bat", SPRAWDZ_BAT)
    _w("INSTALACJA.bat", INSTALACJA_BAT)
    _w("URUCHOM_KURS.bat", URUCHOM_BAT)
    start = START_TUTAJ.format(wersja=d["wersja"], stan_prawny=d["stan_prawny"], poziom=d["poziom"], system=d["system"],
                               wymagania="; ".join(d["wymagania_wstepne"]), umiejetnosci="\n".join(f"- {u}" for u in d["umiejetnosci_koncowe"]))
    _w("START_TUTAJ.md", start)
    shutil.copy(ZRODLO, CEL / "kurs_mentor.json")
    shutil.copy(TU / "RAPORT_CHECKLISTA.md", CEL / "RAPORT_CHECKLISTA.md")
    # manifest z sumami kontrolnymi (bez samego manifestu)
    pliki = {}
    for p in sorted(CEL.rglob("*")):
        if p.is_file() and p.name != "manifest.json":
            pliki[p.relative_to(CEL).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    manifest = {"kurs": d["id"], "nazwa": d["nazwa"], "wersja": d["wersja"], "format": d["format"], "stan_prawny": d["stan_prawny"],
                "mentor_min": "2.5.0", "liczby": {"tygodnie": len(d["tygodnie"]), "lekcje": n, "zadania": sum(len(w["zadania"]) for w in d["tygodnie"]),
                                                  "cwiczenia": licz["cwiczenia"], "quizy": sum(len(v) for v in d["quizy"].values()), "diagnoza": len(d["diagnoza"])},
                "struktura": ["START_TUTAJ.md", "SPRAWDZ_SRODOWISKO.bat", "INSTALACJA.bat", "URUCHOM_KURS.bat", "kurs_mentor.json", "manifest.json", "instalatory/", "lekcje/", "przyklady/", "cwiczenia/", "rozwiazania/", "projekty/", "testy/", "pomoc/"],
                "licencja": "materiały kursu — do użytku z Mentorem; dane fikcyjne; brak plików firm trzecich, kluczy i danych prywatnych",
                "pliki": pliki}
    _w("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=1))
    print(f"Materiały: {CEL} — lekcje {licz['lekcje']}, przykłady {licz['przyklady']}, ćwiczenia {licz['cwiczenia']}, rozwiązania {licz['rozwiazania']}, plików w manifeście {len(pliki)}")


if __name__ == "__main__":
    zbuduj_materialy()
