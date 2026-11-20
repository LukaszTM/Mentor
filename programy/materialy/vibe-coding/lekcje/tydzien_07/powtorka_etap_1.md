# Powtórka etapu 1 i mini-projekt z agentem: kalendarz dostępności
Tydzień 7 · lekcja 24 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** prowadzisz agenta przez mały projekt od specyfikacji, przez plan i małe kroki, do commitów na GitHubie — i oceniasz gotowość do budowania aplikacji.

**Po co mi to?** Etap 2 to większe aplikacje (strona, Flask, baza). Bez nawyku plan → krok → test → przegląd → commit będą się sypać.

## Czego potrzebujesz
- Wszystkie lekcje tygodni 4–7.
- Repozytorium pod-lipa na GitHubie.

## 1 · Wyjaśnienie od podstaw
### Lista kontrolna etapu 1
| umiejętność | sprawdzian |
|---|---|
| narzędzie | agent zainstalowany (albo ścieżka bez konta), znasz tryby i /rewind |
| instrukcje | AGENTS.md + CLAUDE.md z @AGENTS.md, krótkie i aktualne |
| małe kroki | plan w punktach, jedna zmiana, test po każdej |
| Git/GitHub | commit po każdym zielonym kroku, push, .gitignore z .env |
| przegląd | lista 8 pytań przed commitem |
| kontekst | /context, /clear, notatka stan.md |
| porażki | diagnoza zamiast pętli, reguła trzech |
### Mini-projekt: kalendarz.py
Gospodarstwo ma 3 pokoje: Lipowy, Dębowy, Klonowy. Rezerwacja to słownik `{"pokoj": "Lipowy", "od": "2026-12-20", "do": "2026-12-23"}` — daty jako napisy RRRR-MM-DD, `do` to dzień wyjazdu (noc z 22 na 23 jest ostatnia; tego dnia pokój może przyjąć nowego gościa).
- `noce(od, do)` → liczba nocy; do ≤ od → ValueError.
- `koliduje(a, b)` → True, gdy dwie rezerwacje tego samego pokoju nakładają się (wyjazd w dniu przyjazdu następnej NIE jest kolizją).
- `czy_wolny(rezerwacje, pokoj, od, do)` → True, gdy pokój wolny w całym okresie.
- `wolne_pokoje(rezerwacje, od, do)` → lista wolnych pokoi w kolejności Lipowy, Dębowy, Klonowy.
Moduł `datetime` (wbudowany) zamienia napis na datę: `date.fromisoformat("2026-12-20")`; różnica dat `.days` to liczba nocy.
### Proces (to jest sprawdzian, nie tylko kod)
- Tryb planu → plan 4 punktów → commit po każdym punkcie (min. 4 commity).
- Lista 8 pytań przed każdym commitem.
- push na GitHub; w dzienniku: liczba iteracji, porażki agenta, zasady dopisane do AGENTS.md.
Bez konta: zapis pracy agenta w przyklady/odpowiedzi_agenta/v7z3.md (z jednym błędem) — znajdź błąd testem, popraw, zrób te same commity.

## 2 · Demonstracja — krok po kroku
**Przypadki brzegowe kolizji — test w głowie przed agentem**

```
from datetime import date

od = date.fromisoformat("2026-12-20")
do = date.fromisoformat("2026-12-23")
print((do - od).days)
# nakładanie przedziałów [od, do): a.od < b.do and b.od < a.do
print(date(2026, 12, 20) < date(2026, 12, 25) and date(2026, 12, 23) < date(2026, 12, 23))

```

1. A: Lipowy 20–23.12, B: Lipowy 23–25.12. Wyjazd A = przyjazd B → nie kolizja (a.od < b.do: 20 < 25 prawda; b.od < a.do: 23 < 23 fałsz → False).
2. C: Lipowy 22–24.12 vs A → kolizja (20 < 24 i 22 < 23).
3. D: Dębowy 20–23.12 vs A → inny pokój — nie kolizja (warunek pokoju sprawdzasz pierwszy!).
4. E: Lipowy 18–26.12 vs A (obejmuje całą A) → kolizja.
5. Te 4 przypadki wpisujesz do specyfikacji przed prośbą do agenta. Jeśli agent użyje <= zamiast <, przypadek A–B to wyłapie.

✔ **Oczekiwany wynik:** Masz 4 przypadki brzegowe kolizji, które obejmują typowe błędy: <= zamiast <, brak sprawdzenia pokoju, przedział obejmujący.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „kalendarz.py” → tryb planu → kroki → „✔ Sprawdź wynik” → commity → push.

## W praktyce
- Przedziały dat zawsze półotwarte [od, do).
- Przypadki brzegowe przed prośbą do agenta.

## 4 · Ćwiczenie prowadzone
Policz: (1) noce("2026-12-28", "2027-01-02"), (2) czy koliduje Lipowy 20–23.12 z Lipowy 23–25.12 (tak/nie), (3) czy koliduje Lipowy 20–23.12 z Lipowy 21–22.12 (tak/nie). Czas: 15 minut.

📄 `cwiczenia/tydzien_07/powtorka_etap_1_1.md` · rozwiązanie: `rozwiazania/tydzien_07/powtorka_etap_1_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Samoocena procesu. Policz, ile commitów minimum wymaga mini-projekt (plan ma 4 punkty, commit po każdym). Który plik sprawdzisz na GitHubie, by upewnić się, że nie wysłałeś tajemnic (nazwa pliku z kluczami, której NIE powinno tam być)? I wynik `wolne_pokoje` dla rezerwacji [Lipowy 20–23.12] w okresie 21–22.12 — ile pokoi jest wolnych? Czas: 15 minut.

📄 `cwiczenia/tydzien_07/powtorka_etap_1_2.md` · rozwiązanie: `rozwiazania/tydzien_07/powtorka_etap_1_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Wyjazd w dniu przyjazdu wykrywany jako kolizja.**
  - Przyczyna: <= zamiast < w warunku nakładania.
  - Jak sprawdzić: Przypadek A–B z demonstracji.
  - Poprawka: Warunek przedziałów półotwartych: a.od < b.do and b.od < a.do.
- ✘ **Kolizja między różnymi pokojami.**
  - Przyczyna: Brak sprawdzenia pokoju.
  - Jak sprawdzić: Przypadek A–D.
  - Poprawka: Najpierw: jeśli pokoje różne → False.
- ✘ **„TypeError: '<' not supported between instances of 'str' and 'datetime.date'”.**
  - Przyczyna: Porównanie napisu z datą.
  - Jak sprawdzić: Typy zmiennych w warunku.
  - Poprawka: Zamieniaj napisy na daty date.fromisoformat() na początku funkcji.

## Pułapki
- Porównywanie dat jako napisów „RRRR-MM-DD” przypadkiem działa, ale „2026-12-5” (bez zera) już nie — zawsze konwertuj na date.
- Mini-projekt ocenia też proces: 1 commit z całością = proces niezaliczony, nawet przy zielonych testach.

## Dodatkowe zadania
1. Zbuduj kalendarz.py z agentem w 4 krokach i 4 commitach.
2. Samoocena etapu 1 (zadanie tygodnia).
3. Quiz tygodnia 7.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Kiedy dwie rezerwacje tego samego pokoju kolidują?**
  - Gdy a.od < b.do i b.od < a.do (wyjazd w dniu przyjazdu nie koliduje).
- **Dlaczego daty konwertujesz na obiekty date?**
  - Żeby poprawnie porównywać i liczyć różnice, niezależnie od zapisu napisu.
- **Co sprawdza mini-projekt poza kodem?**
  - Proces: plan, małe kroki, commity po każdym kroku, przegląd, push.

## Co potrafię teraz bez patrzenia na przykład?
Zbudowałeś z agentem moduł z datami i przypadkami brzegowymi, w małych krokach z commitami — i oceniłeś gotowość do etapu aplikacji.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — datetime: date.fromisoformat (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat>
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Pro Git (książka, wyd. 2, git-scm.com) — rozdz. 2: Podstawy Gita; dostępne tłumaczenie na polski (dostęp 19.11.2026) — <https://git-scm.com/book/pl/v2>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Rezerwacje Lipowy 10–12 i Lipowy 12–15:
  - A) Kolidują
  - B) Nie kolidują
  - C) Błąd
  - D) Zależy od godziny
- noce("2026-12-30", "2027-01-01") to:
  - A) 1
  - B) 2
  - C) 3
  - D) Błąd
- Minimalny proces mini-projektu to:
  - A) Jeden commit
  - B) Plan, kroki z testem, commit po każdym, push
  - C) Tylko testy
  - D) Tylko kod

Odpowiedzi: B, B, B
