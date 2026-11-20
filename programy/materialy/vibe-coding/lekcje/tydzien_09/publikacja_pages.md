# Publikacja: GitHub Pages — strona pod własnym adresem
Tydzień 9 · lekcja 30 z 48 · ≈ 50 min

**Po tej lekcji potrafisz:** publikujesz stronę z repozytorium na GitHub Pages (adres nazwa.github.io/repo), znasz limity i ograniczenia usługi oraz sprawdzasz, co jest publiczne.

**Po co mi to?** Działający adres to najmocniejszy argument w portfolio i dla klienta. GitHub Pages jest darmowy, ale ma zasady, które trzeba znać przed publikacją.

## Czego potrzebujesz
- Lekcje „GitHub” i „Strona internetowa…”.
- Repozytorium publiczne (w planie GitHub Free Pages działa tylko dla publicznych).

## 1 · Wyjaśnienie od podstaw
### Co to jest GitHub Pages
Usługa GitHuba, która publikuje statyczne pliki (HTML, CSS, JS, obrazy) z repozytorium pod adresem `https://NAZWA.github.io/REPO/`. Statyczne = bez Pythona na serwerze: kalkulator w JS zadziała, aplikacja Flask — nie (tydzień 10 pokaże inny hosting).
### Limity i zasady (dokumentacja GitHub)
| limit | wartość |
|---|---|
| repozytorium źródłowe | zalecane do 1 GB |
| opublikowana strona | najwyżej 1 GB |
| transfer | miękki limit 100 GB miesięcznie |
| czas publikacji | do 10 minut na wdrożenie |
| plan GitHub Free | Pages tylko z repozytoriów publicznych |
GitHub Pages nie jest przeznaczony do sklepów internetowych ani usług SaaS, a dokumentacja zabrania używania go do przesyłania wrażliwych danych (haseł, numerów kart). Formularz rezerwacji zbierający dane gości — nie na Pages.
### Osobne repozytorium na stronę
Twoje główne repo pod-lipa jest prywatne (kod, notatki). Na stronę utwórz OSOBNE publiczne repozytorium, np. `pod-lipa-strona`, z samymi plikami strony: index.html, styl.css, kalkulator.js, obrazy. Zanim je opublikujesz — przegląd: żadnych notatek, kluczy, danych osobowych, plików .md z prywatnymi uwagami.
### Włączenie
- Repozytorium → Settings → Pages → Build and deployment → Source: „Deploy from a branch”, Branch: `main`, folder `/ (root)` → Save.
- Po 1–10 minutach u góry pojawi się adres „Your site is live at https://NAZWA.github.io/pod-lipa-strona/”. Zakładka Actions pokazuje postęp wdrożenia.
- Każdy kolejny push na main publikuje nową wersję.
### Sprawdzenie po publikacji
- Otwórz adres na komputerze i telefonie (inna sieć — np. dane komórkowe).
- Ścieżki plików są wrażliwe na wielkość liter na serwerze: `Lipa.JPG` ≠ `lipa.jpg` (w Windows działało, na Pages — nie).
- F12 → Console i Network: brak 404.
### Własna domena
Możesz podpiąć domenę klienta (np. podlipa.pl) w Settings → Pages → Custom domain + rekord DNS u rejestratora. Klient płaci za domenę u rejestratora; Ty ustawiasz. HTTPS: zaznacz „Enforce HTTPS”.

## 2 · Demonstracja — krok po kroku
**Od plików do adresu w internecie**

```
Struktura publicznego repozytorium strony:

pod-lipa-strona/
├── index.html
├── styl.css
├── kalkulator.js
├── img/
│   └── lipa.jpg
└── README.md   (1 akapit: co to za strona, dane fikcyjne)

Adres po publikacji: https://anna-dev.github.io/pod-lipa-strona/
```

1. github.com → New repository: pod-lipa-strona, Public, bez README.
2. Nowy folder poza PRACA (np. Dokumenty\pod-lipa-strona), skopiuj tylko index.html, styl.css, kalkulator.js, img/. `git init`, commit, `git remote add origin …`, `git push -u origin main`.
3. Settings → Pages → Deploy from a branch → main / (root) → Save. Zakładka Actions: zadanie „pages build and deployment” — po chwili zielone.
4. Adres działa. Na telefonie zdjęcie się nie wyświetla: w HTML `img/Lipa.jpg`, plik `img/lipa.jpg`. Poprawka nazwy, commit, push — po minucie działa.
5. Zapisujesz adres w PRACA w adres_strony.txt (zadanie tygodnia).

✔ **Oczekiwany wynik:** Publiczna strona pod adresem github.io, sprawdzona na telefonie, bez prywatnych plików w repozytorium.

## 3 · Jak to uruchomić
1. Repo strony → Settings → Pages → Deploy from a branch → main → / (root).
2. Postęp: zakładka Actions.

## W praktyce
- Strona klienta: osobne repo, przegląd treści przed publikacją.
- Po każdym push — szybki test na telefonie.

## 4 · Ćwiczenie prowadzone
Odpowiedz według dokumentacji: (1) maksymalny rozmiar opublikowanej strony (GB), (2) miękki limit transferu miesięcznie (GB), (3) ile minut najwyżej trwa wdrożenie, (4) czy na GitHub Free można publikować Pages z repozytorium prywatnego (tak/nie). Czas: 15 minut.

📄 `cwiczenia/tydzien_09/publikacja_pages_1.md` · rozwiązanie: `rozwiazania/tydzien_09/publikacja_pages_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Które pliki mogą trafić do PUBLICZNEGO repozytorium strony? (1) index.html (2) notatki/o_mnie.md (3) styl.css (4) .env (5) img/lipa.jpg — zdjęcie od klientki z jej zgodą (6) dziennik.md. Podaj numery rosnąco jako ciąg cyfr. Czy formularz rezerwacji zbierający numery telefonów gości możesz oprzeć na samym GitHub Pages (tak/nie)? Czas: 15 minut.

📄 `cwiczenia/tydzien_09/publikacja_pages_2.md` · rozwiązanie: `rozwiazania/tydzien_09/publikacja_pages_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **404 „There isn't a GitHub Pages site here”.**
  - Przyczyna: Pages nie włączone, wdrożenie trwa albo brak index.html w korzeniu.
  - Jak sprawdzić: Settings → Pages i zakładka Actions.
  - Poprawka: Włącz źródło main / (root), poczekaj do 10 min, index.html w korzeniu repozytorium.
- ✘ **Obrazek działa lokalnie, na Pages nie.**
  - Przyczyna: Wielkość liter w nazwie pliku.
  - Jak sprawdzić: F12 → Network: 404 dla obrazka.
  - Poprawka: Ujednolić nazwy na małe litery w plikach i HTML.
- ✘ **Opcja Pages niedostępna dla repozytorium.**
  - Przyczyna: Repozytorium prywatne na GitHub Free.
  - Jak sprawdzić: Settings → General → visibility.
  - Poprawka: Osobne publiczne repo tylko z plikami strony.

## Pułapki
- Upublicznienie istniejącego repozytorium upublicznia CAŁĄ historię — dlatego osobne repo strony.
- Pages nie jest miejscem na dane osobowe gości ani płatności.

## Dodatkowe zadania
1. Opublikuj stronę na Pages i zapisz adres (zadanie tygodnia).
2. Sprawdź stronę na telefonie w innej sieci.
3. Napisz 1-akapitowy README repozytorium strony.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego osobne repozytorium na stronę?**
  - Bo Pages na Free wymaga publicznego repo, a główny projekt z notatkami i historią ma zostać prywatny.
- **Czego nie publikujesz na Pages?**
  - Formularzy zbierających wrażliwe dane, sklepów, haseł, kart, danych osobowych.
- **Gdzie widać postęp wdrożenia?**
  - Zakładka Actions repozytorium.

## Co potrafię teraz bez patrzenia na przykład?
Publikujesz statyczną stronę na GitHub Pages z osobnego publicznego repozytorium, znasz limity i zakazy usługi i sprawdzasz efekt na telefonie.

## Źródła (data dostępu w nawiasie)
Narzędzia, ceny i przepisy zmieniają się — przed użyciem w pracy otwórz źródło.
- GitHub Docs — What is GitHub Pages? / Quickstart (dostęp 20.11.2026) — <https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages>
- GitHub Docs — GitHub Pages limits (1 GB, 100 GB/mies., 10 min) (dostęp 19.11.2026) — <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits>
- GitHub Docs — Configuring a publishing source for your GitHub Pages site (dostęp 20.11.2026) — <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>

## Test (w Mentorze: Lekcje → Sprawdź się)
- GitHub Pages publikuje:
  - A) Aplikacje Flask
  - B) Pliki statyczne: HTML, CSS, JS
  - C) Bazy danych
  - D) Pliki .exe
- Adres strony Pages ma postać:
  - A) NAZWA.github.io/REPO
  - B) github.com/pages
  - C) REPO.pl
  - D) localhost
- Limit opublikowanej strony:
  - A) 100 MB
  - B) 1 GB
  - C) 10 GB
  - D) bez limitu
- Plik działa lokalnie, na Pages 404. Pierwsze podejrzenie:
  - A) Wielkość liter w nazwie
  - B) Zły kolor
  - C) Za długi tytuł
  - D) Brak README

Odpowiedzi: B, A, B, A
