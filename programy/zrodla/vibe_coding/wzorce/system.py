"""Mini system rezerwacji „Pod Lipą” — projekt końcowy."""
import sqlite3
from datetime import date, timedelta

from flask import Flask, jsonify, request

from cennik import cena_pokoju
from kalendarz import POKOJE, koliduje, noce, wolne_pokoje
from walidacja import czy_email

SCHEMAT = """CREATE TABLE IF NOT EXISTS rezerwacje (
    id INTEGER PRIMARY KEY, gosc TEXT NOT NULL, email TEXT NOT NULL,
    pokoj TEXT NOT NULL, od TEXT NOT NULL, do TEXT NOT NULL, koszt REAL NOT NULL)"""


def koszt(pokoj, od, do):
    """Suma cen pokoju za każdą noc według miesiąca tej nocy."""
    start = date.fromisoformat(od)
    return round(sum(cena_pokoju(pokoj, (start + timedelta(days=i)).month) for i in range(noce(od, do))), 2)


def _waliduj(d):
    if not isinstance(d, dict):
        raise ValueError("oczekiwano danych JSON")
    gosc = str(d.get("gosc") or "").strip()
    if not gosc:
        raise ValueError("podaj imię gościa")
    if not czy_email(str(d.get("email") or "")):
        raise ValueError("nieprawidłowy e-mail")
    if d.get("pokoj") not in POKOJE:
        raise ValueError("nieznany pokój")
    od, do = d.get("od"), d.get("do")
    try:
        noce(od, do)
    except (TypeError, ValueError):
        raise ValueError("podaj od i do jako RRRR-MM-DD, do po od") from None
    return {"gosc": gosc, "email": d["email"].strip(), "pokoj": d["pokoj"], "od": od, "do": do}


def create_app(sciezka_bazy=":memory:"):
    app = Flask(__name__)
    con = sqlite3.connect(sciezka_bazy, check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute(SCHEMAT)

    def wszystkie():
        return [dict(w) for w in con.execute("SELECT id, gosc, pokoj, od, do, koszt FROM rezerwacje ORDER BY id")]

    @app.route("/")
    def start():
        return "<h1>Pod Lipą</h1><p>System rezerwacji — API: /api/rezerwacje, /api/wolne</p>"

    @app.route("/api/rezerwacje", methods=["GET"])
    def lista():
        return jsonify(wszystkie())

    @app.route("/api/rezerwacje", methods=["POST"])
    def dodaj():
        try:
            r = _waliduj(request.get_json(silent=True))
        except ValueError as e:
            return jsonify({"blad": str(e)}), 400
        if any(koliduje(r, x) for x in wszystkie()):
            return jsonify({"blad": "pokój zajęty w tym terminie"}), 409
        k = koszt(r["pokoj"], r["od"], r["do"])
        with con:
            cur = con.execute("INSERT INTO rezerwacje (gosc, email, pokoj, od, do, koszt) VALUES (?, ?, ?, ?, ?, ?)",
                              (r["gosc"], r["email"], r["pokoj"], r["od"], r["do"], k))
        return jsonify({"id": cur.lastrowid, "koszt": k}), 201

    @app.route("/api/rezerwacje/<int:rid>", methods=["DELETE"])
    def usun(rid):
        with con:
            cur = con.execute("DELETE FROM rezerwacje WHERE id = ?", (rid,))
        if cur.rowcount == 0:
            return jsonify({"blad": "nie ma takiej rezerwacji"}), 404
        return "", 204

    @app.route("/api/wolne")
    def wolne():
        od, do = request.args.get("od"), request.args.get("do")
        try:
            noce(od, do)
            pokoje = wolne_pokoje(wszystkie(), od, do)
        except (TypeError, ValueError):
            return jsonify({"blad": "podaj od i do jako RRRR-MM-DD, do po od"}), 400
        return jsonify({"od": od, "do": do, "wolne": pokoje})

    return app
