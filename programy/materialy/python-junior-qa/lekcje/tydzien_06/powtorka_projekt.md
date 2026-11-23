# Powtórka etapu 2: projekt jak w zespole — struktura, Git, środowisko, czytanie cudzego kodu
Tydzień 6 · lekcja 26 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** porządkujesz repozytorium jak w zespole (struktura, README, .gitignore, requirements.txt, historia commitów), czytasz cudzy projekt metodą „od wejścia do szczegółów” i oceniasz repozytorium listą kontrolną rekrutera.

**Po co mi to?** Pierwsze dni w pracy QA to czytanie cudzego kodu i uruchamianie cudzego projektu. Twoje repozytorium jest pierwszym projektem, który przeczyta rekruter.

## Czego potrzebujesz
- Lekcje tygodni 4–6.
- Projekt do przeczytania z paczki kursu: projekty/cudzy_projekt/ (Mój projekt → Skopiuj materiały kursu).

## 1 · Wyjaśnienie od podstaw
### Czytanie cudzego projektu — od wejścia do szczegółów
1. README i struktura katalogów (co jest czym?). 2. Plik startowy (main.py / app.py) — od `if __name__ == "__main__":`. 3. Importy — mapa zależności między plikami. 4. Nazwy i docstringi funkcji — bez wchodzenia w szczegóły. 5. Uruchom z przykładowymi danymi. 6. Dopiero teraz szczegóły jednej funkcji (debugger krok po kroku).
Zapisuj w notatkach: plik → odpowiedzialność → najważniejsze funkcje → pytania.
### Mapa etapu 2
| temat | umiesz, gdy… |
|---|---|
| pliki, CSV | czytasz CSV do listy słowników i liczysz statystyki z float/int |
| Git w zespole | gałąź → PR → merge; restore/stash/revert bez paniki |
| klasy | piszesz klasę z walidacją w metodach |
| moduły | dzielisz program na pliki z jedną odpowiedzialnością |
| venv | odtwarzasz środowisko z requirements.txt |
| API | GET z timeout, kody HTTP, JSON, błędy sieci |
| debugowanie | odtwórz → zawęź → hipoteza → sprawdź |
| README | obca osoba uruchamia projekt bez pytań |
### Lista kontrolna rekrutera (repozytorium)
- README z opisem, uruchomieniem i przykładem; - .gitignore (brak .venv, __pycache__, .env); - requirements.txt; - czytelna struktura (folder na projekt); - commity z opisami („Dodaj…”, „Popraw…”), nie „asdf”; - brak haseł/kluczy w historii; - kod z funkcjami i docstringami.

## 2 · Demonstracja — krok po kroku
**Repozytorium portfolio po porządkach**

```
python-projekty/
├── README.md              ← tabela: projekt | co robi | technologie | link
├── .gitignore             ← .venv/ __pycache__/ .env
├── kalkulator_bmi/
│   ├── README.md
│   └── bmi.py             ← oblicz_bmi(), kategoria(), blok __main__
├── zgadnij_liczbe/
│   ├── README.md
│   └── zgadnij.py
├── menedzer_zadan/
│   ├── README.md
│   ├── main.py  zadania.py  plik.py
└── raport_cen/
    ├── README.md  requirements.txt
    └── api.py  raport.py

git log --oneline (fragment):
a1b2c3d Dodaj README dla raportu cen
9f8e7d6 Popraw obsługę braku połączenia w api.py
5c4b3a2 Wydziel zapis CSV do raport.py
```

1. Jedno repozytorium python-projekty z folderem na każdy projekt — rekruter widzi całość w jednym miejscu.
2. Główny README.md: tabela projektów z linkami do folderów (Markdown: `[menedżer zadań](menedzer_zadan/)`).
3. Każdy projekt ma własny README z „Jak uruchomić”.
4. .gitignore w katalogu głównym działa dla wszystkich podfolderów.
5. Projekty z bibliotekami mają requirements.txt.
6. Historia commitów opisuje zmiany — widać sposób pracy.
7. Przeniesienie plików do folderów: `git mv bmi.py kalkulator_bmi/bmi.py` — Git zachowa historię pliku.

✔ **Oczekiwany wynik:** Repozytorium, które obca osoba uruchamia bez pytań, a rekruter rozumie w 30 sekund.

## 3 · Jak to uruchomić
1. Terminal w repozytorium: `git mv` dla przenoszenia plików, potem commit i push.
2. GitHub → strona repozytorium → sprawdź, jak wygląda README.

## W praktyce
- Pierwszy dzień w projekcie: README → uruchom → testy → struktura → pytania do zespołu.
- Przed wysłaniem CV: przejdź listę kontrolną na każdym repo.

## 4 · Ćwiczenie prowadzone
Czytasz cudzy projekt: pliki app.py (`if __name__ == "__main__": uruchom()`), baza.py (funkcje zapisz/wczytaj), raport.py (funkcja raport_miesieczny), README.md. (1) Od którego pliku zaczniesz czytać? (2) Który plik pierwszy otworzysz z kodu? (3) Gdzie szukasz odpowiedzi „skąd biorą się dane”? Opcje: README.md / app.py / baza.py / raport.py. Czas: 10 minut.

📄 `cwiczenia/tydzien_06/powtorka_projekt_1.md` · rozwiązanie: `rozwiazania/tydzien_06/powtorka_projekt_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Oceń repozytorium listą kontrolną (spełnia: tak/nie): (1) README: „# projekt” i nic więcej; (2) w repozytorium jest folder .venv z 3000 plików; (3) commity: „zmiany”, „asdf”, „final”, „final2”; (4) plik config.py z `API_KEY = "sk-…"`; (5) każdy projekt w osobnym folderze. Który problem naprawiasz PIERWSZY (wybierz numer 1–5)? Czas: 15 minut.

📄 `cwiczenia/tydzien_06/powtorka_projekt_2.md` · rozwiązanie: `rozwiazania/tydzien_06/powtorka_projekt_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Po przeniesieniu plików importy nie działają**
  - Przyczyna: Moduły w różnych folderach, a import zakłada ten sam katalog.
  - Jak sprawdzić: Uruchom z folderu projektu.
  - Poprawka: Każdy projekt uruchamiaj z jego folderu (cd kalkulator_bmi).
- ✘ **Historia pliku „zniknęła” po przeniesieniu**
  - Przyczyna: Przeniesienie w Eksploratorze + nowy plik.
  - Jak sprawdzić: `git log --follow nowa/sciezka.py`.
  - Poprawka: Przenoś `git mv` — historia zostaje.

## Pułapki
- Czytanie cudzego kodu od pierwszej linii najdłuższego pliku — zaczynaj od README i punktu wejścia.
- Ukrywanie słabych projektów — lepiej 4 porządne niż 10 bałaganu.

## Dodatkowe zadania
1. Przeczytaj projekty/cudzy_projekt i opisz każdy plik w notatki_projekt.md.
2. Uporządkuj repozytorium python-projekty wg listy kontrolnej.
3. Popraw README każdego projektu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Od czego zaczynasz czytanie cudzego projektu?**
  - README i struktura, potem punkt wejścia.
- **Co sprawdza rekruter w repozytorium?**
  - README, porządek, commity, brak sekretów, czytelny kod.
- **Jak przenieść plik z zachowaniem historii?**
  - git mv.

## Co potrafię teraz bez patrzenia na przykład?
Porządkujesz repozytorium jak w zespole, czytasz cudzy projekt od wejścia do szczegółów i oceniasz kod listą kontrolną rekrutera.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — About READMEs (dostęp 23.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
- Pro Git (wydanie 2, wersja polska) — Scott Chacon, Ben Straub (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2>
- PEP 8 — Style Guide for Python Code (dostęp 23.11.2026) — <https://peps.python.org/pep-0008/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Klucz API znaleziony w publicznym repo. Pierwszy krok:
  - A) usunąć plik
  - B) unieważnić klucz u dostawcy
  - C) zmienić nazwę pliku
  - D) nic
- git mv:
  - A) kopiuje plik na GitHub
  - B) przenosi plik z zachowaniem historii
  - C) usuwa plik
  - D) scala gałęzie
- Punkt wejścia programu najczęściej znajdziesz:
  - A) w README
  - B) w bloku if __name__ == "__main__":
  - C) w .gitignore
  - D) w requirements.txt
- Lepsze portfolio:
  - A) 10 projektów bez README
  - B) 4 projekty z README i testami
  - C) 1 plik na 2000 linii
  - D) same zrzuty ekranu

Odpowiedzi: B, B, B, B
