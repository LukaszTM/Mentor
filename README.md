# Mentor — interaktywny nauczyciel

Program desktopowy na Windows, który prowadzi Cię przez **dowolny program nauczania** wczytany z pliku: plan tygodni z zadaniami
opisanymi krok po kroku, krótkie lekcje z testami, timer sesji, dziennik, quizy, odznaki — i asystent AI
(Claude Code, API albo tryb offline), który ma Cię uczyć, nie wyręczać.

W zestawie jest program **„Python od zera → Junior QA”** (13 tygodni, 65 zadań, 32 lekcje, 96 pytań testowych).
Własny program robisz w JSON (Ustawienia → „Zapisz pusty szablon programu”; opis formatu: `programy/FORMAT.md`).

## Uruchomienie

1. Zainstaluj Pythona 3.10+ z python.org (zaznacz **Add Python to PATH**) — to i tak zadanie 1 z tygodnia 0.
2. Rozpakuj folder `mentor_claude` gdziekolwiek (np. `C:\Users\<użytkownik>\mentor_claude`).
3. Kliknij dwukrotnie **`start_mentor.bat`** albo w terminalu:

   ```
   cd mentor_claude
   python mentor.py
   ```

Nie potrzeba żadnych bibliotek — program używa tylko tego, co jest w Pythonie (tkinter).
Przy pierwszym uruchomieniu poda imię, potem w zakładce **Mój projekt** wskaż katalog `nauka-python`.

**Mentor.exe (z Releases) nie wymaga Pythona.** Gdy kurs potrzebuje Pythona i bibliotek (np. Python → Junior QA),
Mentor sam je przygotuje w zakładce **Środowisko** — bez terminala i bez uprawnień administratora (patrz niżej).

### Gdzie są dane

| Uruchomienie | Katalog danych (postępy, kursy, środowiska, logi) |
|---|---|
| `Mentor.exe` na Windows | `%LOCALAPPDATA%\Mentor\` (np. `C:\Users\<Ty>\AppData\Local\Mentor\`) — katalog EXE może być tylko do odczytu |
| `Mentor.exe` z plikiem `portable.txt` obok | katalog EXE (tryb przenośny, np. pendrive) |
| `python mentor.py` (deweloper) | katalog repozytorium |
| zmienna środowiskowa `MENTOR_DANE` | wskazany katalog (testy, nietypowe instalacje) |

Struktura: `mentor_dane.json` (postępy), `programy/` (wbudowane programy JSON i wgrane z pliku), `kursy/<id>/` (kursy z paczek ZIP:
`kurs.json`, `meta.json`, `paczka/` z materiałami; `kursy/_kopie/` — poprzednie wersje), `srodowiska/<id>/.venv` (osobne środowisko Pythona
każdego kursu + `stan.json`), `python/` (Python pobrany przez Mentora, gdy w systemie go nie ma), `pobrane/`, `logi/`.
Pliki ćwiczeń ucznia są **poza** tym wszystkim: `Dokumenty\Mentor\<id kursu>\PRACA\` (albo katalog wskazany w Mój projekt).

Starsza wersja trzymała `mentor_dane.json` i `programy/` obok EXE — nowy Mentor **przenosi je sam** przy pierwszym uruchomieniu
(z kopią `mentor_dane.json.kopia-<data>`; oryginały zostają) i pokazuje na Panelu, co zrobił. Ustawienia → „Otwórz folder danych Mentora”.

## Co robi

| Zakładka | Po co |
|---|---|
| **Jak zacząć** | Przewodnik, który otwiera się sam przy pierwszym uruchomieniu i przy pierwszym wejściu w nowy program (potem: przycisk „Jak zacząć” na Panelu): imię i katalog projektu bez okienek, rytm dnia, pętla lekcja → zadanie → odhaczenie, opis każdej zakładki i „co, jeśli…”. Na Panelu do pierwszego zadania wisi karta **Pierwsze kroki** z 4 przyciskami. |
| **Panel** | Powitanie, seria dni, XP, odznaki, postęp etapów i — najważniejsze — *co masz zrobić dzisiaj* (pon–czw zadanie dnia, pt zadanie tygodnia, sob quiz, nd wolne). Po przerwie ≥ 2 dni pokazuje łagodny komunikat powrotu, nie wyrzut sumienia. |
| **Plan nauki** | Wszystkie tygodnie i zadania programu. Każde zadanie ma rozwijaną sekcję **„Jak to zrobić”** — pełną instrukcję krok po kroku (co kliknąć, co wpisać, jakie komendy), „Gotowe, gdy…” (jak samemu sprawdzić) i „Gdy coś nie działa” (typowe problemy). Przy tygodniu — lekcje do przeczytania przed zadaniem. Jeśli wskażesz katalog projektu, Mentor pokazuje „✔ wykryto zmienne.py” — jako podpowiedź, nie zaliczenie. W kursach z Pythonem pod zadaniem jest pasek **Ćwiczenie w Mentorze**: *Otwórz przykład* (kod w innym kontekście niż zadanie), *Utwórz plik ćwiczenia* (szablon w katalogu PRACA; istniejącego pliku nie nadpisuje bez pytania), *Otwórz w edytorze* (VS Code / PyCharm / Notatnik — nigdy przez „otwórz” systemowe, które by plik uruchomiło), *Uruchom* (interpreter kursu, limit czasu, Anuluj, wyjście i błędy z wyjaśnieniem po polsku, pole danych dla `input()`), *Sprawdź wynik* (test z definicji zadania: uruchomienie bez błędu / oczekiwane wyjście / pytest — zalicza automatycznie; bez testu: „Plik istnieje — wymaga sprawdzenia”, nigdy „Zaliczone”), *Pokaż podpowiedź*. |
| **Lekcje** | Pierwsza lekcja każdego programu to **wprowadzenie** („Start: jak uczyć się z tego programu”). Lekcje zgodne ze standardem (`programy/STANDARD_KURSOW.md`) mają stałą kolejność: 🎯 cel → 💡 po co mi to → 📦 czego potrzebujesz → 1 · wyjaśnienie od podstaw → 2 · demonstracja (przykład w ramce + omówienie każdego kroku + oczekiwany wynik) → 3 · jak to uruchomić → 4 · ćwiczenie prowadzone i 5 · samodzielne z przyciskiem **„Podpowiedź 1 z 3”** (pytanie naprowadzające → gdzie szukać → częściowy przykład → „Pokaż pełne rozwiązanie”) → 6 · typowe błędy i naprawa (komunikat, przyczyna, jak sprawdzić, poprawka) → pułapki → dodatkowe zadania → sprawdzenie (pytania rozwijane + „co potrafię bez przykładu”) → **test 3 pytań**; powtórka na końcu każdego etapu; ← poprzednia / następna →. Lekcje bez bloków standardu — układ klasyczny (cel, wyjaśnienie, przykład, pułapki, zadania, pytania, test). |
| **Sesja nauki** | Timer rytmu dnia 20/50/15/5 min z dzwonkiem i promptem do każdej fazy; pole **„Temat sesji”** zapisuje się razem z minutami. Tryb pełny (90 min), skrócony (45) i mini (30). Osobny **licznik 15 minut własnej walki**. **„Dopisz czas nauki…”** — czas spoza aplikacji: podajesz minuty i temat (lekcję z listy albo własny), odpowiadasz na **3–4 pytania** z tego tematu i dopiero wtedy wpis się zapisuje. XP za dzień nauki przyznaje się **raz na dobę**, niezależnie od liczby wpisów. |
| **Warsztat** | Narzędzia wewnętrzne programu (gdy program je deklaruje — kurs kadrowy ma 9): Firma ćwiczeniowa, Lista płac (brutto→netto krok po kroku, „Tryb ćwiczenia”: najpierw wpisujesz swoje netto), Zasiłki i chorobowe (podstawa z 12 miesięcy z uzupełnianiem, pula 33/14 i okres zasiłkowy), Urlopy i ekwiwalent, Czas pracy (wymiar każdego miesiąca, nadgodziny, dodatek nocny, okres wypowiedzenia), Potrącenia (kwoty wolne), **symulator eZUS/Płatnika** (rejestr ubezpieczonych, ZUA/ZZA/ZWUA/ZCNA/ZIUA z weryfikacją jak w Płatniku, komplety DRA/RCA/RSA z listy płac, skrzynka e-ZLA, rejestr z numerami UPP), **symulator e-Urzędu** (PIT-11 i PIT-4R z kartoteki, UPO) i Przepisy (48 streszczeń offline z linkami do ISAP jako opcją). Każde narzędzie ma „Zapisz do projektu” (.md/.csv). Zero kont zewnętrznych, zero instalacji, zero arkuszy — cały kurs da się przejść w Mentorze. Silnik obliczeń: `kadry.py`, widoki: `warsztat.py`. |
| **Mój projekt** | **Utwórz katalog roboczy kursu** (Mentor zakłada `Dokumenty\Mentor\<kurs>\PRACA`) albo wskaż własny. Mentor zagląda do katalogu: stan narzędzi kursu (z ostatniej realnej diagnozy w zakładce Środowisko — nie z samego PATH), czy jest `CLAUDE.md` (może go utworzyć z zasadami), ostatni commit, czy dziś był commit, ile plików czeka bez commita, które pliki z zadań bieżącego tygodnia już istnieją. **Otwórz terminal tutaj** otwiera terminal w katalogu roboczym z Pythonem kursu na początku PATH (`python`, `pip`, `pytest` działają od razu); **Otwórz Claude Code tutaj** — to samo z uruchomionym `claude`. |
| **Środowisko** | Dla kursów, które uruchamiają kod (Python, biblioteki, Git, przeglądarka). Tabela statusów **z realnych uruchomień** (`python --version`, import w środowisku kursu, `git --version`, Edge): Gotowe / Brak / Nieprawidłowa wersja / Błąd / Opcjonalne / Sprawdzanie. **Zainstaluj brakujące** pokazuje najpierw listę kroków ze źródłem, rozmiarem, potrzebą internetu i uprawnień — i dopiero po zgodzie, w tle (GUI nie zamarza), tworzy osobne `.venv` kursu, instaluje biblioteki **z locka z sumami SHA-256** (tylko zadeklarowane w kursie, z PyPI, bez komend z paczki), a gdy w systemie nie ma Pythona — pobiera oficjalny runtime (python-build-standalone 3.12, suma przypięta w Mentorze) do katalogu Mentora. Potem **Sprawdź działanie**: interpreter, importy, przykładowy pytest, lokalne API + prawdziwe żądanie HTTP, Selenium w prawdziwej przeglądarce (raportowane osobno). „Gotowe” dopiero, gdy testy przechodzą. Przyciski: Sprawdź ponownie, Napraw środowisko, Usuń środowisko, Usuń kurs (PRACA i postępy zostają), Anuluj / Ponów / Pokaż szczegóły (log). Offline: lekcje i teoria działają zawsze, instalacja mówi wprost, że brak sieci. |
| **Asystent** | Trzy karty: **Subskrypcja** (Claude Code — status instalacji, komendy, otwarcie w projekcie), **API** (prawdziwy Claude przez klucz z console.anthropic.com, płatność za użycie; rozmowa w oknie, pliki przez `@nazwa.py`, zasady z CLAUDE.md i kontekst tygodnia w tle) oraz **Offline** (wbudowany emulator bez konta i internetu). |
| **Prompty** | 15 szablonów z dokumentu i etapów (Nowy temat, Utknąłem, Recenzja, Zatrzymaj się, Ja tłumaczę Twój kod, Ukryty błąd, Oczami rekrutera, Próbna rozmowa…) + treść `CLAUDE.md` + szablon bug raportu. „Wypełnij [nawiasy]” pyta o każdy nawias i kopiuje gotowy prompt. |
| **Quiz** | 59 pytań — 5 na tydzień 0–9, 3 na tygodnie 10–12 — z wyjaśnieniami. Błędne odpowiedzi trafiają do **powtórki** i wracają, aż odpowiesz dobrze. 100% = odznaka. Ekran wyniku w aplikacji (bez okienek): punkty, komentarz, **lekcje do powtórzenia** z przyciskami „Otwórz lekcję”, „Powtórz błędne pytania”. **Diagnoza na start** (jeśli program ją ma): kilka pytań z całego kursu, nie blokuje nauki, nie daje XP — wskazuje lekcje, przy których zwolnić. |
| **Dziennik** | Dwa zdania dziennie z losowym pytaniem mentora („Co dziś było najtrudniejsze?”). Pisanie o tym, czego się nauczyłeś, utrwala mocniej niż ponowne czytanie. |
| **Checklista** | Checklista postępów z dokumentu — odhaczasz tylko to, co robisz *bez pomocy Claude*. |
| **Ściąga** | Komendy Claude Code i Gita, linki do dokumentacji i stron do ćwiczeń Selenium. |
| **Ustawienia** | Imię, katalog projektu, **motyw**, eksport `POSTEPY.md` (do repo lub dla kogoś, kto Cię wspiera), reset. |

## Programy nauczania

Ustawienia → **Program nauczania**: lista programów (wbudowane, wgrane z JSON i zaimportowane z paczek ZIP), przełączanie (postępy
każdego programu zapisują się osobno pod jego `id`), **„Importuj kurs ZIP…”**, „Importuj JSON…” (walidacja + kopia do `programy/`),
„Zapisz pusty szablon programu”. Format: `programy/FORMAT.md`.

### Import kursu z paczki ZIP

1. Ustawienia → **Importuj kurs ZIP…** → wybierz plik. Mentor **najpierw pokazuje podgląd**: nazwa, wersja, autor, liczba lekcji i zadań,
   wymagania (Python, biblioteki, narzędzia, przeglądarka), rozmiar, źródło, czy potrzebny internet, jakie uprawnienia (żadnych — wszystko w katalogu użytkownika),
   oraz ostrzeżenie o skryptach w paczce (`.bat`, `.ps1`, `.py` w korzeniu) — **Mentor ich nigdy nie uruchamia**.
2. Po zgodzie paczka jest rozpakowywana do `kursy/<id>/` (katalog tymczasowy → atomowe podmienienie). Odrzucane są: ścieżki z `..`, bezwzględne,
   dowiązania symboliczne, archiwa z >20 000 plików, >2 GB po rozpakowaniu, pojedyncze pliki >512 MB i „bomby” kompresji.
3. Kurs o tym samym `id` w nowszej/innej wersji: Mentor pyta, robi kopię poprzedniej wersji w `kursy/_kopie/` i **zachowuje postępy**
   (identyfikatory zadań i lekcji są stabilne) oraz katalog PRACA.
4. Mentor tworzy katalog roboczy `Dokumenty\Mentor\<id>\PRACA` i podpina go jako „Mój projekt”; jeśli kurs wymaga środowiska, otwiera zakładkę Środowisko.

Obsługiwane paczki: nowe z `mentor-manifest.json` (schemat `mentor-course/1`: `course_id`, `version`, `entrypoint`, `requirements` z `python`,
`python_packages_lock`, `required_tools`, `optional_tools` (`{name, from_week}`), `browser`, `browser_from_week`, `checks`) oraz **starsze** (v1.1:
JSON kursu w korzeniu + `requirements.txt` + skrypty) — wymagania są wtedy brane z pola `srodowisko` programu, z `requirements.txt`/`.lock` albo
rozpoznawane po treści. Biblioteki spoza zaufanej listy (pytest, requests, selenium, flask) bez locka z hashami nie są instalowane automatycznie.
Paczkę przygotujesz funkcją `paczki.zbuduj_paczke(katalog, plik.zip, manifest)`.

Wbudowane programy (źródła w Pythonie z generatorami w `programy/zrodla/*/zbuduj.py`):

| Program | Plik | Co zawiera |
|---|---|---|
| **Python od zera → Junior QA** (2.1) | `programy/python-junior-qa.json` | 13 tygodni (0–12), 65 zadań, 33 lekcje, projekt portfolio z pytest + Selenium. Dostosowany do Mentora 2.7: tydzień 0 zaczyna się od zakładki Środowisko (Python i biblioteki instaluje Mentor, uczeń instaluje tylko Git), katalog roboczy PRACA zakłada Mentor, 37 zadań ma ćwiczenia „w Mentorze” (szablon, przykład, podpowiedź, ▶ Uruchom, ✔ Sprawdź wynik z testem), ściąga „Mentor — środowisko i ćwiczenia” |
| **Kadry i płace — kurs zaawansowany (praktyka 2026)** | `programy/kadry-i-place.json` | 16 tygodni (0–15, każdy ≤ 9 h), 60 zadań, 46 lekcji (41 + 5 powtórek etapów) wg standardu `programy/STANDARD_KURSOW.md` — każda z demonstracją krok po kroku, ćwiczeniem prowadzonym i samodzielnym z 3 podpowiedziami i rozwiązaniem, typowymi błędami; 90 plików ćwiczeń w paczce materiałów; diagnoza na start; 60 pytań quizowych z lekcją do powtórki: prawo pracy, czas pracy, urlopy i staż 2026, lista płac brutto→netto, PIT, zasiłki i kontrola L4 po reformie 2026, zlecenia/dzieło/PPK/cudzoziemcy, ZUS (zgłoszenia, DRA/RCA/RSA, korekty), PIT roczny, ZFŚS/PFRON, kalendarz, rozwiązanie umowy, odprawy, świadectwo, mobbing (nowelizacja 2026), jawność wynagrodzeń, sygnaliści, kontrola PIP/ZUS — wszystko na fikcyjnej firmie, ze wskaźnikami 2026/2027 i podstawą prawną przy każdej liczbie (stan prawny: listopad 2026) |

Kurs kadrowy jest w pełni samowystarczalny: zadania wykonujesz w Warsztacie (symulatory ZUS/US, kalkulatory, przepisy), bez logowania do eZUS/e-Urzędu, bez Płatnika i bez Excela — te systemy są opisane w lekcjach, żeby po kursie przesiadka była tylko kwestią logowania.

**Standard kursów.** `programy/STANDARD_KURSOW.md` opisuje wymagany przebieg każdej lekcji (12 elementów), zasady ćwiczeń, kompletność paczki ZIP i checklistę publikacyjną. Kurs kadrowy jest z nim zgodny (raport: `programy/materialy/kadry-i-place/RAPORT_CHECKLISTA.md`); kurs Python — układ klasyczny (do uzupełnienia o bloki standardu). Paczka materiałów kursu kadrowego: `programy/materialy/kadry-i-place/` (START_TUTAJ.md, SPRAWDZ_SRODOWISKO.bat, INSTALACJA.bat, URUCHOM_KURS.bat, kurs_mentor.json, manifest.json, lekcje/, przyklady/, cwiczenia/, rozwiazania/, projekty/, testy/, pomoc/, instalatory/) — generowana z `programy/zrodla/kadry_i_place/materialy.py`; w Mentorze: Mój projekt → „Skopiuj materiały kursu tutaj”.

Przełączasz w Ustawieniach → Program nauczania → Przełącz. Każdy program ma własny katalog projektu (`nauka-python`, `kadry-praktyka`), własne prompty, ściągę, słowniczek dla Asystenta Offline i pytania rekrutacyjne.

## Mechanizmy, które mają Cię przyciągać z powrotem

- **Seria dni** — liczy dni z zapisaną sesją; **niedziela nie przerywa serii** (plan mówi: wolne).
- **XP** — zadanie 10, piątkowe 25, pierwsza sesja dnia 5, dobra odpowiedź w quizie 2 (+10 za 100%), wpis do dziennika 3.
- **Odznaki** — start, pierwszy tydzień, serie 5/15/30 dni, każdy ukończony etap programu (nazwy z programu), quizy, testy lekcji, XP, dziennik, godziny. Panel zawsze pokazuje *następną* do zdobycia.
- **Wskazówka dnia** — jedna zasada nauki z dokumentu dziennie.
- **Koniec tygodnia** — po odhaczeniu piątego zadania Mentor przypomina o quizie i checkliście („jeśli coś zostaje puste — dodaj tydzień, nie skracaj”).

## Asystent bez subskrypcji Claude Code

Program nauki zakłada Claude Code (plan Pro/Max). Jeśli go nie masz, zakładka **Asystent** daje dwie alternatywy:

**API** — konto na console.anthropic.com, klucz, doładowane saldo. Ten sam model co w Claude Code, w oknie Mentora.
Płacisz za tokeny (krótka rozmowa o pliku to zwykle grosze). Asystent nie uruchamia komend ani nie edytuje plików — czyta je,
gdy wskażesz `@plik.py`. Klucz trzymany jest w `mentor_dane.json` na Twoim dysku.

**Offline** — zero kosztów. To nie model językowy, tylko emulator rozumiejący prompty z planu:

| Napiszesz | Dostaniesz |
|---|---|
| `uczę się pętli`, `/temat git`, `co to jest fixture` | wyjaśnienie z przykładami z gospodarstwa, kod, pułapki, 3 zadania (27 tematów, 25 pojęć) |
| `przejrzyj @bmi.py` | recenzję jak mentor: co dobrze, co błędem (gołe except, input() w arytmetyce, zmienne domyślne…), co czytelniej, pytanie naprowadzające |
| `utknąłem … błąd: TypeError` | co znaczy błąd i pytanie, które naprowadza — bez poprawiania kodu (18 typów błędów) |
| `uruchom @plik.py << 1.8; 75` | uruchomienie pliku, wynik lub traceback przetłumaczony na pytanie |
| `quiz z tygodnia 2`, `zadaj mi 3 pytania` | quiz A–D w rozmowie (wynik liczy się do XP), pytania sprawdzające z wzorcami (`/odpowiedzi`) |
| `wprowadź do @plik.py ukryty błąd`, `/debug` | kopia pliku z jedną mutacją / 62‑liniowy program z 3 błędami do debugowania; `/rozwiazanie` gdy się poddasz |
| `commit`, `/git`, `/init`, `/plan` | propozycja commita i wykonanie za zgodą, status repo, CLAUDE.md, szkielet PLAN.md |
| `odpytaj mnie jak rekruter` | 15 pytań na Junior QA z wzorcowymi odpowiedziami |

Zanim cokolwiek wykona lub zapisze, pyta o zgodę (`t`/`n`) — jak Claude Code w trybie „pytaj”. `/tryb` przełącza na auto.
Przyciski „Wyślij do Asystenta” w Sesji i Promptach wklejają gotowy prompt. Gdy klikniesz „Otwórz Claude Code” bez
zainstalowanego Claude, Mentor zaproponuje Asystenta.

## Wygląd

Wszystko w Ustawieniach → Wygląd, zmiany od razu i na stałe:

- **Czcionka** — krój (lista popularnych + okno „Wszystkie czcionki…” z podglądem i wyszukiwarką) oraz wielkość
  w pięciu krokach (85–150 %). Skalują się wszystkie teksty, tabele i przyciski.
- **Jasność terminala** — suwak 40–100 % dla motywów terminalowych; przyciemnia tekst i akcenty, tło zostaje czarne.
  Domyślnie 70 %, żeby fosfor nie świecił po oczach.
- **Pasek boczny** — szerokość suwakiem albo przeciąganiem prawej krawędzi; bardzo wąsko = zwinięcie do samych ikon
  (z dymkami). Przycisk ◀/▶ w nagłówku paska robi to samo. Zakładki są duże, pogrubione i rozsunięte.
- **Motyw** — klikasz kafelek; motyw zmienia się od razu i zostaje zapamiętany.

- **Wzorowane na PyCharm** — schematy wbudowane (Darcula, Dark i Light z nowego interfejsu, IntelliJ Light) oraz
  najczęściej pobierane z JetBrains Marketplace: Material Oceanic, One Dark, Dracula, Gruvbox Dark, Monokai, Nord,
  Solarized Dark / Light.
- **Wzorowane na VS Code** — Dark Modern, Dark+ (klasyczny), Light Modern.
- **Wzorowane na terminalu Windows** — zielony fosfor i bursztynowy, cały interfejs w czcionce monospace.
- **Mentor (domyślny)** — jasny, ciepły.

Własny motyw to jeden wpis `zbuduj(...)` w `motywy.py` — podajesz kilkanaście kolorów, resztę (tła plakietek,
kolory po najechaniu) program wylicza sam.


## Pliki

- `mentor.py` — aplikacja (okno, timer, nadzór projektu, lekcje, quiz, dziennik)
- `program.py` — wczytywanie i walidacja programów JSON; katalog danych (`%LOCALAPPDATA%\Mentor`), migracja starych danych, kursy z paczek
- `paczki.py` — podgląd i bezpieczny import paczek ZIP (manifest `mentor-course/1` i stare v1.1), synteza wymagań, katalog PRACA, kopie wersji
- `srodowisko.py` — menedżer środowisk: realna diagnoza (Python, .venv, biblioteki, Git/Claude, przeglądarka), plan instalacji, pobranie runtime’u Pythona (SHA-256), `.venv` + pip z locka z hashami, testy końcowe (pytest, API, Selenium), uruchamianie kodu ucznia interpreterem kursu
- `widok_srodowisko.py` — zakładka Środowisko (wątek roboczy + kolejka + `after`, log, Anuluj/Ponów)
- `cwiczenia.py` — ćwiczenia w Mentorze (przykład, szablon, edytor, uruchomienie z limitem, sprawdzenie wyniku)
- `srodowisko_testy/` — skrypty testów końcowych uruchamiane w środowisku kursu (próbka pytest, serwer API, klient HTTP, Selenium + strona HTML)
- `programy/zaleznosci/requirements.lock` — przypięte wersje bibliotek kursów z sumami SHA-256 (Windows i Linux, Python 3.11–3.13)
- `testy/` — testy pytest (`python -m pytest testy -q`; 78 testów): bezpieczeństwo ZIP, import v1.1 bez uruchamiania skryptów, manifest, aktualizacja z kopią, lock, diagnoza, realne `.venv` + pip, testy końcowe, ćwiczenia, GUI (na Windows CI także pobranie runtime’u Pythona i Selenium z Edge)
- `asystent.py` — emulator offline (analiza kodu, uruchamianie, quiz, git) i klient API
- `wiedza_ogolna.py` — wbudowany słownik błędów Pythona (gdy program nie ma własnego)
- `motywy.py` — motywy kolorystyczne
- `programy/python-junior-qa.json` — wbudowany program; `programy/szablon-programu.json` — szkielet; `programy/FORMAT.md` — opis formatu
- `programy/zrodla/python_junior_qa/` — źródła programu w Pythonie (`tresc.py`, `jak.py`, `wiedza.py`, `lekcje_extra.py`, `zbuduj.py`)
- `programy/zrodla/kadry_i_place/` — źródła kursu kadrowego: `plan_tygodni.py` (harmonogram 16 tygodni — jedyne miejsce, które przypisuje lekcje i zadania do tygodni; limit 9 h/tydzień sprawdzany przy budowie), `tygodnie_*.py` (treść zadań), `lekcje_*.py` (treść lekcji), `wyjasnienia.py` (wyjaśnienia przepisane: krótkie zdania, nagłówki, tabele — `zbuduj.py` pilnuje, by żadna liczba ani przepis nie zginęły), `lekcja_delegacje.py` (lekcja o podróżach służbowych + bloki standardu), `standard_1..5.py` (bloki standardu pozostałych lekcji), `powtorki.py`, `diagnoza.py`, `quizy_dodatkowe.py`, `szablony.py`, `materialy.py` (paczka ZIP), `zbuduj.py` (składa JSON i liczy czas lekcji z objętości treści)
- `programy/STANDARD_KURSOW.md` — standard tworzenia kursów; `programy/materialy/kadry-i-place/` — paczka materiałów kursu (generowana)
- `kadry.py` — silnik obliczeń kadrowo-płacowych; `warsztat.py` — widoki Warsztatu
- `start_mentor.bat` — uruchamianie dwuklikiem na Windows
- `mentor_dane.json` — Twoje postępy (w katalogu danych, patrz „Gdzie są dane”)
