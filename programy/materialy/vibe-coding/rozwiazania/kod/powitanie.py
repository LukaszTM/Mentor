"""Powitanie gościa zależne od godziny."""


def powitanie(imie, godzina):
    imie = (imie or "").strip()
    if not imie:
        raise ValueError("imię nie może być puste")
    if not 0 <= godzina <= 23:
        raise ValueError("godzina musi być w zakresie 0–23")
    imie = imie[0].upper() + imie[1:]
    if 5 <= godzina < 18:
        return f"Dzień dobry, {imie}!"
    return f"Dobry wieczór, {imie}!"


if __name__ == "__main__":
    print(powitanie("anna", 9))
