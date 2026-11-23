# -*- coding: utf-8 -*-
"""Sklep testowy „Papierowy Kot” — lokalna aplikacja do ćwiczeń z kursu „Python od zera → Junior QA” (tygodnie 5, 8, 9).

Uruchom (terminal Mentora, w tym katalogu):  python app.py   →   http://127.0.0.1:5001
Logowanie: tester / Test123!      API: http://127.0.0.1:5001/api/produkty?kategoria=biuro

UWAGA: sklep ma CELOWO wprowadzone defekty do znalezienia i opisania w raportach błędów (lista jest w rozwiązaniach kursu — nie zaglądaj przed własną sesją testów).
Dane są fikcyjne. Aplikacja działa tylko lokalnie — nie wystawiaj jej do internetu.
"""
import re

from flask import Flask, abort, jsonify, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "sklep-testowy-tylko-lokalnie"

PRODUKTY = [
    (1, "Zeszyt A5 w kratkę", "zeszyty", 4.50, 120), (2, "Zeszyt A4 w linie", "zeszyty", 6.90, 80), (3, "Długopis niebieski", "pisaki", 2.30, 300),
    (4, "Długopis czarny", "pisaki", 2.30, 250), (5, "Ołówek HB", "pisaki", 1.20, 400), (6, "Gumka do mazania", "akcesoria", 1.50, 150),
    (7, "Temperówka", "akcesoria", 2.80, 90), (8, "Blok rysunkowy A4", "papier", 7.50, 60), (9, "Papier ksero A4, 500 ark.", "papier", 24.99, 35),
    (10, "Kredki 12 kolorów", "plastyka", 12.90, 40), (11, "Farby plakatowe 6 kolorów", "plastyka", 18.50, 25), (12, "Klej w sztyfcie", "akcesoria", 3.40, 110),
    (13, "Nożyczki szkolne", "akcesoria", 8.90, 30), (14, "Segregator A4", "biuro", 11.90, 45), (15, "Koszulki na dokumenty 100 szt.", "biuro", 9.99, 70),
    (16, "Zszywacz", "biuro", 19.90, 15), (17, "Zszywki 1000 szt.", "biuro", 3.90, 0), (18, "Kalendarz 2027", "biuro", 29.90, 20),
    (19, "Marker permanentny", "pisaki", 5.60, 85), (20, "Karteczki samoprzylepne", "biuro", 4.20, 140),
]
P = {p[0]: {"id": p[0], "nazwa": p[1], "kategoria": p[2], "cena": p[3], "ilosc": p[4]} for p in PRODUKTY}
ZAMOWIENIA = []

UKLAD = """<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>{{ tytul }} — Papierowy Kot (sklep testowy)</title>
<style>body{font-family:sans-serif;max-width:900px;margin:20px auto;padding:0 16px}.produkt{border:1px solid #ccc;padding:8px;margin:6px 0}
.blad{color:#b00020}.ok{color:#1b5e20}#promocja{background:#fff3cd;padding:8px}</style></head><body>
<nav><a href="/produkty">Produkty</a> · <a id="link-koszyk" href="/koszyk">Koszyk ({{ liczba }})</a> · {% if zalogowany %}<a id="wyloguj" href="/wyloguj">Wyloguj</a>{% else %}<a href="/logowanie">Zaloguj</a>{% endif %}</nav>
<h1>{{ tytul }}</h1>{{ tresc|safe }}</body></html>"""


def strona(tytul, tresc, kod=200):
    return render_template_string(UKLAD, tytul=tytul, tresc=tresc, liczba=sum(session.get("koszyk", {}).values()), zalogowany="login" in session), kod


def zl(x):
    return f"{x:.2f}".replace(".", ",") + " zł"


def wymaga_logowania():
    if "login" not in session:
        return redirect(url_for("logowanie"))
    return None


@app.route("/")
def index():
    return redirect(url_for("produkty"))


@app.route("/logowanie", methods=["GET", "POST"])
def logowanie():
    blad = ""
    if request.method == "POST":
        login = request.form.get("login", "").strip()
        if login == "tester" and request.form.get("haslo", "") == "Test123!":
            session["login"] = login
            session["koszyk"] = {}
            return redirect(url_for("produkty"))
        blad = '<p class="blad" data-test="blad">Błędny login lub hasło</p>'
    return strona("Logowanie", blad + """<form method="post"><label>Login <input id="login" name="login"></label>
<label>Hasło <input id="haslo" name="haslo" type="password"></label> <button type="submit" data-test="zaloguj">Zaloguj</button></form>""", 401 if blad else 200)


@app.route("/wyloguj")
def wyloguj():
    session.clear()
    return redirect(url_for("logowanie"))


@app.route("/produkty")
def produkty():
    if (r := wymaga_logowania()):
        return r
    q = request.args.get("q", "").strip()
    lista = [p for p in P.values() if q in p["nazwa"]] if q else list(P.values())
    wiersze = "".join(f"""<div class="produkt" data-id="{p['id']}"><span class="nazwa">{p['nazwa']}</span> — <span class="cena">{zl(p['cena'])}</span>
<span class="stan">({p['ilosc']} szt.)</span><form method="post" action="/koszyk/dodaj/{p['id']}" style="display:inline">
<input id="ilosc-{p['id']}" name="ilosc" type="number" value="1" min="1"> <button id="dodaj-{p['id']}" data-test="dodaj">Dodaj do koszyka</button></form></div>""" for p in lista)
    return strona("Produkty", f"""<h2 data-test="powitanie">Witaj, {session['login']}!</h2>
<div id="promocja" style="display:none"></div>
<script>setTimeout(function(){{var p=document.getElementById('promocja');p.textContent='Promocja dnia: −10% z kodem KOT10';p.style.display='block';}},1500);</script>
<form method="get"><input id="szukaj" name="q" value="{q}" placeholder="Szukaj produktu"> <button id="szukaj-btn">Szukaj</button></form>
<p data-test="liczba-wynikow">Znaleziono: {len(lista)}</p><div id="produkty">{wiersze or '<p data-test="brak-wynikow">Brak produktów</p>'}</div>""")


@app.route("/koszyk/dodaj/<int:pid>", methods=["POST"])
def dodaj_do_koszyka(pid):
    if (r := wymaga_logowania()):
        return r
    if pid not in P:
        abort(404)
    try:
        n = int(request.form.get("ilosc", "1"))
    except ValueError:
        return strona("Błąd", '<p class="blad" data-test="blad">Ilość musi być liczbą całkowitą</p>', 400)
    if n < 1:
        return strona("Błąd", '<p class="blad" data-test="blad">Ilość musi być większa od zera</p>', 400)
    k = session.get("koszyk", {})
    k[str(pid)] = k.get(str(pid), 0) + n
    session["koszyk"] = k
    return redirect(url_for("koszyk"))


def suma_koszyka():
    suma = 0
    for pid, n in session.get("koszyk", {}).items():
        suma += P[int(pid)]["cena"] * (n if n < 10 else 1)
    for _ in range(session.get("rabaty", 0)):
        suma *= 0.9
    return round(suma, 2)


@app.route("/koszyk", methods=["GET", "POST"])
def koszyk():
    if (r := wymaga_logowania()):
        return r
    komunikat = ""
    if request.method == "POST":
        if request.form.get("kod", "").strip().upper() == "KOT10":
            session["rabaty"] = session.get("rabaty", 0) + 1
            komunikat = '<p class="ok" data-test="rabat-ok">Kod KOT10 przyjęty: −10%</p>'
        else:
            komunikat = '<p class="blad" data-test="blad">Nieprawidłowy kod rabatowy</p>'
    k = session.get("koszyk", {})
    wiersze = "".join(f'<tr class="pozycja"><td>{P[int(pid)]["nazwa"]}</td><td class="ilosc">{n}</td><td>{zl(P[int(pid)]["cena"])}</td></tr>' for pid, n in k.items())
    tresc = (komunikat + (f'<table id="koszyk"><tr><th>Produkt</th><th>Ilość</th><th>Cena</th></tr>{wiersze}</table>' if k else '<p data-test="pusty">Koszyk jest pusty</p>')
             + f'<p data-test="suma">Suma: {zl(suma_koszyka())}</p><form method="post"><input id="kod" name="kod" placeholder="Kod rabatowy"> <button id="zastosuj">Zastosuj</button></form>'
             + ('<p><a id="do-zamowienia" href="/zamowienie">Przejdź do zamówienia</a></p>' if k else ""))
    return strona("Koszyk", tresc)


@app.route("/zamowienie", methods=["GET", "POST"])
def zamowienie():
    if (r := wymaga_logowania()):
        return r
    bledy = []
    if request.method == "POST":
        imie, email, kod = (request.form.get(x, "").strip() for x in ("imie", "email", "kod_pocztowy"))
        if not imie:
            bledy.append("Podaj imię i nazwisko")
        if "@" not in email or "." not in email.split("@")[-1]:
            bledy.append("Podaj poprawny e-mail")
        if not re.fullmatch(r"\d{2}-?\d{3}", kod):
            bledy.append("Kod pocztowy w formacie NN-NNN")
        if not session.get("koszyk"):
            bledy.append("Koszyk jest pusty")
        if not bledy:
            ZAMOWIENIA.append({"login": session["login"], "suma": suma_koszyka(), "kod": kod})
            session["koszyk"], session["rabaty"] = {}, 0
            return strona("Zamówienie przyjęte", f'<p class="ok" data-test="komunikat">Dziękujemy! Zamówienie nr {len(ZAMOWIENIA)} przyjęte.</p>')
    bl = "".join(f'<p class="blad" data-test="blad">{b}</p>' for b in bledy)
    return strona("Zamówienie", bl + """<form method="post"><label>Imię i nazwisko <input id="imie" name="imie"></label><br>
<label>E-mail <input id="email" name="email"></label><br><label>Kod pocztowy <input id="kod_pocztowy" name="kod_pocztowy" placeholder="00-000"></label><br>
<button type="submit" data-test="zamawiam">Zamawiam</button></form>""", 400 if bledy else 200)


@app.route("/api/produkty")
def api_produkty():
    kat = request.args.get("kategoria")
    lista = [p for p in P.values() if not kat or p["kategoria"] == kat]
    return jsonify(lista)


@app.route("/api/produkty/<int:pid>")
def api_produkt(pid):
    if pid not in P:
        return jsonify({"blad": "nie ma takiego produktu"}), 404
    return jsonify(P[pid])


if __name__ == "__main__":
    print("Sklep testowy: http://127.0.0.1:5001  (login: tester / Test123!)  — Ctrl+C kończy")
    app.run(host="127.0.0.1", port=5001, debug=False)
