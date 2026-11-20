# Konta, plany i koszty: ile naprawdę kosztuje agent
Tydzień 4 · lekcja 13 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wybierasz jeden plan (albo ścieżkę bez konta), liczysz koszt miesięczny z VAT, rozumiesz limity 5-godzinne i tygodniowe oraz różnicę między subskrypcją a płatnością za tokeny (API).

**Po co mi to?** Źle dobrany plan to albo przepłacanie, albo blokada w połowie zadania. Klient zapyta też, ile kosztuje utrzymanie rozwiązania.

## Czego potrzebujesz
- Lekcja „Jak działa model AI” (tokeny).
- Decyzja budżetowa z planu nauki (zadanie v0z1).

## 1 · Wyjaśnienie od podstaw
### Dwa narzędzia, dwa ekosystemy
| | Claude Code (Anthropic) | Codex (OpenAI) |
|---|---|---|
| dostęp w planie | Pro, Max, Team, Enterprise; darmowy plan claude.ai NIE obejmuje Claude Code | ChatGPT Plus i wyższe: CLI, IDE, web; Free i Go — ograniczony dostęp tylko w aplikacji desktop (wdrażany stopniowo) |
| najtańszy pełny plan | Pro: 20 USD/mies. (17 USD przy płatności rocznej) | Plus: 20 USD/mies. |
| wyższe plany | Max 5x: 100 USD, Max 20x: 200 USD | Pro: od 100 USD |
| płatność za użycie | konto API (Console) — płacisz za tokeny | klucz API — płacisz za tokeny |
Ceny podano bez podatku (stan: listopad 2026). W Polsce dolicza się VAT 23%: 20 USD × 1,23 = 24,60 USD, czyli ok. 90–100 zł zależnie od kursu dolara. Ceny i nazwy planów zmieniają się kilka razy w roku — kalendarz aktualizacji kursu przypomina, kiedy sprawdzić strony cenników.
### Limity: okno 5-godzinne i tygodniowe
Subskrypcja to nie „bez limitu”. Oba narzędzia liczą użycie w oknach: krótkim (ok. 5 godzin) i tygodniowym. Po przekroczeniu Claude Code pokazuje komunikat o limicie sesji lub tygodnia i trzeba poczekać (albo dokupić użycie). W Claude Code stan limitów pokazuje polecenie `/usage`, w Codex — `/status`.
### Subskrypcja czy API?
- Subskrypcja: stała cena, limity. Dla nauki i małych projektów — prawie zawsze lepsza.
- API: płacisz za każdy token, bez sufitu. Dokumentacja Claude Code podaje, że w firmach średni koszt to ok. 13 USD na programistę na aktywny dzień, 150–250 USD miesięcznie. Dla początkującego to łatwa droga do niespodzianki na karcie.
### Co zużywa limit najszybciej
- Długie rozmowy (cały kontekst jest wysyłany za każdym razem) — tydzień 7.
- Ogólne polecenia („popraw cały projekt”) — agent czyta wszystko.
- Najmocniejszy model do prostych zadań (`/model` zmienia model).
### Decyzja dla kursu
- Wystarczy JEDEN plan: Claude Pro albo ChatGPT Plus. Lekcje pokazują oba narzędzia; zadania wykonasz tym, które masz.
- Kup na miesiąc, ustaw przypomnienie o odnowieniu, oceniaj po 2 tygodniach w `/usage` / `/status`.
- Ścieżka bez konta: każde zadanie z agentem ma zapis jego pracy z jednym celowo wstawionym błędem — ćwiczysz czytanie i poprawianie kodu agenta.
### Bezpieczeństwo konta
Włącz weryfikację dwuetapową (2FA) na koncie Anthropic/OpenAI i GitHub. Nie udostępniaj konta innym — dostęp do agenta to dostęp do Twoich plików.

## 2 · Demonstracja — krok po kroku
**Sprawdzenie cennika i decyzja w 10 minut**

```
Kalkulacja na kartce (kurs 3,80 zł/USD — wpisz aktualny):

Claude Pro: 20 USD × 1,23 VAT = 24,60 USD × 3,80 = 93,48 zł/mies.
4 miesiące kursu (tydzień 4–15, ok. 3 miesiące + zapas): ok. 280–375 zł.
Alternatywa API: 13 USD dziennie × 20 dni = 260 USD = ok. 990 zł/mies. bez VAT — dlatego dla nauki wybieramy subskrypcję.
```

1. Otwórz claude.com/pricing i chatgpt.com/codex/pricing (oficjalne strony). Zanotuj cenę najtańszego planu, który daje agenta w terminalu, i datę sprawdzenia.
2. Policz koszt z VAT i aktualnym kursem dolara (kurs średni NBP z nbp.pl). Zapisz w koszty.md.
3. Zadaj sobie pytanie: z którego ekosystemu już korzystasz (masz ChatGPT Plus? — wybierz Codex)? Jeśli żadnego — wybierz jeden i nie zmieniaj przez miesiąc.
4. Ustaw w kalendarzu przypomnienie 2 dni przed odnowieniem: „ocenić /usage — zostaję, zmieniam, rezygnuję?”.

✔ **Oczekiwany wynik:** Masz decyzję z kwotą w złotych, datą sprawdzenia ceny i przypomnieniem — bez dwóch planów „na zapas”.

## 3 · Jak to uruchomić
1. Przeglądarka → claude.com/pricing, chatgpt.com/codex/pricing.
2. Po zakupie: w Claude Code `/usage`, w Codex `/status`.

## W praktyce
- Koszt narzędzi wpisuj do wyceny dla klienta.
- Raz w miesiącu: /usage i decyzja o planie.

## 4 · Ćwiczenie prowadzone
Policz: (1) koszt planu za 20 USD z VAT 23% w dolarach, (2) w złotych przy kursie 3,80 zł/USD, (3) ile zapłacisz przez 3 miesiące. Czas: 15 minut.

📄 `cwiczenia/tydzien_04/konta_koszty_1.md` · rozwiązanie: `rozwiazania/tydzien_04/konta_koszty_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj: (1) masz już ChatGPT Plus, (2) nie masz żadnego planu i chcesz zacząć od Claude Code, (3) nie możesz teraz płacić, (4) ktoś radzi „weź klucz API, będzie taniej” — Ty uczysz się 2 godziny dziennie. Opcje: Codex w ramach Plus / Claude Pro / ścieżka bez konta / zostań przy subskrypcji. Czas: 15 minut.

📄 `cwiczenia/tydzien_04/konta_koszty_2.md` · rozwiązanie: `rozwiazania/tydzien_04/konta_koszty_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„You've hit your session limit” w środku zadania.**
  - Przyczyna: Wyczerpane okno 5-godzinne (długa sesja, duży kontekst).
  - Jak sprawdzić: `/usage` (Claude Code) albo `/status` (Codex).
  - Poprawka: Poczekaj do odnowienia okna; na przyszłość krótsze sesje, `/clear` między zadaniami (tydzień 7).
- ✘ **Claude Code po zalogowaniu mówi, że plan nie obejmuje dostępu.**
  - Przyczyna: Darmowy plan claude.ai nie obejmuje Claude Code.
  - Jak sprawdzić: Ustawienia konta na claude.ai → plan.
  - Poprawka: Pro lub wyższy albo konto API (Console); albo ścieżka bez konta.
- ✘ **Rachunek API wyższy niż subskrypcja.**
  - Przyczyna: Płatność za tokeny bez limitu.
  - Jak sprawdzić: Panel rozliczeń dostawcy.
  - Poprawka: Ustaw limit wydatków w panelu API albo wróć do subskrypcji.

## Pułapki
- Ceny w dolarach bez VAT — porównując oferty licz zawsze kwotę z VAT w złotych.
- Reklamy „najlepszego narzędzia” zmieniają się co miesiąc. Umiejętności z kursu (specyfikacja, testy, przegląd zmian) przenoszą się na każde narzędzie.

## Dodatkowe zadania
1. Zapisz w koszty.md decyzję z kwotą w złotych i datą sprawdzenia ceny.
2. Włącz 2FA na koncie dostawcy AI.
3. Ustaw przypomnienie przed odnowieniem planu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czy darmowy plan claude.ai daje Claude Code?**
  - Nie — potrzebny Pro, Max, Team, Enterprise albo konto API.
- **Czym różni się subskrypcja od API?**
  - Subskrypcja: stała cena z limitami okien; API: płatność za każdy token bez sufitu.
- **Jak sprawdzisz, ile limitu zostało?**
  - W Claude Code `/usage`, w Codex `/status`.

## Co potrafię teraz bez patrzenia na przykład?
Wybierasz jeden plan albo ścieżkę bez konta, liczysz koszt z VAT, rozumiesz okna limitów i dlaczego API nie jest „tańsze” dla początkującego.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Help Center — Using Claude Code with your Pro or Max plan (dostęp 19.11.2026) — <https://support.claude.com/en/articles/14552983>
- Ceny planów Claude 2026 — zestawienie (dupple.com, 2.11.2026) (dostęp 19.11.2026) — <https://dupple.com/learn/claude-code-pricing>
- Codex — Pricing (plany ChatGPT i dostęp do Codex) (dostęp 19.11.2026) — <https://chatgpt.com/codex/pricing/>
- Claude Code — Manage costs effectively (/usage, /context, /clear, /compact) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/costs>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ile planów płatnych potrzebujesz do kursu?
  - A) 0 — zawsze
  - B) 1 (albo ścieżka bez konta)
  - C) 2
  - D) 3
- 20 USD + VAT 23% to:
  - A) 20 USD
  - B) 23 USD
  - C) 24,60 USD
  - D) 26 USD
- Polecenie pokazujące limity w Claude Code:
  - A) /usage
  - B) /limits
  - C) /money
  - D) /help
- Dlaczego API bywa ryzykowne dla początkującego?
  - A) Jest wolniejsze
  - B) Płacisz za każdy token, bez sufitu
  - C) Nie działa na Windows
  - D) Wymaga Linuksa

Odpowiedzi: B, C, A, B
