# Weryfikator tygodnia 3 — specyfikacja.md, walidacja.py, rabaty.py.

WYMAGANE = ["cel", "wejscie", "wynik", "przyklady", "przypadki brzegowe", "poza zakresem", "gotowe, gdy"]


def test_specyfikacja():
    s = sekcje_md(tekst("specyfikacja.md"))
    klucze = {k.replace(",", "").replace("  ", " "): v for k, v in s.items()}
    for w in WYMAGANE:
        k = w.replace(",", "")
        assert k in klucze, f"specyfikacja.md: brak sekcji „## {w.capitalize()}”"
        assert klucze[k], f"specyfikacja.md: sekcja „## {w.capitalize()}” jest pusta"
    przyklady = [l for l in klucze["przyklady"] if l.startswith(("-", "*")) and ("→" in l or "->" in l)]
    assert len(przyklady) >= 6, f"specyfikacja.md: {len(przyklady)} przykładów ze strzałką → (potrzeba ≥ 6, każdy w osobnej linii „- … → …”)"
    assert sum(1 for l in klucze["przypadki brzegowe"] if l.startswith(("-", "*"))) >= 3, "specyfikacja.md: potrzeba ≥ 3 przypadków brzegowych (linie „- …”)"
    assert sum(1 for l in klucze["poza zakresem"] if l.startswith(("-", "*"))) >= 2, "specyfikacja.md: potrzeba ≥ 2 pozycji „Poza zakresem”"


EMAILE = [("anna@pod-lipa.pl", True), ("  anna.nowak@pod-lipa.pl ", True), ("jan_k+rez@mail.example.com", True), ("anna@", False), ("@pod-lipa.pl", False),
          ("anna@pod-lipa", False), ("anna@@pod-lipa.pl", False), ("anna nowak@pod-lipa.pl", False), ("", False), ("anna@pod..pl", False),
          ("anna@pod-lipa.p", False), ("anna@.pod-lipa.pl", False), ("anna@pod-lipa.pl.", False), ("anna@pod lipa.pl", False)]
TELEFONY = [("600700800", True), ("600 700 800", True), ("600-700-800", True), ("+48 600 700 800", True), ("+48600700800", True), (" 600700800 ", True),
            ("48600700800", False), ("60070080", False), ("6007008000", False), ("abc", False), ("", False), ("+49 600 700 800", False), ("600 700 8OO", False)]


def test_walidacja_email():
    f = funkcja(modul("walidacja"), "czy_email")
    for t, w in EMAILE:
        assert f(t) is w, f"czy_email({t!r}): oczekiwano {w}, otrzymano {f(t)!r}"


def test_walidacja_telefon():
    f = funkcja(modul("walidacja"), "czy_telefon")
    for t, w in TELEFONY:
        assert f(t) is w, f"czy_telefon({t!r}): oczekiwano {w}, otrzymano {f(t)!r}"


def _r():
    m = modul("rabaty")
    return [funkcja(m, n) for n in ("sezon", "cena_nocy", "rabat", "do_zaplaty")]


def test_rabaty_sezon():
    sezon, cena, _, _ = _r()
    for m in range(1, 13):
        ok(sezon(m), "wysoki" if m in (6, 7, 8, 12) else "niski", f"sezon({m})")
        ok(cena(m), 150 if m in (6, 7, 8, 12) else 110, f"cena_nocy({m})")
    rzuca(sezon, 0, opis="sezon(0)")
    rzuca(sezon, 13, opis="sezon(13)")


def test_rabaty_rabat():
    _, _, rabat, _ = _r()
    for (n, o), w in {(3, 2): 0, (6, 3): 0, (7, 3): 10, (3, 4): 5, (6, 4): 5, (7, 4): 15, (14, 6): 15, (1, 1): 0}.items():
        ok(rabat(n, o), w, f"rabat({n}, {o})")
    rzuca(rabat, 0, 2, opis="rabat(0, 2)")
    rzuca(rabat, 2, 0, opis="rabat(2, 0)")


def test_rabaty_do_zaplaty():
    _, _, _, dz = _r()
    ok(dz(7, 7, 2), 1890.0, "do_zaplaty(7, 7, 2) — lipiec, 7 nocy, 2 osoby")
    ok(dz(3, 2, 1), 220, "do_zaplaty(3, 2, 1) — marzec, bez rabatu")
    ok(dz(12, 7, 4), 3570.0, "do_zaplaty(12, 7, 4) — grudzień, rabat 15%")
    ok(dz(5, 3, 4), 1254.0, "do_zaplaty(5, 3, 4) — maj, 4 osoby, rabat 5%")
