"""Temperatura z (fikcyjnego) API pogody — klucz ze zmiennej środowiskowej."""
import os

URL = "https://api.pogoda.example/v1/current"


def _requests_klient(url, params, headers):
    import requests
    odp = requests.get(url, params=params, headers=headers, timeout=10)
    odp.raise_for_status()
    return odp.json()


def pobierz_temperature(miasto, klient=None):
    klucz = os.environ.get("POGODA_API_KEY")
    if not klucz:
        raise RuntimeError("Ustaw zmienną środowiskową POGODA_API_KEY")
    miasto = (miasto or "").strip()
    if not miasto:
        raise ValueError("podaj miasto")
    dane = (klient or _requests_klient)(URL, {"miasto": miasto}, {"X-API-Key": klucz})
    try:
        return float(dane["current"]["temp"])
    except (KeyError, TypeError, ValueError):
        raise ValueError("nieprawidłowa odpowiedź API") from None
