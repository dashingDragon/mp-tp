#
# Parcours et cycles du cavalier sur un échiquier de taille p x q
#


import time


#
# Force brute
#

def positions(x, y, p, q):
    dep = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
    return [[x + dx, y + dy] for dx, dy in dep if 0 <= x + dx < p and 0 <= y + dy < q]


def ListeParcoursCycles1(a, b, p, q):  # Toutes les solutions
    ech = [[[True] for j in range(q)] for i in range(p)]
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        if ech[x][y]:
            ech[x][y] = False
            l.append([x, y])
            if len(l) == p * q:
                sol.append(l[:])
            lpo = positions(x, y, p, q)
            for u, v in lpo:
                explore(u, v)
            u, v = l.pop()
            ech[u][v] = True
        elif len(l) == p * q and x == a and y == b:
            cyc.append(l[:])

    explore(a, b)
    return sol, cyc


def CompteParcoursCycles1(a, b, p, q):  # Nombre de solutions
    ech = [[[True] for j in range(q)] for i in range(p)]
    sol = 0
    cyc = 0
    l = []

    def explore(x, y):
        nonlocal sol, cyc
        if ech[x][y]:
            ech[x][y] = False
            l.append([x, y])
            if len(l) == p * q:
                sol += 1
            lpo = positions(x, y, p, q)
            for u, v in lpo:
                explore(u, v)
            u, v = l.pop()
            ech[u][v] = True
        elif len(l) == p * q and x == a and y == b:
            cyc += 1

    explore(a, b)
    return sol, cyc


def TrouveParcours1(a, b, p, q):
    ech = [[[True] for j in range(q)] for i in range(p)]
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        if ech[x][y]:
            ech[x][y] = False
            l.append([x, y])
            if len(l) == p * q:
                return True
            lpo = positions(x, y, p, q)
            for u, v in lpo:
                if explore(u, v):
                    return True
            u, v = l.pop()
            ech[u][v] = True
            return False

    if explore(a, b):
        return l


def TrouveCycle1(a, b, p, q):
    ech = [[[True] for j in range(q)] for i in range(p)]
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        if ech[x][y]:
            ech[x][y] = False
            l.append([x, y])
            lpo = positions(x, y, p, q)
            for u, v in lpo:
                if explore(u, v):
                    return True
            u, v = l.pop()
            ech[u][v] = True
            return False
        elif len(l) == p * q and x == a and y == b:
            return True

    if explore(a, b):
        return l


def Total1(p, q):
    tt, tc = 0, 0
    for a in range(p):
        for b in range(q):
            t, c = CompteParcoursCycles1(a, b, p, q)
            tt += t
            tc += c
    return tt, tc, tc // (p * q)


def Test1(p, q):
    t = time.time()
    res = Total1(p, q)
    u = time.time()
    print(res, u - t)


#
# Détection des blocages avec mémorisation des cases accessibles
#

def possibles(p, q):
    return [[positions(x, y, p, q) for y in range(q)] for x in range(p)]


def probleme(lpp, p, q):
    for x in range(p):
        for y in range(q):
            if lpp[x][y] == []:
                return [x, y]
    return [p, q]


def occupe(lpp, x, y):
    a, b = x, y
    for u, v in lpp[x][y]:
        lpp[u][v].remove([x, y])
        if lpp[u][v] == []:
            a, b = u, v
    return [a, b]


def libere(lpp, x, y):
    for u, v in lpp[x][y]:
        lpp[u][v].append([x, y])


def ListeParcoursCycles2(a, b, p, q):  # Liste des solutions
    ppo = possibles(p, q)
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        l.append([x, y])
        if len(l) == p * q:
            sol.append(l[:])
            if [x, y] in positions(a, b, p, q):
                cyc.append(l[:])
        else:
            u, v = occupe(ppo, x, y)
            if [u, v] != [x, y]:
                explore(u, v)
            else:
                for u, v in ppo[x][y]:
                    explore(u, v)
        u, v = l.pop()
        libere(ppo, u, v)

    if probleme(ppo, p, q) == [p, q]:
        explore(a, b)
    return sol, cyc


def CompteParcoursCycles2(a, b, p, q):  # Nombre de solutions
    ppo = possibles(p, q)
    sol = 0
    cyc = 0
    l = []

    def explore(x, y):
        nonlocal sol, cyc
        l.append([x, y])
        if len(l) == p * q:
            sol += 1
            if [x, y] in positions(a, b, p, q):
                cyc += 1
        else:
            u, v = occupe(ppo, x, y)
            if [u, v] != [x, y]:
                explore(u, v)
            else:
                for u, v in ppo[x][y]:
                    explore(u, v)
        u, v = l.pop()
        libere(ppo, u, v)

    if probleme(ppo, p, q) == [p, q]:
        explore(a, b)
    return sol, cyc


def TrouveParcours2(a, b, p, q):
    ppo = possibles(p, q)
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        l.append([x, y])
        if len(l) == p * q:
            return True
        else:
            u, v = occupe(ppo, x, y)
            if [u, v] != [x, y]:
                if explore(u, v):
                    return True
            else:
                for u, v in ppo[x][y]:
                    if explore(u, v):
                        return True
        u, v = l.pop()
        libere(ppo, u, v)
        return False

    if probleme(ppo, p, q) == [p, q]:
        if explore(a, b):
            return l


def TrouveCycle2(a, b, p, q):
    ppo = possibles(p, q)
    sol = []
    cyc = []
    l = []

    def explore(x, y):
        l.append([x, y])
        if len(l) == p * q:
            if [x, y] in positions(a, b, p, q):
                return True
        else:
            u, v = occupe(ppo, x, y)
            if [u, v] != [x, y]:
                if explore(u, v):
                    return True
            else:
                for u, v in ppo[x][y]:
                    if explore(u, v):
                        return True
        u, v = l.pop()
        libere(ppo, u, v)
        return False

    if probleme(ppo, p, q) == [p, q]:
        if explore(a, b):
            return l


def Total2(p, q):
    tt, tc = 0, 0
    for a in range(p):
        for b in range(q):
            t, c = CompteParcoursCycles2(a, b, p, q)
            tt += t
            tc += c
    return tt, tc, tc // (p * q)


def Test2(p, q):
    t = time.time()
    res = Total2(p, q)
    u = time.time()
    print(res, u - t)