# Weryfikator tygodnia 14 — wymagania.md.


def test_wymagania():
    t = tekst("wymagania.md")
    linie = t.splitlines()
    idx = [i for i, l in enumerate(linie) if re.search(r"\bjako\b.+\bchc[eę]\b.+\baby\b", norm(l))]
    assert len(idx) >= 5, f"wymagania.md: {len(idx)} historyjek w formacie „Jako … chcę …, aby …” (potrzeba ≥ 5)"
    granice = idx[1:] + [len(linie)]
    for a, b in zip(idx, granice):
        kryteria = [l for l in linie[a + 1:b] if l.strip().startswith(("-", "*")) and len(l.strip("-* ").strip()) >= 5 and not l.strip().startswith("##")]
        stop = next((j for j, l in enumerate(linie[a + 1:b]) if l.strip().startswith("## ")), None)
        if stop is not None:
            kryteria = [l for l in linie[a + 1:a + 1 + stop] if l.strip().startswith(("-", "*")) and len(l.strip("-* ").strip()) >= 5]
        assert len(kryteria) >= 2, f"wymagania.md: historyjka „{linie[a].strip()[:60]}…” ma mniej niż 2 kryteria akceptacji (linie „- …” pod nią)"
    s = sekcje_md(t)
    pz = next((v for k, v in s.items() if k.startswith("poza zakresem")), None)
    assert pz is not None and sum(1 for l in pz if l.startswith(("-", "*"))) >= 2, "wymagania.md: sekcja „## Poza zakresem” z ≥ 2 pozycjami"
    pyt = next((v for k, v in s.items() if k.startswith("pytania")), None)
    assert pyt is not None and sum(1 for l in pyt if l.startswith(("-", "*", "1", "2", "3", "4", "5"))) >= 3, "wymagania.md: sekcja „## Pytania do klienta” z ≥ 3 pytaniami"
