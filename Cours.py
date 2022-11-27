import numpy as np


def pivot(M, k):
    n = len(M)
    pivot = 0
    for i in range(k, n):
        if abs(M[i, k]) > pivot:
            pivot = abs(M[i, k])
            ligne_p = i
    if pivot == 0:
        return -1
    else:
        return ligne_p


def inversion(M, E, k, q):
    Mi = M.copy()
    Ei = E.copy()
    Mi[k] = M[q]
    Mi[q] = M[k]
    Ei[k] = E[q]
    Ei[q] = E[k]
    return Mi, Ei


def calcul_coeff(M, E, k):
    pivot = M(k, k)
    n = len(M)
    for i in range(k+1, n):
        a = M[i, k]/pivot
        for j in range(k+1, n):
            M[i, j] = M[i, j] - a*M[k, j]
        E[i] = E[i] - a*E[k]
        M[i, k] = 0


def matsup(M, E):
    n = len(M)
    for k in range(n-1):
        q = pivot(M, k)
        if q >= k:
            (M, E) = inversion(M, E, k, q)
            calcul_coeff(M, E, k)
        else:
            return -1
    return M, E


def solution(M, E):
    S = np.zeros_like(E)
    n = len(S)
    S[n-1] = E[n-1]/M[n-1, n-1]
    for i in range(n-2, -1, -1):
        num = E[i]
        for j in range(i+1, n):
            num -= M[i, j]*S[i, j]
        S[i] = num / M[i, i]
    return S
