def est_dedans(o, l):
    for i in range(len(l)):
        if l[i] == o:
            return True
    return False


def index(o, l):
    for i in range(len(l)):
        if l[i] == o:
            return i
    return -1


def indexfort(o, l):
    l_retour = []
    for i in range(len(l)):
        if l[i] == o:
            l_retour.append(i)
    return l_retour


liste_test = [i ** 7 for i in range(1, 5001)]


def type_ordre(l):
    for i in range(len(l)):
        if l[i] != l[i + 1]:
            if l[i] > l[i + 1]:
                return "décroissant"
            if l[i] < l[i + 1]:
                return "croissant"


def index_dicho(o, l):
    """Retourne l'index d'un élément dans une liste, par dichotomie"""
    a = 0
    b = len(l) - 1
    while b - a > 1:
        m = (a + b) // 2
        if l[m] < o:
            a = m
        else:
            b = m
    if l[a] == o:
        return a
    elif l[b] == o:
        return b
    else:
        return -1


def index_dicho_plus(o, l):
    a = 0
    b = len(l) - 1
    while b - a > 1:
        m = (a + b) // 2
        if l[m] < o:
            if type_ordre(l) == "croissant":
                a = m
            elif type_ordre(l) == "décroissant":
                b = m
        else:
            if type_ordre(l) == "croissant":
                b = m
            elif type_ordre(l) == "décroissant":
                a = m
    if l[a] == o:
        return a
    elif l[b] == o:
        return b
    else:
        return -1


def indexfort_dicho(o, l):
    liste_pos = []
    pos = -1
    a = 0
    b = len(l) - 1
    while b - a > 1:
        m = (a + b) // 2
        if l[m] < o:
            a = m
        else:
            b = m
    if l[a] == o:
        pos = a
    elif l[b] == o:
        pos = b
    liste_pos.append(pos)
    pos2 = pos
    while l[pos2 - 1] == l[pos2]:
        liste_pos.append(pos2 - 1)
        pos2 -= 1
    while l[pos + 1] == l[pos]:
        liste_pos.append(pos + 1)
        pos += 1
    return liste_pos


print(indexfort_dicho(35831808, liste_test))

from random import randint

liste_test2 = [randint(0, 10) for i in range(1000)]
liste_test2.sort()
print(liste_test2)
print(indexfort_dicho(2, liste_test2))


def racine_entiere(n):
    a = 0
    b = n
    steps = 0
    while b - a > 1:
        steps += 1
        m = (b + a) // 2
        if m ** 2 > n:
            b = m
        else:
            a = m
    print(steps)
    if a ** 2 == n:
        return a
    elif b ** 2 == n:
        return b
    else:
        return -1


print(racine_entiere(152418033795988302771179776))
