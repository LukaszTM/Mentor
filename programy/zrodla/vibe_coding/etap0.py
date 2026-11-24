# -*- coding: utf-8 -*-
"""Etap 0 (tygodnie 0–3): Fundamenty — komputer, pliki, terminal, czytanie kodu, rozmowa z AI, specyfikacja, pierwszy program z AI."""

from wspolne import (BEZ_KONTA, TN, B, C, L, Q, T, Z, bl, kod, kw, li, test_z, tx, wy, wyjscie_z)

D = "dostęp 19.11.2026"
Z_CC_TERMINAL = ["Claude Code — przewodnik po terminalu dla nowych użytkowników (oficjalna dokumentacja)", "https://code.claude.com/docs/en/terminal-guide", D]
Z_CC_SETUP = ["Claude Code — instalacja i wymagania systemowe (oficjalna dokumentacja)", "https://code.claude.com/docs/en/setup", D]
Z_KARPATHY = ["Collins: „vibe coding” słowem roku 2025; cytat A. Karpathy’ego z lutego 2025 (tech.co, 6.11.2025)", "https://tech.co/news/vibe-coding-word-of-year-2025", D]
Z_SO = ["Stack Overflow Developer Survey 2025 — AI (84% używa, 46% nie ufa dokładności)", "https://survey.stackoverflow.co/2025/ai", D]
Z_METR = ["METR (10.07.2025): Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity — badanie RCT, z AI 19% wolniej", "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/", "dostęp 24.11.2026"]
Z_PY_TUT = ["Python — oficjalny tutorial (python.org, wersja polskojęzyczna częściowo; tłumaczenie robocze w lekcji)", "https://docs.python.org/3/tutorial/", D]
Z_PY_ERR = ["Python — Błędy i wyjątki (oficjalny tutorial, rozdz. 8)", "https://docs.python.org/3/tutorial/errors.html", D]
Z_MS_CMD = ["Microsoft Learn — polecenia wiersza poleceń Windows (cd, dir, mkdir, type)", "https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands", D]
Z_MS_EXT = ["Microsoft — Jak pokazać rozszerzenia nazw plików w Eksploratorze plików", "https://support.microsoft.com/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01", D]
Z_ANTH_PROMPT = ["Anthropic — Prompt engineering overview (dokumentacja Claude)", "https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview", D]
Z_CC_BEST = ["Claude Code — Best practices (oficjalna dokumentacja)", "https://code.claude.com/docs/en/best-practices", D]


# =========================================================================== TYDZIEŃ 0
START = L(
    id="start_vibe", nazwa="Jak uczyć się z tego kursu — czym jest vibe coding", tydzien=0,
    slowa=["vibe coding", "kurs", "plan", "agent", "Claude Code", "Codex", "Mentor"],
    cel="Po tej lekcji wiesz, co zbudujesz w 16 tygodni, ile to kosztuje, jak działa każdy dzień nauki i czym różni się „vibe coding” od programowania na ślepo.",
    po_co="Zanim powierzysz komputer agentowi AI, musisz wiedzieć, co jest Twoją pracą (cel, sprawdzenie, decyzja), a co pracą agenta (pisanie kodu).",
    wymagania=["Mentor uruchomiony na Windows 10/11 (ten program) — nic więcej w tym tygodniu.",
               "Ok. 80 minut dziennie od poniedziałku do piątku i do 90 minut w sobotę; razem ok. 120 godzin przez 16 tygodni (każdy tydzień mieści się w 9 godzinach).",
               "Konta i płatne subskrypcje NIE są potrzebne do tygodnia 4 — wtedy zdecydujesz, czy kupujesz plan (lekcja „Konta, plany i koszty”)."],
    wyjasnienie=(
        "## Co to jest vibe coding\n"
        "W lutym 2025 r. Andrej Karpathy (współzałożyciel OpenAI) opisał nowy sposób tworzenia programów: mówisz komputerowi zwykłym językiem, co ma powstać, "
        "a model AI pisze kod. Nazwał to „vibe coding” i dodał: „to nie jest tak naprawdę programowanie — widzę rzeczy, mówię rzeczy, uruchamiam rzeczy, kopiuję i wklejam, i to przeważnie działa” (tłumaczenie robocze). "
        "W listopadzie 2025 r. słownik Collins wybrał „vibe coding” słowem roku.\n"
        "Kluczowe słowo w tym cytacie to „przeważnie”. Ten kurs uczy wersji, która działa NIE przeważnie, tylko sprawdzalnie: AI pisze kod, a Ty mówisz, co ma powstać, "
        "sprawdzasz wynik testami i decydujesz, co zostaje.\n"
        "## Dwa style — i który wybieramy\n"
        "| styl | jak wygląda | kiedy wystarczy |\n"
        "|---|---|---|\n"
        "| vibe coding „na ślepo” | prosisz, wklejasz, nie czytasz, nie testujesz | zabawa, jednorazowy prototyp na własnym komputerze |\n"
        "| vibe coding odpowiedzialny (ten kurs) | opisujesz cel i kryteria, agent pisze, Ty czytasz zmiany, uruchamiasz testy, zapisujesz wersję w Git | wszystko, co ma działać jutro, dla klienta albo z prawdziwymi danymi |\n"
        "## Co mówią dane (żeby nie wierzyć reklamom)\n"
        "- Ankieta Stack Overflow 2025 (ponad 49 tys. programistów): 84% używa albo planuje używać AI, ale 46% nie ufa dokładności jego odpowiedzi.\n"
        "- Badanie METR (lipiec 2025): doświadczeni programiści na własnych, dużych projektach pracowali z AI o 19% wolniej, choć byli przekonani, że szybciej.\n"
        "- Wniosek dla Ciebie: AI daje ogromną przewagę na starcie i przy prostych aplikacjach, ale bez sprawdzania tworzy błędy, których nie widać od razu.\n"
        "## Co zbudujesz\n"
        "Przez cały kurs pracujesz dla fikcyjnego klienta: gospodarstwa agroturystycznego „Pod Lipą” (dane wymyślone). Kolejno powstaną: kalkulator ceny pobytu, lista gości, "
        "strona internetowa z kalkulatorem, raport z rezerwacji (CSV), aplikacja internetowa z bazą danych, skrypt porządkujący pliki i — w tygodniu 15 — mały system rezerwacji "
        "z testami, dokumentacją i publikacją w GitHub. Każdy element sprawdzają niezależne testy z paczki kursu, których agent nie może zmienić.\n"
        "## Etapy\n"
        "| etap | tygodnie | po etapie potrafisz |\n"
        "|---|---|---|\n"
        "| 0. Fundamenty | 0–3 | poruszać się po plikach i terminalu, czytać prosty kod Pythona, rozumieć komunikat błędu, napisać specyfikację i dostać od AI działający program |\n"
        "| 1. Agent przy pracy | 4–7 | zainstalować i bezpiecznie używać Claude Code i Codex, prowadzić projekt w Git i GitHub, czytać zmiany agenta, zarządzać kontekstem i kosztem |\n"
        "| 2. Budujesz aplikacje | 8–11 | zlecać kod pod testy, debugować z AI, budować stronę, aplikację Flask z bazą, raporty z danych, automatyzacje i bezpiecznie używać kluczy API |\n"
        "| 3. Jakość i zawód | 12–15 | zabezpieczać kod i agenta, znać prawo (prawo autorskie, RODO, AI Act), robić przegląd kodu, CI, README, rozmawiać z klientem, przygotować portfolio i projekt końcowy |\n"
        "## Jak wygląda dzień\n"
        "- Panel → zadanie dnia. Lekcja (zakładka Lekcje) — czytasz wyjaśnienie i demonstrację, potem dwa ćwiczenia z polami „Twoje odpowiedzi”: Mentor sprawdza każde pole i nie zdradza wyniku.\n"
        "- Zadanie dnia z paskiem „Ćwiczenie w Mentorze”: plik powstaje w Twoim katalogu roboczym (Dokumenty\\Mentor\\vibe-coding\\PRACA), „✔ Sprawdź wynik” uruchamia NIEZALEŻNE testy z paczki kursu.\n"
        "- Sobota: quiz tygodnia i powtórka. Niedziela wolna.\n"
        "- Dziennik: 3 zdania — co zbudowałem, co sprawdziłem, czego nie rozumiem.\n"
        "## Ile to kosztuje\n"
        "Tygodnie 0–3: 0 zł (Mentor, Python i darmowe czaty AI). Od tygodnia 4 agent kodujący wymaga płatnego planu: Claude Pro to 20 USD miesięcznie bez podatku (z VAT ok. 90–100 zł, zależnie od kursu), "
        "ChatGPT Plus (Codex) — także 20 USD. Wystarczy JEDEN z nich. Każde zadanie z agentem ma też ścieżkę bez płatnego konta: gotowy zapis pracy agenta z celowo wstawionym błędem, który znajdujesz i poprawiasz. "
        "Ceny zmieniają się — kalendarz aktualizacji w Ściądze przypomina, kiedy je sprawdzić.\n"
        "## Twoja rola: kierownik budowy, nie murarz\n"
        "Agent jest jak bardzo szybki pracownik, który nigdy nie był na Twojej budowie. Ty odpowiadasz za: (1) cel i granice („co ma powstać, czego nie ruszać”), "
        "(2) sprawdzenie („skąd wiem, że działa”), (3) decyzję („zostawiam czy cofam”). Tego nie da się zlecić — i właśnie tego uczy ten kurs."),
    przyklad=("Specyfikacja, którą w tygodniu 4 dasz agentowi (zobacz, jak mało w niej „kodu”):\n\n"
              "Cel: plik kalkulator_pobytu.py z funkcją koszt_pobytu(noce, osoby).\n"
              "Zasady: 120 zł za osobę za noc; od 7 nocy rabat 10%; noce lub osoby mniejsze niż 1 → ValueError.\n"
              "Przykłady: koszt_pobytu(2, 2) → 480.0; koszt_pobytu(7, 1) → 756.0.\n"
              "Nie ruszaj: innych plików w katalogu.\n"
              "Gotowe, gdy: przechodzą testy Mentora (✔ Sprawdź wynik)."),
    demonstracja={"tytul": "Jedna prośba, dwa podejścia — co się zmienia", "kroki": [
        "Podejście „na ślepo”: piszesz do czatu „zrób mi kalkulator ceny noclegu”. Dostajesz kod, kopiujesz, działa dla jednego przykładu. Nie wiesz, co z rabatem, ujemną liczbą nocy, groszami.",
        "Podejście kursu: najpierw zapisujesz specyfikację (powyżej): cel, zasady, przykłady wejście → wynik, czego nie ruszać, jak sprawdzisz.",
        "Agent pisze kod. Ty NIE zaczynasz od czytania kodu, tylko od sprawdzenia: czy przykłady ze specyfikacji dają dokładnie te wyniki? Mentor uruchamia testy i pokazuje ✔ albo listę przypadków, które nie przechodzą.",
        "Gdy coś nie przechodzi — nie piszesz „nie działa, popraw”. Wklejasz agentowi KONKRETNY przypadek: „koszt_pobytu(7, 1) zwraca 840.0, a powinno 756.0 — rabat od 7 nocy nie działa”.",
        "Na końcu zapisujesz wersję (od tygodnia 6 — commit w Git) i jedno zdanie w dzienniku: co sprawdziłeś."],
        "wynik": "Ten sam agent, ten sam model — ale w drugim podejściu wiesz, że program działa, i umiesz to pokazać klientowi lub rekruterowi."},
    jak_uruchomic=["Panel → „Pierwsze kroki” → zadanie diagnostyczne (8 pytań, nie blokuje nauki — pokazuje lekcje do powtórki).",
                   "Plan nauki → tydzień 0 → przeczytaj zadania na cały tydzień (3–4 min).",
                   "Mój projekt → „📁 Utwórz katalog roboczy kursu” (Mentor założy Dokumenty\\Mentor\\vibe-coding\\PRACA) → „📂 Skopiuj materiały kursu tutaj”."],
    cwiczenia=[
        C("prowadzone",
          "Przeczytaj opis etapów i dnia nauki. Odpowiedz w polach poniżej: ile tygodni trwa kurs, w którym tygodniu zaczynasz pracę z płatnym agentem i ile planów płatnych "
          "naprawdę potrzebujesz (Claude Pro albo ChatGPT Plus). Czas: 15 minut.",
          "16 tygodni (0–15); agent od tygodnia 4; wystarczy 1 plan (Claude Pro albo ChatGPT Plus) — każde zadanie z agentem ma też ścieżkę bez konta.",
          ["Spójrz na tabelę „Etapy” — tygodnie 0–15 to ile tygodni?", "Sekcja „Ile to kosztuje”: od którego tygodnia agent kodujący wymaga planu?", "„Wystarczy JEDEN z nich” — ile planów?"],
          "Tygodnie 0–15 to 16 tygodni. Płatny agent: od tygodnia 4. Wystarczy 1 plan — Claude Pro albo ChatGPT Plus; bez planu przechodzisz kurs ścieżką z zapisami pracy agenta.",
          [li("tyg", "Ile tygodni trwa kurs?", 16, bledy=[bl(15, "tygodnie są numerowane od 0 — od 0 do 15 to 16 tygodni")]),
           li("od", "Od którego tygodnia pracujesz z płatnym agentem?", 4),
           li("plany", "Ile płatnych planów potrzebujesz najwyżej?", 1, bledy=[bl(2, "wystarczy jeden — Claude Pro ALBO ChatGPT Plus; kurs pokazuje oba narzędzia, ale zadania wykonasz jednym")])]),
        C("samodzielne",
          "Zdecyduj o swoim rytmie. Otwórz Dziennik i zapisz: w jakie dni i o której godzinie się uczysz, ile minut, oraz co zrobisz, gdy opuścisz dzień. "
          "Potem oceń trzy sytuacje: czy to vibe coding „na ślepo”, czy odpowiedzialny? Czas: 20 minut.",
          "(1) wklejam kod z czatu i od razu wysyłam klientowi — na ślepo; (2) daję agentowi przykłady wejście→wynik i uruchamiam testy — odpowiedzialny; "
          "(3) agent napisał 400 linii, czytam tylko komunikat „Done!” — na ślepo.",
          ["Pytanie kontrolne: czy w danej sytuacji ktoś SPRAWDZIŁ wynik?", "Testy i przykłady wejście → wynik to sprawdzenie; komunikat agenta „gotowe” — nie.", "Sytuacja 2 ma przykłady i testy, 1 i 3 — nie mają sprawdzenia."],
          "(1) na ślepo — nikt nie sprawdził; (2) odpowiedzialny — przykłady i testy; (3) na ślepo — „Done!” to deklaracja agenta, nie dowód.",
          [wy("s1", "(1) Wklejam kod z czatu i od razu wysyłam klientowi", ["na ślepo", "odpowiedzialny"], "na ślepo"),
           wy("s2", "(2) Daję agentowi przykłady wejście→wynik i uruchamiam testy", ["na ślepo", "odpowiedzialny"], "odpowiedzialny"),
           wy("s3", "(3) Agent napisał 400 linii, czytam tylko komunikat „Done!”", ["na ślepo", "odpowiedzialny"], "na ślepo",
              bledy=[bl("odpowiedzialny", "komunikat agenta „gotowe” to jego deklaracja, a nie sprawdzenie — nic nie zostało uruchomione ani przetestowane")])]),
    ],
    typowe_bledy=[
        B("„Nie mam czasu na lekcje, od razu każę AI zrobić całą aplikację”.", "Pokusa skrótu — agent naprawdę potrafi wygenerować dużo kodu.",
          "Czy umiesz powiedzieć, skąd wiesz, że ta aplikacja działa?", "Zacznij od małego kawałka ze specyfikacją i testem; dużą aplikację budujesz w tygodniu 15 — z kamieniami milowymi."),
        B("„Panel pokazuje zaległości z trzech dni”.", "Przerwa w nauce.", "Plan nauki → bieżący tydzień.", "Nie nadrabiaj wszystkiego: jedna lekcja + jedno zadanie dziennie; Mentor nie karze za przerwy."),
        B("„Kupiłem od razu dwa plany i Max”.", "Obawa, że jeden nie wystarczy.", "Lekcja „Konta, plany i koszty” (tydzień 4).", "Zacznij od jednego planu za 20 USD; limity widzisz w /usage (Claude Code) — podnoś plan dopiero, gdy limit naprawdę blokuje pracę."),
    ],
    pulapki=["Vibe coding nie znaczy „nie musisz nic rozumieć” — znaczy „nie musisz pisać każdej linijki sam”. Rozumieć, co program robi i jak to sprawdzić, musisz zawsze.",
             "Dane klienta w kursie są fikcyjne. Nigdy nie wklejaj do AI prawdziwych danych osobowych, haseł ani kluczy (tydzień 12)."],
    zadania=["Przeczytaj w Planie nauki tytuły wszystkich 16 tygodni i zaznacz w dzienniku 2 tematy, które budzą największe obawy.",
             "Zapytaj darmowy czat AI: „Czym jest vibe coding i jakie są jego ryzyka?” — porównaj odpowiedź z tą lekcją i zapisz jedną różnicę.",
             "Zapisz w dzienniku jedno zdanie: po co mi ten kurs (praca, własny projekt, klient)."],
    pytania=[["Jaka jest Twoja rola, gdy kod pisze agent?", "Ustalam cel i granice, sprawdzam wynik (testy, przykłady) i decyduję, co zostaje — agent pisze kod."],
             ["Dlaczego komunikat agenta „gotowe” nie jest dowodem?", "To deklaracja modelu; dowodem jest uruchomienie programu i przejście testów na przykładach ze specyfikacji."],
             ["Ile kosztuje kurs w tygodniach 0–3?", "0 zł — Mentor, Python i darmowe czaty AI; płatny agent jest potrzebny dopiero od tygodnia 4 (i jest ścieżka bez konta)."]],
    podsumowanie="Wiesz, co zbudujesz, ile to kosztuje i jak wygląda dzień; rozumiesz różnicę między vibe codingiem na ślepo a odpowiedzialnym: cel → agent → sprawdzenie → decyzja.",
    test=[T("Co w tym kursie jest dowodem, że kod działa?", ["Komunikat agenta „Done!”", "Przejście testów na przykładach ze specyfikacji", "Długość kodu", "To, że model jest najnowszy"], 1,
            "Dowodem jest uruchomienie i testy; deklaracja agenta to tylko deklaracja."),
          T("Badanie METR z 2025 r. wykazało, że doświadczeni programiści z AI na własnych projektach:", ["Byli 2× szybsi", "Pracowali o 19% wolniej, choć sądzili, że szybciej", "Nie zauważyli różnicy", "Przestali używać AI"], 1,
            "Wniosek: odczucie szybkości to nie pomiar — mierz efekty testami i czasem."),
          T("Od którego tygodnia kursu potrzebny jest płatny agent (lub ścieżka bez konta)?", ["0", "2", "4", "12"], 2, "Tygodnie 0–3 kosztują 0 zł; od tygodnia 4 — Claude Code lub Codex."),
          T("Co znaczy „odpowiedzialny vibe coding”?", ["Nie używam AI", "Opisuję cel i kryteria, agent pisze, ja sprawdzam testami i decyduję", "Kopiuję kod z czatu", "Proszę AI o recenzję zamiast testów"], 1,
            "Cel → agent → sprawdzenie → decyzja.")],
    w_praktyce=["Każde zlecenie dla AI zaczynaj od zdania „Gotowe, gdy…”.", "Zapisuj, co sprawdziłeś — rekruter i klient zapytają właśnie o to."],
    zrodla=[Z_KARPATHY, Z_SO, Z_METR, Z_CC_TERMINAL],
)

JAK_DZIALA_AI = L(
    id="jak_dziala_ai", nazwa="Jak działa model AI i czego się po nim spodziewać", tydzien=0,
    slowa=["model", "LLM", "token", "halucynacja", "kontekst", "czat", "agent", "prompt"],
    cel="Po tej lekcji potrafisz wyjaśnić prostymi słowami, czym jest model językowy, token, okno kontekstu i halucynacja — i z tego wyprowadzić zasady bezpiecznej pracy z AI.",
    po_co="Kto rozumie, że model przewiduje kolejne słowa, ten nie wierzy mu na słowo — i od razu pisze lepsze polecenia.",
    wymagania=["Darmowy czat AI w przeglądarce (claude.ai lub chatgpt.com — wystarczy darmowe konto) albo zakładka Asystent w Mentorze (tryb offline).",
               "Lekcja „Jak uczyć się z tego kursu”."],
    wyjasnienie=(
        "## Model językowy w jednym zdaniu\n"
        "Duży model językowy (LLM, ang. large language model) to program, który nauczył się na ogromnej ilości tekstu i kodu przewidywać, jaki fragment tekstu powinien być następny. "
        "Gdy prosisz o kod, model „dopisuje” najbardziej prawdopodobny kod pasujący do Twojej prośby. Nie uruchamia go w głowie i nie „wie”, czy działa — chyba że ma narzędzie, które go uruchomi (agent).\n"
        "## Token — waluta modelu\n"
        "Model czyta i pisze w tokenach: kawałkach słów (w języku polskim jedno słowo to często 2–3 tokeny, w kodzie jeden token to często kilka znaków). "
        "Od liczby tokenów zależą: koszt (przy płatności za użycie), limity planów i to, ile model „pamięta” w jednej rozmowie.\n"
        "## Okno kontekstu — krótkotrwała pamięć\n"
        "Wszystko, co model widzi w rozmowie (Twoje wiadomości, jego odpowiedzi, wczytane pliki), mieści się w oknie kontekstu o ograniczonym rozmiarze. "
        "Nowa rozmowa = czysta kartka: model nie pamięta poprzedniej, chyba że narzędzie zapisze notatki (w Claude Code: plik CLAUDE.md, w Codex: AGENTS.md — tydzień 5). "
        "Długa rozmowa to drożej i gorzej: model gubi wcześniejsze ustalenia.\n"
        "## Halucynacja\n"
        "Halucynacja to pewnie brzmiąca, ale nieprawdziwa odpowiedź: nieistniejąca funkcja, zmyślona biblioteka, wymyślony przepis prawa. Model nie kłamie celowo — dopisuje prawdopodobny tekst. "
        "Badanie z 2025 r. (USENIX Security) pokazało, że w prawie 20% próbek kodu z 16 modeli pojawiła się co najmniej jedna NIEISTNIEJĄCA paczka do zainstalowania (tydzień 12 pokaże, jak to wykorzystują oszuści).\n"
        "## Czat a agent\n"
        "| | czat (np. claude.ai, chatgpt.com) | agent kodujący (Claude Code, Codex) |\n"
        "|---|---|---|\n"
        "| co widzi | tylko to, co wkleisz | pliki w katalogu projektu (czyta je sam) |\n"
        "| co robi | odpowiada tekstem | czyta pliki, edytuje, uruchamia komendy i testy — za Twoją zgodą |\n"
        "| kto sprawdza | Ty, ręcznie | agent może uruchomić testy, ale decyzja i tak należy do Ciebie |\n"
        "| ryzyko | błędny kod do wklejenia | błędna zmiana w Twoich plikach albo komenda — dlatego są tryby uprawnień (tydzień 5) |\n"
        "## Zasady, które z tego wynikają\n"
        "- Podawaj kontekst: model wie tylko to, co mu pokażesz.\n"
        "- Podawaj przykłady wejście → oczekiwany wynik: wtedy da się sprawdzić odpowiedź.\n"
        "- Weryfikuj fakty i nazwy (biblioteki, komendy, przepisy) w oficjalnym źródle.\n"
        "- Krótkie, osobne rozmowy na osobne zadania.\n"
        "- Nie wklejaj tajemnic: haseł, kluczy API, danych osobowych — rozmowa trafia na serwery dostawcy."),
    przyklad=("Prośba bez kontekstu:\n  „Napisz funkcję do liczenia ceny.”\n\n"
              "Prośba z kontekstem i sprawdzeniem:\n  „Napisz w Pythonie funkcję koszt_pobytu(noce, osoby). Cena: 120 zł za osobę za noc, od 7 nocy rabat 10%.\n"
              "   Przykłady: (2, 2) → 480.0; (7, 1) → 756.0. Dla noce < 1 rzuć ValueError. Odpowiedz samym kodem i jednym zdaniem, jak go uruchomić.”"),
    demonstracja={"tytul": "Test na halucynację — sprawdzasz, zanim uwierzysz", "kroki": [
        "Otwórz darmowy czat AI i zapytaj: „Jak w Pythonie policzyć średnią z listy liczb?”. Odpowiedź zwykle wskazuje moduł statistics i funkcję mean — to prawda (moduł standardowy).",
        "Teraz zapytaj podchwytliwie: „Jak użyć funkcji statistics.weighted_median_fast?” — takiej funkcji NIE MA w module statistics. Zobacz, czy model przyzna, że nie istnieje, czy wymyśli opis.",
        "Sprawdź w oficjalnej dokumentacji (docs.python.org → statistics): lista funkcji jest tam pełna. To jest Twoja metoda na każdą nazwę: oficjalne źródło, nie pewny ton.",
        "Zapisz w dzienniku: co odpowiedział model i co mówi dokumentacja."],
        "wynik": "Wiesz z doświadczenia, że model potrafi pewnym tonem opisać coś, co nie istnieje — i masz nawyk sprawdzania nazw w oficjalnej dokumentacji."},
    jak_uruchomic=["Przeglądarka → claude.ai albo chatgpt.com → załóż darmowe konto (e-mail) → nowa rozmowa.",
                   "Bez konta: Mentor → Asystent → tryb offline (odpowiada z materiałów kursu, bez internetu)."],
    cwiczenia=[
        C("prowadzone",
          "Policz tokeny „na oko”. Przyjmij uproszczenie z lekcji: polskie słowo ≈ 2 tokeny. Twoja prośba do AI ma 150 słów, a odpowiedź modelu 450 słów. "
          "Ile tokenów (w przybliżeniu) zużyła ta wymiana? Druga sprawa: rozmowa ma już 40 000 tokenów, a okno kontekstu modelu w Twoim planie wynosi 200 000 tokenów — jaki procent okna zajmuje? Czas: 15 minut.",
          "(150 + 450) × 2 = 1 200 tokenów; 40 000 / 200 000 = 20% okna.",
          ["Najpierw zsumuj słowa w obie strony — model „płaci” za wejście i wyjście.", "Pomnóż sumę przez 2 (słowo ≈ 2 tokeny).", "Procent okna = zajęte / całe okno × 100."],
          "Słowa: 150 + 450 = 600; tokeny ≈ 600 × 2 = 1 200. Okno: 40 000 / 200 000 × 100 = 20%.",
          [li("tokeny", "Tokeny w wymianie (w przybliżeniu)", 1200, bledy=[bl(600, "to liczba słów — pomnóż przez 2 tokeny na słowo"), bl(900, "policzyłeś tylko odpowiedź modelu — Twoja prośba też zużywa tokeny")]),
           li("procent", "Procent okna kontekstu zajęty przez rozmowę (%)", 20)]),
        C("samodzielne",
          "Zdecyduj, czego użyć: czatu czy agenta. (1) „Wyjaśnij mi, co to jest pętla for” — (2) „Zmień w moim projekcie nazwę funkcji w 12 plikach i uruchom testy” — "
          "(3) „Napisz mi jednorazowo 5-linijkowy przykład” — (4) „Przejrzyj wszystkie pliki projektu i znajdź, gdzie liczymy rabat”. Czas: 15 minut.",
          "(1) czat; (2) agent; (3) czat; (4) agent — agent widzi pliki projektu i może je przeszukać i zmienić, czat widzi tylko to, co wkleisz.",
          ["Zadaj pytanie: czy zadanie wymaga dostępu do MOICH plików?", "Wyjaśnienie pojęcia albo krótki przykład nie wymagają plików.", "Zmiana w 12 plikach i przeszukanie projektu — tylko agent widzi pliki."],
          "(1) czat — wyjaśnienie bez plików; (2) agent — edycja wielu plików i testy; (3) czat — krótki przykład; (4) agent — przeszukanie plików projektu.",
          [wy("z1", "(1) Wyjaśnij pętlę for", ["czat", "agent"], "czat"), wy("z2", "(2) Zmień nazwę funkcji w 12 plikach i uruchom testy", ["czat", "agent"], "agent"),
           wy("z3", "(3) Jednorazowy 5-linijkowy przykład", ["czat", "agent"], "czat"), wy("z4", "(4) Znajdź w projekcie, gdzie liczymy rabat", ["czat", "agent"], "agent",
                                                                                         bledy=[bl("czat", "czat nie widzi Twoich plików — musiałbyś wkleić cały projekt; agent przeszuka go sam")])]),
    ],
    typowe_bledy=[
        B("Model podał nazwę biblioteki, `pip install` kończy się „ERROR: No matching distribution found”.", "Halucynacja — paczka nie istnieje (albo ma inną nazwę).",
          "Wyszukaj nazwę na pypi.org i w dokumentacji projektu.", "Nie instaluj niczego, czego nie znalazłeś w oficjalnym źródle; poproś model o rozwiązanie bez tej paczki."),
        B("„Wczoraj model znał mój projekt, dziś nic nie pamięta”.", "Nowa rozmowa = nowe okno kontekstu.", "Czy to ta sama rozmowa?", "Zapisuj ustalenia w pliku (od tygodnia 5: CLAUDE.md / AGENTS.md) albo wklej streszczenie na początku."),
        B("Po godzinie rozmowy model myli wcześniejsze ustalenia.", "Długi kontekst — starsze fragmenty są streszczane albo „rozmywają się”.", "Ile jest wiadomości w rozmowie?", "Nowa rozmowa ze streszczeniem ustaleń; jedna rozmowa = jedno zadanie."),
    ],
    pulapki=["Pewny ton to nie dowód. Model pisze tak samo pewnie prawdę i nieprawdę.", "Nie każda odpowiedź „to nie istnieje” jest prawdziwa — model też może się mylić w drugą stronę. Rozstrzyga oficjalna dokumentacja."],
    zadania=["Zadaj modelowi to samo pytanie dwa razy w nowych rozmowach i porównaj odpowiedzi — zapisz, czym się różnią.",
             "Poproś model o listę 3 funkcji modułu math i sprawdź każdą na docs.python.org.",
             "Zapisz w dzienniku własnymi słowami: token, kontekst, halucynacja — po jednym zdaniu."],
    pytania=[["Dlaczego model może wymyślić nieistniejącą funkcję?", "Bo przewiduje prawdopodobny tekst, a nie sprawdza faktów — nazwa „brzmi” prawdopodobnie, więc ją dopisuje."],
             ["Czym agent różni się od czatu?", "Agent ma narzędzia: czyta i edytuje pliki projektu oraz uruchamia komendy — za zgodą użytkownika; czat widzi tylko wklejony tekst."],
             ["Dlaczego jedna rozmowa = jedno zadanie?", "Krótszy kontekst to niższy koszt i mniej pomyłek wynikających z mieszania ustaleń."]],
    podsumowanie="Umiesz wyjaśnić token, okno kontekstu i halucynację; wiesz, kiedy wystarczy czat, a kiedy potrzebny agent; sprawdzasz nazwy w oficjalnej dokumentacji.",
    test=[T("Halucynacja modelu to:", ["Błąd połączenia z internetem", "Pewna, ale nieprawdziwa odpowiedź", "Zbyt długa odpowiedź", "Odmowa odpowiedzi"], 1, "Np. zmyślona funkcja lub paczka."),
          T("Co dzieje się w nowej rozmowie z czatem?", ["Model pamięta wszystkie poprzednie", "Model zaczyna z czystym kontekstem", "Model pamięta tylko pliki", "Model kasuje konto"], 1,
            "Pamięć między sesjami dają pliki instrukcji (CLAUDE.md, AGENTS.md), nie sam model."),
          T("Model zaproponował `pip install fastcsv-pro-pl`. Co robisz najpierw?", ["Instaluję", "Sprawdzam, czy paczka istnieje na pypi.org i kto ją wydał", "Pytam model, czy jest pewien", "Instaluję jako administrator"], 1,
            "Model może zmyślić nazwę, a oszuści rejestrują takie nazwy (tydzień 12)."),
          T("Agent kodujący różni się od czatu tym, że:", ["Jest zawsze darmowy", "Widzi pliki projektu i uruchamia komendy za zgodą", "Nie popełnia błędów", "Nie zużywa tokenów"], 1, "Dlatego potrzebuje trybów uprawnień.")],
    w_praktyce=["Przed użyciem nazwy z odpowiedzi AI — 30 sekund na sprawdzenie w dokumentacji.", "Nowe zadanie → nowa rozmowa."],
    zrodla=[Z_ANTH_PROMPT, Z_SO, ["Python — moduł statistics (lista funkcji, oficjalna dokumentacja)", "https://docs.python.org/3/library/statistics.html", D],
            ["Cloud Security Alliance — slopsquatting i halucynowane paczki (omówienie badania USENIX Security 2025)", "https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419/", D]],
)

PLIKI = L(
    id="pliki_foldery", nazwa="Pliki, foldery, rozszerzenia i ścieżki", tydzien=0,
    slowa=["plik", "folder", "katalog", "rozszerzenie", "ścieżka", "Eksplorator", "zip"],
    cel="Po tej lekcji pokazujesz rozszerzenia plików, rozumiesz ścieżkę C:\\Users\\Ty\\Documents\\..., rozpakowujesz ZIP i wiesz, gdzie Mentor trzyma Twoje pliki.",
    po_co="Agent AI pracuje na plikach w konkretnym folderze — jeśli nie wiesz, gdzie on jest, nie sprawdzisz, co agent zmienił.",
    wymagania=["Windows 10/11, Eksplorator plików (Win + E).", "Katalog roboczy kursu utworzony w Mentorze (Mój projekt → „📁 Utwórz katalog roboczy kursu”)."],
    wyjasnienie=(
        "## Plik i folder\n"
        "Plik to porcja danych z nazwą (dokument, zdjęcie, program). Folder (katalog — w programowaniu mówi się raczej „katalog”) to pudełko na pliki i inne foldery. "
        "Projekt programistyczny to po prostu folder z plikami: kodem (.py, .html, .js), danymi (.csv, .json) i opisami (.md).\n"
        "## Rozszerzenie mówi, czym jest plik\n"
        "Rozszerzenie to końcówka nazwy po kropce: `raport.csv`, `app.py`, `index.html`. Windows domyślnie UKRYWA rozszerzenia — wtedy plik `notatki.txt.py` wygląda jak `notatki.txt`. "
        "Pierwsza rzecz w tym kursie: włącz pokazywanie rozszerzeń. Windows 11: Eksplorator → Widok → Pokaż → „Rozszerzenia nazw plików”. Windows 10: Eksplorator → karta Widok → zaznacz „Rozszerzenia nazw plików”.\n"
        "| rozszerzenie | co to | czym otwierasz |\n"
        "|---|---|---|\n"
        "| .py | program w Pythonie | edytor (VS Code, PyCharm, Notatnik); uruchamia go Python |\n"
        "| .md | notatka w Markdown (nagłówki #, listy -) | edytor; GitHub pokazuje ją ładnie |\n"
        "| .html / .css / .js | strona internetowa: treść / wygląd / zachowanie | przeglądarka (podwójne kliknięcie .html) i edytor |\n"
        "| .csv | tabela w tekście, kolumny oddzielone przecinkiem lub średnikiem | edytor, arkusz |\n"
        "| .json | dane w nawiasach { } — format wymiany między programami | edytor |\n"
        "| .zip | spakowane archiwum wielu plików | Eksplorator → „Wyodrębnij wszystkie” |\n"
        "## Ścieżka — adres pliku\n"
        "Ścieżka to adres pliku na dysku: `C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA\\app.py`. Czytasz ją od lewej: dysk C:, folder Users, folder użytkownika, Dokumenty (na dysku folder nazywa się „Documents”) itd. "
        "Separator w Windows to ukośnik wsteczny `\\`; w Pythonie i w internecie zwykle `/` — Python w Windows rozumie oba.\n"
        "- Ścieżka bezwzględna zaczyna się od dysku: `C:\\...`.\n"
        "- Ścieżka względna liczy się od bieżącego folderu: `dane\\rezerwacje.csv` znaczy „folder dane w miejscu, w którym jestem”.\n"
        "- Spacje i polskie znaki w nazwach działają, ale w terminalu ścieżkę ze spacją trzeba ująć w cudzysłów. Dlatego w projektach używamy nazw bez spacji i bez polskich liter: `lista_gosci.py`.\n"
        "## Gdzie są Twoje pliki w tym kursie\n"
        "- Katalog roboczy (PRACA): `Dokumenty\\Mentor\\vibe-coding\\PRACA` — tu powstają wszystkie pliki zadań i tu pracuje agent. Mentor → Mój projekt pokazuje dokładną ścieżkę.\n"
        "- Materiały kursu (lekcje, przykłady, rozwiązania, testy): kopiujesz je przyciskiem „📂 Skopiuj materiały kursu tutaj” — Mentor nie nadpisuje Twoich plików.\n"
        "## ZIP\n"
        "Kurs i programy często przychodzą jako .zip. Nie pracuj „w środku” ZIP-a (podwójne kliknięcie tylko pokazuje zawartość) — najpierw prawy przycisk → „Wyodrębnij wszystkie…”."),
    przyklad=("Struktura katalogu roboczego po tygodniu 3 (tak ma wyglądać u Ciebie):\n\n"
              "PRACA\\\n"
              "├── notatki\\\n"
              "│   └── o_mnie.md\n"
              "├── dane\\\n"
              "│   └── rezerwacje.csv\n"
              "├── witaj.py\n"
              "├── kalkulator_pobytu.py\n"
              "└── dziennik.md"),
    demonstracja={"tytul": "Od ZIP-a do pliku z widocznym rozszerzeniem", "kroki": [
        "Win + E otwiera Eksplorator. Włącz „Rozszerzenia nazw plików” (Widok → Pokaż). Od teraz widzisz `dziennik.md`, a nie `dziennik`.",
        "Mentor → Mój projekt → „Otwórz folder” — Eksplorator otwiera katalog PRACA. Pasek adresu na górze: kliknij w niego, zobaczysz pełną ścieżkę (zaznacz i skopiuj Ctrl+C — przyda się agentowi).",
        "W PRACA: prawy przycisk → Nowy → Folder → nazwa `notatki`. W środku: prawy przycisk → Nowy → Dokument tekstowy → zmień nazwę na `o_mnie.md` (Windows zapyta, czy zmienić rozszerzenie — Tak).",
        "Otwórz `o_mnie.md` Notatnikiem (prawy przycisk → Otwórz za pomocą → Notatnik), wpisz trzy linie: `# O mnie`, `- uczę się vibe codingu`, `- cel: …`, zapisz Ctrl+S.",
        "Sprawdź: w Eksploratorze plik ma nazwę `o_mnie.md`, a nie `o_mnie.md.txt`. Jeśli widzisz `.txt` na końcu — rozszerzenia były ukryte przy tworzeniu; zmień nazwę."],
        "wynik": "W PRACA jest folder notatki z plikiem o_mnie.md; widzisz rozszerzenia i znasz pełną ścieżkę katalogu roboczego."},
    jak_uruchomic=["Win + E → Widok → Pokaż → Rozszerzenia nazw plików (Windows 11).", "Mentor → Mój projekt → „Otwórz folder”."],
    cwiczenia=[
        C("prowadzone",
          "Przeanalizuj ścieżkę `C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA\\dane\\rezerwacje.csv`. Odpowiedz: jak nazywa się plik (z rozszerzeniem), jakie ma rozszerzenie (bez kropki), "
          "w jakim folderze bezpośrednio leży, i jaka jest jego ścieżka względna, jeśli jesteś w folderze PRACA. Czas: 15 minut.",
          "Plik: rezerwacje.csv; rozszerzenie: csv; folder: dane; ścieżka względna od PRACA: dane\\rezerwacje.csv.",
          ["Nazwa pliku to ostatni fragment po ostatnim ukośniku.", "Rozszerzenie — po ostatniej kropce w nazwie pliku.", "Ścieżka względna od PRACA — wszystko, co jest za `PRACA\\`."],
          "Ostatni element: rezerwacje.csv (rozszerzenie csv). Leży bezpośrednio w folderze dane. Od PRACA: dane\\rezerwacje.csv (w Pythonie można też dane/rezerwacje.csv).",
          [tx("plik", "Nazwa pliku z rozszerzeniem", ["rezerwacje.csv"]), tx("roz", "Rozszerzenie (bez kropki)", ["csv"]), tx("folder", "Folder, w którym bezpośrednio leży plik", ["dane"]),
           tx("wzgl", "Ścieżka względna od PRACA", ["dane\\rezerwacje.csv", "dane/rezerwacje.csv"],
              bledy=[bl("rezerwacje.csv", "plik nie leży w samym PRACA, tylko w podfolderze dane — dopisz go przed nazwą")])]),
        C("samodzielne",
          "Dostajesz plik `cennik.pdf.exe` z załącznika maila od „klienta”. Co to jest naprawdę (jakie rozszerzenie decyduje)? Czy go otworzysz? "
          "Druga sytuacja: plik `notatki.txt` po włączeniu rozszerzeń okazuje się nazywać `notatki.txt.txt` — ile kropek ma pełna nazwa? Czas: 15 minut.",
          "`cennik.pdf.exe` to program (decyduje ostatnie rozszerzenie: exe) — nie otwierasz; to typowa sztuczka oszustów przy ukrytych rozszerzeniach. `notatki.txt.txt` ma 2 kropki.",
          ["Które rozszerzenie decyduje — pierwsze czy ostatnie?", ".exe to plik wykonywalny — uruchamia program.", "Policz kropki w nazwie notatki.txt.txt."],
          "Decyduje ostatnie rozszerzenie: exe → to program podszywający się pod PDF; nie otwieraj, usuń. `notatki.txt.txt` — 2 kropki (powstał, gdy rozszerzenia były ukryte, a Ty dopisałeś .txt).",
          [tx("roz", "Rozszerzenie, które decyduje o typie pliku cennik.pdf.exe", ["exe"], bledy=[bl("pdf", "o typie decyduje OSTATNIE rozszerzenie — .pdf w środku nazwy to przebranie")]),
           wy("otworz", "Czy otworzysz cennik.pdf.exe?", TN, "nie"), li("kropki", "Ile kropek ma nazwa notatki.txt.txt?", 2)]),
    ],
    typowe_bledy=[
        B("Plik nazywa się `witaj.py.txt` i Python mówi „can't open file 'witaj.py'”.", "Notatnik dopisał .txt, a rozszerzenia były ukryte.", "Włącz rozszerzenia w Eksploratorze i spójrz na pełną nazwę.", "Zmień nazwę na `witaj.py`; w Notatniku przy zapisie wybierz „Wszystkie pliki (*.*)”."),
        B("„Nie mogę znaleźć pliku, który utworzył agent”.", "Agent pracował w innym folderze niż myślisz.", "Mentor → Mój projekt → ścieżka; w terminalu `cd` pokazuje bieżący folder.", "Uruchamiaj agenta zawsze w katalogu PRACA (przycisk „Otwórz Claude Code tutaj”)."),
        B("Program nie widzi pliku `dane\\rezerwacje.csv`.", "Uruchomiony z innego folderu — ścieżka względna liczy się od bieżącego folderu.", "Sprawdź, gdzie jest terminal (`cd` bez argumentów).", "Uruchamiaj programy z katalogu PRACA albo użyj ścieżki bezwzględnej."),
    ],
    pulapki=["Spacje i polskie znaki w nazwach plików projektu utrudniają pracę w terminalu — używaj `male_litery_z_podkresleniem`.",
             "Nie trzymaj projektu na Pulpicie synchronizowanym z OneDrive — synchronizacja potrafi blokować pliki w trakcie pracy agenta. Katalog PRACA w Dokumentach jest bezpieczniejszy (jeśli Dokumenty też są w OneDrive, wybierz w Mentorze inny katalog, np. C:\\Projekty)."],
    zadania=["Włącz rozszerzenia i znajdź na dysku 3 pliki o różnych rozszerzeniach z tabeli lekcji.", "Utwórz w PRACA foldery `notatki` i `dane`.", "Rozpakuj dowolny ZIP („Wyodrębnij wszystkie”) i sprawdź, czy rozumiesz strukturę folderów."],
    pytania=[["Dlaczego trzeba włączyć widoczne rozszerzenia?", "Bo Windows je ukrywa — nie odróżnisz `app.py` od `app.py.txt`, a oszustwa typu `faktura.pdf.exe` stają się niewidoczne."],
             ["Czym różni się ścieżka bezwzględna od względnej?", "Bezwzględna zaczyna się od dysku (C:\\...), względna liczy się od bieżącego folderu (dane\\plik.csv)."],
             ["Gdzie powstają pliki zadań w tym kursie?", "W katalogu roboczym PRACA (Dokumenty\\Mentor\\vibe-coding\\PRACA, dokładna ścieżka w Mój projekt)."]],
    podsumowanie="Widzisz rozszerzenia, czytasz ścieżki bezwzględne i względne, znasz katalog PRACA i rozpakowujesz ZIP przed pracą.",
    test=[T("Jakie rozszerzenie ma program w Pythonie?", [".txt", ".py", ".exe", ".md"], 1, "Python uruchamia pliki .py."),
          T("Plik `zdjecie.jpg.exe` to:", ["Zdjęcie", "Program wykonywalny", "Dokument", "Archiwum"], 1, "Decyduje ostatnie rozszerzenie."),
          T("Jesteś w folderze PRACA. Ścieżka `dane\\goscie.csv` wskazuje:", ["C:\\dane\\goscie.csv", "PRACA\\dane\\goscie.csv", "Pulpit\\goscie.csv", "Nic"], 1, "Ścieżka względna liczy się od bieżącego folderu."),
          T("Jak poprawnie otworzyć zawartość ZIP do pracy?", ["Podwójnym kliknięciem i edycją w środku", "Prawy przycisk → Wyodrębnij wszystkie", "Zmienić rozszerzenie na .py", "Wysłać mailem"], 1, "Praca w środku ZIP-a często nie zapisuje zmian.")],
    w_praktyce=["Przed każdą sesją z agentem sprawdź, w jakim folderze jesteś.", "Nazwy plików: małe litery, bez spacji i polskich znaków."],
    zrodla=[Z_MS_EXT, Z_MS_CMD, Z_CC_TERMINAL],
)


# =========================================================================== TYDZIEŃ 1
TERMINAL = L(
    id="terminal_cmd", nazwa="Terminal bez strachu: CMD i PowerShell", tydzien=1,
    slowa=["terminal", "cmd", "PowerShell", "cd", "dir", "mkdir", "komenda", "wiersz poleceń"],
    cel="Po tej lekcji otwierasz terminal w katalogu projektu, poruszasz się po folderach (cd, dir), tworzysz foldery i pliki, odróżniasz CMD od PowerShell i bezpiecznie przerywasz komendę.",
    po_co="Agenci kodujący (Claude Code, Codex) działają w terminalu i wykonują w nim komendy — musisz rozumieć, co tam się dzieje, zanim cokolwiek zaakceptujesz.",
    wymagania=["Mentor → Mój projekt → „⌨ Otwórz terminal tutaj” (otwiera CMD w katalogu PRACA ze środowiskiem Pythona kursu).",
               "Lekcja „Pliki, foldery, rozszerzenia i ścieżki”."],
    wyjasnienie=(
        "## Terminal to rozmowa z komputerem tekstem\n"
        "Zamiast klikać, wpisujesz polecenie i naciskasz Enter. Terminal pokazuje znak zachęty (prompt) — miejsce, w którym czeka na polecenie. "
        "Windows ma dwa terminale: CMD (Wiersz polecenia) i PowerShell. Rozpoznasz je po zachęcie:\n"
        "| terminal | zachęta wygląda tak | gdzie go spotkasz |\n"
        "|---|---|---|\n"
        "| CMD | `C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA>` | przycisk Mentora „Otwórz terminal tutaj”, „Otwórz Claude Code tutaj” |\n"
        "| PowerShell | `PS C:\\Users\\Anna>` (z literami PS na początku) | Win + X → Terminal / Windows PowerShell — tu instalujesz Claude Code i Codex |\n"
        "Komendy instalacyjne z dokumentacji są pisane pod konkretny terminal. Dokumentacja Claude Code podaje dwie wskazówki: błąd „The token '&&' is not a valid statement separator” oznacza, "
        "że jesteś w PowerShell, a „'irm' is not recognized” — że jesteś w CMD.\n"
        "## Komendy, których potrzebujesz (CMD)\n"
        "| komenda | co robi | przykład |\n"
        "|---|---|---|\n"
        "| `cd` | pokazuje bieżący folder (bez argumentu) albo przechodzi do folderu | `cd dane` · `cd ..` (piętro wyżej) |\n"
        "| `dir` | lista plików i folderów | `dir` · `dir *.py` (tylko pliki .py) |\n"
        "| `mkdir` | tworzy folder | `mkdir notatki` |\n"
        "| `type` | wyświetla zawartość pliku tekstowego | `type dziennik.md` |\n"
        "| `cls` | czyści ekran | `cls` |\n"
        "| `python plik.py` | uruchamia program w Pythonie | `python witaj.py` |\n"
        "W PowerShell działają też `ls` (lista) i `cat` (zawartość) — to skróty. Agenci często używają ich zamiennie.\n"
        "## Triki, które oszczędzają czas\n"
        "- Tab dopełnia nazwę pliku lub folderu: wpisz `cd da` i naciśnij Tab → `cd dane`.\n"
        "- Strzałka w górę przywołuje poprzednią komendę.\n"
        "- Ctrl + C przerywa działający program (np. zapętlony). Ctrl + C w terminalu to NIE „kopiuj” — kopiujesz zaznaczając myszą i Enter albo prawym przyciskiem.\n"
        "- Wklejanie: prawy przycisk myszy albo Ctrl + V (w nowym Terminalu Windows).\n"
        "- Ścieżkę ze spacją bierz w cudzysłów: `cd \"Moje projekty\"`.\n"
        "## Bezpieczeństwo: czytaj, zanim naciśniesz Enter\n"
        "Terminal wykonuje dokładnie to, co wpiszesz, bez kosza i bez „Cofnij”. Komendy usuwające (`del`, `rmdir /s`, w PowerShell `Remove-Item -Recurse`) usuwają od razu. "
        "Gdy agent proponuje komendę, czytasz ją tak jak przelew w banku: co, gdzie, na czym. Jeśli nie rozumiesz komendy — pytasz agenta „wyjaśnij tę komendę i co się stanie”, zanim zatwierdzisz."),
    przyklad=("Sesja w CMD (to, co wpisujesz, jest po znaku >):\n\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA>cd\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA\n\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA>mkdir dane\n\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA>cd dane\n\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA\\dane>cd ..\n\n"
              "C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA>dir *.md\n"
              " ...\n"
              "18.11.2026  20:14               142 dziennik.md\n"
              "               1 plik(ów)            142 bajtów"),
    demonstracja={"tytul": "Pięć komend w katalogu roboczym", "kroki": [
        "Mentor → Mój projekt → „⌨ Otwórz terminal tutaj”. Otwiera się czarne okno CMD; pierwsza linia mówi „Katalog roboczy: …”, druga pokazuje wersję Pythona kursu (albo prośbę o przygotowanie środowiska).",
        "Wpisz `cd` i Enter — terminal wypisuje bieżący folder. To ta sama ścieżka, którą widzisz w Mój projekt.",
        "Wpisz `mkdir dane` — powstaje folder. `dir` — widzisz go na liście z oznaczeniem <DIR>.",
        "`cd dane` → zachęta kończy się na `\\dane>`. `cd ..` wraca piętro wyżej. Spróbuj `cd da` + Tab — terminal dopełnia nazwę.",
        "`type dziennik.md` (jeśli plik istnieje) wyświetla jego treść. Na koniec `cls` czyści ekran, strzałka w górę przywołuje poprzednie komendy."],
        "wynik": "Umiesz sprawdzić, gdzie jesteś, przejść do folderu i z powrotem, utworzyć folder i obejrzeć plik — bez klikania."},
    jak_uruchomic=["Mentor → Mój projekt → „⌨ Otwórz terminal tutaj” (CMD w PRACA).", "PowerShell: Win + X → „Terminal” albo „Windows PowerShell” (zachęta zaczyna się od PS)."],
    cwiczenia=[
        C("prowadzone",
          "Jesteś w `C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA` (CMD). Wpisujesz po kolei: `mkdir raporty`, `cd raporty`, `cd ..`, `cd dane`. "
          "W jakim folderze jesteś na końcu (sama nazwa ostatniego folderu)? Jaką komendą wyświetlisz zawartość pliku `goscie.csv` w tym folderze? Którą komendą przerwiesz zawieszony program? Czas: 15 minut.",
          "Na końcu jesteś w folderze dane (PRACA\\dane); zawartość pliku: `type goscie.csv`; przerwanie programu: Ctrl + C.",
          ["`cd ..` cofa o jeden poziom — wróciłeś do PRACA.", "Potem `cd dane` — wchodzisz do dane.", "Zawartość pliku tekstowego w CMD wyświetla `type`; przerwanie — kombinacja klawiszy z C."],
          "mkdir raporty (tworzy), cd raporty (wchodzisz), cd .. (wracasz do PRACA), cd dane (wchodzisz do dane) → folder: dane. Plik: `type goscie.csv`. Przerwanie: Ctrl + C.",
          [tx("folder", "Folder na końcu (nazwa)", ["dane"], bledy=[bl("raporty", "po `cd raporty` było jeszcze `cd ..` (powrót do PRACA) i `cd dane`")]),
           tx("type", "Komenda wyświetlająca goscie.csv (CMD)", ["type goscie.csv"], bledy=[bl("cat goscie.csv", "cat działa w PowerShell; w CMD (terminal Mentora) użyj type")]),
           wy("stop", "Jak przerwiesz zawieszony program?", ["Ctrl + C", "Ctrl + Z", "Esc", "zamknę komputer"], "Ctrl + C")]),
        C("samodzielne",
          "Dokumentacja podaje dwie komendy instalacyjne Claude Code: dla PowerShell `irm https://claude.ai/install.ps1 | iex` i dla CMD `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`. "
          "Masz okno z zachętą `C:\\Users\\Anna>` (bez PS). Którą komendę wkleisz? Jaki błąd zobaczysz, jeśli wkleisz tę drugą? Czas: 15 minut. (Niczego jeszcze nie instaluj — instalacja w tygodniu 4.)",
          "Zachęta bez PS = CMD → komenda z curl … install.cmd. Gdybyś wkleił `irm …` w CMD, zobaczysz „'irm' is not recognized as an internal or external command”.",
          ["Zachęta z literami PS na początku oznacza PowerShell, bez nich — CMD.", "`irm` to polecenie PowerShell.", "Dokumentacja: „'irm' is not recognized” = jesteś w CMD."],
          "Okno to CMD (brak PS). Właściwa: wersja z curl i install.cmd. Komenda PowerShell w CMD daje błąd „'irm' is not recognized…”, a komenda CMD w PowerShell — „The token '&&' is not a valid statement separator”.",
          [wy("term", "Jaki to terminal (zachęta C:\\Users\\Anna>)?", ["CMD", "PowerShell"], "CMD"),
           wy("kom", "Którą komendę wkleisz?", ["irm … install.ps1 | iex", "curl … install.cmd && install.cmd && del install.cmd"], "curl … install.cmd && install.cmd && del install.cmd"),
           tx("blad", "Słowo, które pojawi się w błędzie po wklejeniu komendy PowerShell do CMD (pierwsze słowo komendy)", ["irm"])]),
    ],
    typowe_bledy=[
        B("„'python' is not recognized as an internal or external command”.", "Python nie jest zainstalowany albo terminal nie ma go w PATH.", "Mentor → Środowisko → stan Pythona; terminal otwarty z Mentora pokazuje wersję w drugiej linii.",
          "Środowisko → „⬇ Zainstaluj brakujące”, potem otwórz terminal przyciskiem Mentora (ustawia Pythona kursu na początku PATH)."),
        B("„The system cannot find the path specified.” po `cd`.", "Literówka albo folder nie istnieje w bieżącym miejscu.", "`dir` — czy folder jest na liście?", "Użyj Tab do dopełniania nazwy; sprawdź `cd`, gdzie jesteś."),
        B("Terminal „wisi” — kursor miga, nic się nie dzieje.", "Program czeka na dane (input) albo zapętlił się.", "Czy program prosi o wpisanie czegoś?", "Wpisz dane i Enter, a jeśli to pętla — Ctrl + C."),
    ],
    pulapki=["Ctrl + C w terminalu przerywa program, a nie kopiuje (w nowym Terminalu Windows kopiuje tylko, gdy coś jest zaznaczone).",
             "Nigdy nie wklejaj do terminala komendy z nieznanej strony bez zrozumienia — zwłaszcza zaczynającej się od `irm … | iex` lub `curl … | bash`: one pobierają i od razu uruchamiają program. Instalujesz tak tylko z oficjalnego adresu producenta."],
    zadania=["Utwórz komendami foldery `notatki`, `dane`, `raporty` w PRACA i sprawdź `dir`.", "Otwórz PowerShell i CMD obok siebie — zapisz w dzienniku, po czym je rozpoznajesz.", "Przećwicz Tab i strzałkę w górę na 5 komendach."],
    pytania=[["Po czym poznasz, że jesteś w PowerShell?", "Zachęta zaczyna się od liter PS, np. `PS C:\\Users\\Anna>`."],
             ["Jak przejdziesz o jeden folder wyżej?", "`cd ..`"],
             ["Co zrobisz, zanim zatwierdzisz komendę zaproponowaną przez agenta?", "Przeczytam ją i — jeśli jej nie rozumiem — poproszę agenta o wyjaśnienie, co zrobi i na jakich plikach."]],
    podsumowanie="Otwierasz terminal w PRACA, poruszasz się cd/dir, tworzysz foldery, czytasz pliki type, odróżniasz CMD od PowerShell i przerywasz program Ctrl + C.",
    test=[T("Komenda `cd ..` w CMD:", ["Usuwa folder", "Przechodzi o jeden folder wyżej", "Pokazuje pliki", "Tworzy folder .."], 1, "Dwie kropki = folder nadrzędny."),
          T("Zachęta `PS C:\\Users\\Anna>` oznacza:", ["CMD", "PowerShell", "Python", "Claude Code"], 1, "PS = PowerShell."),
          T("Jak przerwiesz zapętlony program w terminalu?", ["Ctrl + C", "Ctrl + S", "Alt + F4 na pulpicie", "Enter"], 0, "Ctrl + C wysyła przerwanie."),
          T("Co oznacza błąd „'irm' is not recognized…”?", ["Brak internetu", "Wkleiłeś komendę PowerShell do CMD", "Brak uprawnień administratora", "Zła wersja Windows"], 1, "Tak podaje dokumentacja Claude Code.")],
    w_praktyce=["Zawsze `cd` przed pracą — wiesz, w jakim folderze działa agent.", "Każdą komendę usuwającą czytaj dwa razy."],
    zrodla=[Z_CC_TERMINAL, Z_CC_SETUP, Z_MS_CMD],
)

PYTHON_URUCH = L(
    id="python_uruchamianie", nazwa="Python: instalacja przez Mentora i pierwszy program", tydzien=1,
    slowa=["python", "instalacja", "środowisko", "venv", "print", "uruchom", "interpreter"],
    cel="Po tej lekcji masz zainstalowane środowisko Pythona kursu, uruchamiasz program przyciskiem w Mentorze i komendą `python plik.py`, a wynik porównujesz z oczekiwanym.",
    po_co="Kod od AI trzeba uruchomić, żeby wiedzieć, czy działa — Python jest silnikiem, na którym wykonasz 90% zadań kursu.",
    wymagania=["Mentor → zakładka Środowisko (sprawdza i instaluje Pythona oraz biblioteki kursu: pytest, flask, requests) — za Twoją zgodą, bez uprawnień administratora.",
               "Internet przy pierwszej instalacji (ok. 30–80 MB).", "Lekcja „Terminal bez strachu”."],
    wyjasnienie=(
        "## Python i interpreter\n"
        "Python to język programowania — zestaw reguł zapisu poleceń. Interpreter Pythona to program, który czyta Twój plik .py linia po linii i wykonuje polecenia. "
        "Kod od AI jest tylko tekstem, dopóki interpreter go nie wykona.\n"
        "## Środowisko kursu (.venv) — dlaczego osobne\n"
        "Mentor tworzy dla kursu osobne środowisko (folder `.venv`) z określonymi wersjami bibliotek: pytest (testy), flask (aplikacje internetowe), requests (pobieranie danych z internetu). "
        "Dzięki temu kurs nie psuje innych programów na komputerze, a testy działają u wszystkich tak samo. Biblioteki instalowane są z listy z sumami kontrolnymi (requirements.lock).\n"
        "## Instalacja krok po kroku\n"
        "- Mentor → Środowisko → „🔍 Sprawdź ponownie” — zobaczysz listę: Python, pakiety, narzędzia (Git, Claude Code, Codex — opcjonalne do późniejszych tygodni).\n"
        "- „⬇ Zainstaluj brakujące” → okno z opisem, co i gdzie powstanie → „Zgadzam się — wykonaj”. Postęp widać na pasku; w razie błędu — „Pokaż szczegóły (pełny log)”.\n"
        "- „✔ Sprawdź działanie” — Mentor uruchamia próbny test. Zielony wynik = gotowe.\n"
        "## Pierwszy program\n"
        "`print(\"Dzień dobry\")` — funkcja print wypisuje tekst. Tekst w cudzysłowach to napis (string). Każda linia to polecenie; Python wykonuje je od góry do dołu.\n"
        "## Trzy sposoby uruchomienia (wszystkie robią to samo)\n"
        "| sposób | jak | kiedy |\n"
        "|---|---|---|\n"
        "| przycisk w zadaniu | pasek „Ćwiczenie w Mentorze” → „▶ Uruchom” | zadania kursu — od razu widać wynik i tłumaczenie błędu po polsku |\n"
        "| terminal | `python witaj.py` w terminalu otwartym przyciskiem Mentora | gdy pracujesz z agentem lub chcesz podać argumenty |\n"
        "| edytor | VS Code / PyCharm → Run | gdy masz edytor (opcjonalnie) |\n"
        "## „✔ Sprawdź wynik” — czym różni się od „Uruchom”\n"
        "„Uruchom” tylko wykonuje program. „Sprawdź wynik” uruchamia go z danymi testowymi i porównuje z oczekiwanym wynikiem albo uruchamia niezależne testy z paczki kursu (sprawdzone sumą SHA-256 — nikt ich nie podmienił). "
        "Dopiero zielony wynik zalicza zadanie automatycznie.\n"
        "## Edytor (opcjonalnie)\n"
        "Mentor otwiera pliki w pierwszym znalezionym edytorze: VS Code, PyCharm, Notepad++, a w ostateczności Notatnik. Polecamy darmowy VS Code (code.visualstudio.com) — w tygodniu 4 przyda się też do rozszerzeń Claude Code i Codex."),
    przyklad=kod("python_uruchamianie:przyklad",
                 "# witaj.py — pierwszy program\n"
                 "print(\"Dzień dobry!\")\n"
                 "print(\"Uczę się vibe codingu.\")\n"
                 "print(\"2 + 3 =\", 2 + 3)\n",
                 "Dzień dobry!\nUczę się vibe codingu.\n2 + 3 = 5\n"),
    demonstracja={"tytul": "Od pustego katalogu do wyniku na ekranie", "kroki": [
        "Środowisko → „⬇ Zainstaluj brakujące” → zgoda. Po kilku minutach „✔ Sprawdź działanie” pokazuje zielony wynik.",
        "Plan nauki → tydzień 1 → zadanie „witaj.py” → „📝 Utwórz plik ćwiczenia”: Mentor tworzy w PRACA plik z komentarzem-nagłówkiem (linie zaczynające się od # Python pomija).",
        "Wpisz trzy linie z przykładu. print(\"…\") wypisuje tekst; w trzeciej linii print dostaje dwie rzeczy: napis i wynik działania 2 + 3 — wypisuje je ze spacją.",
        "Zapisz (Ctrl + S) i kliknij „▶ Uruchom”: okno wyniku pokazuje trzy linie. Zmień 2 + 3 na 20 * 3 i uruchom ponownie — wynik 60.",
        "„✔ Sprawdź wynik” — Mentor szuka w wyjściu oczekiwanych tekstów; pasek zmienia się na „✔ ZALICZONE AUTOMATYCZNIE”.",
        "Ta sama rzecz w terminalu: Mój projekt → „⌨ Otwórz terminal tutaj” → `python witaj.py`."],
        "wynik": "Na ekranie: „Dzień dobry!”, „Uczę się vibe codingu.”, „2 + 3 = 5”; zadanie zaliczone automatycznie."},
    jak_uruchomic=["Środowisko → „⬇ Zainstaluj brakujące” → „✔ Sprawdź działanie”.", "Zadanie → „▶ Uruchom” albo terminal: `python witaj.py`."],
    cwiczenia=[
        C("prowadzone",
          "Co wypisze ten program? Wpisz trzy linie wyniku osobno.\n\n" + kod("python_uruchamianie:c1",
                                                                              "print(\"Pod Lipą\")\nprint(\"Noclegi:\", 4 * 2)\nprint(\"Cena\", 120, \"zł\")\n",
                                                                              "Pod Lipą\nNoclegi: 8\nCena 120 zł\n") +
          "\nCzas: 15 minut. Potem sprawdź, uruchamiając kod (wklej do dowolnego pliku .py w PRACA).",
          "Linia 1: Pod Lipą; linia 2: Noclegi: 8; linia 3: Cena 120 zł.",
          ["print wypisuje to, co w cudzysłowie, dokładnie (bez cudzysłowów).", "4 * 2 Python oblicza przed wypisaniem.", "Elementy oddzielone przecinkiem print łączy pojedynczą spacją."],
          "Pod Lipą / Noclegi: 8 / Cena 120 zł — print łączy argumenty spacją i oblicza 4 * 2 = 8.",
          [tx("l1", "Linia 1", ["Pod Lipą"]), tx("l2", "Linia 2", ["Noclegi: 8"], bledy=[bl("Noclegi: 4 * 2", "Python najpierw oblicza 4 * 2 — wypisuje wynik, nie działanie")]),
           tx("l3", "Linia 3", ["Cena 120 zł"])]),
        C("samodzielne",
          "Uruchamiasz `python wiat.py` i widzisz: `python: can't open file 'C:\\...\\PRACA\\wiat.py': [Errno 2] No such file or directory`. Plik nazywa się `witaj.py`. "
          "Jaki jest numer błędu (Errno) i co poprawisz? Druga sytuacja: „▶ Uruchom” pokazuje komunikat o braku interpretera — do której zakładki Mentora idziesz? Czas: 15 minut.",
          "Errno 2 — brak pliku o podanej nazwie (literówka: wiat.py zamiast witaj.py) → `python witaj.py`. Brak interpretera → zakładka Środowisko.",
          ["Przeczytaj komunikat do końca — jest w nim numer i opis.", "Porównaj nazwę w komendzie z nazwą w `dir`.", "Interpreter instaluje i sprawdza zakładka, w której był przycisk „Zainstaluj brakujące”."],
          "Errno 2 („No such file or directory”) = nie ma pliku o tej nazwie → popraw nazwę: `python witaj.py`. Brak interpretera → Środowisko → Zainstaluj brakujące.",
          [li("errno", "Numer błędu Errno", 2), tx("komenda", "Poprawiona komenda", ["python witaj.py"]),
           wy("zakladka", "Zakładka Mentora przy braku interpretera", ["Środowisko", "Dziennik", "Quiz", "Asystent"], "Środowisko")]),
    ],
    typowe_bledy=[
        B("Instalacja środowiska kończy się błędem pobierania.", "Brak internetu, zapora sieciowa lub chwilowa awaria serwera.", "Środowisko → „Pokaż szczegóły (pełny log)”.", "Sprawdź połączenie i kliknij „Ponów”; w sieci firmowej poproś administratora o dostęp do pypi.org."),
        B("„SyntaxError: unterminated string literal”.", "Brak zamykającego cudzysłowu.", "Linia wskazana w komunikacie — policz cudzysłowy.", "Każdy napis ma cudzysłów otwierający i zamykający tego samego rodzaju."),
        B("Okno wyniku pokazuje „Program pyta o więcej danych, niż podaje test”.", "W kodzie jest input(), a test nie podał wszystkich odpowiedzi.", "Czy zadanie wymaga input()?", "Wpisz dane w polu „Dane dla input()” (jedna linia = jedna odpowiedź) albo usuń zbędne input()."),
    ],
    pulapki=["Nie instaluj Pythona „na wszelki wypadek” z kilku źródeł naraz — Mentor używa swojego środowiska kursu; inne wersje w systemie są w porządku, ale terminal otwieraj przyciskiem Mentora.",
             "Polskie znaki w programie działają (Mentor uruchamia Pythona w trybie UTF-8); jeśli w zwykłym CMD widzisz krzaczki, to kwestia terminala, nie programu."],
    zadania=["Zmień przykład tak, żeby wypisał Twoje imię i wynik 7 * 24.", "Uruchom ten sam plik przyciskiem i z terminala.", "Zapisz w dzienniku różnicę między „Uruchom” a „Sprawdź wynik”."],
    pytania=[["Po co kursowi osobne środowisko .venv?", "Żeby wersje bibliotek były takie same u wszystkich i nie psuły innych programów; testy działają powtarzalnie."],
             ["Czym różni się „Uruchom” od „Sprawdź wynik”?", "Uruchom tylko wykonuje program; Sprawdź wynik porównuje wynik z oczekiwanym albo uruchamia niezależne testy z paczki."],
             ["Co robi print(\"a\", 1 + 1)?", "Wypisuje `a 2` — oblicza 1 + 1 i łączy elementy spacją."]],
    podsumowanie="Masz środowisko kursu, uruchamiasz programy przyciskiem i w terminalu, czytasz komunikat „No such file” i wiesz, że zaliczenie daje „Sprawdź wynik”.",
    test=[T("Co robi interpreter Pythona?", ["Pisze kod za Ciebie", "Wykonuje polecenia z pliku .py", "Instaluje Windows", "Tłumaczy na angielski"], 1, "Interpreter wykonuje kod."),
          T("Co wypisze `print(\"Suma:\", 3 + 4)`?", ["Suma: 3 + 4", "Suma: 7", "Suma:7", "7"], 1, "Najpierw obliczenie, potem wypisanie ze spacją."),
          T("Gdzie instalujesz środowisko kursu?", ["Zakładka Środowisko", "Panel sterowania Windows", "Sklep Microsoft", "Asystent"], 0, "„Zainstaluj brakujące” za Twoją zgodą."),
          T("Kiedy zadanie jest zaliczone automatycznie?", ["Gdy plik istnieje", "Gdy „Sprawdź wynik” daje zielony wynik", "Gdy agent napisze „gotowe”", "Po 24 godzinach"], 1, "Sam plik to dopiero „wymaga sprawdzenia”.")],
    w_praktyce=["Każdy kod od AI uruchamiasz od razu — nie zbieraj „na później” 5 nieprzetestowanych plików.", "Gdy coś nie działa, najpierw czytasz komunikat błędu do końca."],
    zrodla=[Z_PY_TUT, ["Python — używanie Pythona w Windows (oficjalna dokumentacja)", "https://docs.python.org/3/using/windows.html", D],
            ["Python — venv: środowiska wirtualne (oficjalna dokumentacja)", "https://docs.python.org/3/library/venv.html", D]],
)

CZYTANIE_1 = L(
    id="czytanie_kodu_1", nazwa="Czytanie kodu 1: zmienne, napisy, liczby i warunki", tydzien=1,
    slowa=["zmienna", "napis", "liczba", "int", "float", "if", "else", "warunek", "input"],
    cel="Po tej lekcji czytasz krótki program ze zmiennymi, liczbami i warunkiem if/elif/else i przewidujesz, co wypisze — zanim go uruchomisz.",
    po_co="Agent pisze kod szybciej niż Ty czytasz — ale tylko czytając rozumiesz, czy zrobił to, o co prosiłeś. Czytanie jest ważniejsze niż pisanie.",
    wymagania=["Środowisko kursu zainstalowane (lekcja „Python: instalacja…”).", "Plik ćwiczeń: PRACA (dowolny .py do sprawdzania przewidywań)."],
    wyjasnienie=(
        "## Zmienna — etykieta na wartości\n"
        "`noce = 3` oznacza: zapamiętaj wartość 3 pod nazwą `noce`. Znak = w Pythonie to „przypisz”, nie „równa się”. Później `noce` w kodzie oznacza 3, dopóki ktoś nie przypisze nowej wartości.\n"
        "## Typy wartości, które spotkasz najczęściej\n"
        "| typ | przykład | uwaga |\n"
        "|---|---|---|\n"
        "| int (liczba całkowita) | `3`, `-10` | dzielenie `/` zawsze daje float: `7 / 2` → 3.5 |\n"
        "| float (liczba z kropką) | `120.0`, `0.9` | w kodzie kropka, nie przecinek; `0.1 + 0.2` daje 0.30000000000000004 — dlatego kwoty zaokrąglamy round(x, 2) |\n"
        "| str (napis) | `\"Pod Lipą\"` | `\"3\" + \"4\"` daje `\"34\"` (sklejenie), a `3 + 4` daje 7 |\n"
        "| bool (prawda/fałsz) | `True`, `False` | wynik porównań: `noce >= 7` |\n"
        "## Działania\n"
        "`+ - * /` jak w matematyce, `//` dzielenie całkowite (7 // 2 → 3), `%` reszta z dzielenia (7 % 2 → 1), `**` potęga. Kolejność jak w szkole: najpierw * i /, potem + i -; nawiasy zmieniają kolejność.\n"
        "## f-string — napis z wstawionymi wartościami\n"
        "`f\"Koszt: {koszt} zł\"` — litera f przed cudzysłowem i zmienne w klamrach. `{koszt:.2f}` wypisze liczbę z dwoma miejscami po przecinku (kropką).\n"
        "## input — dane od użytkownika\n"
        "`imie = input(\"Imię: \")` czeka, aż użytkownik coś wpisze, i ZAWSZE zwraca napis. Żeby liczyć, trzeba zamienić: `noce = int(input(\"Noce: \"))`. "
        "To jedno z najczęstszych źródeł błędów w kodzie początkujących — i w kodzie AI, gdy prośba była niejasna.\n"
        "## Warunek if / elif / else\n"
        "Kod wcięty pod `if` wykonuje się tylko, gdy warunek jest prawdziwy. `elif` to „w przeciwnym razie, jeśli…”, `else` — „we wszystkich pozostałych przypadkach”. "
        "Python sprawdza od góry i wykonuje PIERWSZY pasujący blok — kolejność warunków ma znaczenie. Wcięcie (4 spacje) jest częścią składni: pokazuje, co należy do bloku.\n"
        "| porównanie | znaczy |\n"
        "|---|---|\n"
        "| `==` | równe (dwa znaki =!) |\n"
        "| `!=` | różne |\n"
        "| `<`, `<=`, `>`, `>=` | mniejsze, mniejsze lub równe… |\n"
        "| `and`, `or`, `not` | i, lub, nie |\n"
        "## Jak czytać kod jak recenzent\n"
        "- Idź linia po linii i zapisuj na kartce wartości zmiennych (tzw. „śledzenie”).\n"
        "- Przy każdym if zapytaj: co się stanie na granicy (np. dokładnie 7 nocy)?\n"
        "- Przewiduj wynik, potem uruchom. Różnica między przewidywaniem a wynikiem to dokładnie to, czego się uczysz."),
    przyklad=kod("czytanie_kodu_1:przyklad",
                 "noce = 7\nosoby = 2\ncena = 120\n\nkoszt = noce * osoby * cena\nif noce >= 7:\n    koszt = koszt * 0.9\n    print(\"Rabat 10% za długi pobyt\")\nelse:\n    print(\"Bez rabatu\")\n\nprint(f\"Do zapłaty: {koszt:.2f} zł\")\n",
                 "Rabat 10% za długi pobyt\nDo zapłaty: 1512.00 zł\n"),
    demonstracja={"tytul": "Śledzenie programu z rabatem — linia po linii", "kroki": [
        "Linie 1–3: trzy zmienne: noce = 7, osoby = 2, cena = 120 (wszystkie int).",
        "Linia 5: koszt = 7 * 2 * 120 = 1680 (int).",
        "Linia 6: warunek noce >= 7 → 7 >= 7 → True (granica WCHODZI, bo >=). Wykonują się dwie wcięte linie: koszt = 1680 * 0.9 = 1512.0 (teraz float) i wypisanie „Rabat 10% za długi pobyt”.",
        "Blok else jest pomijany, bo pierwszy warunek był prawdziwy.",
        "Ostatnia linia: f-string z {koszt:.2f} → „Do zapłaty: 1512.00 zł”.",
        "Zmień noce = 6 i przewidź wynik przed uruchomieniem: 6 * 2 * 120 = 1440, warunek False → „Bez rabatu”, „Do zapłaty: 1440.00 zł”. Gdyby w warunku było > zamiast >=, 7 nocy nie dostałoby rabatu — to typowy błąd granicy."],
        "wynik": "Rabat 10% za długi pobyt / Do zapłaty: 1512.00 zł; po zmianie na 6 nocy: Bez rabatu / Do zapłaty: 1440.00 zł."},
    jak_uruchomic=["Wklej przykład do pliku `rabat.py` w PRACA → zadanie z paskiem albo terminal `python rabat.py`.", "Przewiduj wynik ZANIM uruchomisz — zapisz go w dzienniku."],
    cwiczenia=[
        C("prowadzone",
          "Przewidź wynik (najpierw na kartce, potem uruchom):\n\n" + kod("czytanie_kodu_1:c1",
                                                                       "osoby = 3\nnoce = 2\nkoszt = osoby * noce * 100\nif koszt > 500:\n    print(\"Duża rezerwacja\")\nelif koszt > 300:\n    print(\"Średnia rezerwacja\")\nelse:\n    print(\"Mała rezerwacja\")\nprint(koszt)\n",
                                                                       "Duża rezerwacja\n600\n") +
          "\nWpisz pierwszą linię wyniku i wartość koszt. Czas: 15 minut.",
          "Linia 1: Duża rezerwacja; koszt: 600.",
          ["Policz koszt: 3 * 2 * 100.", "Sprawdź warunki od góry: czy 600 > 500?", "Python wykonuje pierwszy pasujący blok, resztę pomija."],
          "koszt = 3 * 2 * 100 = 600; 600 > 500 → True → „Duża rezerwacja” (elif nie jest już sprawdzany); potem print(koszt) → 600.",
          [tx("l1", "Pierwsza linia wyniku", ["Duża rezerwacja"], bledy=[bl("Średnia rezerwacja", "600 > 300 to prawda, ale Python wykonuje PIERWSZY pasujący blok — 600 > 500 sprawdza wcześniej")]),
           li("koszt", "Wartość koszt", 600)]),
        C("samodzielne",
          "AI napisało fragment:\n\n" + kod("czytanie_kodu_1:c2",
                                             "noce = input(\"Ile nocy? \")\nprint(noce * 2)\n",
                                             None) +
          "\nUżytkownik wpisuje 3. Co wypisze program (bez spacji, dokładnie)? Jak poprawisz pierwszą linię, żeby wynik był 6? Czas: 20 minut.",
          "Wypisze 33 (napis „3” powtórzony 2 razy). Poprawka: noce = int(input(\"Ile nocy? \")) — wtedy 3 * 2 = 6.",
          ["Jakiego typu jest wartość zwrócona przez input()?", "Napis pomnożony przez 2 to… dwa razy ten sam napis.", "Zamiana napisu na liczbę całkowitą: funkcja int()."],
          "input() zwraca napis „3”; „3” * 2 = „33” (powtórzenie napisu). Poprawka: noce = int(input(\"Ile nocy? \")) → 6.",
          [tx("wynik", "Co wypisze program po wpisaniu 3?", ["33"], bledy=[bl("6", "input() zwraca NAPIS — napis razy 2 to powtórzenie, nie mnożenie")]),
           tx("fix", "Poprawiona pierwsza linia", ["noce = int(input(\"Ile nocy? \"))"], zawiera=["noce=int(input("])]),
    ],
    typowe_bledy=[
        B("„TypeError: can only concatenate str (not \"int\") to str”.", "Sklejasz napis z liczbą: \"Koszt: \" + 100.", "Która linia? Jakie typy po obu stronach +?", "Użyj f-stringa: f\"Koszt: {koszt}\" albo str(koszt)."),
        B("„IndentationError: expected an indented block”.", "Po if/else brakuje wciętej linii albo wcięcia są niespójne.", "Linia pod if — czy ma 4 spacje?", "Wcięcie 4 spacje pod każdym if/elif/else; nie mieszaj tabulatora ze spacjami."),
        B("„SyntaxError: invalid syntax” przy `if noce = 7:`.", "Pojedyncze = to przypisanie; porównanie to ==.", "Szukaj = w warunku.", "`if noce == 7:`"),
    ],
    pulapki=["Granice warunków (> czy >=) to miejsce, gdzie AI i ludzie mylą się najczęściej. Zawsze testuj wartość dokładnie na granicy.",
             "0.1 + 0.2 nie daje dokładnie 0.3 — przy pieniądzach zaokrąglaj round(x, 2) albo licz w groszach (int)."],
    zadania=["Zmień w przykładzie rabat na 15% od 10 nocy i przewidź wynik dla 10 nocy.", "Napisz (sam albo z czatem AI) 3 linie z input() i int(), które liczą koszt dla wpisanej liczby nocy.", "Znajdź w kodzie z tej lekcji wszystkie miejsca, gdzie typ zmiennej się zmienia."],
    pytania=[["Co zwraca input()?", "Zawsze napis (str); liczbę trzeba zamienić int() lub float()."],
             ["Dlaczego kolejność warunków if/elif ma znaczenie?", "Python wykonuje pierwszy pasujący blok i pomija resztę."],
             ["Co wypisze print(f\"{2/3:.2f}\")?", "0.67"]],
    podsumowanie="Czytasz zmienne, typy, działania, f-stringi, input i warunki; przewidujesz wynik linia po linii i sprawdzasz granice warunków.",
    test=[T("Co wypisze `print(\"3\" + \"4\")`?", ["7", "34", "3 4", "Błąd"], 1, "Napisy się sklejają."),
          T("Ile wynosi `7 // 2`?", ["3.5", "3", "4", "1"], 1, "// to dzielenie całkowite."),
          T("Dla noce = 7 warunek `noce > 7` jest:", ["True", "False", "Błędem", "Zależy od osób"], 1, "7 nie jest większe od 7 — granica nie wchodzi."),
          T("Jak zamienić napis z input() na liczbę całkowitą?", ["str()", "int()", "print()", "round()"], 1, "int(\"3\") → 3.")],
    w_praktyce=["Przy każdym if od AI zapytaj: co na granicy?", "Kwoty zawsze z zaokrągleniem do groszy."],
    zrodla=[Z_PY_TUT, ["Python tutorial — 3. An Informal Introduction to Python (liczby, napisy)", "https://docs.python.org/3/tutorial/introduction.html", D],
            ["Python tutorial — 4.1 if Statements", "https://docs.python.org/3/tutorial/controlflow.html", D]],
)
