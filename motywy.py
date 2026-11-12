# -*- coding: utf-8 -*-
"""
Motywy kolorystyczne Mentora.

Każdy motyw to słownik kolorów (klucze opisane w zbuduj()) + czcionki.
Grupy:
  - "pycharm"  — wzorowane na PyCharm: schematy wbudowane (Darcula, IntelliJ Light, Dark/Light z nowego UI)
                  i najczęściej pobierane z JetBrains Marketplace (Material, One Dark, Dracula, Gruvbox,
                  Monokai, Nord, Solarized).
  - "vscode"   — wzorowane na Visual Studio Code (Dark Modern, Dark+, Light Modern).
  - "terminal" — wzorowane na klasycznym terminalu Windows: zielony fosfor i bursztyn, czcionka monospace.
Dodanie własnego motywu = jeden wpis w MOTYWY.
"""


def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def mieszaj(a, b, t):
    """Kolor a przesunięty w stronę b o t (0..1). Zwraca '#rrggbb'."""
    ra, ga, ba = _hex(a)
    rb, gb, bb = _hex(b)
    return "#%02x%02x%02x" % (round(ra + (rb - ra) * t), round(ga + (gb - ga) * t), round(ba + (bb - ba) * t))


def zbuduj(id_, nazwa, grupa, *, tlo, karta, ramka, bok, bok_akt, bok_tekst, bok_tytul, tekst, szary, jasny,
           akcent, pomar, czerw, ziel, nieb, btn_tekst="#FFFFFF", ciemny=True,
           font=None, mono=None, zolty=None, ziel_tlo=None, czerw_tlo=None, nieb_tlo=None, akcent_c=None):
    """
    tlo       — tło okna              karta     — tło kart
    ramka     — obramowanie kart      bok       — pasek boczny; bok_akt — aktywna pozycja; bok_tekst/bok_tytul — teksty
    tekst     — tekst główny          szary     — tekst drugorzędny      jasny — pola tekstowe, plakietki neutralne
    akcent    — przyciski główne, postęp, wyróżnienia; akcent_c — po najechaniu
    pomar     — ostrzeżenia/piątek    czerw/ziel/nieb — statusy; *_tlo — tła plakietek statusów
    btn_tekst — tekst na przycisku akcentowym
    """
    kier = "#FFFFFF" if ciemny else "#000000"
    return {
        "id": id_, "nazwa": nazwa, "grupa": grupa, "ciemny": ciemny,
        "font": font or "Segoe UI", "mono": mono or "Consolas",
        "tlo": tlo, "karta": karta, "ramka": ramka, "bok": bok, "bok_akt": bok_akt, "bok_tekst": bok_tekst,
        "bok_tytul": bok_tytul, "tekst": tekst, "szary": szary, "jasny": jasny,
        "akcent": akcent, "akcent_c": akcent_c or mieszaj(akcent, kier, 0.15),
        "pomar": pomar, "pomar_c": mieszaj(pomar, kier, 0.15),
        "czerw": czerw, "ziel": ziel, "nieb": nieb, "btn_tekst": btn_tekst,
        "zolty": zolty or mieszaj(karta, pomar, 0.14 if ciemny else 0.16),
        "ziel_tlo": ziel_tlo or mieszaj(karta, ziel, 0.18),
        "czerw_tlo": czerw_tlo or mieszaj(karta, czerw, 0.18),
        "nieb_tlo": nieb_tlo or mieszaj(karta, nieb, 0.18),
    }


MOTYWY = [
    # ------------------------------------------------------------------ Mentor
    zbuduj("mentor", "Mentor (domyślny)", "mentor", ciemny=False,
           tlo="#F4F2EC", karta="#FFFFFF", ramka="#E3DFD5", bok="#1E2A38", bok_akt="#2C3C50", bok_tekst="#D9E0EA",
           bok_tytul="#FFFFFF", tekst="#1F2933", szary="#6B7280", jasny="#F0EDE6", akcent="#2E7D5B", pomar="#D97706",
           czerw="#B91C1C", ziel="#15803D", nieb="#1D4ED8",
           zolty="#FEF3C7", ziel_tlo="#DCFCE7", czerw_tlo="#FEE2E2", nieb_tlo="#DBEAFE", akcent_c="#276A4D"),

    # ----------------------------------------------------------------- PyCharm
    zbuduj("pc-darcula", "Darcula (klasyczny)", "pycharm",
           tlo="#2B2B2B", karta="#313335", ramka="#3C3F41", bok="#3C3F41", bok_akt="#4B6EAF", bok_tekst="#BBBBBB",
           bok_tytul="#FFFFFF", tekst="#A9B7C6", szary="#808080", jasny="#45494A", akcent="#499C54", pomar="#CC7832",
           czerw="#FF6B68", ziel="#6A8759", nieb="#6897BB"),
    zbuduj("pc-dark", "Dark (nowy interfejs)", "pycharm",
           tlo="#1E1F22", karta="#2B2D30", ramka="#393B40", bok="#2B2D30", bok_akt="#2E436E", bok_tekst="#DFE1E5",
           bok_tytul="#FFFFFF", tekst="#DFE1E5", szary="#868A91", jasny="#393B40", akcent="#3574F0", pomar="#CF8E6D",
           czerw="#F75464", ziel="#57965C", nieb="#548AF7"),
    zbuduj("pc-light", "Light (nowy interfejs)", "pycharm", ciemny=False,
           tlo="#F7F8FA", karta="#FFFFFF", ramka="#EBECF0", bok="#F7F8FA", bok_akt="#D4E2FF", bok_tekst="#27282E",
           bok_tytul="#000000", tekst="#000000", szary="#6C707E", jasny="#F0F1F2", akcent="#3574F0", pomar="#C77D00",
           czerw="#E55765", ziel="#369650", nieb="#3574F0"),
    zbuduj("pc-intellij-light", "IntelliJ Light", "pycharm", ciemny=False,
           tlo="#F2F2F2", karta="#FFFFFF", ramka="#D1D1D1", bok="#E8E8E8", bok_akt="#D5D5D5", bok_tekst="#000000",
           bok_tytul="#000000", tekst="#000000", szary="#6E6E6E", jasny="#EDEDED", akcent="#4A86E8", pomar="#B07400",
           czerw="#DB5C5C", ziel="#59A869", nieb="#4A86E8"),
    zbuduj("pc-material", "Material Oceanic", "pycharm",
           tlo="#263238", karta="#2E3C43", ramka="#37474F", bok="#1E272C", bok_akt="#314549", bok_tekst="#B0BEC5",
           bok_tytul="#EEFFFF", tekst="#EEFFFF", szary="#7E97A6", jasny="#37474F", akcent="#80CBC4", btn_tekst="#1B2A2E",
           pomar="#F78C6C", czerw="#FF5370", ziel="#C3E88D", nieb="#82AAFF"),
    zbuduj("pc-onedark", "One Dark", "pycharm",
           tlo="#21252B", karta="#282C34", ramka="#3E4451", bok="#21252B", bok_akt="#2C313A", bok_tekst="#9DA5B4",
           bok_tytul="#ABB2BF", tekst="#ABB2BF", szary="#6B7280", jasny="#3E4451", akcent="#61AFEF", btn_tekst="#1B2027",
           pomar="#D19A66", czerw="#E06C75", ziel="#98C379", nieb="#61AFEF"),
    zbuduj("pc-dracula", "Dracula", "pycharm",
           tlo="#21222C", karta="#282A36", ramka="#44475A", bok="#191A21", bok_akt="#44475A", bok_tekst="#BFC2CF",
           bok_tytul="#F8F8F2", tekst="#F8F8F2", szary="#8A90B0", jasny="#44475A", akcent="#BD93F9", btn_tekst="#1E1F29",
           pomar="#FFB86C", czerw="#FF5555", ziel="#50FA7B", nieb="#8BE9FD"),
    zbuduj("pc-gruvbox", "Gruvbox Dark", "pycharm",
           tlo="#282828", karta="#32302F", ramka="#504945", bok="#1D2021", bok_akt="#3C3836", bok_tekst="#BDAE93",
           bok_tytul="#EBDBB2", tekst="#EBDBB2", szary="#928374", jasny="#3C3836", akcent="#B8BB26", btn_tekst="#1D2021",
           pomar="#FE8019", czerw="#FB4934", ziel="#B8BB26", nieb="#83A598"),
    zbuduj("pc-monokai", "Monokai", "pycharm",
           tlo="#272822", karta="#2E2F28", ramka="#3E3D32", bok="#1E1F1C", bok_akt="#3E3D32", bok_tekst="#C8C8C2",
           bok_tytul="#F8F8F2", tekst="#F8F8F2", szary="#908E7A", jasny="#3E3D32", akcent="#A6E22E", btn_tekst="#1E1F1C",
           pomar="#FD971F", czerw="#F92672", ziel="#A6E22E", nieb="#66D9EF"),
    zbuduj("pc-nord", "Nord", "pycharm",
           tlo="#2E3440", karta="#3B4252", ramka="#434C5E", bok="#242933", bok_akt="#434C5E", bok_tekst="#D8DEE9",
           bok_tytul="#ECEFF4", tekst="#ECEFF4", szary="#8E9AB3", jasny="#434C5E", akcent="#88C0D0", btn_tekst="#2E3440",
           pomar="#D08770", czerw="#BF616A", ziel="#A3BE8C", nieb="#81A1C1"),
    zbuduj("pc-solarized-dark", "Solarized Dark", "pycharm",
           tlo="#002B36", karta="#073642", ramka="#0E4A58", bok="#00212B", bok_akt="#073642", bok_tekst="#93A1A1",
           bok_tytul="#EEE8D5", tekst="#EEE8D5", szary="#7F9A9F", jasny="#0E4A58", akcent="#268BD2",
           pomar="#CB4B16", czerw="#DC322F", ziel="#859900", nieb="#268BD2"),
    zbuduj("pc-solarized-light", "Solarized Light", "pycharm", ciemny=False,
           tlo="#EEE8D5", karta="#FDF6E3", ramka="#D9D2C2", bok="#073642", bok_akt="#586E75", bok_tekst="#93A1A1",
           bok_tytul="#EEE8D5", tekst="#073642", szary="#7C8A8C", jasny="#EEE8D5", akcent="#268BD2",
           pomar="#CB4B16", czerw="#DC322F", ziel="#859900", nieb="#268BD2"),

    # ----------------------------------------------------------------- VS Code
    zbuduj("vs-dark-modern", "Dark Modern", "vscode",
           tlo="#1F1F1F", karta="#252526", ramka="#2B2B2B", bok="#181818", bok_akt="#37373D", bok_tekst="#CCCCCC",
           bok_tytul="#FFFFFF", tekst="#CCCCCC", szary="#8B949E", jasny="#313131", akcent="#0078D4", pomar="#CE9178",
           czerw="#F14C4C", ziel="#4EC9B0", nieb="#569CD6"),
    zbuduj("vs-dark-plus", "Dark+ (klasyczny)", "vscode",
           tlo="#1E1E1E", karta="#252526", ramka="#3C3C3C", bok="#333333", bok_akt="#252526", bok_tekst="#CCCCCC",
           bok_tytul="#FFFFFF", tekst="#D4D4D4", szary="#858585", jasny="#3C3C3C", akcent="#007ACC", pomar="#D7BA7D",
           czerw="#F48771", ziel="#6A9955", nieb="#569CD6"),
    zbuduj("vs-light-modern", "Light Modern", "vscode", ciemny=False,
           tlo="#F8F8F8", karta="#FFFFFF", ramka="#E5E5E5", bok="#ECECEC", bok_akt="#E4E6F1", bok_tekst="#3B3B3B",
           bok_tytul="#000000", tekst="#3B3B3B", szary="#6F6F6F", jasny="#EDEDED", akcent="#005FB8", pomar="#B8651B",
           czerw="#CD3131", ziel="#008000", nieb="#0000FF"),

    # ---------------------------------------------------------------- Terminal
    zbuduj("term-zielony", "Terminal — zielony fosfor", "terminal", font="Consolas", mono="Consolas",
           tlo="#000000", karta="#050A05", ramka="#1A5A1A", bok="#000000", bok_akt="#0C2E0C", bok_tekst="#1FAF1F",
           bok_tytul="#33FF33", tekst="#33FF33", szary="#1FAF1F", jasny="#0A1F0A", akcent="#33FF33", btn_tekst="#000000",
           pomar="#FFB000", czerw="#FF5555", ziel="#33FF33", nieb="#33FF33"),
    zbuduj("term-bursztyn", "Terminal — bursztynowy", "terminal", font="Consolas", mono="Consolas",
           tlo="#000000", karta="#0A0700", ramka="#6A4A00", bok="#000000", bok_akt="#2A1E00", bok_tekst="#B07800",
           bok_tytul="#FFB000", tekst="#FFB000", szary="#B07800", jasny="#1A1200", akcent="#FFB000", btn_tekst="#000000",
           pomar="#FF8800", czerw="#FF5555", ziel="#FFB000", nieb="#FFB000"),
]

GRUPY = [
    ("mentor", "Mentor"),
    ("pycharm", "Wzorowane na PyCharm"),
    ("vscode", "Wzorowane na VS Code"),
    ("terminal", "Wzorowane na terminalu Windows"),
]

MOTYW_DOMYSLNY = "mentor"


def motyw(id_):
    for m in MOTYWY:
        if m["id"] == id_:
            return m
    return motyw(MOTYW_DOMYSLNY)
