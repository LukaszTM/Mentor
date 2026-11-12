# -*- coding: utf-8 -*-
"""Lekcja wprowadzająca — pierwsza na liście. Tłumaczy, jak uczyć się z tego programu i z aplikacji Mentor."""

LEKCJA_START = {
    "id": "start_jak_sie_uczyc", "tydzien": 0, "czas_min": 15,
    "nazwa": "Start: jak uczyć się z tego programu (przeczytaj najpierw)",
    "cel": "wiesz, co robić każdego dnia, gdzie co jest w Mentorze, jak czytać lekcję i jak odhaczać postępy.",
    "slowa": ["jak zacząć", "jak zaczac", "od czego zacząć", "start", "wprowadzeni", "jak się uczyć", "jak sie uczyc", "jak działa program", "jak dziala program", "mentor"],
    "wyjasnienie":
        "## Co to za kurs i dla kogo\n"
        "16 tygodni (0–15), trzy–cztery zadania tygodniowo, jedna lekcja (ok. godziny) co drugi dzień. Uczysz się na fikcyjnej firmie AGRO-MLEKO (62 pracowników, produkcja "
        "3-zmianowa, zleceniobiorcy, umowy o dzieło) — każdy kazus, lista płac i pismo dotyczą jej pracowników. Nie musisz znać prawa pracy ani księgowości. "
        "Poziom: od podstaw (nie musisz znać prawa pracy, księgowości ani Excela). Potrzebujesz: ok. 90 minut dziennie od poniedziałku do piątku i do 90 minut w sobotę (quiz, powtórka, dokończenie zadania) — każdy tydzień mieści się w 9 godzinach, cały kurs to ok. 130 godzin; do tego Windows z Mentorem i jeden folder na dysku. Nic więcej — kalkulatory, symulatory ZUS/US, przepisy i wszystkie pliki ćwiczeń są w Mentorze i w paczce materiałów (kopiujesz je jednym przyciskiem). Internet nie jest potrzebny; Asystent w trybie offline działa bez konta i bez opłat (tryby API/Subskrypcja są opcjonalne i płatne).\n"
        "## Co będziesz umieć po kursie\n"
        "- zawrzeć i rozwiązać umowę o pracę z kompletem dokumentów i w terminach (ZUA, świadectwo, ekwiwalent),\n"
        "- policzyć wymiar czasu pracy, nadgodziny, nocne, urlop i pensję za część miesiąca,\n"
        "- sporządzić listę płac od brutto do netto z PPK, chorobowym, zasiłkiem, benefitem, delegacją i potrąceniem — i skontrolować ją bilansem,\n"
        "- ustalić podstawę zasiłku, rozliczyć zleceniobiorcę i studenta, przygotować komplet DRA/RCA/RSA i korektę,\n"
        "- zamknąć rok (PIT-4R, PIT-11, ZFŚS, PFRON) i przygotować firmę do kontroli PIP/ZUS z procedurami 2026/2027.\n"
        "## Jak wygląda dzień nauki\n"
        "- Panel → karta „Dzisiaj”: Mentor pokazuje zadanie dnia i lekcję do niego (pon–pt zadania tygodnia i lekcje na przemian, sobota — quiz, powtórka i dokończenie, niedziela — wolne).\n"
        "- Lekcje → czytasz lekcję (ok. 45–75 min z ćwiczeniami; czas podany przy każdej lekcji jest policzony z jej treści). Zawsze ta sama budowa: cel → po co → czego potrzebujesz → wyjaśnienie od podstaw → demonstracja omówiona krok po kroku → jak to uruchomić → ćwiczenie prowadzone → ćwiczenie samodzielne (3 podpowiedzi, potem rozwiązanie) → typowe błędy → sprawdzenie → test.\n"
        "- Plan → zadanie dnia → rozwijasz „Jak to zrobić”: kompletne kroki (co otworzyć, co policzyć, jak nazwać plik). Robisz je w swoim katalogu projektu.\n"
        "- Sesja nauki → timer prowadzi Cię przez 4 fazy (nowy temat 20 min → kazus w Warsztacie 50 → weryfikacja u źródła 15 → wpis do dziennika 5) i sam zapisuje czas.\n"
        "- Plan → zaznaczasz ✔ przy zadaniu (+10 XP; zadanie tygodnia +25). Dziennik → jedno zdanie, czego się nauczyłeś (+3 XP).\n"
        "- Sobota: Quiz tygodnia (4–5 pytań) i powtórka. Po każdym etapie: Checklista — co masz umieć, odhaczasz sam.\n"
        "## Wszystko w Mentorze: Warsztat\n"
        "Kurs nie wymaga żadnych kont zewnętrznych, instalowania programów ani arkusza kalkulacyjnego. Zakładka Warsztat ma 10 narzędzi: Firma ćwiczeniowa (12 osób z danymi), Lista płac (brutto → netto krok po kroku, z „Trybem ćwiczenia”), Zasiłki i chorobowe, Urlopy i ekwiwalent, Czas pracy, Potrącenia, Delegacje i diety, eZUS / Płatnik (symulator zgłoszeń, kompletów DRA/RCA/RSA, e-ZLA — z weryfikacją i numerami UPP), e-Urząd: PIT (PIT-11, PIT-4R, UPO) i Przepisy (48 streszczeń offline). Każde narzędzie ma przycisk „Zapisz do projektu” — wynik trafia do Twojego katalogu jako plik .md/.csv. Zasada: najpierw liczysz na kartce, potem sprawdzasz w Warsztacie.\n"
        "## Twój warsztat: katalog projektu\n"
        "Folder „kadry-praktyka” (nazwę proponuje Mentor; wskazujesz go w Ustawieniach lub w zakładce Mój projekt). Trafiają tam: FIRMA.md (karta firmy — "
        "zadanie 1 tygodnia 0), dziennik.md (Twoje notatki), listy płac i dokumenty ZUS/PIT zapisane z Warsztatu (.md/.csv), pisma w plikach .md. Mentor wykrywa te pliki i podpowiada, czy zadanie "
        "ma już efekt. Git jest opcjonalny — zadanie tygodnia 0 pokaże, jak zapisywać wersje; jeśli nie chcesz, pomijasz „commit” w krokach.\n"
        "## Jak czytać lekcję (7 kroków, 20–40 minut)\n"
        "- 1. Cel i „po co mi to” — jeśli już to umiesz, zrób od razu ćwiczenie samodzielne i test.\n"
        "- 2. Wyjaśnienie od podstaw — każde pojęcie jest objaśnione w lekcji; przepisy sprawdzasz w Warsztat → Przepisy (ISAP tylko dla pogłębienia).\n"
        "- 3. Demonstracja — kompletny przykład z omówieniem każdego kroku; zakryj wynik, przelicz sam, potem porównaj. To najważniejszy krok.\n"
        "- 4. Jak to uruchomić — dokładne kliknięcia w Warsztacie lub plik z paczki materiałów i oczekiwany wynik.\n"
        "- 5. Ćwiczenie prowadzone (podobne do demonstracji) i samodzielne (wymaga decyzji) — każde ma 3 stopniowane podpowiedzi (pytanie → gdzie szukać → częściowy przykład) i pełne rozwiązanie na końcu; plik startowy jest w cwiczenia/, rozwiązanie w rozwiazania/.\n"
        "- 6. Typowe błędy i pułapki — przepisz jeden do dziennika; to są błędy, za które płaci się w kontroli.\n"
        "- 7. Sprawdzenie i test — pytania mówisz na głos, potem test 3 pytań: 2/3 zalicza, możesz powtarzać.\n"
        "## Asystent — nauczyciel, nie wykonawca\n"
        "Zakładka Asystent ma trzy karty: Subskrypcja (Claude Code w terminalu), API (własny klucz, rozmowa w Mentorze) i Offline (wbudowany, bez internetu — "
        "rozumie: „uczę się [temat]”, „co to jest [pojęcie]”, „zadaj mi 3 pytania”, „quiz z tygodnia 4”, „odpytaj mnie jak rekruter”, „utknąłem: [problem]”). "
        "Zasada we wszystkich trybach: najpierw własna próba (podpowiedzi w lekcji odkrywasz po kolei), potem pytanie o podpowiedź — nie o gotowy wynik; gdy nie wiesz nawet, jak zacząć, pytaj od razu — nie ma obowiązku „walczyć” przez określony czas. W trybie offline działa też komenda „podpowiedź” (kolejna wskazówka do ćwiczenia z ostatniej lekcji). Gotowe prompty do każdej sytuacji: zakładka Prompty.\n"
        "## Skąd liczby i czy są aktualne\n"
        "Stan prawny: listopad 2026. Każda stawka, limit i termin ma w lekcji podstawę prawną (artykuł, Dz.U., obwieszczenie). To, co jest dopiero projektem "
        "(np. pełna jawność wynagrodzeń, PIT 2027), jest tak oznaczone. Raz w roku — w styczniu — odświeżasz tabelę wskaźników (zadanie 4 tygodnia 0 "
        "pokazuje, gdzie sprawdzić każdą liczbę). Umiejętność sprawdzania u źródła jest ważniejsza niż zapamiętanie kwoty.\n"
        "## Jeśli coś nie idzie\n"
        "- Nie wiesz, co dziś robić → Panel → „Dzisiaj”.\n"
        "- Nie rozumiesz lekcji → przelicz przykład, zapytaj Asystenta „wytłumacz [temat] inaczej”, zapisz pytanie w Dzienniku, zrób zadanie dnia i wróć do lekcji jutro.\n"
        "- Brak czasu → Ustawienia → skala sesji 50% (45 min) albo wpisz czas ręcznie po nauce (z tematem i 3-pytaniowym testem). 30 minut codziennie bije 3 godziny raz w tygodniu.\n"
        "- Przerwa w nauce → Panel pokaże, ile dni minęło i od czego zacząć; XP i odznaki zostają.\n"
        "- Chcesz inny program → Ustawienia → Program nauczania (postępy każdego programu zapisują się osobno).",
    "przyklad":
        "Dzień 1 krok po kroku (tydzień 0):\n"
        "1. Panel → „Dzisiaj”: zadanie „Katalog projektu i karta firmy ćwiczeniowej”.\n"
        "2. Lekcje → ta lekcja (15 min) → test 3 pytań.\n"
        "3. Plan → Tydzień 0 → zadanie 1 → „Jak to zrobić” (5 kroków): tworzysz folder kadry-praktyka, plik FIRMA.md, wskazujesz folder w Mentorze.\n"
        "4. Sesja nauki → start timera; fazy 2–3 to praca nad zadaniem i sprawdzenie.\n"
        "5. Plan → ✔ przy zadaniu 1 (+10 XP).  6. Dziennik → „Dziś: utworzyłem katalog i FIRMA.md; nie wiem jeszcze, co to PEL” (+3 XP).\n"
        "Jutro: Panel pokaże zadanie 2 (symulatory eZUS/Płatnika i e-Urzędu w Warsztacie) i lekcję „Narzędzia kadrowca”.",
    "zadania": ["Otwórz po kolei każdą zakładkę w pasku bocznym i zapisz w dziennik.md jednym zdaniem, do czego służy.",
                "W Ustawieniach wpisz imię i wskaż katalog projektu; w zakładce Mój projekt sprawdź, czy Mentor go widzi.",
                "Uruchom Sesję nauki, odczekaj 2 minuty i zatrzymaj — zobacz na Panelu, że czas i seria się zapisały."],
    "pytania": [["Gdzie sprawdzisz, co masz dziś zrobić?", "Panel → karta „Dzisiaj” — zadanie dnia, przycisk „Jak to zrobić” i lekcja."],
                ["Co robisz z przykładem w lekcji?", "Zakrywam wynik i liczę sam na kartce, potem sprawdzam w Warsztacie, dopiero potem porównuję."],
                ["Kiedy odhaczasz zadanie w Planie?", "Gdy efekt (plik z Warsztatu, pismo, tabela) jest w katalogu projektu i potrafię go wyjaśnić — nie po samym przeczytaniu."]],
    "pulapki": ["Czytanie wszystkich lekcji naraz bez zadań — po tygodniu nic nie zostaje. Jedna lekcja + jedno zadanie dziennie.",
                "Pomijanie testu lekcji — to 2 minuty i jedyny sygnał, że temat „siedzi”; Mentor zaznacza ✔ dopiero po 2/3."],
    "test": [
        {"p": "Ile zadań ma każdy tydzień i które jest „zadaniem tygodnia”?", "o": ["3 — ostatnie", "5 — piąte (piątek), większe, +25 XP", "7 — po jednym dziennie", "Zależy od tygodnia"], "odp": 1, "w": "Zadania 1–4 to pon–czw, zadanie 5 to piątek."},
        {"p": "Gdzie znajdziesz kompletną instrukcję wykonania zadania?", "o": ["W lekcji", "Plan → zadanie → „Jak to zrobić”", "W Ściądze", "W Dzienniku"], "odp": 1, "w": "Lekcja tłumaczy temat; Plan mówi, co dokładnie zrobić."},
        {"p": "Na czym polega zasada pracy z Asystentem?", "o": ["Prosisz o gotowy wynik i przepisujesz", "Najpierw własna próba i podpowiedzi po kolei, potem pytanie o wskazówkę — nie o wynik", "Używasz tylko w sobotę", "Asystent odhacza zadania"], "odp": 1, "w": "Asystent uczy, nie wyręcza — także w trybie offline; gdy nie wiesz, jak zacząć, pytasz od razu."},
    ],
}
