# -*- coding: utf-8 -*-
"""Lekcja wprowadzająca — pierwsza na liście. Tłumaczy, jak uczyć się z tego programu i z aplikacji Mentor."""

LEKCJA_START = {
    "id": "start_jak_sie_uczyc", "tydzien": 0, "czas_min": 15,
    "nazwa": "Start: jak uczyć się z tego programu (przeczytaj najpierw)",
    "cel": "wiesz, co robić każdego dnia, gdzie co jest w Mentorze, jak czytać lekcję i jak odhaczać postępy.",
    "slowa": ["jak zacząć", "jak zaczac", "od czego zacząć", "start", "wprowadzeni", "jak się uczyć", "jak sie uczyc", "jak działa program", "jak dziala program", "mentor"],
    "wyjasnienie":
        "## Co to za kurs i dla kogo\n"
        "12 tygodni (0–11), pięć zadań tygodniowo, jedna krótka lekcja dziennie. Uczysz się na fikcyjnej firmie AGRO-MLEKO RADZYŃ (62 pracowników, produkcja "
        "3-zmianowa, zleceniobiorcy, umowy o dzieło) — każdy kazus, lista płac i pismo dotyczą jej pracowników. Nie musisz znać prawa pracy ani księgowości. "
        "Potrzebujesz: 60–90 minut dziennie i jednego folderu na dysku. Nic więcej — kalkulatory, symulatory ZUS/US i przepisy są wbudowane w Mentora (zakładka Warsztat).\n"
        "## Jak wygląda dzień nauki\n"
        "- Panel → karta „Dzisiaj”: Mentor pokazuje zadanie dnia i lekcję do niego (pon–czw zadania 1–4, piątek — większe zadanie tygodnia, sobota — quiz, niedziela — wolne).\n"
        "- Lekcje → czytasz lekcję dnia (15–25 min). Zawsze ta sama budowa: cel, wyjaśnienie, przykład liczbowy, pułapki, 3 zadania, pytania, test.\n"
        "- Plan → zadanie dnia → rozwijasz „Jak to zrobić”: kompletne kroki (co otworzyć, co policzyć, jak nazwać plik). Robisz je w swoim katalogu projektu.\n"
        "- Sesja nauki → timer prowadzi Cię przez 4 fazy (nowy temat 20 min → kazus w Warsztacie 50 → weryfikacja u źródła 15 → wpis do dziennika 5) i sam zapisuje czas.\n"
        "- Plan → zaznaczasz ✔ przy zadaniu (+10 XP; zadanie tygodnia +25). Dziennik → jedno zdanie, czego się nauczyłeś (+3 XP).\n"
        "- Sobota: Quiz tygodnia (5 pytań). Po każdym etapie: Checklista — co masz umieć, odhaczasz sam.\n"
        "## Wszystko w Mentorze: Warsztat\n"
        "Kurs nie wymaga żadnych kont zewnętrznych, instalowania programów ani arkusza kalkulacyjnego. Zakładka Warsztat ma 9 narzędzi: Firma ćwiczeniowa (12 osób z danymi), Lista płac (brutto → netto krok po kroku, z „Trybem ćwiczenia”), Zasiłki i chorobowe, Urlopy i ekwiwalent, Czas pracy, Potrącenia, eZUS / Płatnik (symulator zgłoszeń, kompletów DRA/RCA/RSA, e-ZLA — z weryfikacją i numerami UPP), e-Urząd: PIT (PIT-11, PIT-4R, UPO) i Przepisy (48 streszczeń offline). Każde narzędzie ma przycisk „Zapisz do projektu” — wynik trafia do Twojego katalogu jako plik .md/.csv. Zasada: najpierw liczysz na kartce, potem sprawdzasz w Warsztacie.\n"
        "## Twój warsztat: katalog projektu\n"
        "Folder „kadry-praktyka” (nazwę proponuje Mentor; wskazujesz go w Ustawieniach lub w zakładce Mój projekt). Trafiają tam: FIRMA.md (karta firmy — "
        "zadanie 1 tygodnia 0), dziennik.md (Twoje notatki), listy płac i dokumenty ZUS/PIT zapisane z Warsztatu (.md/.csv), pisma w plikach .md. Mentor wykrywa te pliki i podpowiada, czy zadanie "
        "ma już efekt. Git jest opcjonalny — zadanie tygodnia 0 pokaże, jak zapisywać wersje; jeśli nie chcesz, pomijasz „commit” w krokach.\n"
        "## Jak czytać lekcję (5 kroków, ok. 20 minut)\n"
        "- 1. Cel — zdanie „po tej lekcji potrafisz…”. Jeśli już to umiesz, przejdź od razu do testu.\n"
        "- 2. Wyjaśnienie — czytaj z otwartym ISAP (isap.sejm.gov.pl) i sprawdzaj wymienione artykuły; nie zapamiętuj wszystkiego — ściąga i słowniczek są w aplikacji.\n"
        "- 3. Przykład — zakryj wynik i przelicz sam na kartce, potem sprawdź w Warsztacie. Dopiero potem porównaj z wynikiem w lekcji. To najważniejszy krok.\n"
        "- 4. Pułapki — przepisz do dziennika jednym zdaniem; to są błędy, za które płaci się w kontroli.\n"
        "- 5. Zadania i pytania — zadania robisz w katalogu projektu (bez rozwiązań w lekcji — pyta się Asystenta o podpowiedź), pytania mówisz na głos i rozwijasz odpowiedź; test 3 pytań: 2/3 zalicza, możesz powtarzać.\n"
        "## Asystent — nauczyciel, nie wykonawca\n"
        "Zakładka Asystent ma trzy karty: Subskrypcja (Claude Code w terminalu), API (własny klucz, rozmowa w Mentorze) i Offline (wbudowany, bez internetu — "
        "rozumie: „uczę się [temat]”, „co to jest [pojęcie]”, „zadaj mi 3 pytania”, „quiz z tygodnia 4”, „odpytaj mnie jak rekruter”, „utknąłem: [problem]”). "
        "Zasada we wszystkich trybach: najpierw 15 minut własnej pracy, potem pytanie o podpowiedź — nigdy o gotowy wynik. Gotowe prompty do każdej sytuacji: zakładka Prompty.\n"
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
        "Jutro: Panel pokaże zadanie 2 (eZUS, e-Urząd, Płatnik) i lekcję „Narzędzia kadrowca”.",
    "zadania": ["Otwórz po kolei każdą zakładkę w pasku bocznym i zapisz w dziennik.md jednym zdaniem, do czego służy.",
                "W Ustawieniach wpisz imię i wskaż katalog projektu; w zakładce Mój projekt sprawdź, czy Mentor go widzi.",
                "Uruchom Sesję nauki, odczekaj 2 minuty i zatrzymaj — zobacz na Panelu, że czas i seria się zapisały."],
    "pytania": [["Gdzie sprawdzisz, co masz dziś zrobić?", "Panel → karta „Dzisiaj” — zadanie dnia, przycisk „Jak to zrobić” i lekcja."],
                ["Co robisz z przykładem w lekcji?", "Zakrywam wynik i liczę sam (kalkulator/arkusz), dopiero potem porównuję."],
                ["Kiedy odhaczasz zadanie w Planie?", "Gdy efekt (plik, arkusz, pismo) jest w katalogu projektu i działa — nie po samym przeczytaniu."]],
    "pulapki": ["Czytanie wszystkich lekcji naraz bez zadań — po tygodniu nic nie zostaje. Jedna lekcja + jedno zadanie dziennie.",
                "Pomijanie testu lekcji — to 2 minuty i jedyny sygnał, że temat „siedzi”; Mentor zaznacza ✔ dopiero po 2/3."],
    "test": [
        {"p": "Ile zadań ma każdy tydzień i które jest „zadaniem tygodnia”?", "o": ["3 — ostatnie", "5 — piąte (piątek), większe, +25 XP", "7 — po jednym dziennie", "Zależy od tygodnia"], "odp": 1, "w": "Zadania 1–4 to pon–czw, zadanie 5 to piątek."},
        {"p": "Gdzie znajdziesz kompletną instrukcję wykonania zadania?", "o": ["W lekcji", "Plan → zadanie → „Jak to zrobić”", "W Ściądze", "W Dzienniku"], "odp": 1, "w": "Lekcja tłumaczy temat; Plan mówi, co dokładnie zrobić."},
        {"p": "Na czym polega zasada pracy z Asystentem?", "o": ["Prosisz o gotowy wynik i przepisujesz", "Najpierw 15 min własnej pracy, potem pytanie o podpowiedź", "Używasz tylko w sobotę", "Asystent odhacza zadania"], "odp": 1, "w": "Asystent uczy, nie wyręcza — także w trybie offline."},
    ],
}
