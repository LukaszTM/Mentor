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

Twoje postępy zapisują się w `mentor_dane.json` obok programu. Skopiuj ten plik = masz kopię zapasową.

## Co robi

| Zakładka | Po co |
|---|---|
| **Jak zacząć** | Przewodnik, który otwiera się sam przy pierwszym uruchomieniu i przy pierwszym wejściu w nowy program (potem: przycisk „Jak zacząć” na Panelu): imię i katalog projektu bez okienek, rytm dnia, pętla lekcja → zadanie → odhaczenie, opis każdej zakładki i „co, jeśli…”. Na Panelu do pierwszego zadania wisi karta **Pierwsze kroki** z 4 przyciskami. |
| **Panel** | Powitanie, seria dni, XP, odznaki, postęp etapów i — najważniejsze — *co masz zrobić dzisiaj* (pon–czw zadanie dnia, pt zadanie tygodnia, sob quiz, nd wolne). Po przerwie ≥ 2 dni pokazuje łagodny komunikat powrotu, nie wyrzut sumienia. |
| **Plan nauki** | Wszystkie tygodnie i zadania programu. Każde zadanie ma rozwijaną sekcję **„Jak to zrobić”** — pełną instrukcję krok po kroku (co kliknąć, co wpisać, jakie komendy), „Gotowe, gdy…” (jak samemu sprawdzić) i „Gdy coś nie działa” (typowe problemy). Przy tygodniu — lekcje do przeczytania przed zadaniem. Jeśli wskażesz katalog projektu, Mentor pokazuje „✔ wykryto zmienne.py” — jako podpowiedź, nie zaliczenie. |
| **Lekcje** | Pierwsza lekcja każdego programu to **wprowadzenie** („Start: jak uczyć się z tego programu”). Lekcje zgodne ze standardem (`programy/STANDARD_KURSOW.md`) mają stałą kolejność: 🎯 cel → 💡 po co mi to → 📦 czego potrzebujesz → 1 · wyjaśnienie od podstaw → 2 · demonstracja (przykład w ramce + omówienie każdego kroku + oczekiwany wynik) → 3 · jak to uruchomić → 4 · ćwiczenie prowadzone i 5 · samodzielne z przyciskiem **„Podpowiedź 1 z 3”** (pytanie naprowadzające → gdzie szukać → częściowy przykład → „Pokaż pełne rozwiązanie”) → 6 · typowe błędy i naprawa (komunikat, przyczyna, jak sprawdzić, poprawka) → pułapki → dodatkowe zadania → sprawdzenie (pytania rozwijane + „co potrafię bez przykładu”) → **test 3 pytań**; powtórka na końcu każdego etapu; ← poprzednia / następna →. Lekcje bez bloków standardu — układ klasyczny (cel, wyjaśnienie, przykład, pułapki, zadania, pytania, test). |
| **Sesja nauki** | Timer rytmu dnia 20/50/15/5 min z dzwonkiem i promptem do każdej fazy; pole **„Temat sesji”** zapisuje się razem z minutami. Tryb pełny (90 min), skrócony (45) i mini (30). Osobny **licznik 15 minut własnej walki**. **„Dopisz czas nauki…”** — czas spoza aplikacji: podajesz minuty i temat (lekcję z listy albo własny), odpowiadasz na **3–4 pytania** z tego tematu i dopiero wtedy wpis się zapisuje. XP za dzień nauki przyznaje się **raz na dobę**, niezależnie od liczby wpisów. |
| **Warsztat** | Narzędzia wewnętrzne programu (gdy program je deklaruje — kurs kadrowy ma 9): Firma ćwiczeniowa, Lista płac (brutto→netto krok po kroku, „Tryb ćwiczenia”: najpierw wpisujesz swoje netto), Zasiłki i chorobowe (podstawa z 12 miesięcy z uzupełnianiem, pula 33/14 i okres zasiłkowy), Urlopy i ekwiwalent, Czas pracy (wymiar każdego miesiąca, nadgodziny, dodatek nocny, okres wypowiedzenia), Potrącenia (kwoty wolne), **symulator eZUS/Płatnika** (rejestr ubezpieczonych, ZUA/ZZA/ZWUA/ZCNA/ZIUA z weryfikacją jak w Płatniku, komplety DRA/RCA/RSA z listy płac, skrzynka e-ZLA, rejestr z numerami UPP), **symulator e-Urzędu** (PIT-11 i PIT-4R z kartoteki, UPO) i Przepisy (48 streszczeń offline z linkami do ISAP jako opcją). Każde narzędzie ma „Zapisz do projektu” (.md/.csv). Zero kont zewnętrznych, zero instalacji, zero arkuszy — cały kurs da się przejść w Mentorze. Silnik obliczeń: `kadry.py`, widoki: `warsztat.py`. |
| **Mój projekt** | Mentor zagląda do Twojego katalogu: czy są Python/Git/Claude Code w PATH, czy jest `CLAUDE.md` (może go utworzyć z zasadami), ostatni commit, czy dziś był commit, ile plików czeka bez commita, które pliki z zadań bieżącego tygodnia już istnieją. Przycisk **Otwórz Claude Code tutaj** otwiera terminal w katalogu projektu z uruchomionym `claude`. |
| **Asystent** | Trzy karty: **Subskrypcja** (Claude Code — status instalacji, komendy, otwarcie w projekcie), **API** (prawdziwy Claude przez klucz z console.anthropic.com, płatność za użycie; rozmowa w oknie, pliki przez `@nazwa.py`, zasady z CLAUDE.md i kontekst tygodnia w tle) oraz **Offline** (wbudowany emulator bez konta i internetu). |
| **Prompty** | 15 szablonów z dokumentu i etapów (Nowy temat, Utknąłem, Recenzja, Zatrzymaj się, Ja tłumaczę Twój kod, Ukryty błąd, Oczami rekrutera, Próbna rozmowa…) + treść `CLAUDE.md` + szablon bug raportu. „Wypełnij [nawiasy]” pyta o każdy nawias i kopiuje gotowy prompt. |
| **Quiz** | 59 pytań — 5 na tydzień 0–9, 3 na tygodnie 10–12 — z wyjaśnieniami. Błędne odpowiedzi trafiają do **powtórki** i wracają, aż odpowiesz dobrze. 100% = odznaka. Ekran wyniku w aplikacji (bez okienek): punkty, komentarz, **lekcje do powtórzenia** z przyciskami „Otwórz lekcję”, „Powtórz błędne pytania”. **Diagnoza na start** (jeśli program ją ma): kilka pytań z całego kursu, nie blokuje nauki, nie daje XP — wskazuje lekcje, przy których zwolnić. |
| **Dziennik** | Dwa zdania dziennie z losowym pytaniem mentora („Co dziś było najtrudniejsze?”). Pisanie o tym, czego się nauczyłeś, utrwala mocniej niż ponowne czytanie. |
| **Checklista** | Checklista postępów z dokumentu — odhaczasz tylko to, co robisz *bez pomocy Claude*. |
| **Ściąga** | Komendy Claude Code i Gita, linki do dokumentacji i stron do ćwiczeń Selenium. |
| **Ustawienia** | Imię, katalog projektu, **motyw**, eksport `POSTEPY.md` (do repo lub dla kogoś, kto Cię wspiera), reset. |

## Programy nauczania

Ustawienia → **Program nauczania**: lista programów z folderu `programy/`, przełączanie (postępy każdego programu zapisują się
osobno pod jego `id`), **„Wgraj program z pliku…”** (walidacja + kopia do `programy/`), „Zapisz pusty szablon programu”.
Format: `programy/FORMAT.md`.

Wbudowane programy (źródła w Pythonie z generatorami w `programy/zrodla/*/zbuduj.py`):

| Program | Plik | Co zawiera |
|---|---|---|
| **Python od zera → Junior QA** | `programy/python-junior-qa.json` | 13 tygodni (0–12), 65 zadań, 32 lekcje, projekt portfolio z pytest + Selenium |
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
- `program.py` — wczytywanie i walidacja programów JSON
- `asystent.py` — emulator offline (analiza kodu, uruchamianie, quiz, git) i klient API
- `wiedza_ogolna.py` — wbudowany słownik błędów Pythona (gdy program nie ma własnego)
- `motywy.py` — motywy kolorystyczne
- `programy/python-junior-qa.json` — wbudowany program; `programy/szablon-programu.json` — szkielet; `programy/FORMAT.md` — opis formatu
- `programy/zrodla/python_junior_qa/` — źródła programu w Pythonie (`tresc.py`, `jak.py`, `wiedza.py`, `lekcje_extra.py`, `zbuduj.py`)
- `programy/zrodla/kadry_i_place/` — źródła kursu kadrowego: `plan_tygodni.py` (harmonogram 16 tygodni — jedyne miejsce, które przypisuje lekcje i zadania do tygodni; limit 9 h/tydzień sprawdzany przy budowie), `tygodnie_*.py` (treść zadań), `lekcje_*.py` (treść lekcji), `wyjasnienia.py` (wyjaśnienia przepisane: krótkie zdania, nagłówki, tabele — `zbuduj.py` pilnuje, by żadna liczba ani przepis nie zginęły), `lekcja_delegacje.py` (lekcja o podróżach służbowych + bloki standardu), `standard_1..5.py` (bloki standardu pozostałych lekcji), `powtorki.py`, `diagnoza.py`, `quizy_dodatkowe.py`, `szablony.py`, `materialy.py` (paczka ZIP), `zbuduj.py` (składa JSON i liczy czas lekcji z objętości treści)
- `programy/STANDARD_KURSOW.md` — standard tworzenia kursów; `programy/materialy/kadry-i-place/` — paczka materiałów kursu (generowana)
- `kadry.py` — silnik obliczeń kadrowo-płacowych; `warsztat.py` — widoki Warsztatu
- `start_mentor.bat` — uruchamianie dwuklikiem na Windows
- `mentor_dane.json` — Twoje postępy (powstaje po pierwszym uruchomieniu)
