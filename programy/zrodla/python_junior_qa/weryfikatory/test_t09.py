# Weryfikator tygodnia 9 — przypadki testowe, raporty błędów sklepu testowego, GitHub Actions z pytest-html, repozytorium testów (struktura POM, CI w README).


def test_przypadki_testowe():
    t = tekst("przypadki_testowe.md")
    naglowek = next((l for l in t.splitlines() if l.strip().startswith("|") and "oczekiwany" in norm(l)), None)
    assert naglowek, "przypadki_testowe.md: tabela z nagłówkiem zawierającym kolumnę „Oczekiwany wynik”"
    kol = [norm(c.strip()) for c in naglowek.strip().strip("|").split("|")]
    for k in ("id", "kroki", "oczekiwany"):
        assert any(k in c for c in kol), f"przypadki_testowe.md: brak kolumny „{k}” w nagłówku tabeli"
    io = next(i for i, c in enumerate(kol) if "oczekiwany" in c)
    wiersze = [[c.strip() for c in l.strip().strip("|").split("|")] for l in t.splitlines() if re.match(r"^\s*\|\s*TC-\d+", l)]
    assert len(wiersze) >= 10, f"przypadki_testowe.md: {len(wiersze)} przypadków (wiersze „| TC-01 | …”) — potrzeba 10"
    for w in wiersze:
        assert len(w) > io and len(w[io].split()) >= 2, f"{w[0]}: wpisz oczekiwany wynik (co najmniej 2 słowa)"
    ids = [w[0] for w in wiersze]
    assert len(set(ids)) == len(ids), "przypadki_testowe.md: identyfikatory TC-… muszą być unikalne"
    negatywne = sum(1 for w in wiersze if any(s in norm(" ".join(w)) for s in ("blad", "bledn", "odrzuc", "komunikat", "pust", "nie ")))
    assert negatywne >= 3, "przypadki_testowe.md: co najmniej 3 przypadki negatywne (złe dane → komunikat / odrzucenie)"


DEFEKTY = [("10", "kosz"), ("00000",), ("wielk", "szuk"), ("wielk", "login"), ("stan", "kosz"), ("kot10",), ("zszywk",)]


def test_bug_raporty():
    t = tekst("bug_raporty.md")
    czesci = re.split(r"^##\s+", t, flags=re.M)[1:]
    raporty = [c for c in czesci if norm(c.split("\n", 1)[0]).startswith("bug")]
    assert len(raporty) >= 3, f"bug_raporty.md: {len(raporty)} raportów — potrzeba 3 sekcji „## BUG-01: …”"
    for r in raporty:
        tyt = r.split("\n", 1)[0].strip()
        n = norm(r)
        for pole in ("srodowisko", "kroki", "oczekiwany", "rzeczywisty", "waznosc"):
            assert pole in n, f"raport „{tyt}”: brak pola „{pole}”"
        assert re.search(r"^\s*1\.", r, re.M) and re.search(r"^\s*2\.", r, re.M), f"raport „{tyt}”: kroki ponumerowane (1., 2., …)"
        assert len(tyt.split()) >= 4, f"raport „{tyt}”: tytuł mówi gdzie + co + w jakich warunkach (co najmniej 4 słowa)"
    trafione = sum(1 for r in raporty if any(all(k in norm(r) for k in d) for d in DEFEKTY))
    assert trafione >= 2, "bug_raporty.md: co najmniej 2 raporty dotyczą prawdziwych defektów sklepu testowego (porównaj działanie sklepu z wymaganiami w jego README)"


def _workflow():
    pliki = sorted((WS / ".github" / "workflows").glob("*.y*ml")) if (WS / ".github" / "workflows").exists() else []
    assert pliki, "Brak pliku workflow w .github/workflows/ (np. .github/workflows/tests.yml — folder .github z kropką)"
    return pliki[0], pliki[0].read_text(encoding="utf-8")


def test_github_actions():
    p, t = _workflow()
    assert "\t" not in t, f"{p.name}: tabulator w YAML — wcięcia tylko spacjami"
    for f in ("actions/checkout", "actions/setup-python", "pip install -r requirements.txt", "pytest"):
        assert f in t, f"{p.name}: brak „{f}”"
    assert re.search(r"\bpush\b", t), f"{p.name}: uruchamiaj przy push (on: [push, pull_request])"
    assert not re.search(r"(password|token|api_key)\s*:\s*['\"]?\w{6,}", t, re.I), f"{p.name}: sekret w workflow — użyj ${{ secrets.NAZWA }}"


def test_pytest_html():
    p, t = _workflow()
    assert "--html" in t, f"{p.name}: pytest z opcją --html=raport.html (pytest-html)"
    assert "upload-artifact" in t and re.search(r"if:\s*always\(\)", t), f"{p.name}: raport jako artefakt (actions/upload-artifact) z if: always()"
    assert re.search(r"^pytest-html", tekst("requirements.txt"), re.M | re.I), "requirements.txt: dopisz pytest-html (CI instaluje tylko to, co jest na liście)"


def test_repo_testow():
    for f in ("pages/__init__.py", "conftest.py"):
        assert (WS / f).exists(), f"Brak {f} — struktura projektu testów: pages/ (Page Objecty), tests/ (testy), conftest.py (fixtury)"
    strony = [p for p in (WS / "pages").glob("*.py") if p.name != "__init__.py"]
    assert len(strony) >= 2, "pages/: co najmniej 2 Page Objecty (np. login_page.py, cart_page.py)"
    testy = list((WS / "tests").glob("test_*.py")) if (WS / "tests").exists() else []
    assert testy, "tests/: pliki test_*.py z testami E2E"
    liczba = sum(len(re.findall(r"^def test_\w+", p.read_text(encoding="utf-8"), re.M)) for p in testy)
    assert liczba >= 8, f"tests/: {liczba} testów — potrzeba co najmniej 8 (5 z tygodnia 8 + nowe: koszyk, zamówienie, przypadki negatywne)"
    r = tekst("README.md")
    assert "badge.svg" in r, "README.md: odznaka CI ![Testy](https://github.com/…/actions/workflows/tests.yml/badge.svg)"
    s = sekcje_md(r)
    jt = next((k for k in s if "jak testuj" in k), None)
    assert jt and len(" ".join(s[jt]).split()) >= 15, "README.md: sekcja „## Jak testuję” (co najmniej 15 słów: poziomy, narzędzia, jak uruchomić)"
