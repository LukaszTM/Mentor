# Plan projektu końcowego

## Cel
Mini system rezerwacji „Pod Lipą”.

## Użytkownicy
- gość, właścicielka

## Funkcje
- POST /api/rezerwacje z walidacją
- 409 dla kolizji
- GET /api/rezerwacje bez e-maili
- GET /api/wolne
- DELETE /api/rezerwacje/<id>

## Kamienie milowe
- K1 baza i zapis
- K2 kolizje i lista
- K3 wolne i usuwanie
- K4 jakość i wydanie

## Ryzyka
- agent kopiuje moduły → zasada importu w AGENTS.md
- limit planu → praca nad testami bez agenta
- trudne daty → testy brzegowe najpierw

## Gotowe, gdy
- testy Mentora i moje zielone
- tag v1.0.0
