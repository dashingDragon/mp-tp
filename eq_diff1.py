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


def f(x):
    return np.sin(x)**2


def g(x):
    return np.cos(x)**2


# liste_x = np.linspace(-np.pi, np.pi, 500)
# t_y = [f(liste_x), g(liste_x)]
# trace_multi(liste_x, t_y)


def trace_carre(x, y):
    liste_x = np.linspace(x, y, 500)
    trace(liste_x, liste_x ** 2)


def trace_f2(x, y):
    liste_x = np.linspace(x, y, 500)
    trace(liste_x, np.sqrt(liste_x ** 2 - 4))


def x_puissance_n(x, y):
    liste_x = np.linspace(x, y, 500)
    liste_y = []
    for i in range(1, 11):
        liste_y.append(liste_x**i)
    trace_multi(liste_x, liste_y)


def sinc(x):
    #if x == 0:
    if x.any() == 0:
        return 1
    else:
        return np.sin(x)/x


def trace_sinc(x, y):
    liste_x = np.linspace(x, y, 500)
    liste_y = []
    #for i in liste_x:
    #    liste_y.append(sinc(i))
    #trace(liste_x, liste_y)
    trace(liste_x, sinc(liste_x))


def H(x, Q):
    return 1 / np.sqrt((1-x)**2 + x**2/Q**2)


def G(x, Q):
    return 20*np.log10(H(x, Q))


#trace_sinc(10, 20)

# 4.3
#liste_x = np.linspace(0, 3, 500)
#liste_Q = np.linspace(0.1, 5, 10)
#
#listes_y = []
#for Q in liste_Q:
#    liste_y = []
#    for i in liste_x:
#        liste_y.append(H(i, Q))
#    listes_y.append(liste_y)
#trace_multi(liste_x, listes_y)

# 4.4
#liste_x = np.logspace(-2, 2, 500)
#liste_y = H(liste_x, 0.3)
#trace(liste_x, liste_y, True)


liste_x = np.logspace(-2, 2, 500)
liste_Q = np.linspace(0.1, 5, 10)
listes_y = []
for q in liste_Q:
    liste_y = G(liste_x, q)
    listes_y.append(liste_y)


trace_multi(liste_x, listes_y, True)




