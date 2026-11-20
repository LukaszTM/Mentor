# Instrukcje projektu: AGENTS.md i CLAUDE.md — pamięć agenta
Tydzień 5 · lekcja 17 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** piszesz krótki AGENTS.md (cel projektu, polecenia, zasady, czego nie ruszać) i CLAUDE.md, który go importuje — tak, żeby Claude Code i Codex pracowały według tych samych reguł.

**Po co mi to?** Każda nowa sesja to agent bez pamięci. Plik instrukcji jest jak karta przekazania zmiany: bez niego powtarzasz te same ustalenia w każdej prośbie.

## Czego potrzebujesz
- Lekcja „Sesja z agentem”.
- Repozytorium/katalog PRACA z plikami z tygodni 1–3.

## 1 · Wyjaśnienie od podstaw
### Dwa pliki, jeden standard
| | AGENTS.md | CLAUDE.md |
|---|---|---|
| kto czyta | Codex (i wiele innych agentów); Claude Code — gdy nie ma CLAUDE.md | Claude Code |
| gdzie | katalog projektu (Codex: od korzenia repozytorium w dół do bieżącego folderu; globalnie ~/.codex/AGENTS.md) | ./CLAUDE.md lub ./.claude/CLAUDE.md; osobiste: ~/.claude/CLAUDE.md; prywatne lokalne: CLAUDE.local.md |
| szkielet | `/init` w Codex | `/init` w Claude Code |
| limit | domyślnie 32 KiB łącznie (project_doc_max_bytes) | zalecane poniżej 200 linii na plik |
Rekomendacja dokumentacji Claude Code dla projektów używających obu narzędzi: wspólne instrukcje w AGENTS.md, a CLAUDE.md zawiera linię `@AGENTS.md` (import pliku) i ewentualnie dodatki tylko dla Claude. Importy działają do 4 poziomów zagnieżdżenia.
### Co wpisać (i czego nie)
- Cel projektu w 2 zdaniach i dla kogo.
- Polecenia: jak uruchomić program i testy (`python -m pytest -q`).
- Konwencje: język komentarzy (polski), nazwy plików małymi literami, funkcje z return, input() tylko w bloku __main__.
- Zasady pracy: „najpierw plan”, „jedna zmiana naraz”, „po zmianie uruchom testy”, „nie zmieniaj testów, żeby przeszły”.
- Czego nie ruszać: folder WERYFIKATORY, dane klienta, plik .env.
- NIE wpisuj: haseł, kluczy, danych osobowych; długich instrukcji ogólnych („pisz dobry kod”) — to zużywa kontekst i nic nie daje.
### Instrukcje to prośba, nie blokada
Dokumentacja Claude Code: treść CLAUDE.md to kontekst dla modelu, nie wymuszenie. Model zwykle się stosuje, ale może zapomnieć. Twarde zakazy ustawia się w uprawnieniach (reguły deny w `.claude/settings.json`, `/permissions` — tydzień 12). Dlatego „nie czytaj .env” piszesz w instrukcjach ORAZ blokujesz regułą.
### Utrzymanie pliku
- Gdy agent dwa razy popełni ten sam błąd — dopisz jedną linię zasady.
- Co miesiąc usuń nieaktualne linie. Krótszy plik = lepiej przestrzegany i tańszy.
- W Claude Code `/memory` pokazuje, które pliki instrukcji są wczytane.
- AGENTS.md trafia do repozytorium (Git) — jest częścią projektu jak README.

## 2 · Demonstracja — krok po kroku
**Od /init do krótkiego, wspólnego pliku instrukcji**

```
# AGENTS.md — Pod Lipą (kurs vibe coding)

## Projekt
Narzędzia dla agroturystyki „Pod Lipą”: kalkulator ceny, lista gości, walidacja formularza. Dane fikcyjne.

## Polecenia
- testy: `python -m pytest -q`
- uruchomienie: `python <plik>.py`

## Zasady
- Najpierw plan w punktach, zmiany dopiero po akceptacji.
- Jedna funkcja na zmianę; po zmianie uruchom testy.
- Nie zmieniaj testów, żeby przeszły — zgłoś, jeśli test wydaje się błędny.
- Komentarze po polsku; input() tylko w bloku __main__.

## Nie ruszaj
- WERYFIKATORY/, dane/, .env

---
# CLAUDE.md
@AGENTS.md

## Tylko dla Claude Code
- Przy zadaniach > 1 pliku zacznij w trybie planu.
```

1. Claude Code w PRACA: `/init`. Agent czyta projekt i proponuje CLAUDE.md — długi, z opisem każdego pliku.
2. Zamiast przyjmować w całości: każesz przenieść wspólne zasady do AGENTS.md (5 sekcji z przykładu), a w CLAUDE.md zostawić `@AGENTS.md` i jedną linię tylko dla Claude.
3. Skracasz: usuwasz opisy plików, które agent i tak przeczyta, oraz ogólniki. Zostaje ok. 25 linii.
4. Nowa sesja (`/clear`), `/memory` — widzisz wczytane CLAUDE.md i zaimportowany AGENTS.md.
5. Test: prośba „dodaj funkcję do lista_gosci.py”. Agent sam zaczyna od planu i po zmianie uruchamia pytest — bo tak mówią instrukcje.
6. W Codex: nowa sesja w PRACA, `/status` — AGENTS.md jest wczytany; ta sama prośba, to samo zachowanie.

✔ **Oczekiwany wynik:** Jeden krótki AGENTS.md sterujący oboma agentami i CLAUDE.md z importem; zachowanie agentów zgodne z zasadami bez powtarzania ich w każdej prośbie.

## 3 · Jak to uruchomić
1. Claude Code: `/init`, `/memory`.
2. Codex: `/init`, `/status`.

## W praktyce
- AGENTS.md w każdym projekcie od pierwszego dnia.
- Przegląd instrukcji raz w miesiącu.

## 4 · Ćwiczenie prowadzone
Które linie NIE powinny trafić do AGENTS.md? (1) `testy: python -m pytest -q` (2) `klucz API pogody: abc123…` (3) `Nie zmieniaj testów, żeby przeszły` (4) `Pisz zawsze najlepszy możliwy kod` (5) `Nie ruszaj folderu WERYFIKATORY`. Podaj numery jako ciąg cyfr rosnąco (np. 13). Jaką jedną linię wpiszesz w CLAUDE.md, żeby Claude Code wczytał AGENTS.md? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/instrukcje_projektu_1.md` · rozwiązanie: `rozwiazania/tydzien_05/instrukcje_projektu_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Napisałeś w CLAUDE.md „nigdy nie czytaj pliku .env”, a agent i tak raz go otworzył. (1) Czy instrukcja w CLAUDE.md to wymuszenie (tak/nie)? (2) Gdzie ustawisz twardą blokadę — w CLAUDE.md, w regułach uprawnień, czy w README? (3) Ile linii dokumentacja zaleca nie przekraczać w CLAUDE.md? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/instrukcje_projektu_2.md` · rozwiązanie: `rozwiazania/tydzien_05/instrukcje_projektu_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Agent ignoruje część zasad.**
  - Przyczyna: Plik za długi albo zasady sprzeczne/ogólne.
  - Jak sprawdzić: `/memory` — czy plik jest wczytany? Ile ma linii?
  - Poprawka: Skróć do najważniejszych, konkretnych zasad; usuń sprzeczności.
- ✘ **Codex nie stosuje się do zasad z CLAUDE.md.**
  - Przyczyna: Codex czyta AGENTS.md, nie CLAUDE.md.
  - Jak sprawdzić: Czy zasady są w AGENTS.md?
  - Poprawka: Wspólne zasady w AGENTS.md, w CLAUDE.md tylko `@AGENTS.md`.
- ✘ **W repozytorium widać prywatne ścieżki i notatki.**
  - Przyczyna: Osobiste rzeczy w CLAUDE.md projektu.
  - Jak sprawdzić: Treść CLAUDE.md w Git.
  - Poprawka: Osobiste ustawienia w CLAUDE.local.md (dodaj do .gitignore) albo ~/.claude/CLAUDE.md.

## Pułapki
- „/init” generuje dobry początek, ale zwykle za długi — redaguj, nie akceptuj w całości.
- Instrukcje z pobranego cudzego repozytorium też są czytane przez agenta — przeczytaj AGENTS.md/CLAUDE.md, zanim uruchomisz agenta w obcym projekcie (tydzień 12).

## Dodatkowe zadania
1. Napisz AGENTS.md i CLAUDE.md dla PRACA (zadanie tygodnia).
2. Sprawdź /memory lub /status, że pliki są wczytane.
3. Dopisz jedną zasadę po błędzie agenta.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co CLAUDE.md zawiera @AGENTS.md?**
  - Żeby Claude Code wczytał wspólne instrukcje, z których korzysta też Codex.
- **Czy CLAUDE.md blokuje akcje agenta?**
  - Nie — to kontekst; blokady ustawia się w regułach uprawnień.
- **Czego nie wpisujesz do plików instrukcji?**
  - Haseł, kluczy, danych osobowych i ogólników.

## Co potrafię teraz bez patrzenia na przykład?
Piszesz krótki AGENTS.md z poleceniami, zasadami i zakazami, importujesz go w CLAUDE.md, wiesz, że instrukcje to kontekst, a blokady to uprawnienia.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — How Claude remembers your project (CLAUDE.md, @import, AGENTS.md) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/memory>
- Codex — Custom instructions with AGENTS.md (kolejność, limit 32 KiB) (dostęp 20.11.2026) — <https://learn.chatgpt.com/docs/agent-configuration/agents-md>
- Claude Code — Configure permissions (reguły allow/ask/deny, /permissions) (dostęp 20.11.2026) — <https://code.claude.com/docs/en/permissions>
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Codex czyta instrukcje projektu z pliku:
  - A) CLAUDE.md
  - B) AGENTS.md
  - C) README.md
  - D) .env
- Import pliku w CLAUDE.md:
  - A) #include AGENTS.md
  - B) @AGENTS.md
  - C) import AGENTS
  - D) <AGENTS.md>
- Polecenie Claude Code pokazujące wczytane pliki instrukcji:
  - A) /memory
  - B) /files
  - C) /rules
  - D) /agents
- Agent dwa razy popełnił ten sam błąd. Co robisz?
  - A) Zmieniam narzędzie
  - B) Dopisuję jedną konkretną zasadę do AGENTS.md
  - C) Wydłużam plik o ogólniki
  - D) Nic

Odpowiedzi: B, B, A, B
