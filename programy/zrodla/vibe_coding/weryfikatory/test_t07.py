# Weryfikator tygodnia 7 — zepsute_raporty.py, stan.md, kalendarz.py.

R = [{"pokoj": "Lipowy", "noce": 3, "kwota": 720}, {"pokoj": "Dębowy", "noce": 2, "kwota": 440}, {"pokoj": "Lipowy", "noce": 2, "kwota": 480},
     {"pokoj": "Klonowy", "noce": 5, "kwota": 1100}, {"pokoj": "Dębowy", "noce": 5, "kwota": 1000}]


def test_raporty_suma():
    f = funkcja(modul("zepsute_raporty"), "suma_przychodu")
    ok(f(R), 3740, "suma_przychodu(5 rezerwacji)")
    ok(f([]), 0, "suma_przychodu([])")


def test_raporty_srednia():
    f = funkcja(modul("zepsute_raporty"), "srednia_dlugosc")
    ok(f(R), 3.4, "srednia_dlugosc(5 rezerwacji) — (3+2+2+5+5)/5")
    ok(f(R[:2]), 2.5, "srednia_dlugosc(2 rezerwacje)")
    ok(f([]), 0, "srednia_dlugosc([])")


def test_raporty_top():
    f = funkcja(modul("zepsute_raporty"), "top_pokoje")
    ok([tuple(x) for x in f(R)], [("Dębowy", 7), ("Klonowy", 5), ("Lipowy", 5)], "top_pokoje(R)")
    ok([tuple(x) for x in f(R, 1)], [("Dębowy", 7)], "top_pokoje(R, 1)")
    ok([tuple(x) for x in f(R[:1], 5)], [("Lipowy", 3)], "top_pokoje(1 rezerwacja, n=5)")


def test_stan():
    t = tekst("stan.md")
    niepuste = [l for l in t.splitlines() if l.strip()]
    assert len(niepuste) <= 20, f"stan.md ma {len(niepuste)} niepustych linii — notatka przekazania ma być krótka (≤ 20)"
    s = sekcje_md(t)
    for k in ("zrobione", "decyzje", "nastepny krok"):
        assert k in s, f"stan.md: brak sekcji „## {k.capitalize()}”"
        assert any(len(l.strip("-* ").strip()) >= 3 for l in s[k]), f"stan.md: sekcja „{k}” jest pusta"


def _kal():
    m = modul("kalendarz")
    return [funkcja(m, n) for n in ("noce", "koliduje", "czy_wolny", "wolne_pokoje")]


def r(p, od, do):
    return {"pokoj": p, "od": od, "do": do}


def test_kalendarz_noce():
    noce, *_ = _kal()
    ok(noce("2026-12-20", "2026-12-23"), 3, "noce(20.12, 23.12)")
    ok(noce("2026-12-28", "2027-01-02"), 5, "noce(28.12.2026, 2.01.2027)")
    ok(noce("2028-02-28", "2028-03-01"), 2, "noce(28.02.2028, 1.03.2028) — rok przestępny")
    rzuca(noce, "2026-12-23", "2026-12-20", opis="noce(do przed od)")
    rzuca(noce, "2026-12-20", "2026-12-20", opis="noce(od == do)")


def test_kalendarz_koliduje():
    _, kol, _, _ = _kal()
    a = r("Lipowy", "2026-12-20", "2026-12-23")
    assert kol(a, r("Lipowy", "2026-12-23", "2026-12-25")) is False, "wyjazd w dniu przyjazdu nie jest kolizją (Lipowy 20–23 i 23–25)"
    assert kol(r("Lipowy", "2026-12-23", "2026-12-25"), a) is False, "kolejność argumentów nie może zmieniać wyniku (23–25 i 20–23)"
    assert kol(a, r("Lipowy", "2026-12-22", "2026-12-24")) is True, "Lipowy 20–23 i 22–24 kolidują"
    assert kol(a, r("Dębowy", "2026-12-20", "2026-12-23")) is False, "różne pokoje nie kolidują"
    assert kol(a, r("Lipowy", "2026-12-18", "2026-12-26")) is True, "przedział obejmujący (18–26) koliduje z 20–23"
    assert kol(a, r("Lipowy", "2026-12-21", "2026-12-22")) is True, "przedział wewnątrz (21–22) koliduje z 20–23"


def test_kalendarz_wolne():
    _, _, wolny, wolne = _kal()
    rez = [r("Lipowy", "2026-12-20", "2026-12-23"), r("Klonowy", "2026-12-22", "2026-12-27")]
    assert wolny(rez, "Lipowy", "2026-12-23", "2026-12-25") is True, "Lipowy wolny od 23.12 (dzień wyjazdu poprzedniego gościa)"
    assert wolny(rez, "Lipowy", "2026-12-19", "2026-12-21") is False, "Lipowy zajęty 20–23"
    ok(list(wolne(rez, "2026-12-21", "2026-12-22")), ["Dębowy", "Klonowy"], "wolne_pokoje 21–22.12")
    ok(list(wolne(rez, "2026-12-22", "2026-12-24")), ["Dębowy"], "wolne_pokoje 22–24.12")
    ok(list(wolne([], "2026-12-01", "2026-12-02")), ["Lipowy", "Dębowy", "Klonowy"], "wolne_pokoje bez rezerwacji — kolejność Lipowy, Dębowy, Klonowy")


def test_kalendarz_proces():
    repo()
    kod, log = git("log", "--format=%h", "--", "kalendarz.py")
    n = len([l for l in log.splitlines() if l.strip()]) if kod == 0 else 0
    assert n >= 4, f"W historii Gita jest {n} commitów zmieniających kalendarz.py — proces wymaga commita po każdym z 4 kroków"
