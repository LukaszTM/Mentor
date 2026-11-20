# Pierwszy program z AI: od specyfikacji do zielonego testu
Tydzień 3 · lekcja 11 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** przechodzisz pełną pętlę: specyfikacja → prośba do czatu AI → plik w PRACA → uruchomienie → testy Mentora → konkretna poprawka → zapis w dzienniku.

**Po co mi to?** To dokładnie ta sama pętla, którą od tygodnia 4 wykonasz z agentem — tylko wolniej i ręcznie, żebyś widział każdy krok.

## Czego potrzebujesz
- Lekcje „Specyfikacja” i „Rozmowa z AI”.
- Darmowy czat AI.
- Środowisko kursu (zakładka Środowisko — zielone).

## 1 · Wyjaśnienie od podstaw
### Pętla pracy vibe codera
| krok | kto | co powstaje |
|---|---|---|
| 1. Specyfikacja | Ty | specyfikacja.md z przykładami |
| 2. Prośba | Ty | wiadomość z 5 części + specyfikacja |
| 3. Kod | AI | plik .py |
| 4. Uruchomienie | Ty | wynik albo traceback |
| 5. Sprawdzenie | testy Mentora | ✔ albo lista przypadków, które nie przechodzą |
| 6. Poprawka | AI na Twoje konkretne zgłoszenie | nowa wersja |
| 7. Zapis | Ty | dziennik: co sprawdziłem, czego nie rozumiem |
### Kopiowanie kodu z czatu — bez pułapek
- Używaj przycisku „Copy/Kopiuj” bloku kodu (nie zaznaczaj myszą — łatwo uciąć linię).
- Wklejaj CAŁY plik, jeśli model dał cały plik; jeśli dał fragment — zapytaj, gdzie dokładnie go wstawić, albo poproś o cały plik.
- Zapisz z rozszerzeniem .py (nie .txt). Nazwa pliku musi być taka, jak w zadaniu — testy szukają konkretnej nazwy.
- Sprawdź wcięcia po wklejeniu (IndentationError = coś się przesunęło).
### Jak testy Mentora sprawdzają Twój plik
„✔ Sprawdź wynik” uruchamia niezależne testy z paczki kursu (folder WERYFIKATORY). Testy importują Twój plik i wywołują funkcje z różnymi danymi — także takimi, których nie było w przykładach. Wynik: zielony (zaliczone) albo lista nieprzechodzących przypadków, np. „koszt_pobytu(7, 1): oczekiwano 756.0, otrzymano 840.0”. Testów nie da się „przekonać”: suma kontrolna SHA-256 pilnuje, że nikt (także agent) ich nie zmienił.
### Czytaj kod, zanim zaliczysz
Zielony test to warunek konieczny, ale nie jedyny. Zanim zamkniesz zadanie, przeczytaj kod z pytaniami z lekcji „Czytanie kodu 2”: co przyjmuje, co zwraca, kiedy odmawia, co zmienia poza sobą. Jeśli jakiejś linii nie rozumiesz — zapytaj model „wyjaśnij linię 7 jak początkującemu”.
### Ile poprawek to za dużo?
Reguła trzech: jeśli po 3 konkretnych poprawkach błąd wraca — zatrzymaj się. Zwykle specyfikacja jest niejasna albo rozmowa za długa. Popraw specyfikację i zacznij nową rozmowę.

## 2 · Demonstracja — krok po kroku
**Kalkulator pobytu — pełna pętla**

```
Fragment dziennika po zadaniu:

## 2026-12-02 — kalkulator_pobytu.py
- Specyfikacja: 6 przykładów, 2 brzegowe (7 nocy, 0 nocy).
- Iteracje: 2 (pierwsza wersja liczyła rabat od 8 nocy — warunek > zamiast >=).
- Sprawdzenie: testy Mentora ✔, przeczytałem kod: rozumiem wszystkie linie poza round(x, 2) — doczytałem.
- Pytanie: czy cena 120 zł ma być parametrem? (zapisane do specyfikacji v2).
```

1. Specyfikacja (z lekcji start_vibe): koszt_pobytu(noce, osoby, cena_za_osobe_noc=120), rabat 10% od 7 nocy, < 1 → ValueError, wynik zaokrąglony do groszy.
2. Prośba do czatu: specyfikacja + „cały plik w jednym bloku, bez input() w funkcji, blok if __name__ == '__main__' z przykładowym wywołaniem”.
3. Kopiujesz przyciskiem Copy, zapisujesz jako kalkulator_pobytu.py w PRACA (zadanie tygodnia → „📝 Utwórz plik ćwiczenia”, potem wklej pod nagłówkiem).
4. ▶ Uruchom: blok __main__ wypisuje przykład. ✔ Sprawdź wynik: 1 przypadek nie przechodzi — „koszt_pobytu(2, 2, cena_za_osobe_noc=150): TypeError: unexpected keyword argument” — model nazwał parametr „cena”.
5. Zgłoszenie: „Parametr ma się nazywać dokładnie cena_za_osobe_noc (tak jest w specyfikacji) — zmień tylko nazwę”. Nowa wersja → ✔ zielony.
6. Czytasz kod 4 pytaniami i zapisujesz dziennik.

✔ **Oczekiwany wynik:** Zadanie zaliczone automatycznie; wiesz, że nazwy z specyfikacji są częścią „umowy” z testami, a przeczytany kod rozumiesz linia po linii.

## 3 · Jak to uruchomić
1. Zadanie tygodnia → „📝 Utwórz plik ćwiczenia” → wklej kod → „▶ Uruchom” → „✔ Sprawdź wynik”.

## W praktyce
- Jedno zadanie = jedna rozmowa = jeden wpis w dzienniku.
- Nazwy z zadania kopiuj, nie przepisuj.

## 4 · Ćwiczenie prowadzone
Test Mentora pokazał: „koszt_pobytu(7, 2): oczekiwano 1512.0, otrzymano 1680”. Specyfikacja: 120 zł/os./noc, rabat 10% od 7 nocy. Ile wynosi koszt bez rabatu? Czy rabat został naliczony (tak/nie)? Jaki znak porównania najpewniej jest w warunku zamiast >=? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/pierwszy_program_z_ai_1.md` · rozwiązanie: `rozwiazania/tydzien_03/pierwszy_program_z_ai_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Uporządkuj pętlę pracy: wpisz numery kroków w kolejności dla: A) testy Mentora, B) specyfikacja, C) zapis w dzienniku, D) prośba do AI, E) uruchomienie. Podaj kolejność jako ciąg liter (np. ABCDE). Druga sprawa: po ilu nieudanych konkretnych poprawkach zatrzymujesz się i poprawiasz specyfikację? Czas: 15 minut.

📄 `cwiczenia/tydzien_03/pierwszy_program_z_ai_2.md` · rozwiązanie: `rozwiazania/tydzien_03/pierwszy_program_z_ai_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Mentor: „Brak pliku kalkulator_pobytu.py”.**
  - Przyczyna: Plik zapisany pod inną nazwą lub w innym folderze (albo jako .py.txt).
  - Jak sprawdzić: Mój projekt → Otwórz folder; rozszerzenia widoczne?
  - Poprawka: Nazwa dokładnie jak w zadaniu, w katalogu PRACA.
- ✘ **„AssertionError: Brak funkcji koszt_pobytu”.**
  - Przyczyna: Model nazwał funkcję inaczej (np. oblicz_koszt).
  - Jak sprawdzić: Szukaj `def` w pliku.
  - Poprawka: Zmień nazwę na tę ze specyfikacji — nazwy to umowa z testem.
- ✘ **Testy „wiszą” i kończą się po czasie.**
  - Przyczyna: W kodzie jest input() poza blokiem __main__ — test czeka na klawiaturę.
  - Jak sprawdzić: Szukaj input( w pliku.
  - Poprawka: Przenieś input() do bloku if __name__ == "__main__":.

## Pułapki
- Nie dopasowuj specyfikacji do kodu, który „prawie działa”. To kod ma spełnić specyfikację.
- Zielony test ≠ rozumiem kod. Zadanie kończy się, gdy umiesz wyjaśnić każdą linię.

## Dodatkowe zadania
1. Przejdź pełną pętlę dla walidacja.py (zadanie tygodnia).
2. Zapisz w dzienniku liczbę iteracji i co je spowodowało.
3. Poproś model o wyjaśnienie jednej linii, której nie rozumiesz.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Jakie są kroki pętli pracy?**
  - Specyfikacja → prośba → kod → uruchomienie → testy → poprawka → zapis.
- **Dlaczego nazwa funkcji musi być dokładnie taka jak w zadaniu?**
  - Testy importują ją po nazwie — inna nazwa to „Brak funkcji”.
- **Kiedy zadanie jest naprawdę skończone?**
  - Gdy testy są zielone i rozumiesz każdą linię kodu.

## Co potrafię teraz bez patrzenia na przykład?
Przeszedłeś pełną pętlę ze zwykłym czatem: specyfikacja, kod, uruchomienie, testy, konkretna poprawka i dziennik — ta sama pętla czeka Cię z agentem.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Claude Code — Best practices (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>
- Anthropic — Prompt engineering overview (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview>
- Python tutorial — 4.8 Defining Functions (def, return) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co robisz po zielonym teście?
  - A) Nic
  - B) Czytam kod 4 pytaniami i zapisuję dziennik
  - C) Usuwam plik
  - D) Proszę o nowy kod
- Testy Mentora „wiszą”. Najczęstsza przyczyna:
  - A) Za wolny komputer
  - B) input() poza blokiem __main__
  - C) Zła wersja Windows
  - D) Brak internetu
- Model nazwał funkcję inaczej niż w zadaniu. Co robisz?
  - A) Zmieniam zadanie
  - B) Zmieniam nazwę na tę ze specyfikacji
  - C) Usuwam test
  - D) Ignoruję
- Reguła trzech poprawek mówi:
  - A) Zawsze 3 iteracje
  - B) Po 3 nieudanych poprawkach popraw specyfikację i zacznij nową rozmowę
  - C) 3 pliki naraz
  - D) 3 testy

Odpowiedzi: B, B, B, B
