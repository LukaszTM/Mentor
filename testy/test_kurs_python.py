# -*- coding: utf-8 -*-
"""Kurs „Python od zera → Junior QA” 3.0: budowanie ze źródeł (pełny i demo), standard lekcji, klucze odpowiedzi, kod w lekcjach, niezależne weryfikatory zadań
(przechodzą na rozwiązaniach wzorcowych, nie przechodzą na pustym katalogu i plikach startowych z błędami), sklep testowy, paczka materiałów, brak odniesień osobistych i Mentor end-to-end."""

import json
import shutil
import subprocess
import sys

import pytest

import cwiczenia as C
import odpowiedzi as O
import program


MODULY = ("zbuduj", "reszta", "powtorki", "wspolne", "sprawdz_weryfikatory", "zadania_wszystkie", "materialy", "zrodla",
          *(f"zadania{i}" for i in range(4)), *(f"etap{i}{b}" for i in range(5) for b in ("", "b")))


def _wyczysc():
    for m in MODULY:
        sys.modules.pop(m, None)


@pytest.fixture(scope="module")
def zrodla(repo):
    """Źródła kursu na początku sys.path; moduły o tych samych nazwach z innych kursów (zbuduj, reszta, powtorki) usunięte z pamięci."""
    z = repo / "programy" / "zrodla" / "python_junior_qa"
    _wyczysc()
    sys.path.insert(0, str(z))
    yield z
    sys.path.remove(str(z))
    _wyczysc()


@pytest.fixture(scope="module")
def vibe(repo):
    return json.loads((repo / "programy" / "python-junior-qa.json").read_text(encoding="utf-8"))


def test_json_zgodny_ze_zrodlami(zrodla, vibe):
    import zbuduj
    zbudowany = json.loads(json.dumps(zbuduj.zbuduj(), ensure_ascii=False))
    assert zbudowany == vibe, "programy/python-junior-qa.json nieaktualny — uruchom programy/zrodla/python_junior_qa/zbuduj.py"
    demo = json.loads(json.dumps(zbuduj.zbuduj(demo=True), ensure_ascii=False))
    assert demo == json.loads((zbuduj.CEL_DEMO).read_text(encoding="utf-8")), "python-junior-qa-demo.json nieaktualny — zbuduj.py --demo"
    assert demo["id"] == "python-junior-qa-demo" and len(demo["tygodnie"]) == 4 and all(l["tydzien"] < 4 for l in demo["lekcje"])


def test_walidacja_i_struktura(vibe):
    assert program.waliduj(vibe) == []
    assert vibe["id"] == "python-junior-qa" and len(vibe["tygodnie"]) == 13 and len(vibe["lekcje"]) == 39
    assert [z["id"] for w in vibe["tygodnie"] for z in w["zadania"]] == [f"t{t}z{n}" for t in range(13) for n in range(1, 6)], "identyfikatory zadań stabilne"
    assert all(w["czas_min"] <= 540 for w in vibe["tygodnie"])
    assert 85 * 60 <= sum(w["czas_min"] for w in vibe["tygodnie"]) <= 110 * 60
    for l in vibe["lekcje"]:
        assert [c["rodzaj"] for c in l["cwiczenia"]] == ["prowadzone", "samodzielne"], l["id"]
        assert l["zrodla"] and all(z[1].startswith("https://") for z in l["zrodla"]), l["id"]
        assert len(l["typowe_bledy"]) >= 2 and 3 <= len(l["test"]) <= 5, l["id"]
    lekcje = {l["id"] for l in vibe["lekcje"]}
    assert all(q["lekcja"] in lekcje for qs in vibe["quizy"].values() for q in qs)
    assert all(q["lekcja"] in lekcje for q in vibe["diagnoza"])


def test_klucze_odpowiedzi_przyjmuja_poprawne_wartosci(vibe):
    n = 0
    for l in vibe["lekcje"]:
        for c in l["cwiczenia"]:
            if c.get("odpowiedzi"):
                assert O.waliduj_pola(c["odpowiedzi"], l["id"]) == []
                wynik = O.sprawdz(c["odpowiedzi"], {p["id"]: O.poprawna(p) for p in c["odpowiedzi"]})
                assert wynik["komplet"], (l["id"], wynik)
                n += 1
    assert n >= 75, n


def test_typowe_pomylki_sa_rozpoznawane(vibe):
    """Pola z listą „bledy” dają podpowiedź (nie „nie zgadza się”) dla typowej pomyłki — i nigdy nie zaliczają jej."""
    for l in vibe["lekcje"]:
        for c in l["cwiczenia"]:
            for p in c.get("odpowiedzi") or []:
                for b in p.get("bledy") or []:
                    ok, info = O.sprawdz_pole(p, b["wartosc"])
                    assert ok is False and info == b["komunikat"], (l["id"], p["id"], b, info)


def test_kod_z_lekcji_daje_podane_wyjscie(zrodla, srodowisko_kursu):
    import wspolne
    import zbuduj  # noqa: F401  (rejestruje kod ze wszystkich lekcji)
    assert len(wspolne.KOD_DO_SPRAWDZENIA) >= 30
    for gdzie, kod, oczekiwane in wspolne.KOD_DO_SPRAWDZENIA:
        if oczekiwane is None:
            continue
        p = subprocess.run([str(srodowisko_kursu.python_venv()), "-X", "utf8", "-c", kod], capture_output=True, text=True, encoding="utf-8", timeout=60)
        assert p.stdout.replace("\r\n", "\n") == oczekiwane, (gdzie, p.stdout, p.stderr[-500:])


def test_sumy_weryfikatorow_w_zadaniach(zrodla, vibe):
    import zbuduj
    n = 0
    for w in vibe["tygodnie"]:
        for z in w["zadania"]:
            s = z["cwiczenie"]["sprawdzenie"]
            if s["rodzaj"] == "test_zewnetrzny":
                assert s["sha256"] == zbuduj.sha_weryfikatora(s["plik_testu"].split("/")[-1]), z["id"]
                n += 1
    assert n >= 55, n


@pytest.mark.skipif(not shutil.which("git"), reason="weryfikatory z repozytorium wymagają programu git")
def test_weryfikatory_wzorce_puste_i_bledne(zrodla, srodowisko_kursu):
    import sprawdz_weryfikatory as SW
    assert SW.kontrola(log=lambda *_: None, python=str(srodowisko_kursu.python_venv())) == []


def test_przyklady_pytest_z_lekcji_przechodza(zrodla, srodowisko_kursu, tmp_path):
    import wspolne
    import zbuduj  # noqa: F401
    for gdzie, kod, _ in wspolne.KOD_DO_SPRAWDZENIA:
        if gdzie in ("pytest", "parametrize_fixture"):
            f = tmp_path / f"test_{gdzie}.py"
            f.write_text(kod, encoding="utf-8")
            p = subprocess.run([str(srodowisko_kursu.python_venv()), "-m", "pytest", "-q", "-p", "no:cacheprovider", str(f)], capture_output=True, text=True, encoding="utf-8", cwd=tmp_path)
            assert p.returncode == 0, (gdzie, p.stdout[-800:])


def test_sklep_testowy_ma_celowe_defekty(repo, srodowisko_kursu):
    """Sklep testowy działa zgodnie z README w ścieżkach podstawowych i ma celowe defekty (materiał na raporty błędów). Uruchamiany Pythonem kursu (Flask)."""
    skrypt = """
import importlib.util, sys
spec = importlib.util.spec_from_file_location("sklep_testowy", sys.argv[1])
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
k = m.app.test_client()
assert k.post("/logowanie", data={"login": "tester", "haslo": "zle"}).status_code == 401
assert k.post("/logowanie", data={"login": "tester", "haslo": "Test123!"}).status_code == 302
h = k.get("/produkty").get_data(as_text=True)
assert "Witaj, tester!" in h and h.count('class="produkt"') == 20
assert k.get("/produkty?q=długopis").get_data(as_text=True).count('class="produkt"') == 0, "defekt: wyszukiwarka"
k.post("/koszyk/dodaj/1", data={"ilosc": "10"})
assert "Suma: 4,50 zł" in k.get("/koszyk").get_data(as_text=True), "defekt: suma dla ilości >= 10"
assert k.get("/api/produkty?kategoria=biuro").json[0]["nazwa"] == "Segregator A4"
print("OK")
"""
    app = repo / "programy" / "zrodla" / "python_junior_qa" / "projekty" / "sklep_testowy" / "app.py"
    p = subprocess.run([str(srodowisko_kursu.python_venv()), "-X", "utf8", "-c", skrypt, str(app)], capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0 and "OK" in p.stdout, p.stdout + p.stderr[-1500:]


def test_brak_odniesien_osobistych(repo):
    """Kurs dla odbiorców zewnętrznych: żadnych danych i odniesień do życia prywatnego autora."""
    import re
    zakazane = re.compile(r"łukasz|lukasz|kapsl|gospodarstw|krow|krasul|mućk|radzy|brzost|obora|ciągnik|mleko|stado|LukaszTM|@gmail", re.I)
    for baza in (repo / "programy" / "zrodla" / "python_junior_qa", repo / "programy" / "materialy" / "python-junior-qa"):
        for p in baza.rglob("*"):
            if p.is_file() and p.suffix in (".py", ".md", ".json", ".csv", ".txt", ".bat", ".yml", ".html"):
                t = p.read_text(encoding="utf-8", errors="ignore")
                assert not zakazane.search(t), (p, zakazane.search(t).group(0))
    assert not zakazane.search((repo / "programy" / "python-junior-qa.json").read_text(encoding="utf-8"))


def test_paczka_materialow(repo, vibe):
    mat = repo / "programy" / "materialy" / "python-junior-qa"
    p = subprocess.run([sys.executable, str(mat / "testy" / "sprawdz_kurs.py")], capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0, p.stdout + p.stderr
    assert json.loads((mat / "kurs_mentor.json").read_text(encoding="utf-8")) == vibe, "paczka nieaktualna — uruchom materialy.py (i materialy.py --demo)"
    for f in ("START_TUTAJ.md", "mentor-manifest.json", "pytest.ini", "dane/produkty.csv", "projekty/sklep_testowy/app.py", "projekty/cudzy_projekt/app.py", "przyklady/do_poprawy.py", "przyklady/magazyn_ukryty.py", "przyklady/tydzien_01/zmienne.py", "rozwiazania/kod/app.py", "pomoc/FAQ.md"):
        assert (mat / f).is_file(), f
    calosc = "\n".join(x.read_text(encoding="utf-8", errors="ignore") for x in mat.rglob("*") if x.is_file() and x.suffix in (".md", ".py", ".json", ".txt", ".csv", ".ini", ".bat"))
    import re
    assert not re.search(r"sk-" + r"ant-[A-Za-z0-9]", calosc), "klucz Anthropic w paczce"
    assert not re.search(r"[\w.]+@gmail\.com", calosc), "prawdziwy adres e-mail w paczce"
    assert "BEGIN PRIVATE KEY" not in calosc


def test_mentor_end_to_end(repo, vibe, srodowisko_kursu, tmp_path):
    """Kurs nie jest wbudowany: uczeń importuje Python-junior-qa-kurs.zip, a Mentor uruchamia weryfikator z zaimportowanej paczki (SHA-256, izolacja, MENTOR_WORKSPACE)."""
    import paczki
    import srodowisko
    zp = shutil.make_archive(str(tmp_path / "Python-junior-qa-kurs"), "zip", repo / "programy" / "materialy", "python-junior-qa")
    assert paczki.przejrzyj_zip(zp)["manifest"]["course_id"] == "python-junior-qa"
    paczki.importuj_zip(zp, nadpisz=True, utworz_prace=False)
    assert program.katalog_materialow("python-junior-qa") == program.KATALOG_KURSOW / "python-junior-qa" / "paczka"
    sr = srodowisko.Srodowisko("python-junior-qa", vibe.get("srodowisko"))
    sr.venv = srodowisko_kursu.venv
    praca = tmp_path / "PRACA"
    praca.mkdir()
    zad = next(z for w in vibe["tygodnie"] for z in w["zadania"] if z["id"] == "t1z2")
    d = C.definicja(zad)
    (praca / "kalkulator.py").write_text("a = float(input())\nd = input()\nb = float(input())\nprint(a + b)\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, praca / "kalkulator.py")
    assert w["status"] == C.STATUS_BLAD, w
    shutil.copy(repo / "programy" / "zrodla" / "python_junior_qa" / "wzorce" / "kalkulator.py", praca / "kalkulator.py")
    w = C.wykonaj_sprawdzenie(sr, d, praca / "kalkulator.py")
    assert w["status"] == C.STATUS_ZALICZONE, w
    zad = next(z for w in vibe["tygodnie"] for z in w["zadania"] if z["id"] == "t3z1")
    d = C.definicja(zad)
    (praca / "funkcje.py").write_text("def inna():\n    pass\n", encoding="utf-8")
    w = C.wykonaj_sprawdzenie(sr, d, praca / "funkcje.py")
    assert w["status"] == C.STATUS_BLAD and "brakuje funkcji" in w["opis"].lower(), w
    paczki.usun_kurs("python-junior-qa")
