# -*- coding: utf-8 -*-
# Wspólny początek plików WERYFIKATORY/test_tNN.py (zbuduj.py wkleja go na górę każdego testu — test musi działać jako jeden plik).
import importlib.util
import os
import re
import sys
import unicodedata
from pathlib import Path

import pytest

WS = Path(os.environ.get("MENTOR_WORKSPACE") or ".").resolve()


def plik(nazwa):
    p = WS / nazwa
    assert p.exists(), f"Brak pliku {nazwa} w katalogu roboczym {WS}"
    return p


def tekst(nazwa):
    return plik(nazwa).read_text(encoding="utf-8", errors="replace")


def modul(nazwa):
    """Importuje plik ucznia <nazwa>.py z katalogu roboczego (świeżo, bez pamięci podręcznej)."""
    p = WS / f"{nazwa}.py"
    assert p.exists(), f"Brak pliku {nazwa}.py w katalogu roboczym {WS}"
    if str(WS) not in sys.path:
        sys.path.insert(0, str(WS))
    spec = importlib.util.spec_from_file_location(f"uczen_{nazwa}", p)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except (OSError, EOFError) as e:
        if "stdin" in str(e) or isinstance(e, EOFError):
            pytest.fail(f"{nazwa}.py wywołuje input() przy imporcie — przenieś input() do bloku if __name__ == \"__main__\":")
        raise
    return m


def funkcja(m, nazwa):
    assert hasattr(m, nazwa) and callable(getattr(m, nazwa)), f"Brak funkcji {nazwa}"
    return getattr(m, nazwa)


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).casefold().replace("ł", "l")
    return "".join(c for c in s if not unicodedata.combining(c))


def sekcje_md(t):
    """{nagłówek_znormalizowany: [linie treści]} dla nagłówków ## w Markdown."""
    wynik, biez = {}, None
    for linia in t.splitlines():
        m = re.match(r"^\s*##\s+(.+?)\s*$", linia)
        if m:
            biez = norm(m.group(1)).strip(" :")
            wynik[biez] = []
        elif biez is not None and linia.strip():
            wynik[biez].append(linia.strip())
    return wynik


def ok(wynik, oczekiwany, opis):
    liczba = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
    if liczba(oczekiwany):
        assert liczba(wynik) and abs(float(wynik) - float(oczekiwany)) < 0.005, f"{opis}: oczekiwano {oczekiwany}, otrzymano {wynik!r}"
    else:
        assert wynik == oczekiwany, f"{opis}: oczekiwano {oczekiwany!r}, otrzymano {wynik!r}"


def rzuca(f, *a, wyjatek=ValueError, opis="", **k):
    try:
        w = f(*a, **k)
    except wyjatek:
        return
    except Exception as e:  # noqa: BLE001
        pytest.fail(f"{opis}: oczekiwano {wyjatek.__name__}, a funkcja rzuciła {type(e).__name__}: {e}")
    pytest.fail(f"{opis}: oczekiwano {wyjatek.__name__}, a funkcja zwróciła {w!r}")


def git(*args):
    """Uruchamia git w katalogu roboczym; zwraca (kod, wyjście). Brak gita → czytelny błąd testu."""
    import shutil
    import subprocess
    if not shutil.which("git"):
        pytest.fail("Nie znaleziono programu git — zainstaluj Git for Windows (lekcja „Git”) i uruchom Mentora ponownie")
    p = subprocess.run(["git", "-C", str(WS), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).strip()


def repo():
    assert (WS / ".git").exists(), f"W katalogu roboczym {WS} nie ma repozytorium Git — wpisz git init (lekcja „Git”)"


# Weryfikator tygodnia 12 — podatna_aplikacja.py, reguły agenta, LICENSE.
import json as _json


def _app(monkeypatch, klucz="klucz-testowy-123"):
    if klucz is None:
        monkeypatch.delenv("FLASK_SECRET_KEY", raising=False)
    else:
        monkeypatch.setenv("FLASK_SECRET_KEY", klucz)
    return funkcja(modul("podatna_aplikacja"), "create_app")()


def test_podatna_xss(monkeypatch):
    k = _app(monkeypatch).test_client()
    t = k.get("/powitanie", query_string={"imie": "<script>alert(1)</script>"}).get_data(as_text=True)
    assert "<script>" not in t, "/powitanie: znacznik <script> z parametru trafia do strony bez zmian — XSS (użyj escape)"
    assert "&lt;script&gt;" in t, "/powitanie: oczekiwano zamiany < na &lt; (escape)"
    assert "Ania" in k.get("/powitanie", query_string={"imie": "Ania"}).get_data(as_text=True), "/powitanie: zwykłe imię powinno się wyświetlać"


def test_podatna_sql(monkeypatch):
    k = _app(monkeypatch).test_client()
    ok(k.get("/szukaj", query_string={"email": "x' OR '1'='1"}).get_json(), [], "/szukaj z atakiem SQL injection — wynik powinien być pusty")
    w = k.get("/szukaj", query_string={"email": "anna@pod-lipa.pl"}).get_json()
    ok([g.get("imie") for g in w], ["Anna"], "/szukaj?email=anna@pod-lipa.pl")


def test_podatna_sekret(monkeypatch):
    ok(_app(monkeypatch).config.get("SECRET_KEY"), "klucz-testowy-123", "SECRET_KEY powinien pochodzić ze zmiennej FLASK_SECRET_KEY")
    with pytest.raises(RuntimeError) as e:
        _app(monkeypatch, klucz=None)
    assert "FLASK_SECRET_KEY" in str(e.value), "komunikat RuntimeError powinien podać nazwę zmiennej FLASK_SECRET_KEY"
    t = tekst("podatna_aplikacja.py")
    assert not re.search(r"SECRET_KEY[\"']?\]?\s*=\s*[\"']", t), "w kodzie jest wpisany SECRET_KEY — tylko ze zmiennej środowiskowej"
    assert "tajne123" not in t, "w kodzie został stary klucz „tajne123”"


def test_podatna_debug():
    t = tekst("podatna_aplikacja.py")
    assert not re.search(r"debug\s*=\s*True", t), "podatna_aplikacja.py: debug=True — usuń (debugger pozwala wykonać kod)"
    assert "0.0.0.0" not in t, "podatna_aplikacja.py: host=\"0.0.0.0\" — usuń"


ENV_REGULY = {"read(./.env)", "read(.env)", "read(**/.env)", "read(./**/.env)", "read(./.env*)", "read(.env*)", "read(//**/.env)"}


def test_agent_reguly():
    p = WS / ".claude" / "settings.json"
    assert p.exists(), "Brak pliku .claude/settings.json w katalogu roboczym (folder .claude w PRACA)"
    try:
        d = _json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        pytest.fail(f".claude/settings.json to nie jest poprawny JSON: {e}")
    perm = d.get("permissions") or {}
    deny = [str(r).replace(" ", "").lower() for r in perm.get("deny") or []]
    assert any(r in ENV_REGULY for r in deny), ".claude/settings.json: w permissions.deny brak reguły Read dla .env (np. \"Read(./.env)\")"
    assert any(r.startswith("bash(") for r in deny), ".claude/settings.json: w permissions.deny brak żadnej reguły Bash(…) (np. \"Bash(curl *)\")"
    allow = [str(r).replace(" ", "").lower() for r in perm.get("allow") or []]
    assert not any(r in ("bash", "bash(*)") for r in allow), ".claude/settings.json: allow dla całego Bash znosi ostrożność — usuń"
    assert str(perm.get("defaultMode") or "").lower() != "bypasspermissions", ".claude/settings.json: defaultMode bypassPermissions — nie na Twoim komputerze"


def test_agent_opis():
    s = sekcje_md(tekst("bezpieczenstwo_agenta.md"))
    for k in ("reguly", "test regul", "obce repozytorium"):
        assert k in s and any(len(l.strip("-* ").strip()) >= 3 for l in s[k]), f"bezpieczenstwo_agenta.md: brak niepustej sekcji „## {k}”"


def test_licencja():
    t = tekst("LICENSE")
    glowa = t[:400]
    assert re.search(r"MIT License|Apache License|GNU GENERAL PUBLIC LICENSE", glowa, re.I), "LICENSE: nie rozpoznano licencji (MIT, Apache-2.0, GPL-3.0) — użyj szablonu z GitHuba lub choosealicense.com"
    if re.search(r"MIT License", glowa, re.I):
        m = re.search(r"Copyright \(c\)\s*(20\d\d)\s+(.+)", t)
        assert m and m.group(2).strip() and "[" not in m.group(2), "LICENSE (MIT): uzupełnij linię Copyright (c) ROK Imię Nazwisko"
