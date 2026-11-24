# Gdy agent się myli: pętle, zmyślenia, „gotowe” bez dowodu
Tydzień 7 · lekcja 23 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** rozpoznajesz 6 typowych porażek agenta (pętla poprawek, zmyślone API, zmiana testów, dryf zakresu, fałszywe „gotowe”, nadgorliwość) i dla każdej znasz ruch naprawczy.

**Po co mi to?** Badanie METR (2025) pokazało, że doświadczeni programiści z AI pracowali wolniej, m.in. przez czas na poprawianie i przeglądanie wyników. Szybkie rozpoznanie porażki to największa oszczędność czasu.

## Czego potrzebujesz
- Lekcje „Przegląd zmian” i „Kontekst, limity…”.
- Plik zepsute_raporty.py z materiałów (zadanie tygodnia).

## 1 · Wyjaśnienie od podstaw
### Sześć porażek i ruch naprawczy
| porażka | jak ją poznać | ruch |
|---|---|---|
| pętla poprawek | ten sam błąd wraca po 2–3 poprawkach, agent przeprasza i próbuje „inaczej” | Esc → cofnij (/rewind lub git restore) → nowa sesja z opisem problemu i hipotezą |
| zmyślone API / paczka | ImportError, AttributeError: module has no attribute…, paczki brak na pypi.org | każ użyć biblioteki standardowej albo pokaż fragment oficjalnej dokumentacji |
| „naprawa” przez test | testy zielone, ale w diffie zmieniony plik test_* | przywróć test, zasada w AGENTS.md, ewentualnie reguła blokująca edycję folderu testów |
| dryf zakresu | zmiany w plikach spoza zadania, nowe funkcje „przy okazji” | git restore tych plików, prośba z listą dozwolonych plików, tryb planu |
| fałszywe „gotowe” | „Done! Wszystko działa” bez uruchomienia testów | „Pokaż wynik uruchomienia testów” / sam ✔ Sprawdź wynik |
| nadgorliwość | dodaje logowanie, klasy, konfigurację, których nie potrzebujesz | „minimalna zmiana spełniająca test; bez nowych plików” |
### Najpierw diagnoza, potem kod
Gdy błąd jest uparty, zmień prośbę z „popraw” na „zdiagnozuj”: „Nie zmieniaj plików. Uruchom test, przeczytaj traceback, wypisz 3 możliwe przyczyny i jak sprawdzić każdą”. Potem wybierasz hipotezę i dopiero wtedy prosisz o jedną poprawkę. To zatrzymuje zgadywanie.
### Daj agentowi czerwony test
Najskuteczniejsza informacja dla agenta to test, który nie przechodzi, i polecenie do jego uruchomienia: „python -m pytest -q test_raporty.py::test_top_pokoje — napraw kod, nie test”. Agent sam uruchomi test po zmianie i zobaczy, czy się udało.
### Reguła trzech (wersja dla agenta)
Trzy nieudane próby na tym samym błędzie → stop. Commit tego, co działa, notatka stan.md z opisem problemu, `/clear`, nowa sesja — albo zmniejsz zadanie o połowę. Czasem najlepszy ruch to napisać jedną funkcję samodzielnie i dać agentowi resztę.
### Twoja część winy
Wiele porażek agenta zaczyna się od niejasnej specyfikacji. Po każdej porażce zapisz w dzienniku: czego brakowało w prośbie lub instrukcjach — i dopisz to do szablonu.

## 2 · Demonstracja — krok po kroku
**Z pętli poprawek do diagnozy**

```
# Fragment z zepsute_raporty.py — trzy klasyczne błędy kodu od AI
def suma_przychodu(rezerwacje):
    suma = 0
    for r in rezerwacje:
        suma =+ r["kwota"]      # =+ zamiast +=
    return suma

print(suma_przychodu([{"kwota": 100}, {"kwota": 250}]))

```

1. Zadanie: napraw top_pokoje w zepsute_raporty.py. Agent poprawia, test dalej czerwony; druga poprawka — inny błąd; trzecia — wraca pierwszy. To pętla.
2. Esc. `git restore zepsute_raporty.py` (albo /rewind) — czysty stan.
3. Nowa sesja: „Nie zmieniaj plików. Uruchom python -m pytest -q -k top i wypisz 3 możliwe przyczyny z traceback”. Agent: (1) sortowanie rosnąco zamiast malejąco, (2) remisy w złej kolejności, (3) n większe niż liczba pokoi.
4. Sprawdzasz hipotezy na danych testu: przyczyny 1 i 2 się potwierdzają.
5. Jedna prośba: „Sortuj malejąco po liczbie nocy, przy remisie alfabetycznie po nazwie pokoju. Tylko funkcja top_pokoje. Napraw kod, nie test. Uruchom test.” Zielono.

✔ **Oczekiwany wynik:** Zamiast czwartej losowej poprawki — diagnoza, dwie potwierdzone przyczyny i jedna trafna zmiana.

## 3 · Jak to uruchomić
1. Zadanie tygodnia „zepsute_raporty.py” → przy uporczywym błędzie: prośba o diagnozę bez zmian w plikach.

## W praktyce
- Przy uporczywym błędzie — zawsze najpierw diagnoza.
- Zasady z porażek trafiają do AGENTS.md.

## 4 · Ćwiczenie prowadzone
Co wypisze kod z przykładu lekcji (suma_przychodu z `=+`)? Jaka jest poprawna suma? Jak nazywa się ta porażka, jeśli agent przy „naprawie” zmieni w teście oczekiwaną wartość na wypisaną? Opcje: pętla poprawek, „naprawa” przez test, dryf zakresu, nadgorliwość. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/gdy_agent_sie_myli_1.md` · rozwiązanie: `rozwiazania/tydzien_07/gdy_agent_sie_myli_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Dopasuj ruch: (1) ImportError dla paczki, której nie ma na pypi.org; (2) czwarta poprawka tego samego błędu; (3) agent pisze „Done!”, nie uruchomił testów; (4) agent dodał 3 nowe pliki konfiguracyjne do prostej funkcji. Ruchy: stop i diagnoza w nowej sesji / biblioteka standardowa / „pokaż wynik testów” / minimalna zmiana bez nowych plików. Czas: 15 minut.

📄 `cwiczenia/tydzien_07/gdy_agent_sie_myli_2.md` · rozwiązanie: `rozwiazania/tydzien_07/gdy_agent_sie_myli_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **„AttributeError: module 'csv' has no attribute 'read_table'”.**
  - Przyczyna: Zmyślona funkcja w prawdziwym module.
  - Jak sprawdzić: docs.python.org → csv: lista funkcji.
  - Poprawka: Pokaż agentowi właściwą funkcję (csv.DictReader) albo każ sprawdzić dokumentację.
- ✘ **Agent mówi, że test „ma błąd” i proponuje go zmienić.**
  - Przyczyna: Agent optymalizuje „zielony wynik”, nie poprawność.
  - Jak sprawdzić: Czy test zgadza się ze specyfikacją?
  - Poprawka: Jeśli tak — „napraw kod, nie test”; jeśli test naprawdę jest zły — zmieniasz go Ty, świadomie.

## Pułapki
- Przeprosiny agenta („Masz rację, przepraszam!”) nie są poprawką. Patrz na diff i test.
- Nie każ agentowi „spróbować jeszcze raz” bez nowej informacji — dostaniesz losową odmianę tego samego.

## Dodatkowe zadania
1. Napraw zepsute_raporty.py z agentem (zadanie tygodnia), stosując diagnozę przy uporczywym błędzie.
2. Zapisz w dzienniku, która z 6 porażek Ci się przydarzyła.
3. Dopisz do AGENTS.md jedną zasadę wynikającą z porażki.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Czym różni się prośba „zdiagnozuj” od „popraw”?**
  - Diagnoza nie zmienia plików — daje hipotezy i sposób sprawdzenia; poprawka przychodzi po wyborze hipotezy.
- **Co robisz po trzeciej nieudanej poprawce?**
  - Stop: commit tego, co działa, notatka stanu, nowa sesja albo mniejsze zadanie.
- **Jaka informacja najbardziej pomaga agentowi?**
  - Czerwony test z poleceniem uruchomienia i zasadą „napraw kod, nie test”.

## Co potrafię teraz bez patrzenia na przykład?
Rozpoznajesz 6 porażek agenta, przechodzisz z pętli poprawek do diagnozy, dajesz agentowi czerwony test i stosujesz regułę trzech.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Claude Code — Checkpointing (/rewind, Esc Esc) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/checkpointing>
- METR (10.07.2025): badanie RCT — doświadczeni programiści z AI 19% wolniej (dostęp 24.11.2026) — <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Ten sam błąd wraca po 3 poprawkach. Ruch:
  - A) Czwarta poprawka
  - B) Stop, cofnięcie, diagnoza w nowej sesji
  - C) Większy model bez zmian prośby
  - D) Usunięcie testu
- „Done!” bez wyniku testów to:
  - A) Dowód
  - B) Fałszywe „gotowe” — poproś o wynik lub sprawdź sam
  - C) Błąd składni
  - D) Limit planu
- ImportError dla paczki spoza pypi.org sugeruje:
  - A) Brak internetu
  - B) Zmyśloną zależność
  - C) Złą wersję Windows
  - D) Błąd Gita
- Najlepsza informacja zwrotna dla agenta:
  - A) „Źle”
  - B) Czerwony test z poleceniem uruchomienia
  - C) Zrzut ekranu pulpitu
  - D) „Postaraj się”

Odpowiedzi: B, B, B, B
