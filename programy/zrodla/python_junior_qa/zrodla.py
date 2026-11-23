# -*- coding: utf-8 -*-
"""Źródła kursu „Python od zera → Junior QA” — wyłącznie materiały merytoryczne: dokumentacja oficjalna, standardy (ISTQB/SJSI, OWASP),
polskie tłumaczenia dokumentacji i raporty rynku pracy. Każde źródło: [tytuł, adres https, data dostępu]. Adresy sprawdzone 23.11.2026."""

D = "dostęp 23.11.2026"

# --- Python (polskie tłumaczenie oficjalnej dokumentacji + oryginał)
PY_TUT_PL = ["Python — Poradnik (oficjalna dokumentacja, wersja polska)", "https://docs.python.org/pl/3/tutorial/", D]
PY_TUT_INTRO = ["Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy)", "https://docs.python.org/pl/3/tutorial/introduction.html", D]
PY_TUT_CTRL = ["Python — Poradnik: Więcej narzędzi kontroli przepływu (if, for, range, funkcje)", "https://docs.python.org/pl/3/tutorial/controlflow.html", D]
PY_TUT_DS = ["Python — Poradnik: Struktury danych (listy, krotki, słowniki)", "https://docs.python.org/pl/3/tutorial/datastructures.html", D]
PY_TUT_ERR = ["Python — Poradnik: Błędy i wyjątki", "https://docs.python.org/pl/3/tutorial/errors.html", D]
PY_TUT_IO = ["Python — Poradnik: Wejście i wyjście (f-stringi, pliki)", "https://docs.python.org/pl/3/tutorial/inputoutput.html", D]
PY_TUT_MOD = ["Python — Poradnik: Moduły", "https://docs.python.org/pl/3/tutorial/modules.html", D]
PY_TUT_CLS = ["Python — Poradnik: Klasy", "https://docs.python.org/pl/3/tutorial/classes.html", D]
PY_TUT_VENV = ["Python — Poradnik: Środowiska wirtualne i pakiety", "https://docs.python.org/pl/3/tutorial/venv.html", D]
PY_STDTYPES = ["Python — Built-in Types (str, list, dict: metody)", "https://docs.python.org/3/library/stdtypes.html", D]
PY_CSV = ["Python — csv: CSV File Reading and Writing", "https://docs.python.org/3/library/csv.html", D]
PY_SQLITE = ["Python — sqlite3: DB-API 2.0 interface for SQLite (placeholders ?)", "https://docs.python.org/3/library/sqlite3.html", D]
PY_DATETIME = ["Python — datetime: Basic date and time types", "https://docs.python.org/3/library/datetime.html", D]
PY_RANDOM = ["Python — random: Generate pseudo-random numbers", "https://docs.python.org/3/library/random.html", D]
PY_PDB = ["Python — pdb: The Python Debugger (breakpoint())", "https://docs.python.org/3/library/pdb.html", D]
PY_JSON = ["Python — json: JSON encoder and decoder", "https://docs.python.org/3/library/json.html", D]
PY_PEP8 = ["PEP 8 — Style Guide for Python Code", "https://peps.python.org/pep-0008/", D]
PY_PEP257 = ["PEP 257 — Docstring Conventions", "https://peps.python.org/pep-0257/", D]
PY_315 = ["Python 3.15.0 — informacja o wydaniu (9.10.2026; instalator Windows, Python install manager)", "https://python.org/downloads/release/python-3150/", D]
PY_WIN = ["Python — Using Python on Windows", "https://docs.python.org/3/using/windows.html", D]

# --- Git i GitHub
GIT_PL = ["Pro Git (wydanie 2, wersja polska) — Scott Chacon, Ben Straub", "https://git-scm.com/book/pl/v2", D]
GIT_PL_PODST = ["Pro Git PL — Podstawy Gita (rejestrowanie zmian, historia, cofanie)", "https://git-scm.com/book/pl/v2/Podstawy-Gita-Rejestrowanie-zmian-w-repozytorium", D]
GIT_PL_GAL = ["Pro Git PL — Gałęzie Gita", "https://git-scm.com/book/pl/v2/Ga%C5%82%C4%99zie-Gita-Czym-jest-ga%C5%82%C4%85%C5%BA", D]
GIT_DOCS = ["Git — Reference (git restore, git stash, git log)", "https://git-scm.com/docs", D]
GH_PR = ["GitHub Docs — About pull requests", "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests", D]
GH_ACTIONS_PY = ["GitHub Docs — Building and testing Python (actions/checkout@v6, actions/setup-python, pytest)", "https://docs.github.com/en/actions/tutorials/build-and-test-code/python", D]
GH_README = ["GitHub Docs — About READMEs", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes", D]

# --- testowanie: ISTQB / SJSI (PL), pytest, Selenium
ISTQB_CTFL = ["ISTQB — Certified Tester Foundation Level (CTFL) v4.0 (sylabus v4.0.1, egzamin 40 pytań, próg 26, 60 min)", "https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0", D]
SJSI_CTFL_PL = ["SJSI — Egzamin przykładowy CTFL 4.0, wersja polska (terminologia: pomyłka, defekt, awaria, klasy równoważności, wartości brzegowe)", "https://testerzy.pl/pliki/certyfikacja/egzamin-przykladowy-ctfl-ver-4-0-pytania-pl.pdf/podglad", D]
ISTQB_SLOWNIK = ["ISTQB Glossary — słownik terminów testowania (dostępny w języku polskim)", "https://glossary.istqb.org/", D]
PYTEST_START = ["pytest — Get Started", "https://docs.pytest.org/en/stable/getting-started.html", D]
PYTEST_ASSERT = ["pytest — How to write and report assertions in tests", "https://docs.pytest.org/en/stable/how-to/assert.html", D]
PYTEST_FIX = ["pytest — How to use fixtures", "https://docs.pytest.org/en/stable/how-to/fixtures.html", D]
PYTEST_PARAM = ["pytest — How to parametrize fixtures and test functions", "https://docs.pytest.org/en/stable/how-to/parametrize.html", D]
PYTEST_TMP = ["pytest — How to use temporary directories and files in tests (tmp_path)", "https://docs.pytest.org/how-to/tmp_path.html", D]
PYTEST_CHANGES = ["pytest — Changelog (9.2.0 z 27.10.2026; 9.0 bez Pythona 3.9)", "https://pytest.org/en/latest/changelog.html", D]
SEL_MANAGER = ["Selenium — Selenium Manager (sterowniki i przeglądarki automatycznie, od 4.6; cache, SE_OFFLINE)", "https://selenium.dev/documentation/selenium_manager", D]
SEL_WAITS = ["Selenium (Python) — Waits: explicit i implicit", "https://selenium-python.readthedocs.io/waits.html", D]
SEL_POM = ["Selenium — Page object models (test practices)", "https://selenium.dev/documentation/test_practices/encouraged/page_object_models", D]
SEL_API_WAIT = ["Selenium Python API — selenium.webdriver.support.wait (WebDriverWait)", "https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.wait.html", D]

# --- web, bazy, bezpieczeństwo
FLASK = ["Flask — dokumentacja (3.1.x): Quickstart, szablony, testowanie", "https://flask.palletsprojects.com/", D]
OWASP_SQLI = ["OWASP — SQL Injection Prevention Cheat Sheet (zapytania parametryzowane)", "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html", D]
OWASP_QP = ["OWASP — Query Parameterization Cheat Sheet", "https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html", D]

# --- narzędzia
PYCHARM = ["JetBrains — Unified PyCharm (darmowe funkcje podstawowe, Pro w subskrypcji, Community włączony do jednego produktu)", "https://www.jetbrains.com/help/pycharm/2026.3/unified-pycharm.html", D]
CC_SETUP = ["Claude Code — Set up Claude Code (instalacja, Windows)", "https://code.claude.com/docs/en/setup", D]
CC_BEST = ["Claude Code — Best practices", "https://code.claude.com/docs/en/best-practices", D]
CC_MEM = ["Claude Code — How Claude remembers your project (CLAUDE.md)", "https://code.claude.com/docs/en/memory", D]

# --- rynek pracy (PL)
RYNEK_JJ = ["Antyweb — barometr justjoin.it i rocketjobs.pl za I kw. 2026: oferty juniorskie 5% ogłoszeń (10.04.2026)", "https://antyweb.pl/rynek-pracy-it-juniorzy", D]
RYNEK_BDJ = ["Bulldogjob — IT Community Report 2025: wynagrodzenia testerów manualnych (junior UoP 6 900 zł brutto)", "https://bulldogjob.com/it-report/salaries/tester", D]
