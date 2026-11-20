# -*- coding: utf-8 -*-
"""Etap 1, tygodnie 4–5: konta i koszty, instalacja Claude Code i Codex, sesja agenta, instrukcje projektu, małe kroki."""

from wspolne import (TN, B, C, L, T, bl, kw, li, tx, wy)

D = "dostęp 19.11.2026"
Z_CC_SETUP = ["Claude Code — Set up Claude Code (instalacja, wymagania, Windows)", "https://code.claude.com/docs/en/setup", D]
Z_CC_TERM = ["Claude Code — Terminal guide for new users", "https://code.claude.com/docs/en/terminal-guide", D]
Z_CC_COSTS = ["Claude Code — Manage costs effectively (/usage, /context, /clear, /compact)", "https://code.claude.com/docs/en/costs", D]
Z_CC_MODES = ["Claude Code — Permission modes (default, acceptEdits, plan, auto…)", "https://code.claude.com/docs/en/permission-modes", D]
Z_CC_PERM = ["Claude Code — Configure permissions (reguły allow/ask/deny, /permissions)", "https://code.claude.com/docs/en/permissions", "dostęp 20.11.2026"]
Z_CC_MEM = ["Claude Code — How Claude remembers your project (CLAUDE.md, @import, AGENTS.md)", "https://code.claude.com/docs/en/memory", D]
Z_CC_CHECK = ["Claude Code — Checkpointing (/rewind, Esc Esc)", "https://code.claude.com/docs/en/checkpointing", D]
Z_CC_BEST = ["Claude Code — Best practices", "https://code.claude.com/docs/en/best-practices", D]
Z_CL_PLANS = ["Claude Help Center — Using Claude Code with your Pro or Max plan", "https://support.claude.com/en/articles/14552983", D]
Z_CL_PRICE = ["Ceny planów Claude 2026 — zestawienie (dupple.com, 2.11.2026)", "https://dupple.com/learn/claude-code-pricing", D]
Z_CX_README = ["OpenAI Codex CLI — README (instalacja, logowanie, licencja Apache-2.0)", "https://cdn.jsdelivr.net/gh/openai/codex@main/README.md", D]
Z_CX_WIN = ["Codex — aplikacja na Windows (ChatGPT desktop, sandbox Windows, WSL2)", "https://learn.chatgpt.com/docs/app/windows", D]
Z_CX_PERM = ["Codex — Permission modes (Ask for approval, Approve for me, Full access)", "https://learn.chatgpt.com/docs/permission-modes", D]
Z_CX_SAND = ["Codex — Sandboxing (read-only, workspace-write, danger-full-access)", "https://learn.chatgpt.com/docs/sandboxing?surface=cli", D]
Z_CX_PRICE = ["Codex — Pricing (plany ChatGPT i dostęp do Codex)", "https://chatgpt.com/codex/pricing/", D]
Z_CX_AGENTS = ["Codex — Custom instructions with AGENTS.md (kolejność, limit 32 KiB)", "https://learn.chatgpt.com/docs/agent-configuration/agents-md", "dostęp 20.11.2026"]
Z_CX_SLASH = ["Codex CLI — slash commands (/init, /diff, /status, /compact, /new, /review, /permissions)", "https://developers.openai.com/codex/cli/slash-commands", "dostęp 20.11.2026"]


# =========================================================================== TYDZIEŃ 4
KONTA = L(
    id="konta_koszty", nazwa="Konta, plany i koszty: ile naprawdę kosztuje agent", tydzien=4,
    slowa=["plan", "subskrypcja", "limit", "API", "token", "koszt", "Pro", "Plus", "VAT"],
    cel="Po tej lekcji wybierasz jeden plan (albo ścieżkę bez konta), liczysz koszt miesięczny z VAT, rozumiesz limity 5-godzinne i tygodniowe oraz różnicę między subskrypcją a płatnością za tokeny (API).",
    po_co="Źle dobrany plan to albo przepłacanie, albo blokada w połowie zadania. Klient zapyta też, ile kosztuje utrzymanie rozwiązania.",
    wymagania=["Lekcja „Jak działa model AI” (tokeny).", "Decyzja budżetowa z planu nauki (zadanie v0z1)."],
    wyjasnienie=(
        "## Dwa narzędzia, dwa ekosystemy\n"
        "| | Claude Code (Anthropic) | Codex (OpenAI) |\n"
        "|---|---|---|\n"
        "| dostęp w planie | Pro, Max, Team, Enterprise; darmowy plan claude.ai NIE obejmuje Claude Code | ChatGPT Plus i wyższe: CLI, IDE, web; Free i Go — ograniczony dostęp tylko w aplikacji desktop (wdrażany stopniowo) |\n"
        "| najtańszy pełny plan | Pro: 20 USD/mies. (17 USD przy płatności rocznej) | Plus: 20 USD/mies. |\n"
        "| wyższe plany | Max 5x: 100 USD, Max 20x: 200 USD | Pro: od 100 USD |\n"
        "| płatność za użycie | konto API (Console) — płacisz za tokeny | klucz API — płacisz za tokeny |\n"
        "Ceny podano bez podatku (stan: listopad 2026). W Polsce dolicza się VAT 23%: 20 USD × 1,23 = 24,60 USD, czyli ok. 90–100 zł zależnie od kursu dolara. "
        "Ceny i nazwy planów zmieniają się kilka razy w roku — kalendarz aktualizacji kursu przypomina, kiedy sprawdzić strony cenników.\n"
        "## Limity: okno 5-godzinne i tygodniowe\n"
        "Subskrypcja to nie „bez limitu”. Oba narzędzia liczą użycie w oknach: krótkim (ok. 5 godzin) i tygodniowym. Po przekroczeniu Claude Code pokazuje komunikat o limicie sesji lub tygodnia i trzeba poczekać (albo dokupić użycie). "
        "W Claude Code stan limitów pokazuje polecenie `/usage`, w Codex — `/status`.\n"
        "## Subskrypcja czy API?\n"
        "- Subskrypcja: stała cena, limity. Dla nauki i małych projektów — prawie zawsze lepsza.\n"
        "- API: płacisz za każdy token, bez sufitu. Dokumentacja Claude Code podaje, że w firmach średni koszt to ok. 13 USD na programistę na aktywny dzień, 150–250 USD miesięcznie. Dla początkującego to łatwa droga do niespodzianki na karcie.\n"
        "## Co zużywa limit najszybciej\n"
        "- Długie rozmowy (cały kontekst jest wysyłany za każdym razem) — tydzień 7.\n"
        "- Ogólne polecenia („popraw cały projekt”) — agent czyta wszystko.\n"
        "- Najmocniejszy model do prostych zadań (`/model` zmienia model).\n"
        "## Decyzja dla kursu\n"
        "- Wystarczy JEDEN plan: Claude Pro albo ChatGPT Plus. Lekcje pokazują oba narzędzia; zadania wykonasz tym, które masz.\n"
        "- Kup na miesiąc, ustaw przypomnienie o odnowieniu, oceniaj po 2 tygodniach w `/usage` / `/status`.\n"
        "- Ścieżka bez konta: każde zadanie z agentem ma zapis jego pracy z jednym celowo wstawionym błędem — ćwiczysz czytanie i poprawianie kodu agenta.\n"
        "## Bezpieczeństwo konta\n"
        "Włącz weryfikację dwuetapową (2FA) na koncie Anthropic/OpenAI i GitHub. Nie udostępniaj konta innym — dostęp do agenta to dostęp do Twoich plików."),
    przyklad=("Kalkulacja na kartce (kurs 3,80 zł/USD — wpisz aktualny):\n\n"
              "Claude Pro: 20 USD × 1,23 VAT = 24,60 USD × 3,80 = 93,48 zł/mies.\n"
              "4 miesiące kursu (tydzień 4–15, ok. 3 miesiące + zapas): ok. 280–375 zł.\n"
              "Alternatywa API: 13 USD dziennie × 20 dni = 260 USD = ok. 990 zł/mies. bez VAT — dlatego dla nauki wybieramy subskrypcję."),
    demonstracja={"tytul": "Sprawdzenie cennika i decyzja w 10 minut", "kroki": [
        "Otwórz claude.com/pricing i chatgpt.com/codex/pricing (oficjalne strony). Zanotuj cenę najtańszego planu, który daje agenta w terminalu, i datę sprawdzenia.",
        "Policz koszt z VAT i aktualnym kursem dolara (kurs średni NBP z nbp.pl). Zapisz w koszty.md.",
        "Zadaj sobie pytanie: z którego ekosystemu już korzystasz (masz ChatGPT Plus? — wybierz Codex)? Jeśli żadnego — wybierz jeden i nie zmieniaj przez miesiąc.",
        "Ustaw w kalendarzu przypomnienie 2 dni przed odnowieniem: „ocenić /usage — zostaję, zmieniam, rezygnuję?”."],
        "wynik": "Masz decyzję z kwotą w złotych, datą sprawdzenia ceny i przypomnieniem — bez dwóch planów „na zapas”."},
    jak_uruchomic=["Przeglądarka → claude.com/pricing, chatgpt.com/codex/pricing.", "Po zakupie: w Claude Code `/usage`, w Codex `/status`."],
    cwiczenia=[
        C("prowadzone",
          "Policz: (1) koszt planu za 20 USD z VAT 23% w dolarach, (2) w złotych przy kursie 3,80 zł/USD, (3) ile zapłacisz przez 3 miesiące. Czas: 15 minut.",
          "(1) 24,60 USD; (2) 93,48 zł; (3) 280,44 zł.",
          ["VAT doliczasz mnożąc przez 1,23.", "Dolary na złote: razy kurs.", "Trzy miesiące: razy 3."],
          "20 × 1,23 = 24,60 USD; 24,60 × 3,80 = 93,48 zł; 93,48 × 3 = 280,44 zł.",
          [kw("usd", "Koszt z VAT (USD)", 24.60, bledy=[bl(20, "to cena bez podatku — w Polsce doliczasz VAT 23%")]),
           kw("pln", "Koszt miesięczny (zł)", 93.48, bledy=[bl(76.0, "przeliczyłeś cenę bez VAT")]), kw("kw", "3 miesiące (zł)", 280.44)]),
        C("samodzielne",
          "Dopasuj: (1) masz już ChatGPT Plus, (2) nie masz żadnego planu i chcesz zacząć od Claude Code, (3) nie możesz teraz płacić, (4) ktoś radzi „weź klucz API, będzie taniej” — Ty uczysz się 2 godziny dziennie. "
          "Opcje: Codex w ramach Plus / Claude Pro / ścieżka bez konta / zostań przy subskrypcji. Czas: 15 minut.",
          "(1) Codex w ramach Plus; (2) Claude Pro; (3) ścieżka bez konta; (4) zostań przy subskrypcji — API bez sufitu łatwo przekracza 20 USD miesięcznie.",
          ["Masz już plan — nie kupuj drugiego.", "Claude Code wymaga co najmniej Pro.", "API to płatność za każdy token, bez górnej granicy."],
          "(1) Codex z Plus; (2) Claude Pro; (3) ścieżka bez konta; (4) subskrypcja — przewidywalny koszt.",
          [wy("s1", "(1) Mam ChatGPT Plus", ["Codex w ramach Plus", "Claude Pro", "ścieżka bez konta", "zostań przy subskrypcji"], "Codex w ramach Plus"),
           wy("s2", "(2) Brak planu, chcę Claude Code", ["Codex w ramach Plus", "Claude Pro", "ścieżka bez konta", "zostań przy subskrypcji"], "Claude Pro"),
           wy("s3", "(3) Nie mogę teraz płacić", ["Codex w ramach Plus", "Claude Pro", "ścieżka bez konta", "zostań przy subskrypcji"], "ścieżka bez konta"),
           wy("s4", "(4) Rada: klucz API zamiast planu", ["Codex w ramach Plus", "Claude Pro", "ścieżka bez konta", "zostań przy subskrypcji"], "zostań przy subskrypcji")]),
    ],
    typowe_bledy=[
        B("„You've hit your session limit” w środku zadania.", "Wyczerpane okno 5-godzinne (długa sesja, duży kontekst).", "`/usage` (Claude Code) albo `/status` (Codex).", "Poczekaj do odnowienia okna; na przyszłość krótsze sesje, `/clear` między zadaniami (tydzień 7)."),
        B("Claude Code po zalogowaniu mówi, że plan nie obejmuje dostępu.", "Darmowy plan claude.ai nie obejmuje Claude Code.", "Ustawienia konta na claude.ai → plan.", "Pro lub wyższy albo konto API (Console); albo ścieżka bez konta."),
        B("Rachunek API wyższy niż subskrypcja.", "Płatność za tokeny bez limitu.", "Panel rozliczeń dostawcy.", "Ustaw limit wydatków w panelu API albo wróć do subskrypcji."),
    ],
    pulapki=["Ceny w dolarach bez VAT — porównując oferty licz zawsze kwotę z VAT w złotych.",
             "Reklamy „najlepszego narzędzia” zmieniają się co miesiąc. Umiejętności z kursu (specyfikacja, testy, przegląd zmian) przenoszą się na każde narzędzie."],
    zadania=["Zapisz w koszty.md decyzję z kwotą w złotych i datą sprawdzenia ceny.", "Włącz 2FA na koncie dostawcy AI.", "Ustaw przypomnienie przed odnowieniem planu."],
    pytania=[["Czy darmowy plan claude.ai daje Claude Code?", "Nie — potrzebny Pro, Max, Team, Enterprise albo konto API."],
             ["Czym różni się subskrypcja od API?", "Subskrypcja: stała cena z limitami okien; API: płatność za każdy token bez sufitu."],
             ["Jak sprawdzisz, ile limitu zostało?", "W Claude Code `/usage`, w Codex `/status`."]],
    podsumowanie="Wybierasz jeden plan albo ścieżkę bez konta, liczysz koszt z VAT, rozumiesz okna limitów i dlaczego API nie jest „tańsze” dla początkującego.",
    test=[T("Ile planów płatnych potrzebujesz do kursu?", ["0 — zawsze", "1 (albo ścieżka bez konta)", "2", "3"], 1, "Claude Pro albo ChatGPT Plus."),
          T("20 USD + VAT 23% to:", ["20 USD", "23 USD", "24,60 USD", "26 USD"], 2, "20 × 1,23."),
          T("Polecenie pokazujące limity w Claude Code:", ["/usage", "/limits", "/money", "/help"], 0, "Paski okien limitów."),
          T("Dlaczego API bywa ryzykowne dla początkującego?", ["Jest wolniejsze", "Płacisz za każdy token, bez sufitu", "Nie działa na Windows", "Wymaga Linuksa"], 1, "Niespodzianka na karcie.")],
    w_praktyce=["Koszt narzędzi wpisuj do wyceny dla klienta.", "Raz w miesiącu: /usage i decyzja o planie."],
    zrodla=[Z_CL_PLANS, Z_CL_PRICE, Z_CX_PRICE, Z_CC_COSTS],
)

INST_CC = L(
    id="instalacja_claude_code", nazwa="Instalacja Claude Code w Windows i pierwsze uruchomienie", tydzien=4,
    slowa=["Claude Code", "instalacja", "PowerShell", "claude --version", "claude doctor", "PATH", "logowanie"],
    cel="Po tej lekcji masz zainstalowany Claude Code, sprawdzasz go `claude --version` i `claude doctor`, logujesz się i uruchamiasz pierwszą sesję w katalogu PRACA — albo wiesz, jak naprawić najczęstsze błędy instalacji.",
    po_co="Agent musi działać w Twoim katalogu projektu. Instalacja z oficjalnego adresu i sprawdzenie wersji to też pierwsza lekcja bezpieczeństwa.",
    wymagania=["Windows 10 w wersji 1809 lub nowszej (albo Windows 11), 4 GB RAM, internet.", "Plan Claude Pro lub wyższy (do logowania; samą instalację możesz zrobić bez planu).", "Lekcja „Terminal bez strachu”."],
    wyjasnienie=(
        "## Trzy sposoby instalacji (wybierz jeden)\n"
        "| sposób | gdzie wpisujesz | polecenie |\n"
        "|---|---|---|\n"
        "| PowerShell (zalecany) | Windows PowerShell — zachęta `PS C:\\…>` | `irm https://claude.ai/install.ps1 \\| iex` |\n"
        "| CMD | Wiersz polecenia (np. terminal Mentora) | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |\n"
        "| WinGet | PowerShell lub CMD | `winget install Anthropic.ClaudeCode` (bez automatycznych aktualizacji) |\n"
        "Uprawnienia administratora NIE są potrzebne. Instalator nie pokazuje paska postępu — poczekaj, aż wróci zachęta. "
        "Dokumentacja: w PowerShell błąd „The token '&&' is not a valid statement separator” znaczy, że wkleiłeś komendę CMD; „'irm' is not recognized” — że jesteś w CMD.\n"
        "## Sprawdzenie\n"
        "Zamknij i otwórz NOWE okno terminala (nowe okno wczytuje zaktualizowaną ścieżkę PATH). Wpisz `claude --version` — zobaczysz numer wersji i „(Claude Code)”. "
        "`claude doctor` sprawdza instalację i ustawienia (tylko odczyt, niczego nie zmienia).\n"
        "## Najczęstsze problemy (z dokumentacji)\n"
        "- „'claude' is not recognized…” — folder `%USERPROFILE%\\.local\\bin` nie jest w PATH. Dokumentacja podaje dwie linie PowerShell dopisujące go do PATH użytkownika (są w sekcji Typowe błędy). Potem nowe okno.\n"
        "- Błędy SSL/TLS na starszym Windows 10 — w PowerShell najpierw `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`, potem instalacja.\n"
        "- Komunikat o architekturze 32-bit — otworzyłeś „Windows PowerShell (x86)”; użyj zwykłego PowerShell.\n"
        "## Git for Windows — opcjonalny teraz, potrzebny w tygodniu 6\n"
        "Claude Code działa bez Gita (używa wtedy PowerShell jako narzędzia powłoki). Z zainstalowanym Git for Windows może używać Git Bash. W tygodniu 6 i tak zainstalujesz Gita.\n"
        "## Pierwsze uruchomienie\n"
        "- Mentor → Mój projekt → „Otwórz Claude Code tutaj” (uruchamia `claude` w PRACA). Albo terminal Mentora → `claude`.\n"
        "- Przy pierwszym starcie: wybór motywu i logowanie w przeglądarce (konto z planem Pro/Max albo konto Console).\n"
        "- Claude Code zapyta, czy ufasz temu folderowi — potwierdzasz tylko dla katalogu PRACA, nie dla całego dysku ani folderu Użytkownika.\n"
        "- `/help` — lista poleceń; Esc — przerwanie pracy agenta; `exit` albo dwa razy Ctrl + D — wyjście.\n"
        "## Bez terminala?\n"
        "Claude Code jest też w aplikacji desktop Claude, w rozszerzeniu VS Code i w przeglądarce (claude.ai/code). Kurs uczy terminala, bo tam najlepiej widać, co agent robi — ale umiejętności są te same.\n"
        "## Na natywnym Windows nie ma piaskownicy\n"
        "Dokumentacja: izolacja (sandboxing) komend nie jest obsługiwana na natywnym Windows (działa w WSL2). Dlatego tryby uprawnień i Twoja kontrola zmian są tu jeszcze ważniejsze (tydzień 5)."),
    przyklad=("PS C:\\Users\\Anna> irm https://claude.ai/install.ps1 | iex\n"
              "... (instalacja, kilka minut bez paska postępu)\n"
              "PS C:\\Users\\Anna> exit\n\n"
              "(nowe okno)\nPS C:\\Users\\Anna> claude --version\n2.1.290 (Claude Code)\n"
              "PS C:\\Users\\Anna> claude doctor\n(raport: wersja, metoda instalacji, ustawienia — bez błędów)"),
    demonstracja={"tytul": "Instalacja i pierwsza sesja w PRACA", "kroki": [
        "Win + X → „Terminal” (albo „Windows PowerShell”). Zachęta zaczyna się od PS. Wklej komendę z adresem https://claude.ai/install.ps1 — dokładnie z dokumentacji, nie z forum.",
        "Poczekaj na powrót zachęty. Zamknij okno, otwórz nowe, `claude --version` — numer wersji. `claude doctor` — bez czerwonych pozycji.",
        "Mentor → Środowisko → „🔍 Sprawdź ponownie”: narzędzie „claude” ma zielony znacznik.",
        "Mój projekt → „Otwórz Claude Code tutaj”. Zaloguj się w przeglądarce. Na pytanie o zaufanie folderowi sprawdź ścieżkę — ma kończyć się na \\PRACA.",
        "Pierwsza prośba (tylko odczyt): „Wypisz pliki w tym katalogu i w jednym zdaniu powiedz, co robi kalkulator_pobytu.py. Niczego nie zmieniaj.” Agent czyta pliki bez pytania o zgodę (odczyt w katalogu roboczym nie wymaga zgody) i odpowiada.",
        "Wyjdź: `exit`. Zapisz w instalacja.txt wynik `claude --version` (zadanie tygodnia)."],
        "wynik": "Działający Claude Code w PRACA, potwierdzony wersją i claude doctor; pierwsza sesja tylko do odczytu."},
    jak_uruchomic=["PowerShell → `irm https://claude.ai/install.ps1 | iex` → nowe okno → `claude --version`.", "Mentor → Mój projekt → „Otwórz Claude Code tutaj”."],
    cwiczenia=[
        C("prowadzone",
          "Masz okno z zachętą `PS C:\\Users\\Anna>`. (1) Którą komendę instalacji wkleisz: ps1 czy cmd? (2) Po instalacji `claude --version` daje „'claude' is not recognized”. Co robisz NAJPIERW: nowe okno czy reinstalacja? "
          "(3) Jakim poleceniem sprawdzisz instalację bez zmieniania czegokolwiek? Czas: 15 minut.",
          "(1) ps1 (PowerShell); (2) najpierw nowe okno terminala (PATH), dopiero potem poprawka PATH z dokumentacji; (3) `claude doctor`.",
          ["PS na początku zachęty = PowerShell.", "Stare okno nie widzi nowego PATH.", "Polecenie diagnostyczne ma w nazwie „lekarza”."],
          "PowerShell → install.ps1. „not recognized” tuż po instalacji to zwykle stare okno — otwórz nowe; jeśli dalej — dopisz %USERPROFILE%\\.local\\bin do PATH. Diagnostyka: claude doctor.",
          [wy("kom", "(1) Komenda instalacji", ["ps1", "cmd"], "ps1"), wy("najpierw", "(2) Co najpierw?", ["nowe okno", "reinstalacja"], "nowe okno"),
           tx("diag", "(3) Polecenie diagnostyczne", ["claude doctor"], bledy=[bl("claude --version", "to tylko numer wersji; pełną diagnostykę daje claude doctor")])]),
        C("samodzielne",
          "Claude Code przy pierwszym uruchomieniu pyta, czy ufasz folderowi. Ścieżka to (A) `C:\\Users\\Anna`, (B) `C:\\Users\\Anna\\Documents\\Mentor\\vibe-coding\\PRACA`, (C) `C:\\`. Który potwierdzisz? "
          "Druga sprawa: czy na natywnym Windows Claude Code izoluje komendy w piaskownicy (tak/nie)? Czas: 15 minut.",
          "Tylko B (katalog projektu). Nie — na natywnym Windows sandboxing nie jest obsługiwany (WSL2 tak).",
          ["Zaufanie = agent pracuje na plikach tego folderu.", "Folder użytkownika zawiera dokumenty, zdjęcia, hasła przeglądarki.", "Dokumentacja: sandboxing tylko macOS/Linux/WSL2."],
          "B — wyłącznie katalog projektu. Piaskownicy na natywnym Windows nie ma — tym ważniejsze są tryby uprawnień i przegląd zmian.",
          [wy("folder", "Który folder potwierdzisz?", ["A", "B", "C"], "B", bledy=[bl("A", "folder użytkownika to wszystkie Twoje dokumenty — agent nie powinien mieć do nich dostępu")]),
           wy("sandbox", "Czy jest piaskownica na natywnym Windows?", TN, "nie")]),
    ],
    typowe_bledy=[
        B("„'claude' is not recognized as an internal or external command” w nowym oknie.", "Folder %USERPROFILE%\\.local\\bin nie trafił do PATH.", "`claude doctor` nie działa; sprawdź, czy istnieje plik %USERPROFILE%\\.local\\bin\\claude.exe.",
          "PowerShell: `$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')` i `[Environment]::SetEnvironmentVariable('PATH', \"$currentPath;$env:USERPROFILE\\.local\\bin\", 'User')`, potem nowe okno (polecenia z dokumentacji)."),
        B("„The token '&&' is not a valid statement separator”.", "Komenda CMD wklejona do PowerShell.", "Zachęta zaczyna się od PS?", "Użyj wersji irm … install.ps1 | iex albo otwórz CMD."),
        B("Błąd SSL/TLS przy pobieraniu.", "Starszy Windows 10 bez TLS 1.2 domyślnie.", "Wersja Windows (winver).", "W PowerShell: `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`, potem instalacja."),
    ],
    pulapki=["Instaluj wyłącznie z adresu claude.ai/install… lub przez winget z identyfikatorem Anthropic.ClaudeCode. Strony „Claude Code za darmo” i paczki o podobnych nazwach to częsta pułapka.",
             "Nie uruchamiaj Claude Code w C:\\ ani w folderze użytkownika — agent widzi wtedy wszystkie Twoje pliki."],
    zadania=["Zainstaluj Claude Code i zapisz wynik `claude --version` w instalacja.txt.", "Uruchom `claude doctor` i przeczytaj raport.", "Pierwsza sesja tylko do odczytu w PRACA."],
    pytania=[["Jak sprawdzisz, że instalacja się udała?", "Nowe okno → `claude --version` (numer wersji) i `claude doctor`."],
             ["Dlaczego otwierasz nowe okno po instalacji?", "Stare okno ma starą wartość PATH i nie widzi programu."],
             ["Jakiemu folderowi ufasz przy pierwszym uruchomieniu?", "Tylko katalogowi projektu (PRACA)."]],
    podsumowanie="Instalujesz Claude Code z oficjalnego adresu, sprawdzasz wersję i claude doctor, naprawiasz PATH i TLS, uruchamiasz pierwszą sesję tylko w PRACA.",
    test=[T("Zalecana komenda instalacji w PowerShell:", ["pip install claude", "irm https://claude.ai/install.ps1 | iex", "npm i claude-free", "winget install claude-pl"], 1, "Z dokumentacji."),
          T("Czy instalacja Claude Code wymaga uprawnień administratora?", ["Tak", "Nie", "Tylko na Windows 11", "Tylko przez WinGet"], 1, "Instaluje się w profilu użytkownika."),
          T("Polecenie wyjścia z sesji Claude Code:", ["exit", "quit!", "Alt + F4 zawsze", "logout"], 0, "Albo dwa razy Ctrl + D."),
          T("„'irm' is not recognized” znaczy:", ["Brak internetu", "Jesteś w CMD, a komenda jest dla PowerShell", "Zły plan", "Za stary Python"], 1, "Wskazówka z dokumentacji.")],
    w_praktyce=["Raz w miesiącu `claude doctor`.", "Wersję narzędzia zapisuj w README projektu przy zgłaszaniu błędów."],
    zrodla=[Z_CC_SETUP, Z_CC_TERM, Z_CL_PLANS],
)

INST_CODEX = L(
    id="instalacja_codex", nazwa="Codex: CLI i aplikacja na Windows, logowanie i tryby pracy", tydzien=4,
    slowa=["Codex", "CLI", "aplikacja", "sandbox", "workspace-write", "logowanie", "ChatGPT"],
    cel="Po tej lekcji instalujesz Codex (CLI w PowerShell albo aplikację ChatGPT desktop), logujesz się kontem ChatGPT, rozumiesz piaskownicę workspace-write i wybierasz bezpieczny tryb uprawnień.",
    po_co="Codex to drugi wiodący agent kodujący. Kto zna oba, umie przenieść nawyki między narzędziami — a rynek pracy wymaga elastyczności.",
    wymagania=["Windows 10/11, internet.", "Plan ChatGPT Plus lub wyższy dla CLI (Free i Go — ograniczony dostęp tylko w aplikacji, wdrażany stopniowo).", "Lekcja „Instalacja Claude Code” (analogiczne kroki)."],
    wyjasnienie=(
        "## Dwie formy Codex\n"
        "| | Codex CLI (terminal) | Codex w aplikacji ChatGPT desktop |\n"
        "|---|---|---|\n"
        "| instalacja | PowerShell: `powershell -ExecutionPolicy ByPass -c \"irm https://chatgpt.com/codex/install.ps1 \\| iex\"` albo `npm install -g @openai/codex` (wymaga Node.js) | Microsoft Store albo `winget install --id 9PLM9XGG6VKS -s msstore` |\n"
        "| start | `codex` w katalogu projektu | wybierasz folder projektu w aplikacji |\n"
        "| izolacja na Windows | natywna piaskownica Windows albo WSL2 | natywna piaskownica Windows albo WSL2 |\n"
        "Logowanie: „Sign in with ChatGPT” (konta Plus, Pro, Business, Edu, Enterprise) albo klucz API (płatność za tokeny — lekcja o kosztach). Codex CLI jest otwartym oprogramowaniem (licencja Apache-2.0).\n"
        "## Piaskownica (sandbox) — co agent może dotknąć\n"
        "| tryb piaskownicy | co wolno |\n"
        "|---|---|\n"
        "| read-only | tylko czytać pliki |\n"
        "| workspace-write | czytać i zmieniać pliki w katalogu projektu; wyjście poza katalog lub internet wymaga zgody |\n"
        "| danger-full-access | wszystko na komputerze i w sieci — tylko w izolowanych maszynach |\n"
        "## Tryby uprawnień (aplikacja i CLI)\n"
        "- „Ask for approval” — pracuje w katalogu projektu, pyta przed wyjściem poza niego i przed dostępem do internetu. Tryb startowy w kursie.\n"
        "- „Approve for me” — Codex sam ocenia prośby o zgodę (automatyczny przegląd). Wygodniej, mniej kontroli.\n"
        "- „Full access” — cały komputer i internet bez pytania. W kursie: nigdy.\n"
        "W CLI tryb zmienisz poleceniem `/permissions`; przy starcie możesz go podać jawnie: `codex --sandbox workspace-write --ask-for-approval on-request`.\n"
        "## Polecenia w sesji Codex CLI\n"
        "| polecenie | co robi |\n"
        "|---|---|\n"
        "| `/init` | tworzy szkielet pliku AGENTS.md (instrukcje projektu — tydzień 5) |\n"
        "| `/diff` | pokazuje zmiany w plikach (Git) |\n"
        "| `/status` | ustawienia sesji, model, tryb zgód, zużycie tokenów |\n"
        "| `/compact` | streszcza rozmowę, by zwolnić kontekst |\n"
        "| `/new` | nowa rozmowa bez wychodzenia |\n"
        "| `/review` | prośba o przegląd zmian w katalogu (ryzyka, brakujące testy) |\n"
        "| `/model` | zmiana modelu |\n"
        "## Claude Code i Codex — ta sama praca, inne przyciski\n"
        "| czynność | Claude Code | Codex |\n"
        "|---|---|---|\n"
        "| instrukcje projektu | CLAUDE.md (czyta też AGENTS.md, gdy nie ma CLAUDE.md) | AGENTS.md |\n"
        "| zmiana trybu zgód | Shift + Tab, `/permissions` (reguły) | `/permissions` |\n"
        "| limity i zużycie | `/usage`, `/context` | `/status` |\n"
        "| podsumowanie rozmowy | `/compact` | `/compact` |\n"
        "| przerwanie | Esc | Esc |\n"
        "Nazwy modeli zmieniają się często — kurs ich nie wpisuje; sprawdzisz je w `/model`."),
    przyklad=("PS C:\\Users\\Anna> powershell -ExecutionPolicy ByPass -c \"irm https://chatgpt.com/codex/install.ps1 | iex\"\n"
              "(nowe okno)\nPS C:\\Users\\Anna> cd Documents\\Mentor\\vibe-coding\\PRACA\n"
              "PS C:\\...\\PRACA> codex --sandbox workspace-write --ask-for-approval on-request\n"
              "> Sign in with ChatGPT  (przeglądarka)\n"
              "> Opisz w 2 zdaniach pliki w tym katalogu. Niczego nie zmieniaj."),
    demonstracja={"tytul": "Codex w trybie „pytaj o zgodę” — pierwsza sesja tylko do odczytu", "kroki": [
        "PowerShell → komenda instalacyjna z chatgpt.com/codex/install.ps1 (z dokumentacji). Nowe okno → `codex --version`.",
        "Przejdź do PRACA (`cd` ze ścieżką z Mój projekt) i uruchom `codex --sandbox workspace-write --ask-for-approval on-request`.",
        "Zaloguj się „Sign in with ChatGPT”. Sprawdź `/status`: katalog roboczy to PRACA, tryb zgód on-request.",
        "Prośba tylko do odczytu: „Wypisz pliki i powiedz, co robi rabaty.py. Niczego nie zmieniaj.” Odczyt w katalogu nie wymaga zgody.",
        "Poproś o coś poza katalogiem, np. „pokaż pliki na Pulpicie” — Codex zapyta o zgodę. Odmów. Tak wygląda granica piaskownicy.",
        "Wyjdź (Ctrl + C dwa razy albo /quit). Zapisz `codex --version` w instalacja.txt, jeśli to Twoje narzędzie."],
        "wynik": "Działający Codex w PRACA z piaskownicą workspace-write; widziałeś prośbę o zgodę przy wyjściu poza katalog."},
    jak_uruchomic=["PowerShell → instalacja → nowe okno → w PRACA: `codex --sandbox workspace-write --ask-for-approval on-request`.", "Albo: aplikacja ChatGPT desktop → Codex → wybór folderu PRACA → tryb „Ask for approval”."],
    cwiczenia=[
        C("prowadzone",
          "Dopasuj tryb piaskownicy do sytuacji: (1) chcesz, żeby agent tylko przeczytał kod i wyjaśnił go, (2) zwykła praca nad zadaniem w PRACA, (3) ktoś radzi „ustaw pełny dostęp, będzie szybciej”. "
          "Opcje: read-only, workspace-write, danger-full-access, żaden z nich. Czas: 15 minut.",
          "(1) read-only; (2) workspace-write; (3) żaden z nich — danger-full-access tylko w izolowanych maszynach, nie na Twoim komputerze.",
          ["Samo czytanie — najwęższy tryb.", "Zmiany plików tylko w projekcie — tryb z „workspace” w nazwie.", "Pełny dostęp = cały komputer i internet bez pytania."],
          "(1) read-only, (2) workspace-write, (3) odmawiasz — pełny dostęp nie na komputerze z Twoimi danymi.",
          [wy("s1", "(1) Tylko wyjaśnij kod", ["read-only", "workspace-write", "danger-full-access", "żaden z nich"], "read-only"),
           wy("s2", "(2) Zwykła praca", ["read-only", "workspace-write", "danger-full-access", "żaden z nich"], "workspace-write"),
           wy("s3", "(3) „Pełny dostęp, będzie szybciej”", ["read-only", "workspace-write", "danger-full-access", "żaden z nich"], "żaden z nich",
              bledy=[bl("danger-full-access", "na komputerze z Twoimi dokumentami i hasłami pełny dostęp bez pytania to zbyt duże ryzyko")])]),
        C("samodzielne",
          "Przetłumacz polecenia między narzędziami: (1) w Codex chcesz zobaczyć zużycie tokenów — polecenie? (2) w Codex chcesz szkielet pliku instrukcji projektu — polecenie? "
          "(3) jak nazywa się plik instrukcji, który czytają OBA narzędzia (Claude Code — gdy nie ma CLAUDE.md)? Czas: 15 minut.",
          "(1) /status; (2) /init; (3) AGENTS.md.",
          ["Tabela poleceń Codex w lekcji.", "Szkielet instrukcji tworzy polecenie „inicjalizacji”.", "Claude Code czyta ten plik, gdy brak CLAUDE.md."],
          "/status (zużycie i ustawienia), /init (szkielet AGENTS.md), wspólny plik: AGENTS.md.",
          [tx("p1", "(1) Zużycie tokenów w Codex", ["/status"]), tx("p2", "(2) Szkielet instrukcji w Codex", ["/init"]), tx("p3", "(3) Wspólny plik instrukcji", ["AGENTS.md"])]),
    ],
    typowe_bledy=[
        B("„running scripts is disabled on this system” przy instalacji.", "Zasady wykonywania skryptów PowerShell.", "Czy użyłeś pełnej komendy z -ExecutionPolicy ByPass?", "Skopiuj komendę z dokumentacji w całości: powershell -ExecutionPolicy ByPass -c \"irm … | iex\"."),
        B("`npm` is not recognized.", "Brak Node.js (wariant instalacji przez npm).", "`node --version`.", "Użyj instalatora PowerShell albo zainstaluj Node.js LTS z nodejs.org."),
        B("Codex po zalogowaniu nie daje dostępu w CLI.", "Plan Free/Go — CLI wymaga Plus lub wyższego.", "Ustawienia konta ChatGPT → plan.", "Plus albo aplikacja desktop (ograniczony dostęp) albo ścieżka bez konta."),
    ],
    pulapki=["„Approve for me” jest wygodne, ale to model ocenia zgody za Ciebie. W kursie zaczynasz od „Ask for approval” i zmieniasz świadomie.",
             "Klucz API wklejony do logowania to płatność za tokeny — trzymaj go z dala od plików projektu (tydzień 11)."],
    zadania=["Zainstaluj Codex (jeśli to Twoje narzędzie) i zapisz `codex --version`.", "Pierwsza sesja tylko do odczytu w trybie on-request.", "Przetestuj granicę: prośba o plik spoza PRACA → odmów zgody."],
    pytania=[["Co oznacza workspace-write?", "Agent czyta i zmienia pliki w katalogu projektu; wyjście poza niego i internet wymagają zgody."],
             ["Którego trybu nie używasz na swoim komputerze?", "Full access / danger-full-access."],
             ["Jak sprawdzisz zużycie tokenów w Codex?", "/status."]],
    podsumowanie="Instalujesz Codex CLI albo aplikację, logujesz się ChatGPT, pracujesz w piaskownicy workspace-write z trybem „pytaj o zgodę” i znasz odpowiedniki poleceń z Claude Code.",
    test=[T("Codex CLI w PowerShell instalujesz:", ["pip install codex", "powershell -ExecutionPolicy ByPass -c \"irm https://chatgpt.com/codex/install.ps1 | iex\"", "winget install codex-free", "Ze strony z torrentami"], 1, "Oficjalny instalator."),
          T("Tryb piaskownicy do zwykłej pracy w projekcie:", ["read-only", "workspace-write", "danger-full-access", "brak"], 1, "Zmiany tylko w projekcie."),
          T("Plik instrukcji projektu dla Codex:", ["README.txt", "AGENTS.md", "codex.ini", "CLAUDE.md wyłącznie"], 1, "/init tworzy szkielet."),
          T("Polecenie Codex pokazujące zmiany w plikach:", ["/diff", "/show", "/git", "/changes"], 0, "Staged, unstaged i nowe pliki.")],
    w_praktyce=["Ustaw tryb jawnie przy starcie — nie licz na domyślny.", "Jedno narzędzie na zadanie; porównuj je na tych samych specyfikacjach."],
    zrodla=[Z_CX_README, Z_CX_WIN, Z_CX_PERM, Z_CX_SAND, Z_CX_SLASH],
)


# =========================================================================== TYDZIEŃ 5
SESJA = L(
    id="sesja_agenta", nazwa="Sesja z agentem: prośba, zgody, tryby, przerwanie i cofnięcie", tydzien=5,
    slowa=["sesja", "zgoda", "tryb planu", "acceptEdits", "auto", "Shift+Tab", "Esc", "checkpoint", "/rewind"],
    cel="Po tej lekcji prowadzisz sesję z agentem od prośby do zatwierdzonej zmiany: czytasz prośby o zgodę, wybierasz tryb (ręczny, akceptuj edycje, plan), przerywasz Esc i cofasz zmiany /rewind.",
    po_co="Każda zgoda to decyzja o Twoich plikach. Kto rozumie tryby i cofanie, pracuje szybko i bez strachu.",
    wymagania=["Zainstalowany Claude Code lub Codex (albo ścieżka bez konta — lekcja przez demonstrację).", "Lekcja „Instalacja…”."],
    wyjasnienie=(
        "## Co dzieje się po wysłaniu prośby\n"
        "Agent: (1) czyta pliki, żeby zrozumieć projekt, (2) planuje, (3) proponuje działania — edycję pliku, komendę w terminalu, pobranie strony, (4) po każdej akcji sprawdza wynik i decyduje, co dalej. "
        "Ty widzisz każdą proponowaną akcję i — zależnie od trybu — zatwierdzasz ją.\n"
        "## Prośba o zgodę w Claude Code\n"
        "W trybie ręcznym (domyślnym) odczyt plików w katalogu roboczym nie wymaga zgody; komendy (z wyjątkiem wbudowanej listy komend tylko do odczytu) i edycje plików — wymagają. "
        "Okno zgody pokazuje, co agent chce zrobić, i opcje: Tak / Tak i nie pytaj ponownie / Nie. Przy Tak lub Nie klawisz Tab otwiera pole na krótką uwagę dla agenta („nie, najpierw uruchom testy”).\n"
        "„Nie pytaj ponownie” dla komendy zapisuje regułę na stałe w `.claude/settings.local.json` — dla edycji plików działa tylko do końca sesji.\n"
        "## Tryby uprawnień Claude Code (Shift + Tab przełącza)\n"
        "| tryb | co robi | kiedy w kursie |\n"
        "|---|---|---|\n"
        "| default (ręczny) | pyta o edycje i komendy | początek, zadania z nowym typem zmian |\n"
        "| acceptEdits | edycje plików bez pytania, komendy dalej z pytaniem | gdy plan jest zatwierdzony, a zmiany przeglądasz w Git |\n"
        "| plan | tylko czyta i proponuje plan; edycje zablokowane do Twojej akceptacji; Ctrl + G otwiera plan do edycji | każde zadanie większe niż jedna funkcja |\n"
        "| auto | klasyfikator ocenia akcje zamiast Ciebie, blokuje m.in. pobierz-i-uruchom (curl … \\| bash), wysyłanie danych, force push | dopiero gdy pewnie czytasz zmiany; dokumentacja: „nie gwarantuje bezpieczeństwa” |\n"
        "| bypassPermissions | bez żadnych pytań | nigdy na komputerze z Twoimi danymi (tylko izolowane maszyny) |\n"
        "Uwaga: od niedawnych wersji Claude Code może startować w trybie auto — sprawdź tryb na dole ekranu przy starcie i przełącz Shift + Tab na ręczny lub planu, jeśli chcesz kontrolować każdą zmianę. Tryb planu od razu: `claude --permission-mode plan`.\n"
        "## Codex — odpowiedniki\n"
        "„Ask for approval” ≈ ręczny w obrębie projektu; „Approve for me” ≈ auto; „Full access” ≈ bypass. Przełączasz `/permissions`. Plan: poproś „najpierw plan, nie zmieniaj plików, dopóki nie zatwierdzę”.\n"
        "## Przerwanie i cofnięcie\n"
        "- Esc przerywa agenta w połowie (oba narzędzia). Kontekst zostaje — możesz skorygować kierunek.\n"
        "- Claude Code tworzy punkt kontrolny (checkpoint) przed każdą Twoją prośbą. `/rewind` albo dwa razy Esc przy pustym polu otwiera menu: przywróć kod i rozmowę / tylko rozmowę / tylko kod / podsumuj od tego miejsca.\n"
        "- Ograniczenia z dokumentacji: zmiany zrobione komendami w terminalu nie zawsze są śledzone; checkpointy to NIE zamiennik systemu kontroli wersji — od tygodnia 6 każdą dobrą wersję zapisujesz w Git.\n"
        "## Dobra pierwsza prośba w sesji\n"
        "„Przeczytaj specyfikacja.md i walidacja.py. Zaproponuj plan zmian w punktach, nie zmieniaj plików. Gotowe, gdy: przechodzą testy Mentora.”"),
    przyklad=("Okno zgody (tryb ręczny), agent chce uruchomić testy — wygląd przybliżony, dokładne słowa zależą od wersji:\n\n"
              "  Bash command: python -m pytest -q\n"
              "  Do you want to proceed?\n  ❯ 1. Yes\n    2. Yes, and don't ask again for python -m pytest commands in this project\n    3. No, and tell Claude what to do differently (esc)\n\n"
              "Wybór 2 jest rozsądny dla testów (bezpieczne, często powtarzane). Dla `del`, `rmdir`, `git push --force` — zawsze tylko 1 albo 3."),
    demonstracja={"tytul": "Zadanie w trybie planu, potem cofnięcie złej zmiany", "kroki": [
        "Claude Code w PRACA, Shift + Tab do „plan mode”. Prośba: „Dodaj do rabaty.py funkcję rabat_lojalnosciowy(liczba_pobytow): 3% od 3. pobytu. Najpierw plan.”",
        "Agent czyta pliki i pokazuje plan: nowa funkcja, test w osobnym pliku, bez zmian w istniejących funkcjach. Ctrl + G — dopisujesz w planie „maks. 15% łącznie z innymi rabatami — NIE zmieniaj funkcji rabat()”. Zatwierdzasz.",
        "Agent proponuje edycję rabaty.py — widzisz różnicę (linie dodane). Akceptujesz. Proponuje `python -m pytest -q` — akceptujesz; testy przechodzą.",
        "Druga prośba: „Uprość cały plik”. Agent przepisuje 4 funkcje. Testy Mentora robią się czerwone.",
        "Esc Esc → menu checkpointów → wybierasz punkt sprzed „Uprość cały plik” → „Restore code and conversation”. Plik wraca do stanu z zielonym testem.",
        "Wniosek do dziennika: „ogólne prośby (uprość wszystko) = ryzyko; jedna funkcja na prośbę”."],
        "wynik": "Nowa funkcja dodana przez plan → zgodę → test, a zła ogólna zmiana cofnięta checkpointem w kilka sekund."},
    jak_uruchomic=["Claude Code: Shift + Tab (tryby), Esc (przerwij), Esc Esc lub /rewind (cofnij).", "Codex: /permissions (tryby), Esc (przerwij), /diff (zobacz zmiany)."],
    cwiczenia=[
        C("prowadzone",
          "Agent w trybie ręcznym proponuje kolejno: (1) odczyt rabaty.py, (2) edycję rabaty.py, (3) komendę `python -m pytest -q`, (4) komendę `rmdir /s /q dane`. "
          "Przy których Claude Code w ogóle zapyta o zgodę (w trybie ręcznym)? Przy której wybierzesz „Nie” i dlaczego (numer)? Czas: 15 minut.",
          "Zapyta przy 2, 3 i 4 (odczyt w katalogu roboczym nie wymaga zgody). „Nie” przy 4 — usuwa cały folder dane bez kosza.",
          ["Tabela z dokumentacji: odczyt w katalogu roboczym — bez zgody.", "Edycje i komendy (poza listą tylko-do-odczytu) — z pytaniem.", "rmdir /s /q usuwa folder z zawartością bez pytania."],
          "Pytanie o zgodę: 2, 3, 4. Odmowa: 4 — nieodwracalne usunięcie danych, nie było w zadaniu.",
          [li("ile", "Przy ilu z 4 akcji padnie pytanie o zgodę?", 3, bledy=[bl(4, "odczyt plików w katalogu roboczym nie wymaga zgody")]),
           li("nie", "Numer akcji, przy której odmówisz", 4)]),
        C("samodzielne",
          "Dobierz tryb Claude Code: (1) nowe, większe zadanie (3 pliki) — chcesz najpierw zobaczyć plan; (2) plan zatwierdzony, zmiany i tak przejrzysz w Git, nie chcesz klikać każdej edycji; "
          "(3) pierwszy dzień z agentem, chcesz widzieć każdą akcję. Opcje: default, acceptEdits, plan, bypassPermissions. Czy checkpoint cofnie zmianę zrobioną komendą `del raport.txt` na pewno (tak/nie)? Czas: 15 minut.",
          "(1) plan; (2) acceptEdits; (3) default. Nie — zmiany z komend terminala nie zawsze są śledzone przez checkpointy.",
          ["Plan = najpierw czyta i proponuje.", "acceptEdits = edycje bez pytania, komendy z pytaniem.", "Dokumentacja checkpointów: komendy Bash nie zawsze śledzone."],
          "(1) plan, (2) acceptEdits, (3) default; checkpoint nie gwarantuje cofnięcia usunięcia plików komendą — dlatego Git.",
          [wy("t1", "(1) Większe zadanie, najpierw plan", ["default", "acceptEdits", "plan", "bypassPermissions"], "plan"),
           wy("t2", "(2) Plan zatwierdzony, przegląd w Git", ["default", "acceptEdits", "plan", "bypassPermissions"], "acceptEdits"),
           wy("t3", "(3) Pierwszy dzień", ["default", "acceptEdits", "plan", "bypassPermissions"], "default"),
           wy("rew", "Checkpoint na pewno cofnie del raport.txt?", TN, "nie")]),
    ],
    typowe_bledy=[
        B("Agent zmienił 6 plików, a prosiłeś o jedną funkcję.", "Ogólna prośba i tryb bez planu.", "Czy prośba mówiła, których plików nie ruszać?", "Tryb planu, lista plików w prośbie, potem /rewind do stanu sprzed zmiany."),
        B("Kliknąłeś „don't ask again” dla komendy, której nie chcesz.", "Reguła zapisana na stałe w .claude/settings.local.json.", "`/permissions` — lista reguł i plików, z których pochodzą.", "Usuń regułę w /permissions."),
        B("Agent „myśli” od kilku minut i zużywa limit.", "Zbyt szerokie zadanie, pętla prób.", "Co pokazuje ostatnia akcja?", "Esc, potem krótsza, konkretniejsza prośba albo tryb planu."),
    ],
    pulapki=["Tryb auto i „Approve for me” nie zastępują Twojego przeglądu — dokumentacja Claude Code mówi wprost, że auto nie gwarantuje bezpieczeństwa.",
             "Checkpointy przechowywane są lokalnie przez ok. 30 dni i obejmują 100 ostatnich punktów — to bezpieczeństwo na teraz, nie archiwum projektu."],
    zadania=["Wykonaj jedno zadanie w trybie planu z edycją planu Ctrl + G.", "Przećwicz /rewind na celowo złej zmianie.", "Zapisz w sesja_agenta.md każdą decyzję o zgodzie (zadanie tygodnia)."],
    pytania=[["Jak przerwiesz agenta w połowie?", "Esc."], ["Co robi tryb planu?", "Agent tylko czyta i proponuje plan; zmiany plików czekają na moją akceptację."],
             ["Dlaczego checkpoint nie zastępuje Gita?", "Nie śledzi wszystkich zmian z komend, jest lokalny i krótkotrwały; Git zapisuje trwałą historię wersji."]],
    podsumowanie="Rozumiesz cykl sesji, czytasz prośby o zgodę, dobierasz tryb, przerywasz Esc i cofasz /rewind — z świadomością ograniczeń checkpointów.",
    test=[T("Skrót przełączający tryby w Claude Code:", ["Ctrl + T", "Shift + Tab", "Alt + M", "F5"], 1, "default → acceptEdits → plan…"),
          T("W trybie ręcznym bez pytania agent może:", ["Usuwać pliki", "Czytać pliki w katalogu roboczym", "Instalować paczki", "Robić git push"], 1, "Odczyt nie wymaga zgody."),
          T("„Yes, and don't ask again” dla komendy zapisuje regułę:", ["Na 5 minut", "Na stałe w .claude/settings.local.json", "Nigdzie", "W CLAUDE.md"], 1, "Usuniesz ją w /permissions."),
          T("Który tryb jest tylko dla izolowanych maszyn?", ["plan", "default", "bypassPermissions", "acceptEdits"], 2, "Bez żadnych pytań.")],
    w_praktyce=["Każde zadanie > 1 funkcja zaczynaj w trybie planu.", "„Nie pytaj ponownie” tylko dla testów i komend tylko do odczytu."],
    zrodla=[Z_CC_MODES, Z_CC_PERM, Z_CC_CHECK, Z_CX_PERM],
)

INSTRUKCJE = L(
    id="instrukcje_projektu", nazwa="Instrukcje projektu: AGENTS.md i CLAUDE.md — pamięć agenta", tydzien=5,
    slowa=["AGENTS.md", "CLAUDE.md", "/init", "@import", "pamięć", "instrukcje", "konwencje"],
    cel="Po tej lekcji piszesz krótki AGENTS.md (cel projektu, polecenia, zasady, czego nie ruszać) i CLAUDE.md, który go importuje — tak, żeby Claude Code i Codex pracowały według tych samych reguł.",
    po_co="Każda nowa sesja to agent bez pamięci. Plik instrukcji jest jak karta przekazania zmiany: bez niego powtarzasz te same ustalenia w każdej prośbie.",
    wymagania=["Lekcja „Sesja z agentem”.", "Repozytorium/katalog PRACA z plikami z tygodni 1–3."],
    wyjasnienie=(
        "## Dwa pliki, jeden standard\n"
        "| | AGENTS.md | CLAUDE.md |\n"
        "|---|---|---|\n"
        "| kto czyta | Codex (i wiele innych agentów); Claude Code — gdy nie ma CLAUDE.md | Claude Code |\n"
        "| gdzie | katalog projektu (Codex: od korzenia repozytorium w dół do bieżącego folderu; globalnie ~/.codex/AGENTS.md) | ./CLAUDE.md lub ./.claude/CLAUDE.md; osobiste: ~/.claude/CLAUDE.md; prywatne lokalne: CLAUDE.local.md |\n"
        "| szkielet | `/init` w Codex | `/init` w Claude Code |\n"
        "| limit | domyślnie 32 KiB łącznie (project_doc_max_bytes) | zalecane poniżej 200 linii na plik |\n"
        "Rekomendacja dokumentacji Claude Code dla projektów używających obu narzędzi: wspólne instrukcje w AGENTS.md, a CLAUDE.md zawiera linię `@AGENTS.md` (import pliku) i ewentualnie dodatki tylko dla Claude. Importy działają do 4 poziomów zagnieżdżenia.\n"
        "## Co wpisać (i czego nie)\n"
        "- Cel projektu w 2 zdaniach i dla kogo.\n"
        "- Polecenia: jak uruchomić program i testy (`python -m pytest -q`).\n"
        "- Konwencje: język komentarzy (polski), nazwy plików małymi literami, funkcje z return, input() tylko w bloku __main__.\n"
        "- Zasady pracy: „najpierw plan”, „jedna zmiana naraz”, „po zmianie uruchom testy”, „nie zmieniaj testów, żeby przeszły”.\n"
        "- Czego nie ruszać: folder WERYFIKATORY, dane klienta, plik .env.\n"
        "- NIE wpisuj: haseł, kluczy, danych osobowych; długich instrukcji ogólnych („pisz dobry kod”) — to zużywa kontekst i nic nie daje.\n"
        "## Instrukcje to prośba, nie blokada\n"
        "Dokumentacja Claude Code: treść CLAUDE.md to kontekst dla modelu, nie wymuszenie. Model zwykle się stosuje, ale może zapomnieć. Twarde zakazy ustawia się w uprawnieniach (reguły deny w `.claude/settings.json`, `/permissions` — tydzień 12). "
        "Dlatego „nie czytaj .env” piszesz w instrukcjach ORAZ blokujesz regułą.\n"
        "## Utrzymanie pliku\n"
        "- Gdy agent dwa razy popełni ten sam błąd — dopisz jedną linię zasady.\n"
        "- Co miesiąc usuń nieaktualne linie. Krótszy plik = lepiej przestrzegany i tańszy.\n"
        "- W Claude Code `/memory` pokazuje, które pliki instrukcji są wczytane.\n"
        "- AGENTS.md trafia do repozytorium (Git) — jest częścią projektu jak README."),
    przyklad=("# AGENTS.md — Pod Lipą (kurs vibe coding)\n\n"
              "## Projekt\nNarzędzia dla agroturystyki „Pod Lipą”: kalkulator ceny, lista gości, walidacja formularza. Dane fikcyjne.\n\n"
              "## Polecenia\n- testy: `python -m pytest -q`\n- uruchomienie: `python <plik>.py`\n\n"
              "## Zasady\n- Najpierw plan w punktach, zmiany dopiero po akceptacji.\n- Jedna funkcja na zmianę; po zmianie uruchom testy.\n"
              "- Nie zmieniaj testów, żeby przeszły — zgłoś, jeśli test wydaje się błędny.\n- Komentarze po polsku; input() tylko w bloku __main__.\n\n"
              "## Nie ruszaj\n- WERYFIKATORY/, dane/, .env\n\n"
              "---\n# CLAUDE.md\n@AGENTS.md\n\n## Tylko dla Claude Code\n- Przy zadaniach > 1 pliku zacznij w trybie planu."),
    demonstracja={"tytul": "Od /init do krótkiego, wspólnego pliku instrukcji", "kroki": [
        "Claude Code w PRACA: `/init`. Agent czyta projekt i proponuje CLAUDE.md — długi, z opisem każdego pliku.",
        "Zamiast przyjmować w całości: każesz przenieść wspólne zasady do AGENTS.md (5 sekcji z przykładu), a w CLAUDE.md zostawić `@AGENTS.md` i jedną linię tylko dla Claude.",
        "Skracasz: usuwasz opisy plików, które agent i tak przeczyta, oraz ogólniki. Zostaje ok. 25 linii.",
        "Nowa sesja (`/clear`), `/memory` — widzisz wczytane CLAUDE.md i zaimportowany AGENTS.md.",
        "Test: prośba „dodaj funkcję do lista_gosci.py”. Agent sam zaczyna od planu i po zmianie uruchamia pytest — bo tak mówią instrukcje.",
        "W Codex: nowa sesja w PRACA, `/status` — AGENTS.md jest wczytany; ta sama prośba, to samo zachowanie."],
        "wynik": "Jeden krótki AGENTS.md sterujący oboma agentami i CLAUDE.md z importem; zachowanie agentów zgodne z zasadami bez powtarzania ich w każdej prośbie."},
    jak_uruchomic=["Claude Code: `/init`, `/memory`.", "Codex: `/init`, `/status`."],
    cwiczenia=[
        C("prowadzone",
          "Które linie NIE powinny trafić do AGENTS.md? (1) `testy: python -m pytest -q` (2) `klucz API pogody: abc123…` (3) `Nie zmieniaj testów, żeby przeszły` (4) `Pisz zawsze najlepszy możliwy kod` (5) `Nie ruszaj folderu WERYFIKATORY`. "
          "Podaj numery jako ciąg cyfr rosnąco (np. 13). Jaką jedną linię wpiszesz w CLAUDE.md, żeby Claude Code wczytał AGENTS.md? Czas: 15 minut.",
          "Nie powinny: 2 (tajemnica) i 4 (ogólnik) → „24”. W CLAUDE.md: `@AGENTS.md`.",
          ["Szukaj tajemnic.", "Szukaj linii, które nic konkretnego nie mówią.", "Import pliku w CLAUDE.md zaczyna się od @."],
          "2 — klucz to tajemnica (plik trafia do repozytorium), 4 — ogólnik bez treści. Import: @AGENTS.md.",
          [tx("zle", "Numery linii do usunięcia", ["24"], bledy=[bl("2", "linia 4 to ogólnik — zużywa kontekst, niczego nie zmienia"), bl("4", "linia 2 to tajemnica — klucze nigdy nie trafiają do plików w repozytorium")]),
           tx("import", "Linia importu w CLAUDE.md", ["@AGENTS.md"])]),
        C("samodzielne",
          "Napisałeś w CLAUDE.md „nigdy nie czytaj pliku .env”, a agent i tak raz go otworzył. (1) Czy instrukcja w CLAUDE.md to wymuszenie (tak/nie)? (2) Gdzie ustawisz twardą blokadę — w CLAUDE.md, w regułach uprawnień, czy w README? "
          "(3) Ile linii dokumentacja zaleca nie przekraczać w CLAUDE.md? Czas: 15 minut.",
          "(1) nie — to kontekst; (2) reguły uprawnień (deny w .claude/settings.json, /permissions); (3) 200.",
          ["Dokumentacja: instrukcje to kontekst, nie enforcement.", "Blokady egzekwuje Claude Code, nie model.", "Zalecenie długości: poniżej …"],
          "Instrukcje nie wymuszają; twarde zakazy — reguły deny w uprawnieniach; CLAUDE.md poniżej 200 linii.",
          [wy("wym", "(1) CLAUDE.md wymusza?", TN, "nie"), wy("gdzie", "(2) Twarda blokada", ["CLAUDE.md", "reguły uprawnień", "README"], "reguły uprawnień"), li("linie", "(3) Zalecany limit linii", 200)]),
    ],
    typowe_bledy=[
        B("Agent ignoruje część zasad.", "Plik za długi albo zasady sprzeczne/ogólne.", "`/memory` — czy plik jest wczytany? Ile ma linii?", "Skróć do najważniejszych, konkretnych zasad; usuń sprzeczności."),
        B("Codex nie stosuje się do zasad z CLAUDE.md.", "Codex czyta AGENTS.md, nie CLAUDE.md.", "Czy zasady są w AGENTS.md?", "Wspólne zasady w AGENTS.md, w CLAUDE.md tylko `@AGENTS.md`."),
        B("W repozytorium widać prywatne ścieżki i notatki.", "Osobiste rzeczy w CLAUDE.md projektu.", "Treść CLAUDE.md w Git.", "Osobiste ustawienia w CLAUDE.local.md (dodaj do .gitignore) albo ~/.claude/CLAUDE.md."),
    ],
    pulapki=["„/init” generuje dobry początek, ale zwykle za długi — redaguj, nie akceptuj w całości.",
             "Instrukcje z pobranego cudzego repozytorium też są czytane przez agenta — przeczytaj AGENTS.md/CLAUDE.md, zanim uruchomisz agenta w obcym projekcie (tydzień 12)."],
    zadania=["Napisz AGENTS.md i CLAUDE.md dla PRACA (zadanie tygodnia).", "Sprawdź /memory lub /status, że pliki są wczytane.", "Dopisz jedną zasadę po błędzie agenta."],
    pytania=[["Po co CLAUDE.md zawiera @AGENTS.md?", "Żeby Claude Code wczytał wspólne instrukcje, z których korzysta też Codex."],
             ["Czy CLAUDE.md blokuje akcje agenta?", "Nie — to kontekst; blokady ustawia się w regułach uprawnień."],
             ["Czego nie wpisujesz do plików instrukcji?", "Haseł, kluczy, danych osobowych i ogólników."]],
    podsumowanie="Piszesz krótki AGENTS.md z poleceniami, zasadami i zakazami, importujesz go w CLAUDE.md, wiesz, że instrukcje to kontekst, a blokady to uprawnienia.",
    test=[T("Codex czyta instrukcje projektu z pliku:", ["CLAUDE.md", "AGENTS.md", "README.md", ".env"], 1, "Od korzenia repozytorium w dół."),
          T("Import pliku w CLAUDE.md:", ["#include AGENTS.md", "@AGENTS.md", "import AGENTS", "<AGENTS.md>"], 1, "Do 4 poziomów."),
          T("Polecenie Claude Code pokazujące wczytane pliki instrukcji:", ["/memory", "/files", "/rules", "/agents"], 0, "Widać CLAUDE.md i importy."),
          T("Agent dwa razy popełnił ten sam błąd. Co robisz?", ["Zmieniam narzędzie", "Dopisuję jedną konkretną zasadę do AGENTS.md", "Wydłużam plik o ogólniki", "Nic"], 1, "Plik instrukcji rośnie z doświadczenia.")],
    w_praktyce=["AGENTS.md w każdym projekcie od pierwszego dnia.", "Przegląd instrukcji raz w miesiącu."],
    zrodla=[Z_CC_MEM, Z_CX_AGENTS, Z_CC_PERM, Z_CC_BEST],
)

MALE_KROKI = L(
    id="male_kroki", nazwa="Małe kroki: plan → jedna zmiana → test → zapis", tydzien=5,
    slowa=["mały krok", "plan", "iteracja", "zakres", "test", "zapis wersji", "dekompozycja"],
    cel="Po tej lekcji dzielisz zadanie na kroki po jednej zmianie, prowadzisz agenta krok po kroku z testem po każdym i wiesz, kiedy zatrzymać sesję.",
    po_co="Dokumentacja Claude Code (Best practices) zaleca: najpierw eksploracja i plan, potem kod, i zawsze sposób weryfikacji. Duże prośby dają duże, niesprawdzalne zmiany.",
    wymagania=["Lekcje „Sesja z agentem” i „Instrukcje projektu”."],
    wyjasnienie=(
        "## Dlaczego małe kroki\n"
        "Zmiana w 1 funkcji = 10 linii do przejrzenia i jeden test. Zmiana w 6 plikach = 300 linii i nie wiesz, która linia zepsuła rabat. "
        "Małe kroki obniżają też koszt: agent czyta mniej, a błąd cofasz jednym ruchem.\n"
        "## Rytm jednego kroku\n"
        "| faza | Twoja prośba / działanie |\n"
        "|---|---|\n"
        "| 1. Eksploracja | „Przeczytaj X i Y, powiedz, jak działa Z. Nie zmieniaj plików.” |\n"
        "| 2. Plan | „Zaproponuj plan w punktach dla [cel]. Każdy punkt = jedna zmiana z testem.” |\n"
        "| 3. Krok | „Zrób tylko punkt 1. Potem uruchom testy i pokaż wynik.” |\n"
        "| 4. Sprawdzenie | czytasz zmianę (diff), testy Mentora, własny przykład |\n"
        "| 5. Zapis | od tygodnia 6: commit z opisem; do tego czasu — checkpoint i kopia |\n"
        "Potem punkt 2 — i tak dalej. Po 3–5 krokach albo przy zmianie tematu: `/clear` (Claude Code) albo `/new` (Codex) i nowa sesja.\n"
        "## Jak podzielić zadanie\n"
        "- Po funkcjach: każda funkcja ze specyfikacji to krok.\n"
        "- Po warstwach: najpierw logika (funkcje + testy), potem wejście/wyjście (pliki, formularz), na końcu wygląd.\n"
        "- Po przypadkach: najpierw przypadek podstawowy, potem brzegowe.\n"
        "## Sygnały, że krok jest za duży\n"
        "- Agent proponuje zmiany w więcej niż 2 plikach naraz.\n"
        "- Nie umiesz w jednym zdaniu powiedzieć, co ten krok zmienia.\n"
        "- Agent pracuje dłużej niż kilka minut bez pokazania wyniku.\n"
        "## Weryfikacja wpisana w prośbę\n"
        "Każda prośba kończy się kryterium: „Gotowe, gdy test_konwerter przechodzi” albo „Gotowe, gdy dla \"1 234,56 zł\" funkcja zwraca 1234.56”. "
        "Agent, który ma sposób sprawdzenia, sam uruchamia test i poprawia się, zanim odda pracę."),
    przyklad=("Plan dla konwerter.py (zadanie tygodnia), zatwierdzony w trybie planu:\n\n"
              "1. parsuj_kwote(tekst) — „1 234,56 zł” → 1234.56; test 5 przykładów.\n"
              "2. Złe dane w parsuj_kwote („abc”, „”) → ValueError; test.\n"
              "3. zl_na_eur(kwota, kurs) — zaokrąglenie do centów; ValueError dla kursu ≤ 0 i kwoty < 0; test.\n"
              "4. formatuj_zl(kwota) → „1 234,56 zł”; test.\n"
              "Po każdym punkcie: testy Mentora + przegląd zmian."),
    demonstracja={"tytul": "Jedno zadanie, dwie strategie", "kroki": [
        "Strategia A: „Napisz konwerter.py ze wszystkimi funkcjami ze specyfikacji”. Agent tworzy 120 linii, testy: 3 z 9 czerwone, w trzech różnych funkcjach. Naprawa wymaga 4 kolejnych rund.",
        "Strategia B (tryb planu): plan 4 punktów jak w przykładzie. „Zrób punkt 1 i uruchom testy” — 15 linii, zielone dla parsuj_kwote (pozostałe czerwone, bo funkcji jeszcze nie ma — to oczekiwane).",
        "Punkt 2: agent dodaje ValueError. Przeglądasz 6 linii zmian. Punkt 3 i 4 analogicznie.",
        "Porównanie w dzienniku: A — 5 rund i 120 linii czytania na raz; B — 4 rundy po 10–20 linii, każdy błąd złapany w miejscu powstania."],
        "wynik": "Strategia małych kroków daje tyle samo kodu, ale każdą zmianę rozumiesz i weryfikujesz od razu."},
    jak_uruchomic=["Claude Code: Shift + Tab → plan; po każdym kroku `python -m pytest -q` lub „✔ Sprawdź wynik”.", "Codex: „najpierw plan, nie zmieniaj plików” → „zrób punkt 1” → /diff."],
    cwiczenia=[
        C("prowadzone",
          "Podziel na kroki prośbę: „Dodaj do lista_gosci.py usuwanie gościa, wyszukiwanie po imieniu i zapis listy do pliku CSV, i popraw raport, żeby był posortowany”. "
          "Ile niezależnych zmian (kroków) zawiera ta prośba? Który krok zrobisz OSTATNI według zasady „najpierw logika, potem wejście/wyjście”? Opcje: usuwanie, wyszukiwanie, zapis do CSV, sortowanie raportu. Czas: 15 minut.",
          "4 kroki; ostatni — zapis do CSV (wejście/wyjście).",
          ["Policz czasowniki: dodaj usuwanie, wyszukiwanie, zapis, popraw raport.", "Logika = działania na liście w pamięci.", "Zapis do pliku to wejście/wyjście."],
          "Cztery kroki: usuwanie, wyszukiwanie, sortowanie raportu (logika), na końcu zapis do CSV (wyjście).",
          [li("ile", "Liczba kroków", 4), wy("ostatni", "Krok ostatni", ["usuwanie", "wyszukiwanie", "zapis do CSV", "sortowanie raportu"], "zapis do CSV")]),
        C("samodzielne",
          "Które sygnały oznaczają „krok za duży”? (1) agent chce zmienić 5 plików, (2) zmiana dotyczy jednej funkcji i jednego testu, (3) nie umiesz w jednym zdaniu powiedzieć, co zmienia krok, "
          "(4) agent pracuje 12 minut bez wyniku. Podaj liczbę sygnałów „za duży” i jedną komendę Claude Code, którą zaczniesz nową sesję po zakończeniu tematu. Czas: 15 minut.",
          "3 sygnały (1, 3, 4); nowa sesja: /clear.",
          ["Jedna funkcja + test to wzorcowy mały krok.", "Pozostałe trzy to sygnały ostrzegawcze.", "Komenda czyszcząca rozmowę w Claude Code."],
          "Za duży: 1, 3, 4 → 3 sygnały. Nowa sesja: /clear (w Codex /new).",
          [li("ile", "Liczba sygnałów „za duży”", 3), tx("kom", "Komenda nowej sesji w Claude Code", ["/clear"])]),
    ],
    typowe_bledy=[
        B("Agent „przy okazji” refaktoryzuje sąsiednie funkcje.", "Brak granicy kroku w prośbie.", "Czy prośba mówi „tylko punkt 1”?", "„Zrób tylko punkt 1, nie zmieniaj innych funkcji”; zasada w AGENTS.md."),
        B("Testy czerwone po kroku, nie wiesz dlaczego.", "Krok obejmował kilka zmian.", "Diff kroku.", "Cofnij (/rewind lub git restore) i podziel krok."),
    ],
    pulapki=["Mały krok nie znaczy „bez planu”. Plan całości robisz raz na początku — i aktualizujesz.",
             "Czerwone testy funkcji, których jeszcze nie ma, są w porządku w trakcie planu — ważne, by zielone były te z bieżącego kroku."],
    zadania=["Zbuduj konwerter.py w 4 krokach z planem (zadanie tygodnia).", "Zapisz w dzienniku porównanie z prośbą „wszystko naraz”.", "Dopisz do AGENTS.md zasadę „jeden punkt planu na raz”."],
    pytania=[["Jakie są fazy jednego kroku?", "Eksploracja, plan, jedna zmiana, sprawdzenie, zapis."],
             ["W jakiej kolejności dzielisz pracę po warstwach?", "Logika z testami, potem wejście/wyjście, na końcu wygląd."],
             ["Kiedy zaczynasz nową sesję?", "Po 3–5 krokach albo przy zmianie tematu."]],
    podsumowanie="Dzielisz zadania na kroki z testem po każdym, rozpoznajesz krok za duży i zamykasz sesję we właściwym momencie.",
    test=[T("Najlepsza pierwsza prośba do nowego zadania:", ["Napisz wszystko", "Przeczytaj pliki i zaproponuj plan, nie zmieniaj plików", "Uprość projekt", "Zrób to szybko"], 1, "Eksploracja i plan."),
          T("Sygnał, że krok jest za duży:", ["Zmiana 1 funkcji", "Agent chce zmienić 5 plików naraz", "Jeden test", "Krótki diff"], 1, "Podziel."),
          T("Każda prośba powinna kończyć się:", ["Podziękowaniem", "Kryterium „Gotowe, gdy…”", "Emoji", "Nazwą modelu"], 1, "Agent może się sam sprawdzić."),
          T("Nowa rozmowa w Codex:", ["/new", "/clear", "/restart", "/init"], 0, "W Claude Code — /clear.")],
    w_praktyce=["Plan w punktach to część dokumentacji zadania — zapisz go w specyfikacji.", "Jedna sesja = jeden temat."],
    zrodla=[Z_CC_BEST, Z_CC_MODES, Z_CC_COSTS],
)
