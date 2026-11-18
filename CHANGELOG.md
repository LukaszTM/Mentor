# Zmiany w Mentorze

## 2.7.3 — kurs „Kadry i płace” 2.2: audyt faktów (stan prawny 18.11.2026) i materiały zagraniczne w tłumaczeniu

- **Poprawki merytoryczne po audycie ze sprawdzonymi źródłami** (Dziennik Ustaw/ELI, ISAP, legislacja.gov.pl, Sejm, ZUS, GUS, NBP, MF, PIP, Zielona Linia):
  reforma PIP (ustawa z 11.03.2026, Dz.U. 2026 poz. 473, od 8.07.2026) — grzywny 2 000–60 000 zł (recydywa 3 000–90 000), mandat do 10 000 zł, decyzja o ustaleniu
  stosunku pracy, abolicja do 8.07.2027, kontrole zdalne, interpretacje GIP, odwołanie od nakazu 7 dni; mobbing wg uchwalonej ustawy z 19.06.2026 (Dz.U. 2026 poz. 1046) —
  zadośćuczynienie ≥ 6× minimalne albo odszkodowanie bez wymogu rozstroju zdrowia, regres wobec sprawcy, brak przepisu zwalniającego pracodawcę, odrębny regulamin
  od 10 pracowników (art. 94³ᵃ) zamiast „obwieszczenia”, dyskryminacja 1×/3× minimalne, art. 18³ᶠ–18³ᵍ, KPC; jawność w rekrutacji — bez osobnego wykroczenia
  (kary dopiero w projekcie UC127; status projektu 18.11.2026); obywatele Ukrainy po wygaszeniu specustawy (Dz.U. 2026 poz. 203) — powiadomienie PUP w 7 dni, ochrona
  czasowa do 4.03.2027; odsetki 9,25% / 10,50% i przeliczone kwoty w ćwiczeniach; wymiar grudnia 2026 = 160 h; FP 1,00% + FS 1,45%; PIT 2027 (ustawa uchwalona,
  decyzja prezydenta do 27.11.2026); nowe przepisy: układy zbiorowe (Dz.U. 2025 poz. 1661), upały (Dz.U. 2026 poz. 927, od 11.01.2027), praca platformowa (UC160),
  rozporządzenie 883/2004, delegowanie; tabela zmian 2025–2027 w lekcji „Źródła prawa”, sekcja „Zapowiedzi na 2027” w lekcji „Wskaźniki”.
- **Dwie nowe lekcje z materiałów zagranicznych (tłumaczenie + zestawienie z KP)**: „Praktyki HR z zagranicy (ACAS, CIPD) po polsku” (tydzień 2) — słowniczek EN–PL,
  onboarding wg CIPD z obowiązkami KP, rozmowa okresowa wg ACAS, skarga pracownicza i postępowanie dyscyplinarne wg Kodeksu ACAS 2015 zestawione z art. 94³ᵃ i 108–113 KP,
  exit interview z RODO, lista rozwiązań, których nie wolno przenieść; „Prawo UE i standardy międzynarodowe w kadrach” (tydzień 11) — koordynacja ubezpieczeń
  (883/2004: A1, US-3/US-4/US-36, telepraca transgraniczna), delegowanie (96/71, 2018/957) z dopłatą do płacy państwa przyjmującego i przykładem liczbowym (Niemcy),
  dyrektywy wdrożone w KP, wyroki TSUE (CCOO, Schultz-Hoff, Max-Planck, Tyco, Matzak, C-19/23), konwencje MOP, EU-OSHA „Heat at work” + polskie progi 28/35°C.
  48 lekcji, 96 ćwiczeń, 62 przepisy, 134,8 h; każdy tydzień ≤ 9 h.
- **Źródła w lekcjach**: pole `zrodla` lekcji (`[tytuł, adres, data dostępu]`) — Mentor pokazuje kartę „Źródła — sprawdzone materiały” pod lekcją z linkiem
  „otwórz ↗”; pole `zrodla_kursu` programu — karta „Źródła programu” w Ściądze; paczka materiałów: sekcja „Źródła” w pliku każdej lekcji i `ZRODLA.md`
  (format opisany w `programy/FORMAT.md`). Raport kursu: sekcja F w `RAPORT_CHECKLISTA.md`.

## 2.7.2 — paczki z niezależnymi testami, lokalne API kursu, rubryka oceny własnej (na podstawie paczki AI Developer Lab 1.5)

- **`sprawdzenie.rodzaj = "test_zewnetrzny"`**: niezależne testy zachowania z paczki kursu (np. `WERYFIKATORY/test_zachowania.py`, wybór testu przez `wybor` = `pytest -k`).
  Plik testu jest weryfikowany sumą SHA-256 (z definicji zadania, manifestu lub `INTEGRITY.json` paczki — bez sumy nie jest uruchamiany), kopiowany do katalogu
  tymczasowego tylko do odczytu i uruchamiany pytestem interpreterem kursu z limitem czasu; katalog roboczy ucznia trafia do testu przez `MENTOR_WORKSPACE`.
  Zaliczenie wyłącznie po zielonych testach; czytelne komunikaty: brak pliku, brak funkcji z kontraktu, liczba czerwonych przypadków, zmieniony plik testu.
- **Lokalny serwer API kursu** (`srodowisko.api_lokalne` / manifest `local_api`): karta w zakładce Środowisko — Uruchom (po potwierdzeniu; Mentor pokazuje skrypt
  i sumę SHA-256), Zatrzymaj, Sprawdź API (prawdziwe GET /health), Otwórz w przeglądarce. Skrypt z paczki uruchamiany interpreterem kursu, tylko 127.0.0.1,
  nigdy automatycznie; zatrzymywany przy zamknięciu Mentora.
- **Zmienne dla kodu ucznia** przy każdym uruchomieniu i w terminalu z Mentora: `MENTOR_WORKSPACE`, `MENTOR_COURSE_ROOT`, `MENTOR_SANDBOX_HTML`, `MENTOR_API_URL`
  — kurs trzymany poza PRACA (Dokumenty\Mentor\<kurs>\PRACA) może wskazać swoje materiały bez zgadywania ścieżek.
- **Rubryka oceny własnej z dowodami**: zadania bez niezależnego testu („Plik istnieje — wymaga sprawdzenia”) i zadania bez pliku `.py` dostają dialog z kryteriami
  (pole `rubryka` albo zdania z „Gotowe, gdy”) i polem dowodów; odhaczenie dopiero po potwierdzeniu wszystkich kryteriów i wpisaniu dowodu; status „ocena własna”
  jest odróżniony od „zaliczone automatycznie”.
- Manifest: `requirements.python_packages`, `local_api`, `sandbox_html`, `external_tests`; pole `srodowisko` programu uzupełnia manifest; priorytet pakietów:
  manifest → lock paczki → `srodowisko` programu → requirements.
- Testy: `testy/test_paczka_zaawansowana.py` (pakiety z manifestu, weryfikacja sum, test_zewnetrzny: zaliczenie/porażka/brak funkcji/zmieniony test/zły wybór,
  start/stop/health lokalnego API, odrzucenie skryptu ze złą sumą, rubryka).
- **Paczka AI Developer Lab 1.5 → 1.5.1** (dostarczona osobno): 12 ćwiczeń z kontraktem używa `test_zewnetrzny`, zadeklarowane lokalne API i sandbox HTML, ścieżki
  do sandboxu przez `MENTOR_SANDBOX_HTML` (przykłady, szablony, lekcje, rozwiązania), teksty dopasowane do zakładek Mentora („Plan nauki”, karta API), manifest 1.5.1,
  `INTEGRITY.json` przeliczony. Zweryfikowano: import, środowisko, 12 testów zielonych dla rozwiązań referencyjnych z paczki i czerwonych dla szablonów, API start/health/POST/stop.

## 2.7.1 — kurs Python → Junior QA dostosowany do środowiska w Mentorze

- **Tydzień 0 przepisany**: zadanie 1 to „Środowisko kursu w Mentorze + Git” (Sprawdź ponownie → Zainstaluj brakujące → plan → zgoda → testy; Git z git-scm.com;
  PyCharm i Claude Code opcjonalne), zadanie 2 — katalog roboczy PRACA i CLAUDE.md przyciskami w Mój projekt, zadanie 3 — hello.py w całości przyciskami
  (Utwórz plik ćwiczenia → ▶ Uruchom → ✔ Sprawdź wynik → celowe zepsucie i czytanie błędu po polsku; terminal tylko jako wariant), zadania 4–5 — terminal z Mentora.
  Lekcja „Narzędzia” przepisana (co robi Mentor, co robisz sam, czym jest osobne środowisko kursu, PATH), lekcje „Start” i „Terminal” uzupełnione, quiz, checklista,
  cel etapu 0 i cele lekcji zaktualizowane.
- **Każde zadanie z ćwiczeniem** dostaje ostatni krok „W Mentorze (bez terminala)” generowany z definicji sprawdzenia (jakie dane podaje test, co musi być w wyjściu / pytest),
  a zadania tygodni 1–5 — przykłady w innym kontekście i podpowiedzi. Nowa ściąga „Mentor — środowisko i ćwiczenia”.
- **Poprawki merytoryczne**: „Krowa je trawę” ma 14 znaków i 5 samogłosek (kurs podawał 15 i 6 — test zadania by nie przechodził); kolejność danych w kalkulatorze
  (liczba, działanie, liczba) zapisana wprost; lekcja venv odnosi się do środowiska kursu Mentora; zadanie venv tłumaczy, że to drugie, własne środowisko.
- **Sprawdzanie ćwiczeń**: plik zawierający tylko szablon (komentarze) nigdy nie zalicza; `uruchom_bez_bledu` wymaga co najmniej jednej linii wyjścia;
  program, który pyta o więcej danych niż test (EOFError), dostaje „wymaga sprawdzenia ręcznego” zamiast „błąd”; wszystkie sprawdzenia zweryfikowane na wzorcowych
  rozwiązaniach napisanych według kroków zadania (zaliczają) i na samych szablonach (nie zaliczają).
- **Mentor**: Mój projekt i przewodnik „Jak zacząć” mają „Utwórz katalog roboczy kursu”; „Otwórz terminal tutaj” otwiera terminal w katalogu roboczym z Pythonem kursu
  na początku PATH; teksty Panelu/przewodnika mówią o katalogu roboczym zamiast o konkretnej nazwie folderu.

## 2.7.0 — środowiska kursów, import paczek ZIP, ćwiczenia w Mentorze

Cel (specyfikacja „instalacja środowisk”): osoba na czystym Windows uruchamia `Mentor.exe`, importuje kurs, przygotowuje wymagane
środowisko i zaczyna ćwiczyć — **bez terminala, bez plików .bat, bez szukania instalatorów i bez uprawnień administratora**.

### Etap 1 — MVP
- **Katalog danych użytkownika**: `%LOCALAPPDATA%\Mentor\` (`mentor_dane.json`, `programy/`, `kursy/`, `srodowiska/`, `python/`, `pobrane/`, `logi/`).
  Katalog EXE może być tylko do odczytu; Mentor nigdy nie zapisuje do `sys._MEIPASS`. `portable.txt` obok EXE = tryb przenośny; `MENTOR_DANE` = własny katalog.
- **Migracja** starych danych (`mentor_dane.json` i `programy/` obok EXE) przy pierwszym uruchomieniu — z kopią `mentor_dane.json.kopia-<data>`,
  oryginały zostają, raport na Panelu.
- **Import kursu ZIP** (Ustawienia → „Importuj kurs ZIP…”; dotychczasowy import JSON zostaje jako „Importuj JSON…”):
  podgląd przed importem (nazwa, wersja, autor, lekcje, zadania, wymagania, rozmiar, źródło, SHA-256, internet, uprawnienia, lista skryptów),
  bezpieczne rozpakowanie (odrzucane `..`, ścieżki bezwzględne, dowiązania; limity liczby plików, rozmiaru, bomby kompresji; katalog tymczasowy + atomowe podmienienie),
  paczki z `mentor-manifest.json` (`mentor-course/1`) i **stare paczki v1.1** (JSON w korzeniu + `requirements.txt` + `.bat/.ps1` — **skrypty nigdy nie są uruchamiane**),
  aktualizacja wersji tylko po potwierdzeniu, z kopią poprzedniej wersji w `kursy/_kopie/`; postępy (stabilne id zadań/lekcji) i katalog PRACA zostają.
- **Zakładka Środowisko**: statusy z **realnych uruchomień** (`python --version` przez probe JSON, `.venv`, import pytest/requests/selenium/flask w środowisku kursu,
  `git --version`, `claude --version`, Edge/Chrome z wersją, materiały kursu): Gotowe / Brak / Nieprawidłowa wersja / Błąd / Opcjonalne / Sprawdzanie / Nie sprawdzono / Pominięto.
  Rozróżnienie Pythona systemowego, zarządzanego przez Mentora i środowiska kursu; Python zapakowany w `Mentor.exe` nigdy nie jest środowiskiem ćwiczeń.
- **Zainstaluj brakujące**: najpierw lista kroków (źródło, rozmiar, internet, uprawnienia) → zgoda → wątek roboczy + kolejka + `after` (GUI nie zamarza):
  osobne `.venv` kursu w `srodowiska/<id>/`, `pip install --require-hashes --only-binary=:all:` z locka z sumami SHA-256 (`programy/zaleznosci/requirements.lock`:
  pytest 9.2, requests 2.34, selenium 4.52, flask 3.1 + zależności; Windows i Linux, Python 3.11–3.13). Tylko składniki zadeklarowane w kursie; żadnych komend z JSON/ZIP.
  Pasek postępu, log, przyciski Anuluj / Ponów / Pokaż szczegóły; obsługa: brak internetu (bez zawieszania), brak miejsca, brak uprawnień, limit czasu, uszkodzone pobranie
  (zła suma → plik usunięty), brak pip, konflikt wersji (czytelny komunikat). „Gotowe” dopiero po testach końcowych.
- **Sprawdź działanie** (testy końcowe w środowisku kursu, z limitami czasu i sprzątaniem): interpreter, importy, przykładowy pytest, lokalny serwer API + prawdziwe
  żądanie HTTP, Selenium otwierające dołączoną stronę HTML w prawdziwej przeglądarce (raportowane osobno; informacja o pobraniu sterownika przez Selenium Manager).
  Wyniki z datą i wersjami w `stan.json`; zmiana kursu lub locka unieważnia wyniki.
- Przewodnik „Jak zacząć” (krok 1a), Panel (plakietka stanu + „Pierwsze kroki”) i Mój projekt pokazują stan środowiska; przyciski Napraw środowisko,
  Sprawdź ponownie, Otwórz katalog kursu, Usuń środowisko, Usuń kurs (domyślnie zostawia PRACA i postępy).

### Etap 2
- **Python bez wymagania instalacji**: gdy w systemie nie ma zgodnego Pythona, Mentor pobiera oficjalny runtime
  python-build-standalone 3.12.12 (x86_64 Windows, `install_only`, 45,8 MB) z przypiętą sumą SHA-256, rozpakowuje do `python/` w katalogu danych
  (bez winget, bez administratora) i tworzy z niego `.venv` kursu. Alternatywnie link do python.org.
- Przeglądarka (Edge/Chrome) wykrywana realnie; wymagana dopiero od tygodnia, w którym kurs jej używa (`przegladarka_od_tygodnia`).
- Logi `logi/srodowisko_<id>.log`, naprawa środowiska (usunięcie i odbudowa), tryb offline: lekcje i teoria działają, instalacja mówi wprost o braku sieci.

### Etap 3
- **Ćwiczenia w Mentorze** (pasek pod zadaniem w kursach z Pythonem): Otwórz przykład (kod w innym kontekście niż zadanie), Utwórz plik ćwiczenia
  (szablon w katalogu PRACA; istniejącego pliku nie nadpisuje bez pytania, robi kopię), Otwórz w edytorze (VS Code / PyCharm / Notatnik — nigdy `os.startfile` na `.py`),
  Uruchom (tylko po kliknięciu; interpreter kursu, limit czasu, Anuluj, stdout/stderr, traceback po polsku, dane dla `input()`),
  Sprawdź wynik (`uruchom_bez_bledu` / `wyjscie_zawiera` / `pytest` → zalicza automatycznie; bez testu → „Plik istnieje — wymaga sprawdzenia”, nie „Zaliczone”), Pokaż podpowiedź.
- Katalog `PRACA` tworzony automatycznie (`Dokumenty\Mentor\<id>\PRACA`) i podpinany jako „Mój projekt”; katalog projektu jest teraz zapamiętywany **per kurs**.
- Kurs **Python → Junior QA 2.1**: pole `srodowisko` (Python ≥3.11,<3.14; pytest, requests, selenium, flask; Git i Claude Code opcjonalne; Edge od tygodnia 8)
  i `cwiczenie` dla 37 zadań z plikiem `.py` (szablony, przykłady, dane testowe, sprawdzenia — w tym pytest dla zadań z tygodni 7, 8, 10, 11).
- Asystent (`/uruchom`) uruchamia pliki interpreterem kursu zamiast Pythonem Mentora (w EXE `sys.executable` to `Mentor.exe`).

### Narzędzia i jakość
- Nowe moduły: `paczki.py`, `srodowisko.py`, `widok_srodowisko.py`, `cwiczenia.py`, `srodowisko_testy/`, `programy/zaleznosci/requirements.lock`.
- Testy `testy/` (pytest, 59 testów): zip-slip i ścieżki bezwzględne, dowiązania, limity, bomba kompresji, paczka v1.1 bez uruchamiania skryptów, manifest, sprzeczne metadane,
  aktualizacja z kopią i stabilnymi id, walidacja locka, realny `.venv` + pip z hashami, testy końcowe, anulowanie, uruchamianie plików ucznia, sprawdzenia ćwiczeń,
  GUI (nowe widoki, import przez Ustawienia, diagnoza bez blokowania), na Windows CI także pobranie runtime’u Pythona z weryfikacją SHA-256 i Selenium z Edge.
- CI: krok pytest na `windows-latest` przed PyInstallerem; `mentor.spec` dołącza `srodowisko_testy/` i `programy/zaleznosci/`.
- Dokumentacja: README (gdzie są dane, import ZIP, Środowisko, ćwiczenia), `programy/FORMAT.md` (`srodowisko`, `cwiczenie`, manifest).
- Zachowane: wszystkie dotychczasowe moduły, funkcje, identyfikatory kursów, format JSON, dane użytkowników i pipeline PyInstaller.

## 2.6.0 — kurs kadrowy 2.1
- Realny harmonogram 16 tygodni (`plan_tygodni.py`), etykiety czasu liczone z treści, wyjaśnienia „jedna reguła — jedno zdanie” z tabelami,
  lekcja o podróżach służbowych i dietach + kalkulator diet w Warsztacie.
