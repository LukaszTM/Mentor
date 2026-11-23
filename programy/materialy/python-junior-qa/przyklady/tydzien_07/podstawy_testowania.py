def czy_ilosc_poprawna(ilosc):
    """Wymaganie: ilość w zamówieniu to liczba całkowita od 1 do 50."""
    return isinstance(ilosc, int) and 1 <= ilosc <= 50


def czy_ilosc_z_defektem(ilosc):
    return isinstance(ilosc, int) and 1 <= ilosc < 50


PRZYPADKI = [(0, False), (1, True), (25, True), (50, True), (51, False), (-5, False), ("10", False)]
for funkcja in (czy_ilosc_poprawna, czy_ilosc_z_defektem):
    nieudane = [d for d, oczekiwane in PRZYPADKI if funkcja(d) != oczekiwane]
    print(funkcja.__name__, "— nieudane przypadki:", nieudane)
