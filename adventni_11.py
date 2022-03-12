"""
vstupy =[[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
[2, 7, 4, 5, 8, 5, 4, 7, 1, 1 ],
[5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
[6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
[6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
[4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
[2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
[6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
[4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
[5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]

"""
vstupy = [[1, 2, 2, 4, 3, 4, 6, 3, 8, 4],
[5, 6, 2, 1, 1, 2, 8, 5, 8, 7],
[6, 3, 8, 8, 4, 2, 6, 5, 4, 6],
[1, 5, 5, 6, 2, 4, 7, 7, 5, 6],
[1, 4, 5, 1, 8, 1, 1, 5, 7, 3],
[1, 8, 3, 2, 3, 8, 8, 1, 2, 2],
[2, 7, 4, 8, 5, 4, 5, 6, 4, 7],
[2, 5, 8, 2, 8, 7, 7, 4, 3, 2],
[3, 1, 8, 5, 6, 4, 3, 8, 7, 1],
[2, 2, 2, 4, 8, 7, 6, 6, 2, 7]]



flash = 0
def booom():
    global flash
    for a, radek in enumerate(vstupy):
        for b, cislo in enumerate(radek):
            if cislo > 9:
                vstupy[a].insert(b, 0)
                flash += 1
                del vstupy[a][b + 1]

                try:
                    if a > 0:
                        qw = vstupy[a - 1][b + 1]
                        if qw != 0:
                            vstupy[a - 1].insert(b + 1, qw + 1)
                            del vstupy[a - 1][b + 2]
                except IndexError:
                    True

                try:
                    we = vstupy[a][b + 1]
                    if we != 0:
                        vstupy[a].insert(b + 1, we + 1)
                        del vstupy[a][b + 2]
                except IndexError:
                    True

                try:
                    er = vstupy[a + 1][b + 1]
                    if er != 0:
                        vstupy[a + 1].insert(b + 1, er + 1)
                        del vstupy[a + 1][b + 2]
                except IndexError:
                    True

                try:
                    rt = vstupy[a + 1][b]
                    if rt != 0:
                        vstupy[a + 1].insert(b, rt + 1)
                        del vstupy[a + 1][b + 1]
                except IndexError:
                    True

                try:
                    if b > 0:
                        tz = vstupy[a+1][b-1]
                        if tz != 0:
                            vstupy[a + 1].insert(b - 1, tz + 1)
                            del vstupy[a + 1][b]
                except IndexError:
                    True

                try:
                    if b > 0:
                        zu = vstupy[a][b - 1]
                        if zu != 0:
                            vstupy[a].insert(b - 1, zu + 1)
                            del vstupy[a][b]
                except IndexError:
                    True

                try:
                    if b > 0 and a > 0:
                        ui = vstupy[a - 1][b - 1]
                        if ui != 0:
                            vstupy[a - 1].insert(b - 1, ui + 1)
                            del vstupy[a - 1][b]
                except IndexError:
                    True

                try:
                    if a > 0:
                        io = vstupy[a - 1][b]
                        if io != 0:
                            del vstupy[a - 1][b]
                            vstupy[a - 1].insert(b, io + 1)
                except IndexError:
                    True





def main():
    global flash
    flash = 0
    global k
    k = 315

    while k > 1:
        for r, radek in enumerate(vstupy):
            for c, cislo in enumerate(radek):
                vstupy[r].insert(c, cislo + 1)
                del vstupy[r][c+1]

        while any(11 in sublist for sublist in vstupy) or any(10 in sublist for sublist in vstupy):
            booom()

        print(k, vstupy)
        k -= 1
    print("flashes", flash)

main()

"""

předešlá = cesta [-1]
for jeskyňky in zadani
    if předešlá in jeskyňky
        for jeskyňka in jeskyňky
            if jeskyňka != předešlá
                if jeskyňka jeMalým and jeskyňka in cesta
                    break
"""