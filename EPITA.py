from random import *

def etat(i, j):
    if abs(i) == 2 or abs(j) == 2:
        return 3
    return abs(i)+abs(j)


def liste_voisins(i, j):
    if etat(i, j) == 3:
        return [(i, j)]
    else:
        return [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]


def marche():
    pos = (0, 0)
    c = 0
    while etat(pos[0], pos[1]) != 3:
        lv = liste_voisins(pos[0], pos[1])
        pos = choice(lv)
        c += 1
    return c


def simulation(n):
    s = 0 ; sc = 0
    for i in range(n):
        t = marche()
        s += t
        sc += t**2
    e = s/n
    v = n/(n-1)*(sc/n - e**2)
    return e, v


print(simulation(1000000))

