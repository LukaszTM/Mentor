# Raport — checklista publikacyjna (STANDARD_KURSOW.md §11), kurs „Python od zera → Junior QA” 3.0

| punkt | stan | dowód |
|---|---|---|
| Uczeń wie, co umie po kursie i ile czasu nauka zajmie | TAK | START_TUTAJ.md, lekcja „Start”, czas tygodni policzony z treści (≤ 9 h) |
| Każda lekcja wyjaśnia, pokazuje działający przykład i omawia go krok po kroku | TAK | 39 lekcji; kod demonstracji uruchamiany w testach (testy/test_kurs_python.py) |
| Żadne zadanie nie wymaga niepokazanych umiejętności | TAK | kolejność lekcji → zadania tygodnia; wymagania lekcji |
| Pliki startowe, dane, przykłady i rozwiązania w paczce | TAK | przyklady/, dane/, projekty/, rozwiazania/kod/ |
| Narzędzia legalnie / z oficjalnego źródła | TAK | Python i biblioteki — Mentor z locka SHA-256; Git — git-scm.com; Selenium Manager — oficjalny |
| Instalacja według instrukcji, także przy typowym błędzie | TAK | lekcja „Narzędzia”, typowe błędy, pomoc/FAQ.md |
| Każde zadanie: oczekiwany wynik, sprawdzenie, podpowiedzi | TAK | „Gotowe, gdy”, weryfikatory, problemy, 3 podpowiedzi w ćwiczeniach |
| Quizy i powtórki z wyjaśnieniami; postęp = praca | TAK | 72 pytania z wyjaśnieniem; 60 zadań sprawdzanych testami |
| Przykłady działają w deklarowanych wersjach | TAK | testy CI (Windows, Python 3.12, lock) |
| JSON przechodzi walidację i import | TAK | program.waliduj, sprawdz_paczki.py, test end-to-end |
| ZIP bez sekretów, pirackich plików, danych osobowych | TAK | test_brak_odniesien_osobistych, dane fikcyjne |
| Osoba testująca (nie autor) zaczyna bez dopytywania | DO SPRAWDZENIA | wymaga testu z osobą spoza projektu |
