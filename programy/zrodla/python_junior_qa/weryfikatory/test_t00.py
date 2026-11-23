# Weryfikator tygodnia 0 — CLAUDE.md z zasadami, repozytorium Git z pierwszym commitem, notatki własnymi słowami.


def _punkty(t):
    return [l.strip()[1:].strip() for l in t.splitlines() if l.strip().startswith(("-", "*")) and len(l.strip()) > 2]


def test_claude_md():
    t = tekst("CLAUDE.md")
    p = _punkty(t)
    assert len(p) >= 3, f"CLAUDE.md: {len(p)} zasad w formie listy — potrzeba co najmniej 3 linii zaczynających się od „- ”"
    assert any("rozwiaza" in norm(x) or "gotow" in norm(x) for x in p), \
        "CLAUDE.md: dopisz zasadę o tym, że asystent nie podaje gotowych rozwiązań zadań (np. „- Nie podawaj gotowych rozwiązań — najpierw wskazówka”)"
    assert all(len(x.split()) >= 3 for x in p), "CLAUDE.md: każda zasada to pełne zdanie (co najmniej 3 słowa)"


def test_repo():
    repo()
    kod, log = git("log", "--oneline")
    assert kod == 0 and log.strip(), "Repozytorium nie ma jeszcze commita — git add i git commit -m \"…\""
    kod, pliki = git("ls-files")
    sledzone = set(pliki.split())
    for f in ("hello.py", "README.md"):
        assert f in sledzone, f"{f} nie jest w repozytorium (git ls-files) — git add {f} i commit"
    assert tekst("README.md").lstrip().startswith("# "), "README.md: pierwsza linia to tytuł w Markdown, np. „# Nauka Pythona”"
    kod, adres = git("remote", "get-url", "origin")
    assert kod == 0 and "github.com" in adres, "Brak zdalnego repozytorium origin na GitHubie — git remote add origin https://github.com/…/nauka-python.git i git push -u origin main"


def test_notatki():
    s = sekcje_md(tekst("notatki.md"))
    for nazwa, klucz in (("Zmienna", "zmienna"), ("Funkcja", "funkcja"), ("Pętla", "petla")):
        assert klucz in s, f"notatki.md: brak sekcji „## {nazwa}”"
        slowa = len(" ".join(s[klucz]).split())
        assert slowa >= 20, f"notatki.md: sekcja „## {nazwa}” ma {slowa} słów — napisz co najmniej 20 słów własnymi słowami, z przykładem"
