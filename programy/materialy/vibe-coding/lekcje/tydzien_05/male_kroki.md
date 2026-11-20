# Małe kroki: plan → jedna zmiana → test → zapis
Tydzień 5 · lekcja 18 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** dzielisz zadanie na kroki po jednej zmianie, prowadzisz agenta krok po kroku z testem po każdym i wiesz, kiedy zatrzymać sesję.

**Po co mi to?** Dokumentacja Claude Code (Best practices) zaleca: najpierw eksploracja i plan, potem kod, i zawsze sposób weryfikacji. Duże prośby dają duże, niesprawdzalne zmiany.

## Czego potrzebujesz
- Lekcje „Sesja z agentem” i „Instrukcje projektu”.

## 1 · Wyjaśnienie od podstaw
### Dlaczego małe kroki
Zmiana w 1 funkcji = 10 linii do przejrzenia i jeden test. Zmiana w 6 plikach = 300 linii i nie wiesz, która linia zepsuła rabat. Małe kroki obniżają też koszt: agent czyta mniej, a błąd cofasz jednym ruchem.
### Rytm jednego kroku
| faza | Twoja prośba / działanie |
|---|---|
| 1. Eksploracja | „Przeczytaj X i Y, powiedz, jak działa Z. Nie zmieniaj plików.” |
| 2. Plan | „Zaproponuj plan w punktach dla [cel]. Każdy punkt = jedna zmiana z testem.” |
| 3. Krok | „Zrób tylko punkt 1. Potem uruchom testy i pokaż wynik.” |
| 4. Sprawdzenie | czytasz zmianę (diff), testy Mentora, własny przykład |
| 5. Zapis | od tygodnia 6: commit z opisem; do tego czasu — checkpoint i kopia |
Potem punkt 2 — i tak dalej. Po 3–5 krokach albo przy zmianie tematu: `/clear` (Claude Code) albo `/new` (Codex) i nowa sesja.
### Jak podzielić zadanie
- Po funkcjach: każda funkcja ze specyfikacji to krok.
- Po warstwach: najpierw logika (funkcje + testy), potem wejście/wyjście (pliki, formularz), na końcu wygląd.
- Po przypadkach: najpierw przypadek podstawowy, potem brzegowe.
### Sygnały, że krok jest za duży
- Agent proponuje zmiany w więcej niż 2 plikach naraz.
- Nie umiesz w jednym zdaniu powiedzieć, co ten krok zmienia.
- Agent pracuje dłużej niż kilka minut bez pokazania wyniku.
### Weryfikacja wpisana w prośbę
Każda prośba kończy się kryterium: „Gotowe, gdy test_konwerter przechodzi” albo „Gotowe, gdy dla "1 234,56 zł" funkcja zwraca 1234.56”. Agent, który ma sposób sprawdzenia, sam uruchamia test i poprawia się, zanim odda pracę.

## 2 · Demonstracja — krok po kroku
**Jedno zadanie, dwie strategie**

```
Plan dla konwerter.py (zadanie tygodnia), zatwierdzony w trybie planu:

1. parsuj_kwote(tekst) — „1 234,56 zł” → 1234.56; test 5 przykładów.
2. Złe dane w parsuj_kwote („abc”, „”) → ValueError; test.
3. zl_na_eur(kwota, kurs) — zaokrąglenie do centów; ValueError dla kursu ≤ 0 i kwoty < 0; test.
4. formatuj_zl(kwota) → „1 234,56 zł”; test.
Po każdym punkcie: testy Mentora + przegląd zmian.
```

1. Strategia A: „Napisz konwerter.py ze wszystkimi funkcjami ze specyfikacji”. Agent tworzy 120 linii, testy: 3 z 9 czerwone, w trzech różnych funkcjach. Naprawa wymaga 4 kolejnych rund.
2. Strategia B (tryb planu): plan 4 punktów jak w przykładzie. „Zrób punkt 1 i uruchom testy” — 15 linii, zielone dla parsuj_kwote (pozostałe czerwone, bo funkcji jeszcze nie ma — to oczekiwane).
3. Punkt 2: agent dodaje ValueError. Przeglądasz 6 linii zmian. Punkt 3 i 4 analogicznie.
4. Porównanie w dzienniku: A — 5 rund i 120 linii czytania na raz; B — 4 rundy po 10–20 linii, każdy błąd złapany w miejscu powstania.

✔ **Oczekiwany wynik:** Strategia małych kroków daje tyle samo kodu, ale każdą zmianę rozumiesz i weryfikujesz od razu.

## 3 · Jak to uruchomić
1. Claude Code: Shift + Tab → plan; po każdym kroku `python -m pytest -q` lub „✔ Sprawdź wynik”.
2. Codex: „najpierw plan, nie zmieniaj plików” → „zrób punkt 1” → /diff.

## W praktyce
- Plan w punktach to część dokumentacji zadania — zapisz go w specyfikacji.
- Jedna sesja = jeden temat.

## 4 · Ćwiczenie prowadzone
Podziel na kroki prośbę: „Dodaj do lista_gosci.py usuwanie gościa, wyszukiwanie po imieniu i zapis listy do pliku CSV, i popraw raport, żeby był posortowany”. Ile niezależnych zmian (kroków) zawiera ta prośba? Który krok zrobisz OSTATNI według zasady „najpierw logika, potem wejście/wyjście”? Opcje: usuwanie, wyszukiwanie, zapis do CSV, sortowanie raportu. Czas: 15 minut.

📄 `cwiczenia/tydzien_05/male_kroki_1.md` · rozwiązanie: `rozwiazania/tydzien_05/male_kroki_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które sygnały oznaczają „krok za duży”? (1) agent chce zmienić 5 plików, (2) zmiana dotyczy jednej funkcji i jednego testu, (3) nie umiesz w jednym zdaniu powiedzieć, co zmienia krok, (4) agent pracuje 12 minut bez wyniku. Podaj liczbę sygnałów „za duży” i jedną komendę Claude Code, którą zaczniesz nową sesję po zakończeniu tematu. Czas: 15 minut.

📄 `cwiczenia/tydzien_05/male_kroki_2.md` · rozwiązanie: `rozwiazania/tydzien_05/male_kroki_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Agent „przy okazji” refaktoryzuje sąsiednie funkcje.**
  - Przyczyna: Brak granicy kroku w prośbie.
  - Jak sprawdzić: Czy prośba mówi „tylko punkt 1”?
  - Poprawka: „Zrób tylko punkt 1, nie zmieniaj innych funkcji”; zasada w AGENTS.md.
- ✘ **Testy czerwone po kroku, nie wiesz dlaczego.**
  - Przyczyna: Krok obejmował kilka zmian.
  - Jak sprawdzić: Diff kroku.
  - Poprawka: Cofnij (/rewind lub git restore) i podziel krok.

## Pułapki
- Mały krok nie znaczy „bez planu”. Plan całości robisz raz na początku — i aktualizujesz.
- Czerwone testy funkcji, których jeszcze nie ma, są w porządku w trakcie planu — ważne, by zielone były te z bieżącego kroku.

## Dodatkowe zadania
1. Zbuduj konwerter.py w 4 krokach z planem (zadanie tygodnia).
2. Zapisz w dzienniku porównanie z prośbą „wszystko naraz”.
3. Dopisz do AGENTS.md zasadę „jeden punkt planu na raz”.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie są fazy jednego kroku?**
  - Eksploracja, plan, jedna zmiana, sprawdzenie, zapis.
- **W jakiej kolejności dzielisz pracę po warstwach?**
  - Logika z testami, potem wejście/wyjście, na końcu wygląd.
- **Kiedy zaczynasz nową sesję?**
  - Po 3–5 krokach albo przy zmianie tematu.

## Co potrafię teraz bez patrzenia na przykład?
Dzielisz zadania na kroki z testem po każdym, rozpoznajesz krok za duży i zamykasz sesję we właściwym momencie.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Claude Code — Permission modes (default, acceptEdits, plan, auto…) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/permission-modes>
- Claude Code — Manage costs effectively (/usage, /context, /clear, /compact) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/costs>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Najlepsza pierwsza prośba do nowego zadania:
  - A) Napisz wszystko
  - B) Przeczytaj pliki i zaproponuj plan, nie zmieniaj plików
  - C) Uprość projekt
  - D) Zrób to szybko
- Sygnał, że krok jest za duży:
  - A) Zmiana 1 funkcji
  - B) Agent chce zmienić 5 plików naraz
  - C) Jeden test
  - D) Krótki diff
- Każda prośba powinna kończyć się:
  - A) Podziękowaniem
  - B) Kryterium „Gotowe, gdy…”
  - C) Emoji
  - D) Nazwą modelu
- Nowa rozmowa w Codex:
  - A) /new
  - B) /clear
  - C) /restart
  - D) /init

Odpowiedzi: B, B, B, A
