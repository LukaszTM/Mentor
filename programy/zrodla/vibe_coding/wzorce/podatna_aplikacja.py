"""Aplikacja po przeglądzie bezpieczeństwa: escape, parametry SQL, sekret ze zmiennej, bez debug."""
import os
import sqlite3

from flask import Flask, jsonify, request
from markupsafe import escape


def create_app():
    klucz = os.environ.get("FLASK_SECRET_KEY")
    if not klucz:
        raise RuntimeError("Ustaw zmienną środowiskową FLASK_SECRET_KEY")
    app = Flask(__name__)
    app.config["SECRET_KEY"] = klucz
    con = sqlite3.connect(":memory:", check_same_thread=False)
    con.execute("CREATE TABLE goscie (imie TEXT, email TEXT)")
    con.executemany("INSERT INTO goscie VALUES (?, ?)", [("Anna", "anna@pod-lipa.pl"), ("Piotr", "piotr@pod-lipa.pl")])

    @app.route("/powitanie")
    def powitanie():
        imie = request.args.get("imie", "gościu")
        return f"<h1>Witaj {escape(imie)}!</h1>"

    @app.route("/szukaj")
    def szukaj():
        email = request.args.get("email", "")
        wiersze = con.execute("SELECT imie, email FROM goscie WHERE email = ?", (email,)).fetchall()
        return jsonify([{"imie": i, "email": e} for i, e in wiersze])

    return app


if __name__ == "__main__":
    create_app().run()
