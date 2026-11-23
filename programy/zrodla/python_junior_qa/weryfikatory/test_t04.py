# Weryfikator tygodnia 4 — gałąź i pull request (TYDZIEN4.md), zapis.py, csv_odczyt.py, odzyskiwanie.md, magazyn_csv.py.
import csv as _csv

CSV_TEST = ("id,nazwa,kategoria,cena,ilosc\n"
            "1,Zeszyt A5 w kratkę,zeszyty,4.50,120\n"
            "3,Długopis niebieski,pisaki,2.30,300\n"
            "9,\"Papier ksero A4, 500 ark.\",papier,24.99,35\n"
            "17,Zszywki 1000 szt.,biuro,3.90,0\n"
            "14,Segregator A4,biuro,11.90,45\n")


def _csv_plik(tmp_path, tresc=CSV_TEST):
    p = tmp_path / "produkty.csv"
    p.write_text(tresc, encoding="utf-8")
    return p


def test_galaz_pr():
    repo()
    kod, galezie = git("branch", "-a", "--format=%(refname:short)")
    nazwy = [g.strip() for g in galezie.splitlines()]
    kandydaci = [g for g in nazwy if g.endswith("feature/tydzien4")]
    assert kandydaci, "Brak gałęzi feature/tydzien4 (lokalnie albo na GitHubie: git branch -a) — git switch -c feature/tydzien4"
    assert any(git("merge-base", "--is-ancestor", g, "HEAD")[0] == 0 for g in kandydaci), \
        "Gałąź feature/tydzien4 nie jest scalona z bieżącą gałęzią — Merge pull request na GitHubie, potem git switch main i git pull"
    kod, pliki = git("ls-files")
    assert "TYDZIEN4.md" in pliki.split(), "TYDZIEN4.md nie jest w repozytorium na gałęzi main"
    assert len([l for l in tekst("TYDZIEN4.md").splitlines() if l.strip()]) >= 3, "TYDZIEN4.md: co najmniej 3 niepuste linie (co zrobiłem w tygodniu 4)"


def test_zapis(tmp_path):
    m = modul("zapis")
    zap, wcz, dop = funkcja(m, "zapisz_liste"), funkcja(m, "wczytaj_liste"), funkcja(m, "dopisz")
    p = tmp_path / "produkty.txt"
    zap(["Zeszyt A5", "Długopis niebieski", "Gumka"], p)
    assert p.read_bytes().decode("utf-8").splitlines() == ["Zeszyt A5", "Długopis niebieski", "Gumka"], "zapisz_liste: każdy element w osobnej linii, kodowanie utf-8"
    dop(p, "Klej w sztyfcie")
    ok(wcz(p), ["Zeszyt A5", "Długopis niebieski", "Gumka", "Klej w sztyfcie"], "wczytaj_liste po dopisz")
    p.write_text("  Zeszyt  \n\nKlej\n\n", encoding="utf-8")
    ok(wcz(p), ["Zeszyt", "Klej"], "wczytaj_liste — bez spacji na brzegach i bez pustych linii")
    zap([], p)
    ok(wcz(p), [], "zapisz_liste([]) i wczytaj")
    ok(wcz(tmp_path / "nie_ma.txt"), [], "wczytaj_liste dla nieistniejącego pliku zwraca []")


def test_csv_odczyt(tmp_path):
    m = modul("csv_odczyt")
    wcz, sr, brak, wart = (funkcja(m, n) for n in ("wczytaj", "srednia_cena", "brak_na_stanie", "wartosc_magazynu"))
    p = wcz(_csv_plik(tmp_path))
    ok(len(p), 5, "liczba wczytanych produktów")
    ok(p[2]["nazwa"], "Papier ksero A4, 500 ark.", "nazwa z przecinkiem w cudzysłowie")
    assert isinstance(p[0]["cena"], float) and isinstance(p[0]["ilosc"], int), "wczytaj: cena jako float, ilosc jako int"
    ok(sr(p), 9.52, "srednia_cena (zaokrąglona do 2 miejsc)")
    ok(brak(p), ["Zszywki 1000 szt."], "brak_na_stanie")
    ok(wart(p), 2640.15, "wartosc_magazynu (suma cena × ilość, 2 miejsca)")
    ok(sr([]), 0, "srednia_cena([])")
    ok(wart([]), 0, "wartosc_magazynu([])")


def test_odzyskiwanie():
    s = sekcje_md(tekst("odzyskiwanie.md"))
    for slowo in ("restore", "stash", "revert"):
        klucz = next((k for k in s if slowo in k), None)
        assert klucz, f"odzyskiwanie.md: brak sekcji z „{slowo}” w nagłówku (np. „## git {slowo}”)"
        tresc = " ".join(s[klucz])
        assert len(tresc.split()) >= 15, f"odzyskiwanie.md: sekcja „{slowo}” — co najmniej 15 słów: kiedy używasz, co robi, czego nie cofniesz"
        assert f"git {slowo}" in tresc, f"odzyskiwanie.md: w sekcji „{slowo}” wpisz polecenie, którego użyłeś(-aś) (git {slowo} …)"


def test_magazyn_csv(tmp_path):
    m = modul("magazyn_csv")
    wcz, zap, dodaj, stat, szukaj = (funkcja(m, n) for n in ("wczytaj", "zapisz", "dodaj", "statystyki", "szukaj"))
    p = wcz(_csv_plik(tmp_path))
    st = stat(p)
    ok(st["liczba"], 5, "statystyki: liczba")
    ok(st["srednia_cena"], 9.52, "statystyki: srednia_cena")
    ok(st["najdrozszy"], "Papier ksero A4, 500 ark.", "statystyki: najdrozszy")
    ok(st["wartosc"], 2640.15, "statystyki: wartosc")
    ok(stat([]), {"liczba": 0, "srednia_cena": 0, "najdrozszy": None, "wartosc": 0}, "statystyki([])")
    dodaj(p, "Klej w sztyfcie", "akcesoria", 3.4, 110)
    ok(p[-1]["id"], 18, "id nowego produktu = największe id + 1")
    for zle, opis in ((("zeszyt a5 w kratkę", "zeszyty", 1.0, 1), "duplikat nazwy (bez względu na wielkość liter)"),
                      (("Nowy", "biuro", -1, 5), "cena ujemna"), (("Nowy", "biuro", 2.0, -1), "ilość ujemna"), (("", "biuro", 2.0, 1), "pusta nazwa")):
        rzuca(dodaj, p, *zle, opis=f"dodaj — {opis}")
    ok(len(p), 6, "liczba produktów po błędnych próbach dodania (bez zmian)")
    ok([x["nazwa"] for x in szukaj(p, "BIURO")], ["Zszywki 1000 szt.", "Segregator A4"], "szukaj(\"BIURO\") — po kategorii, bez wielkości liter")
    ok([x["nazwa"] for x in szukaj(p, "zeszyt")], ["Zeszyt A5 w kratkę"], "szukaj(\"zeszyt\") — po nazwie")
    ok(szukaj(p, "farby"), [], "szukaj(\"farby\")")
    cel = tmp_path / "zapis.csv"
    zap(p, cel)
    ok(wcz(cel), p, "zapisz → wczytaj daje te same dane")
    with open(cel, encoding="utf-8", newline="") as f:
        assert next(_csv.reader(f)) == ["id", "nazwa", "kategoria", "cena", "ilosc"], "zapisz: nagłówek id,nazwa,kategoria,cena,ilosc"
