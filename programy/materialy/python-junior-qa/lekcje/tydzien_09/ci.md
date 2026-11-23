# GitHub Actions i pytest-html: testy uruchamiane przy każdym pushu
Tydzień 9 · lekcja 33 z 39 · ≈ 45 min

**Po tej lekcji potrafisz:** tworzysz workflow GitHub Actions (.github/workflows/tests.yml), który przy każdym pushu instaluje zależności i uruchamia pytest, dodajesz raport HTML (pytest-html) jako artefakt i odznakę statusu w README.

**Po co mi to?** Zielony znaczek CI przy projekcie mówi rekruterowi: testy naprawdę działają, a nie tylko „u mnie”. W firmach żaden pull request nie jest scalany bez zielonego CI.

## Czego potrzebujesz
- Repozytorium na GitHubie z testami pytest i requirements.txt.
- Lekcje „venv” i „pytest”.
- GitHub Actions jest darmowe dla repozytoriów publicznych.

## 1 · Wyjaśnienie od podstaw
### Ciągła integracja (CI)
Po każdym pushu serwer pobiera kod, instaluje środowisko od zera i uruchamia testy. Wynik widać przy commicie i w pull requeście (✔ albo ✘). To automatyczny test regresji.
### Workflow = plik YAML
Plik `.github/workflows/tests.yml` w repozytorium. YAML: wcięcia **spacjami** (nie Tab), `klucz: wartość`, listy z `-`.
```
name: Testy
on: [push, pull_request]
jobs:
  testy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -v
```
`on` — kiedy uruchomić; `runs-on` — system maszyny; `uses` — gotowa akcja (checkout pobiera kod, setup-python instaluje Pythona); `run` — polecenie. Wersje akcji podane jak w dokumentacji GitHub.
### Raport HTML: pytest-html
Dopisz `pytest-html` do requirements.txt i zmień polecenie: `python -m pytest -v --html=raport.html --self-contained-html`. Raport zapisz jako **artefakt** (do pobrania z zakładki Actions):
```
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: raport-testow
          path: raport.html
```
`if: always()` — raport trafia na GitHub także wtedy, gdy testy padły (wtedy jest najbardziej potrzebny).
### Selenium w CI
Maszyny ubuntu-latest mają przeglądarkę Chrome; w CI uruchamiasz ją bez okna (`--headless=new`). Sklep testowy/aplikację startujesz w kroku przed testami (np. `python app.py &` i chwila na start) albo w fixturze.
### Odznaka w README
`![Testy](https://github.com/TWOJA-NAZWA/REPO/actions/workflows/tests.yml/badge.svg)` — zielona/czerwona plakietka na górze README.
### Czytanie wyniku
Actions → przebieg → zadanie „testy” → rozwiń krok z ✘ — zobaczysz ten sam wynik pytest co lokalnie.

## 2 · Demonstracja — krok po kroku
**Pierwszy zielony pipeline**

```
# .github/workflows/tests.yml
name: Testy
on: [push, pull_request]
jobs:
  testy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Zależności
        run: python -m pip install -r requirements.txt
      - name: Testy z raportem
        run: python -m pytest -v --html=raport.html --self-contained-html
      - name: Raport jako artefakt
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: raport-testow
          path: raport.html
```

1. Utwórz katalogi `.github\workflows` w repozytorium (kropka na początku nazwy!) i plik tests.yml z ramki.
2. `name` — nazwa widoczna w zakładce Actions; `on: [push, pull_request]` — przy każdym pushu i PR.
3. `runs-on: ubuntu-latest` — darmowa maszyna z Linuksem; Twój kod Pythona działa tam tak samo.
4. `actions/checkout@v6` — pobiera Twoje repozytorium; `actions/setup-python@v5` z `python-version` — instaluje Pythona.
5. `pip install -r requirements.txt` — dlatego requirements.txt musi zawierać wszystko (pytest, pytest-html…).
6. `pytest … --html=raport.html --self-contained-html` — jeden plik HTML z wynikami.
7. `upload-artifact` z `if: always()` — raport do pobrania nawet przy czerwonym wyniku.
8. commit + push → GitHub → Actions: żółta kropka (trwa) → zielony ✔ po ok. minucie. Zepsuj test, push → czerwony ✘ i e-mail o nieudanym przebiegu.

✔ **Oczekiwany wynik:** Zakładka Actions z zielonym przebiegiem i artefaktem raport-testow; odznaka „Testy passing” w README.

## 3 · Jak to uruchomić
1. W repozytorium: `mkdir .github\workflows` → plik tests.yml → `git add .github` → commit → push.
2. GitHub → zakładka Actions → przebieg → Summary → Artifacts → raport-testow.

## W praktyce
- Każdy PR: zielone CI przed recenzją.
- Czerwone CI na main = wszyscy przerywają i naprawiają (zasada zespołu).

## 4 · Ćwiczenie prowadzone
Na wzór demonstracji uzupełnij brakujące elementy workflow: (1) nazwa akcji pobierającej kod (z wersją jak w lekcji), (2) klucz określający system maszyny, (3) warunek, żeby raport trafił na GitHub także przy czerwonych testach. Czas: 10 minut.

📄 `cwiczenia/tydzien_09/ci_1.md` · rozwiązanie: `rozwiazania/tydzien_09/ci_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
CI jest czerwone, lokalnie wszystko zielone. Log: `ModuleNotFoundError: No module named 'requests'`. (1) Najbardziej prawdopodobna przyczyna (wybierz)? (2) Co robisz (wybierz)? (3) Gdyby log mówił `yaml: line 9: found character that cannot start any token` — co jest źle (wybierz)? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/ci_2.md` · rozwiązanie: `rozwiazania/tydzien_09/ci_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Zakładka Actions pusta po pushu**
  - Przyczyna: Plik w złym miejscu (np. github/workflows bez kropki) albo rozszerzenie .yml.txt.
  - Jak sprawdzić: Ścieżka na GitHubie: .github/workflows/tests.yml.
  - Poprawka: Przenieś plik do .github/workflows/ z rozszerzeniem .yml.
- ✘ **ERROR: file or directory not found: tests/**
  - Przyczyna: Polecenie pytest wskazuje katalog, którego nie ma w repozytorium.
  - Jak sprawdzić: Struktura repo na GitHubie.
  - Poprawka: Popraw ścieżkę albo uruchamiaj samo `python -m pytest`.
- ✘ **Selenium w CI: SessionNotCreatedException / brak ekranu**
  - Przyczyna: Przeglądarka bez trybu headless na serwerze bez ekranu.
  - Jak sprawdzić: Opcje przeglądarki w fixturze.
  - Poprawka: `--headless=new`; w CI Chrome (`webdriver.Chrome(options=...)`).

## Pułapki
- Sekrety (hasła, klucze) w pliku workflow — tylko w Settings → Secrets and variables → Actions.
- Wersje akcji „@main” zamiast konkretnej — zmiana po stronie autora może zepsuć Twój pipeline.

## Dodatkowe zadania
1. tests.yml uruchamiający pytest przy pushu — zielony znaczek.
2. pytest-html i raport jako artefakt.
3. Odznaka CI w README repozytorium testów.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi CI?**
  - Przy każdej zmianie instaluje środowisko od zera i uruchamia testy.
- **Dlaczego if: always() przy raporcie?**
  - Żeby raport był dostępny także przy czerwonych testach.
- **Gdzie trzymasz sekrety dla Actions?**
  - W Settings → Secrets and variables → Actions, nie w pliku.

## Co potrafię teraz bez patrzenia na przykład?
Tworzysz workflow GitHub Actions z pytest, raportem HTML jako artefaktem i odznaką w README; czytasz logi i naprawiasz typowe przyczyny czerwonego CI.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — Building and testing Python (actions/checkout@v6, actions/setup-python, pytest) (dostęp 23.11.2026) — <https://docs.github.com/en/actions/tutorials/build-and-test-code/python>
- GitHub Docs — About READMEs (dostęp 23.11.2026) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
- pytest — Get Started (dostęp 23.11.2026) — <https://docs.pytest.org/en/stable/getting-started.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Plik workflow umieszczasz w:
  - A) .github/workflows/
  - B) workflows/
  - C) github/
  - D) .git/workflows/
- CI czerwone, lokalnie zielone — częsta przyczyna:
  - A) zbyt szybki komputer
  - B) brak pakietu w requirements.txt
  - C) kolor motywu
  - D) nazwa gałęzi
- Wcięcia w YAML:
  - A) Tab
  - B) spacje
  - C) dowolne
  - D) nawiasy
- Raport pytest-html tworzy opcja:
  - A) --report
  - B) --html=raport.html
  - C) -v
  - D) --junit

Odpowiedzi: A, B, B, B
