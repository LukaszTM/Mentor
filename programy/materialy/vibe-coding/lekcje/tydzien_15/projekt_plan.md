# Projekt końcowy: plan, kamienie milowe i praca z agentem
Tydzień 15 · lekcja 46 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** planujesz projekt końcowy — mini system rezerwacji „Pod Lipą” albo własny projekt — z celem, funkcjami (MVP), kamieniami milowymi, ryzykami i kryteriami „Gotowe, gdy”, i prowadzisz agenta według tego planu.

**Po co mi to?** Projekt końcowy łączy wszystko z kursu i jest głównym elementem portfolio. Dobry plan to różnica między ukończonym projektem a porzuconym w połowie.

## Czego potrzebujesz
- Wszystkie lekcje tygodni 0–14.
- Repozytorium pod-lipa z CI.

## 1 · Wyjaśnienie od podstaw
### Dwie drogi
- Domyślna: „Pod Lipą — mini system rezerwacji” (specyfikacja poniżej, sprawdzana niezależnymi testami Mentora).
- Własny projekt (np. z Twojej branży): ten sam zakres jakości — plan, testy (≥ 10), CI, README, AGENTS.md, bezpieczeństwo — oceniany rubryką przez Ciebie, mentora lub rekrutera.
### Specyfikacja domyślna (plik system.py)
| funkcja | zachowanie |
|---|---|
| `create_app(sciezka_bazy=":memory:")` | aplikacja Flask z bazą SQLite rezerwacji |
| `GET /` | strona HTML z nazwą „Pod Lipą” |
| `POST /api/rezerwacje` (JSON: gosc, email, pokoj, od, do) | 201 i `{"id", "koszt"}`; złe dane (e-mail, pokój, daty) → 400; kolizja z istniejącą rezerwacją → 409 |
| `GET /api/rezerwacje` | 200 i lista rezerwacji (id, gosc, pokoj, od, do, koszt) — BEZ e-maili (minimalizacja danych) |
| `GET /api/wolne?od=&do=` | wolne pokoje według zapisanych rezerwacji |
| `DELETE /api/rezerwacje/<id>` | 204; nieznane id → 404 |
Koszt = suma cen pokoju za każdą noc według cennik.cena_pokoju(pokoj, miesiąc tej nocy). Moduły z kursu (walidacja, kalendarz, cennik) importujesz — nie kopiujesz.
### MVP i kamienie milowe
MVP (minimum viable product) — najmniejsza wersja, która spełnia cel. Kamienie milowe dla wersji domyślnej:
| # | kamień | gotowe, gdy |
|---|---|---|
| 1 | baza i zapis rezerwacji | POST zapisuje, testy 201/400 |
| 2 | kolizje i lista | 409 dla kolizji, GET bez e-maili |
| 3 | wolne pokoje i usuwanie | /api/wolne z bazy, DELETE 204/404 |
| 4 | jakość | ≥ 10 Twoich testów, CI zielone, README, bezpieczeństwo |
| 5 | wydanie | CHANGELOG, tag v1.0.0, prezentacja |
### Ryzyka
Zapisz 3–5 ryzyk z planem: „agent przepisze moduły z kursu” → zasada w AGENTS.md; „zabraknie limitu planu” → praca bez agenta nad testami i README; „kolizje dat — trudne przypadki” → testy brzegowe z tygodnia 7 przed kodem.
### Praca z agentem w projekcie
- Każdy kamień = osobna gałąź i PR z CI.
- Sesja zaczyna się od: AGENTS.md + plan_projektu.md + notatka stan.md.
- Najpierw testy kamienia (ze specyfikacji), potem implementacja „bez zmiany testów”.
- Po kamieniu: przegląd 8 pytań + tabela 6 dziur bezpieczeństwa, merge, notatka stanu.

## 2 · Demonstracja — krok po kroku
**Kamień 1 z agentem — testy najpierw**

```
# plan_projektu.md

## Cel
Mini system rezerwacji „Pod Lipą”: goście sprawdzają wolne pokoje i rezerwują; właścicielka widzi listę.

## Użytkownicy
- gość (rezerwuje), właścicielka (przegląda, usuwa)

## Funkcje (MVP)
- POST /api/rezerwacje z walidacją
- 409 dla kolizji
- GET /api/rezerwacje bez e-maili
- GET /api/wolne
- DELETE /api/rezerwacje/<id>

## Kamienie milowe
- K1 baza i zapis
- K2 kolizje i lista
- K3 wolne i usuwanie
- K4 jakość
- K5 wydanie

## Ryzyka
- agent kopiuje moduły zamiast importu → zasada w AGENTS.md

## Gotowe, gdy
- testy Mentora zielone, ≥ 10 moich testów, CI zielone, README, tag v1.0.0
```

1. Gałąź k1-zapis. Prośba (tryb planu): „Na podstawie plan_projektu.md napisz TYLKO testy test_system.py dla kamienia 1: POST poprawny → 201 i id; zły e-mail, nieznany pokój, do ≤ od → 400. Nie implementuj.”
2. Przegląd testów: czy przykłady są ze specyfikacji? Dopisujesz brakujący: pusty JSON → 400. Testy czerwone (brak system.py) — dobrze.
3. Prośba: „Zaimplementuj system.py tak, by przeszły testy kamienia 1; importuj walidacja, kalendarz, cennik; SQL tylko z ?; nie zmieniaj testów”.
4. Testy zielone, przegląd diffu (8 pytań + 6 dziur): koszt liczony za noc z miesiącem każdej nocy — sprawdzasz ręcznie rezerwację 30.11–2.12 (noc listopadowa po cenie niskiej, grudniowa po wysokiej).
5. PR, CI zielone, merge, notatka stan.md. Kamień 1 zamknięty.

✔ **Oczekiwany wynik:** Kamień 1 gotowy z testami napisanymi przed kodem, przeglądem bezpieczeństwa i zielonym CI; plan prowadzi kolejne sesje.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „plan_projektu.md” → „✔ Sprawdź wynik” (sekcje planu).
2. Każdy kamień: gałąź → testy → implementacja → PR → CI → merge.

## W praktyce
- Każdy projekt: MVP + kamienie + ryzyka na jednej stronie.
- Kamień = gałąź = PR.

## 4 · Ćwiczenie prowadzone
Koszt rezerwacji Lipowego od 2026-11-30 do 2026-12-02 według specyfikacji (cena za noc według miesiąca TEJ nocy; Lipowy: 180 zł w sezonie wysokim, 140 zł w niskim; grudzień — wysoki). Ile nocy? Ile kosztuje noc 30.11? Koszt łączny (zł)? Czas: 15 minut.

📄 `cwiczenia/tydzien_15/projekt_plan_1.md` · rozwiązanie: `rozwiazania/tydzien_15/projekt_plan_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj kod odpowiedzi API projektu: (1) POST z e-mailem „anna@”, (2) POST Lipowego 21–22.12, gdy istnieje Lipowy 20–23.12, (3) DELETE /api/rezerwacje/999 (brak), (4) poprawny POST. Opcje: 201, 400, 404, 409. Czy GET /api/rezerwacje zwraca e-maile gości (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_15/projekt_plan_2.md` · rozwiązanie: `rozwiazania/tydzien_15/projekt_plan_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Projekt „rozlewa się” — po tygodniu brak działającej wersji.**
  - Przyczyna: Za duży zakres, brak MVP i kamieni.
  - Jak sprawdzić: Czy kamień 1 jest zamknięty?
  - Poprawka: Utnij do MVP; kamień po kamieniu z merge.
- ✘ **Agent skopiował kalendarz.py do system.py.**
  - Przyczyna: Brak zasady importu.
  - Jak sprawdzić: Diff — duplikat kodu.
  - Poprawka: Zasada w AGENTS.md: „importuj moduły kursu, nie kopiuj”; cofnij i powtórz krok.

## Pułapki
- Własny projekt jest świetny do portfolio, ale musi mieć ten sam poziom jakości — bez testów i CI nie zastąpi wersji domyślnej.
- Nie dodawaj logowania, płatności, maili w MVP — to osobne, trudne tematy bezpieczeństwa.

## Dodatkowe zadania
1. Napisz plan_projektu.md (zadanie tygodnia).
2. Zrealizuj kamienie 1–4 (zadanie tygodnia).
3. Notatka stan.md po każdym kamieniu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co to jest MVP?**
  - Najmniejsza wersja produktu, która spełnia cel i daje się sprawdzić.
- **Dlaczego testy kamienia przed implementacją?**
  - Bo to umowa z agentem i dowód, że kamień jest skończony.
- **Dlaczego lista rezerwacji nie zawiera e-maili?**
  - Minimalizacja danych osobowych — API zwraca tylko to, co potrzebne.

## Co potrafię teraz bez patrzenia na przykład?
Masz plan projektu z MVP, kamieniami, ryzykami i kryteriami, a każdy kamień prowadzisz przez testy, agenta, przegląd, PR i CI.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Atlassian — Acceptance criteria (dostęp 20.11.2026) — <https://www.atlassian.com/work-management/project-management/acceptance-criteria>
- GitHub Docs — About READMEs (dostęp 20.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Kolizja rezerwacji w API — kod:
  - A) 400
  - B) 404
  - C) 409
  - D) 500
- Kamień milowy jest zamknięty, gdy:
  - A) Agent napisze „gotowe”
  - B) Spełnia kryteria, testy i CI zielone, merge zrobiony
  - C) Minie tydzień
  - D) Kod jest długi
- Moduły z kursu w projekcie:
  - A) Kopiujesz do jednego pliku
  - B) Importujesz
  - C) Przepisujesz od nowa
  - D) Usuwasz

Odpowiedzi: C, B, B
