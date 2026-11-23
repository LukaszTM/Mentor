"""Kalkulator BMI: wskaźnik masy ciała i kategoria (progi WHO: 18.5, 25, 30)."""

PROG_NIEDOWAGI = 18.5
PROG_NADWAGI = 25
PROG_OTYLOSCI = 30


def oblicz_bmi(waga, wzrost):
    """Zwraca BMI zaokrąglone do 1 miejsca; waga w kg, wzrost w metrach.

    Wartości ≤ 0 albo wzrost > 3 (podany w centymetrach) → ValueError.
    """
    if waga <= 0 or wzrost <= 0:
        raise ValueError("waga i wzrost muszą być większe od zera")
    if wzrost > 3:
        raise ValueError("podaj wzrost w metrach, np. 1.75")
    return round(waga / wzrost ** 2, 1)


def kategoria(bmi):
    """Zwraca kategorię BMI: niedowaga, norma, nadwaga albo otyłość."""
    if bmi < PROG_NIEDOWAGI:
        return "niedowaga"
    if bmi < PROG_NADWAGI:
        return "norma"
    if bmi < PROG_OTYLOSCI:
        return "nadwaga"
    return "otyłość"


if __name__ == "__main__":
    wzrost = float(input("Wzrost w metrach: ").replace(",", "."))
    waga = float(input("Waga w kg: ").replace(",", "."))
    try:
        bmi = oblicz_bmi(waga, wzrost)
    except ValueError as e:
        if wzrost > 3:
            print("Uwaga: wzrost podaj w metrach, nie w centymetrach")
        else:
            print("Podaj wartości większe od zera")
    else:
        print(f"BMI: {bmi:.1f} — {kategoria(bmi)}")
