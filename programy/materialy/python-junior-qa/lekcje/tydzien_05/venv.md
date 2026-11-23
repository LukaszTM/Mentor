# venv, pip, requirements.txt i .gitignore
Tydzień 5 · lekcja 22 z 39 · ≈ 40 min

**Po tej lekcji potrafisz:** tworzysz własne środowisko wirtualne projektu (python -m venv .venv), aktywujesz je, instalujesz pakiety pip i zapisujesz je w requirements.txt oraz wykluczasz .venv i sekrety z Gita plikiem .gitignore.

**Po co mi to?** CI (tydzień 9) i każdy członek zespołu odtwarza Twoje środowisko z requirements.txt. Repozytorium z wrzuconym .venv to pierwsza rzecz, którą rekruter zauważa.

## Czego potrzebujesz
- Lekcja „Narzędzia” (środowisko kursu).
- Terminal PowerShell w katalogu projektu.
- Internet do pip install (pakiety z PyPI).

## 1 · Wyjaśnienie od podstaw
### Dlaczego osobne środowisko
Projekt A potrzebuje selenium 4.52, projekt B — starszej wersji. Środowisko wirtualne (venv) to katalog z własnym Pythonem i pakietami tylko dla jednego projektu. Mentor robi to za Ciebie dla kursu; teraz zrobisz to sam dla własnego projektu — tak jak w pracy.
### Krok po kroku (PowerShell, w katalogu projektu)
1. `python -m venv .venv` — tworzy katalog .venv (w terminalu Mentora `python` to Python kursu — może być bazą).
2. `.\.venv\Scripts\Activate.ps1` — aktywacja; zachęta zaczyna się od `(.venv)`. W CMD: `.venv\Scripts\activate.bat`.
   Błąd „running scripts is disabled on this system” → jednorazowo `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (dotyczy tylko Twojego konta).
3. `python -m pip install requests` — instalacja z PyPI (oficjalne repozytorium pakietów). `python -m pip` gwarantuje, że pip należy do aktywnego Pythona.
4. `python -m pip freeze > requirements.txt` — zapis dokładnych wersji (np. `requests==2.34.2`).
5. Na innym komputerze / w CI: `python -m pip install -r requirements.txt`.
6. `deactivate` — wyjście ze środowiska.
### .gitignore
Plik tekstowy w katalogu repozytorium, każda linia to wzorzec plików, których Git ma nie śledzić:
```
.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
report.html
```
`.env` to plik z sekretami (klucze API) — nigdy w repozytorium. Jeśli coś już zacommitowałeś: `git rm -r --cached .venv`, potem commit.
### Bezpieczeństwo pakietów
Instaluj tylko pakiety o nazwach sprawdzonych w dokumentacji — literówka w nazwie (np. „reqeusts”) może zainstalować złośliwą podróbkę. Mentor dla kursu instaluje z pliku z sumami SHA-256 (lock), dlatego tam to ryzyko nie istnieje.

## 2 · Demonstracja — krok po kroku
**Własne środowisko projektu od zera**

```
PS C:\…\PRACA\pogoda> python -m venv .venv
PS C:\…\PRACA\pogoda> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\…\pogoda> python -m pip install requests
Successfully installed certifi-… charset-normalizer-… idna-… requests-2.34.2 urllib3-…
(.venv) PS C:\…\pogoda> python -m pip freeze > requirements.txt
(.venv) PS C:\…\pogoda> Get-Content requirements.txt
certifi==2026.10.23
charset-normalizer==3.5.2
idna==3.…
requests==2.34.2
urllib3==2.…
(.venv) PS C:\…\pogoda> Set-Content .gitignore ".venv/`n__pycache__/`n.env"
(.venv) PS C:\…\pogoda> git status --short
?? .gitignore
?? api.py
?? requirements.txt
```

1. `python -m venv .venv` — powstaje katalog .venv (kilkadziesiąt MB). Kropka na początku nazwy to konwencja „katalog techniczny”.
2. `Activate.ps1` — od teraz `python` i `pip` w tym oknie to te z .venv; widać `(.venv)` w zachęcie.
3. `pip install requests` instaluje też zależności requests (certifi, idna…).
4. `pip freeze > requirements.txt` — znak `>` przekierowuje wynik do pliku.
5. `.gitignore` z trzema liniami (w PowerShell `` `n `` to nowa linia; możesz też utworzyć plik w edytorze).
6. `git status --short` — .venv NIE pojawia się na liście (zignorowany), widać tylko pliki projektu.

✔ **Oczekiwany wynik:** Projekt z .venv (niewidocznym dla Gita), requirements.txt z dokładnymi wersjami i .gitignore.

## 3 · Jak to uruchomić
1. PowerShell → `cd` do katalogu projektu → polecenia z ramki.
2. Weryfikacja: `python -c "import sys; print(sys.prefix)"` — ścieżka powinna kończyć się na .venv.

## W praktyce
- Pierwsze polecenia w nowym projekcie: venv → .gitignore → git init.
- W CI: pip install -r requirements.txt, potem pytest.

## 4 · Ćwiczenie prowadzone
Ułóż kroki (numery po przecinku): 1 `python -m pip freeze > requirements.txt`, 2 `.\.venv\Scripts\Activate.ps1`, 3 `python -m venv .venv`, 4 `python -m pip install requests`, 5 dopisz `.venv/` do .gitignore. Czas: 10 minut.

📄 `cwiczenia/tydzien_05/venv_1.md` · rozwiązanie: `rozwiazania/tydzien_05/venv_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które pliki/katalogi trafiają do repozytorium (tak/nie)? (1) requirements.txt, (2) .venv/, (3) .env z kluczem API, (4) api.py, (5) __pycache__/. Dodatkowo (6): kolega po sklonowaniu repo ma błąd ModuleNotFoundError: requests — jakie polecenie wpisze (wpisz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_05/venv_2.md` · rozwiązanie: `rozwiazania/tydzien_05/venv_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **.\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system**
  - Przyczyna: Domyślna polityka PowerShell blokuje skrypty.
  - Jak sprawdzić: `Get-ExecutionPolicy -Scope CurrentUser`.
  - Poprawka: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` albo aktywacja w CMD (activate.bat).
- ✘ **pip install działa, a import nie (ModuleNotFoundError)**
  - Przyczyna: Pakiet zainstalowany do innego Pythona.
  - Jak sprawdzić: `python -m pip --version` — ścieżka?
  - Poprawka: Aktywuj .venv i używaj `python -m pip`.
- ✘ **Na GitHubie tysiące plików z .venv**
  - Przyczyna: .gitignore dodany po commicie.
  - Jak sprawdzić: `git ls-files .venv | Measure-Object`.
  - Poprawka: `git rm -r --cached .venv`, commit; .gitignore z .venv/.

## Pułapki
- Literówka w nazwie pakietu (typosquatting) — kopiuj nazwy z oficjalnej dokumentacji.
- pip freeze w środowisku z „wszystkim” (systemowym) — requirements z setką zbędnych pakietów.

## Dodatkowe zadania
1. Utwórz .venv w katalogu projektu pogody, zainstaluj requests, zapisz requirements.txt.
2. Dodaj .gitignore z .venv/, __pycache__/, .env.
3. Sprawdź git status — .venv niewidoczny.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Po co venv?**
  - Osobne pakiety i wersje dla każdego projektu.
- **Co zawiera requirements.txt?**
  - Listę pakietów z wersjami do odtworzenia środowiska.
- **Co wpisujesz do .gitignore na start?**
  - .venv/, __pycache__/, .env, pliki raportów.

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz i aktywujesz venv, instalujesz pakiety pip, zapisujesz requirements.txt i chronisz repozytorium plikiem .gitignore.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Poradnik: Środowiska wirtualne i pakiety (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/venv.html>
- Pro Git PL — Podstawy Gita (rejestrowanie zmian, historia, cofanie) (dostęp 23.11.2026) — <https://git-scm.com/book/pl/v2/Podstawy-Gita-Rejestrowanie-zmian-w-repozytorium>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Tworzenie środowiska wirtualnego:
  - A) pip venv
  - B) python -m venv .venv
  - C) git venv
  - D) venv install
- Odtworzenie zależności z pliku:
  - A) pip freeze
  - B) pip install -r requirements.txt
  - C) pip list
  - D) git pull
- Czy .venv commitujesz?
  - A) tak, zawsze
  - B) nie — każdy tworzy własne z requirements.txt
  - C) tylko na main
  - D) tylko w PR
- Plik .env z kluczem API:
  - A) do repozytorium
  - B) do .gitignore
  - C) do README
  - D) do requirements.txt

Odpowiedzi: B, B, B, B
