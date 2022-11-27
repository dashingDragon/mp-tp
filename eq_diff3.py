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
        Tp.append(T[i])
    Tp.append(f(T, x, param))  # pour le rang n
    return Tp


def Euler(f, T, Tx, param=()):
    """Execution de F pour différentes valeurs de x"""
    retour = [T]  # première colonne du tableau sont les conditions initiales
    for j in range(len(Tx) - 1):  # on remplit les x-1 colonnes restantes
        pas = Tx[j + 1] - Tx[j]  # différence entre 2 x consécutifs
        Tp = F(f, T, Tx[j], param)  # on trouve les dérivées (de y' à y^(n) )
        for i in range(len(T)):
            T[i] = T[i] + pas*Tp[i]  # connaissant une valeur de y en x (dans T)
            # et sa dérivée (dans Tp), on trouve y en x+pas
        retour.append(T.copy())
    return retour  # conversion d'une liste python en np.array,
    # juste pr le confort de lecture


def f(T, x, param=()):
    """Equation de y"""
    w = param[0]
    Q = param[1]
    return -w/Q*T[1]-w**2*np.sin(T[0])


liste_x = np.linspace(0, 50, 500)
listes_y = []
liste_Q = np.linspace(0.1, 5, 10)
for q in liste_Q:
    listes_y.append(Euler(f, [1, 0], liste_x, (1, q)))
trace_multi(liste_x, listes_y)

for i in range(len(listes_y)):
    #liste = listes_y[i]
    #tri = []  # tri contient une liste de triplets (x, y, y'), on trie selon x
    #for x in range(len(liste_x)):
    #    tri.append((liste_x[x], liste[x][0], liste[x][1]))
    #tri = sorted(tri)
    #liste_y = []  # contient donc juste y et dy
    #liste_dy = []
    #for x in range(len(tri)):
    #    liste_y.append(tri[x][1])
    #    liste_dy.append(tri[x][2])
    #plt.plot(liste_y, liste_dy)
    liste_y = []
    liste_dy = []
    for couple in listes_y[i]:
        liste_y.append(couple[0])
        liste_dy.append(couple[1])
    plt.plot(liste_y, liste_dy)
plt.show()

val_dx = np.linspace(0.1, 5, 15)
for i in range(len(val_dx)):
    plt.plot(liste_x, Euler(f, [0, val_dx[i]], liste_x, (1, 3)), color=(1-i/len(val_dx), 1-i/len(val_dx), i/len(val_dx)))
plt.show()

liste_a = []
liste_b = []
for i in range(len(val_dx)):
    liste = Euler(f, [0, val_dx[i]], liste_x, (1, 3))
    liste_cy = []
    liste_cdy = []
    for c in range(len(liste)):
        liste_cy.append(liste[c][0])
        liste_cdy.append(liste[c][1])
    plt.plot(liste_cy, liste_cdy)
    #tri = []
    #for i in range(len(liste)):
    #    tri.append((liste[i][0], liste[i][1]))
    #liste_y = []  # contient donc juste y et dy
    #liste_dy = []
    #for x in range(len(tri)):
    #    liste_y.append(tri[x][0])
    #    liste_dy.append(tri[x][1])
    #plt.plot(liste_y, liste_dy)
plt.show()
