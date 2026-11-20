# Rozwiązanie — ćwiczenie 1 (prowadzone) — API i klucze: pobierasz dane z internetu i nie zdradzasz sekretów

Najpierw własna próba. Podpowiedzi odkrywaj po kolei.

## Podpowiedź 1
setx zapisuje trwale dla przyszłych okien.

## Podpowiedź 2
Bieżące okno: polecenie set.

## Podpowiedź 3
Dokumentacja requests zaleca zawsze podawać timeout.

## Rozwiązanie
setx działa dopiero w nowych oknach; w bieżącym: set POGODA_API_KEY=k123; requests bez timeout czeka bez limitu.

## Oczekiwany wynik
(1) setx działa w nowych oknach; (2) set POGODA_API_KEY=k123; (3) brak — bez timeout żądanie może czekać bez końca.

## Wyjaśnij własnymi słowami
Dlaczego to działa? Co się zmieni, gdy zmienisz jedną daną (granicę, typ, plik)?
