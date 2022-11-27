import time
import random
import numpy as np
import matplotlib.pyplot as plt


#
# Tri rapide (quick sort)
#

def pivot2(t, v):
    tg = []
    td = []
    for k in range(len(t)):
        if t[k] < v:
            tg.append(t[k])
        else:
            td.append(t[k])
    return tg, td


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(pivot2(t, 5))


def tripivot2(t):
    if len(t) <= 1:
        return t[:]
    else:
        m = len(t) // 2
        v = t[m]
        t.pop(m)
        tg, td = pivot2(t, v)
        return tripivot2(tg) + [v] + tripivot2(td)


print(tripivot2([3, 1, 4, 1, 5, 9, 2, 6]))


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


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(pivot3(t, 5))


def tripivot3(t):
    if len(t) <= 1:
        return t[:]
    else:
        m = len(t) // 2
        v = t[m]
        tg, tm, td = pivot3(t, v)
        return tripivot3(tg) + tm + tripivot3(td)


print(tripivot3([3, 1, 4, 1, 5, 9, 2, 6]))


#
# Version avec les listes utilisées comme des tableaux
#

def fusion(ta, tb):
    na, nb = len(ta), len(tb)
    nf = na + nb
    tf = [None] * nf
    ka, kb = 0, 0
    for kf in range(nf):
        if kb == nb:
            tf[kf] = ta[ka]
            ka += 1
        elif ka == na:
            tf[kf] = tb[kb]
            kb += 1
        elif ta[ka] < tb[kb]:
            tf[kf] = ta[ka]
            ka += 1
        else:
            tf[kf] = tb[kb]
            kb += 1
        kf += 1
    return tf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


# Variante avec un while

def fusion(ta, tb):
    na, nb = len(ta), len(tb)
    nf = na + nb
    tf = [None] * nf
    ka, kb = 0, 0
    while ka + kb < nf:  # while ka < na or kb < nb:
        if kb == nb:
            tf[ka + kb] = ta[ka]
            ka += 1
        elif ka == na:
            tf[ka + kb] = tb[kb]
            kb += 1
        elif ta[ka] < tb[kb]:
            tf[ka + kb] = ta[ka]
            ka += 1
        else:
            tf[ka + kb] = tb[kb]
            kb += 1
    return tf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


#
# Version avec les listes utilisées comme des tableaux, avec utilisation des connecteurs logiques
#

def fusion(ta, tb):
    na, nb = len(ta), len(tb)
    nf = na + nb
    tf = [None] * nf
    ka, kb = 0, 0
    for kf in range(nf):
        if kb == nb or ka < na and ta[ka] < tb[kb]:
            tf[kf] = ta[ka]
            ka += 1
        else:
            tf[kf] = tb[kb]
            kb += 1
        kf += 1
    return tf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


# Variante avec un while

def fusion(ta, tb):
    na, nb = len(ta), len(tb)
    nf = na + nb
    tf = [None] * nf
    ka, kb = 0, 0
    while ka < na or kb < nb:  # while ka + kb < nf:
        if kb == nb or ka < na and ta[ka] < tb[kb]:
            tf[ka + kb] = ta[ka]
            ka += 1
        else:
            tf[ka + kb] = tb[kb]
            kb += 1
    return tf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


#
# Version avec création dynamique de la liste
#

def fusion(la, lb):
    na, nb = len(la), len(lb)
    nf = na + nb
    lf = []
    ka, kb = 0, 0
    for kf in range(nf):
        if kb == nb or ka < na and la[ka] < lb[kb]:
            lf.append(la[ka])
            ka += 1
        else:
            lf.append(lb[kb])
            kb += 1
    return lf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


# Variante avec un while

def fusion(la, lb):
    na, nb = len(la), len(lb)
    nf = na + nb
    lf = []
    ka, kb = 0, 0
    while ka + kb < nf:
        if kb == nb or ka < na and la[ka] < lb[kb]:
            lf.append(la[ka])
            ka += 1
        else:
            lf.append(lb[kb])
            kb += 1
    return lf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


#
# Version qui vide les listes à fusionner
#

def fusion(la, lb):
    lf = []
    while la != [] or lb != []:
        if la == []:
            lf.append(lb.pop(0))
        elif lb == []:
            lf.append(la.pop(0))
        elif la[0] < lb[0]:
            lf.append(la.pop(0))
        else:
            lf.append(lb.pop(0))
    return lf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(a, b)
print(a, b, f)


# variante avec usage des connecteurs

def fusion(la, lb):
    lf = []
    while la != [] or lb != []:
        if lb == [] or (la != [] and la[0] < lb[0]):
            lf.append(la.pop(0))
        else:
            lf.append(lb.pop(0))
    return lf


a = [2, 3, 5, 7, 11]
b = [1, 3, 4, 5, 6, 9]
f = fusion(b, a)
print(a, b, f)


#
# Tri par fusion, enfin !
#

def TriFusion(l):
    if len(l) <= 1:
        return l[:]
    else:
        p = len(l) // 2
        return fusion(TriFusion(l[p:]), TriFusion(l[:p]))


print(TriFusion([3, 1, 4, 1, 5, 9, 2, 6]))


def TriFonction(f, l):
    s = f.__name__
    l3 = l.copy()
    print(60 * '*')
    print('Tri effectué par la fonction', s)
    t1 = time.time()
    l2 = f(l)
    t2 = time.time()
    #  print(s, '(', l, ') = ', l2, sep='')
    # j'ai retiré la ligne du dessus par souci de lisibilité
    print("Etat de tri : ", sorted(l3) == l2)
    print("Temps de tri : ", t2 - t1, "secondes")
    print(60 * '*')
    return t2 - t1


def TesteFonctionTri(t):
    print()
    print()
    print("Liste initiale :")
    print(t)
    # liste_fonctions = [TPI_lin, TPI_lin2]
    TriFonction(tripivot2, t)
    TriFonction(tripivot3, t)
    TriFonction(TriFusion, t)
    print("Liste finale (ne devrait pas être différente) : ")
    print(t)


# t1 = [random.random() * 100 for i in range(10)]
# TesteFonctionTri(t1)
# t2 = [random.random() * 100 for i in range(100)]
# TesteFonctionTri(t2)
# t3 = [random.random() * 100 for i in range(1000)]
# TesteFonctionTri(t3)
# t4 = [random.random() * 100 for i in range(10000)]
# TesteFonctionTri(t4)


def TableauComparatif():
    x = np.array([])
    for i in range(1, 6):
        x = np.append(x, 10 ** i)
    print("Voila la liste des abscisses")
    print(x)
    y = np.array([])
    for i in range(1, 6):
        l = [random.random() * 100 for i in range(10 ** i)]
        tps = TriFonction(tripivot2, l)
        y = np.append(y, tps)
    plt.plot(x, y, label="tripivot2")
    y = np.array([])
    for i in range(1, 6):
        l = [random.random() * 100 for i in range(10 ** i)]
        tps = TriFonction(tripivot3, l)
        y = np.append(y, tps)
    plt.plot(x, y, label="tripivot3")
    y = np.array([])
    for i in range(1, 6):
        l = [random.random() * 100 for i in range(10 ** i)]
        tps = TriFonction(TriFusion, l)
        y = np.append(y, tps)
    plt.plot(x, y, label="TriFusion")
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps de tri (s)")
    plt.legend()
    plt.show()


# TableauComparatif()


def TableauComparatif2(a, n):
    x = np.array([])
    for i in range(1, n):
        x = np.append(x, 10 ** i)
    for f in a:
        y = np.array([])
        for i in range(1, n):
            l = [random.random() * 100 for i in range(10 ** i)]
            tps = TriFonction(f, l)
            y = np.append(y, tps)
        plt.plot(x, y, label=f.__name__)
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps de tri (s)")
    plt.legend()
    plt.xscale('log')
    plt.grid(True, which="both", linestyle="--")
    plt.show()


TableauComparatif2([TriFusion, tripivot2, tripivot3], 6)
