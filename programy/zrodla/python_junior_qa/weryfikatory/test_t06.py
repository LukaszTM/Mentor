# Weryfikator tygodnia 6 — do_poprawy.py (debugowanie), notatki_projekt.md, bmi.py po refaktoryzacji, README.md, porządek w repozytorium.
import ast as _ast


def test_debugowanie():
    m = modul("do_poprawy")
    sr, razem, kat = funkcja(m, "srednia_ceny"), funkcja(m, "razem_koszyka"), funkcja(m, "kategoria_ceny")
    ok(sr([4.0, 2.0, 6.0]), 4.0, "srednia_ceny([4.0, 2.0, 6.0]) — błąd 1: pierwszy element pomijany")
    ok(sr([10.0]), 10.0, "srednia_ceny([10.0])")
    ok(sr([]), 0, "srednia_ceny([]) — pusta lista")
    ok(razem([(2.0, 3), (5.0, 2)]), 16.0, "razem_koszyka — błąd 2: suma nadpisywana zamiast dodawana")
    ok(razem([]), 0, "razem_koszyka([])")
    for cena, w in ((5, "tani"), (9.99, "tani"), (10, "średni"), (49.99, "średni"), (50, "drogi"), (500, "drogi")):
        ok(kat(cena), w, f"kategoria_ceny({cena}) — błąd 3: kolejność progów")


def test_notatki_projekt():
    s = sekcje_md(tekst("notatki_projekt.md"))
    for f in ("readme.md", "app.py", "baza.py", "raport.py"):
        klucz = next((k for k in s if f.replace(".", "") in k.replace(".", "")), None)
        assert klucz, f"notatki_projekt.md: brak sekcji dla pliku {f} (np. „## {f}”)"
        assert len(" ".join(s[klucz]).split()) >= 10, f"notatki_projekt.md: sekcja {f} — co najmniej 10 słów: odpowiedzialność pliku i najważniejsze funkcje"
    pyt = next((k for k in s if "pytania" in k), None)
    assert pyt and any(l.startswith(("-", "*")) for l in s[pyt]), "notatki_projekt.md: sekcja „## Pytania” z co najmniej jednym pytaniem w formie listy"


def test_bmi_refaktoryzacja():
    m = modul("bmi")
    obl, kat = funkcja(m, "oblicz_bmi"), funkcja(m, "kategoria")
    ok(obl(81, 1.80), 25.0, "oblicz_bmi(81, 1.80)")
    ok(obl(50, 1.70), 17.3, "oblicz_bmi(50, 1.70)")
    for zle in ((0, 1.7), (70, 0), (-5, 1.7), (80, 180)):
        rzuca(obl, *zle, opis=f"oblicz_bmi{zle}")
    for bmi, w in ((18.4, "niedowaga"), (18.5, "norma"), (24.9, "norma"), (25, "nadwaga"), (29.9, "nadwaga"), (30, "otyłość")):
        ok(kat(bmi), w, f"kategoria({bmi})")
    for n in ("oblicz_bmi", "kategoria"):
        assert (getattr(m, n).__doc__ or "").strip(), f"bmi.py: funkcja {n} bez docstringu"
    stale = [w.targets[0].id for w in drzewo("bmi.py").body if isinstance(w, _ast.Assign) and isinstance(w.targets[0], _ast.Name) and w.targets[0].id.isupper()]
    assert stale, "bmi.py: progi jako stałe na górze pliku (np. PROG_NADWAGI = 25) zamiast liczb w warunkach"


def test_readme():
    t = tekst("README.md")
    assert t.lstrip().startswith("# "), "README.md: pierwsza linia to tytuł „# …”"
    s = sekcje_md(t)
    proj = next((k for k in s if "projekty" in k), None)
    assert proj, "README.md: brak sekcji „## Projekty”"
    wiersze = [l for l in s[proj] if l.startswith("|") and not set(l) <= set("|-: ")]
    assert len(wiersze) >= 5, f"README.md: tabela projektów — nagłówek + co najmniej 4 projekty (jest {max(len(wiersze) - 1, 0)})"
    uru = next((k for k in s if "jak uruchomic" in k), None)
    assert uru, "README.md: brak sekcji „## Jak uruchomić”"
    assert "```" in t.split("##", 1)[-1], "README.md: polecenia uruchomienia w bloku kodu (```)"


ZLE_OPISY = {"zmiany", "asdf", "final", "final2", "x", "update", "commit", "fix", "poprawki", "test"}


def test_porzadek_repo():
    gi = tekst(".gitignore")
    for w in (".venv", "__pycache__", ".env"):
        assert w in gi, f".gitignore: brak wpisu {w}"
    repo()
    kod, pliki = git("ls-files")
    sledzone = pliki.split()
    zle = [p for p in sledzone if p.startswith(".venv/") or "__pycache__/" in p or p.endswith(".pyc") or p.split("/")[-1] == ".env"]
    assert not zle, f"W repozytorium są pliki, które powinny być ignorowane: {zle[:5]} — git rm -r --cached …"
    wzor = re.compile(r"(api_key|apikey|token|haslo|password|secret)\s*=\s*['\"][^'\"]{6,}['\"]", re.I)
    for p in sledzone:
        if p.endswith((".py", ".md", ".txt", ".json", ".yml", ".yaml", ".cfg", ".ini")) and (WS / p).is_file():
            assert not wzor.search((WS / p).read_text(encoding="utf-8", errors="ignore")), f"{p}: wygląda na sekret (hasło/klucz) zapisany w kodzie — usuń, unieważnij, przenieś do .env"
    kod, log = git("log", "--format=%s")
    opisy = [l.strip() for l in log.splitlines() if l.strip()]
    assert len(opisy) >= 5, f"Historia ma {len(opisy)} commitów — porządkuj małymi krokami (co najmniej 5 commitów)"
    slabe = [o for o in opisy if o.lower() in ZLE_OPISY]
    assert len(slabe) <= len(opisy) // 5, f"Za dużo commitów z opisem bez treści ({len(slabe)}): {slabe[:5]} — opisuj, co zmieniasz („Dodaj…”, „Popraw…”)"
