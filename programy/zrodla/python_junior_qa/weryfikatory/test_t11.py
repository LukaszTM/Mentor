# Weryfikator tygodnia 11 — aplikacja Flask projektu Magazyn (test_client na bazie tymczasowej), testy E2E w POM, uruchomienie jedną komendą i CI.


@pytest.fixture
def apka(tmp_path):
    a = modul("app")
    b = modul("baza")
    db = tmp_path / "web.db"
    app = funkcja(a, "create_app")(db)
    app.config["TESTING"] = True
    con = b.utworz_baze(db)
    return app.test_client(), b, con, db


def _html(o):
    return o.get_data(as_text=True)


def test_lista(apka):
    k, b, con, _ = apka
    b.dodaj_produkt(con, "Zeszyt A5", "zeszyty", 4.5, 120)
    b.dodaj_produkt(con, "Segregator A4", "biuro", 11.9, 45)
    o = k.get("/")
    assert o.status_code == 200, f"GET / → {o.status_code}"
    h = _html(o)
    for f in ("Zeszyt A5", "Segregator A4", "120", "4,50"):
        assert f in h, f"strona główna: brak „{f}” (nazwa, ilość, cena z przecinkiem i 2 miejscami)"
    assert h.index("Segregator A4") < h.index("Zeszyt A5"), "strona główna: produkty alfabetycznie"


def test_formularz(apka):
    k, b, con, _ = apka
    assert k.get("/dodaj").status_code == 200, "GET /dodaj → formularz"
    o = k.post("/dodaj", data={"nazwa": "Klej w sztyfcie", "kategoria": "akcesoria", "cena": "3,40", "ilosc": "10"})
    assert o.status_code == 302, f"poprawny formularz → przekierowanie (302), jest {o.status_code}"
    assert "Klej w sztyfcie" in _html(k.get("/")), "po dodaniu produkt jest na liście"
    zle = [({"nazwa": "", "kategoria": "biuro", "cena": "2", "ilosc": "1"}, "nazw"),
           ({"nazwa": "X1", "kategoria": "biuro", "cena": "abc", "ilosc": "1"}, "cen"),
           ({"nazwa": "X2", "kategoria": "biuro", "cena": "-1", "ilosc": "1"}, "cen"),
           ({"nazwa": "X3", "kategoria": "biuro", "cena": "2", "ilosc": "1.5"}, "ilo"),
           ({"nazwa": "X4", "kategoria": "", "cena": "2", "ilosc": "1"}, "kategori"),
           ({"nazwa": "klej w sztyfcie", "kategoria": "akcesoria", "cena": "2", "ilosc": "1"}, "istnieje")]
    for dane, slowo in zle:
        o = k.post("/dodaj", data=dane)
        assert o.status_code == 400, f"POST /dodaj {dane} → oczekiwano 400, jest {o.status_code}"
        assert slowo in norm(_html(o)), f"POST /dodaj {dane}: komunikat dla użytkownika ze słowem „{slowo}…”"
    assert len(b.pobierz_produkty(con)) == 1, "błędne formularze nie mogą dodać produktu do bazy"
    o = k.post("/dodaj", data={"nazwa": "<script>alert(1)</script>", "kategoria": "", "cena": "1", "ilosc": "1"})
    assert "<script>alert(1)</script>" not in _html(o), "wpisany tekst wraca na stronę zabezpieczony (Jinja {{ }}) — bez wstrzykniętego <script>"


def test_historia(apka):
    k, b, con, _ = apka
    m = modul("magazyn")
    pid = b.dodaj_produkt(con, "Zszywacz", "biuro", 19.9, 0)
    m.przyjecie(con, pid, 15, "2026-11-20")
    m.wydanie(con, pid, 5, "2026-11-22")
    o = k.get(f"/produkt/{pid}")
    assert o.status_code == 200, f"GET /produkt/{pid} → {o.status_code}"
    h = _html(o)
    for f in ("Zszywacz", "2026-11-20", "2026-11-22", "15", "5"):
        assert f in h, f"strona produktu: brak „{f}” (nazwa i historia operacji)"
    assert h.index("2026-11-20") < h.index("2026-11-22"), "historia rosnąco po dacie"
    assert k.get("/produkt/9999").status_code == 404, "nieistniejący produkt → 404"


def test_e2e_pom():
    nazwa = "test_e2e.py" if (WS / "test_e2e.py").exists() else "tests/test_e2e.py"
    t = tekst(nazwa)
    assert len(re.findall(r"^def test_\w+", t, re.M)) >= 3, f"{nazwa}: co najmniej 3 testy E2E (lista, dodanie formularzem, historia)"
    assert re.search(r"from pages[\w.]* import|import pages", t), f"{nazwa}: testy używają Page Objectów z pages/"
    assert "sleep" not in t, f"{nazwa}: bez time.sleep"
    cf = "".join(p.read_text(encoding="utf-8") for p in (WS / "conftest.py", WS / "tests" / "conftest.py") if p.exists())
    assert "make_server" in cf or "serwer" in cf, "conftest.py: fixtura uruchamiająca aplikację na serwerze testowym (werkzeug make_server w wątku)"
    assert "create_app" in cf, "conftest.py: serwer testowy z create_app(ścieżka bazy tymczasowej)"


def test_jedna_komenda_i_ci():
    t = tekst("app.py")
    assert re.search(r"if __name__ == ['\"]__main__['\"]:", t) and ".run(" in t, "app.py: uruchomienie jedną komendą — app.run(…) w bloku __main__"
    assert "debug=True" not in t.split("__main__")[-1] or "environ" in t, "app.py: debug=True tylko lokalnie (np. zależnie od zmiennej środowiskowej)"
    r = tekst("README.md")
    assert "python app.py" in r, "README.md: polecenie uruchomienia `python app.py`"
    wf = sorted((WS / ".github" / "workflows").glob("*.y*ml"))
    assert wf and "pytest" in wf[0].read_text(encoding="utf-8"), "workflow CI uruchamia pytest"
