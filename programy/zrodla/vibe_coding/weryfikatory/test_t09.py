# Weryfikator tygodnia 9 — index.html, styl.css, kalkulator.js, adres GitHub Pages.
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser

ZLE_ALT = {"", "image", "img", "obrazek", "zdjecie", "zdjęcie", "foto", "photo", "picture", "grafika"}


class _Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tagi = []
        self.title = ""
        self._w_title = False

    def handle_starttag(self, tag, attrs):
        self.tagi.append((tag, dict(attrs)))
        self._w_title = tag == "title"

    def handle_endtag(self, tag):
        if tag == "title":
            self._w_title = False

    def handle_data(self, data):
        if self._w_title:
            self.title += data


def _html():
    p = _Parser()
    p.feed(tekst("index.html"))
    return p


def _tag(p, nazwa):
    return [a for t, a in p.tagi if t == nazwa]


def test_strona_naglowek():
    p = _html()
    html = _tag(p, "html")
    assert html and (html[0].get("lang") or "").lower().startswith("pl"), "index.html: brak lang=\"pl\" w znaczniku <html>"
    metas = _tag(p, "meta")
    assert any((m.get("charset") or "").lower().replace("-", "") == "utf8" for m in metas), "index.html: brak <meta charset=\"utf-8\">"
    assert any((m.get("name") or "").lower() == "viewport" and "width=device-width" in (m.get("content") or "").replace(" ", "") for m in metas), \
        "index.html: brak <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
    t = p.title.strip()
    assert t and t.lower() != "document", f"index.html: tytuł strony „{t}” — wpisz konkretny tytuł"
    assert len(_tag(p, "h1")) == 1, f"index.html: powinien być dokładnie jeden <h1> (jest {len(_tag(p, 'h1'))})"


def test_strona_formularz():
    p = _html()
    assert any(a.get("id") == "kalkulator" for a in _tag(p, "form")), "index.html: brak <form id=\"kalkulator\">"
    ids = {a.get("id") for t, a in p.tagi if a.get("id")}
    etykiety = {a.get("for") for a in _tag(p, "label")}
    for pole in ("noce", "osoby"):
        assert any(a.get("id") == pole for a in _tag(p, "input")), f"index.html: brak <input id=\"{pole}\">"
        assert pole in etykiety, f"index.html: pole {pole} bez etykiety <label for=\"{pole}\">"
    assert "wynik" in ids, "index.html: brak elementu z id=\"wynik\" na wynik kalkulatora"


def test_strona_zasoby():
    p = _html()
    assert any("kalkulator.js" in (a.get("src") or "") for a in _tag(p, "script")), "index.html: brak <script src=\"kalkulator.js\">"
    assert any("styl.css" in (a.get("href") or "") and "stylesheet" in (a.get("rel") or "") for a in _tag(p, "link")), "index.html: brak <link rel=\"stylesheet\" href=\"styl.css\">"
    for a in _tag(p, "img"):
        alt = (a.get("alt") or "").strip()
        assert norm(alt) not in {norm(z) for z in ZLE_ALT} and len(alt) >= 5, f"obrazek {a.get('src')}: alt „{alt}” nie opisuje treści zdjęcia"
    css = tekst("styl.css")
    assert "@media" in css, "styl.css: brak reguły @media (wersja na telefon/szerszy ekran)"


NODE_TEST = r'''
const el = () => ({ addEventListener() {}, value: "", textContent: "" });
globalThis.document = { querySelector: el, getElementById: el, addEventListener() {} };
globalThis.window = globalThis;
%KOD%
;(function () {
  const f = (typeof obliczKoszt === "function") ? obliczKoszt : null;
  if (!f) { console.log("BRAK_FUNKCJI"); return; }
  const wyniki = [f(2, 2), f(7, 1), f(7, 1, 99.99), f(6, 1)];
  const bledy = [[0, 1], [1.5, 1], [NaN, 1], [2, 0]].map(a => { try { f(...a); return "brak"; } catch (e) { return "blad"; } });
  console.log(JSON.stringify({ wyniki, bledy }));
})();
'''


def test_kalkulator_js():
    js = tekst("kalkulator.js")
    assert re.search(r"function\s+obliczKoszt\s*\(|obliczKoszt\s*=\s*(function|\()", js), "kalkulator.js: brak funkcji obliczKoszt"
    for fraza, opis in (("addEventListener", "obsługi zdarzenia (addEventListener)"), ("preventDefault", "e.preventDefault() w obsłudze submit"), ("textContent", "wypisania wyniku przez textContent")):
        assert fraza in js, f"kalkulator.js: brak {opis}"
    assert "innerHTML" not in js, "kalkulator.js: znaleziono innerHTML — wstawiaj tekst przez textContent (bezpieczeństwo, XSS)"
    node = shutil.which("node")
    if not node:
        pytest.skip("Node.js nie jest zainstalowany — sprawdzono tylko strukturę skryptu (wyniki sprawdzisz w konsoli F12)")
    with tempfile.TemporaryDirectory() as td:
        skrypt = Path(td, "t.js")
        skrypt.write_text(NODE_TEST.replace("%KOD%", js), encoding="utf-8")
        p = subprocess.run([node, str(skrypt)], cwd=td, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    out = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ""
    assert "BRAK_FUNKCJI" not in out, "kalkulator.js: obliczKoszt nie jest dostępna jako funkcja globalna"
    assert out.startswith("{"), "kalkulator.js nie uruchamia się poza stroną (błąd JS):\n" + (p.stderr or p.stdout)[-800:]
    import json as _json
    d = _json.loads(out)
    ok(d["wyniki"][0], 480, "obliczKoszt(2, 2)")
    ok(d["wyniki"][1], 756, "obliczKoszt(7, 1)")
    ok(d["wyniki"][2], 629.94, "obliczKoszt(7, 1, 99.99) — zaokrąglenie do groszy")
    ok(d["wyniki"][3], 720, "obliczKoszt(6, 1)")
    ok(d["bledy"], ["blad"] * 4, "obliczKoszt dla (0, 1), (1.5, 1), (NaN, 1), (2, 0) — każdy ma rzucić błąd")


def test_pages():
    t = tekst("adres_strony.txt")
    assert re.search(r"https://[a-z0-9-]+\.github\.io/[\w.-]+/?", t, re.I), "adres_strony.txt: brak adresu w formacie https://NAZWA.github.io/REPO/"
