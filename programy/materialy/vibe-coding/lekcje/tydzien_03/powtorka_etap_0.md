# Powtórka etapu 0 i mini-projekt: rabaty sezonowe
Tydzień 3 · lekcja 12 z 48 · ≈ 55 min

**Po tej lekcji potrafisz:** samodzielnie (z czatem AI) budujesz mały moduł rabaty.py od specyfikacji do zielonego testu i oceniasz, czy jesteś gotowy na agenta.

**Po co mi to?** Etap 1 daje Ci agenta, który zmienia pliki sam. Bez pewnych podstaw z etapu 0 nie odróżnisz dobrej zmiany od złej.

## Czego potrzebujesz
- Wszystkie lekcje tygodni 0–3.
- Quiz tygodnia 3 (sobota).

## 1 · Wyjaśnienie od podstaw
### Co już umiesz (lista kontrolna)
| umiejętność | sprawdzian |
|---|---|
| pliki i ścieżki | wiesz, gdzie jest PRACA, widzisz rozszerzenia |
| terminal | cd, dir, mkdir, type, python plik.py, Ctrl + C |
| czytanie kodu | przewidujesz wynik funkcji z if, for, listą i słownikiem |
| błędy | czytasz traceback od dołu, znasz 8 wyjątków |
| rozmowa z AI | 5 części prośby, iteracje, reguła trzech |
| specyfikacja | 7 sekcji, przypadki brzegowe, kryteria tak/nie |
### Mini-projekt: rabaty.py
Gospodarstwo „Pod Lipą” ma cennik sezonowy. Specyfikacja (pełna w zadaniu tygodnia):
- `sezon(miesiac)` → "wysoki" dla 6, 7, 8 i 12; "niski" dla pozostałych 1–12; inna liczba → ValueError.
- `cena_nocy(miesiac)` → 150 zł w sezonie wysokim, 110 zł w niskim (za osobę).
- `rabat(noce, osoby)` → procent rabatu: 10 od 7 nocy, 5 dla 4+ osób, rabaty SUMUJĄ SIĘ (7 nocy i 4 osoby → 15), maksymalnie 15.
- `do_zaplaty(miesiac, noce, osoby)` → kwota po rabacie, zaokrąglona do groszy.
### Jak się ocenić
- Ile iteracji z AI potrzebowałeś? (1–3 dobrze, 4+ — wróć do lekcji „Specyfikacja”).
- Czy umiesz wyjaśnić każdą linię? (jeśli nie — lekcje „Czytanie kodu” 1–2).
- Czy czytasz traceback bez pomocy? (jeśli nie — „Komunikat błędu”).
- Quiz tygodnia 3 ≥ 70%? Jeśli nie, Mentor wskaże lekcje do powtórki.
### Co dalej
Tydzień 4: decyzja o planie (koszty), instalacja Claude Code i Codex. Jeśli nie kupujesz planu — przechodzisz kurs ścieżką z zapisami pracy agenta; umiejętności są te same: czytanie, sprawdzanie, poprawianie.

## 2 · Demonstracja — krok po kroku
**Specyfikacja → test w głowie dla rabat()**

```
def sezon(miesiac):
    if miesiac not in range(1, 13):
        raise ValueError("miesiąc 1–12")
    return "wysoki" if miesiac in (6, 7, 8, 12) else "niski"

print(sezon(7), sezon(3), sezon(12))

```

1. Wypisujesz przykłady z reguł: (3, 2) → 0; (7, 2) → 10; (3, 4) → 5; (7, 4) → 15; (14, 6) → 15 (maks.).
2. Brzegowe: (6, 3) → 0 (tuż przed obiema granicami); (7, 3) → 10; (6, 4) → 5.
3. Prosisz czat o rabaty.py z tymi przykładami. Dostajesz funkcję rabat z if/elif: if noce >= 7: return 10 / elif osoby >= 4: return 5.
4. Twój przykład (7, 4) → oczekujesz 15, kod daje 10: elif nie pozwala zsumować rabatów — to dokładnie błąd, który złapałby test.
5. Konkretna poprawka: „rabaty się sumują: dwa niezależne if dodające do zmiennej, na końcu min(wynik, 15)”. Test w głowie: (7, 4) → 10 + 5 = 15 ✔.

✔ **Oczekiwany wynik:** Złapałeś błąd logiczny (elif zamiast sumowania) jeszcze przed uruchomieniem — dzięki przykładom ze specyfikacji.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „Mini-projekt: rabaty.py” → „📝 Utwórz plik ćwiczenia” → czat AI → „✔ Sprawdź wynik”.

## W praktyce
- Przed każdym etapem — lista kontrolna umiejętności.
- Przykłady kombinacji (7 nocy + 4 osoby) łapią błędy logiki.

## 4 · Ćwiczenie prowadzone
Policz według specyfikacji mini-projektu: (1) rabat(7, 4), (2) rabat(10, 2), (3) do_zaplaty(7, 7, 2) — lipiec, 7 nocy, 2 osoby (150 zł/os./noc, rabat 10%). Czas: 15 minut.

📄 `cwiczenia/tydzien_03/powtorka_etap_0_1.md` · rozwiązanie: `rozwiazania/tydzien_03/powtorka_etap_0_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Samoocena gotowości. Odpowiedz uczciwie: (1) czy potrafisz bez pomocy przeczytać traceback i wskazać linię? (2) ile iteracji potrzebowałeś w kalkulator_pobytu? Następnie policz: miesiąc 13 w sezon() — co powinno się stać (nazwa wyjątku)? I ile wynosi do_zaplaty(3, 2, 1) (marzec, 2 noce, 1 osoba)? Czas: 20 minut.

📄 `cwiczenia/tydzien_03/powtorka_etap_0_2.md` · rozwiązanie: `rozwiazania/tydzien_03/powtorka_etap_0_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Rabat 7 nocy + 4 osoby wychodzi 10 zamiast 15.**
  - Przyczyna: elif zamiast niezależnych if — rabaty się nie sumują.
  - Jak sprawdzić: Przykład (7, 4).
  - Poprawka: Dwa osobne if dodające do zmiennej, potem min(…, 15).
- ✘ **sezon("7") zwraca „niski”.**
  - Przyczyna: Napis "7" to nie liczba 7 — `"7" in (6, 7, 8, 12)` to False.
  - Jak sprawdzić: Skąd przychodzi miesiąc (input? CSV?)
  - Poprawka: Zamień na int przy wczytywaniu danych; w specyfikacji zapisz typ wejścia.

## Pułapki
- Mini-projekt to nie egzamin — jeśli utknąłeś, rozwiązanie wzorcowe jest w materiałach (rozwiazania/), ale najpierw 3 konkretne iteracje z AI.
- Nie przechodź do etapu 1 z poczuciem „kopiuję, ale nie wiem co” — to sygnał, by powtórzyć lekcje czytania kodu.

## Dodatkowe zadania
1. Zbuduj rabaty.py i zalicz test.
2. Wypełnij samoocenę w dzienniku.
3. Zrób quiz tygodnia 3.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego elif psuje sumowanie rabatów?**
  - Bo wykonuje tylko pierwszy pasujący blok — drugi rabat jest pomijany.
- **Jakie przykłady wpiszesz dla granic rabatu?**
  - 6 i 7 nocy, 3 i 4 osoby, oraz kombinację 7 nocy i 4 osób.
- **Kiedy jesteś gotowy na agenta?**
  - Gdy czytasz traceback i kod samodzielnie, piszesz specyfikację z przykładami i zaliczasz mini-projekt w 1–3 iteracjach.

## Co potrafię teraz bez patrzenia na przykład?
Zbudowałeś mini-projekt od specyfikacji do testu, oceniłeś gotowość i wiesz, które lekcje powtórzyć przed etapem z agentem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Python — oficjalny tutorial (python.org, wersja polskojęzyczna częściowo; tłumaczenie robocze w lekcji) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/>
- Anthropic — Use examples (multishot prompting) (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting>

## Test (w Mentorze: Lekcje → Sprawdź się)
- rabat(7, 4) według specyfikacji to:
  - A) 10
  - B) 5
  - C) 15
  - D) 20
- Miesiąc 12 to sezon:
  - A) wysoki
  - B) niski
  - C) błąd
  - D) zależy od roku
- Jaki jest dobry wynik samooceny przed etapem 1?
  - A) Kopiuję kod bez czytania
  - B) Czytam traceback i kod sam, mini-projekt w 1–3 iteracjach
  - C) Nie potrzebuję testów
  - D) Mam dwa plany AI

Odpowiedzi: C, A, B
