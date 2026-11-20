# -*- coding: utf-8 -*-
"""Sobotnia powtórka każdego tygodnia (quiz, karta przeglądu, dziennik, zadanie dodatkowe z lekcji) — zadanie v{t}z9."""

from wspolne import Z

KARTA_TYGODNIA = {5: ("karta_tryby", "Wybór trybu uprawnień"), 6: ("karta_diff", "Przegląd diffu: „drobne usprawnienia” agenta"),
                  7: ("karta_koszt", "Koszt i kontekst sesji"), 10: ("karta_sql", "Zapytania SQL od agenta"), 11: ("karta_git", "Ratunek w Gicie"),
                  12: ("karta_injection", "Podejrzane README w obcym repozytorium"), 13: ("karta_ci", "Czerwone CI, zielone lokalnie"),
                  14: ("karta_wycena", "Wycena zlecenia")}


def powtorka(t, lekcje):
    karta = KARTA_TYGODNIA.get(t)
    krok_karty = (f"Warsztat → Karty przeglądu → „{karta[1]}”: rozstrzygnij sam, potem wpisz odpowiedzi (Mentor sprawdzi każde pole)." if karta else
                  "Lekcje tygodnia → sekcja „Sprawdzenie”: odpowiedz na głos na wszystkie pytania, potem rozwiń odpowiedzi i porównaj.")
    return Z(f"v{t}z9", f"Powtórka tygodnia {t}: quiz, karta, dziennik", "Ostatni dzień tygodnia (piątek albo sobota): quiz tygodnia, trening decyzji, porządek w dzienniku i jedno zadanie dodatkowe z lekcji — utrwalenie bez nowego materiału.",
             ["Plan nauki → tydzień → „Quiz tygodnia” (5 pytań). Błędne odpowiedzi wskazują lekcję — przeczytaj jej podsumowanie i typowe błędy.",
              krok_karty,
              "Wybierz jedno zadanie z sekcji „Dodatkowe zadania” w lekcjach tygodnia (" + ", ".join(lekcje) + ") i wykonaj je.",
              "Dziennik: odpowiedz na 2 pytania dziennika z Panelu, dopisz „czego nie rozumiem” i plan na poniedziałek." + (" Commit i push." if t >= 6 else ""),
              "„✔ Sprawdź wynik” przy pliku dziennik.md otworzy listę kryteriów do samooceny."],
             "Quiz zrobiony (błędy przeczytane w lekcjach), karta lub pytania sprawdzające, jedno zadanie dodatkowe, wpis w dzienniku z planem na kolejny tydzień.",
             ["Quiz poniżej 60% → nie przechodź dalej bez przeczytania wskazanych lekcji; to nie kara, tylko sygnał."],
             ["dziennik.md"], 75, xp=10,
             cwiczenie={"plik": "dziennik.md", "sprawdzenie": {"rodzaj": "plik_istnieje"}},
             rubryka=["Quiz tygodnia wykonany, błędne pytania przeczytane w lekcjach", "Karta przeglądu albo pytania sprawdzające", "Jedno zadanie dodatkowe z lekcji", "Wpis w dzienniku z planem na kolejny tydzień"])
