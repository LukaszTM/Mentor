"""Aplikacja Flask „Pod Lipą”: kalkulator ceny i wolne pokoje."""
from flask import Flask, jsonify, request

from kalendarz import noce, wolne_pokoje
from kalkulator_pobytu import koszt_pobytu


def create_app(rezerwacje=None):
    app = Flask(__name__)
    rez = list(rezerwacje) if rezerwacje is not None else []

    @app.route("/")
    def start():
        return "<h1>Pod Lipą</h1><p>API: /api/cena?noce=2&osoby=2, /api/wolne?od=2026-12-20&do=2026-12-23</p>"

    @app.route("/api/cena")
    def cena():
        n = request.args.get("noce", type=int)
        o = request.args.get("osoby", type=int)
        if n is None or o is None:
            return jsonify({"blad": "podaj noce i osoby jako liczby całkowite"}), 400
        try:
            return jsonify({"koszt": koszt_pobytu(n, o)})
        except ValueError as e:
            return jsonify({"blad": str(e)}), 400

    @app.route("/api/wolne")
    def wolne():
        od, do = request.args.get("od"), request.args.get("do")
        try:
            noce(od, do)
            pokoje = wolne_pokoje(rez, od, do)
        except (TypeError, ValueError):
            return jsonify({"blad": "podaj od i do jako RRRR-MM-DD, do po od"}), 400
        return jsonify({"od": od, "do": do, "wolne": pokoje})

    return app


if __name__ == "__main__":
    create_app().run()
