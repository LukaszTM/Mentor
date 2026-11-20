# Weryfikator tygodnia 6 — repozytorium Git i GitHub.

ZLE_OPISY = {"zmiany", "fix", "update", "asdf", "commit", "poprawki", "wip", "test"}


def test_git_repo():
    repo()
    kod, log = git("log", "--format=%s")
    assert kod == 0 and log, "Repozytorium nie ma jeszcze commitów — git add <pliki> i git commit -m \"opis\""
    opisy = [l.strip() for l in log.splitlines() if l.strip()]
    assert len(opisy) >= 3, f"W historii jest {len(opisy)} commitów — potrzeba co najmniej 3"
    dobre = [o for o in opisy if len(o) >= 10 and o.lower() not in ZLE_OPISY]
    assert len(dobre) >= 3, "Co najmniej 3 commity muszą mieć opis ≥ 10 znaków mówiący, co zmieniono (nie „fix”, „zmiany”)"


def test_git_ignore():
    repo()
    t = tekst(".gitignore")
    linie = {l.strip().rstrip("/") for l in t.splitlines() if l.strip() and not l.strip().startswith("#")}
    for w in (".env", ".venv", "__pycache__"):
        assert w in linie, f".gitignore: brak wpisu {w}"
    kod, pliki = git("ls-files")
    sledzone = pliki.splitlines()
    assert ".env" not in sledzone, "Plik .env jest w repozytorium — git rm --cached .env, commit, a klucze z niego unieważnij"
    assert not any(p.startswith(".venv/") for p in sledzone), "Folder .venv jest w repozytorium — git rm -r --cached .venv i commit"


def test_github():
    repo()
    t = tekst("adres_repo.txt")
    m = re.search(r"https://github\.com/([\w.-]+)/([\w.-]+?)(?:\.git)?/?(?:\s|$)", t)
    assert m, "adres_repo.txt: brak adresu w formacie https://github.com/NAZWA/REPO"
    kod, url = git("remote", "get-url", "origin")
    assert kod == 0, "Repozytorium nie ma zdalnego origin — git remote add origin https://github.com/NAZWA/pod-lipa.git"
    assert "github.com" in url, f"origin wskazuje {url} — oczekiwano adresu github.com"
    nazwa = lambda s: s.lower().rstrip("/").removesuffix(".git").split("github.com")[-1].strip(":/")
    assert nazwa(url) == nazwa(m.group(0).strip()), f"Adres w adres_repo.txt ({m.group(0).strip()}) nie pasuje do origin ({url})"
    kod, _ = git("rev-parse", "--verify", "--quiet", "refs/remotes/origin/main")
    assert kod == 0, "Brak gałęzi origin/main — wyślij historię: git push -u origin main"
    assert (WS / "README.md").exists(), "Brak README.md w repozytorium"
