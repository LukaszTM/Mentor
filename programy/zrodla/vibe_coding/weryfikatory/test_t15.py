# Weryfikator tygodnia 15 — plan projektu, mini system rezerwacji (system.py), wydanie 1.0.0.
import subprocess

PLAN = {"cel": 0, "uzytkownicy": 1, "funkcje": 5, "kamienie milowe": 4, "ryzyka": 3, "gotowe, gdy": 2}


def test_plan():
    s = sekcje_md(tekst("plan_projektu.md"))
    for k, n in PLAN.items():
        sek = next((v for kk, v in s.items() if kk.replace(",", "") == k.replace(",", "")), None)
        assert sek is not None and sek, f"plan_projektu.md: brak niepustej sekcji „## {k.capitalize()}”"
        if n:
            ile = sum(1 for l in sek if l.startswith(("-", "*", "|")) or re.match(r"\d+[.)]", l))
            assert ile >= n, f"plan_projektu.md: sekcja „{k}” ma {ile} pozycji (potrzeba ≥ {n})"


def _klient():
    return funkcja(modul("system"), "create_app")(":memory:").test_client()


def R(gosc="Anna", email="anna@pod-lipa.pl", pokoj="Lipowy", od="2026-12-20", do="2026-12-23"):
    return {"gosc": gosc, "email": email, "pokoj": pokoj, "od": od, "do": do}


def test_projekt_strona():
    k = _klient()
    o = k.get("/")
    ok(o.status_code, 200, "GET /")
    assert "Pod Lipą" in o.get_data(as_text=True), "GET / — strona powinna zawierać „Pod Lipą”"


def test_projekt_zapis_i_koszt():
    k = _klient()
    o = k.post("/api/rezerwacje", json=R())
    ok(o.status_code, 201, "POST poprawnej rezerwacji Lipowy 20–23.12")
    d = o.get_json() or {}
    assert isinstance(d.get("id"), int), "odpowiedź 201 powinna zawierać liczbowe id"
    ok(d.get("koszt"), 540, "koszt Lipowego 20–23.12 (3 noce × 180 zł, grudzień)")
    o = k.post("/api/rezerwacje", json=R(pokoj="Lipowy", od="2026-11-30", do="2026-12-02", email="ewa@pod-lipa.pl"))
    ok((o.get_json() or {}).get("koszt"), 320, "koszt 30.11–2.12: noc listopadowa 140 zł + grudniowa 180 zł")
    ok((k.post("/api/rezerwacje", json=R(pokoj="Dębowy", od="2027-03-01", do="2027-03-03")).get_json() or {}).get("koszt"), 240, "koszt Dębowego w marcu (2 × 120 zł)")


def test_projekt_walidacja():
    k = _klient()
    for dane, opis in ((R(email="anna@"), "zły e-mail"), (R(pokoj="Brzozowy"), "nieznany pokój"), (R(od="2026-12-23", do="2026-12-20"), "do przed od"),
                       (R(od="2026-13-01", do="2026-13-03"), "zła data"), (R(gosc="  "), "puste imię gościa"), ({"gosc": "Anna"}, "brak pól")):
        o = k.post("/api/rezerwacje", json=dane)
        ok(o.status_code, 400, f"POST: {opis}")
        assert "blad" in (o.get_json() or {}), f"POST ({opis}): brak klucza „blad” w odpowiedzi"
    ok(k.post("/api/rezerwacje", data="nie json", content_type="text/plain").status_code, 400, "POST bez JSON")


def test_projekt_kolizje():
    k = _klient()
    k.post("/api/rezerwacje", json=R())
    o = k.post("/api/rezerwacje", json=R(gosc="Piotr", email="piotr@pod-lipa.pl", od="2026-12-21", do="2026-12-22"))
    ok(o.status_code, 409, "POST kolidującej rezerwacji Lipowego 21–22.12")
    ok(k.post("/api/rezerwacje", json=R(gosc="Piotr", email="piotr@pod-lipa.pl", od="2026-12-23", do="2026-12-25")).status_code, 201, "wyjazd 23.12 = przyjazd 23.12 — bez kolizji")
    ok(k.post("/api/rezerwacje", json=R(gosc="Ola", email="ola@pod-lipa.pl", pokoj="Dębowy")).status_code, 201, "inny pokój w tych samych datach")


def test_projekt_lista_bez_emaili():
    k = _klient()
    k.post("/api/rezerwacje", json=R())
    k.post("/api/rezerwacje", json=R(gosc="Ola", email="ola@pod-lipa.pl", pokoj="Dębowy"))
    o = k.get("/api/rezerwacje")
    ok(o.status_code, 200, "GET /api/rezerwacje")
    lista = o.get_json()
    ok([(r["gosc"], r["pokoj"], r["od"], r["do"]) for r in lista], [("Anna", "Lipowy", "2026-12-20", "2026-12-23"), ("Ola", "Dębowy", "2026-12-20", "2026-12-23")], "lista rezerwacji w kolejności dodania")
    assert all("email" not in r for r in lista), "GET /api/rezerwacje zwraca e-maile — minimalizacja danych: usuń pole email z listy"
    assert all("koszt" in r and "id" in r for r in lista), "każda pozycja listy powinna mieć id i koszt"


def test_projekt_wolne_i_usuwanie():
    k = _klient()
    i = k.post("/api/rezerwacje", json=R()).get_json()["id"]
    ok(k.get("/api/wolne?od=2026-12-21&do=2026-12-22").get_json()["wolne"], ["Dębowy", "Klonowy"], "/api/wolne po rezerwacji Lipowego")
    ok(k.get("/api/wolne?od=2026-12-21").status_code, 400, "/api/wolne bez daty do")
    ok(k.delete(f"/api/rezerwacje/{i}").status_code, 204, "DELETE istniejącej rezerwacji")
    ok(k.get("/api/wolne?od=2026-12-21&do=2026-12-22").get_json()["wolne"], ["Lipowy", "Dębowy", "Klonowy"], "/api/wolne po usunięciu")
    ok(k.delete(f"/api/rezerwacje/{i}").status_code, 404, "DELETE nieistniejącej rezerwacji")


def test_projekt_bezpieczenstwo():
    t = tekst("system.py")
    assert not re.search(r"execute(many)?\(\s*f[\"']", t) and not re.search(r"execute(many)?\([^)]*[\"']\s*(%|\+)", t), "system.py: SQL z formatowaniem napisów — tylko parametry ?"
    assert not re.search(r"debug\s*=\s*True", t) and "0.0.0.0" not in t, "system.py: debug=True albo host 0.0.0.0"
    for mod in ("walidacja", "kalendarz", "cennik"):
        assert re.search(rf"^\s*(from\s+{mod}\s+import|import\s+{mod})", t, re.M), f"system.py: brak importu modułu {mod} — korzystaj z modułów kursu zamiast kopiować kod"


def test_projekt_jakosc():
    p = plik("test_system.py")
    wynik = subprocess.run([sys.executable, "-X", "utf8", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-o", "addopts=", p.name], cwd=str(WS),
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
    out = wynik.stdout + wynik.stderr
    assert wynik.returncode == 0, "Twoje testy test_system.py nie przechodzą:\n" + out[-1500:]
    m = re.search(r"(\d+) passed", out)
    assert m and int(m.group(1)) >= 10, f"test_system.py: {m.group(1) if m else 0} testów — potrzeba ≥ 10"
    for f in ("README.md", "AGENTS.md"):
        assert (WS / f).exists(), f"Brak {f} w projekcie"
    assert list((WS / ".github" / "workflows").glob("*.y*ml")) if (WS / ".github" / "workflows").is_dir() else False, "Brak workflow CI w .github/workflows/"
    repo()
    kod, log = git("log", "--oneline")
    n = len([l for l in log.splitlines() if l.strip()]) if kod == 0 else 0
    assert n >= 10, f"Historia Gita ma {n} commitów — projekt prowadzony kamieniami powinien mieć ≥ 10"


def test_wydanie():
    t = tekst("CHANGELOG.md")
    assert re.search(r"^##\s*\[?1\.0\.0\]?\s*-\s*20\d\d-\d\d-\d\d", t, re.M), "CHANGELOG.md: brak wpisu „## [1.0.0] - RRRR-MM-DD” (z prawdziwą datą)"
    assert re.search(r"^###\s*(Dodano|Added)", t, re.M | re.I), "CHANGELOG.md: brak sekcji „### Dodano”"
    repo()
    kod, tagi = git("tag", "-l", "v1.0.0")
    assert kod == 0 and "v1.0.0" in tagi, "Brak tagu v1.0.0 — git tag -a v1.0.0 -m \"Wersja 1.0.0\" (i git push origin v1.0.0)"
    assert "licencja" in sekcje_md(tekst("README.md")), "README.md: brak sekcji „## Licencja”"
