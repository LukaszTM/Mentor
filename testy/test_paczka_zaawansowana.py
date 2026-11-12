# -*- coding: utf-8 -*-
"""Mechanizmy dla kursów w stylu „AI Developer Lab”: pakiety z manifestu, niezależne testy z paczki (test_zewnetrzny) z weryfikacją SHA-256,
lokalny serwer API uruchamiany tylko na żądanie po weryfikacji sumy, zmienne MENTOR_* dla kodu ucznia, rubryka oceny własnej."""

import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest

import cwiczenia as C
import paczki
import program
import srodowisko as S

ID = "kurs-zaaw"
TEST_ZACHOWANIA = '''import importlib.util, os
from pathlib import Path
import pytest
WORK = Path(os.environ["MENTOR_WORKSPACE"])

def load(name):
    p = WORK / name
    assert p.is_file(), f"Brak pliku {p}"
    spec = importlib.util.spec_from_file_location("student_module", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

@pytest.mark.parametrize("arg, oczek", [(200, "PASS"), (404, "NOT FOUND"), (500, "FAIL")])
def test_ocena(arg, oczek):
    m = load("ocena.py")
    assert callable(getattr(m, "ocen", None)), "Brak funkcji ocen"
    assert m.ocen(arg) == oczek

def test_inny():
    assert True
'''
API = '''import json, sys
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        raw = json.dumps({"status": "ok"}).encode()
        self.send_response(200 if self.path == "/health" else 404); self.send_header("Content-Length", str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def log_message(self, *a): pass
HTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else PORT), H).serve_forever()
'''


def _sha(b):
    return hashlib.sha256(b).hexdigest()


@pytest.fixture(scope="module")
def kurs(kurs_json, tmp_path_factory):
    """Importuje paczkę z manifestem (python_packages, local_api, sandbox), WERYFIKATORY i INTEGRITY.json; zwraca (id, katalog paczki, PRACA)."""
    import socket
    with socket.socket() as sk:
        sk.bind(("127.0.0.1", 0))
        port = sk.getsockname()[1]
    src = tmp_path_factory.mktemp("src")
    d = dict(kurs_json)
    d["id"] = ID
    d["wersja"] = "1.0"
    d["nazwa"] = "Kurs zaawansowany"
    d.pop("srodowisko", None)
    (src / "kurs_mentor.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    (src / "WERYFIKATORY").mkdir()
    (src / "WERYFIKATORY" / "test_zachowania.py").write_text(TEST_ZACHOWANIA, encoding="utf-8")
    (src / "srodowiska").mkdir()
    (src / "srodowiska" / "api.py").write_text(API.replace("PORT", str(port)), encoding="utf-8")
    (src / "srodowiska" / "qa_sandbox.html").write_text("<html><title>QA</title></html>", encoding="utf-8")
    integ = {p.relative_to(src).as_posix(): _sha(p.read_bytes()) for p in src.rglob("*") if p.is_file()}
    (src / "INTEGRITY.json").write_text(json.dumps(integ), encoding="utf-8")
    man = {"schema": "mentor-course/1", "course_id": ID, "version": "1.0", "entrypoint": "kurs_mentor.json",
           "requirements": {"python": ">=3.11,<3.14", "python_packages": ["pytest", "requests"], "browser": "edge", "browser_from_week": 4},
           "local_api": {"script": "srodowiska/api.py", "port": port, "health_path": "/health", "sha256": integ["srodowiska/api.py"]},
           "sandbox_html": "srodowiska/qa_sandbox.html"}
    z = paczki.zbuduj_paczke(src, tmp_path_factory.mktemp("zip") / "kurs.zip", manifest=man)
    w = paczki.importuj_zip(z)
    yield ID, w["katalog"] / "paczka", w["praca"], port
    paczki.usun_kurs(ID)


def _sr(kurs):
    kid, mat, praca, port = kurs
    meta = program.meta_kursu(kid)
    return S.Srodowisko(kid, meta["wymagania"]), mat, praca, port


def test_manifest_pakiety_i_api(kurs):
    sr, mat, praca, port = _sr(kurs)
    assert sr.pakiety_wymagane() == ["pytest", "requests"], "python_packages z manifestu"
    assert sr.api_lokalne()["port"] == port and sr.api_lokalne()["skrypt"] == "srodowiska/api.py"
    env = sr.env_ucznia(praca)
    assert env["MENTOR_WORKSPACE"] == str(praca) and env["MENTOR_COURSE_ROOT"] == str(mat)
    assert env["MENTOR_SANDBOX_HTML"].endswith("qa_sandbox.html") and env["MENTOR_API_URL"] == f"http://127.0.0.1:{port}"


def test_plik_paczki_weryfikuje_sume(kurs):
    sr, mat, praca, port = _sr(kurs)
    p, suma = sr.plik_paczki("WERYFIKATORY/test_zachowania.py")
    assert p.is_file() and len(suma) == 64
    with pytest.raises(RuntimeError, match="nie zgadza"):
        sr.plik_paczki("WERYFIKATORY/test_zachowania.py", "0" * 64)
    (mat / "bez_sumy.py").write_text("print(1)\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="sumy kontrolnej"):
        sr.plik_paczki("bez_sumy.py")
    with pytest.raises(RuntimeError, match="Niedozwolona"):
        sr.plik_paczki("../kurs.json")
    with pytest.raises(RuntimeError, match="nie ma pliku"):
        sr.plik_paczki("WERYFIKATORY/nie_ma.py")


def test_test_zewnetrzny(srodowisko_kursu, kurs):
    """Niezależny test z paczki: przechodzi tylko dla poprawnego rozwiązania; zmiana pliku testu = odrzucenie; brak funkcji = czytelny komunikat."""
    sr, mat, praca, port = _sr(kurs)
    sr_venv = srodowisko_kursu  # środowisko z pytestem (python-junior-qa) — ten sam interpreter, inna paczka
    sr.venv = sr_venv.venv
    zad = {"id": "x", "tytul": "X", "pliki": ["ocena.py"], "cwiczenie": {"plik": "ocena.py", "sprawdzenie": {"rodzaj": "test_zewnetrzny", "plik_testu": "WERYFIKATORY/test_zachowania.py", "wybor": "test_ocena"}}}
    d = C.definicja(zad)
    assert d["sprawdzenie"]["rodzaj"] == "test_zewnetrzny"
    plik = praca / "ocena.py"
    plik.write_text("# szablon\n", encoding="utf-8")
    assert C.wykonaj_sprawdzenie(sr, d, plik)["status"] == C.STATUS_BLAD
    plik.write_text("def ocen(s):\n    return 'PASS' if s in (200, 201) else ('NOT FOUND' if s == 404 else 'FAIL')\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_ZALICZONE and "3 passed" in w["opis"], w
    plik.write_text("def ocen(s):\n    return 'PASS'\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_BLAD and "nie przechodzą" in w["opis"] and "2 przypadk" in w["opis"], w["opis"]
    plik.write_text("def inna():\n    pass\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_BLAD and "brakuje funkcji ocen" in w["opis"]
    plik.unlink()
    plik.write_text("def ocen(s):\n    return 'PASS'\n", encoding="utf-8")
    tz = mat / "WERYFIKATORY" / "test_zachowania.py"
    oryg = tz.read_bytes()
    tz.write_bytes(oryg + b"\n# x\n")
    w = C.wykonaj_sprawdzenie(sr, d, plik)
    assert w["status"] == C.STATUS_BLAD and "SHA-256" in w["opis"]
    tz.write_bytes(oryg)
    zly = C.definicja({"id": "y", "tytul": "Y", "pliki": ["ocena.py"], "cwiczenie": {"plik": "ocena.py", "sprawdzenie": {"rodzaj": "test_zewnetrzny", "plik_testu": "WERYFIKATORY/test_zachowania.py", "wybor": "test_nie_istnieje"}}})
    w = C.wykonaj_sprawdzenie(sr, zly, plik)
    assert w["status"] == C.STATUS_BLAD and "Nie znaleziono testów" in w["opis"]


def test_lokalne_api_start_stop(srodowisko_kursu, kurs):
    sr, mat, praca, port = _sr(kurs)
    sr.venv = srodowisko_kursu.venv
    assert not sr.api_stan()["dziala"]
    assert sr.api_sprawdz()[0] is None
    ok, msg = sr.api_uruchom()
    assert ok, msg
    assert sr.api_stan()["dziala"]
    kod, tresc = sr.api_sprawdz()
    assert kod == 200 and "ok" in tresc
    with pytest.raises(urllib.error.HTTPError):
        urllib.request.urlopen(f"http://127.0.0.1:{port}/inne", timeout=5)
    ok2, msg2 = sr.api_uruchom()
    assert ok2 and "już działa" in msg2
    assert sr.api_zatrzymaj()[0]
    time.sleep(0.3)
    assert not sr.api_stan()["dziala"] and sr.api_sprawdz()[0] is None
    # skrypt ze złą sumą nie startuje
    sr.wym["api_lokalne"]["sha256"] = "0" * 64
    ok3, msg3 = sr.api_uruchom()
    assert not ok3 and "SHA-256" in msg3


def test_rubryka_z_gotowe_gdy():
    zad = {"id": "r", "tytul": "R", "sprawdz": "Plik ma 3 sekcje. Każda sekcja ma przykład; nic nie jest skopiowane. Commit „dzień 2” jest na GitHubie."}
    r = C._rubryka(zad, {"rubryka": None})
    assert len(r) == 3 and r[0] == "Plik ma 3 sekcje"
    assert C._rubryka(zad, {"rubryka": ["A", "B"]}) == ["A", "B"]
    assert C._rubryka({"id": "p", "tytul": "P"}, {"rubryka": None}) == ["Zadanie wykonane zgodnie z opisem"]
