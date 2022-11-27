# Fonctions utiles

import random
import time
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


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPI_lin(t0)
print(t0)


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


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPI_lin2(t0)
print(t0)


def TPI_dic(t):
    for k in range(len(t)):
        j = placedichotomique(t, 0, k, t[k])
        if j < k:
            for i in range(k, j, -1):
                echange(t, i - 1, i)


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPI_dic(t0)
print(t0)


def TPI_dic2(t):
    for k in range(len(t)):
        j = placedichotomique(t, 0, k, t[k])
        if j < k:
            aux = t[k]
            for i in range(k, j, -1):
                t[i] = t[i - 1]
            t[j] = aux


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPI_dic2(t0)
print(t0)


def TPS(t):
    for k in range(len(t) - 1, -1, -1):
        j = indicemax(t, 0, k + 1)
        if j < k:
            echange(t, j, k)


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPS(t0)
print(t0)


def TPS2(t):
    for k in range(len(t)):
        j = indicemin(t, k, len(t))
        if 0 < j:
            echange(t, k, j)


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPS(t0)
print(t0)


# Fonctions de tri pour des tuples

def FTPI_lin(t):
    r = ()
    for k in range(len(t)):
        j = place(r, 0, k, t[k])
        r = r[:j] + (t[k],) + r[j:]
    return r


t0 = (3, 1, 4, 1, 5, 9, 2, 6)
print(t0)
t1 = FTPI_lin(t0)
print(t1)


def FTPI_dic(t):
    r = ()
    for k in range(len(t)):
        j = placedichotomique(r, 0, k, t[k])
        r = r[:j] + (t[k],) + r[j:]
    return r


t0 = (3, 1, 4, 1, 5, 9, 2, 6)
print(t0)
t1 = FTPI_lin(t0)
print(t1)


def TriFonction(f, l):
    s = f.__name__
    l3 = l.copy()
    print(60 * '*')
    print('Tri effectué par la fonction', s)
    t1 = time.time()
    if f == FTPI_lin or f == FTPI_dic:
        l2 = list(f(l))
    else:
        l2 = l.copy()
        f(l2)
    t2 = time.time()
    #  print(s, '(', l, ') = ', l2, sep='')
    # j'ai retiré la ligne du dessus par souci de lisibilité
    print("Etat de tri : ", sorted(l3) == l2)
    print("Temps de tri : ", t2-t1, "secondes")
    print(60 * '*')
    return t2-t1


def TesteFonctionTri(t):
    print()
    print()
    print("Liste initiale :")
    print(t)
    # liste_fonctions = [TPI_lin, TPI_lin2]
    TriFonction(TPI_lin, t)
    TriFonction(TPI_lin2, t)
    TriFonction(TPI_dic, t)
    TriFonction(TPI_dic2, t)
    TriFonction(TPS, t)
    TriFonction(TPS2, t)
    TriFonction(FTPI_lin, t)
    TriFonction(FTPI_dic, t)

    print("Liste finale (ne devrait pas être différente) : ")
    print(t)


#t1 = [random.random() * 100 for i in range(10)]
#TesteFonctionTri(t1)
#t2 = [random.random() * 100 for i in range(100)]
#TesteFonctionTri(t2)
#t3 = [random.random() * 100 for i in range(1000)]
#TesteFonctionTri(t3)
#t4 = [random.random() * 100 for i in range(10000)]
#TesteFonctionTri(t4)


def TableauComparatif2(a, n):
    x= np.array([])
    for i in range(1, n):
        x = np.append(x, 10**i)
    for f in a:
        y = np.array([])
        for i in range(1, n):
            l = [random.random() * 100 for i in range(10**i)]
            tps = TriFonction(f, l)
            y = np.append(y, tps)
        plt.plot(x, y, label=f.__name__)
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps de tri (s)")
    plt.legend()
    plt.xscale('log')
    plt.show()


TableauComparatif2([TPI_lin, TPI_lin2, TPI_dic, TPI_dic2, TPS, TPS2, FTPI_dic, FTPI_lin], 5)

