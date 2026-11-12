# -*- coding: utf-8 -*-
"""Automatyczne porządkowanie wyjaśnień: nagłówki sekcji z lead-u akapitu, rozbijanie wyliczeń (1)…(n)
i długich łańcuchów „; ” na punkty. Treść się nie zmienia — tylko podział na linie."""
import re

_KONIEC_ZDANIA = re.compile(r"\.\s+[A-ZĄĆĘŁŃÓŚŹŻ]")


def _naglowek(akapit):
    """(naglowek, reszta), gdy akapit zaczyna się krótkim lead-em zakończonym ':' lub ' — '."""
    for sep in (":", " — "):
        i = akapit.find(sep)
        if 3 <= i <= 70 and not _KONIEC_ZDANIA.search(akapit[:i]) and ";" not in akapit[:i]:
            lead = akapit[:i].strip()
            if lead and lead[0].isupper():
                return lead, akapit[i + len(sep):].strip()
    return None, akapit


def _podziel_srednikami(tekst):
    """Dzieli po „; ” poza nawiasami; zwraca listę części (bez zmiany treści)."""
    czesci, poziom, start = [], 0, 0
    for i, ch in enumerate(tekst):
        if ch == "(":
            poziom += 1
        elif ch == ")":
            poziom = max(0, poziom - 1)
        elif ch == ";" and poziom == 0 and tekst[i + 1:i + 2] == " ":
            czesci.append(tekst[start:i].strip())
            start = i + 1
    czesci.append(tekst[start:].strip())
    return [c for c in czesci if c]


def _wyliczenie(a):
    """Rozbija „(1) … (2) …” na punkty; zwraca listę linii albo None."""
    if a.count("(1)") != 1 or "(2)" not in a:
        return None
    przed, *czesci = re.split(r"\s?\((?=\d{1,2}\)|[a-h]\))", a)
    linie = [przed.strip()] if przed.strip() else []
    for cz in czesci:
        m = re.match(r"(\d{1,2}|[a-h])\)\s*(.*)", cz, re.S)
        if m:
            linie.append("- " + m.group(2).strip().rstrip(";").rstrip(",").strip())
    return linie


def uczytelnij(wyjasnienie):
    out = []
    for akapit in wyjasnienie.split("\n"):
        a = akapit.strip()
        if not a:
            continue
        if a.startswith(("## ", "- ", "• ")):
            out.append(a)
            continue
        naglowek, a = _naglowek(a)
        if naglowek:
            out.append("## " + naglowek)
        linie = _wyliczenie(a)
        if linie:
            out.extend(linie)
            continue
        out.extend(_zdania_na_punkty(a))
    return "\n".join(out)


def _zdania(tekst):
    """Dzieli na zdania po „. ” + wielka litera (skróty typu „art. 52” zostają)."""
    zdania, start = [], 0
    for m in _KONIEC_ZDANIA.finditer(tekst):
        zdania.append(tekst[start:m.start() + 1].strip())
        start = m.start() + 1
    zdania.append(tekst[start:].strip())
    return [z for z in zdania if z]


def _zdania_na_punkty(akapit):
    """Zdania z długą listą „; ” zamienia na punkty, pozostałe skleja w akapity."""
    out, bufor = [], []
    for zd in _zdania(akapit):
        czesci = _podziel_srednikami(zd)
        if len(czesci) >= 3 and len(zd) >= 160 and min(len(c) for c in czesci) >= 8:
            if bufor:
                out.append(" ".join(bufor))
                bufor = []
            i = czesci[0].find(": ")
            if 0 < i < 60:
                out.append(czesci[0][:i + 1])
                czesci[0] = czesci[0][i + 2:]
            out.extend("- " + c.rstrip(".") for c in czesci)
        else:
            bufor.append(zd)
    if bufor:
        out.append(" ".join(bufor))
    return out
