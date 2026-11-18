# -*- coding: utf-8 -*-
"""
Automatyczne sprawdzanie odpowiedzi: ćwiczenia w lekcjach i formularze w Warsztacie.

Uczeń wpisuje wynik (kwotę, liczbę, datę, kod, wybór), Mentor porównuje go z kluczem i pokazuje ✔/✘ przy KAŻDYM polu —
bez ujawniania poprawnej wartości. Przy typowej pomyłce (pole „bledy” w kluczu) podpowiada, skąd się wzięła.

Format pola klucza (lista „odpowiedzi” w ćwiczeniu albo „pola” w formularzu — patrz programy/FORMAT.md):
  {"id": "netto", "etykieta": "Netto do wypłaty (zł)", "typ": "kwota", "wartosc": 3605.85, "tol": 0.01,
   "bledy": [{"wartosc": 3501.73, "komunikat": "to netto z PPK — tu PPK nie ma"}]}
  typ: "kwota" (liczba z groszami, tolerancja domyślna 0,01), "liczba" (dokładnie albo z „tol”), "data" (RRRR-MM-DD),
       "tekst" (kod, numer artykułu, krótkie słowo — porównanie bez wielkości liter, spacji i znaków przestankowych;
                „wartosc” może być listą dopuszczalnych zapisów; „zawiera”: lista fragmentów, które muszą wystąpić),
       "wybor" (jedna z „opcje”).
Moduł nie importuje tkintera — da się go testować bez okna.
"""

import datetime as dt
import re
import unicodedata

TYPY = ("kwota", "liczba", "data", "tekst", "wybor")
_MIESIACE = {"stycznia": 1, "lutego": 2, "marca": 3, "kwietnia": 4, "maja": 5, "czerwca": 6, "lipca": 7, "sierpnia": 8,
             "września": 9, "wrzesnia": 9, "października": 10, "pazdziernika": 10, "listopada": 11, "grudnia": 12}
_JEDNOSTKI = r"(zł|zl|pln|%|proc\.?|h|godz\.?|godzin[ay]?|dni|dzień|dnia|tyg\.?|tygodni[e]?|mies\.?|miesi[ąa]c[ae]?|miesięcy|lat[a]?|rok|osób|osoby|szt\.?|eur|km|pkt)"


# ============================================================ odczyt wpisu ucznia
def _warianty_liczby(tekst):
    """Możliwe odczyty wpisu jako liczby. „3 605,85 zł” → [3605.85]; „3.605” → [3.605, 3605.0] (kropka bywa separatorem tysięcy)."""
    if isinstance(tekst, bool):
        return []
    if isinstance(tekst, (int, float)):
        return [float(tekst)]
    s = str(tekst or "").strip().lower()
    for a, b in ((" ", " "), (" ", " "), ("−", "-"), ("–", "-"), ("—", "-")):
        s = s.replace(a, b)
    s = re.sub(r"\s*" + _JEDNOSTKI + r"\s*$", "", s).strip()
    s = s.replace(" ", "").replace("'", "")
    if not s:
        return []
    kandydaci = []
    if "," in s:
        kandydaci.append(s.replace(".", "").replace(",", "."))
    elif s.count(".") > 1:
        kandydaci.append(s.replace(".", ""))
    else:
        kandydaci.append(s)
        if re.fullmatch(r"-?\d{1,3}\.\d{3}", s):
            kandydaci.append(s.replace(".", ""))
    wynik = []
    for k in kandydaci:
        if re.fullmatch(r"-?\d+(\.\d+)?", k):
            wynik.append(float(k))
    return wynik


def liczba(tekst):
    """Pierwszy odczyt wpisu jako liczby albo None."""
    w = _warianty_liczby(tekst)
    return w[0] if w else None


def data(tekst, rok=None):
    """„2027-02-28”, „28.02.2027”, „28.2.27”, „28/02/2027”, „28 lutego 2027”, a z rokiem domyślnym także „28.02” i „28 lutego”."""
    if isinstance(tekst, dt.datetime):
        return tekst.date()
    if isinstance(tekst, dt.date):
        return tekst
    s = str(tekst or "").strip().lower()
    s = re.sub(r"\s*(r\.|roku|r)\s*$", "", s).strip().rstrip(".")
    if not s:
        return None
    m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if m:
        r, mm, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = re.fullmatch(r"(\d{1,2})[.\-/ ](\d{1,2})(?:[.\-/ ](\d{2}|\d{4}))?", s)
        if m:
            d, mm = int(m.group(1)), int(m.group(2))
            r = m.group(3)
        else:
            m = re.fullmatch(r"(\d{1,2})\s+([a-ząćęłńóśźż]+)(?:\s+(\d{4}))?", s)
            if not m or m.group(2) not in _MIESIACE:
                return None
            d, mm, r = int(m.group(1)), _MIESIACE[m.group(2)], m.group(3)
        if r is None:
            if rok is None:
                return None
            r = rok
        r = int(r)
        if r < 100:
            r += 2000
    try:
        return dt.date(r, mm, d)
    except ValueError:
        return None


def tekst_norm(s):
    """Porównywalna postać krótkiego tekstu/kodu: bez wielkości liter, ogonków, spacji i znaków przestankowych („01 10 00” = „011000”)."""
    s = unicodedata.normalize("NFKD", str(s if s is not None else "")).casefold().replace("ł", "l")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s.,;:\-–—_/\\()\[\]\"„”'’§]+", "", s)


# ============================================================ sprawdzanie
def _jako_date(w):
    return w if isinstance(w, dt.date) else data(w)


def sprawdz_pole(pole, wpis):
    """(ok, komunikat). ok: True — dobrze, False — źle, None — pole puste. Komunikat nigdy nie zawiera poprawnej wartości."""
    typ = pole.get("typ", "kwota")
    surowy = "" if wpis is None else str(wpis).strip()
    if not surowy:
        return None, "puste"
    if typ in ("kwota", "liczba"):
        kandydaci = _warianty_liczby(surowy)
        if not kandydaci:
            return False, "to nie wygląda na liczbę — wpisz np. 1 234,56"
        cel = float(pole["wartosc"])
        tol = float(pole.get("tol", 0.01 if typ == "kwota" else 0.0)) + 1e-9
        if any(abs(k - cel) <= tol for k in kandydaci):
            return True, "dobrze"
        k = kandydaci[0]
        for b in pole.get("bledy") or []:
            if abs(k - float(b["wartosc"])) <= max(tol, 0.01) + 1e-9:
                return False, b.get("komunikat", "typowa pomyłka")
        if abs(k + cel) <= tol and cel != 0:
            return False, "wartość się zgadza, znak nie — sprawdź, czy to dopłata, czy zwrot"
        if typ == "kwota" and abs(k - cel) <= 1.0:
            return False, "blisko — różnica poniżej 1 zł: sprawdź zaokrąglenia (grosze przy składkach, pełne złote przy podstawie i zaliczce PIT)"
        if cel and abs(k - cel) / abs(cel) <= 0.02:
            return False, "blisko — różnica do 2%: prześledź jeszcze raz każdy krok rachunku"
        return False, "nie zgadza się"
    if typ == "data":
        cel = _jako_date(pole["wartosc"])
        d = data(surowy, rok=cel.year if cel else None)
        if d is None:
            return False, "to nie wygląda na datę — wpisz np. 28.02.2027 albo 2027-02-28"
        if d == cel:
            return True, "dobrze"
        for b in pole.get("bledy") or []:
            if _jako_date(b["wartosc"]) == d:
                return False, b.get("komunikat", "typowa pomyłka")
        roznica = (d - cel).days
        if d.weekday() >= 5 and 0 < -roznica <= 2:
            return False, "ten dzień to sobota lub niedziela — sprawdź regułę przesunięcia terminu"
        if abs(roznica) == 1:
            return False, "różnica jednego dnia — sprawdź, czy termin liczysz od właściwego dnia (dzień zdarzenia czy następny)"
        if d.day == cel.day and d.month == cel.month:
            return False, "dzień i miesiąc się zgadzają, rok nie"
        return False, "nie zgadza się"
    if typ == "wybor":
        if tekst_norm(surowy) == tekst_norm(pole["wartosc"]):
            return True, "dobrze"
        for b in pole.get("bledy") or []:
            if tekst_norm(b["wartosc"]) == tekst_norm(surowy):
                return False, b.get("komunikat", "typowa pomyłka")
        return False, "nie zgadza się"
    # tekst
    n = tekst_norm(surowy)
    wzorce = pole.get("wartosc")
    wzorce = wzorce if isinstance(wzorce, (list, tuple)) else ([] if wzorce in (None, "") else [wzorce])
    if any(tekst_norm(w) == n for w in wzorce):
        return True, "dobrze"
    fragmenty = pole.get("zawiera") or []
    if fragmenty and all(tekst_norm(f) in n for f in fragmenty):
        return True, "dobrze"
    for b in pole.get("bledy") or []:
        if tekst_norm(b["wartosc"]) == n:
            return False, b.get("komunikat", "typowa pomyłka")
    return False, "nie zgadza się"


def sprawdz(pola, wpisy):
    """Sprawdza wszystkie pola. wpisy: {id: tekst}. Zwraca {"wyniki": [{"id","ok","info"}], "ok": n, "max": m, "puste": p, "komplet": bool}."""
    wyniki, dobre, puste = [], 0, 0
    for p in pola:
        ok, info = sprawdz_pole(p, (wpisy or {}).get(p["id"]))
        wyniki.append({"id": p["id"], "ok": ok, "info": info})
        dobre += ok is True
        puste += ok is None
    return {"wyniki": wyniki, "ok": dobre, "max": len(pola), "puste": puste, "komplet": dobre == len(pola) and bool(pola)}


def poprawna(pole):
    """Poprawna wartość do pokazania PO próbach (przycisk „Pokaż poprawne wartości”)."""
    typ, w = pole.get("typ", "kwota"), pole.get("wartosc")
    if typ == "kwota":
        return f"{float(w):,.2f}".replace(",", " ").replace(".", ",")
    if typ == "liczba":
        f = float(w)
        return str(int(f)) if f == int(f) else str(f).replace(".", ",")
    if typ == "data":
        d = _jako_date(w)
        return d.strftime("%d.%m.%Y") if d else str(w)
    if isinstance(w, (list, tuple)):
        return str(w[0]) if w else " + ".join(pole.get("zawiera") or [])
    if w in (None, ""):
        return " + ".join(pole.get("zawiera") or [])
    return str(w)


# ============================================================ walidacja klucza (program.waliduj, testy, budowanie kursu)
def waliduj_pola(pola, gdzie=""):
    """Lista błędów struktury klucza odpowiedzi (pusta = OK)."""
    bledy = []
    if not isinstance(pola, list) or not pola:
        return [f"{gdzie}: „odpowiedzi” musi być niepustą listą pól."]
    ids = set()
    for i, p in enumerate(pola, 1):
        g = f"{gdzie}: pole {i}"
        if not isinstance(p, dict) or not p.get("id") or not p.get("etykieta"):
            bledy.append(f"{g} — brak „id” lub „etykieta”.")
            continue
        if p["id"] in ids:
            bledy.append(f"{g} — powtórzone id „{p['id']}”.")
        ids.add(p["id"])
        typ = p.get("typ", "kwota")
        if typ not in TYPY:
            bledy.append(f"{g} — nieznany typ „{typ}”.")
            continue
        w = p.get("wartosc")
        if typ in ("kwota", "liczba"):
            if isinstance(w, bool) or not isinstance(w, (int, float)):
                bledy.append(f"{g} — „wartosc” musi być liczbą.")
        elif typ == "data":
            if _jako_date(w) is None:
                bledy.append(f"{g} — „wartosc” musi być datą RRRR-MM-DD.")
        elif typ == "wybor":
            opcje = p.get("opcje")
            if not isinstance(opcje, list) or len(opcje) < 2 or w not in opcje:
                bledy.append(f"{g} — „opcje” (min. 2) muszą zawierać „wartosc”.")
        else:
            if w in (None, "", []) and not p.get("zawiera"):
                bledy.append(f"{g} — tekst wymaga „wartosc” albo „zawiera”.")
        for b in p.get("bledy") or []:
            if not isinstance(b, dict) or "wartosc" not in b or not b.get("komunikat"):
                bledy.append(f"{g} — wpis „bledy” wymaga „wartosc” i „komunikat”.")
    return bledy
