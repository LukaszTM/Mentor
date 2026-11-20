"""Walidacja e-maila i telefonu gościa."""


def czy_email(tekst):
    t = (tekst or "").strip()
    if t.count("@") != 1 or " " in t:
        return False
    lokalna, domena = t.split("@")
    if not lokalna or "." not in domena or ".." in domena or domena.startswith(".") or domena.endswith("."):
        return False
    koncowka = domena.rsplit(".", 1)[1]
    return len(koncowka) >= 2 and koncowka.isalpha()


def czy_telefon(tekst):
    t = (tekst or "").strip().replace(" ", "").replace("-", "")
    if t.startswith("+48"):
        t = t[3:]
    return len(t) == 9 and t.isdigit()
