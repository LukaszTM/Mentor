# Weryfikator tygodnia 13 — README.md i CI (GitHub Actions).

SEKCJE = ["opis", "wymagania", "instalacja", "uruchomienie", "testy", "konfiguracja", "ograniczenia", "jak powstal", "licencja"]
TAJ = [r"sk-[A-Za-z0-9_\-]{16,}", r"ghp_[A-Za-z0-9]{20,}"]
ZAMIENNIKI = ("wygeneruj", "twoj", "przyklad", "losow", "xxx", "wartosc", "klucz", "...", "<", "$", "{")


def _sekrety(t):
    """Wzorce kluczy i przypisania NAZWA=wartość, które nie wyglądają na zamiennik (np. „twoj_klucz”)."""
    if any(re.search(wz, t) for wz in TAJ):
        return True
    for m in re.finditer(r"(?i)(api[_-]?key|secret[_-]?key|token|haslo|hasło|password)\s*[:=]\s*[\"']?([^\s\"'`]{8,})", t):
        w = norm(m.group(2))
        if not any(z in w for z in ZAMIENNIKI) and re.search(r"\d", w) and re.search(r"[a-z]", w):
            return True
    return False


def test_readme():
    t = tekst("README.md")
    s = sekcje_md(t)
    for k in SEKCJE:
        assert any(n == k or n.startswith(k) for n in s), f"README.md: brak sekcji „## {k.capitalize()}”"
    assert "pytest" in t, "README.md: brak polecenia uruchomienia testów (python -m pytest -q)"
    assert "bin/activate" not in t, "README.md: polecenie z Linuksa (…/bin/activate) — podaj wersję dla Windows (.venv\\Scripts\\activate)"
    assert not _sekrety(t), "README.md: coś wygląda na wartość klucza/hasła — w README tylko nazwy zmiennych (albo zamiennik typu twoj_klucz)"
    n = len([l for l in t.splitlines() if l.strip()])
    assert n >= 25, f"README.md ma {n} niepustych linii — za mało na pełną dokumentację (≥ 25)"


def test_ci():
    req = [l.strip().lower() for l in tekst("requirements.txt").splitlines() if l.strip() and not l.strip().startswith("#")]
    for p in ("flask", "pytest"):
        assert any(re.match(rf"{p}\b", l) for l in req), f"requirements.txt: brak {p}"
    wf = list((WS / ".github" / "workflows").glob("*.y*ml")) if (WS / ".github" / "workflows").is_dir() else []
    assert wf, "Brak pliku workflow w .github/workflows/ (np. testy.yml)"
    t = "\n".join(p.read_text(encoding="utf-8") for p in wf)
    for fraza, opis in (("actions/checkout", "kroku actions/checkout"), ("actions/setup-python", "kroku actions/setup-python"),
                        ("requirements.txt", "instalacji zależności pip install -r requirements.txt"), ("pytest", "uruchomienia pytest"),
                        ("pull_request", "zdarzenia pull_request"), ("push", "zdarzenia push")):
        assert fraza in t, f"workflow: brak {opis}"
    assert not _sekrety(t), "workflow: coś wygląda na sekret wpisany w plik — użyj ${{ secrets.NAZWA }}"
