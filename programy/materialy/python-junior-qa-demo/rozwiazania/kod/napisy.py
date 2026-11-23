tekst = input("Wpisz zdanie: ").strip()

print(tekst.upper())
print(tekst[::-1])
print("znaków:", len(tekst))
samogloski = 0
for znak in tekst.lower():
    if znak in "aąeęioóuy":
        samogloski += 1
print("samogłosek:", samogloski)
slowa = tekst.split()
print("słów:", len(slowa))
najdluzsze = ""
for s in slowa:
    if len(s) > len(najdluzsze):
        najdluzsze = s
print("najdłuższe:", najdluzsze)
