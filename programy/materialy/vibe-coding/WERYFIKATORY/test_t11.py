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


# Weryfikator tygodnia 11 — pogoda.py (API i klucz), porzadki.py, /api/wolne.
import tempfile


class _Klient:
    def __init__(self, odp):
        self.odp, self.wywolania = odp, []

    def __call__(self, url, params, headers):
        self.wywolania.append((url, dict(params or {}), dict(headers or {})))
        return self.odp


def _p():
    return funkcja(modul("pogoda"), "pobierz_temperature")


def test_pogoda_dziala(monkeypatch):
    monkeypatch.setenv("POGODA_API_KEY", "SEKRET-TESTOWY-123")
    k = _Klient({"current": {"temp": 4.5}})
    ok(_p()("Radzyń", klient=k), 4.5, "pobierz_temperature z odpowiedzią temp 4.5")
    assert k.wywolania, "funkcja nie wywołała klienta"
    url, params, headers = k.wywolania[0]
    assert headers.get("X-API-Key") == "SEKRET-TESTOWY-123", "klucz powinien trafić do nagłówka X-API-Key (z POGODA_API_KEY)"
    assert params.get("miasto") == "Radzyń", "miasto powinno trafić do params jako „miasto”"
    assert "SEKRET-TESTOWY-123" not in url, "klucz nie może być w adresie URL"


def test_pogoda_bez_klucza(monkeypatch):
    monkeypatch.delenv("POGODA_API_KEY", raising=False)
    try:
        _p()("Radzyń", klient=_Klient({"current": {"temp": 1}}))
    except RuntimeError as e:
        assert "POGODA_API_KEY" in str(e), "komunikat RuntimeError powinien podać nazwę zmiennej POGODA_API_KEY"
        return
    pytest.fail("bez zmiennej POGODA_API_KEY funkcja powinna rzucić RuntimeError (nie używaj klucza domyślnego w kodzie)")


def test_pogoda_zle_dane(monkeypatch):
    monkeypatch.setenv("POGODA_API_KEY", "k")
    rzuca(_p(), "Radzyń", klient=_Klient({"blad": "x"}), opis="pobierz_temperature dla odpowiedzi bez current.temp")
    rzuca(_p(), "  ", klient=_Klient({"current": {"temp": 1}}), opis="pobierz_temperature z pustym miastem")


def test_pogoda_bez_klucza_w_kodzie():
    t = tekst("pogoda.py")
    assert re.search(r"os\.environ|os\.getenv|getenv\(", t), "pogoda.py: klucz musi pochodzić ze zmiennej środowiskowej (os.environ)"
    assert not re.search(r"environ\.get\(\s*[\"']POGODA_API_KEY[\"']\s*,\s*[\"'][^\"']+[\"']", t), "pogoda.py: klucz „domyślny” w os.environ.get(…, \"…\") — usuń go"
    assert "timeout" in t, "pogoda.py: domyślny klient powinien ustawiać timeout w requests.get"
    gi = WS / ".gitignore"
    assert gi.exists() and ".env" in gi.read_text(encoding="utf-8"), ".gitignore: brak wpisu .env"


def _u():
    return funkcja(modul("porzadki"), "uporzadkuj")


def _folder(td):
    d = Path(td)
    for n in ("Lipa.JPG", "faktura.pdf", "goscie.csv", "notatka", "plan.txt", ".ukryty.txt"):
        (d / n).write_text(n, encoding="utf-8")
    (d / "zdjecia").mkdir()
    (d / "zdjecia" / "Lipa.JPG").write_text("stare", encoding="utf-8")
    (d / "podfolder").mkdir()
    return d


def test_porzadki_proba():
    with tempfile.TemporaryDirectory() as td:
        d = _folder(td)
        przed = sorted(p.name for p in d.iterdir())
        plan = [tuple(x) for x in _u()(str(d))]
        po = sorted(p.name for p in d.iterdir())
    ok(po, przed, "tryb próby (wykonaj=False) nie może zmieniać plików")
    oczek = [("Lipa.JPG", "zdjecia/Lipa_1.JPG"), ("faktura.pdf", "dokumenty/faktura.pdf"), ("goscie.csv", "dane/goscie.csv"), ("notatka", "inne/notatka"), ("plan.txt", "inne/plan.txt")]
    plan = [(a, b.replace("\\", "/")) for a, b in plan]
    ok(plan, oczek, "plan porządkowania (posortowany po nazwie pliku; konflikt Lipa.JPG → Lipa_1.JPG; ukryte i foldery pominięte)")


def test_porzadki_wykonaj():
    with tempfile.TemporaryDirectory() as td:
        d = _folder(td)
        _u()(str(d), wykonaj=True)
        assert (d / "zdjecia" / "Lipa.JPG").read_text(encoding="utf-8") == "stare", "istniejący plik zdjecia/Lipa.JPG został nadpisany"
        assert (d / "zdjecia" / "Lipa_1.JPG").exists(), "brak zdjecia/Lipa_1.JPG po przeniesieniu"
        for p in ("dokumenty/faktura.pdf", "dane/goscie.csv", "inne/notatka", "inne/plan.txt"):
            assert (d / p).exists(), f"brak {p} po przeniesieniu"
        assert (d / ".ukryty.txt").exists() and (d / "podfolder").is_dir(), "plik ukryty i podfolder powinny zostać na miejscu"
        log = d / ".porzadki.log"
        assert log.exists(), "brak logu .porzadki.log w porządkowanym folderze"
        ok(len([l for l in log.read_text(encoding="utf-8").splitlines() if l.strip()]), 5, "liczba linii w .porzadki.log (jedna na przeniesiony plik)")


def _wolne_app():
    m = modul("app")
    rez = [{"pokoj": "Lipowy", "od": "2026-12-20", "do": "2026-12-23"}, {"pokoj": "Klonowy", "od": "2026-12-22", "do": "2026-12-27"}]
    return funkcja(m, "create_app")(rezerwacje=rez).test_client()


def test_wolne_wyniki():
    k = _wolne_app()
    for od, do, w in (("2026-12-21", "2026-12-22", ["Dębowy", "Klonowy"]), ("2026-12-23", "2026-12-25", ["Lipowy", "Dębowy"]), ("2026-12-01", "2026-12-05", ["Lipowy", "Dębowy", "Klonowy"])):
        o = k.get(f"/api/wolne?od={od}&do={do}")
        ok(o.status_code, 200, f"/api/wolne?od={od}&do={do}")
        ok(o.get_json(), {"od": od, "do": do, "wolne": w}, f"/api/wolne?od={od}&do={do}")


def test_wolne_bledy():
    k = _wolne_app()
    for q in ("od=2026-12-21", "do=2026-12-22", "od=2026-13-01&do=2026-13-03", "od=jutro&do=pojutrze", "od=2026-12-25&do=2026-12-24", "od=2026-12-25&do=2026-12-25"):
        o = k.get(f"/api/wolne?{q}")
        ok(o.status_code, 400, f"/api/wolne?{q}")
        assert "blad" in (o.get_json() or {}), f"/api/wolne?{q}: brak klucza „blad” w JSON"


def test_wolne_stare_trasy():
    k = _wolne_app()
    ok((k.get("/api/cena?noce=2&osoby=2").get_json() or {}).get("koszt"), 480, "/api/cena nadal działa po dodaniu /api/wolne")
    k2 = funkcja(modul("app"), "create_app")().test_client()
    ok(k2.get("/api/wolne?od=2026-12-01&do=2026-12-02").get_json()["wolne"], ["Lipowy", "Dębowy", "Klonowy"], "create_app() bez rezerwacji — wszystkie pokoje wolne")
