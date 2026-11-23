# Weryfikator tygodnia 8 — skrypty Selenium (budowa kodu), lokatory sklepu testowego, Page Object LoginPage (na sterowniku-atrapie), testy E2E w POM.
import ast as _ast

# lokatory sklepu testowego (projekty/sklep_testowy/README.md)
ID_SKLEPU = {"login", "haslo", "promocja", "szukaj", "szukaj-btn", "produkty", "koszyk", "kod", "zastosuj", "do-zamowienia", "imie", "email", "kod_pocztowy",
             "link-koszyk", "wyloguj"} | {f"ilosc-{i}" for i in range(1, 21)} | {f"dodaj-{i}" for i in range(1, 21)}
DATA_TEST = {"zaloguj", "blad", "powitanie", "liczba-wynikow", "brak-wynikow", "dodaj", "suma", "pusty", "rabat-ok", "zamawiam", "komunikat"}
TEKSTY = {"Zaloguj", "Szukaj", "Dodaj do koszyka", "Zastosuj", "Zamawiam", "Przejdź do zamówienia", "Wyloguj", "Koszyk", "Produkty"}


def _znany(wartosc):
    w = str(wartosc)
    return (any(re.search(rf"#{re.escape(i)}\b|id\s*=\s*['\"]{re.escape(i)}['\"]|@id\s*=\s*['\"]{re.escape(i)}['\"]", w) for i in ID_SKLEPU)
            or w in ID_SKLEPU or any(f"data-test={d}" in w.replace("'", "").replace('"', "") for d in DATA_TEST) or any(t in w for t in TEKSTY)
            or re.search(r"\.(produkt|pozycja|nazwa|cena|stan|ilosc)\b", w) or re.search(r"\bname\s*=\s*['\"]?(login|haslo|q|ilosc|kod|imie|email|kod_pocztowy)", w))


def _sleep(nazwa):
    return any(isinstance(w, _ast.Call) and getattr(w.func, "attr", getattr(w.func, "id", "")) == "sleep" for w in _ast.walk(drzewo(nazwa)))


def _quit_w_finally_albo_fixturze(nazwa):
    for w in _ast.walk(drzewo(nazwa)):
        if isinstance(w, _ast.Try) and any(isinstance(c, _ast.Call) and getattr(c.func, "attr", "") == "quit" for f in w.finalbody for c in _ast.walk(f)):
            return True
        if isinstance(w, _ast.FunctionDef) and any(isinstance(y, _ast.Yield) for y in _ast.walk(w)) \
                and "quit" in [getattr(c.func, "attr", "") for c in _ast.walk(w) if isinstance(c, _ast.Call)]:
            return True
    return False


def test_selenium_start():
    w = wywolania("selenium_start.py")
    for f in ("get", "find_element", "send_keys", "click", "save_screenshot", "quit"):
        assert f in w, f"selenium_start.py: brak wywołania {f}(…) — skrypt ma otworzyć sklep, zalogować się, zrobić zrzut i zamknąć przeglądarkę"
    assert "127.0.0.1:5001" in tekst("selenium_start.py"), "selenium_start.py: otwórz sklep testowy http://127.0.0.1:5001"
    assert w.count("find_element") >= 3, "selenium_start.py: co najmniej 3 elementy (login, hasło, przycisk)"
    assert _quit_w_finally_albo_fixturze("selenium_start.py"), "selenium_start.py: driver.quit() w bloku finally — przeglądarka zamknie się też po błędzie"


def test_lokatory():
    m = modul("lokatory")
    from selenium.webdriver.common.by import By
    lok = getattr(m, "LOKATORY", None)
    assert isinstance(lok, dict) and len(lok) >= 5, "lokatory.py: słownik LOKATORY z co najmniej 5 elementami strony"
    for nazwa, sposoby in lok.items():
        assert isinstance(sposoby, (list, tuple)) and len(sposoby) >= 3, f"LOKATORY[{nazwa!r}]: lista trzech lokatorów (ID, CSS, XPath)"
        rodzaje = {s[0] for s in sposoby}
        assert rodzaje >= {By.ID, By.CSS_SELECTOR, By.XPATH} or (len(rodzaje) >= 3 and By.CSS_SELECTOR in rodzaje and By.XPATH in rodzaje), \
            f"LOKATORY[{nazwa!r}]: trzy różne sposoby — By.ID (albo By.NAME przy braku id), By.CSS_SELECTOR, By.XPATH"
        for by, wartosc in sposoby:
            assert _znany(wartosc), f"LOKATORY[{nazwa!r}]: {by} = {wartosc!r} nie pasuje do żadnego elementu sklepu testowego (README sklepu: id, data-test, teksty przycisków)"
            if by == By.XPATH:
                assert not str(wartosc).startswith("/html"), f"LOKATORY[{nazwa!r}]: XPath od /html jest kruchy — zacznij od // i atrybutu albo tekstu"


def test_formularz():
    w = wywolania("formularz.py")
    t = tekst("formularz.py")
    assert "until" in w and "WebDriverWait" in t, "formularz.py: czekaj na elementy WebDriverWait(…).until(EC.…)"
    assert "expected_conditions" in t, "formularz.py: warunki z selenium.webdriver.support.expected_conditions"
    assert not _sleep("formularz.py"), "formularz.py: bez time.sleep — czekanie na warunek"
    assert w.count("send_keys") >= 3, "formularz.py: wypełnij co najmniej 3 pola formularza zamówienia"
    for pole in ("imie", "email", "kod_pocztowy"):
        assert pole in t, f"formularz.py: brak pola {pole} formularza zamówienia"
    assert "komunikat" in t or "blad" in t, "formularz.py: odczytaj komunikat po wysłaniu ([data-test=komunikat] albo [data-test=blad])"
    assert _quit_w_finally_albo_fixturze("formularz.py"), "formularz.py: driver.quit() w finally"


class _El:
    def __init__(self, drv, loc):
        self.drv, self.loc, self.text = drv, loc, drv.teksty.get(loc[1], "")

    def send_keys(self, *t):
        self.drv.log.append(("send_keys", self.loc[1], "".join(map(str, t))))

    def click(self):
        self.drv.log.append(("click", self.loc[1]))

    def clear(self):
        self.drv.log.append(("clear", self.loc[1]))

    def is_displayed(self):
        return True

    def is_enabled(self):
        return True

    def get_attribute(self, n):
        return self.text


class _Driver:
    """Atrapa WebDrivera: zapisuje działania strony, nie otwiera przeglądarki."""
    def __init__(self):
        self.log, self.url = [], ""
        self.teksty = {"[data-test=blad]": "Błędny login lub hasło", "blad": "Błędny login lub hasło"}

    def get(self, url):
        self.url = url
        self.log.append(("get", url))

    def find_element(self, by, wartosc):
        return _El(self, (by, wartosc))

    def find_elements(self, by, wartosc):
        return [_El(self, (by, wartosc))]


def _login_page():
    for n in ("login_page", "pages.login_page"):
        if (WS / (n.replace(".", "/") + ".py")).exists():
            if n.startswith("pages") and str(WS) not in sys.path:
                sys.path.insert(0, str(WS))
            m = modul("login_page") if n == "login_page" else __import__(n, fromlist=["LoginPage"])
            return getattr(m, "LoginPage", None)
    pytest.fail("Brak pliku login_page.py (w PRACA albo w pages/)")


def test_login_page():
    LoginPage = _login_page()
    assert LoginPage, "login_page.py: klasa LoginPage"
    d = _Driver()
    s = LoginPage(d)
    for nazwa in ("open", "login", "error_text"):
        assert callable(getattr(s, nazwa, None)), f"LoginPage: brak metody {nazwa}()"
    s.open()
    assert d.url.endswith("/logowanie") and "127.0.0.1:5001" in d.url, f"open(): oczekiwano adresu http://127.0.0.1:5001/logowanie, otwarto {d.url!r}"
    s.login("tester", "zle-haslo")
    wpisy = {(a, b): c for a, b, *c in [x for x in d.log if x[0] == "send_keys"]}
    assert any(k[1] in ("login", "#login") and v == ["tester"] for k, v in wpisy.items()), "login(): wpisz login do pola #login"
    assert any(k[1] in ("haslo", "#haslo", "input[name=haslo]") and v == ["zle-haslo"] for k, v in wpisy.items()), "login(): wpisz hasło do pola #haslo"
    assert any(x[0] == "click" and ("zaloguj" in x[1].lower()) for x in d.log), "login(): kliknij przycisk [data-test=zaloguj]"
    kolejnosc = [x[0] for x in d.log if x[0] in ("send_keys", "click")]
    assert kolejnosc[-1] == "click", "login(): najpierw wpisz dane, na końcu kliknij"
    assert "Błędny login" in str(s.error_text()), "error_text(): zwróć tekst elementu [data-test=blad]"
    for atr in ("LOGIN", "HASLO", "ZALOGUJ", "BLAD"):
        assert isinstance(getattr(LoginPage, atr, None), tuple), f"LoginPage: lokator {atr} jako krotka (By…, \"…\") w klasie"
    assert not _sleep("login_page.py" if (WS / "login_page.py").exists() else "pages/login_page.py"), "LoginPage: bez time.sleep"


def test_testy_e2e():
    nazwa = "test_sklep.py" if (WS / "test_sklep.py").exists() else "tests/test_sklep.py"
    t = tekst(nazwa)
    testy = re.findall(r"^def (test_\w+)\(", t, re.M)
    assert len(testy) >= 5, f"{nazwa}: {len(testy)} testów — potrzeba 5 (logowanie, błędne hasło, koszyk, zamówienie, wylogowanie albo podobne)"
    assert "LoginPage" in t, f"{nazwa}: testy używają Page Objectów (LoginPage i inne)"
    assert not _sleep(nazwa), f"{nazwa}: bez time.sleep"
    fx = tekst("conftest.py") if (WS / "conftest.py").exists() else t
    assert "@pytest.fixture" in fx and "yield" in fx and "quit" in fx, "fixture przeglądarki (w conftest.py albo w pliku testów): @pytest.fixture, yield driver, driver.quit()"
    assert re.search(r"assert\s", t), f"{nazwa}: asercje są w testach"
