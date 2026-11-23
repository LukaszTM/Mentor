"""Magazyn — interfejs webowy (Flask). Uruchom: python app.py → http://127.0.0.1:5000"""
import os
from datetime import date

from flask import Flask, abort, redirect, render_template, request, url_for

import baza
import magazyn


def create_app(sciezka_bazy="magazyn.db"):
    app = Flask(__name__)
    app.config["BAZA"] = str(sciezka_bazy)

    def polaczenie():
        return baza.utworz_baze(app.config["BAZA"])

    @app.template_filter("zl")
    def zl(x):
        return f"{x:.2f}".replace(".", ",")

    @app.route("/")
    def index():
        return render_template("index.html", produkty=baza.pobierz_produkty(polaczenie()))

    @app.route("/dodaj", methods=["GET", "POST"])
    def dodaj():
        if request.method == "GET":
            return render_template("dodaj.html", blad=None, dane={})
        dane = {k: request.form.get(k, "").strip() for k in ("nazwa", "kategoria", "cena", "ilosc")}
        blad = None
        try:
            cena = float(dane["cena"].replace(",", "."))
        except ValueError:
            cena = None
        if not dane["nazwa"]:
            blad = "Podaj nazwę produktu"
        elif not dane["kategoria"]:
            blad = "Podaj kategorię"
        elif cena is None or cena < 0:
            blad = "Cena musi być liczbą nieujemną"
        elif not dane["ilosc"].isdigit():
            blad = "Ilość musi być liczbą całkowitą ≥ 0"
        if blad is None:
            con = polaczenie()
            if any(p["nazwa"].lower() == dane["nazwa"].lower() for p in baza.pobierz_produkty(con)):
                blad = "Produkt o tej nazwie już istnieje"
            else:
                baza.dodaj_produkt(con, dane["nazwa"], dane["kategoria"], cena, int(dane["ilosc"]))
                return redirect(url_for("index"))
        return render_template("dodaj.html", blad=blad, dane=dane), 400

    @app.route("/produkt/<int:pid>", methods=["GET", "POST"])
    def produkt(pid):
        con = polaczenie()
        p = baza.pobierz_produkt(con, pid)
        if p is None:
            abort(404)
        blad = None
        if request.method == "POST":
            try:
                n = int(request.form.get("ilosc", ""))
                f = magazyn.przyjecie if request.form.get("typ") == "przyjecie" else magazyn.wydanie
                f(con, pid, n, date.today().isoformat())
                return redirect(url_for("produkt", pid=pid))
            except ValueError as e:
                blad = str(e)
        return render_template("produkt.html", p=baza.pobierz_produkt(con, pid), historia=magazyn.historia(con, pid), blad=blad), 400 if blad else 200

    return app


if __name__ == "__main__":
    create_app().run(port=5000, debug=os.environ.get("FLASK_DEBUG") == "1")
