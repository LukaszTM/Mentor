# -*- coding: utf-8 -*-
"""Uruchamiany interpreterem środowiska kursu: dla podanych modułów wypisuje JSON {modul: wersja|null} (realny import)."""
import importlib
import json
import sys

wynik = {}
for m in sys.argv[1:]:
    try:
        mod = importlib.import_module(m)
        w = getattr(mod, "__version__", None)
        if w is None:
            try:
                from importlib.metadata import version
                w = version(m)
            except Exception:  # noqa: BLE001
                w = "ok"
        wynik[m] = str(w)
    except Exception:  # noqa: BLE001
        wynik[m] = None
print(json.dumps(wynik))
