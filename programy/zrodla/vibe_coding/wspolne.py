# -*- coding: utf-8 -*-
"""Wspólne pomocniki źródeł kursu „Vibe coding od podstaw” (lekcje, ćwiczenia, zadania, quizy, klucze odpowiedzi).

Każda lekcja powstaje przez L(...), które pilnuje bloków standardu (STANDARD_KURSOW.md §3), każde zadanie przez Z(...).
Kod z ćwiczeń „co wypisze program?” jest zapisywany w KOD_DO_SPRAWDZENIA i uruchamiany w testach (testy/test_vibe.py) —
klucz odpowiedzi nie może się rozjechać z tym, co naprawdę wypisuje Python.
"""

TN = ["tak", "nie"]
KOD_DO_SPRAWDZENIA = []          # (gdzie, kod, oczekiwane_wyjście) — sprawdzane w testach


# ------------------------------------------------------------------ pola odpowiedzi (sprawdzanie automatyczne)
def kw(i, et, w, **k):
    return dict(id=i, etykieta=et, typ="kwota", wartosc=w, **k)


def li(i, et, w, **k):
    return dict(id=i, etykieta=et, typ="liczba", wartosc=w, **k)


def tx(i, et, w=None, **k):
    d = dict(id=i, etykieta=et, typ="tekst", **k)
    if w is not None:
        d["wartosc"] = w
    return d


def wy(i, et, opcje, w, **k):
    return dict(id=i, etykieta=et, typ="wybor", opcje=list(opcje), wartosc=w, **k)


def bl(w, kom):
    return {"wartosc": w, "komunikat": kom}


def kod(gdzie, zrodlo, wyjscie):
    """Rejestruje fragment kodu i jego oczekiwane wyjście (sprawdzane w testach); zwraca kod do wstawienia w treść."""
    KOD_DO_SPRAWDZENIA.append((gdzie, zrodlo, wyjscie))
    return zrodlo


# ------------------------------------------------------------------ bloki lekcji
def C(rodzaj, tresc, wynik, wskazowki, rozwiazanie, odpowiedzi=None):
    assert rodzaj in ("prowadzone", "samodzielne"), rodzaj
    assert len(wskazowki) == 3, (tresc[:60], len(wskazowki))
    c = {"rodzaj": rodzaj, "tresc": tresc, "wynik": wynik, "wskazowki": list(wskazowki), "rozwiazanie": rozwiazanie}
    if odpowiedzi:
        c["odpowiedzi"] = odpowiedzi
    return c


def B(komunikat, przyczyna, diagnoza, poprawka):
    return {"komunikat": komunikat, "przyczyna": przyczyna, "diagnoza": diagnoza, "poprawka": poprawka}


def T(p, o, odp, w):
    assert 0 <= odp < len(o), p
    return {"p": p, "o": list(o), "odp": odp, "w": w}


def Q(p, o, odp, w, lekcja):
    q = T(p, o, odp, w)
    q["lekcja"] = lekcja
    return q


WYMAGANE_LEKCJI = ("id", "nazwa", "slowa", "cel", "po_co", "wymagania", "wyjasnienie", "przyklad", "demonstracja", "jak_uruchomic",
                   "cwiczenia", "typowe_bledy", "pulapki", "zadania", "pytania", "podsumowanie", "test", "zrodla")


def L(**l):
    for k in WYMAGANE_LEKCJI:
        assert l.get(k), f"lekcja {l.get('id')}: brak pola {k}"
    assert [c["rodzaj"] for c in l["cwiczenia"]] == ["prowadzone", "samodzielne"], l["id"]
    assert 3 <= len(l["test"]) <= 5, l["id"]
    assert len(l["typowe_bledy"]) >= 2, l["id"]
    assert l["demonstracja"].get("kroki") and l["demonstracja"].get("wynik"), l["id"]
    if l["cel"].startswith("Po tej lekcji "):
        l["cel"] = l["cel"][len("Po tej lekcji "):]           # Mentor poprzedza cel słowami „Po tej lekcji potrafisz:”
        if l["cel"].startswith("potrafisz "):
            l["cel"] = l["cel"][len("potrafisz "):]
    l["pytania"] = [list(p) for p in l["pytania"]]
    l["zrodla"] = [list(z) for z in l["zrodla"]]
    for z in l["zrodla"]:
        assert len(z) == 3 and z[1].startswith("https://"), (l["id"], z)
    return l


# ------------------------------------------------------------------ zadania
def test_z(plik, test, wybor, przyklad=None, podpowiedz=None, szablon=None, stdin=None):
    """Ćwiczenie w Mentorze sprawdzane niezależnym testem z paczki (WERYFIKATORY/<test>). Sumę SHA-256 wpisuje zbuduj.py."""
    c = {"plik": plik, "sprawdzenie": {"rodzaj": "test_zewnetrzny", "plik_testu": f"WERYFIKATORY/{test}", "wybor": wybor, "limit_s": 90}}
    if przyklad:
        c["przyklad"] = przyklad
    if podpowiedz:
        c["podpowiedz"] = podpowiedz
    if szablon:
        c["szablon"] = szablon
    if stdin:
        c["stdin"] = stdin
    return c


def wyjscie_z(plik, teksty, min_linii=1, przyklad=None, podpowiedz=None, szablon=None, stdin=None):
    c = {"plik": plik, "sprawdzenie": {"rodzaj": "wyjscie_zawiera", "tekst": list(teksty), "min_linii": min_linii}}
    if stdin:
        c["sprawdzenie"]["stdin"] = stdin
        c["stdin"] = stdin
    if przyklad:
        c["przyklad"] = przyklad
    if podpowiedz:
        c["podpowiedz"] = podpowiedz
    if szablon:
        c["szablon"] = szablon
    return c


def Z(id, tytul, opis, kroki, sprawdz, problemy, pliki, czas_min, xp=10, cwiczenie=None, rubryka=None):
    assert kroki and sprawdz and problemy, id
    z = {"id": id, "tytul": tytul, "opis": opis, "kroki": list(kroki), "sprawdz": sprawdz, "problemy": list(problemy),
         "pliki": list(pliki), "xp": xp, "czas_min": czas_min}
    if cwiczenie:
        z["cwiczenie"] = cwiczenie
    if rubryka:
        z["rubryka"] = list(rubryka)
    return z


# Ścieżka bez płatnego konta (STANDARD §7.6) — wspólny akapit do zadań z agentem
BEZ_KONTA = ("Bez płatnego konta: otwórz w paczce kursu plik „przyklady/odpowiedzi_agenta/{id}.md” — to zapis tego, co agent wygenerował dla tej "
             "samej specyfikacji, z JEDNYM celowo wstawionym błędem. Przepisz kod do swojego pliku, uruchom testy Mentora, znajdź i popraw błąd — "
             "to dokładnie ta sama umiejętność: czytasz, sprawdzasz i poprawiasz pracę AI.")
