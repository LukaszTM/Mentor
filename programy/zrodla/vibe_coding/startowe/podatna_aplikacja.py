# podatna_aplikacja.py — „szybka” aplikacja od agenta (4 dziury bezpieczeństwa)
import sqlite3

from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "tajne123"
    con = sqlite3.connect(":memory:", check_same_thread=False)
    con.execute("CREATE TABLE goscie (imie TEXT, email TEXT)")
    con.executemany("INSERT INTO goscie VALUES (?, ?)", [("Anna", "anna@pod-lipa.pl"), ("Piotr", "piotr@pod-lipa.pl")])

    @app.route("/powitanie")
    def powitanie():
        imie = request.args.get("imie", "gościu")
        return f"<h1>Witaj {imie}!</h1>"

    @app.route("/szukaj")
    def szukaj():
        email = request.args.get("email", "")
        wiersze = con.execute(f"SELECT imie, email FROM goscie WHERE email = '{email}'").fetchall()
        return jsonify([{"imie": i, "email": e} for i, e in wiersze])

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0")
