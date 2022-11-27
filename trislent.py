# Procédures itératives de tri par insertion en place

def TPI1(t):
    for k in range(len(t)):
        j = k - 1
        while j >= 0 and t[j] > t[k]:
            j -= 1
        j += 1
        if j < k:
            for i in range(k, j, -1):
                t[i - 1], t[i] = t[i], t[i - 1]


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPI1(t0)
print(t0)
print()

from math import *


def TPI2(t):
    def echange(i, j):
        nonlocal nbe
        nbe += 1
        aux = t[i]
        t[i] = t[j]
        t[j] = aux

    def compare(i, j):
        nonlocal nbc
        nbc += 1
        return t[i] > t[j]

    nbe, nbc = 0, 0
    for k in range(len(t)):
        j = k - 1
        while j >= 0 and compare(j, k):
            j -= 1
        j += 1
        if j < k:
            for i in range(k, j, -1):
                echange(i, i - 1)
    return nbe, nbc, log(nbe)/log(len(t)),  log(nbc)/log(len(t))


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
print(TPI2(t0))
print(t0)
print()


# Procédures itératives de tri par sélection en place

def TPS1(t):
    for k in range(len(t) - 1, -1, -1):
        imax = 0
        for i in range(1, k + 1):
            if t[i] > t[imax]:
                imax = i
        if imax < k:
            t[imax], t[k] = t[k], t[imax]


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TPS1(t0)
print(t0)
print()


def TPS2(t):
    def echange(i, j):
        nonlocal nbe
        nbe += 1
        aux = t[i]
        t[i] = t[j]
        t[j] = aux

    def compare(i, j):
        nonlocal nbc
        nbc += 1
        return t[i] > t[j]

    nbe, nbc = 0, 0
    for k in range(len(t) - 1, -1, -1):
        imax = 0
        for i in range(1, k + 1):
            if compare(i, imax):
                imax = i
        if imax < k:
            echange(imax, k)
    return nbe, nbc, log(nbe)/len(t),  log(nbc)/log(len(t))


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
print(TPS2(t0))
print(t0)
print()


# procédures itératives de tri à bulles

def TAB1(t):
    for k in range(len(t) - 1, 0, -1):
        for j in range(k):
            if t[j + 1] < t[j]:
                aux = t[j]
                t[j] = t[j + 1]
                t[j + 1] = aux


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TAB1(t0)
print(t0)
print()


def TAB2(t):
    def echange(i, j):
        nonlocal nbe
        nbe += 1
        aux = t[i]
        t[i] = t[j]
        t[j] = aux

    def compare(i, j):
        nonlocal nbc
        nbc += 1
        return t[i] > t[j]

    nbe, nbc = 0, 0
    for k in range(len(t) - 1, 0, -1):
        for j in range(k):
            if compare(j, j + 1):
                echange(j, j + 1)
    return nbe, nbc


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
print(TAB2(t0))
print(t0)
print()


# procédures itératives de tri à bulles optimisé

def TBO1(t):
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


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
TBO1(t0)
print(t0)
print()


def TBO2(t):
    def echange(i, j):
        nonlocal nbe
        nbe += 1
        aux = t[i]
        t[i] = t[j]
        t[j] = aux

    def compare(i, j):
        nonlocal nbc
        nbc += 1
        return t[i] > t[j]

    nbe, nbc = 0, 0
    k = len(t) - 1
    encore = True
    while encore:
        encore = False
        for j in range(k):
            if compare(j, j + 1):
                encore = True
                echange(j, j + 1)
        k -= 1
    return nbe, nbc


t0 = [3, 1, 4, 1, 5, 9, 2, 6]
print(t0)
print(TBO2(t0))
print(t0)
print()

from random import *
from matplotlib import pyplot as plt

def test(f, n):
    t = [random() for k in range(n)]
    return f(t)


print(test(TPI2, 10000))


def tests(lf, n):
    t = [random() for k in range(n)]
    res = []
    for f in lf:
        u = t[:]
        res.append(f(u))
    return res


#print(tests([TPI2, TPS2], 400))
