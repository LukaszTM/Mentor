# -*- coding: utf-8 -*-
"""Etap 3, tygodnie 14–15: klient i wymagania, portfolio i praca, rozmowa rekrutacyjna; projekt końcowy (plan, wydanie), powtórka."""

from wspolne import (TN, B, C, L, T, bl, kod, kw, li, tx, wy)
from etap3 import D2, Z_GH_README, Z_LIC

Z_ATL_US = ["Atlassian — User stories: przykłady i szablon (tłumaczenie robocze)", "https://www.atlassian.com/agile/project-management/user-stories", D2]
Z_ATL_AC = ["Atlassian — Acceptance criteria", "https://www.atlassian.com/work-management/project-management/acceptance-criteria", D2]
Z_NIEREJ = ["Działalność nierejestrowana 2026: limit 10 813,50 zł (money.pl)", "https://direct.money.pl/artykuly/porady/dzialalnosc-nierejestrowana-2026-limit-10-813,50-zl,-po-przekroczeniu-7-dni-na-ceidg", D2]
Z_SO = ["Stack Overflow Developer Survey 2025 — AI (zaufanie, vibe coding w pracy zawodowej)", "https://survey.stackoverflow.co/2025/ai", "dostęp 19.11.2026"]
Z_GH_PROFILE = ["GitHub Docs — Managing your profile README", "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme", D2]
Z_GH_PIN = ["GitHub Docs — Pinning items to your profile", "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile", D2]
Z_STAR = ["MIT Career Advising — The STAR method for behavioral interviews", "https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/", D2]
Z_SEMVER = ["Semantic Versioning 2.0.0 (semver.org, wersja polska)", "https://semver.org/lang/pl/", D2]
Z_KEEPCL = ["Keep a Changelog (wersja polska)", "https://keepachangelog.com/pl/1.1.0/", D2]
Z_GH_REL = ["GitHub Docs — About releases (tagi i wydania)", "https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases", D2]
Z_CC_BEST = ["Claude Code — Best practices", "https://code.claude.com/docs/en/best-practices", "dostęp 19.11.2026"]
Z_RETRO = ["Atlassian — Retrospektywa: jak ją przeprowadzić", "https://www.atlassian.com/team-playbook/plays/retrospective", D2]


# =========================================================================== TYDZIEŃ 14
KLIENT = L(
    id="wymagania_klienta", nazwa="Praca z klientem: od maila do wymagań, wyceny i odbioru", tydzien=14,
    slowa=["klient", "wymagania", "historyjka", "kryteria akceptacji", "wycena", "zakres", "odbiór", "umowa"],
    cel="Po tej lekcji zamieniasz nieprecyzyjny mail klienta w historyjki użytkownika z kryteriami akceptacji, listę pytań i zakres „poza projektem”, przygotowujesz wycenę z buforem i plan odbioru.",
    po_co="Najczęstsza przyczyna konfliktów z klientem to niejasny zakres, nie zły kod. Agent przyspiesza pisanie kodu — ale nie zrozumie za Ciebie, czego klient naprawdę potrzebuje.",
    wymagania=["Lekcja „Specyfikacja” (tydzień 3).", "Plik pomoc/brief_klienta.md z materiałów (zadanie tygodnia)."],
    wyjasnienie=(
        "## Historyjka użytkownika\n"
        "Format: „Jako [kto] chcę [co], aby [po co]”. Pod nią kryteria akceptacji — sprawdzalne zdania tak/nie. Przykład:\n"
        "„Jako gość chcę zobaczyć wolne pokoje w wybranych datach, aby zarezerwować pobyt bez dzwonienia.”\n"
        "- Dla dat 21–22.12 przy rezerwacji Lipowego 20–23.12 lista nie zawiera Lipowego.\n"
        "- Data wyjazdu przed datą przyjazdu → komunikat po polsku, brak listy.\n"
        "- Strona działa na telefonie o szerokości 375 px.\n"
        "## Od maila do wymagań — 5 kroków\n"
        "| krok | wynik |\n"
        "|---|---|\n"
        "| 1. Wypisz potrzeby z maila (rzeczowniki i czasowniki) | lista „co ma umieć” |\n"
        "| 2. Każdą zamień na historyjkę z 2–4 kryteriami | wymagania.md |\n"
        "| 3. Zaznacz niejasności | lista pytań do klienta |\n"
        "| 4. Ustal, czego NIE robisz | sekcja „Poza zakresem” |\n"
        "| 5. Priorytety: musi / powinno / może (MoSCoW) | kolejność pracy |\n"
        "Agent pomaga: „Na podstawie maila zaproponuj historyjki i 10 pytań o niejasności; nie zakładaj odpowiedzi”. Ty weryfikujesz i rozmawiasz z klientem.\n"
        "## Wycena\n"
        "- Rozbij pracę na zadania (historyjki + testy + README + wdrożenie + poprawki po odbiorze).\n"
        "- Szacuj godziny dla każdego, dodaj bufor 30–50% na nieznane (pierwsze projekty prawie zawsze się przeciągają).\n"
        "- Dolicz koszty: plan AI w czasie projektu, hosting, domena (płaci klient — zapisz to).\n"
        "- Wycena ryczałtowa = zakres musi być zamknięty; zmiany zakresu → osobna wycena (zapis w umowie).\n"
        "## Forma rozliczenia (Polska, w skrócie)\n"
        "Drobne zlecenia możesz rozliczać w działalności nierejestrowanej do 225% minimalnego wynagrodzenia na kwartał (2026: 10 813,50 zł); po przekroczeniu 7 dni na wpis do CEIDG. "
        "Inne formy: umowa o dzieło/zlecenie, własna działalność. Prawa autorskie i powierzenie danych — w umowie. To nie porada podatkowa — sprawdź aktualne przepisy lub zapytaj księgowego.\n"
        "## Odbiór\n"
        "Odbiór = przejście kryteriów akceptacji przy kliencie (lista z historyjek), nie „czy się podoba”. Po odbiorze: README, dostęp do repozytorium, instrukcja dla klienta, okres poprawek (np. 14 dni), co dalej z utrzymaniem (aktualizacje, koszty)."),
    przyklad=("Fragment maila klientki:\n„Chciałabym, żeby goście mogli sami sprawdzić, czy jest wolny pokój, i żeby nie dzwonili o ceny. Fajnie, jakby było też zdjęcia i może płatność online? I żeby działało na telefonie.”\n\n"
              "Z tego: US-1 wolne pokoje (musi), US-2 kalkulator ceny (musi), US-3 galeria (powinno), US-4 telefon (musi — jako kryterium dla wszystkich), "
              "płatność online → poza zakresem v1 (osobna wycena: operator płatności, regulamin, RODO). Pytania: ile pokoi, sezonowość cen, kto aktualizuje rezerwacje, czy zbieramy dane gości."),
    demonstracja={"tytul": "Mail → wymagania → wycena w 45 minut", "kroki": [
        "Czytasz pomoc/brief_klienta.md. Wypisujesz 7 potrzeb, w tym 2 ukryte („nie chcę przepisywać rezerwacji z zeszytu” = import danych).",
        "Agent (nowa sesja, tryb planu): proponuje 8 historyjek i 12 pytań. Odrzucasz 2 historyjki (logowanie gości, newsletter — nikt o nie nie prosił), 4 pytania łączysz.",
        "Poza zakresem: płatności online, aplikacja mobilna, integracja z portalami rezerwacyjnymi.",
        "Wycena: 6 historyjek × średnio 4 h + testy 6 h + README i wdrożenie 4 h + poprawki 4 h = 38 h; bufor 40% → 53 h. Koszty narzędzi i hostingu — osobna pozycja.",
        "Wysyłasz klientce wymagania i pytania PRZED wyceną końcową; wycenę po odpowiedziach."],
        "wynik": "Wymagania z kryteriami, lista pytań, jasny „poza zakresem” i wycena z buforem — klientka wie, co dostanie i za ile."},
    jak_uruchomic=["Zadanie tygodnia „wymagania.md” → „✔ Sprawdź wynik” (struktura historyjek)."],
    cwiczenia=[
        C("prowadzone",
          "Wycena: 5 historyjek po 4 h, testy 6 h, README i wdrożenie 4 h, poprawki 4 h. (1) Suma godzin bez bufora, (2) z buforem 40% (zaokrąglij w górę do pełnej godziny), (3) wartość przy stawce 80 zł/h (zł). Czas: 15 minut.",
          "(1) 34 h; (2) 48 h (34 × 1,4 = 47,6 → 48); (3) 3 840 zł.",
          ["5 × 4 = 20, plus 6 + 4 + 4.", "Pomnóż przez 1,4.", "Godziny z buforem × stawka."],
          "20 + 14 = 34 h; 34 × 1,4 = 47,6 → 48 h; 48 × 80 = 3 840 zł.",
          [li("h", "(1) Godziny bez bufora", 34), li("hb", "(2) Godziny z buforem", 48, bledy=[bl(47.6, "zaokrąglij w górę do pełnej godziny")]), kw("zl", "(3) Wartość (zł)", 3840)]),
        C("samodzielne",
          "Które kryteria akceptacji są poprawne (sprawdzalne)? (1) „Kalkulator jest intuicyjny”, (2) „Dla 7 nocy i 2 osób w lipcu kalkulator pokazuje kwotę z rabatem 10%”, (3) „Strona ładuje się szybko”, (4) „Formularz z pustą datą pokazuje komunikat po polsku i nie wysyła danych”. "
          "Podaj liczbę poprawnych. Do której sekcji trafia „płatność online” w wersji 1? Czas: 15 minut.",
          "2 poprawne (2 i 4); płatność → Poza zakresem.",
          ["Czy dwie osoby, sprawdzając, dadzą tę samą odpowiedź?", "„Intuicyjny” i „szybko” — opinie bez progu.", "Płatność nie była potwierdzona i wymaga osobnych decyzji."],
          "Sprawdzalne: 2 i 4. Płatność online → Poza zakresem (osobna wycena).",
          [li("ile", "Liczba poprawnych", 2), wy("sekcja", "Sekcja dla płatności online", ["Historyjki (musi)", "Poza zakresem", "Pytania"], "Poza zakresem")]),
    ],
    typowe_bledy=[
        B("Klient przy odbiorze: „myślałam, że będzie też…”.", "Zakres nie spisany, brak „Poza zakresem”.", "Czy klient potwierdził wymagania na piśmie?", "Wymagania z sekcją Poza zakresem wysłane i potwierdzone przed pracą; zmiany = nowa wycena."),
        B("Projekt trwa 2× dłużej niż wycena.", "Brak bufora, nieuwzględnione testy/README/poprawki.", "Porównaj wycenę z rzeczywistym czasem (dziennik).", "Bufor 30–50%, osobne pozycje na testy, dokumentację i poprawki."),
    ],
    pulapki=["„Agent zrobi to w godzinę” nie jest podstawą wyceny — czas zabierają rozmowy, testy, poprawki i odbiór.", "Nie obiecuj „bezpieczeństwa” ani „zgodności z RODO” bez sprawdzenia — obiecuj konkretne środki (lista z tygodnia 12)."],
    zadania=["Napisz wymagania.md z briefu klientki (zadanie tygodnia).", "Przygotuj wycena.md z buforem.", "Zapisz 5 pytań do klientki."],
    pytania=[["Jaki jest format historyjki użytkownika?", "Jako [kto] chcę [co], aby [po co] + sprawdzalne kryteria akceptacji."], ["Po co sekcja „Poza zakresem”?", "Żeby klient i Ty mieli tę samą wizję i żeby zmiany zakresu były osobno wyceniane."],
             ["Czym jest odbiór?", "Sprawdzeniem kryteriów akceptacji przy kliencie, nie oceną „czy się podoba”."]],
    podsumowanie="Zamieniasz mail klienta w historyjki z kryteriami, pytania i zakres, wyceniasz z buforem i planujesz odbiór oraz formę rozliczenia.",
    test=[T("Poprawne kryterium akceptacji:", ["Strona jest ładna", "Dla dat 21–22.12 lista nie zawiera zajętego Lipowego", "Działa szybko", "Klient zadowolony"], 1, "Tak/nie."),
          T("Bufor w wycenie pierwszych projektów:", ["0%", "30–50%", "200%", "Nie stosuje się"], 1, "Nieznane zawsze się pojawiają."),
          T("Klient prosi w trakcie o płatności online. Ruch:", ["Robię za darmo", "Osobna wycena — zmiana zakresu", "Odmawiam bez rozmowy", "Ukrywam w kosztach"], 1, "Zmiana zakresu."),
          T("Limit działalności nierejestrowanej 2026:", ["10 813,50 zł na kwartał", "10 813,50 zł na rok", "Brak limitu", "3 000 zł na miesiąc"], 0, "225% minimalnego wynagrodzenia.")],
    w_praktyce=["Każde zlecenie: wymagania.md potwierdzone przez klienta przed kodem.", "Dziennik godzin — podstawa kolejnych wycen."],
    zrodla=[Z_ATL_US, Z_ATL_AC, Z_NIEREJ],
)

PORTFOLIO = L(
    id="portfolio_praca", nazwa="Portfolio i ścieżki zawodowe vibe codera", tydzien=14,
    slowa=["portfolio", "GitHub", "profil", "CV", "ścieżka", "junior", "freelance", "dowód"],
    cel="Po tej lekcji wybierasz ścieżkę (praca w firmie, zlecenia, automatyzacja we własnej branży), budujesz portfolio z 3 projektów z dowodami (testy, CI, README, opis procesu) i przygotowujesz profil GitHub oraz CV pod tę ścieżkę.",
    po_co="Rekruter i klient nie widzą Twojej nauki — widzą repozytoria. Ankieta Stack Overflow 2025: większość zawodowych programistów nie uznaje „vibe codingu” za część swojej pracy — wyróżnia Cię dyscyplina: testy, przegląd, dokumentacja.",
    wymagania=["Repozytoria z kursu (pod-lipa, pod-lipa-strona).", "Lekcje „README” i „CI”."],
    wyjasnienie=(
        "## Trzy realistyczne ścieżki\n"
        "| ścieżka | co sprzedajesz | czego się dalej uczysz |\n"
        "|---|---|---|\n"
        "| automatyzacja we własnej branży | skrypty, raporty, małe narzędzia w Twojej obecnej pracy (biuro, handel, rolnictwo, logistyka) | dane (Excel/CSV), API usług, bezpieczeństwo danych |\n"
        "| zlecenia dla małych firm | strony, kalkulatory, proste aplikacje, integracje | komunikacja z klientem, wycena, utrzymanie, hosting |\n"
        "| praca w firmie IT (junior / tester / wsparcie) | umiejętność czytania, testowania i przeglądu kodu z AI | podstawy programowania głębiej (Python, SQL, Git), testy automatyczne |\n"
        "Uczciwie: sam „vibe coding” rzadko jest nazwą stanowiska. Stanowiska wymagają umiejętności, które ćwiczyłeś: testów, Gita, przeglądu, specyfikacji. Kurs „Python od zera → Junior QA” w Mentorze to naturalne pogłębienie ścieżki testera.\n"
        "## Portfolio: 3 projekty, każdy z dowodami\n"
        "- Projekt końcowy (tydzień 15) — główny.\n"
        "- Strona na GitHub Pages — widoczny efekt.\n"
        "- Jedno małe narzędzie z Twojej branży (automatyzacja, raport) — pokazuje, że rozwiązujesz realne problemy.\n"
        "Każdy z: README (z sekcją „Jak powstał”), testami, zielonym CI, licencją, sensowną historią commitów, bez sekretów i danych osobowych.\n"
        "## Profil GitHub\n"
        "- Repozytorium o nazwie takiej jak login → jego README wyświetla się na profilu (dokumentacja GitHub „profile README”): 5 zdań o Tobie, umiejętności, linki do projektów.\n"
        "- Przypnij (pin) 3 najlepsze repozytoria.\n"
        "- Zdjęcie i opis profesjonalne; e-mail kontaktowy osobny od prywatnego.\n"
        "## CV i opis projektów\n"
        "Projekt w CV: problem → co zbudowałeś → jak sprawdziłeś (testy, CI) → wynik. Przykład: „System rezerwacji dla agroturystyki (Python, Flask, SQLite): API rezerwacji z walidacją, 40 testów, CI na GitHub Actions; kod z agentami AI pod moją specyfikacją i przeglądem.” "
        "Nie ukrywaj AI — pokaż, że umiesz z nim pracować odpowiedzialnie.\n"
        "## Gdzie szukać\n"
        "Portale z ofertami IT (np. justjoin.it, nofluffjobs.com, pracuj.pl), lokalne firmy i znajomi przedsiębiorcy (zlecenia), grupy i meetupy, platformy freelancerskie. Ucz się angielskiego technicznego — dokumentacja narzędzi jest po angielsku."),
    przyklad=("README profilu (github.com/NAZWA/NAZWA):\n\n# Cześć, jestem Anna\nBuduję małe aplikacje i automatyzacje w Pythonie z pomocą agentów AI — zawsze ze specyfikacją, testami i przeglądem kodu.\n\n"
              "**Projekty**\n- [Pod Lipą — mini system rezerwacji](…) — Flask, SQLite, 40 testów, CI\n- [Strona z kalkulatorem](…) — HTML/CSS/JS, GitHub Pages\n- [Porządkowanie faktur](…) — automatyzacja plików z trybem próby\n\n"
              "**Narzędzia:** Python, Git/GitHub, pytest, Claude Code, Codex"),
    demonstracja={"tytul": "Przegląd portfolio oczami rekrutera — 3 minuty na profil", "kroki": [
        "Otwierasz swój profil w oknie prywatnym (tak widzi go obcy). Pierwsze 10 sekund: czy wiadomo, kim jesteś i co umiesz? Jeśli nie — profile README.",
        "Przypięte repozytoria: każde ma opis (About) i README z sekcją „Jak uruchomić”? Repo bez README rekruter zamyka.",
        "Zakładka Actions: zielone przebiegi = dowód testów.",
        "Historia commitów: „fix”, „asdf” vs „Dodaj walidację dat w /api/wolne (400)” — to też ocenia rekruter.",
        "Szukasz sekretów i danych: wyszukiwarka w repo („key”, „password”, „@gmail”). Czysto."],
        "wynik": "Profil, na którym w 3 minuty widać ścieżkę, 3 projekty z dowodami jakości i brak wpadek."},
    jak_uruchomic=["github.com → nowe repo o nazwie loginu → README profilu; profil → Customize your pins.", "Zadanie tygodnia „portfolio.md” (plan i lista kontrolna)."],
    cwiczenia=[
        C("prowadzone",
          "Lista kontrolna projektu do portfolio ma 6 pozycji: README z „Jak powstał”, testy, zielone CI, licencja, historia commitów z opisami, brak sekretów i danych. Projekt ma: README bez sekcji „Jak powstał”, 25 testów, CI zielone, brak LICENSE, commity „fix” i „zmiany”, czysto z sekretami. "
          "Ile pozycji jest spełnionych? Którą poprawisz najszybciej (opcje: licencja, historia commitów)? Czas: 15 minut.",
          "3 spełnione (testy, CI, brak sekretów); najszybciej licencja (plik z szablonu GitHuba w minutę).",
          ["Przejdź po kolei 6 pozycji.", "README bez „Jak powstał” — niespełnione.", "Historii commitów nie poprawisz szybko bez przepisywania — licencję tak."],
          "Spełnione: testy, CI, sekrety = 3. Licencja — minuta; README uzupełnisz; historię poprawiaj na przyszłość.",
          [li("ile", "Spełnione pozycje", 3), wy("szybko", "Najszybsza poprawka", ["licencja", "historia commitów"], "licencja")]),
        C("samodzielne",
          "Dopasuj ścieżkę: (1) pracujesz w biurze rachunkowym i chcesz automatyzować raporty, (2) chcesz robić strony i kalkulatory dla lokalnych firm, (3) chcesz etat w firmie IT i lubisz szukać błędów. "
          "Opcje: automatyzacja we własnej branży / zlecenia dla małych firm / praca w firmie IT (tester/junior). Czas: 15 minut.",
          "(1) automatyzacja we własnej branży; (2) zlecenia dla małych firm; (3) praca w firmie IT (tester/junior).",
          ["Najkrótsza droga to problemy, które już znasz.", "Strony dla firm to zlecenia.", "Szukanie błędów — testowanie."],
          "Automatyzacja w branży, zlecenia, ścieżka testera/juniora.",
          [wy(f"s{i}", t, ["automatyzacja we własnej branży", "zlecenia dla małych firm", "praca w firmie IT (tester/junior)"], w) for i, t, w in
           ((1, "(1) Biuro rachunkowe", "automatyzacja we własnej branży"), (2, "(2) Strony dla firm", "zlecenia dla małych firm"), (3, "(3) Etat, szukanie błędów", "praca w firmie IT (tester/junior)"))]),
    ],
    typowe_bledy=[
        B("Rekruter: „nie widzę, co Pan/Pani umie”.", "Repozytoria bez README, brak opisu profilu.", "Profil w oknie prywatnym.", "Profile README, przypięte 3 projekty z README i CI."),
        B("W publicznym repo znaleziono stary klucz.", "Klucz w historii commitów.", "Wyszukiwarka GitHuba w repo / secret scanning.", "Unieważnij klucz; jeśli repo to portfolio — rozważ nowe repo bez tej historii."),
    ],
    pulapki=["Ilość nie zastępuje jakości: 3 dopracowane projekty > 20 porzuconych.", "Nie publikuj projektów z kursu jako pracy dla prawdziwego klienta — opisz uczciwie: projekt szkoleniowy, dane fikcyjne."],
    zadania=["Wybierz ścieżkę i zaplanuj portfolio (zadanie tygodnia).", "Profile README i 3 przypięte repozytoria.", "Opis projektu końcowego do CV (4 zdania)."],
    pytania=[["Co powinien mieć projekt w portfolio?", "README z opisem procesu, testy, zielone CI, licencję, czytelną historię i brak sekretów."], ["Dlaczego nie ukrywać pracy z AI?", "Bo firmy jej używają — wyróżnia odpowiedzialny proces: specyfikacja, testy, przegląd."],
             ["Jak wygląda opis projektu w CV?", "Problem → rozwiązanie → jak sprawdzone → wynik, z technologiami."]],
    podsumowanie="Wybierasz ścieżkę, budujesz portfolio 3 projektów z dowodami jakości, profil GitHub i opis projektów do CV — uczciwie wobec pracy z AI.",
    test=[T("Rekruter ma 3 minuty na profil. Najważniejsze:", ["Liczba repozytoriów", "Profile README i 3 dopracowane projekty z README i CI", "Kolorowy avatar", "Liczba gwiazdek"], 1, "Jakość i dowody."),
          T("README profilu GitHub to repozytorium o nazwie:", ["profile", "takiej jak login", "readme", "about"], 1, "Dokumentacja GitHub."),
          T("Praca z AI w CV:", ["Ukryć", "Opisać z procesem: specyfikacja, testy, przegląd", "Napisać, że AI zrobiło wszystko", "Pominąć projekt"], 1, "Odpowiedzialność to atut.")],
    w_praktyce=["Raz w miesiącu przegląd profilu oczami rekrutera.", "Każdy nowy projekt od razu z README i CI."],
    zrodla=[Z_GH_PROFILE, Z_GH_PIN, Z_SO, Z_LIC],
)

ROZMOWA_REK = L(
    id="rozmowa_rekrutacyjna", nazwa="Rozmowa rekrutacyjna i zadanie praktyczne z AI", tydzien=14,
    slowa=["rozmowa", "rekrutacja", "STAR", "zadanie praktyczne", "live coding", "pytania", "AI na rozmowie"],
    cel="Po tej lekcji odpowiadasz na 10 typowych pytań o pracę z AI i projekty metodą STAR, wykonujesz zadanie praktyczne z głośnym myśleniem i zadajesz rekruterowi pytania o zasady używania AI w firmie.",
    po_co="Na rozmowie sprawdza się, czy rozumiesz kod, którego nie napisałeś sam, i czy można Ci zaufać z agentem w firmowym repozytorium.",
    wymagania=["Lekcja „Portfolio”.", "Projekt końcowy w toku (do opowiadania)."],
    wyjasnienie=(
        "## Metoda STAR\n"
        "Odpowiedź na pytanie „opowiedz o sytuacji, gdy…”: Sytuacja (kontekst), Zadanie (co było do zrobienia), Akcja (co TY zrobiłeś), Rezultat (wynik, najlepiej liczbowy). 1–2 minuty.\n"
        "Przykład: „S: agent oddał raport, który pomijał wiersze z CSV. Z: raport miał liczyć wszystkie 40 rezerwacji. A: porównałem liczbę wierszy, znalazłem except: continue, kazałem zgłaszać zły wiersz z numerem, dopisałem test. R: raport liczy 40/40, błąd nie wróci (test regresji).”\n"
        "## 10 pytań, które padną (przygotuj odpowiedzi)\n"
        "| pytanie | czego szukają |\n"
        "|---|---|\n"
        "| Jak sprawdzasz kod od AI? | proces: testy, przegląd diffu, lista bezpieczeństwa |\n"
        "| Opowiedz o błędzie agenta, który złapałeś | STAR, konkret |\n"
        "| Kiedy NIE używasz AI? | dane wrażliwe, decyzje bez weryfikacji, gdy szybciej samemu |\n"
        "| Jak chronisz sekrety? | zmienne środowiskowe, .gitignore, deny, unieważnienie po wycieku |\n"
        "| Wyjaśnij ten fragment kodu | czytanie kodu — ćwiczone od tygodnia 1 |\n"
        "| Co to jest test i po co mutanty? | rozumienie testów |\n"
        "| Jak dzielisz duże zadanie? | małe kroki, plan, commity |\n"
        "| Co robisz, gdy agent się zapętla? | diagnoza, reguła trzech, nowa sesja |\n"
        "| Jak pracujesz z Gitem w zespole? | gałąź, PR, przegląd, CI |\n"
        "| Czego się teraz uczysz? | konkretny plan rozwoju |\n"
        "## Zadanie praktyczne\n"
        "Bywa: „napraw błąd w tym repo” albo „dodaj funkcję” — czasem z AI, czasem bez. Zasady: najpierw przeczytaj i zapytaj o niejasności, mów na głos, co robisz i dlaczego, uruchom testy przed i po, pokaż diff i wyjaśnij każdą linię. "
        "Jeśli wolno używać AI — pokaż proces (plan, prośba z kryteriami, przegląd), nie tylko wynik. Jeśli nie wolno — Twoje czytanie kodu i traceback wystarczą na proste zadania.\n"
        "## Twoje pytania do firmy\n"
        "- Jakich narzędzi AI używacie i jakie są zasady (dane, repozytoria, zgody)?\n"
        "- Jak wygląda przegląd kodu i CI?\n"
        "- Jak wygląda wdrożenie nowej osoby (onboarding), kto będzie mentorem?\n"
        "- Po czym poznam po 3 miesiącach, że dobrze mi idzie?\n"
        "## Uczciwość\n"
        "Nie przypisuj sobie wiedzy, której nie masz. „Tego jeszcze nie robiłem, ale sprawdziłbym to tak: …” jest lepsze niż zgadywanie. Rekruterzy szybko rozpoznają wyuczone frazy bez zrozumienia."),
    przyklad=("Pytanie: „Jak sprawdzasz kod od AI?”\n\nOdpowiedź (45 s): „Zaczynam od specyfikacji z przykładami — z nich piszę testy, zanim agent napisze kod. Agent pracuje w trybie planu, małymi krokami. "
              "Po każdym kroku czytam diff według listy: zakres, testy, zależności, sekrety, ukryte błędy, SQL i HTML. Testy uruchamiam lokalnie i w CI. "
              "Na przykład w projekcie rezerwacji wyłapałem w ten sposób f-string w zapytaniu SQL — dopisałem test z „x' OR '1'='1” i poprawkę na parametry.”"),
    demonstracja={"tytul": "Symulacja: 20 minut zadania praktycznego", "kroki": [
        "Zadanie: „W repo jest błąd: /api/wolne zwraca 500 dla braku parametru. Napraw.” Czytasz README i AGENTS.md, uruchamiasz testy (wszystkie zielone — brak testu na ten przypadek).",
        "Mówisz na głos: „Najpierw odtworzę błąd i napiszę test, który go pokazuje”. Test czerwony — 500.",
        "Traceback: TypeError z fromisoformat(None). Hipoteza: trasa łapie tylko ValueError. Poprawka jednej linii (TypeError, ValueError).",
        "Testy zielone. Pokazujesz diff (2 linie + test) i mówisz, dlaczego nie zmieniłeś niczego innego.",
        "Pytanie rekrutera: „Użyłbyś AI?” — „Tak, do diagnozy lub poprawki, ale test i przegląd zrobiłbym tak samo”."],
        "wynik": "Rozwiązanie z testem regresji, minimalny diff i jasne wyjaśnienie procesu — dokładnie to, co ocenia rekruter."},
    jak_uruchomic=["Zadanie tygodnia: odpowiedzi na 10 pytań w odpowiedzi_rekrutacja.md + nagranie lub próba z drugą osobą.", "Asystent Mentora może zadawać pytania jak rekruter."],
    cwiczenia=[
        C("prowadzone",
          "Przypisz części odpowiedzi do STAR: (1) „raport pomijał wiersze z CSV”, (2) „miał liczyć wszystkie 40 rezerwacji”, (3) „znalazłem except: continue i dopisałem test”, (4) „teraz liczy 40/40”. Opcje: S, T, A, R. Czas: 15 minut.",
          "(1) S; (2) T; (3) A; (4) R.",
          ["Sytuacja — kontekst problemu.", "Zadanie — co było do osiągnięcia.", "Akcja — co zrobiłeś; Rezultat — wynik."],
          "S, T, A, R.",
          [wy(f"s{i}", t, ["S", "T", "A", "R"], w) for i, t, w in ((1, "(1)", "S"), (2, "(2)", "T"), (3, "(3)", "A"), (4, "(4)", "R"))]),
        C("samodzielne",
          "Na zadaniu praktycznym: uporządkuj kroki — A) uruchom testy przed zmianą, B) przeczytaj README i zapytaj o niejasności, C) pokaż diff i wyjaśnij, D) napisz test odtwarzający błąd, E) popraw przyczynę. Ciąg liter. "
          "Czy „nie wiem, sprawdziłbym to tak…” to dobra odpowiedź, gdy czegoś nie znasz (tak/nie)? Czas: 15 minut.",
          "BADEC; tak.",
          ["Najpierw zrozumienie, potem stan wyjściowy.", "Test przed poprawką.", "Na końcu pokazanie wyniku."],
          "README → testy → test błędu → poprawka → diff = BADEC. Uczciwe „nie wiem + jak sprawdzę” — tak.",
          [tx("kol", "Kolejność", ["BADEC"]), wy("nw", "„Nie wiem, sprawdziłbym…” dobra odpowiedź?", TN, "tak")]),
    ],
    typowe_bledy=[
        B("Na prośbę „wyjaśnij ten kod” — cisza.", "Kod w portfolio pisał agent, a nie był czytany.", "Czy umiesz opisać każdą funkcję swojego projektu?", "Przed rozmową: przejdź swój projekt plik po pliku i opowiedz go na głos."),
        B("Odpowiedzi ogólne („zawsze testuję”).", "Brak przykładów.", "Czy każda odpowiedź ma konkret z projektu?", "Przygotuj 3 historie STAR z kursu i projektu końcowego."),
    ],
    pulapki=["Nie używaj AI potajemnie na rozmowie, jeśli zasady tego zabraniają — to dyskwalifikuje.", "Nie mów źle o poprzednich pracodawcach ani narzędziach — mów, czego się nauczyłeś."],
    zadania=["Przygotuj odpowiedzi na 10 pytań i 3 historie STAR (zadanie tygodnia).", "Zrób próbną rozmowę z Asystentem lub znajomym.", "Przygotuj 4 pytania do firmy."],
    pytania=[["Co to jest metoda STAR?", "Sytuacja, Zadanie, Akcja, Rezultat — struktura odpowiedzi na pytania o doświadczenie."], ["Jak zachowujesz się na zadaniu praktycznym?", "Czytam, pytam, testuję przed i po, myślę na głos, pokazuję minimalny diff."],
             ["O co pytasz firmę w sprawie AI?", "O narzędzia, zasady dotyczące danych i repozytoriów, przegląd kodu i CI."]],
    podsumowanie="Masz odpowiedzi STAR na 10 pytań, umiesz przeprowadzić zadanie praktyczne z głośnym myśleniem i zadajesz rzeczowe pytania o zasady AI w firmie.",
    test=[T("STAR to:", ["Ocena w gwiazdkach", "Sytuacja, Zadanie, Akcja, Rezultat", "Nazwa frameworka", "Rodzaj testu"], 1, "Struktura odpowiedzi."),
          T("Na zadaniu praktycznym najpierw:", ["Piszesz kod", "Czytasz README i uruchamiasz testy", "Prosisz AI o całość", "Zmieniasz testy"], 1, "Zrozumienie i stan wyjściowy."),
          T("Nie znasz odpowiedzi. Najlepiej:", ["Zgadnąć pewnym tonem", "Powiedzieć, jak byś to sprawdził", "Zmienić temat", "Milczeć"], 1, "Uczciwość i proces.")],
    w_praktyce=["Każdy projekt: 1 historia STAR w notatkach.", "Raz w tygodniu: wyjaśnij na głos jeden plik swojego projektu."],
    zrodla=[Z_STAR, Z_SO, Z_CC_BEST],
)


# =========================================================================== TYDZIEŃ 15
PLAN = L(
    id="projekt_plan", nazwa="Projekt końcowy: plan, kamienie milowe i praca z agentem", tydzien=15,
    slowa=["projekt końcowy", "plan", "kamień milowy", "ryzyko", "specyfikacja", "MVP", "harmonogram"],
    cel="Po tej lekcji planujesz projekt końcowy — mini system rezerwacji „Pod Lipą” albo własny projekt — z celem, funkcjami (MVP), kamieniami milowymi, ryzykami i kryteriami „Gotowe, gdy”, i prowadzisz agenta według tego planu.",
    po_co="Projekt końcowy łączy wszystko z kursu i jest głównym elementem portfolio. Dobry plan to różnica między ukończonym projektem a porzuconym w połowie.",
    wymagania=["Wszystkie lekcje tygodni 0–14.", "Repozytorium pod-lipa z CI."],
    wyjasnienie=(
        "## Dwie drogi\n"
        "- Domyślna: „Pod Lipą — mini system rezerwacji” (specyfikacja poniżej, sprawdzana niezależnymi testami Mentora).\n"
        "- Własny projekt (np. z Twojej branży): ten sam zakres jakości — plan, testy (≥ 10), CI, README, AGENTS.md, bezpieczeństwo — oceniany rubryką przez Ciebie, mentora lub rekrutera.\n"
        "## Specyfikacja domyślna (plik system.py)\n"
        "| funkcja | zachowanie |\n"
        "|---|---|\n"
        "| `create_app(sciezka_bazy=\":memory:\")` | aplikacja Flask z bazą SQLite rezerwacji |\n"
        "| `GET /` | strona HTML z nazwą „Pod Lipą” |\n"
        "| `POST /api/rezerwacje` (JSON: gosc, email, pokoj, od, do) | 201 i `{\"id\", \"koszt\"}`; złe dane (e-mail, pokój, daty) → 400; kolizja z istniejącą rezerwacją → 409 |\n"
        "| `GET /api/rezerwacje` | 200 i lista rezerwacji (id, gosc, pokoj, od, do, koszt) — BEZ e-maili (minimalizacja danych) |\n"
        "| `GET /api/wolne?od=&do=` | wolne pokoje według zapisanych rezerwacji |\n"
        "| `DELETE /api/rezerwacje/<id>` | 204; nieznane id → 404 |\n"
        "Koszt = suma cen pokoju za każdą noc według cennik.cena_pokoju(pokoj, miesiąc tej nocy). Moduły z kursu (walidacja, kalendarz, cennik) importujesz — nie kopiujesz.\n"
        "## MVP i kamienie milowe\n"
        "MVP (minimum viable product) — najmniejsza wersja, która spełnia cel. Kamienie milowe dla wersji domyślnej:\n"
        "| # | kamień | gotowe, gdy |\n"
        "|---|---|---|\n"
        "| 1 | baza i zapis rezerwacji | POST zapisuje, testy 201/400 |\n"
        "| 2 | kolizje i lista | 409 dla kolizji, GET bez e-maili |\n"
        "| 3 | wolne pokoje i usuwanie | /api/wolne z bazy, DELETE 204/404 |\n"
        "| 4 | jakość | ≥ 10 Twoich testów, CI zielone, README, bezpieczeństwo |\n"
        "| 5 | wydanie | CHANGELOG, tag v1.0.0, prezentacja |\n"
        "## Ryzyka\n"
        "Zapisz 3–5 ryzyk z planem: „agent przepisze moduły z kursu” → zasada w AGENTS.md; „zabraknie limitu planu” → praca bez agenta nad testami i README; „kolizje dat — trudne przypadki” → testy brzegowe z tygodnia 7 przed kodem.\n"
        "## Praca z agentem w projekcie\n"
        "- Każdy kamień = osobna gałąź i PR z CI.\n"
        "- Sesja zaczyna się od: AGENTS.md + plan_projektu.md + notatka stan.md.\n"
        "- Najpierw testy kamienia (ze specyfikacji), potem implementacja „bez zmiany testów”.\n"
        "- Po kamieniu: przegląd 8 pytań + tabela 6 dziur bezpieczeństwa, merge, notatka stanu."),
    przyklad=("# plan_projektu.md\n\n## Cel\nMini system rezerwacji „Pod Lipą”: goście sprawdzają wolne pokoje i rezerwują; właścicielka widzi listę.\n\n"
              "## Użytkownicy\n- gość (rezerwuje), właścicielka (przegląda, usuwa)\n\n## Funkcje (MVP)\n- POST /api/rezerwacje z walidacją\n- 409 dla kolizji\n- GET /api/rezerwacje bez e-maili\n- GET /api/wolne\n- DELETE /api/rezerwacje/<id>\n\n"
              "## Kamienie milowe\n- K1 baza i zapis\n- K2 kolizje i lista\n- K3 wolne i usuwanie\n- K4 jakość\n- K5 wydanie\n\n"
              "## Ryzyka\n- agent kopiuje moduły zamiast importu → zasada w AGENTS.md\n\n## Gotowe, gdy\n- testy Mentora zielone, ≥ 10 moich testów, CI zielone, README, tag v1.0.0"),
    demonstracja={"tytul": "Kamień 1 z agentem — testy najpierw", "kroki": [
        "Gałąź k1-zapis. Prośba (tryb planu): „Na podstawie plan_projektu.md napisz TYLKO testy test_system.py dla kamienia 1: POST poprawny → 201 i id; zły e-mail, nieznany pokój, do ≤ od → 400. Nie implementuj.”",
        "Przegląd testów: czy przykłady są ze specyfikacji? Dopisujesz brakujący: pusty JSON → 400. Testy czerwone (brak system.py) — dobrze.",
        "Prośba: „Zaimplementuj system.py tak, by przeszły testy kamienia 1; importuj walidacja, kalendarz, cennik; SQL tylko z ?; nie zmieniaj testów”.",
        "Testy zielone, przegląd diffu (8 pytań + 6 dziur): koszt liczony za noc z miesiącem każdej nocy — sprawdzasz ręcznie rezerwację 30.11–2.12 (noc listopadowa po cenie niskiej, grudniowa po wysokiej).",
        "PR, CI zielone, merge, notatka stan.md. Kamień 1 zamknięty."],
        "wynik": "Kamień 1 gotowy z testami napisanymi przed kodem, przeglądem bezpieczeństwa i zielonym CI; plan prowadzi kolejne sesje."},
    jak_uruchomic=["Zadanie tygodnia „plan_projektu.md” → „✔ Sprawdź wynik” (sekcje planu).", "Każdy kamień: gałąź → testy → implementacja → PR → CI → merge."],
    cwiczenia=[
        C("prowadzone",
          "Koszt rezerwacji Lipowego od 2026-11-30 do 2026-12-02 według specyfikacji (cena za noc według miesiąca TEJ nocy; Lipowy: 180 zł w sezonie wysokim, 140 zł w niskim; grudzień — wysoki). Ile nocy? Ile kosztuje noc 30.11? Koszt łączny (zł)? Czas: 15 minut.",
          "2 noce; noc 30.11 — 140 zł (listopad, sezon niski); noc 1.12 — 180 zł; razem 320 zł.",
          ["Noce: 30/1 i 1/2.", "30 listopada — sezon niski.", "1 grudnia — wysoki."],
          "Noc 30.11: 140 zł, noc 1.12: 180 zł → 320 zł.",
          [li("noce", "Liczba nocy", 2), kw("n1", "Noc 30.11 (zł)", 140), kw("razem", "Koszt łączny (zł)", 320, bledy=[bl(360, "noc 30.11 jest w listopadzie (sezon niski — 140 zł), nie w grudniu"), bl(280, "noc 1.12 jest już w grudniu (sezon wysoki — 180 zł)")])]),
        C("samodzielne",
          "Dopasuj kod odpowiedzi API projektu: (1) POST z e-mailem „anna@”, (2) POST Lipowego 21–22.12, gdy istnieje Lipowy 20–23.12, (3) DELETE /api/rezerwacje/999 (brak), (4) poprawny POST. Opcje: 201, 400, 404, 409. "
          "Czy GET /api/rezerwacje zwraca e-maile gości (tak/nie)? Czas: 15 minut.",
          "(1) 400; (2) 409; (3) 404; (4) 201; nie — minimalizacja danych.",
          ["Zły e-mail — złe dane.", "Kolizja — konflikt (409).", "Brak zasobu — 404; utworzenie — 201."],
          "400, 409, 404, 201; lista bez e-maili.",
          [wy(f"k{i}", t, ["201", "400", "404", "409"], w) for i, t, w in ((1, "(1) zły e-mail", "400"), (2, "(2) kolizja", "409"), (3, "(3) brak id", "404"), (4, "(4) poprawny POST", "201"))]
          + [wy("mail", "Lista zawiera e-maile?", TN, "nie")]),
    ],
    typowe_bledy=[
        B("Projekt „rozlewa się” — po tygodniu brak działającej wersji.", "Za duży zakres, brak MVP i kamieni.", "Czy kamień 1 jest zamknięty?", "Utnij do MVP; kamień po kamieniu z merge."),
        B("Agent skopiował kalendarz.py do system.py.", "Brak zasady importu.", "Diff — duplikat kodu.", "Zasada w AGENTS.md: „importuj moduły kursu, nie kopiuj”; cofnij i powtórz krok."),
    ],
    pulapki=["Własny projekt jest świetny do portfolio, ale musi mieć ten sam poziom jakości — bez testów i CI nie zastąpi wersji domyślnej.", "Nie dodawaj logowania, płatności, maili w MVP — to osobne, trudne tematy bezpieczeństwa."],
    zadania=["Napisz plan_projektu.md (zadanie tygodnia).", "Zrealizuj kamienie 1–4 (zadanie tygodnia).", "Notatka stan.md po każdym kamieniu."],
    pytania=[["Co to jest MVP?", "Najmniejsza wersja produktu, która spełnia cel i daje się sprawdzić."], ["Dlaczego testy kamienia przed implementacją?", "Bo to umowa z agentem i dowód, że kamień jest skończony."],
             ["Dlaczego lista rezerwacji nie zawiera e-maili?", "Minimalizacja danych osobowych — API zwraca tylko to, co potrzebne."]],
    podsumowanie="Masz plan projektu z MVP, kamieniami, ryzykami i kryteriami, a każdy kamień prowadzisz przez testy, agenta, przegląd, PR i CI.",
    test=[T("Kolizja rezerwacji w API — kod:", ["400", "404", "409", "500"], 2, "Konflikt zasobu."),
          T("Kamień milowy jest zamknięty, gdy:", ["Agent napisze „gotowe”", "Spełnia kryteria, testy i CI zielone, merge zrobiony", "Minie tydzień", "Kod jest długi"], 1, "Kryteria tak/nie."),
          T("Moduły z kursu w projekcie:", ["Kopiujesz do jednego pliku", "Importujesz", "Przepisujesz od nowa", "Usuwasz"], 1, "Jedno źródło prawdy.")],
    w_praktyce=["Każdy projekt: MVP + kamienie + ryzyka na jednej stronie.", "Kamień = gałąź = PR."],
    zrodla=[Z_CC_BEST, Z_ATL_AC, Z_GH_README],
)

WYDANIE = L(
    id="projekt_wydanie", nazwa="Wydanie wersji 1.0: CHANGELOG, tag, release i przekazanie", tydzien=15,
    slowa=["wydanie", "release", "tag", "wersja", "SemVer", "CHANGELOG", "przekazanie", "utrzymanie"],
    cel="Po tej lekcji wydajesz wersję 1.0.0 projektu: lista kontrolna przed wydaniem, CHANGELOG, tag Git i release na GitHubie, a dla klienta — przekazanie z instrukcją i planem utrzymania.",
    po_co="„Skończone” w zawodzie znaczy: wydane, opisane i możliwe do utrzymania. Wydanie z tagiem to też dowód dla rekrutera, że doprowadzasz projekty do końca.",
    wymagania=["Projekt końcowy z kamieniami 1–4.", "Lekcje „README” i „CI”."],
    wyjasnienie=(
        "## Wersjonowanie semantyczne (SemVer)\n"
        "Numer GŁÓWNA.MNIEJSZA.POPRAWKA: 1.0.0 — pierwsza stabilna; 1.1.0 — nowa funkcja zgodna wstecz; 1.1.1 — poprawka błędu; 2.0.0 — zmiana łamiąca zgodność (np. inny format API).\n"
        "## Lista kontrolna przed wydaniem\n"
        "| obszar | sprawdzenie |\n"
        "|---|---|\n"
        "| testy | wszystkie zielone lokalnie i w CI |\n"
        "| bezpieczeństwo | tabela 6 dziur, brak sekretów w repo (wyszukiwanie), debug wyłączony, SECRET_KEY ze zmiennej |\n"
        "| dane | brak prawdziwych danych osobowych, *.db w .gitignore |\n"
        "| dokumentacja | README (test obcej osoby), CHANGELOG, LICENSE |\n"
        "| zależności | requirements.txt z wersjami, każda paczka zweryfikowana |\n"
        "| instrukcje agenta | AGENTS.md aktualny |\n"
        "## CHANGELOG.md (zasady „Keep a Changelog”)\n"
        "```\n# Changelog\n\n## [1.0.0] - 2027-03-10\n### Dodano\n- API rezerwacji z walidacją (201/400/409)\n- Lista rezerwacji bez danych kontaktowych\n### Bezpieczeństwo\n- Zapytania SQL wyłącznie z parametrami\n```\n"
        "Sekcje: Dodano, Zmieniono, Naprawiono, Usunięto, Bezpieczeństwo. Najnowsza wersja na górze. Piszesz dla ludzi, nie wklejasz listy commitów.\n"
        "## Tag i release\n"
        "- `git tag -a v1.0.0 -m \"Wersja 1.0.0\"` → `git push origin v1.0.0`.\n"
        "- GitHub → Releases → Draft a new release → wybierz tag v1.0.0 → opis z CHANGELOG → Publish.\n"
        "- Release może zawierać pliki do pobrania (np. ZIP), ale kod źródłowy GitHub dołącza sam.\n"
        "## Przekazanie klientowi\n"
        "- Instrukcja dla użytkownika (nie programisty): jak uruchomić, jak dodać/usunąć rezerwację, co robić, gdy coś nie działa.\n"
        "- Dostępy: repozytorium (zaproszenie klienta jako właściciela/organizacji), hosting, domena — na konto klienta, nie Twoje.\n"
        "- Plan utrzymania: aktualizacje zależności (np. raz na kwartał), kopie bazy, kto i za ile poprawia błędy po okresie gwarancyjnym.\n"
        "## Retrospektywa\n"
        "Po wydaniu 30 minut: co poszło dobrze, co źle, co zmienię w następnym projekcie (dla siebie i w AGENTS.md/szablonach). To najkrótsza droga do szybszych i tańszych projektów."),
    przyklad=("Opis release v1.0.0 na GitHubie:\n\n**Pod Lipą — mini system rezerwacji 1.0.0**\n\nPierwsza stabilna wersja projektu szkoleniowego (dane fikcyjne).\n\n"
              "- API rezerwacji: zapis z walidacją, kolizje (409), lista bez e-maili, wolne pokoje, usuwanie\n- 46 testów, CI na GitHub Actions\n- Bezpieczeństwo: SQL z parametrami, escape w HTML, sekrety ze zmiennych środowiskowych\n\n"
              "Uruchomienie: README → Instalacja."),
    demonstracja={"tytul": "Wydanie z listą kontrolną — jedna wpadka złapana", "kroki": [
        "Lista kontrolna: testy zielone, CI zielone. Wyszukiwanie w repo „SECRET” — w system.py `SECRET_KEY = os.environ.get(\"FLASK_SECRET_KEY\", \"dev\")`: domyślna wartość „dev”. Poprawka: brak zmiennej → RuntimeError; test.",
        "README: test obcej osoby — OK. CHANGELOG według szablonu.",
        "`git tag -a v1.0.0 -m \"Wersja 1.0.0\"`, `git push origin v1.0.0`. GitHub → Releases → nowy release z opisem.",
        "Retrospektywa: dobrze — testy przed kodem; źle — kamień 2 trwał 2× dłużej (kolizje); zmiana — przypadki brzegowe dat do szablonu specyfikacji."],
        "wynik": "Wersja 1.0.0 z tagiem i release, bez domyślnego sekretu, z CHANGELOG i wnioskami na następny projekt."},
    jak_uruchomic=["`git tag -a v1.0.0 -m \"Wersja 1.0.0\"` → `git push origin v1.0.0` → GitHub Releases.", "Zadanie tygodnia „Wydanie 1.0.0” → „✔ Sprawdź wynik”."],
    cwiczenia=[
        C("prowadzone",
          "Dobierz numer wersji po 1.2.3 według SemVer: (1) poprawka błędu walidacji dat, (2) nowa funkcja — eksport CSV, zgodna wstecz, (3) zmiana formatu odpowiedzi API (stare aplikacje przestaną działać). Czas: 15 minut.",
          "(1) 1.2.4; (2) 1.3.0; (3) 2.0.0.",
          ["Poprawka — ostatnia liczba.", "Nowa zgodna funkcja — środkowa, ostatnia na 0.", "Zmiana łamiąca — pierwsza, reszta na 0."],
          "1.2.4, 1.3.0, 2.0.0.",
          [tx("v1", "(1)", ["1.2.4"]), tx("v2", "(2)", ["1.3.0"]), tx("v3", "(3)", ["2.0.0"])]),
        C("samodzielne",
          "Przekazanie klientce: na czyje konto rejestrujesz domenę i hosting (moje / klientki)? Jaką komendą wyślesz tag v1.0.0 na GitHub (pełna komenda)? Która sekcja CHANGELOG opisze „SQL z parametrami” (Dodano / Bezpieczeństwo / Naprawiono)? Czas: 15 minut.",
          "Konto klientki; git push origin v1.0.0; Bezpieczeństwo.",
          ["Klient powinien być właścicielem swoich zasobów.", "Tag wysyłasz osobno — push z nazwą taga.", "Keep a Changelog ma sekcję o bezpieczeństwie."],
          "Na konto klientki; `git push origin v1.0.0`; sekcja Bezpieczeństwo.",
          [wy("konto", "Czyje konto?", ["moje", "klientki"], "klientki"), tx("push", "Komenda", ["git push origin v1.0.0"]), wy("sekcja", "Sekcja CHANGELOG", ["Dodano", "Bezpieczeństwo", "Naprawiono"], "Bezpieczeństwo")]),
    ],
    typowe_bledy=[
        B("Tag jest lokalnie, ale nie ma go na GitHubie.", "`git push` nie wysyła tagów domyślnie.", "`git ls-remote --tags origin`.", "`git push origin v1.0.0`."),
        B("Release zawiera plik .env albo bazę z danymi.", "Ręcznie dołączony ZIP z całego folderu.", "Lista plików w release.", "Usuń zasób z release, unieważnij sekrety; ZIP buduj z `git archive` (tylko pliki z repo)."),
    ],
    pulapki=["Wydanie w piątek wieczorem bez czasu na poprawki — zły pomysł także w małych projektach.", "Hosting i domena na Twoje konto = klient jest od Ciebie zależny; przenieś na konto klienta."],
    zadania=["Lista kontrolna, CHANGELOG, tag v1.0.0 i release (zadanie tygodnia).", "Instrukcja dla użytkownika (1 strona).", "Retrospektywa w dzienniku."],
    pytania=[["Co oznacza 2.0.0 w SemVer?", "Zmianę łamiącą zgodność wstecz."], ["Co zawiera CHANGELOG?", "Opis zmian dla ludzi w sekcjach Dodano/Zmieniono/Naprawiono/Usunięto/Bezpieczeństwo, najnowsze na górze."],
             ["Co przekazujesz klientowi?", "Instrukcję, dostępy na jego konto, plan utrzymania i dokumentację."]],
    podsumowanie="Wydajesz wersję 1.0.0 z listą kontrolną, CHANGELOG, tagiem i release, przekazujesz projekt klientowi i robisz retrospektywę.",
    test=[T("Pierwsza stabilna wersja według SemVer:", ["0.1.0", "1.0.0", "1.1.1", "10"], 1, "Publiczne API ustalone."),
          T("Wysłanie tagu na GitHub:", ["git push", "git push origin v1.0.0", "git tag --push", "git release"], 1, "Tagi osobno."),
          T("Przed wydaniem sprawdzasz:", ["Tylko kolor strony", "Testy, CI, sekrety, dane, README, CHANGELOG, licencję", "Liczbę commitów", "Nic"], 1, "Lista kontrolna."),
          T("Retrospektywa służy do:", ["Oceniania klienta", "Wniosków na kolejny projekt", "Usuwania historii", "Marketingu"], 1, "Ciągłe doskonalenie.")],
    w_praktyce=["Każde wydanie: lista kontrolna + CHANGELOG + tag.", "Retrospektywa po każdym projekcie — 30 minut."],
    zrodla=[Z_SEMVER, Z_KEEPCL, Z_GH_REL, Z_RETRO],
)

POWTORKA_3 = L(
    id="powtorka_etap_3", nazwa="Podsumowanie kursu: Twój proces, mapa dalszej nauki i plan utrzymania wiedzy", tydzien=15,
    slowa=["podsumowanie", "proces", "nawyki", "dalsza nauka", "aktualizacje", "plan", "etap 3"],
    cel="Po tej lekcji masz spisany własny proces pracy z agentami (jedna strona), plan nauki na 3 miesiące i plan sprawdzania zmian w narzędziach, cenach i przepisach.",
    po_co="Narzędzia AI zmieniają się co kilka tygodni; proces i nawyki zostają. Kurs kończy się, praca dopiero zaczyna.",
    wymagania=["Projekt końcowy wydany (albo w ostatnim kamieniu).", "Dziennik z całego kursu."],
    wyjasnienie=(
        "## Twój proces na jednej stronie (wzór)\n"
        "| faza | Twój nawyk |\n"
        "|---|---|\n"
        "| zlecenie | wymagania z kryteriami, poza zakresem, pytania |\n"
        "| specyfikacja | 7 sekcji, przykłady i brzegi |\n"
        "| testy | ze specyfikacji, przed kodem, sprawdzone mutantem |\n"
        "| agent | AGENTS.md, tryb planu, małe kroki, notatka stanu, /clear |\n"
        "| przegląd | 8 pytań + 6 dziur bezpieczeństwa, recenzja AI w nowej sesji |\n"
        "| Git | gałąź, PR, CI, merge tylko na zielono |\n"
        "| sekrety i dane | zmienne środowiskowe, deny, dane fikcyjne, RODO |\n"
        "| wydanie | lista kontrolna, CHANGELOG, tag, retrospektywa |\n"
        "## Co sprawdzać regularnie (kalendarz w Ściądze)\n"
        "- Ceny i limity planów (co kwartał) — strony cenników Anthropic i OpenAI.\n"
        "- Nowe wersje Claude Code i Codex (`claude --version`, `codex --version`, informacje o zmianach) — tryby uprawnień i domyślne ustawienia się zmieniają.\n"
        "- AI Act: 2.12.2026 (koniec okresu przejściowego art. 50), 2.12.2027 (wysokie ryzyko, załącznik III).\n"
        "- Limit działalności nierejestrowanej — co roku w styczniu (zależy od minimalnego wynagrodzenia).\n"
        "- Zależności projektów — raz na kwartał aktualizacja z testami.\n"
        "## Dalsza nauka (wybierz jedną ścieżkę na 3 miesiące)\n"
        "| cel | następny krok |\n"
        "|---|---|\n"
        "| tester / QA | kurs „Python od zera → Junior QA” w Mentorze, pytest głębiej, Selenium |\n"
        "| aplikacje webowe | szablony Jinja, formularze, autoryzacja (z dużą ostrożnością), hosting PaaS |\n"
        "| dane i automatyzacje | pandas, Excel z Pythona (openpyxl), API usług w Twojej branży |\n"
        "| zlecenia | 1 płatne małe zlecenie z pełnym procesem (wymagania → wydanie) |\n"
        "## Ostatnia rada\n"
        "Najważniejsza umiejętność z kursu to nie żadne polecenie, tylko pytanie: „Skąd wiem, że to działa?”. Zadawaj je agentowi, sobie i każdemu narzędziu."),
    przyklad=("Fragment proces.md:\n\n# Mój proces pracy z agentami\n1. Wymagania → potwierdzenie klienta.\n2. Specyfikacja z 6+ przykładami.\n3. Testy ze specyfikacji (czerwone).\n"
              "4. Agent w trybie planu: punkt po punkcie, test po każdym.\n5. Przegląd: 8 pytań + 6 dziur; recenzja AI w nowej sesji.\n6. PR → CI → merge.\n7. Raz na kwartał: ceny, wersje narzędzi, zależności."),
    demonstracja={"tytul": "Przegląd dziennika z 16 tygodni", "kroki": [
        "Przeglądasz wpisy „czego nie rozumiem” — 3 tematy powtarzają się (np. daty, SQL, CI). To lista do dalszej nauki.",
        "Liczysz iteracje z agentem na zadanie: tydzień 4 — średnio 5, tydzień 11 — średnio 2. Dowód postępu do rozmowy rekrutacyjnej.",
        "Najczęstsze porażki agenta z Twojego dziennika → 3 nowe linie do szablonu AGENTS.md na kolejne projekty.",
        "Spisujesz proces na jedną stronę i plan 3 miesięcy z jednym celem."],
        "wynik": "Proces na jednej stronie, szablon AGENTS.md z doświadczeń, plan nauki i kalendarz sprawdzania zmian."},
    jak_uruchomic=["Zadanie tygodnia „proces.md i plan 3 miesięcy”.", "Ściąga → kalendarz aktualizacji."],
    cwiczenia=[
        C("prowadzone",
          "Uporządkuj fazy procesu: A) przegląd, B) specyfikacja, C) testy, D) wydanie, E) wymagania, F) agent w małych krokach. Ciąg liter. Czas: 15 minut.",
          "EBCFAD.",
          ["Najpierw rozmowa z klientem.", "Testy przed agentem.", "Wydanie na końcu."],
          "Wymagania → specyfikacja → testy → agent → przegląd → wydanie = EBCFAD.",
          [tx("kol", "Kolejność", ["EBCFAD"])]),
        C("samodzielne",
          "Kalendarz: (1) do kiedy trwa okres przejściowy art. 50 AI Act (data), (2) jak często sprawdzasz ceny planów (opcje: co tydzień / co kwartał / raz w życiu), (3) kiedy sprawdzasz limit działalności nierejestrowanej (opcje: w styczniu / w lipcu / nigdy). Czas: 15 minut.",
          "(1) 2026-12-02; (2) co kwartał; (3) w styczniu.",
          ["Data z lekcji „Prawo”.", "Ceny zmieniają się kilka razy w roku.", "Minimalne wynagrodzenie zmienia się od stycznia."],
          "2.12.2026; co kwartał; w styczniu.",
          [dict(id="d", etykieta="(1) Data", typ="data", wartosc="2026-12-02"), wy("ceny", "(2) Ceny planów", ["co tydzień", "co kwartał", "raz w życiu"], "co kwartał"),
           wy("limit", "(3) Limit nierejestrowanej", ["w styczniu", "w lipcu", "nigdy"], "w styczniu")]),
    ],
    typowe_bledy=[
        B("Po kursie wracasz do „kopiuj-wklej bez testów”.", "Brak spisanego procesu i szablonów.", "Czy masz proces.md i szablony?", "Szablony (specyfikacja, AGENTS.md, PR) w Mentorze → Ściąga; proces na jednej stronie przy biurku."),
        B("Instrukcje z kursu przestały pasować do nowej wersji narzędzia.", "Zmiany w narzędziach (tryby, polecenia).", "Wersja narzędzia i informacje o zmianach.", "Kalendarz aktualizacji; zasady (testy, przegląd, sekrety) są niezależne od wersji."),
    ],
    pulapki=["Nie goń każdego nowego narzędzia — sprawdzaj je na tej samej specyfikacji i testach, którymi oceniasz obecne.", "Ucz się dalej czytania kodu — to umiejętność, której AI nie zastąpi Ci na rozmowie i przy odbiorze."],
    zadania=["Napisz proces.md i plan 3 miesięcy (zadanie tygodnia).", "Przejrzyj dziennik i zapisz 3 wnioski.", "Ustaw przypomnienia z kalendarza aktualizacji."],
    pytania=[["Jakie pytanie jest najważniejsze w vibe codingu?", "„Skąd wiem, że to działa?”"], ["Co sprawdzasz co kwartał?", "Ceny i limity planów, wersje narzędzi, zależności projektów."],
             ["Jak wybierasz dalszą naukę?", "Jedna ścieżka na 3 miesiące, z konkretnym celem i projektem."]],
    podsumowanie="Masz własny proces pracy z agentami na jednej stronie, plan dalszej nauki i kalendarz sprawdzania zmian — kurs zamknięty, nawyki zostają.",
    test=[T("Pierwsza faza procesu przy zleceniu:", ["Agent", "Wymagania z kryteriami", "Wydanie", "CI"], 1, "Od klienta."),
          T("Nowe narzędzie AI sprawdzasz:", ["Na nowym, ciekawym projekcie bez testów", "Na tej samej specyfikacji i testach co obecne", "Czytając reklamy", "Wcale"], 1, "Porównanie na tym samym."),
          T("Umiejętność, której AI nie zastąpi na rozmowie:", ["Pisanie promptów", "Czytanie i wyjaśnianie kodu", "Instalacja", "Kopiowanie"], 1, "Ćwiczona od tygodnia 1.")],
    w_praktyce=["proces.md przy biurku.", "Kwartalny przegląd: ceny, wersje, zależności."],
    zrodla=[Z_CC_BEST, Z_SO, ["Rozporządzenie (UE) 2026/1744 („Digital Omnibus” dla AI Act) — EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2026/1744/oj", "dostęp 24.11.2026"]],
)
