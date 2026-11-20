# Rozmowa rekrutacyjna i zadanie praktyczne z AI
Tydzień 14 · lekcja 45 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** odpowiadasz na 10 typowych pytań o pracę z AI i projekty metodą STAR, wykonujesz zadanie praktyczne z głośnym myśleniem i zadajesz rekruterowi pytania o zasady używania AI w firmie.

**Po co mi to?** Na rozmowie sprawdza się, czy rozumiesz kod, którego nie napisałeś sam, i czy można Ci zaufać z agentem w firmowym repozytorium.

## Czego potrzebujesz
- Lekcja „Portfolio”.
- Projekt końcowy w toku (do opowiadania).

## 1 · Wyjaśnienie od podstaw
### Metoda STAR
Odpowiedź na pytanie „opowiedz o sytuacji, gdy…”: Sytuacja (kontekst), Zadanie (co było do zrobienia), Akcja (co TY zrobiłeś), Rezultat (wynik, najlepiej liczbowy). 1–2 minuty.
Przykład: „S: agent oddał raport, który pomijał wiersze z CSV. Z: raport miał liczyć wszystkie 40 rezerwacji. A: porównałem liczbę wierszy, znalazłem except: continue, kazałem zgłaszać zły wiersz z numerem, dopisałem test. R: raport liczy 40/40, błąd nie wróci (test regresji).”
### 10 pytań, które padną (przygotuj odpowiedzi)
| pytanie | czego szukają |
|---|---|
| Jak sprawdzasz kod od AI? | proces: testy, przegląd diffu, lista bezpieczeństwa |
| Opowiedz o błędzie agenta, który złapałeś | STAR, konkret |
| Kiedy NIE używasz AI? | dane wrażliwe, decyzje bez weryfikacji, gdy szybciej samemu |
| Jak chronisz sekrety? | zmienne środowiskowe, .gitignore, deny, unieważnienie po wycieku |
| Wyjaśnij ten fragment kodu | czytanie kodu — ćwiczone od tygodnia 1 |
| Co to jest test i po co mutanty? | rozumienie testów |
| Jak dzielisz duże zadanie? | małe kroki, plan, commity |
| Co robisz, gdy agent się zapętla? | diagnoza, reguła trzech, nowa sesja |
| Jak pracujesz z Gitem w zespole? | gałąź, PR, przegląd, CI |
| Czego się teraz uczysz? | konkretny plan rozwoju |
### Zadanie praktyczne
Bywa: „napraw błąd w tym repo” albo „dodaj funkcję” — czasem z AI, czasem bez. Zasady: najpierw przeczytaj i zapytaj o niejasności, mów na głos, co robisz i dlaczego, uruchom testy przed i po, pokaż diff i wyjaśnij każdą linię. Jeśli wolno używać AI — pokaż proces (plan, prośba z kryteriami, przegląd), nie tylko wynik. Jeśli nie wolno — Twoje czytanie kodu i traceback wystarczą na proste zadania.
### Twoje pytania do firmy
- Jakich narzędzi AI używacie i jakie są zasady (dane, repozytoria, zgody)?
- Jak wygląda przegląd kodu i CI?
- Jak wygląda wdrożenie nowej osoby (onboarding), kto będzie mentorem?
- Po czym poznam po 3 miesiącach, że dobrze mi idzie?
### Uczciwość
Nie przypisuj sobie wiedzy, której nie masz. „Tego jeszcze nie robiłem, ale sprawdziłbym to tak: …” jest lepsze niż zgadywanie. Rekruterzy szybko rozpoznają wyuczone frazy bez zrozumienia.

## 2 · Demonstracja — krok po kroku
**Symulacja: 20 minut zadania praktycznego**

```
Pytanie: „Jak sprawdzasz kod od AI?”

Odpowiedź (45 s): „Zaczynam od specyfikacji z przykładami — z nich piszę testy, zanim agent napisze kod. Agent pracuje w trybie planu, małymi krokami. Po każdym kroku czytam diff według listy: zakres, testy, zależności, sekrety, ukryte błędy, SQL i HTML. Testy uruchamiam lokalnie i w CI. Na przykład w projekcie rezerwacji wyłapałem w ten sposób f-string w zapytaniu SQL — dopisałem test z „x' OR '1'='1” i poprawkę na parametry.”
```

1. Zadanie: „W repo jest błąd: /api/wolne zwraca 500 dla braku parametru. Napraw.” Czytasz README i AGENTS.md, uruchamiasz testy (wszystkie zielone — brak testu na ten przypadek).
2. Mówisz na głos: „Najpierw odtworzę błąd i napiszę test, który go pokazuje”. Test czerwony — 500.
3. Traceback: TypeError z fromisoformat(None). Hipoteza: trasa łapie tylko ValueError. Poprawka jednej linii (TypeError, ValueError).
4. Testy zielone. Pokazujesz diff (2 linie + test) i mówisz, dlaczego nie zmieniłeś niczego innego.
5. Pytanie rekrutera: „Użyłbyś AI?” — „Tak, do diagnozy lub poprawki, ale test i przegląd zrobiłbym tak samo”.

✔ **Oczekiwany wynik:** Rozwiązanie z testem regresji, minimalny diff i jasne wyjaśnienie procesu — dokładnie to, co ocenia rekruter.

## 3 · Jak to uruchomić
1. Zadanie tygodnia: odpowiedzi na 10 pytań w odpowiedzi_rekrutacja.md + nagranie lub próba z drugą osobą.
2. Asystent Mentora może zadawać pytania jak rekruter.

## W praktyce
- Każdy projekt: 1 historia STAR w notatkach.
- Raz w tygodniu: wyjaśnij na głos jeden plik swojego projektu.

## 4 · Ćwiczenie prowadzone
Przypisz części odpowiedzi do STAR: (1) „raport pomijał wiersze z CSV”, (2) „miał liczyć wszystkie 40 rezerwacji”, (3) „znalazłem except: continue i dopisałem test”, (4) „teraz liczy 40/40”. Opcje: S, T, A, R. Czas: 15 minut.

📄 `cwiczenia/tydzien_14/rozmowa_rekrutacyjna_1.md` · rozwiązanie: `rozwiazania/tydzien_14/rozmowa_rekrutacyjna_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Na zadaniu praktycznym: uporządkuj kroki — A) uruchom testy przed zmianą, B) przeczytaj README i zapytaj o niejasności, C) pokaż diff i wyjaśnij, D) napisz test odtwarzający błąd, E) popraw przyczynę. Ciąg liter. Czy „nie wiem, sprawdziłbym to tak…” to dobra odpowiedź, gdy czegoś nie znasz (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_14/rozmowa_rekrutacyjna_2.md` · rozwiązanie: `rozwiazania/tydzien_14/rozmowa_rekrutacyjna_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Na prośbę „wyjaśnij ten kod” — cisza.**
  - Przyczyna: Kod w portfolio pisał agent, a nie był czytany.
  - Jak sprawdzić: Czy umiesz opisać każdą funkcję swojego projektu?
  - Poprawka: Przed rozmową: przejdź swój projekt plik po pliku i opowiedz go na głos.
- ✘ **Odpowiedzi ogólne („zawsze testuję”).**
  - Przyczyna: Brak przykładów.
  - Jak sprawdzić: Czy każda odpowiedź ma konkret z projektu?
  - Poprawka: Przygotuj 3 historie STAR z kursu i projektu końcowego.

## Pułapki
- Nie używaj AI potajemnie na rozmowie, jeśli zasady tego zabraniają — to dyskwalifikuje.
- Nie mów źle o poprzednich pracodawcach ani narzędziach — mów, czego się nauczyłeś.

## Dodatkowe zadania
1. Przygotuj odpowiedzi na 10 pytań i 3 historie STAR (zadanie tygodnia).
2. Zrób próbną rozmowę z Asystentem lub znajomym.
3. Przygotuj 4 pytania do firmy.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Co to jest metoda STAR?**
  - Sytuacja, Zadanie, Akcja, Rezultat — struktura odpowiedzi na pytania o doświadczenie.
- **Jak zachowujesz się na zadaniu praktycznym?**
  - Czytam, pytam, testuję przed i po, myślę na głos, pokazuję minimalny diff.
- **O co pytasz firmę w sprawie AI?**
  - O narzędzia, zasady dotyczące danych i repozytoriów, przegląd kodu i CI.

## Co potrafię teraz bez patrzenia na przykład?
Masz odpowiedzi STAR na 10 pytań, umiesz przeprowadzić zadanie praktyczne z głośnym myśleniem i zadajesz rzeczowe pytania o zasady AI w firmie.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- MIT Career Advising — The STAR method for behavioral interviews (dostęp 20.11.2026) — <https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/>
- Stack Overflow Developer Survey 2025 — AI (zaufanie, vibe coding w pracy zawodowej) (dostęp 19.11.2026) — <https://survey.stackoverflow.co/2025/ai>
- Claude Code — Best practices (dostęp 19.11.2026) — <https://code.claude.com/docs/en/best-practices>

## Test (w Mentorze: Lekcje → Sprawdź się)
- STAR to:
  - A) Ocena w gwiazdkach
  - B) Sytuacja, Zadanie, Akcja, Rezultat
  - C) Nazwa frameworka
  - D) Rodzaj testu
- Na zadaniu praktycznym najpierw:
  - A) Piszesz kod
  - B) Czytasz README i uruchamiasz testy
  - C) Prosisz AI o całość
  - D) Zmieniasz testy
- Nie znasz odpowiedzi. Najlepiej:
  - A) Zgadnąć pewnym tonem
  - B) Powiedzieć, jak byś to sprawdził
  - C) Zmienić temat
  - D) Milczeć

Odpowiedzi: B, B, B
