"""
vstup = [1, 1, 1, 1, 3, 1, 4, 1, 4, 1, 1, 2, 5, 2, 5, 1, 1, 1, 4, 3, 1, 4, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 4, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 5, 1, 1, 2, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 1, 1, 1, 2, 1, 1, 5, 2, 1, 1, 1, 1, 4, 5, 1, 1, 2, 4, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 3, 1, 1, 4, 2, 1, 5, 1, 2, 1, 1, 1, 1, 1, 3, 3, 1, 5, 1, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 4, 1, 4, 3, 1, 1, 1, 4, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 5, 1, 1, 3, 5, 1, 1, 5, 2, 1, 1, 1, 1, 1, 4, 4, 1, 1, 2, 1, 1, 1, 4, 1, 1, 1, 1, 5, 3, 1, 1, 1, 5, 1, 1, 1, 4, 1, 4, 1, 1, 1, 5, 1, 1, 3, 2, 2, 1, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 4, 1, 1, 1, 1, 1, 4, 1, 1, 2, 4, 2, 1, 2, 3, 1, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 3, 1, 1, 4, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 1, 3, 1, 1, 5, 1, 1, 3, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 1, 3, 5, 1, 1, 4, 4, 1, 3, 4, 1, 2, 4, 1, 1, 3, 1]
i = 0
c = 1
vloz = []
vysledek = 0
while c < 257:
    while i < len(vstup):
        cislo = vstup.pop(i)
        if cislo > 0:
            cislo = cislo - 1
            vstup.insert(i, cislo)
        else:
            cislo = 6
            vstup.insert(i, cislo)
            vloz.append(8)
        i += 1
    if vloz:
        for osmicky in vloz:
            vstup.append(osmicky)

    print(c,len(vstup))
    vloz = []
    i = 0
    c += 1
"""
####################################
nuly = 0
jednicky = 197
dvojky = 28
trojky = 26
ctyrky = 30
petky = 19
sestky = 0
sedmicky = 0
osmicky = 0

cyklus = 256

while cyklus:
    mezi_nuly = nuly
    nuly = jednicky
    jednicky = dvojky
    dvojky = trojky
    trojky = ctyrky
    ctyrky = petky
    petky = sestky
    sestky = sedmicky + mezi_nuly
    sedmicky = osmicky
    osmicky = mezi_nuly
    vysledek = nuly + jednicky + dvojky + trojky + ctyrky + petky + sestky + sedmicky + osmicky
    cyklus -= 1
print(vysledek)















