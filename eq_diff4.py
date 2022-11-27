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


def F(f, T, param=()):
    """création du tableau contenant les dérivées"""
    couple = f(T, param)  # pour le rang n
    Tp = [T[1], couple[0], T[3], couple[1]]
    return Tp  # doit retourner [dx, dx2, dy, dy2]


def Euler(f, T, Tx, param=()):
    """Execution de F pour différentes valeurs de x"""
    retour = [T]  # première colonne du tableau sont les conditions initiales
    for j in range(len(Tx) - 1):  # on remplit les x-1 colonnes restantes
        pas = Tx[j + 1] - Tx[j]  # différence entre 2 x consécutifs
        Tp = F(f, T, param)  # on trouve les dérivées (de y' à y^(n) )
        for i in range(len(T)):
            T[i] = T[i] + pas * Tp[i]  # connaissant une valeur de y en x (dans T)
            # et sa dérivée (dans Tp), on trouve y en x+pas
        retour.append(T.copy())
    return np.array(retour)  # conversion d'une liste python en np.array,
    # juste pr le confort de lecture


def f(T, param=()):
    """Equation de x et y"""
    dx = T[1]
    dy = T[3]
    a = param[0]
    g = param[1]
    dx2 = -a * np.sqrt(dx ** 2 + dy ** 2) * dx
    dy2 = -a * np.sqrt(dx ** 2 + dy ** 2) * dy - g
    return dx2, dy2


liste_t = np.linspace(0, 50, 500)
liste_vi = np.linspace(0, 500, 10)
for i in liste_vi:
    liste_c = Euler(f, [0, 20, 0, i], liste_t, (0.000005, 10))
    liste_xy = []
    for i in range(len(liste_c)):
        liste_xy.append((liste_c[i][0], liste_c[i][2]))
    plt.plot(sorted(liste_xy))
plt.show()
