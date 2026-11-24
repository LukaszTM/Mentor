# Jak uczyć się z tego kursu — czym jest vibe coding
Tydzień 0 · lekcja 1 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** wiesz, co zbudujesz w 16 tygodni, ile to kosztuje, jak działa każdy dzień nauki i czym różni się „vibe coding” od programowania na ślepo.

**Po co mi to?** Zanim powierzysz komputer agentowi AI, musisz wiedzieć, co jest Twoją pracą (cel, sprawdzenie, decyzja), a co pracą agenta (pisanie kodu).

## Czego potrzebujesz
- Mentor uruchomiony na Windows 10/11 (ten program) — nic więcej w tym tygodniu.
- Ok. 80 minut dziennie od poniedziałku do piątku i do 90 minut w sobotę; razem ok. 120 godzin przez 16 tygodni (każdy tydzień mieści się w 9 godzinach).
- Konta i płatne subskrypcje NIE są potrzebne do tygodnia 4 — wtedy zdecydujesz, czy kupujesz plan (lekcja „Konta, plany i koszty”).

## 1 · Wyjaśnienie od podstaw
### Co to jest vibe coding
W lutym 2025 r. Andrej Karpathy (współzałożyciel OpenAI) opisał nowy sposób tworzenia programów: mówisz komputerowi zwykłym językiem, co ma powstać, a model AI pisze kod. Nazwał to „vibe coding” i dodał: „to nie jest tak naprawdę programowanie — widzę rzeczy, mówię rzeczy, uruchamiam rzeczy, kopiuję i wklejam, i to przeważnie działa” (tłumaczenie robocze). W listopadzie 2025 r. słownik Collins wybrał „vibe coding” słowem roku.
Kluczowe słowo w tym cytacie to „przeważnie”. Ten kurs uczy wersji, która działa NIE przeważnie, tylko sprawdzalnie: AI pisze kod, a Ty mówisz, co ma powstać, sprawdzasz wynik testami i decydujesz, co zostaje.
### Dwa style — i który wybieramy
| styl | jak wygląda | kiedy wystarczy |
|---|---|---|
| vibe coding „na ślepo” | prosisz, wklejasz, nie czytasz, nie testujesz | zabawa, jednorazowy prototyp na własnym komputerze |
| vibe coding odpowiedzialny (ten kurs) | opisujesz cel i kryteria, agent pisze, Ty czytasz zmiany, uruchamiasz testy, zapisujesz wersję w Git | wszystko, co ma działać jutro, dla klienta albo z prawdziwymi danymi |
### Co mówią dane (żeby nie wierzyć reklamom)
- Ankieta Stack Overflow 2025 (ponad 49 tys. programistów): 84% używa albo planuje używać AI, ale 46% nie ufa dokładności jego odpowiedzi.
- Badanie METR (lipiec 2025): doświadczeni programiści na własnych, dużych projektach pracowali z AI o 19% wolniej, choć byli przekonani, że szybciej.
- Wniosek dla Ciebie: AI daje ogromną przewagę na starcie i przy prostych aplikacjach, ale bez sprawdzania tworzy błędy, których nie widać od razu.
### Co zbudujesz
Przez cały kurs pracujesz dla fikcyjnego klienta: gospodarstwa agroturystycznego „Pod Lipą” (dane wymyślone). Kolejno powstaną: kalkulator ceny pobytu, lista gości, strona internetowa z kalkulatorem, raport z rezerwacji (CSV), aplikacja internetowa z bazą danych, skrypt porządkujący pliki i — w tygodniu 15 — mały system rezerwacji z testami, dokumentacją i publikacją w GitHub. Każdy element sprawdzają niezależne testy z paczki kursu, których agent nie może zmienić.
### Etapy
| etap | tygodnie | po etapie potrafisz |
|---|---|---|
| 0. Fundamenty | 0–3 | poruszać się po plikach i terminalu, czytać prosty kod Pythona, rozumieć komunikat błędu, napisać specyfikację i dostać od AI działający program |
| 1. Agent przy pracy | 4–7 | zainstalować i bezpiecznie używać Claude Code i Codex, prowadzić projekt w Git i GitHub, czytać zmiany agenta, zarządzać kontekstem i kosztem |
| 2. Budujesz aplikacje | 8–11 | zlecać kod pod testy, debugować z AI, budować stronę, aplikację Flask z bazą, raporty z danych, automatyzacje i bezpiecznie używać kluczy API |
| 3. Jakość i zawód | 12–15 | zabezpieczać kod i agenta, znać prawo (prawo autorskie, RODO, AI Act), robić przegląd kodu, CI, README, rozmawiać z klientem, przygotować portfolio i projekt końcowy |
### Jak wygląda dzień
- Panel → zadanie dnia. Lekcja (zakładka Lekcje) — czytasz wyjaśnienie i demonstrację, potem dwa ćwiczenia z polami „Twoje odpowiedzi”: Mentor sprawdza każde pole i nie zdradza wyniku.
- Zadanie dnia z paskiem „Ćwiczenie w Mentorze”: plik powstaje w Twoim katalogu roboczym (Dokumenty\Mentor\vibe-coding\PRACA), „✔ Sprawdź wynik” uruchamia NIEZALEŻNE testy z paczki kursu.
- Sobota: quiz tygodnia i powtórka. Niedziela wolna.
- Dziennik: 3 zdania — co zbudowałem, co sprawdziłem, czego nie rozumiem.
### Ile to kosztuje
Tygodnie 0–3: 0 zł (Mentor, Python i darmowe czaty AI). Od tygodnia 4 agent kodujący wymaga płatnego planu: Claude Pro to 20 USD miesięcznie bez podatku (z VAT ok. 90–100 zł, zależnie od kursu), ChatGPT Plus (Codex) — także 20 USD. Wystarczy JEDEN z nich. Każde zadanie z agentem ma też ścieżkę bez płatnego konta: gotowy zapis pracy agenta z celowo wstawionym błędem, który znajdujesz i poprawiasz. Ceny zmieniają się — kalendarz aktualizacji w Ściądze przypomina, kiedy je sprawdzić.
### Twoja rola: kierownik budowy, nie murarz
Agent jest jak bardzo szybki pracownik, który nigdy nie był na Twojej budowie. Ty odpowiadasz za: (1) cel i granice („co ma powstać, czego nie ruszać”), (2) sprawdzenie („skąd wiem, że działa”), (3) decyzję („zostawiam czy cofam”). Tego nie da się zlecić — i właśnie tego uczy ten kurs.

## 2 · Demonstracja — krok po kroku
**Jedna prośba, dwa podejścia — co się zmienia**

```
Specyfikacja, którą w tygodniu 4 dasz agentowi (zobacz, jak mało w niej „kodu”):

Cel: plik kalkulator_pobytu.py z funkcją koszt_pobytu(noce, osoby).
Zasady: 120 zł za osobę za noc; od 7 nocy rabat 10%; noce lub osoby mniejsze niż 1 → ValueError.
Przykłady: koszt_pobytu(2, 2) → 480.0; koszt_pobytu(7, 1) → 756.0.
Nie ruszaj: innych plików w katalogu.
Gotowe, gdy: przechodzą testy Mentora (✔ Sprawdź wynik).
```

1. Podejście „na ślepo”: piszesz do czatu „zrób mi kalkulator ceny noclegu”. Dostajesz kod, kopiujesz, działa dla jednego przykładu. Nie wiesz, co z rabatem, ujemną liczbą nocy, groszami.
2. Podejście kursu: najpierw zapisujesz specyfikację (powyżej): cel, zasady, przykłady wejście → wynik, czego nie ruszać, jak sprawdzisz.
3. Agent pisze kod. Ty NIE zaczynasz od czytania kodu, tylko od sprawdzenia: czy przykłady ze specyfikacji dają dokładnie te wyniki? Mentor uruchamia testy i pokazuje ✔ albo listę przypadków, które nie przechodzą.
4. Gdy coś nie przechodzi — nie piszesz „nie działa, popraw”. Wklejasz agentowi KONKRETNY przypadek: „koszt_pobytu(7, 1) zwraca 840.0, a powinno 756.0 — rabat od 7 nocy nie działa”.
5. Na końcu zapisujesz wersję (od tygodnia 6 — commit w Git) i jedno zdanie w dzienniku: co sprawdziłeś.

✔ **Oczekiwany wynik:** Ten sam agent, ten sam model — ale w drugim podejściu wiesz, że program działa, i umiesz to pokazać klientowi lub rekruterowi.

## 3 · Jak to uruchomić
1. Panel → „Pierwsze kroki” → zadanie diagnostyczne (8 pytań, nie blokuje nauki — pokazuje lekcje do powtórki).
2. Plan nauki → tydzień 0 → przeczytaj zadania na cały tydzień (3–4 min).
3. Mój projekt → „📁 Utwórz katalog roboczy kursu” (Mentor założy Dokumenty\Mentor\vibe-coding\PRACA) → „📂 Skopiuj materiały kursu tutaj”.

## W praktyce
- Każde zlecenie dla AI zaczynaj od zdania „Gotowe, gdy…”.
- Zapisuj, co sprawdziłeś — rekruter i klient zapytają właśnie o to.

## 4 · Ćwiczenie prowadzone
Przeczytaj opis etapów i dnia nauki. Odpowiedz w polach poniżej: ile tygodni trwa kurs, w którym tygodniu zaczynasz pracę z płatnym agentem i ile planów płatnych naprawdę potrzebujesz (Claude Pro albo ChatGPT Plus). Czas: 15 minut.

📄 `cwiczenia/tydzien_00/start_vibe_1.md` · rozwiązanie: `rozwiazania/tydzien_00/start_vibe_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Zdecyduj o swoim rytmie. Otwórz Dziennik i zapisz: w jakie dni i o której godzinie się uczysz, ile minut, oraz co zrobisz, gdy opuścisz dzień. Potem oceń trzy sytuacje: czy to vibe coding „na ślepo”, czy odpowiedzialny? Czas: 20 minut.

📄 `cwiczenia/tydzien_00/start_vibe_2.md` · rozwiązanie: `rozwiazania/tydzien_00/start_vibe_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„Nie mam czasu na lekcje, od razu każę AI zrobić całą aplikację”.**
  - Przyczyna: Pokusa skrótu — agent naprawdę potrafi wygenerować dużo kodu.
  - Jak sprawdzić: Czy umiesz powiedzieć, skąd wiesz, że ta aplikacja działa?
  - Poprawka: Zacznij od małego kawałka ze specyfikacją i testem; dużą aplikację budujesz w tygodniu 15 — z kamieniami milowymi.
- ✘ **„Panel pokazuje zaległości z trzech dni”.**
  - Przyczyna: Przerwa w nauce.
  - Jak sprawdzić: Plan nauki → bieżący tydzień.
  - Poprawka: Nie nadrabiaj wszystkiego: jedna lekcja + jedno zadanie dziennie; Mentor nie karze za przerwy.
- ✘ **„Kupiłem od razu dwa plany i Max”.**
  - Przyczyna: Obawa, że jeden nie wystarczy.
  - Jak sprawdzić: Lekcja „Konta, plany i koszty” (tydzień 4).
  - Poprawka: Zacznij od jednego planu za 20 USD; limity widzisz w /usage (Claude Code) — podnoś plan dopiero, gdy limit naprawdę blokuje pracę.

## Pułapki
- Vibe coding nie znaczy „nie musisz nic rozumieć” — znaczy „nie musisz pisać każdej linijki sam”. Rozumieć, co program robi i jak to sprawdzić, musisz zawsze.
- Dane klienta w kursie są fikcyjne. Nigdy nie wklejaj do AI prawdziwych danych osobowych, haseł ani kluczy (tydzień 12).

## Dodatkowe zadania
1. Przeczytaj w Planie nauki tytuły wszystkich 16 tygodni i zaznacz w dzienniku 2 tematy, które budzą największe obawy.
2. Zapytaj darmowy czat AI: „Czym jest vibe coding i jakie są jego ryzyka?” — porównaj odpowiedź z tą lekcją i zapisz jedną różnicę.
3. Zapisz w dzienniku jedno zdanie: po co mi ten kurs (praca, własny projekt, klient).

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jaka jest Twoja rola, gdy kod pisze agent?**
  - Ustalam cel i granice, sprawdzam wynik (testy, przykłady) i decyduję, co zostaje — agent pisze kod.
- **Dlaczego komunikat agenta „gotowe” nie jest dowodem?**
  - To deklaracja modelu; dowodem jest uruchomienie programu i przejście testów na przykładach ze specyfikacji.
- **Ile kosztuje kurs w tygodniach 0–3?**
  - 0 zł — Mentor, Python i darmowe czaty AI; płatny agent jest potrzebny dopiero od tygodnia 4 (i jest ścieżka bez konta).

## Co potrafię teraz bez patrzenia na przykład?
Wiesz, co zbudujesz, ile to kosztuje i jak wygląda dzień; rozumiesz różnicę między vibe codingiem na ślepo a odpowiedzialnym: cel → agent → sprawdzenie → decyzja.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Collins: „vibe coding” słowem roku 2025; cytat A. Karpathy’ego z lutego 2025 (tech.co, 6.11.2025) (dostęp 19.11.2026) — <https://tech.co/news/vibe-coding-word-of-year-2025>
- Stack Overflow Developer Survey 2025 — AI (84% używa, 46% nie ufa dokładności) (dostęp 19.11.2026) — <https://survey.stackoverflow.co/2025/ai>
- METR (10.07.2025): Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity — badanie RCT, z AI 19% wolniej (dostęp 24.11.2026) — <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
- Claude Code — przewodnik po terminalu dla nowych użytkowników (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/terminal-guide>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co w tym kursie jest dowodem, że kod działa?
  - A) Komunikat agenta „Done!”
  - B) Przejście testów na przykładach ze specyfikacji
  - C) Długość kodu
  - D) To, że model jest najnowszy
- Badanie METR z 2025 r. wykazało, że doświadczeni programiści z AI na własnych projektach:
  - A) Byli 2× szybsi
  - B) Pracowali o 19% wolniej, choć sądzili, że szybciej
  - C) Nie zauważyli różnicy
  - D) Przestali używać AI
- Od którego tygodnia kursu potrzebny jest płatny agent (lub ścieżka bez konta)?
  - A) 0
  - B) 2
  - C) 4
  - D) 12
- Co znaczy „odpowiedzialny vibe coding”?
  - A) Nie używam AI
  - B) Opisuję cel i kryteria, agent pisze, ja sprawdzam testami i decyduję
  - C) Kopiuję kod z czatu
  - D) Proszę AI o recenzję zamiast testów

Odpowiedzi: B, B, C, B
