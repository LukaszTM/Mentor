# Python: instalacja przez Mentora i pierwszy program
Tydzień 1 · lekcja 5 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** masz zainstalowane środowisko Pythona kursu, uruchamiasz program przyciskiem w Mentorze i komendą `python plik.py`, a wynik porównujesz z oczekiwanym.

**Po co mi to?** Kod od AI trzeba uruchomić, żeby wiedzieć, czy działa — Python jest silnikiem, na którym wykonasz 90% zadań kursu.

## Czego potrzebujesz
- Mentor → zakładka Środowisko (sprawdza i instaluje Pythona oraz biblioteki kursu: pytest, flask, requests) — za Twoją zgodą, bez uprawnień administratora.
- Internet przy pierwszej instalacji (ok. 30–80 MB).
- Lekcja „Terminal bez strachu”.

## 1 · Wyjaśnienie od podstaw
### Python i interpreter
Python to język programowania — zestaw reguł zapisu poleceń. Interpreter Pythona to program, który czyta Twój plik .py linia po linii i wykonuje polecenia. Kod od AI jest tylko tekstem, dopóki interpreter go nie wykona.
### Środowisko kursu (.venv) — dlaczego osobne
Mentor tworzy dla kursu osobne środowisko (folder `.venv`) z określonymi wersjami bibliotek: pytest (testy), flask (aplikacje internetowe), requests (pobieranie danych z internetu). Dzięki temu kurs nie psuje innych programów na komputerze, a testy działają u wszystkich tak samo. Biblioteki instalowane są z listy z sumami kontrolnymi (requirements.lock).
### Instalacja krok po kroku
- Mentor → Środowisko → „🔍 Sprawdź ponownie” — zobaczysz listę: Python, pakiety, narzędzia (Git, Claude Code, Codex — opcjonalne do późniejszych tygodni).
- „⬇ Zainstaluj brakujące” → okno z opisem, co i gdzie powstanie → „Zgadzam się — wykonaj”. Postęp widać na pasku; w razie błędu — „Pokaż szczegóły (pełny log)”.
- „✔ Sprawdź działanie” — Mentor uruchamia próbny test. Zielony wynik = gotowe.
### Pierwszy program
`print("Dzień dobry")` — funkcja print wypisuje tekst. Tekst w cudzysłowach to napis (string). Każda linia to polecenie; Python wykonuje je od góry do dołu.
### Trzy sposoby uruchomienia (wszystkie robią to samo)
| sposób | jak | kiedy |
|---|---|---|
| przycisk w zadaniu | pasek „Ćwiczenie w Mentorze” → „▶ Uruchom” | zadania kursu — od razu widać wynik i tłumaczenie błędu po polsku |
| terminal | `python witaj.py` w terminalu otwartym przyciskiem Mentora | gdy pracujesz z agentem lub chcesz podać argumenty |
| edytor | VS Code / PyCharm → Run | gdy masz edytor (opcjonalnie) |
### „✔ Sprawdź wynik” — czym różni się od „Uruchom”
„Uruchom” tylko wykonuje program. „Sprawdź wynik” uruchamia go z danymi testowymi i porównuje z oczekiwanym wynikiem albo uruchamia niezależne testy z paczki kursu (sprawdzone sumą SHA-256 — nikt ich nie podmienił). Dopiero zielony wynik zalicza zadanie automatycznie.
### Edytor (opcjonalnie)
Mentor otwiera pliki w pierwszym znalezionym edytorze: VS Code, PyCharm, Notepad++, a w ostateczności Notatnik. Polecamy darmowy VS Code (code.visualstudio.com) — w tygodniu 4 przyda się też do rozszerzeń Claude Code i Codex.

## 2 · Demonstracja — krok po kroku
**Od pustego katalogu do wyniku na ekranie**

```
# witaj.py — pierwszy program
print("Dzień dobry!")
print("Uczę się vibe codingu.")
print("2 + 3 =", 2 + 3)

```

1. Środowisko → „⬇ Zainstaluj brakujące” → zgoda. Po kilku minutach „✔ Sprawdź działanie” pokazuje zielony wynik.
2. Plan nauki → tydzień 1 → zadanie „witaj.py” → „📝 Utwórz plik ćwiczenia”: Mentor tworzy w PRACA plik z komentarzem-nagłówkiem (linie zaczynające się od # Python pomija).
3. Wpisz trzy linie z przykładu. print("…") wypisuje tekst; w trzeciej linii print dostaje dwie rzeczy: napis i wynik działania 2 + 3 — wypisuje je ze spacją.
4. Zapisz (Ctrl + S) i kliknij „▶ Uruchom”: okno wyniku pokazuje trzy linie. Zmień 2 + 3 na 20 * 3 i uruchom ponownie — wynik 60.
5. „✔ Sprawdź wynik” — Mentor szuka w wyjściu oczekiwanych tekstów; pasek zmienia się na „✔ ZALICZONE AUTOMATYCZNIE”.
6. Ta sama rzecz w terminalu: Mój projekt → „⌨ Otwórz terminal tutaj” → `python witaj.py`.

✔ **Oczekiwany wynik:** Na ekranie: „Dzień dobry!”, „Uczę się vibe codingu.”, „2 + 3 = 5”; zadanie zaliczone automatycznie.

## 3 · Jak to uruchomić
1. Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.
2. Zadanie → „▶ Uruchom” albo terminal: `python witaj.py`.

## W praktyce
- Każdy kod od AI uruchamiasz od razu — nie zbieraj „na później” 5 nieprzetestowanych plików.
- Gdy coś nie działa, najpierw czytasz komunikat błędu do końca.

## 4 · Ćwiczenie prowadzone
Co wypisze ten program? Wpisz trzy linie wyniku osobno.

print("Pod Lipą")
print("Noclegi:", 4 * 2)
print("Cena", 120, "zł")

Czas: 15 minut. Potem sprawdź, uruchamiając kod (wklej do dowolnego pliku .py w PRACA).

📄 `cwiczenia/tydzien_01/python_uruchamianie_1.md` · rozwiązanie: `rozwiazania/tydzien_01/python_uruchamianie_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Uruchamiasz `python wiat.py` i widzisz: `python: can't open file 'C:\...\PRACA\wiat.py': [Errno 2] No such file or directory`. Plik nazywa się `witaj.py`. Jaki jest numer błędu (Errno) i co poprawisz? Druga sytuacja: „▶ Uruchom” pokazuje komunikat o braku interpretera — do której zakładki Mentora idziesz? Czas: 15 minut.

📄 `cwiczenia/tydzien_01/python_uruchamianie_2.md` · rozwiązanie: `rozwiazania/tydzien_01/python_uruchamianie_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Instalacja środowiska kończy się błędem pobierania.**
  - Przyczyna: Brak internetu, zapora sieciowa lub chwilowa awaria serwera.
  - Jak sprawdzić: Środowisko → „Pokaż szczegóły (pełny log)”.
  - Poprawka: Sprawdź połączenie i kliknij „Ponów”; w sieci firmowej poproś administratora o dostęp do pypi.org.
- ✘ **„SyntaxError: unterminated string literal”.**
  - Przyczyna: Brak zamykającego cudzysłowu.
  - Jak sprawdzić: Linia wskazana w komunikacie — policz cudzysłowy.
  - Poprawka: Każdy napis ma cudzysłów otwierający i zamykający tego samego rodzaju.
- ✘ **Okno wyniku pokazuje „Program pyta o więcej danych, niż podaje test”.**
  - Przyczyna: W kodzie jest input(), a test nie podał wszystkich odpowiedzi.
  - Jak sprawdzić: Czy zadanie wymaga input()?
  - Poprawka: Wpisz dane w polu „Dane dla input()” (jedna linia = jedna odpowiedź) albo usuń zbędne input().

## Pułapki
- Nie instaluj Pythona „na wszelki wypadek” z kilku źródeł naraz — Mentor używa swojego środowiska kursu; inne wersje w systemie są w porządku, ale terminal otwieraj przyciskiem Mentora.
- Polskie znaki w programie działają (Mentor uruchamia Pythona w trybie UTF-8); jeśli w zwykłym CMD widzisz krzaczki, to kwestia terminala, nie programu.

## Dodatkowe zadania
1. Zmień przykład tak, żeby wypisał Twoje imię i wynik 7 * 24.
2. Uruchom ten sam plik przyciskiem i z terminala.
3. Zapisz w dzienniku różnicę między „Uruchom” a „Sprawdź wynik”.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co kursowi osobne środowisko .venv?**
  - Żeby wersje bibliotek były takie same u wszystkich i nie psuły innych programów; testy działają powtarzalnie.
- **Czym różni się „Uruchom” od „Sprawdź wynik”?**
  - Uruchom tylko wykonuje program; Sprawdź wynik porównuje wynik z oczekiwanym albo uruchamia niezależne testy z paczki.
- **Co robi print("a", 1 + 1)?**
  - Wypisuje `a 2` — oblicza 1 + 1 i łączy elementy spacją.

## Co potrafię teraz bez patrzenia na przykład?
Masz środowisko kursu, uruchamiasz programy przyciskiem i w terminalu, czytasz komunikat „No such file” i wiesz, że zaliczenie daje „Sprawdź wynik”.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — oficjalny tutorial (python.org, wersja polskojęzyczna częściowo; tłumaczenie robocze w lekcji) (dostęp 19.11.2026) — <https://docs.python.org/3/tutorial/>
- Python — używanie Pythona w Windows (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://docs.python.org/3/using/windows.html>
- Python — venv: środowiska wirtualne (oficjalna dokumentacja) (dostęp 19.11.2026) — <https://docs.python.org/3/library/venv.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Co robi interpreter Pythona?
  - A) Pisze kod za Ciebie
  - B) Wykonuje polecenia z pliku .py
  - C) Instaluje Windows
  - D) Tłumaczy na angielski
- Co wypisze `print("Suma:", 3 + 4)`?
  - A) Suma: 3 + 4
  - B) Suma: 7
  - C) Suma:7
  - D) 7
- Gdzie instalujesz środowisko kursu?
  - A) Zakładka Środowisko
  - B) Panel sterowania Windows
  - C) Sklep Microsoft
  - D) Asystent
- Kiedy zadanie jest zaliczone automatycznie?
  - A) Gdy plik istnieje
  - B) Gdy „Sprawdź wynik” daje zielony wynik
  - C) Gdy agent napisze „gotowe”
  - D) Po 24 godzinach

Odpowiedzi: B, B, A, B
