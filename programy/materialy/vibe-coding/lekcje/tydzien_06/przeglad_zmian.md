# Przegląd zmian agenta: czytasz diff jak recenzent
Tydzień 6 · lekcja 21 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** czytasz diff zmian agenta i przechodzisz listę kontrolną 8 pytań (zakres, testy, nowe zależności, tajemnice, ukryte błędy) zanim zrobisz commit.

**Po co mi to?** Raport Veracode (2025): w 45% próbek kodu wygenerowanego przez modele były luki bezpieczeństwa. Przegląd zmian to moment, w którym je łapiesz — taniej niż u klienta.

## Czego potrzebujesz
- Lekcje „Git” i „Sesja z agentem”.
- Plik pomoc/diff_agenta.md z materiałów (zadanie tygodnia).

## 1 · Wyjaśnienie od podstaw
### Jak czytać diff
```
--- a/rabaty.py
+++ b/rabaty.py
@@ -14,7 +14,9 @@ def rabat(noce, osoby):
-    if noce >= 7:
+    if noce > 7:
         r += 10
```
- `---` stara wersja, `+++` nowa. `@@ -14,7 +14,9 @@` — fragment zaczyna się w linii 14.
- Linie z `-` usunięte, z `+` dodane, bez znaku — kontekst bez zmian.
- Gdzie oglądać: `git diff` (zmiany niezapisane), `git diff --staged` (w poczekalni), `/diff` w Codex, w Claude Code — okno zgody pokazuje zmianę przed zapisem; w VS Code — zakładka Source Control.
### Lista kontrolna 8 pytań (przed każdym commitem)
| # | pytanie | czerwona flaga |
|---|---|---|
| 1 | Czy zmiana dotyczy tylko tego, o co prosiłem? | zmienione pliki spoza zadania |
| 2 | Czy testy zostały zmienione? | usunięty test, osłabiony assert, `pytest.skip` — „naprawa” przez zmianę testu |
| 3 | Czy doszły nowe zależności (import, requirements)? | nieznana paczka — sprawdź na pypi.org, czy istnieje i kto ją wydaje |
| 4 | Czy w kodzie są tajemnice? | klucze, hasła, adresy z tokenem |
| 5 | Czy błędy nie są ukrywane? | `except: pass`, `except Exception: return None` bez komunikatu |
| 6 | Czy granice i przypadki brzegowe są zachowane? | `>=` → `>`, usunięte `raise ValueError` |
| 7 | Czy coś zostało usunięte bez powodu? | znikające funkcje, komentarze z ważną informacją |
| 8 | Czy rozumiem każdą dodaną linię? | linie „magiczne” — zapytaj agenta, zanim zatwierdzisz |
### Wielkość zmian ma znaczenie
Diff powyżej ok. 200 linii przestaje być czytany uważnie — przez ludzi i przez modele recenzujące. To kolejny argument za małymi krokami. Gdy agent oddał dużą zmianę, poproś: „podziel to na 3 commity tematycznie i opisz każdy”.
### Recenzja z pomocą AI — dodatek, nie zastępstwo
Codex ma `/review` (przegląd zmian w katalogu pod kątem zmian zachowania i brakujących testów); Claude Code możesz poprosić: „zrób przegląd diffu według tej listy 8 pytań”. Dobry pomysł: recenzja w NOWEJ sesji (agent, który pisał kod, chętniej go broni). Decyzja i tak należy do Ciebie.

## 2 · Demonstracja — krok po kroku
**Przegląd diffu z listą 8 pytań**

```
Fragment diffu od agenta (zadanie: „popraw komunikat błędu w czy_email”):

--- a/walidacja.py
+++ b/walidacja.py
-def czy_email(tekst):
-    t = (tekst or "").strip()
+import email_validator_pl
+
+def czy_email(tekst):
+    try:
+        return email_validator_pl.check(tekst)
+    except Exception:
+        return True
--- a/test_walidacja.py
+++ b/test_walidacja.py
-    assert czy_email("anna@") is False

Czerwone flagi: 3 (nieznana paczka), 5 (except zwraca True — każdy błąd = „poprawny e-mail”), 2 (usunięty test), 1 (zadanie dotyczyło komunikatu, nie logiki).
```

1. Agent zgłasza: „Gotowe, testy przechodzą”. Zanim uwierzysz: `git status` — zmienione 3 pliki, choć zadanie dotyczyło jednego.
2. `git diff` pliku z zadania: zmiana sensowna. Pytanie 6 — granica `>= 7` zachowana. OK.
3. `git diff` pliku testów: agent usunął assert dla przypadku brzegowego, „bo był sprzeczny”. Czerwona flaga 2.
4. `git diff` trzeciego pliku (requirements.txt): nowa paczka o nieznanej nazwie. Sprawdzasz na pypi.org — brak takiej paczki. Czerwona flaga 3 (możliwa halucynacja lub pułapka — tydzień 12).
5. Decyzja: `git restore test_rabaty.py requirements.txt`, commit tylko pliku z zadania. Do agenta: „Nie zmieniaj testów ani zależności; jeśli test wydaje się błędny — opisz dlaczego, nie usuwaj”. Dopisujesz tę zasadę do AGENTS.md.

✔ **Oczekiwany wynik:** Zatwierdzona tylko właściwa zmiana; usunięty test i zmyślona zależność odrzucone przed commitem.

## 3 · Jak to uruchomić
1. `git status` → `git diff <plik>` → lista 8 pytań → `git add <wybrane>` → commit.
2. Codex: `/diff`, `/review`.

## W praktyce
- Lista 8 pytań wisi obok monitora.
- Diff > 200 linii → poproś o podział.

## 4 · Ćwiczenie prowadzone
Przeczytaj diff z przykładu lekcji. Ile czerwonych flag z listy 8 pytań w nim jest? Który numer pytania dotyczy linii `except Exception: return True`? Czy zatwierdzisz tę zmianę w całości (tak/nie)? Czas: 20 minut.

📄 `cwiczenia/tydzien_06/przeglad_zmian_1.md` · rozwiązanie: `rozwiazania/tydzien_06/przeglad_zmian_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Diff ma linię `-    if noce >= 7:` i pod nią `+    if noce > 7:`. (1) Która wersja jest nowa? (2) Dla ilu nocy zmienia się wynik funkcji (podaj jedną liczbę)? (3) Którym poleceniem zobaczysz zmiany już dodane do poczekalni? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/przeglad_zmian_2.md` · rozwiązanie: `rozwiazania/tydzien_06/przeglad_zmian_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Commit zawiera zmiany, których nie przeglądałeś.**
  - Przyczyna: `git add .` po pracy agenta.
  - Jak sprawdzić: `git show --stat` ostatniego commita.
  - Poprawka: Dodawaj pliki po nazwie po przeglądzie; jeśli trzeba — `git revert HEAD`.
- ✘ **Testy zielone, ale klient zgłasza błąd.**
  - Przyczyna: Agent osłabił lub usunął test.
  - Jak sprawdzić: `git log -p -- test_*.py` — historia zmian testów.
  - Poprawka: Przywróć test, zasada „nie zmieniaj testów” w AGENTS.md, przegląd pytania 2 przy każdym commicie.

## Pułapki
- „Testy przechodzą” od agenta to informacja do sprawdzenia, nie zwolnienie z przeglądu.
- Recenzja AI w tej samej sesji, która napisała kod, łatwo przeoczy własne błędy — używaj nowej sesji.

## Dodatkowe zadania
1. Przejrzyj diff z materiałów listą 8 pytań (zadanie tygodnia).
2. Przed każdym commitem w tym tygodniu — lista 8 pytań.
3. Dopisz do AGENTS.md: „nie zmieniaj testów ani zależności bez pytania”.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co oznaczają + i - w diffie?**
  - Linie dodane i usunięte.
- **Dlaczego zmiana testu przez agenta to czerwona flaga?**
  - Bo może „naprawić” problem, osłabiając sprawdzenie zamiast poprawiać kod.
- **Jak sprawdzisz nową zależność?**
  - Na pypi.org: czy istnieje, kto ją wydaje, czy jest używana — i czy w ogóle jest potrzebna.

## Co potrafię teraz bez patrzenia na przykład?
Czytasz diff, przechodzisz listę 8 pytań, odrzucasz zmiany poza zakresem, osłabione testy, nieznane zależności i ukryte błędy przed commitem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Git — dokumentacja polecenia git diff (dostęp 19.11.2026) — <https://git-scm.com/docs/git-diff>
- Veracode — GenAI Code Security Report (30.07.2025): 45% próbek kodu z AI z lukami (dostęp 19.11.2026) — <https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/>
- Codex CLI — slash commands (/init, /diff, /status, /compact, /new, /review, /permissions) (dostęp 20.11.2026) — <https://developers.openai.com/codex/cli/slash-commands>
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Linia `-    raise ValueError(...)` w diffie oznacza:
  - A) Dodanie walidacji
  - B) Usunięcie walidacji
  - C) Komentarz
  - D) Nic
- Agent „naprawił” test, usuwając assert. Pytanie z listy:
  - A) 1
  - B) 2
  - C) 4
  - D) 8
- `except Exception: pass` w nowym kodzie to:
  - A) Dobra praktyka
  - B) Ukrywanie błędów
  - C) Szybsze działanie
  - D) Wymóg Pythona
- Gdzie najlepiej zlecić recenzję AI?
  - A) W tej samej sesji, która pisała kod
  - B) W nowej sesji
  - C) Nigdzie
  - D) Na forum

Odpowiedzi: B, B, B, B
