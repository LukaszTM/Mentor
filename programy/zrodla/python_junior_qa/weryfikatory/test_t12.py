# Weryfikator tygodnia 12 — README projektu, PLAN_TESTOW.md, RECENZJA.md powiązana z commitami, dziennik aplikacji.


def test_readme_projektu():
    t = tekst("README.md")
    s = sekcje_md(t)
    for k in ("jak uruchomic", "jak testuj"):
        klucz = next((x for x in s if k in x), None)
        assert klucz, f"README.md: brak sekcji „## {'Jak uruchomić' if 'uruch' in k else 'Jak testuję'}”"
    jt = next(x for x in s if "jak testuj" in x)
    assert len(" ".join(s[jt]).split()) >= 25, "README.md: „Jak testuję” — co najmniej 25 słów: poziomy testów, narzędzia, liczba testów, jak uruchomić"
    assert re.search(r"!\[[^\]]*\]\([^)]+\.(png|jpg|jpeg|gif)\)", t, re.I), "README.md: zrzut ekranu aplikacji ![opis](zrzuty/lista.png)"
    assert "badge.svg" in t, "README.md: odznaka CI"
    for z in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", t):
        if not z.startswith("http"):
            assert (WS / z).exists(), f"README.md: obrazek {z} nie istnieje w repozytorium"


def test_plan_testow():
    s = sekcje_md(tekst("PLAN_TESTOW.md"))
    for k in ("zakres", "poza zakresem", "ryzyka", "poziomy", "recznie", "kryteria"):
        klucz = next((x for x in s if k in x), None)
        assert klucz and s[klucz], f"PLAN_TESTOW.md: brak (albo pusta) sekcja z „{k}” w nagłówku"
    r = next(x for x in s if "ryzyka" in x)
    assert sum(1 for l in s[r] if l.startswith(("-", "*", "|"))) >= 3, "PLAN_TESTOW.md: co najmniej 3 ryzyka"
    d = next((x for x in s if "defekt" in x), None)
    assert d and sum(1 for l in s[d] if l.startswith(("-", "*"))) >= 3, "PLAN_TESTOW.md: sekcja „## Znalezione defekty” z co najmniej 3 pozycjami (z odnośnikiem do raportu)"


def test_recenzja():
    t = tekst("RECENZJA.md")
    uwagi = re.split(r"^##\s+", t, flags=re.M)[1:]
    assert len(uwagi) >= 3, f"RECENZJA.md: {len(uwagi)} uwag — opisz co najmniej 3 (## Uwaga 1 …)"
    repo()
    for u in uwagi:
        tyt = u.split("\n", 1)[0].strip()
        assert "decyzja" in norm(u), f"RECENZJA.md „{tyt}”: zapisz decyzję (wdrażam / nie wdrażam i dlaczego)"
    wdrozone = 0
    for sha in set(re.findall(r"\b[0-9a-f]{7,40}\b", t)):
        if git("cat-file", "-t", sha)[1].strip() == "commit":
            wdrozone += 1
    assert wdrozone >= 3, "RECENZJA.md: przy 3 wdrożonych uwagach podaj skrót commita (np. 3f2a1c9) — commity muszą istnieć w repozytorium"


def test_dziennik_aplikacji():
    t = tekst("dziennik_aplikacji.md")
    wiersze = [l for l in t.splitlines() if l.strip().startswith("|") and re.search(r"\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{4}", l)]
    assert len(wiersze) >= 5, f"dziennik_aplikacji.md: {len(wiersze)} aplikacji z datą — potrzeba 5 wierszy tabeli (data | firma | stanowisko | link | status)"
    for w in wiersze:
        kom = [c.strip() for c in w.strip().strip("|").split("|")]
        assert len(kom) >= 5 and all(kom[:5]), f"dziennik_aplikacji.md: wiersz „{w.strip()[:60]}…” — uzupełnij datę, firmę, stanowisko, link i status"
