# Zmiany w Mentorze

## 2.9.0 — nowy kurs „Vibe coding od podstaw” (16 tygodni, Claude Code + Codex) i konfigurowalny Warsztat

- **Kurs „Vibe coding od podstaw” 1.0** (`programy/vibe-coding.json`, źródła `programy/zrodla/vibe_coding/`): dla osoby zaczynającej od zera — pliki, terminal,
  czytanie kodu i traceback, rozmowa z AI i specyfikacja (tydz. 0–3); Claude Code i Codex w Windows, tryby uprawnień, AGENTS.md/CLAUDE.md, małe kroki, Git i GitHub,
  przegląd zmian agenta, kontekst i koszty (4–7); testy jako umowa, debugowanie, refaktoryzacja, HTML/CSS/JS z GitHub Pages, CSV/JSON, Flask, SQLite, API z kluczami,
  automatyzacje (8–11); bezpieczeństwo kodu i agenta (XSS, SQL injection, sekrety, slopsquatting, prompt injection, reguły deny), prawo (prawa do kodu z AI, licencje,
  RODO, AI Act po Digital Omnibus), pull requesty z recenzją AI, README, CI w GitHub Actions, wymagania klienta i wycena, portfolio, rozmowa rekrutacyjna i projekt końcowy
  — mini system rezerwacji wydany jako 1.0.0 (12–15). 48 lekcji według standardu, 96 ćwiczeń — każde z polami „Twoje odpowiedzi”, 73 zadania (≈ 117 h, każdy tydzień ≤ 9 h),
  80 pytań quizowych, diagnoza, 10 kart przeglądu w Warsztacie, kalendarz aktualizacji (ceny planów, wersje narzędzi, terminy AI Act).
- **Niezależne testy zadań**: 39 zadań z kodem i plikami sprawdzają weryfikatory z paczki (`WERYFIKATORY/test_t00…t15.py`, suma SHA-256 w kursie i `INTEGRITY.json`):
  zachowanie funkcji, testy ucznia uruchamiane na mutantach, struktura HTML i JS (z Node.js — także wyniki), API Flask, SQL injection, historia Gita, tag wydania.
  `programy/zrodla/vibe_coding/sprawdz_weryfikatory.py` pilnuje, że każdy test przechodzi na rozwiązaniu wzorcowym i nie przechodzi na pustym katalogu, plikach startowych
  z błędami i zapisach pracy agenta z celowym błędem (ścieżka bez płatnego konta).
- **Fakty sprawdzone u źródeł (19–20.11.2026)**: dokumentacja Claude Code (instalacja, tryby, uprawnienia, pamięć, checkpointy, koszty), Codex (instalacja, tryby, piaskownica,
  AGENTS.md, polecenia), cenniki, raporty Veracode 2025, METR 2025, Stack Overflow 2025, badanie slopsquatting (USENIX 2025), OWASP Top 10 dla LLM 2025, PARP, AI Act — 108 źródeł z datą dostępu.
- **Warsztat konfigurowalny przez program** (pole `warsztat_opis`): nazwy narzędzi, nagłówek i opis formularzy, tekst na ekranie startowym — kurs kadrowy bez zmian.
- **Mój projekt**: wskazówka o repozytorium Git wskazuje lekcję o Gicie bieżącego kursu (zamiast stałego tekstu kursu Python).
- Testy: `testy/test_vibe.py` (budowanie ze źródeł, klucze odpowiedzi, kod z lekcji, sumy, weryfikatory na wzorcach i błędach, paczka, Mentor end-to-end).

## 2.8.1 — kurs „Kadry i płace” 3.1: drugi przegląd przed wydaniem — klucze zgodne z rozwiązaniami, PIT-11 według urzędowego wzoru

Przegląd wszystkich 87 ćwiczeń z kluczem (treść ↔ wynik ↔ rozwiązanie ↔ klucz), 10 formularzy i 225 pytań testowych; numeracja PIT-11 porównana z urzędowym wzorem PIT-11(29).

- **Błędny klucz**: „Rozliczenia miesięczne” ćw. 1 — klucz mówił o 8 raportach RCA, a rozwiązanie o 10 (8 pracowników + 2 zleceniobiorców); teraz 10, z podpowiedziami dla 8 i 12.
- **Symulator PIT-11** (Warsztat → e-Urząd: PIT): u podatnika do 26 lat składki od przychodów zwolnionych trafiały do poz. 95 — według wzoru PIT-11(29) to poz. 97
  (podatnik ich nie odlicza), a składki od przychodów z wiersza 2 — poz. 96; poz. 28 pokazuje numer kwadratu (1 albo 3); nota o zasiłku macierzyńskim (wiersz 12).
  `kadry.skladki_do_pit11()` dzieli składki tak samo jak lista płac.
- **Lekcja o PIT-11 i formularz PIT-11**: wiersz 5 (dzieło) i wiersz 6 (zlecenie) rozdzielone, poz. 95/96/97, poz. 112, kwadraty poz. 28 z numerami jak na druku;
  usunięte nieistniejące pole „czy zwolnienie stosowano na wniosek”.
- **Akta osobowe**: szablon onboardingu przypisywał orzeczenia okresowe do części A — poprawnie część B (§ 3 pkt 2 rozporządzenia o dokumentacji pracowniczej);
  część A to badania wstępne i dokumenty z rekrutacji. (Błąd wprowadziła poprzednia korekta.)
- **Wzory ZUS**: w lekcji o rozliczeniach — rozporządzenie z 9.04.2026 (Dz.U. 2026 poz. 518), nowe RCA i DRA od rozliczenia za kwiecień 2026, brak raportu RZA
  (za osobę zgłoszoną tylko do ubezpieczenia zdrowotnego składasz RCA).
- **Spójność ćwiczeń** (11 miejsc): komplet RSA dla zasiłku wypłaconego 10.12 (12/2026, nie 11/2026), odsetki od dnia po terminie (17.11), terminy wypadające w niedzielę
  (17.01.2027 → 18.01), A1 przy pracy w dwóch państwach (art. 13 i US-4 zamiast umowy ramowej), okres zwolnienia z FP po urlopie rodzicielskim, wypłata 8.01.2027,
  staż na dzień rozwiązania umowy, liczba kompletów korygujących, koszt aneksów, zespół powypadkowy bez SIP.
- **Klucze uczciwe wobec uczącego się**: ćwiczenie o procedurze antymobbingowej sprawdza fakty (termin 5.05.2027, kanały, skład komisji, rejestr), a nie liczby dni
  z przykładowej procedury; luka płacowa z tolerancją zaokrąglenia; termin odpowiedzi na wniosek o pracę zdalną z jawnym założeniem o sobocie.
- **Warsztat**: Lista płac liczy umowę o pracę — przy zleceniobiorcy i wykonawcy dzieła ostrzega i nie dodaje wiersza do listy miesiąca (z listy powstają RCA i PIT-11);
  komplet ZUS przypomina o RCA zleceniobiorców.
- **Panel odpowiedzi**: lista wyboru z długą opcją ma własny wiersz na całą szerokość, a etykiety zawijają się w faktycznej szerokości karty (nic nie chowa się pod polem).
- Kurs: 87 ćwiczeń z kluczem (423 pola, 56 podpowiedzi), 10 formularzy (139 pól, 33 podpowiedzi). Test `test_skladki_do_pit11_ulga_dla_mlodych`.

## 2.8.0 — kurs „Kadry i płace” 3.0: pełny audyt merytoryczny, sprawdzanie automatyczne, prawdziwe formularze, projekt końcowy, kalendarz aktualizacji

- **Sprawdzanie automatyczne ćwiczeń** (`odpowiedzi.py`, `odpowiedzi_ui.py`; pole `odpowiedzi` ćwiczenia): pod 87 z 96 ćwiczeń kursu kadrowego są pola
  „Twoje odpowiedzi” (422 pola: kwoty, daty, kody, wybory). Mentor ocenia każde pole osobno i nie ujawnia wyniku; 52 typowe pomyłki mają własną podpowiedź
  („to netto bez PPK”, „31.01.2027 to niedziela…”). Wynik wzorcowy odsłania się po komplecie albo po „Pokaż klucz” (po 2 próbach). Budowanie kursu sprawdza,
  że każda wartość klucza występuje w rozwiązaniu ćwiczenia.
- **Warsztat → Formularze** (pole `formularze` programu): 10 ćwiczeń na wzorach prawdziwych druków z numerami pól — ZUS ZUA, ZWUA (dwa scenariusze, blok V z kodami),
  RCA (blok III.B i III.C), RSA, PIT-2 w wersji 9 (dwa scenariusze), PIT-11 w wersji 29 (poz. 28–33, 95, 122), świadectwo pracy wg wzoru MRPiPS (ust. 1–8) —
  139 pól ze sprawdzaniem, zapis wypełnionego druku do projektu; kroki „Formularz” dopisane do zadań tygodniowych.
- **Projekt końcowy „Zamknięcie roku 2026 w AGRO-MLEKO”** — 35 pól: lista płac za grudzień (premia roczna, choroba, pierwsza wypłata nowego roku podatkowego),
  komplet ZUS i RSA/RPA wg zasady kasowej, PIT, wskaźniki i terminy 2027, korekta odpisu ZFŚS.
- **Kalendarz aktualizacji kursu** (pole `aktualizacje`): 17 dat do sprawdzenia w przepisach (PIT 2027, diety 2027, UC127, UDER105, wskaźniki 2027, autozapis PPK,
  mobbing 5.05.2027, abolicja PIP, ochrona czasowa UA…) — karta „Aktualność przepisów” na Panelu i pełna lista z przyciskiem „Sprawdzone” w Ściądze.
- **Pełny audyt merytoryczny kursu** (wszystkie 48 lekcji, 60 zadań, quizy, 33 szablony, 64 przepisy, ściąga — ze źródłami: ELI/Dz.U., M.P., ZUS, MF, PFR, SN):
  m.in. zwolnienia grupowe i indywidualne (regulamin bez związków, ochrona art. 39/177 — tylko wypowiedzenie zmieniające, staż do odprawy na dzień rozwiązania,
  limit 74 250 zł w 2027), świadectwo pracy wg urzędowego wzoru, kody ZWUA 20R–53W i 400–442, PIT-2 — litery części wg wzoru, PIT-11 — składka zdrowotna w poz. 122
  i dochód jako przychód minus koszty, terminy roczne 2027 przesunięte przez niedziele (1.02 i 1.03.2027), projekt UDER105, limit 30-krotności 2027 z obwieszczenia
  (300 990 zł), mandat PIP 2 000–5 000 zł (recydywa do 10 000), limit kontroli mikroprzedsiębiorcy 6 dni, praca zdalna (7 dni roboczych, powrót w 30 dni),
  sygnaliści (próg w etatach), zasada kasowa w RSA/RCA, potrącenia z zasiłków. Dwa nowe wpisy w bibliotece przepisów (potrącenia z zasiłków, kary porządkowe);
  automat spójności odwołań do nazw lekcji, szablonów i przepisów.
- **Silnik i Warsztat**: `kadry.lista_plac(bez_zus=…)` i pole „Odprawa / odszkod. (bez ZUS)” w Liście płac; lista „za miesiąc” i „wypłata w miesiącu”;
  komplet ZUS z list wypłaconych w miesiącu; potrącenia z zasiłku; PIT-11 symulatora z numerami pozycji wersji 29 i terminami przesuniętymi na dzień roboczy.
- **Treść**: nowe sekcje — czas pracy kierowców (ustawa z 16.04.2004 i rozporządzenie 561/2006), sankcje PPK, inne ścieżki pracy cudzoziemców (praca sezonowa,
  pobyt czasowy i praca, Niebieska Karta), liczenie stanu zatrudnienia do PFRON; „Jeśli zaczynasz od zera” w lekcji startowej; źródła zagraniczne — tylko otwarte
  (ACAS na licencji OGL, CIPD), SHRM oznaczone jako płatne i nieobowiązkowe. Kurs: 48 lekcji, 96 ćwiczeń, 64 przepisy, 136 h; każdy tydzień ≤ 9 h.
- **Testy**: `testy/test_odpowiedzi.py` (silnik sprawdzania, klucze ćwiczeń i formularzy) i `testy/test_kadry.py` (silnik płacowy na przypadkach z lekcji).

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
