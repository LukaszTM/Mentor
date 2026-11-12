# START TUTAJ — Kadry i płace: kurs zaawansowany (praktyka 2026)

**Wersja kursu:** 2.0 · stan prawny: listopad 2026 · format `mentor-program/1`
**Poziom:** od podstaw — bez znajomości prawa pracy, księgowości i arkuszy kalkulacyjnych.
**Czas:** 12 tygodni × 5 dni × 60–90 minut.
**System:** Windows 10/11 (Mentor.exe); działa też z Pythonem 3.10+ na innych systemach.
**Potrzebujesz:** 60–90 minut dziennie przez 12 tygodni; jeden folder na dysku na pliki ćwiczeń; Mentor (ten program) — nic więcej: żadnych kont, instalacji ani arkuszy; internet niepotrzebny.
**Nie potrzebujesz:** internetu (kurs i Asystent offline działają bez sieci), kont w eZUS/e-Urzędzie (w Mentorze są symulatory), Excela, Pythona, żadnych instalacji poza samym Mentorem.

## Co będziesz umieć po kursie
- zawrzeć i rozwiązać umowę o pracę z kompletem dokumentów i w terminach
- policzyć wymiar czasu pracy, nadgodziny, nocne, urlop i pensję za część miesiąca
- sporządzić i skontrolować listę płac od brutto do netto (PPK, chorobowe, zasiłek, benefity, potrącenia)
- ustalić podstawę zasiłku, rozliczyć zleceniobiorcę, przygotować komplet DRA/RCA/RSA i korektę
- zamknąć rok (PIT-4R, PIT-11, ZFŚS, PFRON) i przygotować firmę do kontroli PIP/ZUS z procedurami 2026/2027

## Pierwsze 30 minut (krok po kroku)
1. **Rozpakuj ZIP** do zwykłego folderu, np. `C:\Users\<Ty>\Mentor` (ścieżka może mieć spacje i polskie znaki). Nie uruchamiaj z wnętrza archiwum.
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
