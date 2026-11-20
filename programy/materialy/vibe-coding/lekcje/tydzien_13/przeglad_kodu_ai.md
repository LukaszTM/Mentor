# Przegląd kodu jak w zespole: pull request, recenzja AI i Twoja decyzja
Tydzień 13 · lekcja 40 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** pracujesz na gałęziach i pull requestach, robisz przegląd według listy (poprawność, testy, bezpieczeństwo, czytelność, zakres), używasz recenzji AI jako drugiej pary oczu i piszesz komentarze, które da się wykonać.

**Po co mi to?** W firmie każdy kod — także od AI — przechodzi przegląd przed włączeniem do głównej gałęzi. Umiejętność recenzji jest bardziej poszukiwana niż umiejętność generowania kodu.

## Czego potrzebujesz
- Lekcje „Przegląd zmian agenta” i „Bezpieczeństwo kodu”.
- Repozytorium pod-lipa na GitHubie.

## 1 · Wyjaśnienie od podstaw
### Gałąź i pull request
- `git switch -c funkcja/rabat-lojalnosciowy` — nowa gałąź na zmianę.
- Commity na gałęzi, `git push -u origin funkcja/rabat-lojalnosciowy`.
- GitHub → „Compare & pull request”: tytuł, opis (co, dlaczego, jak sprawdzić), prośba o przegląd.
- Po akceptacji: Merge → main. Gałąź usuwasz.
Pull request (PR) to miejsce rozmowy o zmianie: komentarze przy liniach, wyniki testów CI (tydzień 13), historia poprawek.
### Na co patrzy recenzent (wytyczne Google Engineering Practices, skrót)
| obszar | pytania |
|---|---|
| projekt | czy zmiana pasuje do reszty, czy to dobre miejsce? |
| funkcjonalność | czy robi to, co opisano, także na brzegach? |
| złożoność | czy da się prościej? czy ktoś zrozumie za miesiąc? |
| testy | czy są, czy sprawdzają coś sensownego, czy nie zostały osłabione? |
| nazwy i komentarze | czy nazwy mówią, co robią; czy komentarze wyjaśniają „dlaczego”? |
| bezpieczeństwo | 6 dziur z lekcji tygodnia 12 |
| zakres | tylko to, co w opisie — bez „przy okazji” |
### Recenzja AI — jak jej używać
Codex `/review` przegląda zmiany pod kątem zmian zachowania i brakujących testów; Claude Code poprosisz: „Zrób przegląd diffu gałęzi względem main według tej listy; dla każdej uwagi: plik, linia, waga (blokujące/sugestia), propozycja”. Zasady: recenzja w NOWEJ sesji (nie tej, która pisała kod); traktuj uwagi jak hipotezy — część będzie fałszywa; ostateczna decyzja i odpowiedzialność są Twoje.
### Komentarz, który da się wykonać
Zły: „to jest źle”. Dobry: „[blokujące] `rabat.py:14` — dla 3. pobytu (granica) funkcja zwraca 0, specyfikacja mówi 3%. Proponuję `>= 3` i test `test_trzeci_pobyt_ma_rabat`”. Oznaczaj wagę: blokujące / sugestia / pytanie / pochwała (tak — mówienie, co jest dobre, też jest częścią recenzji).
### Opis PR (szablon)
„Co: … Dlaczego: … Jak sprawdzić: polecenie + oczekiwany wynik. Ryzyka: … Powstało z AI: tak/nie, co przejrzałem ręcznie: …”

## 2 · Demonstracja — krok po kroku
**Przegląd PR z pomocą AI — co przyjąć, co odrzucić**

```
Opis pull requesta:

**Co:** rabat lojalnościowy 3% od 3. pobytu (funkcja rabat_lojalnosciowy, użycie w do_zaplaty).
**Dlaczego:** prośba klientki z 12.12 (wymagania.md, US-4).
**Jak sprawdzić:** `python -m pytest -q` → 31 passed; ręcznie: do_zaplaty(3, 2, 1, pobyty=3) → 213,40 zł.
**Ryzyka:** łączenie z rabatem za długi pobyt — limit 15% zachowany (test_limit_rabatu).
**AI:** kod z Claude Code; przejrzałem wszystkie linie, testy napisałem ze specyfikacji.
```

1. Gałąź funkcja/rabat-lojalnosciowy, PR na GitHubie. Uruchamiasz recenzję AI w nowej sesji z listą obszarów.
2. AI zgłasza 5 uwag: (1) brak testu dla 3. pobytu — trafne; (2) „użyj dataclass zamiast słownika” — sugestia poza zakresem; (3) „możliwy SQL injection” w pliku bez SQL — fałszywy alarm; (4) magiczna liczba 0.03 — trafne; (5) opis PR nie wspomina limitu 15% — trafne.
3. Przyjmujesz 1, 4, 5 (komentarze w PR z wagą), 2 zapisujesz jako pomysł na później, 3 odrzucasz z uzasadnieniem.
4. Poprawki na gałęzi, testy zielone, merge.

✔ **Oczekiwany wynik:** PR z 3 trafnymi poprawkami z recenzji AI, jedną sugestią odłożoną i jednym fałszywym alarmem odrzuconym — decyzja po Twojej stronie.

## 3 · Jak to uruchomić
1. `git switch -c funkcja/nazwa` → commity → `git push -u origin funkcja/nazwa` → GitHub: Compare & pull request.
2. Codex: `/review`; Claude Code: prośba o przegląd diffu w nowej sesji.

## W praktyce
- Jedna zmiana = jedna gałąź = jeden PR.
- Opis PR z „Jak sprawdzić”.

## 4 · Ćwiczenie prowadzone
Recenzja AI zgłosiła: (1) „brak testu dla granicy 3 pobytów” w PR o rabacie od 3. pobytu, (2) „podatność XSS” w pliku, który nie generuje HTML, (3) „zmień nazwę zmiennej x na liczba_pobytow”. Dla każdej: przyjmuję / odrzucam. Którą oznaczysz jako blokującą (numer)? Czas: 15 minut.

📄 `cwiczenia/tydzien_13/przeglad_kodu_ai_1.md` · rozwiązanie: `rozwiazania/tydzien_13/przeglad_kodu_ai_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Ułóż polecenia pracy z gałęzią w kolejności: A) `git push -u origin funkcja/x`, B) `git switch -c funkcja/x`, C) utworzenie PR na GitHubie, D) commity na gałęzi, E) merge po akceptacji. Podaj ciąg liter. Czas: 15 minut.

📄 `cwiczenia/tydzien_13/przeglad_kodu_ai_2.md` · rozwiązanie: `rozwiazania/tydzien_13/przeglad_kodu_ai_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **PR ma 40 plików i 2 000 linii.**
  - Przyczyna: Wiele tematów naraz albo przepisanie przez agenta.
  - Jak sprawdzić: Files changed w PR.
  - Poprawka: Podziel na kilka PR po jednym temacie; formatowanie osobno.
- ✘ **Recenzja AI „zatwierdziła” błąd.**
  - Przyczyna: Recenzja w tej samej sesji albo bez listy kryteriów.
  - Jak sprawdzić: Kto i jak recenzował?
  - Poprawka: Nowa sesja, lista obszarów, testy — i Twoja recenzja jako ostatnia.

## Pułapki
- Recenzja AI nie jest dowodem jakości — to lista hipotez.
- Nie łącz (merge) PR z czerwonymi testami CI, nawet „na chwilę”.

## Dodatkowe zadania
1. Zrób PR z jedną zmianą i przegląd według listy (zadanie tygodnia).
2. Użyj recenzji AI w nowej sesji i oceń trafność uwag.
3. Napisz opis PR według szablonu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co gałąź i pull request?**
  - Żeby zmiana została przejrzana i przetestowana, zanim trafi do main.
- **Jak traktujesz uwagi recenzji AI?**
  - Jak hipotezy: sprawdzam, przyjmuję trafne, odrzucam fałszywe z uzasadnieniem.
- **Jak wygląda dobry komentarz w recenzji?**
  - Waga, plik i linia, konkretny problem, propozycja poprawki lub testu.

## Co potrafię teraz bez patrzenia na przykład?
Pracujesz na gałęziach i PR, recenzujesz według listy, używasz recenzji AI jako drugiej pary oczu i piszesz wykonalne komentarze.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Google Engineering Practices — What to look for in a code review (dostęp 20.11.2026) — <https://google.github.io/eng-practices/review/reviewer/looking-for.html>
- GitHub Docs — About pull requests (dostęp 20.11.2026) — <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
- Codex CLI — slash commands (/review) (dostęp 20.11.2026) — <https://developers.openai.com/codex/cli/slash-commands>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Nowa gałąź i przełączenie:
  - A) git switch -c nazwa
  - B) git branch-new
  - C) git push -b
  - D) git make
- Recenzję AI najlepiej uruchomić:
  - A) W sesji, która pisała kod
  - B) W nowej sesji z listą kryteriów
  - C) Wcale
  - D) Po merge
- Dobry komentarz recenzji zawiera:
  - A) „Źle”
  - B) Wagę, miejsce, problem i propozycję
  - C) Emoji
  - D) Tylko pochwałę
- PR z czerwonymi testami:
  - A) Merge, poprawię później
  - B) Nie łączymy do main
  - C) Usuwamy testy
  - D) Zmieniamy gałąź

Odpowiedzi: A, B, B, B
