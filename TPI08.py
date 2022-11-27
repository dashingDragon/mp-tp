import time
import random
import numpy as np
import matplotlib.pyplot as plt


def echange(tab, i, j):
    aux = tab[i]
    tab[i] = tab[j]
    tab[j] = aux


def place(tab, deb, fin, val):
    ind = fin - 1
    while ind >= 0 and tab[ind] > val:
        ind -= 1
    return ind + 1


def placedichotomique(tab, deb, fin, val):
    d, f = deb, fin
    while f - d > 0:
        m = (d + f) // 2
        if val < tab[m]:
            f = m
        else:
            d = m + 1
    return d


def indicemax(tab, deb, fin):
    imax = deb
    for i in range(deb + 1, fin):
        if tab[i] > tab[imax]:
            imax = i
    return imax


def indicemin(tab, deb, fin):
    imin = deb
    for i in range(deb + 1, fin):
        if tab[i] < tab[imin]:
            imin = i
    return imin


# Procédures de tris en place

def TPI_lin(t):
    for k in range(len(t)):
        j = place(t, 0, k, t[k])
        if j < k:
            for i in range(k, j, -1):
                echange(t, i - 1, i)


def TPI_lin2(t):
    for k in range(len(t)):
        v = t[k]
        j = k - 1
        while j >= 0 and t[j] > v:
            j -= 1
        j += 1
        if j < k:
            aux = t[k]
            for i in range(k, j, -1):
                t[i] = t[i - 1]
            t[j] = aux


def TPI_dic(t):
    for k in range(len(t)):
        j = placedichotomique(t, 0, k, t[k])
        if j < k:
            for i in range(k, j, -1):
                echange(t, i - 1, i)


def TPI_dic2(t):
    for k in range(len(t)):
        j = placedichotomique(t, 0, k, t[k])
        if j < k:
            aux = t[k]
            for i in range(k, j, -1):
                t[i] = t[i - 1]
            t[j] = aux


def TPS(t):
    for k in range(len(t) - 1, -1, -1):
        j = indicemax(t, 0, k + 1)
        if j < k:
            echange(t, j, k)


def TPS2(t):
    for k in range(len(t)):
        j = indicemin(t, k, len(t))
        if 0 < j:
            echange(t, k, j)


def FTPI_lin(t):
    r = ()
    for k in range(len(t)):
        j = place(r, 0, k, t[k])
        r = r[:j] + (t[k],) + r[j:]
    return r


def FTPI_dic(t):
    r = ()
    for k in range(len(t)):
        j = placedichotomique(r, 0, k, t[k])
        r = r[:j] + (t[k],) + r[j:]
    return r


def pivot2(t, v):
    tg = []
    td = []
    for k in range(len(t)):
        if t[k] < v:
            tg.append(t[k])
        else:
            td.append(t[k])
    return tg, td


def tripivot2(t):
    if len(t) <= 1:
        return t[:]
    else:
        m = len(t) // 2
        v = t[m]
        t.pop(m)
        tg, td = pivot2(t, v)
        return tripivot2(tg) + [v] + tripivot2(td)


def pivot3(t, v):
    tg = []
    tm = []
    td = []
    for k in range(len(t)):
        if t[k] < v:
            tg.append(t[k])
        elif t[k] == v:
            tm.append(t[k])
        else:
            td.append(t[k])
    return tg, tm, td


def tripivot3(t):
    if len(t) <= 1:
        return t[:]
    else:
        m = len(t) // 2
        v = t[m]
        tg, tm, td = pivot3(t, v)
        return tripivot3(tg) + tm + tripivot3(td)


def fusion(la, lb):
    lf = []
    while la != [] or lb != []:
        if lb == [] or (la != [] and la[0] < lb[0]):
            lf.append(la.pop(0))
        else:
            lf.append(lb.pop(0))
    return lf


def TriFusion(l):
    if len(l) <= 1:
        return l[:]
    else:
        p = len(l) // 2
        return fusion(TriFusion(l[p:]), TriFusion(l[:p]))


def pere(k):
    return (k - 1) // 2


def fils(k):
    return 2 * k + 1


def fille(k):
    return 2 * (k + 1)


def sommet(k):
    return k == 0


def echange(t, i, j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux


def compare(t, i, j):
    return t[i] >= t[j]


def remonte(t, k):
    while not (sommet(k) or compare(t, pere(k), k)):
        echange(t, k, pere(k))
        k = pere(k)


def descend(t, k, p):
    l = k
    while (fille(l) < p and not compare(t, l, fille(l))) or (fils(l) < p and not compare(t, l, fils(l))):
        if fille(l) < p and not compare(t, fils(l), fille(l)):
            echange(t, l, fille(l))
            l = fille(l)
        else:
            echange(t, l, fils(l))
            l = fils(l)


def formertas(t):
    for k in range(1, len(t)):
        remonte(t, k)


def triertas(t):
    for p in range(len(t) - 1, 0, -1):
        echange(t, 0, p)
        descend(t, 0, p)


def tripartas(t):
    formertas(t)
    triertas(t)


l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
print(l)
tripartas(l)
print(l)


#
# Tri à bulle
#

# Version avec fonctions auxiliaires

def echange(t, i, j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux


def remontebulle(t, d, f):
    for k in range(d + 1, f):
        if t[k] < t[k - 1]:
            echange(t, k, k - 1)


def tribulle(t):
    for k in range(len(t), 0, -1):  # range(len(t), 1, -1)
        remontebulle(t, 0, k)


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


# Version tout en un

def tribulle(t):
    for k in range(len(t), 0, -1):
        for j in range(1, k):
            if t[j] < t[j - 1]:
                aux = t[j]
                t[j] = t[j - 1]
                t[j - 1] = aux


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


# Version tout en un légèrement simplifiée

def tribulle(t):
    for k in range(len(t) - 1, 0, -1):
        for j in range(k):
            if t[j + 1] < t[j]:
                aux = t[j]
                t[j] = t[j + 1]
                t[j + 1] = aux


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


# Version optimisée

def temoinremontebulle(t, d, f):
    ind = True
    for k in range(d + 1, f):
        if t[k] < t[k - 1]:
            ind = False
            echange(t, k, k - 1)
    return ind


def tribulle(t):
    for k in range(len(t), 0, -1):
        if temoinremontebulle(t, 0, k):
            break


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


# Version optimisée plus propre

def temoinremontebulle(t, d, f):
    ind = False
    for k in range(d + 1, f):
        if t[k] < t[k - 1]:
            ind = True
            echange(t, k, k - 1)
    return ind


def tribulle(t):
    k = len(t)
    while temoinremontebulle(t, 0, k):
        k -= 1


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


# Version optimisée tout en un

def tribulle(t):
    k = len(t) - 1
    encore = True
    while encore:
        encore = False
        for j in range(k):
            if t[j + 1] < t[j]:
                encore = True
                aux = t[j]
                t[j] = t[j + 1]
                t[j + 1] = aux
        k -= 1


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(t)
tribulle(t)
print(t)


def TriPerso(t):
    if len(t) <= 10:
        u = t[:]
        TPS2(u)
        return u
    else:
        m = len(t) // 2
        v = t[m]
        tg, tm, td = pivot3(t, v)
        return TriPerso(tg) + tm + TriPerso(td)


def TriPerso(t):
    if len(t) <= 10:
        u = t[:]
        TPS2(u)
        return u
    else:
        m = len(t) // 2
        v = t[m]
        tg, tm, td = pivot3(t, v)
        return TriPerso(tg) + tm + TriPerso(td)


def TriPerso2(t):
    if len(t) <= 10:
        return list(FTPI_dic(t))
    else:
        m = len(t) // 2
        v = t[m]
        tg, tm, td = pivot3(t, v)
        return TriPerso2(tg) + tm + TriPerso2(td)


def TriFonction(f, l, e):
    s = f.__name__
    l3 = l.copy()
    print(60 * '*')
    print('Tri effectué par la fonction', s)
    t1 = time.time()
    for i in range(e):
        if f == tribulle or f == tripartas:
            l2 = l[:]
            f(l2)
        else:
            l2 = f(l)
    t2 = time.time()
    #  print(s, '(', l, ') = ', l2, sep='')
    # j'ai retiré la ligne du dessus par souci de lisibilité
    print("Etat de tri : ", sorted(l3) == l2)
    print("Temps de tri : ", t2 - t1, "secondes")
    print(60 * '*')
    return t2 - t1


def TableauComparatif2(a, n, e):
    x = np.array([])
    for i in range(1, n):
        x = np.append(x, 10 ** i)
    for f in a:
        y = np.array([])
        for i in range(1, n):
            l = [random.random() * 100 for i in range(10 ** i)]
            tps = TriFonction(f, l, e)
            y = np.append(y, tps)
        plt.plot(x, y, label=f.__name__)
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps de tri (s)")
    plt.legend()
    plt.xscale('log')
    plt.grid(True, which="both", linestyle="--")
    plt.show()


TableauComparatif2([TPI_lin, TPI_lin2, TPS, TPS2, FTPI_lin, tribulle, TriPerso, TriPerso2], 4, 1)
TableauComparatif2([TriFusion, tripivot2, tripivot3, tripartas, TriPerso, TriPerso2], 5, 1)

# Tri de 10000 petites listes par les fonctions lentes
TableauComparatif2([TPI_lin, TPI_lin2, TPI_dic, TPI_dic2, TPS, TPS2, FTPI_dic, FTPI_lin, tribulle, TriPerso, TriPerso2], 3, 10000)

