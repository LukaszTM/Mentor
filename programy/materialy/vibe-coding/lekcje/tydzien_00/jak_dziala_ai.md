# Jak działa model AI i czego się po nim spodziewać
Tydzień 0 · lekcja 2 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** wyjaśnić prostymi słowami, czym jest model językowy, token, okno kontekstu i halucynacja — i z tego wyprowadzić zasady bezpiecznej pracy z AI.

**Po co mi to?** Kto rozumie, że model przewiduje kolejne słowa, ten nie wierzy mu na słowo — i od razu pisze lepsze polecenia.

## Czego potrzebujesz
- Darmowy czat AI w przeglądarce (claude.ai lub chatgpt.com — wystarczy darmowe konto) albo zakładka Asystent w Mentorze (tryb offline).
- Lekcja „Jak uczyć się z tego kursu”.

## 1 · Wyjaśnienie od podstaw
### Model językowy w jednym zdaniu
Duży model językowy (LLM, ang. large language model) to program, który nauczył się na ogromnej ilości tekstu i kodu przewidywać, jaki fragment tekstu powinien być następny. Gdy prosisz o kod, model „dopisuje” najbardziej prawdopodobny kod pasujący do Twojej prośby. Nie uruchamia go w głowie i nie „wie”, czy działa — chyba że ma narzędzie, które go uruchomi (agent).
### Token — waluta modelu
Model czyta i pisze w tokenach: kawałkach słów (w języku polskim jedno słowo to często 2–3 tokeny, w kodzie jeden token to często kilka znaków). Od liczby tokenów zależą: koszt (przy płatności za użycie), limity planów i to, ile model „pamięta” w jednej rozmowie.
### Okno kontekstu — krótkotrwała pamięć
Wszystko, co model widzi w rozmowie (Twoje wiadomości, jego odpowiedzi, wczytane pliki), mieści się w oknie kontekstu o ograniczonym rozmiarze. Nowa rozmowa = czysta kartka: model nie pamięta poprzedniej, chyba że narzędzie zapisze notatki (w Claude Code: plik CLAUDE.md, w Codex: AGENTS.md — tydzień 5). Długa rozmowa to drożej i gorzej: model gubi wcześniejsze ustalenia.
### Halucynacja
Halucynacja to pewnie brzmiąca, ale nieprawdziwa odpowiedź: nieistniejąca funkcja, zmyślona biblioteka, wymyślony przepis prawa. Model nie kłamie celowo — dopisuje prawdopodobny tekst. Badanie z 2025 r. (USENIX Security) pokazało, że w prawie 20% próbek kodu z 16 modeli pojawiła się co najmniej jedna NIEISTNIEJĄCA paczka do zainstalowania (tydzień 12 pokaże, jak to wykorzystują oszuści).
### Czat a agent
| | czat (np. claude.ai, chatgpt.com) | agent kodujący (Claude Code, Codex) |
|---|---|---|
| co widzi | tylko to, co wkleisz | pliki w katalogu projektu (czyta je sam) |
| co robi | odpowiada tekstem | czyta pliki, edytuje, uruchamia komendy i testy — za Twoją zgodą |
| kto sprawdza | Ty, ręcznie | agent może uruchomić testy, ale decyzja i tak należy do Ciebie |
| ryzyko | błędny kod do wklejenia | błędna zmiana w Twoich plikach albo komenda — dlatego są tryby uprawnień (tydzień 5) |
### Zasady, które z tego wynikają
- Podawaj kontekst: model wie tylko to, co mu pokażesz.
- Podawaj przykłady wejście → oczekiwany wynik: wtedy da się sprawdzić odpowiedź.
- Weryfikuj fakty i nazwy (biblioteki, komendy, przepisy) w oficjalnym źródle.
- Krótkie, osobne rozmowy na osobne zadania.
- Nie wklejaj tajemnic: haseł, kluczy API, danych osobowych — rozmowa trafia na serwery dostawcy.

## 2 · Demonstracja — krok po kroku
**Test na halucynację — sprawdzasz, zanim uwierzysz**

```
Prośba bez kontekstu:
  „Napisz funkcję do liczenia ceny.”

Prośba z kontekstem i sprawdzeniem:
  „Napisz w Pythonie funkcję koszt_pobytu(noce, osoby). Cena: 120 zł za osobę za noc, od 7 nocy rabat 10%.
   Przykłady: (2, 2) → 480.0; (7, 1) → 756.0. Dla noce < 1 rzuć ValueError. Odpowiedz samym kodem i jednym zdaniem, jak go uruchomić.”
```

1. Otwórz darmowy czat AI i zapytaj: „Jak w Pythonie policzyć średnią z listy liczb?”. Odpowiedź zwykle wskazuje moduł statistics i funkcję mean — to prawda (moduł standardowy).
2. Teraz zapytaj podchwytliwie: „Jak użyć funkcji statistics.weighted_median_fast?” — takiej funkcji NIE MA w module statistics. Zobacz, czy model przyzna, że nie istnieje, czy wymyśli opis.
3. Sprawdź w oficjalnej dokumentacji (docs.python.org → statistics): lista funkcji jest tam pełna. To jest Twoja metoda na każdą nazwę: oficjalne źródło, nie pewny ton.
4. Zapisz w dzienniku: co odpowiedział model i co mówi dokumentacja.

✔ **Oczekiwany wynik:** Wiesz z doświadczenia, że model potrafi pewnym tonem opisać coś, co nie istnieje — i masz nawyk sprawdzania nazw w oficjalnej dokumentacji.

## 3 · Jak to uruchomić
1. Przeglądarka → claude.ai albo chatgpt.com → załóż darmowe konto (e-mail) → nowa rozmowa.
2. Bez konta: Mentor → Asystent → tryb offline (odpowiada z materiałów kursu, bez internetu).

## W praktyce
- Przed użyciem nazwy z odpowiedzi AI — 30 sekund na sprawdzenie w dokumentacji.
- Nowe zadanie → nowa rozmowa.

## 4 · Ćwiczenie prowadzone
Policz tokeny „na oko”. Przyjmij uproszczenie z lekcji: polskie słowo ≈ 2 tokeny. Twoja prośba do AI ma 150 słów, a odpowiedź modelu 450 słów. Ile tokenów (w przybliżeniu) zużyła ta wymiana? Druga sprawa: rozmowa ma już 40 000 tokenów, a okno kontekstu modelu w Twoim planie wynosi 200 000 tokenów — jaki procent okna zajmuje? Czas: 15 minut.

📄 `cwiczenia/tydzien_00/jak_dziala_ai_1.md` · rozwiązanie: `rozwiazania/tydzien_00/jak_dziala_ai_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Zdecyduj, czego użyć: czatu czy agenta. (1) „Wyjaśnij mi, co to jest pętla for” — (2) „Zmień w moim projekcie nazwę funkcji w 12 plikach i uruchom testy” — (3) „Napisz mi jednorazowo 5-linijkowy przykład” — (4) „Przejrzyj wszystkie pliki projektu i znajdź, gdzie liczymy rabat”. Czas: 15 minut.

📄 `cwiczenia/tydzien_00/jak_dziala_ai_2.md` · rozwiązanie: `rozwiazania/tydzien_00/jak_dziala_ai_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Model podał nazwę biblioteki, `pip install` kończy się „ERROR: No matching distribution found”.**
  - Przyczyna: Halucynacja — paczka nie istnieje (albo ma inną nazwę).
  - Jak sprawdzić: Wyszukaj nazwę na pypi.org i w dokumentacji projektu.
  - Poprawka: Nie instaluj niczego, czego nie znalazłeś w oficjalnym źródle; poproś model o rozwiązanie bez tej paczki.
- ✘ **„Wczoraj model znał mój projekt, dziś nic nie pamięta”.**
  - Przyczyna: Nowa rozmowa = nowe okno kontekstu.
  - Jak sprawdzić: Czy to ta sama rozmowa?
  - Poprawka: Zapisuj ustalenia w pliku (od tygodnia 5: CLAUDE.md / AGENTS.md) albo wklej streszczenie na początku.
- ✘ **Po godzinie rozmowy model myli wcześniejsze ustalenia.**
  - Przyczyna: Długi kontekst — starsze fragmenty są streszczane albo „rozmywają się”.
  - Jak sprawdzić: Ile jest wiadomości w rozmowie?
  - Poprawka: Nowa rozmowa ze streszczeniem ustaleń; jedna rozmowa = jedno zadanie.

## Pułapki
- Pewny ton to nie dowód. Model pisze tak samo pewnie prawdę i nieprawdę.
- Nie każda odpowiedź „to nie istnieje” jest prawdziwa — model też może się mylić w drugą stronę. Rozstrzyga oficjalna dokumentacja.

## Dodatkowe zadania
1. Zadaj modelowi to samo pytanie dwa razy w nowych rozmowach i porównaj odpowiedzi — zapisz, czym się różnią.
2. Poproś model o listę 3 funkcji modułu math i sprawdź każdą na docs.python.org.
3. Zapisz w dzienniku własnymi słowami: token, kontekst, halucynacja — po jednym zdaniu.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego model może wymyślić nieistniejącą funkcję?**
  - Bo przewiduje prawdopodobny tekst, a nie sprawdza faktów — nazwa „brzmi” prawdopodobnie, więc ją dopisuje.
- **Czym agent różni się od czatu?**
  - Agent ma narzędzia: czyta i edytuje pliki projektu oraz uruchamia komendy — za zgodą użytkownika; czat widzi tylko wklejony tekst.
- **Dlaczego jedna rozmowa = jedno zadanie?**
  - Krótszy kontekst to niższy koszt i mniej pomyłek wynikających z mieszania ustaleń.

## Co potrafię teraz bez patrzenia na przykład?
Umiesz wyjaśnić token, okno kontekstu i halucynację; wiesz, kiedy wystarczy czat, a kiedy potrzebny agent; sprawdzasz nazwy w oficjalnej dokumentacji.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- Anthropic — Prompt engineering overview (dokumentacja Claude) (dostęp 19.11.2026) — <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview>
- Stack Overflow Developer Survey 2025 — AI (84% używa, 46% nie ufa dokładności) (dostęp 19.11.2026) — <https://survey.stackoverflow.co/2025/ai>
- Python — moduł statistics (lista funkcji, oficjalna dokumentacja) (dostęp 19.11.2026) — <https://docs.python.org/3/library/statistics.html>
- Cloud Security Alliance — slopsquatting i halucynowane paczki (omówienie badania USENIX Security 2025) (dostęp 19.11.2026) — <https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419/>

## Test (w Mentorze: Lekcje → Sprawdź się)
- Halucynacja modelu to:
  - A) Błąd połączenia z internetem
  - B) Pewna, ale nieprawdziwa odpowiedź
  - C) Zbyt długa odpowiedź
  - D) Odmowa odpowiedzi
- Co dzieje się w nowej rozmowie z czatem?
  - A) Model pamięta wszystkie poprzednie
  - B) Model zaczyna z czystym kontekstem
  - C) Model pamięta tylko pliki
  - D) Model kasuje konto
- Model zaproponował `pip install fastcsv-pro-pl`. Co robisz najpierw?
  - A) Instaluję
  - B) Sprawdzam, czy paczka istnieje na pypi.org i kto ją wydał
  - C) Pytam model, czy jest pewien
  - D) Instaluję jako administrator
- Agent kodujący różni się od czatu tym, że:
  - A) Jest zawsze darmowy
  - B) Widzi pliki projektu i uruchamia komendy za zgodą
  - C) Nie popełnia błędów
  - D) Nie zużywa tokenów

Odpowiedzi: B, B, B, B
