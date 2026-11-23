import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

PRODUKTY = [{"id": 1, "nazwa": "Zeszyt A5", "cena": 4.5, "kategoria": "zeszyty"},
            {"id": 14, "nazwa": "Segregator A4", "cena": 11.9, "kategoria": "biuro"}]


class Api(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/produkty"):
            tresc, kod = json.dumps(PRODUKTY).encode(), 200
        else:
            tresc, kod = b'{"blad": "nie ma"}', 404
        self.send_response(kod)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(tresc)

    def log_message(self, *args):
        pass


serwer = HTTPServer(("127.0.0.1", 0), Api)
threading.Thread(target=serwer.serve_forever, daemon=True).start()
adres = f"http://127.0.0.1:{serwer.server_port}"

odp = requests.get(adres + "/api/produkty", timeout=5)
print(odp.status_code, odp.headers["Content-Type"])
for p in odp.json():
    print(p["id"], p["nazwa"], p["cena"])
print("Brak zasobu:", requests.get(adres + "/api/koszyk", timeout=5).status_code)
serwer.shutdown()
serwer.server_close()
try:
    requests.get(adres + "/api/produkty", timeout=3)
except requests.exceptions.RequestException:
    print("Serwer niedostępny — sprawdź, czy działa i czy adres jest dobry")
