# Raport zgodności ze STANDARDEM TWORZENIA KURSÓW v1.0 — „Vibe coding od podstaw”

Wersja kursu: 1.0 · Mentor 2.9.0 · data raportu: 20.11.2026 · autor raportu: zespół kursu (Claude) — **raport uczciwy: status końcowy poniżej**

## A. Testy jakości (STANDARD §10)

| Test | Wynik | Jak sprawdzono |
|---|---|---|
| Import | ✅ TAK | `program.waliduj` → 0 błędów; dymny test GUI (Xvfb): wszystkie widoki, 16 tygodni planu, 48 lekcji, 96 paneli „Twoje odpowiedzi” wypełnionych kluczem → komplet, 10 kart przeglądu → komplet; CI waliduje JSON przy każdym buildzie |
| Świeży komputer / środowisko | ⚠️ CZĘŚCIOWO | Mentor.exe budowany i uruchamiany na czystym `windows-latest` (CI). Instalacja środowiska kursu (.venv z locka) testowana w CI. Polecenia instalacji Claude Code i Codex przepisane z oficjalnej dokumentacji (dostęp 19–20.11.2026), format `claude --version` sprawdzony na wersji 2.1.329 — **instalacji na fizycznym Windows w tej sesji nie wykonano** |
| Offline | ⚠️ CZĘŚCIOWO (z natury kursu) | Lekcje, ćwiczenia, karty, testy zadań i Asystent offline działają bez sieci. Instalacja środowiska, agentów, GitHub i Pages wymagają internetu — opisane wprost w lekcjach |
| Przejście ucznia (pierwsze 2 zadania) | ⚠️ CZĘŚCIOWO | Autor w roli ucznia: zadania v0z1–v0z2 i v1z4 (pierwszy kod pod niezależny test) przez Mentora — `test_vibe.py::test_mentor_end_to_end`. **Nie wykonano przez osobę niebędącą autorem** |
| Ćwiczenia | ✅ TAK | 96 ćwiczeń (48 × prowadzone + samodzielne), każde z wynikiem, 3 podpowiedziami, rozwiązaniem i polami sprawdzanymi automatycznie; klucz zgodny z treścią (`zbuduj.py`), typowe pomyłki dają podpowiedź (test); kod z lekcji uruchamiany w testach (wyjście = to, co w kluczu) |
| Zadania | ✅ TAK | 73 zadania; 39 sprawdzanych niezależnymi testami z paczki (SHA-256) — każdy test przechodzi na rozwiązaniu wzorcowym i NIE przechodzi na pustym katalogu, 5 plikach startowych z błędami i 9 zapisach agenta z celowym błędem (`sprawdz_weryfikatory.py`, test w CI) |
| Błędy | ✅ TAK | Każda lekcja: „Typowe błędy i naprawa” (komunikat, przyczyna, diagnoza, poprawka); komunikaty weryfikatorów po polsku z danymi → oczekiwane → otrzymane; `pomoc/FAQ.md`, `pomoc/BLEDY.md`, `pomoc/ODZYSKIWANIE.md` |
| Dostępność | ✅ TAK | Polskie instrukcje, kod w ramkach, motywy i skalowanie Mentora, wyniki ✔/✘ z tekstem |
| Aktualizacja | ✅ TAK | Stabilne id lekcji i zadań; kalendarz aktualizacji (15 terminów: ceny planów, wersje narzędzi, AI Act, limit działalności nierejestrowanej, OWASP); daty dostępu przy 108 źródłach |
| Licencje i bezpieczeństwo | ✅ TAK | Wyłącznie własne pliki kursu; dane, klucze i adresy w przykładach fikcyjne; test paczki szuka prawdziwych sekretów i danych prywatnych; manifest SHA-256 + INTEGRITY.json |

## B. Checklista publikacyjna (STANDARD §11)

| # | Kryterium | Status | Dowód |
|---|---|---|---|
| 1 | Uczeń wie, co będzie umiał i ile czasu to zajmie | ✅ TAK | START_TUTAJ.md, lekcja wprowadzająca; czas liczony z treści (≈ 117 h, tydzień ≤ 9 h — `zbuduj.py` odrzuca przekroczenie) |
| 2 | Każda lekcja: wyjaśnienie, działający przykład, omówienie krok po kroku | ✅ TAK | 48/48 (asercje w `wspolne.L`) |
| 3 | Zadania nie wymagają rzeczy niepokazanych | ✅ TAK | kolejność: pliki → terminal → czytanie kodu → specyfikacja → agent → Git → testy → web → dane → bezpieczeństwo → zawód; quizy nie pytają o lekcje z przyszłości (asercja) |
| 4 | Pliki startowe, dane, przykłady, rozwiązania w paczce | ✅ TAK | `przyklady/` (7 plików startowych, 9 zapisów pracy agenta), `dane/`, `rozwiazania/` (96 + kod wzorcowy), `pomoc/` (4 materiały do zadań) |
| 5 | Zależności legalne / z oficjalnego źródła | ✅ TAK | pytest, flask, requests z locka z SHA-256; Claude Code, Codex, Git — oficjalne polecenia instalacji |
| 6 | Instalacja według instrukcji, także przy typowym błędzie | ⚠️ CZĘŚCIOWO | lekcje instalacji z błędami z dokumentacji (PATH, TLS, PS vs CMD, ExecutionPolicy); **nieprzetestowane na fizycznym Windows przez osobę testującą** |
| 7 | Oczekiwany wynik, sprawdzenie, stopniowane podpowiedzi | ✅ TAK | ćwiczenia i zadania (kroki, „Gotowe, gdy”, problemy, podpowiedź w pasku ćwiczenia) |
| 8 | Postępy = wykonana praca | ✅ TAK | zaliczenie automatyczne tylko po zielonych testach z paczki; zadania opisowe — samoocena z kryteriami |
| 9 | Przykłady działają na deklarowanym systemie | ⚠️ CZĘŚCIOWO | weryfikatory i wzorce testowane w CI na Windows (`test_vibe.py`); **zadania nie były przeklikane w exe na Windows przez osobę testującą** |
| 10 | JSON przechodzi walidację i import | ✅ TAK | `program.waliduj`, CI |
| 11 | ZIP bez sekretów i pirackich plików | ✅ TAK | patrz A |
| 12 | Osoba spoza zespołu zaczyna bez dopytywania | ❌ NIE (jeszcze) | wymagany test jednej osoby na Windows: START_TUTAJ.md → tydzień 0 → v1z4 |

## C. Status

**GOTOWY DO TESTU Z UCZNIEM** — 9 kryteriów TAK, 2 CZĘŚCIOWO (6, 9), 1 NIE (12). Brakuje testu, którego nie da się wykonać bez drugiej osoby i fizycznego Windows (instalacja agenta, pierwsze zadania w exe).
