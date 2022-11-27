import time
import random
import numpy as np
import matplotlib.pyplot as plt


#
# Fonction de fusion avec les listes utilisées comme des tableaux
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
# Variante avec les listes utilisées comme des tableaux, avec utilisation des connecteurs logiques
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
# Variante avec création dynamique de la liste
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
# Variante qui vide les listes à fusionner
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


# Variante avec usage des connecteurs

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
# Fonction de tri par fusion, enfin !
#

def TriFusion(l):
    if len(l) <= 1:
        return l[:]
    else:
        p = len(l) // 2
        return fusion(TriFusion(l[p:]), TriFusion(l[:p]))


print(TriFusion([3, 1, 4, 1, 5, 9, 2, 6]))


#
# Procédure de tri par fusion en place dans un tableau
#

def echange(t, i, j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux


def fusionpartielle(t, d, m, f):
    ka, kb = d, m
    while ka < kb and kb < f:
        if t[ka] > t[kb]:
            for k in range(kb, ka, -1):
                echange(t, k, k - 1)
            kb += 1
        ka += 1


def trifusionpartielle(t, d, f):
    if f - d > 1:
        m = (d + f) // 2
        trifusionpartielle(t, d, m)
        trifusionpartielle(t, m, f)
        fusionpartielle(t, d, m, f)


def trifusion(t):
    trifusionpartielle(t, 0, len(t))


t = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
print(t)
trifusion(t)
print(t)


#
# Fonction de tri rapide (quick sort)
#

def pivot2(t, ip):
    tg = []
    td = []
    v = t[ip]
    for k in range(0, ip):
        if t[k] < v:
            tg.append(t[k])
        else:
            td.append(t[k])
    for k in range(ip + 1, len(t)):
        if t[k] < v:
            tg.append(t[k])
        else:
            td.append(t[k])
    return tg, td


t = [3, 1, 4, 1, 5, 9, 2, 6]
print(pivot2(t, 4))


def tripivot2(t):
    if len(t) <= 1:
        return t[:]
    else:
        m = len(t) // 2
        tg, td = pivot2(t, m)
        return tripivot2(tg) + [t[m]] + tripivot2(td)


print(tripivot2([3, 1, 4, 1, 5, 9, 2, 6]))


#
# Variante avec 3 listes
#

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
# Procédure de tri rapide en place
#

def echange(t, i, j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux


def pivotpartiel(t, d, f):
    j = d + 1
    v = t[d]
    for k in range(d + 1, f):
        if t[k] < v:
            if j < k:
                echange(t, j, k)
            j += 1
    j -= 1
    if d < j:
        echange(t, d, j)
    return j


def tripivotpartiel(t, d, f):
    if f - d > 1:
        m = (d + f) // 2
        echange(t, d, m)
        j = pivotpartiel(t, d, f)
        tripivotpartiel(t, d, j)
        tripivotpartiel(t, j + 1, f)


def tripivot(t):
    tripivotpartiel(t, 0, len(t))


def TriFonction(f, l, e):
    s = f.__name__
    l3 = l.copy()
    print(60 * '*')
    print('Tri effectué par la fonction', s)
    t1 = time.time()
    for i in range(e):
        if f == tripivotpartiel or f == trifusionpartielle:
            l2 = l[:]
            f(l2, 0, len(t))
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


TableauComparatif2([tripivot, tripivot2, tripivot3], 6, 10)
TableauComparatif2([trifusion], 4, 10)


