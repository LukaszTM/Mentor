# -*- coding: utf-8 -*-
"""Lokalny serwer API do testu środowiska: GET /health → {"status": "ok"}. Używa Flaska, jeśli jest w środowisku, inaczej http.server.
Uruchamiany interpreterem kursu: python api_serwer.py <port>. Zatrzymywany przez Mentora po teście."""
import json
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
try:
    from flask import Flask, jsonify

    app = Flask("mentor_test_api")

    @app.get("/health")
    def health():
        return jsonify(status="ok", serwer="flask")

    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/health":
                body = json.dumps({"status": "ok", "serwer": "http.server"}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                self.send_response(404)
                self.end_headers()

        def log_message(self, *a):
            pass

    HTTPServer(("127.0.0.1", port), H).serve_forever()
