# -*- coding: utf-8 -*-
"""Prawdziwe żądanie HTTP do lokalnego API z biblioteką kursu: python api_klient.py <url> requests|urllib"""
import json
import sys

url, klient = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "urllib")
if klient == "requests":
    import requests

    r = requests.get(url, timeout=10)
    r.raise_for_status()
    d = r.json()
else:
    import urllib.request

    with urllib.request.urlopen(url, timeout=10) as r:
        d = json.loads(r.read().decode("utf-8"))
assert d.get("status") == "ok", d
print(json.dumps({"klient": klient, "odpowiedz": d}))
