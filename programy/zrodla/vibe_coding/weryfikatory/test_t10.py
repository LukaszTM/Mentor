# Weryfikator tygodnia 10 — raport.py (CSV), app.py (Flask), baza.py (SQLite).
import json as _json
import tempfile

CSV_TEST = ("﻿data_przyjazdu;pokoj;noce;osoby;kwota\n2026-07-03;Lipowy;3;2;1 080,00\n2026-07-10;Dębowy;7;4;3528,00\n\n"
            "2026-08-01;Lipowy;2;2;720,00\n2026-08-15;Dębowy;1;1;160,50\n;;;;\n")


def _r():
    m = modul("raport")
    return [funkcja(m, n) for n in ("wczytaj", "przychod_miesieczny", "najczestszy_pokoj", "zapisz_json")]


def _plik_tmp(tresc, td, nazwa="r.csv"):
    p = Path(td) / nazwa
    p.write_text(tresc, encoding="utf-8")
    return str(p)


def test_raport_wczytaj():
    wczytaj, *_ = _r()
    with tempfile.TemporaryDirectory() as td:
        rez = wczytaj(_plik_tmp(CSV_TEST, td))
    ok(len(rez), 4, "liczba wczytanych rezerwacji (puste wiersze pomijane)")
    ok(rez[0]["kwota"], 1080.0, "kwota „1 080,00” (spacja tysięcy, przecinek)")
    ok(rez[1]["noce"], 7, "noce jako liczba całkowita")
    ok(rez[1]["pokoj"], "Dębowy", "pokoj z polskim znakiem")
    assert "data_przyjazdu" in rez[0], "brak klucza data_przyjazdu — usuń BOM (encoding=\"utf-8-sig\")"


def test_raport_zly_wiersz():
    wczytaj, *_ = _r()
    zle = "data_przyjazdu;pokoj;noce;osoby;kwota\n2026-07-03;Lipowy;3;2;1080,00\n2026-07-04;Lipowy;trzy;2;100,00\n"
    with tempfile.TemporaryDirectory() as td:
        with pytest.raises(ValueError) as e:
            wczytaj(_plik_tmp(zle, td))
    assert "3" in str(e.value), f"komunikat błędu powinien wskazać numer wiersza (3, licząc nagłówek jako 1): „{e.value}”"


def test_raport_sumy_i_pokoj():
    wczytaj, przychod, pokoj, _ = _r()
    with tempfile.TemporaryDirectory() as td:
        rez = wczytaj(_plik_tmp(CSV_TEST, td))
    ok(przychod(rez), {"2026-07": 4608.0, "2026-08": 880.5}, "przychod_miesieczny")
    ok(pokoj(rez), "Dębowy", "najczestszy_pokoj — remis 2:2, alfabetycznie pierwszy (Dębowy)")
    ok(pokoj([]), None, "najczestszy_pokoj([])")


def test_raport_json():
    _, _, _, zapisz = _r()
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "w.json"
        zapisz({"pokoj": "Dębowy", "suma": 1.5}, str(p))
        t = p.read_text(encoding="utf-8")
    assert "Dębowy" in t, "zapisz_json: polskie znaki zapisane jako \\u… — użyj ensure_ascii=False"
    ok(_json.loads(t), {"pokoj": "Dębowy", "suma": 1.5}, "zapisz_json — zawartość")


def test_raport_plik_kursu():
    wczytaj, przychod, *_ = _r()
    p = WS / "dane" / "rezerwacje.csv"
    assert p.exists(), "Brak pliku dane/rezerwacje.csv w katalogu roboczym — skopiuj go z materiałów kursu (folder dane)"
    rez = wczytaj(str(p))
    ok(len(rez), 40, "liczba rezerwacji w dane/rezerwacje.csv")
    ok(round(sum(przychod(rez).values()), 2), 47874.0, "suma przychodu z dane/rezerwacje.csv")


def _app(**k):
    m = modul("app")
    return funkcja(m, "create_app")(**k)


def test_flask_trasy():
    k = _app().test_client()
    o = k.get("/")
    ok(o.status_code, 200, "GET /")
    assert "Pod Lipą" in o.get_data(as_text=True), "GET / — strona startowa powinna zawierać „Pod Lipą”"
    o = k.get("/api/cena?noce=2&osoby=2")
    ok(o.status_code, 200, "GET /api/cena?noce=2&osoby=2")
    ok((o.get_json() or {}).get("koszt"), 480, "koszt dla 2 nocy i 2 osób")
    ok((k.get("/api/cena?noce=7&osoby=1").get_json() or {}).get("koszt"), 756.0, "koszt dla 7 nocy i 1 osoby")
    ok(k.get("/nie-ma-takiej").status_code, 404, "GET nieistniejącego adresu")


def test_flask_bledy():
    k = _app().test_client()
    for url in ("/api/cena?noce=2", "/api/cena?noce=abc&osoby=2", "/api/cena?noce=0&osoby=2"):
        o = k.get(url)
        ok(o.status_code, 400, f"GET {url}")
        assert "blad" in (o.get_json() or {}), f"GET {url}: odpowiedź JSON powinna mieć klucz „blad” z komunikatem"


def test_flask_bez_debug():
    t = tekst("app.py")
    assert not re.search(r"debug\s*=\s*True", t.split('if __name__ == "__main__"')[0]), "app.py: debug=True poza blokiem __main__ — tryb debug tylko lokalnie"
    assert "0.0.0.0" not in t, "app.py: host=\"0.0.0.0\" udostępnia aplikację w całej sieci — usuń"


def _b():
    m = modul("baza")
    return [funkcja(m, n) for n in ("polacz", "dodaj_goscia", "znajdz_po_emailu", "lista_gosci")]


def test_baza_zapis_odczyt():
    polacz, dodaj, znajdz, lista = _b()
    con = polacz(":memory:")
    i1 = dodaj(con, "Anna", "anna@pod-lipa.pl", 2)
    i2 = dodaj(con, "Piotr", "piotr@pod-lipa.pl", 3)
    assert i1 != i2, "dodaj_goscia powinna zwracać różne id"
    g = znajdz(con, "piotr@pod-lipa.pl")
    ok({k: g[k] for k in ("id", "imie", "email", "noce")} if g else None, {"id": i2, "imie": "Piotr", "email": "piotr@pod-lipa.pl", "noce": 3}, "znajdz_po_emailu")
    ok(znajdz(con, "brak@pod-lipa.pl"), None, "znajdz_po_emailu — brak gościa")
    ok([x["imie"] for x in lista(con)], ["Anna", "Piotr"], "lista_gosci — kolejność dodania")


def test_baza_reguly():
    polacz, dodaj, _, _ = _b()
    con = polacz(":memory:")
    dodaj(con, "Anna", "anna@pod-lipa.pl", 2)
    rzuca(dodaj, con, "Inna", "anna@pod-lipa.pl", 1, opis="dodaj_goscia z istniejącym e-mailem")
    rzuca(dodaj, con, "", "x@pod-lipa.pl", 1, opis="dodaj_goscia z pustym imieniem")
    rzuca(dodaj, con, "Ewa", "ewa@pod-lipa.pl", 0, opis="dodaj_goscia z 0 nocy")


def test_baza_sql_injection():
    polacz, dodaj, znajdz, lista = _b()
    con = polacz(":memory:")
    dodaj(con, "Anna", "anna@pod-lipa.pl", 2)
    zly = "x' OR '1'='1"
    ok(znajdz(con, zly), None, "znajdz_po_emailu(\"x' OR '1'='1\") — atak SQL injection nie może zwrócić gościa")
    dodaj(con, "Atak", zly, 1)
    ok(znajdz(con, zly)["email"], zly, "e-mail z apostrofami zapisany dosłownie")
    ok(len(lista(con)), 2, "lista_gosci po zapisie podejrzanego e-maila")
    t = tekst("baza.py")
    assert not re.search(r"execute(many)?\(\s*f[\"']", t), "baza.py: execute z f-stringiem — używaj parametrów ?"
    assert not re.search(r"execute(many)?\([^)]*[\"']\s*(%|\+)", t), "baza.py: execute z formatowaniem % albo sklejaniem + — używaj parametrów ?"
