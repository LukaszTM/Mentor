# Weryfikator tygodnia 0 — struktura katalogu roboczego i słowniczek.


def test_struktura_foldery():
    for f in ("notatki", "dane"):
        assert (WS / f).is_dir(), f"Brak folderu {f} bezpośrednio w katalogu roboczym {WS} (nazwa małymi literami, bez spacji)"


def test_struktura_o_mnie():
    p = WS / "notatki" / "o_mnie.md"
    if not p.exists() and (WS / "notatki" / "o_mnie.md.txt").exists():
        pytest.fail("Jest notatki/o_mnie.md.txt — rozszerzenia były ukryte; zmień nazwę na o_mnie.md")
    assert p.exists(), "Brak pliku notatki/o_mnie.md"
    linie = [l.strip() for l in p.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    assert any(l.startswith("#") for l in linie), "notatki/o_mnie.md: brak nagłówka zaczynającego się od #"
    assert sum(1 for l in linie if l.startswith(("- ", "* "))) >= 2, "notatki/o_mnie.md: potrzebne co najmniej 2 punkty listy (linie zaczynające się od „- ”)"


def test_struktura_dziennik():
    t = tekst("dziennik.md")
    assert re.search(r"\b20\d\d-\d\d-\d\d\b|\b\d{1,2}\.\d{1,2}\.20\d\d\b", t), "dziennik.md: brak wpisu z datą (RRRR-MM-DD albo DD.MM.RRRR) — zamień RRRR-MM-DD z szablonu na dzisiejszą datę"
    tresc = [l for l in t.splitlines() if l.strip().startswith("-") and len(l.split(":", 1)[-1].strip()) >= 3]
    assert tresc, "dziennik.md: wpisz treść przynajmniej przy jednym punkcie (co zrobiłem / co sprawdziłem / czego nie rozumiem)"


POJECIA = ["model", "token", "kontekst", "halucynacja", "agent", "prompt", "specyfikacja", "test"]


def test_slowniczek():
    t = tekst("slowniczek.md")
    znalezione = {}
    for linia in t.splitlines():
        m = re.match(r"^\s*[-*]\s*\**([^:*]+?)\**\s*:\s*(.*)$", linia)
        if m:
            znalezione[norm(m.group(1)).strip()] = m.group(2).strip()
    for p in POJECIA:
        assert p in znalezione, f"slowniczek.md: brak pojęcia „{p}” w formacie „- {p}: wyjaśnienie”"
        assert len(znalezione[p].split()) >= 6, f"slowniczek.md: wyjaśnienie pojęcia „{p}” ma mniej niż 6 słów — napisz je pełnym zdaniem"
