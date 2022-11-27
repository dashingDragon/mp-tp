import numpy as np
from matplotlib import pyplot as plt


def trace(liste_x, liste_y, log=False):
    # fig = plt.figure()
    if log:
        plt.semilogx()
    plt.plot(liste_x, liste_y)
    plt.show()


def trace_multi(liste_x, listes_y, log=False):
    # fig = plt.figure()
    if log:
        plt.semilogx()
    for liste_y in listes_y:
        plt.plot(liste_x, liste_y)
    plt.show()


def F(f, T, x, param=()):
    """création du tableau contenant les dérivées"""
    n = len(T)  # degré de dérivation le plus haut
    Tp = []
    for i in range(1, n):  # de 1 à n-1
        Tp.append(T[1])
    Tp.append(f(T, x, param))  # pour le rang n
    return Tp


def Euler(f, T, Tx, param=()):
    """Execution de F pour différentes valeurs de x"""
    retour = [T]  # première colonne du tableau sont les dérivées de y, de y a y^(n)
    for j in range(len(Tx) - 1):  # on remplit les x-1 colonnes restantes
        pas = Tx[j + 1] - Tx[j]  # différence entre 2 x consécutifs
        Tp = F(f, T, Tx[j], param)  # création de la nouvelle colonne de dérivées, mtn de y' à y^(n+1)
        for i in range(len(T)):
            T[i] = T[i] + pas*Tp[i]
        retour.append(T.copy())
    return np.array(retour)


def f(T, x, param=()):
    """Equation de y"""
    return 5*(2 - T[0])**2


liste_x = np.linspace(0, 10, 500)
trace(liste_x, Euler(f, [1], liste_x))