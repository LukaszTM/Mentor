import requests


def pobierz_produkty(adres, timeout=10):
    """Lista produktów z API (JSON). Kod ≠ 200 albo brak połączenia → RuntimeError z opisem."""
    try:
        odp = requests.get(adres, timeout=timeout)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"brak połączenia z {adres}: {type(e).__name__}") from e
    if odp.status_code != 200:
        raise RuntimeError(f"serwer odpowiedział kodem {odp.status_code}")
    return odp.json()


def tanie(produkty, limit):
    """Nazwy produktów z ceną poniżej limitu, rosnąco po cenie."""
    return [p["nazwa"] for p in sorted(produkty, key=lambda p: p["cena"]) if p["cena"] < limit]


if __name__ == "__main__":
    try:
        lista = pobierz_produkty("http://127.0.0.1:5001/api/produkty")
    except RuntimeError as e:
        print("Nie udało się pobrać produktów:", e)
    else:
        for p in lista[:3]:
            print(p["id"], p["nazwa"], p["cena"])
        print("Poniżej 5 zł:", tanie(lista, 5))
