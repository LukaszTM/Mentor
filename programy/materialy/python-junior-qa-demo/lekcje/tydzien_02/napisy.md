# Napisy i ich metody: upper, lower, strip, split, replace, len, wycinki
Tydzień 2 · lekcja 11 z 16 · ≈ 45 min

**Po tej lekcji potrafisz:** przetwarzasz tekst metodami napisów (upper, lower, strip, split, join, replace, count, startswith), liczysz znaki i słowa, odwracasz napis wycinkiem i wiesz, że metody zwracają NOWY napis.

**Po co mi to?** Dane od użytkowników to tekst z literówkami i spacjami; wyszukiwarka sklepu, walidacja e-maila i porównania w testach opierają się na tych metodach.

## Czego potrzebujesz
- Lekcje „Listy” i „Pętle”.

## 1 · Wyjaśnienie od podstaw
### Napis to ciąg znaków
Napis indeksujesz jak listę: `"Zeszyt"[0]` → "Z", `[-1]` → "t", `[0:3]` → "Zes". `len("Zeszyt")` → 6. `[::-1]` odwraca napis.
### Napisy są niezmienne
`nazwa.upper()` NIE zmienia `nazwa` — zwraca nowy napis. Zapisz wynik: `nazwa = nazwa.upper()` albo od razu wypisz.
### Najważniejsze metody
| metoda | przykład | wynik |
|---|---|---|
| `upper()` / `lower()` | `"Klej".upper()` | "KLEJ" |
| `strip()` | `"  klej ".strip()` | "klej" |
| `split()` | `"zeszyt długopis klej".split()` | ['zeszyt', 'długopis', 'klej'] |
| `split(";")` | `"a;b".split(";")` | ['a', 'b'] |
| `", ".join(lista)` | `", ".join(["a", "b"])` | "a, b" |
| `replace(stare, nowe)` | `"4,50".replace(",", ".")` | "4.50" |
| `count(x)` | `"banan".count("a")` | 2 |
| `startswith(x)` | `"PL123".startswith("PL")` | True |
| `find(x)` | `"a@b.pl".find("@")` | 1 (brak → -1) |
### Wyszukiwanie bez względu na wielkość liter
`fraza.lower() in nazwa.lower()` — „DŁUGOPIS” znajdzie „Długopis niebieski”. Brak `.lower()` w wyszukiwarce to częsty błąd, który zgłasza tester (sklep testowy w tygodniu 8 ma taki celowo).
### Liczenie samogłosek
Pętla po napisie: `for znak in tekst.lower(): if znak in "aąeęioóuy": ile += 1`.

## 2 · Demonstracja — krok po kroku
**Analiza zdania: wielkie litery, od tyłu, słowa, samogłoski**

```
zdanie = "  Ala ma kota i psa  "
czyste = zdanie.strip()
print(czyste.upper())
print(czyste[::-1])
print(len(czyste), "znaków")
slowa = czyste.split()
print(len(slowa), "słów:", ", ".join(slowa))
samogloski = 0
for znak in czyste.lower():
    if znak in "aąeęioóuy":
        samogloski += 1
print("Samogłoski:", samogloski)
najdluzsze = max(slowa, key=len)
print("Najdłuższe:", najdluzsze)
print("4,50 zł".replace(",", "."), "Długopis".lower().startswith("dług"))

```

1. `strip()` — usuwa spacje z brzegów; `czyste` ma 17 znaków (spacje w środku się liczą).
2. `upper()` zwraca nowy napis wielkimi literami — `czyste` się nie zmienia.
3. `[::-1]` — wycinek z krokiem -1: napis od tyłu.
4. `split()` bez argumentu dzieli po spacjach → lista 5 słów; `", ".join(slowa)` skleja je z przecinkiem.
5. Pętla po znakach: `lower()` zamienia „A” na „a”, `in "aąeęioóuy"` sprawdza samogłoskę → 7 (a, a, a, o, a, i, a).
6. `max(slowa, key=len)` — najdłuższe słowo według długości; przy remisie pierwsze (kota, 4 litery).
7. `replace` zamienia przecinek na kropkę (przyda się przy float), `lower().startswith` — wyszukiwanie po początku.

✔ **Oczekiwany wynik:** Siedem linii, m.in. „5 słów: Ala, ma, kota, i, psa” i „Samogłoski: 7”.

## 3 · Jak to uruchomić
1. Zapisz jako tekst.py → ▶ Uruchom.
2. Zmień zdanie na własne i przewidź liczbę samogłosek przed uruchomieniem.

## W praktyce
- Testując wyszukiwarkę: wielkie/małe litery, spacje, polskie znaki, pusta fraza.
- Porównania w testach: najpierw strip(), potem porównuj.

## 4 · Ćwiczenie prowadzone
Dla napisu `t = "Zeszyt A5 w kratkę"` podaj: (1) `len(t)`, (2) `t.split()` — ile elementów, (3) `t.lower().count("z")`, (4) `t.replace("A5", "A4")`. Czas: 15 minut.

📄 `cwiczenia/tydzien_02/napisy_1.md` · rozwiązanie: `rozwiazania/tydzien_02/napisy_1.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 5 · Ćwiczenie samodzielne
Wyszukiwarka sklepu: `def pasuje(fraza, nazwa): return fraza in nazwa`. (1) Co zwróci `pasuje("długopis", "Długopis niebieski")`? (2) Popraw treść return (wpisz nowe wyrażenie), żeby nie zależała od wielkości liter i spacji na brzegach frazy. (3) Co wtedy zwróci `pasuje("  DŁUGOPIS ", "Długopis niebieski")`? Czas: 15 minut.

📄 `cwiczenia/tydzien_02/napisy_2.md` · rozwiązanie: `rozwiazania/tydzien_02/napisy_2.md`
✔ W Mentorze pod ćwiczeniem są pola „Twoje odpowiedzi” — Mentor sprawdzi każde pole.

## 6 · Typowe błędy i naprawa
- ✘ **Napis się „nie zmienia” po .upper()**
  - Przyczyna: Wynik metody nie został zapisany.
  - Jak sprawdzić: Czy jest `x = x.upper()`?
  - Poprawka: Przypisz wynik albo użyj go od razu.
- ✘ **AttributeError: 'list' object has no attribute 'lower'**
  - Przyczyna: Metoda napisu wywołana na liście (np. po split()).
  - Jak sprawdzić: `print(type(x))`.
  - Poprawka: Wywołaj na każdym elemencie w pętli albo przed split().
- ✘ **TypeError: 'str' object does not support item assignment**
  - Przyczyna: Próba zmiany znaku: `t[0] = "z"`.
  - Jak sprawdzić: Napisy są niezmienne.
  - Poprawka: Zbuduj nowy napis: `t = "z" + t[1:]`.

## Pułapki
- Polskie litery: „Ą”.lower() działa poprawnie, ale porównania z ogonkami i bez to różne napisy („zolty” ≠ „żółty”).
- split(",") nie usuwa spacji: "a, b".split(",") → ['a', ' b'].

## Dodatkowe zadania
1. Program: wpisz zdanie → wielkie litery, od tyłu, liczba znaków, samogłosek, słów, najdłuższe słowo.
2. Wyszukiwarka produktów bez względu na wielkość liter.
3. Zamiana „4,50” na liczbę 4.5.

## Sprawdzenie — odpowiedz na głos, potem rozwiń
- **Dlaczego t.upper() nie zmienia t?**
  - Napisy są niezmienne — metoda zwraca nowy napis.
- **Co robi "-".join(["a", "b"])?**
  - Zwraca "a-b".
- **Jak odwrócić napis?**
  - t[::-1].

## Co potrafię teraz bez patrzenia na przykład?
Przetwarzasz tekst metodami napisów, liczysz znaki/słowa/samogłoski, odwracasz napis i budujesz wyszukiwanie niezależne od wielkości liter.

## Źródła (data dostępu w nawiasie)
Wersje narzędzi i dane rynkowe zmieniają się — przed użyciem w pracy otwórz źródło.
- Python — Built-in Types (str, list, dict: metody) (dostęp 23.11.2026) — <https://docs.python.org/3/library/stdtypes.html>
- Python — Poradnik: Nieformalne wprowadzenie (liczby, napisy, listy) (dostęp 23.11.2026) — <https://docs.python.org/pl/3/tutorial/introduction.html>

## Test (w Mentorze: Lekcje → Sprawdź się)
- "Klej".lower() zwraca:
  - A) "KLEJ"
  - B) "klej"
  - C) None
  - D) zmienia oryginał
- "a b  c".split() daje:
  - A) ['a', 'b', '', 'c']
  - B) ['a', 'b', 'c']
  - C) ['a b  c']
  - D) błąd
- "abc"[::-1] to:
  - A) "abc"
  - B) "cba"
  - C) "c"
  - D) błąd
- "PL" in "pl-123" daje:
  - A) True
  - B) False
  - C) błąd
  - D) None

Odpowiedzi: B, B, B, B
