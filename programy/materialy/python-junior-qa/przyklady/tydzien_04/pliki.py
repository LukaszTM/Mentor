from pathlib import Path

produkty = ["Zeszyt A5", "Długopis niebieski", "Gumka"]
with open("produkty.txt", "w", encoding="utf-8") as f:
    for p in produkty:
        f.write(p + "\n")
with open("produkty.txt", "a", encoding="utf-8") as f:
    f.write("Klej w sztyfcie\n")
with open("produkty.txt", encoding="utf-8") as f:
    for nr, linia in enumerate(f, 1):
        print(nr, linia.strip())
print("Linii:", len(Path("produkty.txt").read_text(encoding="utf-8").splitlines()))
try:
    open("brak.txt", encoding="utf-8")
except FileNotFoundError:
    print("Nie ma pliku brak.txt")
Path("produkty.txt").unlink()
