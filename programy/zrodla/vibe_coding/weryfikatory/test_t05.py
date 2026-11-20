# Weryfikator tygodnia 5 — AGENTS.md/CLAUDE.md i konwerter.py.

TAJEMNICE = [r"sk-[A-Za-z0-9_\-]{16,}", r"ghp_[A-Za-z0-9]{20,}", r"(?i)(api[_-]?key|token|hasło|haslo|password)\s*[:=]\s*\S{6,}"]


def test_instrukcje_agents():
    t = tekst("AGENTS.md")
    linie = t.splitlines()
    assert len(linie) <= 200, f"AGENTS.md ma {len(linie)} linii — skróć do najważniejszych (≤ 200)"
    for wz in TAJEMNICE:
        assert not re.search(wz, t), "AGENTS.md: coś wygląda na klucz, token albo hasło — usuń je z pliku (instrukcje trafiają do repozytorium)"
    s = sekcje_md(t)
    for k in ("projekt", "polecenia", "zasady", "nie ruszaj"):
        assert k in s and s[k], f"AGENTS.md: brak niepustej sekcji „## {k.capitalize()}”"
    assert any("pytest" in l for l in s["polecenia"]), "AGENTS.md: w sekcji Polecenia brak polecenia uruchamiania testów (python -m pytest -q)"
    assert sum(1 for l in s["zasady"] if l.startswith(("-", "*"))) >= 3, "AGENTS.md: potrzeba co najmniej 3 zasad (linie „- …”) w sekcji Zasady"
    assert sum(1 for l in s["nie ruszaj"] if l.startswith(("-", "*"))) >= 1, "AGENTS.md: sekcja Nie ruszaj potrzebuje co najmniej jednej pozycji"


def test_instrukcje_claude():
    t = tekst("CLAUDE.md")
    assert any(l.strip() == "@AGENTS.md" for l in t.splitlines()), "CLAUDE.md: brak osobnej linii @AGENTS.md (import wspólnych instrukcji)"
    for wz in TAJEMNICE:
        assert not re.search(wz, t), "CLAUDE.md: coś wygląda na klucz, token albo hasło — usuń"


def _k():
    m = modul("konwerter")
    return funkcja(m, "parsuj_kwote"), funkcja(m, "zl_na_eur"), funkcja(m, "formatuj_zl")


def test_konwerter_parsuj():
    p, _, _ = _k()
    for t, w in (("1 234,56 zł", 1234.56), ("1234.56", 1234.56), ("  99 zł", 99), ("1 234 zł", 1234), ("0,5", 0.5), ("12 000,00", 12000)):
        ok(p(t), w, f"parsuj_kwote({t!r})")


def test_konwerter_parsuj_zle():
    p, _, _ = _k()
    for t in ("abc", "", "12,3,4", "zł"):
        rzuca(p, t, opis=f"parsuj_kwote({t!r})")


def test_konwerter_eur():
    _, e, _ = _k()
    ok(e(430, 4.30), 100.0, "zl_na_eur(430, 4.30)")
    ok(e(100, 4.27), 23.42, "zl_na_eur(100, 4.27) — zaokrąglenie do centów")
    ok(e(0, 4.3), 0, "zl_na_eur(0, 4.3)")
    rzuca(e, -5, 4.3, opis="zl_na_eur(-5, 4.3)")
    rzuca(e, 100, 0, opis="zl_na_eur(100, 0)")
    rzuca(e, 100, -4.3, opis="zl_na_eur(100, -4.3)")


def test_konwerter_formatuj():
    _, _, f = _k()
    for k, w in ((1234.56, "1 234,56 zł"), (5, "5,00 zł"), (1000000, "1 000 000,00 zł"), (0.1, "0,10 zł"), (999.999, "1 000,00 zł")):
        wynik = f(k).replace(" ", " ")
        ok(wynik, w, f"formatuj_zl({k!r})")
