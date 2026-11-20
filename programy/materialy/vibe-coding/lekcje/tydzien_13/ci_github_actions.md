# Automatyczne testy w chmurze: GitHub Actions (CI)
Tydzień 13 · lekcja 42 z 48 · ≈ 45 min

**Po tej lekcji potrafisz:** dodajesz workflow GitHub Actions, który przy każdym push i pull requeście instaluje zależności z requirements.txt i uruchamia pytest — i czytasz jego wynik w zakładce Actions.

**Po co mi to?** CI (ciągła integracja) sprawdza każdą zmianę tak samo, niezależnie od Twojego komputera i humoru agenta. Zielony znaczek przy PR to standard w zespołach.

## Czego potrzebujesz
- Repozytorium pod-lipa z testami.
- Lekcje „Testy jako umowa” i „Przegląd kodu”.

## 1 · Wyjaśnienie od podstaw
### Workflow = przepis w YAML
Plik `.github/workflows/testy.yml` w repozytorium. GitHub uruchamia go na swojej maszynie (runnerze) przy zdarzeniach, które wskażesz.
```
name: Testy
on:
  push:
    branches: [main]
  pull_request:
jobs:
  testy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest -q
```
- `on` — kiedy: push na main i każdy pull request.
- `runs-on: ubuntu-latest` — maszyna z Linuksem (testy Pythona działają tak samo; ścieżki w kodzie pisz przez pathlib!).
- `uses:` — gotowe akcje: pobranie kodu (checkout), instalacja Pythona (setup-python).
- `run:` — polecenia jak w terminalu.
YAML jest czuły na wcięcia (spacje, nie tabulatory) — agent zwykle pisze go dobrze, ale literówka w wcięciu psuje cały plik.
### requirements.txt
Lista zależności do instalacji: `flask`, `requests`, `pytest` — najlepiej z wersjami (`flask==3.1.3`), żeby CI instalował to samo co Ty. `pip freeze` pokazuje zainstalowane wersje (wybierz tylko potrzebne).
### Czytanie wyniku
Zakładka Actions → przebieg → zadanie „testy” → rozwijasz krok. Czerwony krok „python -m pytest -q” pokazuje ten sam raport co lokalnie. Typowe różnice: wielkość liter w nazwach plików (Linux!), brak pliku w repo (był tylko lokalnie), brak zależności w requirements, zmienne środowiskowe (w testach nie używaj prawdziwych kluczy — fałszywy klient).
### Sekrety w CI
Jeśli CI potrzebuje klucza (np. do testu integracyjnego) — Settings → Secrets and variables → Actions, a w YAML `${{ secrets.NAZWA }}`. Nigdy klucz w pliku workflow. W kursie testy nie potrzebują kluczy.
### Koszt
Dla repozytoriów publicznych standardowe runnery GitHuba są bez opłat; dla prywatnych plan Free ma miesięczną pulę minut (aktualny limit w dokumentacji „About billing for GitHub Actions”). Testy kursu trwają ok. minuty.
### Ochrona main
Settings → Rules/Branches: wymagaj przejścia testów przed merge do main. Wtedy nawet agent z uprawnieniem do push nie włączy czerwonej zmiany przez PR.

## 2 · Demonstracja — krok po kroku
**Pierwszy przebieg CI — czerwony, potem zielony**

```
requirements.txt:

flask==3.1.3
requests==2.34.2
pytest==9.2.0

Odznaka w README (opcjonalnie):
![Testy](https://github.com/NAZWA/pod-lipa/actions/workflows/testy.yml/badge.svg)
```

1. Prośba do agenta: „Dodaj .github/workflows/testy.yml (push na main i pull_request, Python 3.12, pip install -r requirements.txt, python -m pytest -q) i requirements.txt z flask, requests, pytest”.
2. Commit, push. Zakładka Actions: przebieg czerwony — test_raport_plik_kursu: brak dane/rezerwacje.csv (plik był w .gitignore).
3. Decyzja: fikcyjne dane szkoleniowe mogą być w repo — usuwasz wpis z .gitignore dla tego jednego pliku, commit. Drugi przebieg: test kalendarza czerwony na Linuksie — w kodzie ścieżka 'dane\\rezerwacje.csv' z ukośnikiem wstecznym.
4. Poprawka przez pathlib (Path("dane") / "rezerwacje.csv"), push — zielono. Odznaka w README.
5. Włączasz regułę: testy muszą przejść przed merge do main.

✔ **Oczekiwany wynik:** CI uruchamia testy przy każdej zmianie, wykrył dwa problemy niewidoczne lokalnie i chroni gałąź main.

## 3 · Jak to uruchomić
1. Plik .github/workflows/testy.yml + requirements.txt → commit → push → zakładka Actions.
2. Zadanie tygodnia → „✔ Sprawdź wynik” (struktura workflow i requirements).

## W praktyce
- Każde repozytorium z kodem: CI od pierwszego tygodnia.
- Reguła: merge tylko z zielonym CI.

## 4 · Ćwiczenie prowadzone
W workflow z lekcji: (1) która gotowa akcja pobiera kod repozytorium (nazwa bez @v…), (2) jaki system ma runner, (3) przy jakich DWÓCH zdarzeniach uruchamia się workflow (wybierz parę). Czas: 15 minut.

📄 `cwiczenia/tydzien_13/ci_github_actions_1.md` · rozwiązanie: `rozwiazania/tydzien_13/ci_github_actions_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
CI jest czerwone, lokalnie zielone. Dopasuj przyczynę: (1) „FileNotFoundError: dane\\rezerwacje.csv”, (2) „ModuleNotFoundError: No module named 'flask'”, (3) „FileNotFoundError: Lipa.JPG” (plik w repo to lipa.jpg). Przyczyny: ścieżka z ukośnikiem wstecznym / brak w requirements.txt / wielkość liter. Czas: 15 minut.

📄 `cwiczenia/tydzien_13/ci_github_actions_2.md` · rozwiązanie: `rozwiazania/tydzien_13/ci_github_actions_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Workflow się nie uruchamia.**
  - Przyczyna: Plik w złym folderze (musi być .github/workflows/) albo błąd YAML.
  - Jak sprawdzić: Zakładka Actions — komunikat o błędzie pliku.
  - Poprawka: Ścieżka .github/workflows/testy.yml, wcięcia spacjami.
- ✘ **Testy w CI wiszą.**
  - Przyczyna: input() albo prawdziwe wywołanie API bez timeout.
  - Jak sprawdzić: Log kroku pytest.
  - Poprawka: input() tylko w __main__, testy z fałszywym klientem.

## Pułapki
- Zielone CI = testy przeszły, a nie „kod jest dobry”. Słabe testy dają zielone CI dla złego kodu.
- Nie wklejaj kluczy do plików workflow — Secrets w ustawieniach repozytorium.

## Dodatkowe zadania
1. Dodaj testy.yml i requirements.txt, doprowadź CI do zielonego (zadanie tygodnia).
2. Dodaj odznakę do README.
3. Włącz wymóg zielonych testów przed merge.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co robi CI?**
  - Automatycznie uruchamia testy przy każdej zmianie na czystej maszynie.
- **Dlaczego w CI wychodzą błędy niewidoczne lokalnie?**
  - Inny system (Linux), czyste środowisko: tylko pliki z repo i zależności z requirements.
- **Gdzie trzymasz klucze potrzebne w CI?**
  - W Secrets repozytorium, odwołanie ${{ secrets.NAZWA }}.

## Co potrafię teraz bez patrzenia na przykład?
Dodajesz workflow GitHub Actions z pytest, utrzymujesz requirements.txt, czytasz i naprawiasz czerwone przebiegi i chronisz main wymogiem testów.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — Building and testing Python (GitHub Actions) (dostęp 20.11.2026) — <https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python>
- GitHub Docs — About billing for GitHub Actions (minuty, repozytoria publiczne) (dostęp 20.11.2026) — <https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions>
- GitHub Docs — Workflow syntax for GitHub Actions (dostęp 20.11.2026) — <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Plik workflow umieszczasz w:
  - A) .github/workflows/
  - B) docs/
  - C) WERYFIKATORY/
  - D) .claude/
- `runs-on: ubuntu-latest` oznacza:
  - A) Windows
  - B) Linux
  - C) Twój komputer
  - D) Telefon
- Zależności dla CI zapisujesz w:
  - A) README
  - B) requirements.txt
  - C) AGENTS.md
  - D) .gitignore
- Zielone CI gwarantuje:
  - A) Brak błędów
  - B) Że testy przeszły
  - C) Bezpieczeństwo
  - D) Zgodność z RODO

Odpowiedzi: A, B, B, B
