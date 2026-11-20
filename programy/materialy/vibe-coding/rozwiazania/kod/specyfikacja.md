# Specyfikacja: czy_telefon

## Cel
Funkcja sprawdzająca numer telefonu gościa w formularzu rezerwacji „Pod Lipą”.

## Wejście
Napis (str).

## Wynik
True albo False.

## Przykłady
- "600700800" → True
- "600 700 800" → True
- "+48 600-700-800" → True
- "48600700800" → False
- "12345" → False
- "" → False

## Przypadki brzegowe
- pusty napis → False
- spacje na brzegach ignorujemy
- inny kierunkowy (+49) → False

## Poza zakresem
- numery zagraniczne
- sprawdzanie, czy numer istnieje

## Gotowe, gdy
- przechodzą testy Mentora i wszystkie przykłady

## Pytania do klienta
- czy przyjmujemy numery zagraniczne?
