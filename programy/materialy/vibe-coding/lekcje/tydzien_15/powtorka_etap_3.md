# Podsumowanie kursu: Twój proces, mapa dalszej nauki i plan utrzymania wiedzy
Tydzień 15 · lekcja 48 z 48 · ≈ 45 min

**Po tej lekcji potrafisz:** masz spisany własny proces pracy z agentami (jedna strona), plan nauki na 3 miesiące i plan sprawdzania zmian w narzędziach, cenach i przepisach.

**Po co mi to?** Narzędzia AI zmieniają się co kilka tygodni; proces i nawyki zostają. Kurs kończy się, praca dopiero zaczyna.

## Czego potrzebujesz
- Projekt końcowy wydany (albo w ostatnim kamieniu).
- Dziennik z całego kursu.

## 1 · Wyjaśnienie od podstaw
### Twój proces na jednej stronie (wzór)
| faza | Twój nawyk |
|---|---|
| zlecenie | wymagania z kryteriami, poza zakresem, pytania |
| specyfikacja | 7 sekcji, przykłady i brzegi |
| testy | ze specyfikacji, przed kodem, sprawdzone mutantem |
| agent | AGENTS.md, tryb planu, małe kroki, notatka stanu, /clear |
| przegląd | 8 pytań + 6 dziur bezpieczeństwa, recenzja AI w nowej sesji |
| Git | gałąź, PR, CI, merge tylko na zielono |
| sekrety i dane | zmienne środowiskowe, deny, dane fikcyjne, RODO |
| wydanie | lista kontrolna, CHANGELOG, tag, retrospektywa |
### Co sprawdzać regularnie (kalendarz w Ściądze)
- Ceny i limity planów (co kwartał) — strony cenników Anthropic i OpenAI.
- Nowe wersje Claude Code i Codex (`claude --version`, `codex --version`, informacje o zmianach) — tryby uprawnień i domyślne ustawienia się zmieniają.
- AI Act: 2.12.2026 (koniec okresu przejściowego art. 50), 2.12.2027 (wysokie ryzyko, załącznik III).
- Limit działalności nierejestrowanej — co roku w styczniu (zależy od minimalnego wynagrodzenia).
- Zależności projektów — raz na kwartał aktualizacja z testami.
### Dalsza nauka (wybierz jedną ścieżkę na 3 miesiące)
| cel | następny krok |
|---|---|
| tester / QA | kurs „Python od zera → Junior QA” w Mentorze, pytest głębiej, Selenium |
| aplikacje webowe | szablony Jinja, formularze, autoryzacja (z dużą ostrożnością), hosting PaaS |
| dane i automatyzacje | pandas, Excel z Pythona (openpyxl), API usług w Twojej branży |
| zlecenia | 1 płatne małe zlecenie z pełnym procesem (wymagania → wydanie) |
### Ostatnia rada
Najważniejsza umiejętność z kursu to nie żadne polecenie, tylko pytanie: „Skąd wiem, że to działa?”. Zadawaj je agentowi, sobie i każdemu narzędziu.

## 2 · Demonstracja — krok po kroku
**Przegląd dziennika z 16 tygodni**

```
Fragment proces.md:

# Mój proces pracy z agentami
1. Wymagania → potwierdzenie klienta.
2. Specyfikacja z 6+ przykładami.
3. Testy ze specyfikacji (czerwone).
4. Agent w trybie planu: punkt po punkcie, test po każdym.
5. Przegląd: 8 pytań + 6 dziur; recenzja AI w nowej sesji.
6. PR → CI → merge.
7. Raz na kwartał: ceny, wersje narzędzi, zależności.
```

1. Przeglądasz wpisy „czego nie rozumiem” — 3 tematy powtarzają się (np. daty, SQL, CI). To lista do dalszej nauki.
2. Liczysz iteracje z agentem na zadanie: tydzień 4 — średnio 5, tydzień 11 — średnio 2. Dowód postępu do rozmowy rekrutacyjnej.
3. Najczęstsze porażki agenta z Twojego dziennika → 3 nowe linie do szablonu AGENTS.md na kolejne projekty.
4. Spisujesz proces na jedną stronę i plan 3 miesięcy z jednym celem.

✔ **Oczekiwany wynik:** Proces na jednej stronie, szablon AGENTS.md z doświadczeń, plan nauki i kalendarz sprawdzania zmian.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „proces.md i plan 3 miesięcy”.
2. Ściąga → kalendarz aktualizacji.

## W praktyce
- proces.md przy biurku.
- Kwartalny przegląd: ceny, wersje, zależności.

## 4 · Ćwiczenie prowadzone
Uporządkuj fazy procesu: A) przegląd, B) specyfikacja, C) testy, D) wydanie, E) wymagania, F) agent w małych krokach. Ciąg liter. Czas: 15 minut.

📄 `cwiczenia/tydzien_15/powtorka_etap_3_1.md` · rozwiązanie: `rozwiazania/tydzien_15/powtorka_etap_3_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Kalendarz: (1) do kiedy trwa okres przejściowy art. 50 AI Act (data), (2) jak często sprawdzasz ceny planów (opcje: co tydzień / co kwartał / raz w życiu), (3) kiedy sprawdzasz limit działalności nierejestrowanej (opcje: w styczniu / w lipcu / nigdy). Czas: 15 minut.

📄 `cwiczenia/tydzien_15/powtorka_etap_3_2.md` · rozwiązanie: `rozwiazania/tydzien_15/powtorka_etap_3_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Po kursie wracasz do „kopiuj-wklej bez testów”.**
  - Przyczyna: Brak spisanego procesu i szablonów.
  - Jak sprawdzić: Czy masz proces.md i szablony?
  - Poprawka: Szablony (specyfikacja, AGENTS.md, PR) w Mentorze → Ściąga; proces na jednej stronie przy biurku.
- ✘ **Instrukcje z kursu przestały pasować do nowej wersji narzędzia.**
  - Przyczyna: Zmiany w narzędziach (tryby, polecenia).
  - Jak sprawdzić: Wersja narzędzia i informacje o zmianach.
  - Poprawka: Kalendarz aktualizacji; zasady (testy, przegląd, sekrety) są niezależne od wersji.

## Pułapki
- Nie goń każdego nowego narzędzia — sprawdzaj je na tej samej specyfikacji i testach, którymi oceniasz obecne.
- Ucz się dalej czytania kodu — to umiejętność, której AI nie zastąpi Ci na rozmowie i przy odbiorze.

## Dodatkowe zadania
1. Napisz proces.md i plan 3 miesięcy (zadanie tygodnia).
2. Przejrzyj dziennik i zapisz 3 wnioski.
3. Ustaw przypomnienia z kalendarza aktualizacji.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie pytanie jest najważniejsze w vibe codingu?**
  - „Skąd wiem, że to działa?”
- **Co sprawdzasz co kwartał?**
  - Ceny i limity planów, wersje narzędzi, zależności projektów.
- **Jak wybierasz dalszą naukę?**
  - Jedna ścieżka na 3 miesiące, z konkretnym celem i projektem.

## Co potrafię teraz bez patrzenia na przykład?
Masz własny proces pracy z agentami na jednej stronie, plan dalszej nauki i kalendarz sprawdzania zmian — kurs zamknięty, nawyki zostają.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Stack Overflow Developer Survey 2025 — AI (zaufanie, vibe coding w pracy zawodowej) (dostęp 19.11.2026) — <https://survey.stackoverflow.co/2025/ai>
- Rozporządzenie (UE) 2026/1744 („Digital Omnibus” dla AI Act) — EUR-Lex (dostęp 24.11.2026) — <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Pierwsza faza procesu przy zleceniu:
  - A) Agent
  - B) Wymagania z kryteriami
  - C) Wydanie
  - D) CI
- Nowe narzędzie AI sprawdzasz:
  - A) Na nowym, ciekawym projekcie bez testów
  - B) Na tej samej specyfikacji i testach co obecne
  - C) Czytając reklamy
  - D) Wcale
- Umiejętność, której AI nie zastąpi na rozmowie:
  - A) Pisanie promptów
  - B) Czytanie i wyjaśnianie kodu
  - C) Instalacja
  - D) Kopiowanie

Odpowiedzi: B, B, B
