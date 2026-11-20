# Rozmowa z AI: kontekst, przykłady, ograniczenia, format
Tydzień 2 · lekcja 9 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** piszesz prośbę do AI z pięciu części (cel, kontekst, przykłady, ograniczenia, format odpowiedzi) i prowadzisz rozmowę iteracyjnie zamiast jednym wielkim promptem.

**Po co mi to?** Jakość kodu od AI zależy najbardziej od jakości prośby — to Twoja główna „klawiatura” jako vibe codera.

## Czego potrzebujesz
- Darmowy czat AI (claude.ai lub chatgpt.com).
- Lekcja „Komunikat błędu”.

## 1 · Wyjaśnienie od podstaw
### Model wie tylko to, co mu powiesz
Dokumentacja Anthropic radzi traktować model jak bardzo zdolnego nowego pracownika bez kontekstu firmy: im dokładniej wyjaśnisz, czego chcesz i po co, tym lepszy wynik. Wytyczne OpenAI mówią to samo: jasne instrukcje, przykłady, podział złożonych zadań na kroki.
### Pięć części dobrej prośby
| część | pytanie | przykład |
|---|---|---|
| cel | co ma powstać? | funkcja lista_gosci.py: dodawanie gości i raport |
| kontekst | dla kogo, w czym, co już jest? | Python 3.12, Windows, początkujący; plik ma być prosty, bez bibliotek |
| przykłady | jakie wejście → jaki wynik? | dodaj_goscia(lista, "Anna", 2) → lista ma 1 element |
| ograniczenia | czego nie robić? | bez input() w funkcjach, bez zmiany nazw funkcji, polskie komunikaty |
| format | jak ma wyglądać odpowiedź? | cały plik w jednym bloku kodu + 3 zdania, jak go sprawdzić |
### Przykłady są najważniejsze
Dokumentacja Anthropic nazywa to „multishot prompting”: kilka przykładów wejście → wynik mówi modelowi więcej niż akapit opisu. Dla Ciebie mają drugi plus — przykłady to gotowe testy: po odpowiedzi sprawdzasz, czy program daje dokładnie te wyniki.
### Iteracja zamiast „promptu idealnego”
- Najpierw poproś o plan albo pytania: „Zanim napiszesz kod, zadaj mi do 5 pytań o niejasności”.
- Potem mały kawałek (jedna funkcja), uruchomienie, poprawka.
- Każda poprawka konkretna: „dla (7, 1) wychodzi 840, a ma być 756 — rabat nie działa na granicy 7 nocy”.
- Gdy rozmowa się „rozjeżdża” (model miesza wersje), zaczynasz nową z krótkim podsumowaniem ustaleń.
### Rola i poziom
„Jesteś cierpliwym mentorem Pythona; wyjaśniaj prosto, bo jestem początkujący” zmienia styl wyjaśnień. Rola nie zastąpi jednak konkretów z tabeli.
### Poproś o sprawdzalność
Dodawaj do każdej prośby: „podaj, jak mam sprawdzić, że działa (polecenie i oczekiwany wynik)” oraz „wypisz założenia, które przyjąłeś”. Założenia to miejsca, w których model zgadywał — tam szukasz błędów.
### Czego nie wklejać
Haseł, kluczy API, danych osobowych prawdziwych klientów, poufnych dokumentów firmy. Dane w kursie są fikcyjne — w pracy zastępujesz prawdziwe dane przykładowymi.

## 2 · Demonstracja — krok po kroku
**Ta sama prośba w trzech iteracjach**

```
Prośba z pięciu części (wklej do czatu w zadaniu tygodnia):

Cel: napisz plik lista_gosci.py z funkcjami dodaj_goscia(lista, imie, noce), liczba_gosci(lista) i raport(lista).
Kontekst: Python 3.12, Windows, uczę się — kod ma być prosty, bez bibliotek, z komentarzami po polsku.
Przykłady: po dodaj_goscia(l, "Anna", 2) lista ma element {"imie": "Anna", "noce": 2}; liczba_gosci(l) → 1; raport zwraca napis „Anna: 2 noce”.
Ograniczenia: bez input() w funkcjach; noce < 1 → ValueError; puste imię → ValueError.
Format: cały plik w jednym bloku kodu, potem lista założeń i polecenie do sprawdzenia.
```

1. Iteracja 0 (zła): „zrób listę gości”. Model daje program z input() w pętli, który pyta o gości bez końca — nie da się go przetestować.
2. Iteracja 1: wklejasz prośbę z pięciu części, ale najpierw dopisujesz: „zadaj do 5 pytań, zanim napiszesz kod”. Model pyta np., czy imiona mogą się powtarzać i jak liczyć gości — odpowiadasz.
3. Iteracja 2: model daje plik. Sprawdzasz przykłady (Uruchom + własne wywołania). Jeden nie działa: raport zwraca „Anna: 2 nocy”.
4. Iteracja 3: konkretna poprawka: „raport dla 2 nocy zwraca ‚2 nocy’, ma być ‚2 noce’; dla 1 — ‚1 noc’, dla 5 — ‚5 nocy’. Popraw tylko funkcję raport”. Działa.
5. Wnioski do dziennika: pytania modelu ujawniły luki w specyfikacji; przykłady złapały błąd odmiany.

✔ **Oczekiwany wynik:** Działający plik po 3 krótkich iteracjach i lista założeń, z których jedna (odmiana „noc/noce/nocy”) wymagała decyzji człowieka.

## 3 · Jak to uruchomić
1. Czat AI → nowa rozmowa → wklej prośbę z przykładu.
2. Odpowiedź → skopiuj kod do pliku w PRACA → ▶ Uruchom.

## W praktyce
- Szablon 5 części trzymaj w Ściądze → Prompty.
- „Zadaj pytania, zanim napiszesz kod” — najtańsza poprawa jakości.

## 4 · Ćwiczenie prowadzone
Oceń prośbę: „Napisz w Pythonie funkcję, która liczy cenę pobytu. Ma być dobra.” Których z pięciu części brakuje? Zaznacz dla każdej: jest / brak. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/rozmowa_z_ai_1.md` · rozwiązanie: `rozwiazania/tydzien_02/rozmowa_z_ai_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Model odpowiedział kodem, ale dla Twojego przykładu (7 nocy, 1 osoba) program wypisuje 840.0 zamiast 756.0. Która wiadomość jest najlepszą następną prośbą? (A) „Nie działa, popraw.” (B) „Dla (7, 1) jest 840.0, ma być 756.0 — rabat 10% od 7 nocy nie działa; popraw tylko warunek rabatu i pokaż zmienioną linię.” (C) „Napisz wszystko od nowa lepiej.” Ile założeń warto poprosić model wypisać po każdej odpowiedzi — zero czy wszystkie? Czas: 15 minut.

📄 `cwiczenia/tydzien_02/rozmowa_z_ai_2.md` · rozwiązanie: `rozwiazania/tydzien_02/rozmowa_z_ai_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Model pisze dużo więcej, niż prosiłeś (GUI, baza, logowanie).**
  - Przyczyna: Brak ograniczeń zakresu.
  - Jak sprawdzić: Czy prośba mówi, czego nie robić?
  - Poprawka: Dopisz „tylko X; bez interfejsu graficznego, bez bibliotek, maks. 40 linii”.
- ✘ **Każda poprawka psuje coś innego.**
  - Przyczyna: Za długa rozmowa, model miesza wersje plików.
  - Jak sprawdzić: Ile wersji kodu jest w rozmowie?
  - Poprawka: Nowa rozmowa: wklej aktualny plik + 3 zdania ustaleń + jedną prośbę.
- ✘ **Kod nie pasuje do Twojego Pythona/systemu (ścieżki /home/…, komendy Linuksa).**
  - Przyczyna: Brak kontekstu systemu.
  - Jak sprawdzić: Czy podałeś Windows i wersję Pythona?
  - Poprawka: Kontekst: „Windows 11, CMD, Python 3.12”.

## Pułapki
- Grzeczność nie szkodzi, ale nie zastępuje konkretów — „proszę, zrób to dobrze” nic nie mówi modelowi.
- Model chętnie się zgadza („Masz rację!”) nawet z błędną uwagą. Jeśli kwestionujesz wynik, poproś o sprawdzenie na przykładzie, a nie o przyznanie racji.

## Dodatkowe zadania
1. Przepisz jedną swoją wcześniejszą prośbę do AI na wersję z pięciu części i porównaj wyniki.
2. Poproś model o 5 pytań przed kodem w zadaniu tygodnia.
3. Zapisz w dzienniku 3 założenia, które model przyjął bez pytania.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie jest pięć części dobrej prośby?**
  - Cel, kontekst, przykłady wejście → wynik, ograniczenia, format odpowiedzi.
- **Dlaczego przykłady są tak ważne?**
  - Mówią modelowi najwięcej i jednocześnie są gotowymi testami do sprawdzenia odpowiedzi.
- **Co robisz, gdy rozmowa się rozjeżdża?**
  - Zaczynam nową rozmowę z aktualnym plikiem i krótkim podsumowaniem ustaleń.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz prośby z pięciu części, prosisz o pytania i założenia, poprawiasz iteracyjnie konkretnymi przypadkami i wiesz, czego nie wklejać.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Anthropic — Prompt engineering overview (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview>
- Anthropic — Be clear, direct, and detailed (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct>
- Anthropic — Use examples (multishot prompting) (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting>
- OpenAI — Prompt engineering guide (dokumentacja platformy) (dostęp 19.11.2026) — <https://platform.openai.com/docs/guides/prompt-engineering>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co najbardziej poprawia trafność kodu od AI?
  - A) Dłuższe podziękowania
  - B) Przykłady wejście → oczekiwany wynik
  - C) Wielkie litery
  - D) Prośba „zrób dobrze”
- Model po poprawce psuje inne rzeczy. Co robisz?
  - A) Piszę „źle!”
  - B) Nowa rozmowa z aktualnym plikiem i podsumowaniem
  - C) Kupuję droższy plan
  - D) Wyłączam komputer
- Po co prosić o listę założeń?
  - A) Żeby było dłużej
  - B) Bo pokazują, gdzie model zgadywał
  - C) Bo tak każe prawo
  - D) Nie warto
- Co nie powinno trafić do czatu AI?
  - A) Fikcyjne dane z kursu
  - B) Prawdziwy klucz API
  - C) Opis funkcji
  - D) Traceback z kursu

Odpowiedzi: B, B, B, B
