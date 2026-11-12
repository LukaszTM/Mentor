# Rozwiązanie — ćwiczenie 1 (prowadzone) — Jawność wynagrodzeń: co obowiązuje (2025), co nadchodzi (dyrektywa 2023/970), audyt luki płacowej
Plik startowy: `cwiczenia/tydzien_11/jawnosc_wynagrodzen_1.md`

Zasada: najpierw własna próba. Podpowiedzi odkrywaj po kolei — rozwiązanie dopiero na końcu.

## Podpowiedź 1 — pytanie naprowadzające
Jak liczysz medianę przy parzystej liczbie osób? (Średnia z dwóch środkowych.)

## Podpowiedź 2 — gdzie szukać
Demonstracja, kroki 1–4; dane w pliku mają kolumny: płeć | zasadnicze | staż | nocne (zł/mies.) | premia (średnia 12 mies.).

## Podpowiedź 3 — częściowy przykład
Szkic: suma M / 8, suma K / 10; sortuj i weź środek; luka = (śr. M − śr. K)/śr. M; korekta: różnica stażu × 2% × ~5 000; różnica nocnych…

## Pełne rozwiązanie
```
Dane (z pliku): M (8): zasadnicze+dodatki: 5 400, 5 300, 5 250, 5 200, 5 200, 5 150, 5 200, 5 140 → suma 41 840 → średnia 5 230; mediana (5 200 + 5 200)/2 = 5 200. K (10): 5 150, 5 100, 5 050, 5 000, 5 000, 5 000, 4 950, 4 950, 4 950, 4 950 → suma 50 100 → średnia 5 010; mediana (5 000 + 5 000)/2 = 5 000.
Luka: średnia (5 230 − 5 010)/5 230 = 4,2%; mediana (5 200 − 5 000)/5 200 = 3,8% — poniżej progu 5% dyrektywy, ale art. 18³ᶜ KP i tak wymaga równej płacy za jednakową pracę.
Rozkład: staż — M średnio 4,5 roku, K 3,0 → 1,5 roku × 2% × ~5 000 = ok. 150 zł; nocne — M średnio 110 zł/mies., K 50 → 60 zł. Po odjęciu: M 5 230 − 150 − 110 = 4 970 vs K 5 010 − 0 − 50 = 4 960 → różnica 10 zł (0,2%) — brak luki w zasadniczym.
Wniosek: różnica wynika z obiektywnych, neutralnych kryteriów (staż, praca nocna) stosowanych jednakowo; udokumentuj (arkusz + uzasadnienie), wpisz kategorię do siatki płac, monitoruj co roku; wyrównania nie są potrzebne. Uwaga na „nocne”: jeśli kobiety nie pracują w nocy, bo grafik je pomija — kryterium przestaje być neutralne (pośrednia dyskryminacja) → sprawdź rozkład zmian.
```

## Oczekiwany wynik
M: średnia 5 230, mediana 5 200; K: średnia 5 010, mediana 5 000; luka 4,2% (średnia) / 3,8% (mediana) — poniżej 5%, ale: po korekcie o staż (M +1,5 roku → ok. 150 zł) i nocne (M +60 zł) zasadnicze M 5 020 vs K 4 990 → 0,6% — w granicach błędu; działanie: siatka i monitoring, bez wyrównań; dokumentacja uzasadnienia.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co by się zmieniło, gdyby zmienił się jeden fakt (etat, staż, data, kwota)?
