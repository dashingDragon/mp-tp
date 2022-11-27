from time import time
import math


def crible(n):
    liste_bool = [True] * (n + 1)
    liste_bool[0], liste_bool[1] = False, False
    i = 2
    t = time()
    while i ** 2 <= n:
        if liste_bool[i]:
            for j in range(i * i, n + 1, i):
                liste_bool[j] = False
        i += 1
    return "temps : " + str(time() - t) + "\n", liste_bool


print(crible(10 ** 4))


# méthode des rectangles à droite
# exemple de l'intégrale de la fonction t donne 4*(1+t**2) sur [0, 1]


def rect_d(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for k in range(1, n + 1):
        s += f(a + k * pas)
    return s * pas


def rect_m(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for k in range(n):
        s += f(a + (k + 1 / 2) * pas)
    return s * pas


def rect_g(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for k in range(n):
        s += f(a + k * pas)
    return s * pas


def rect_d_opti(f, a, b, n):
    pas = (b - a) / n
    s = 0
    x = a + pas
    for k in range(n):
        s += f(x)
        x += pas
    return s * pas


def rect_m_opti(f, a, b, n):
    pas = (b - a) / n
    s = 0
    x = a + pas / 2
    for k in range(n):
        s += f(x)
        x += pas
    return s * pas


def rect_g_opti(f, a, b, n):
    pas = (b - a) / n
    s = 0
    x = a
    for k in range(n):
        s += f(x)
        x += pas
    return s * pas


def trapeze(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for k in range(n):
        s += (f(a + k * pas) + f(a + (k + 1) * pas)) / 2
    return s * pas


def simpson(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for k in range(n):
        s += (f(a + k * pas) + 4 * f(a + (2 * k + 1) * pas / 2) + f(a + (k + 1) * pas)) / 6
    return s * pas


def simpson_bis(f, a, b, n):
    h = (b - a) / n
    s1 = 0
    s2 = a + h / 2
    for k in range(1, n):
        s1 += f(a + k * h)
        s2 += f(a + (k + 1 / 2) * h)
    return h / 6 * (f(a) + f(b) + 2 * s1 + 4 * s2)


def eval(f):
    t = time()
    v = f(lambda t: 4 / (1 + t * t), 0, 1, 10 ** 6)
    dt = time() - t
    print("Temps écoulé : ", "{:.5f}".format(round(dt, 5)), " Ecart : ", format(math.pi - v, '.3e'), " | Fonction : ",
          f.__name__, )


eval(rect_d)
eval(rect_d_opti)
eval(rect_m)
eval(rect_m_opti)
eval(rect_g)
eval(rect_g_opti)
eval(trapeze)
eval(simpson)
eval(simpson_bis)
