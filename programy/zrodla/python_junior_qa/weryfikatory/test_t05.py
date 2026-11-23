# Weryfikator tygodnia 5 — produkt.py (klasa), menedżer w 3 plikach (main.py, zadania.py, plik.py), requirements.txt i .gitignore, api.py, raport_cen.py.
import ast as _ast
import csv as _csv
import json as _json
import threading as _threading
from http.server import BaseHTTPRequestHandler as _Handler, HTTPServer as _Server

PRODUKTY_API = [{"id": 1, "nazwa": "Zeszyt A5", "kategoria": "zeszyty", "cena": 4.5, "ilosc": 120},
                {"id": 9, "nazwa": "Papier ksero A4", "kategoria": "papier", "cena": 24.99, "ilosc": 35},
                {"id": 17, "nazwa": "Zszywki", "kategoria": "biuro", "cena": 3.9, "ilosc": 0},
                {"id": 16, "nazwa": "Zszywacz", "kategoria": "biuro", "cena": 19.9, "ilosc": 8}]


@pytest.fixture
def api():
    class H(_Handler):
        def do_GET(self):
            if self.path.startswith("/api/produkty"):
                kod, tresc = 200, _json.dumps(PRODUKTY_API).encode()
            elif self.path.startswith("/api/awaria"):
                kod, tresc = 500, b'{"blad": "awaria"}'
            else:
                kod, tresc = 404, b'{"blad": "nie ma"}'
            self.send_response(kod)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(tresc)

        def log_message(self, *a):
            pass
    srv = _Server(("127.0.0.1", 0), H)
    _threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()
    srv.server_close()


def test_produkt():
    m = modul("produkt")
    P = funkcja(m, "Produkt")
    p = P("Kredki", 12.9, 40)
    p.wydaj(15)
    p.przyjmij(5)
    ok(p.ilosc, 30, "ilosc po wydaj(15) i przyjmij(5)")
    ok(p.wartosc(), 387.0, "wartosc()")
    ok(str(p), "Kredki — 12.90 zł, 30 szt.", "str(produkt)")
    ok(P("Klej", 3.4).ilosc, 0, "domyślna ilość")
    for metoda, n in (("wydaj", 31), ("wydaj", 0), ("przyjmij", 0), ("przyjmij", -2)):
        rzuca(getattr(p, metoda), n, opis=f"{metoda}({n})")
    ok(p.ilosc, 30, "ilosc po nieudanych operacjach (bez zmian)")
    p.wydaj(30)
    ok(p.ilosc, 0, "wydanie całego stanu (wartość brzegowa)")
    rzuca(P, "Zły", -1, 5, opis="Produkt z ceną ujemną")
    a, b = P("A", 1.0, 1), P("B", 2.0, 2)
    a.przyjmij(1)
    ok(b.ilosc, 2, "dwa obiekty mają osobne ilości")


def test_menedzer_moduly(tmp_path):
    z = modul("zadania")
    pl = modul("plik")
    dodaj, oznacz, usun, otwarte = (funkcja(z, n) for n in ("dodaj", "oznacz", "usun", "otwarte"))
    lista = []
    dodaj(lista, " Zamówić papier ")
    dodaj(lista, "Policzyć zeszyty")
    oznacz(lista, 2)
    ok(otwarte(lista), ["Zamówić papier"], "otwarte")
    rzuca(dodaj, lista, "", opis="dodaj pusty tytuł")
    rzuca(oznacz, lista, 3, opis="oznacz(…, 3) przy 2 zadaniach")
    ok(usun(lista, 1), "Zamówić papier", "usun zwraca tytuł")
    sc = tmp_path / "zadania.json"
    funkcja(pl, "zapisz")(lista, sc)
    ok(funkcja(pl, "wczytaj")(sc), lista, "plik.zapisz → plik.wczytaj")
    ok(funkcja(pl, "wczytaj")(tmp_path / "brak.json"), [], "wczytaj nieistniejący plik")
    assert "ą" in sc.read_text(encoding="utf-8") or "ę" in sc.read_text(encoding="utf-8") or "Policzyć" in sc.read_text(encoding="utf-8"), \
        "plik.zapisz: polskie litery czytelne w pliku (json.dump(…, ensure_ascii=False))"
    main = tekst("main.py")
    assert ("import zadania" in main or "from zadania import" in main) and ("import plik" in main or "from plik import" in main), \
        "main.py ma importować moduły zadania i plik"
    assert "def dodaj" not in main and "def wczytaj" not in main, "main.py nie powinien powtarzać funkcji z zadania.py/plik.py — tylko menu"
    modul("main")  # import nie może uruchamiać menu (input) — blok if __name__ == "__main__":
    kod, out = uruchom("main.py", "1\nZamówić papier\n3\n0\n")
    bez_bledu(kod, out, "menu: dodaj, lista, koniec")
    zawiera(out, "Zamówić papier", dane="menu main.py: 1 → tytuł → 3 → 0")


def test_srodowisko_projektu():
    req = [l.strip() for l in tekst("requirements.txt").splitlines() if l.strip() and not l.startswith("#")]
    assert any(re.match(r"requests==\d", l, re.I) for l in req), "requirements.txt: brak linii requests==wersja (python -m pip freeze > requirements.txt)"
    gi = tekst(".gitignore")
    for wzor in (".venv", "__pycache__", ".env"):
        assert wzor in gi, f".gitignore: brak wpisu {wzor}"
    if (WS / ".git").exists():
        kod, pliki = git("ls-files")
        assert not any(x.startswith(".venv/") for x in pliki.split()), ".venv jest w repozytorium — git rm -r --cached .venv i commit"


def test_api(api):
    m = modul("api")
    pob, tanie = funkcja(m, "pobierz_produkty"), funkcja(m, "tanie")
    p = pob(api + "/api/produkty")
    ok(len(p), 4, "pobierz_produkty — liczba produktów")
    ok(p[0]["nazwa"], "Zeszyt A5", "pobierz_produkty — pierwszy produkt")
    for zly in ("/api/awaria", "/api/nie-ma"):
        try:
            pob(api + zly)
        except RuntimeError as e:
            assert ("500" if "awaria" in zly else "404") in str(e), f"RuntimeError dla {zly} ma zawierać kod odpowiedzi; jest: {e}"
        except Exception as e:  # noqa: BLE001
            pytest.fail(f"pobierz_produkty({zly}) rzuciła {type(e).__name__} — oczekiwano RuntimeError z kodem odpowiedzi")
        else:
            pytest.fail(f"pobierz_produkty({zly}) nie zgłosiła błędu dla kodu innego niż 200")
    rzuca(pob, "http://127.0.0.1:9/api/produkty", wyjatek=RuntimeError, opis="pobierz_produkty — serwer niedostępny (RuntimeError zamiast ConnectionError)")
    ok(tanie(p, 20), ["Zszywki", "Zeszyt A5", "Zszywacz"], "tanie(produkty, 20) — nazwy z ceną < 20, rosnąco po cenie")
    ok(tanie(p, 1), [], "tanie(produkty, 1)")
    get = [w for w in _ast.walk(drzewo("api.py")) if isinstance(w, _ast.Call) and getattr(w.func, "attr", "") == "get" and getattr(w.func.value, "id", "") == "requests"]
    assert get and all(any(k.arg == "timeout" for k in w.keywords) for w in get), "api.py: requests.get(…) zawsze z timeout=…"


def test_raport_cen(tmp_path):
    m = modul("raport_cen")
    zap, ostrz = funkcja(m, "zapisz_raport"), funkcja(m, "ostrzezenia")
    cel = tmp_path / "raport.csv"
    ok(zap(PRODUKTY_API, cel, "2026-11-23"), 4, "zapisz_raport zwraca liczbę zapisanych wierszy")
    with open(cel, encoding="utf-8", newline="") as f:
        w = list(_csv.reader(f))
    ok(w[0], ["data", "nazwa", "kategoria", "cena"], "nagłówek raportu")
    ok([x[1] for x in w[1:]], ["Papier ksero A4", "Zszywacz", "Zeszyt A5", "Zszywki"], "kolejność: malejąco po cenie")
    ok(w[1][0], "2026-11-23", "data w każdym wierszu")
    ok(float(w[1][3]), 24.99, "cena w raporcie")
    ok(ostrz(PRODUKTY_API), ["Zszywacz", "Zszywki"], "ostrzezenia — ilość < 10, alfabetycznie")
    ok(ostrz(PRODUKTY_API, 1), ["Zszywki"], "ostrzezenia(…, prog=1)")
    ok(zap([], tmp_path / "pusty.csv", "2026-11-23"), 0, "raport z pustej listy")
