from matplotlib import pyplot as plt
from math import *


def cercle():
    n = 200
    lt = [2 * k * pi / n for k in range(n + 1)]
    ly = [sin(t) for t in lt]
    lx = [cos(t) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    #   plt.show()


def ellipse(a, b):
    n = 200
    lt = [2 * k * pi / n for k in range(n + 1)]
    lx = [a * cos(t) for t in lt]
    ly = [b * sin(t) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def parabole(p):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [2 * p * t for t in lt]
    ly = [2 * p * t * t for t in lt]
    plt.plot(lx, ly)
    plt.show()


def hyperbole(a, b):
    n = 2000
    lt = [k / n for k in range(-n, n + 1)]
    lx = [a * cosh(t) for t in lt]
    ly = [b * sinh(t) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def cycloide(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * (t - sin(t)) for t in lt]
    ly = [a * (1 - cos(t)) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def astroide(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * cos(t) ** 3 for t in lt]
    ly = [a * sin(t) ** 3 for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def cissoide(a):
    n = 200
    lt = [3 * k / n for k in range(-n, n + 1)]
    lx = [a * t * t / (1 + t * t) for t in lt]
    ly = [a * t ** 3 / (1 + t * t) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def strophoide(a):
    n = 200
    lt = [3 * k / n for k in range(-n, n + 1)]
    lx = [a * (1 - t * t) / (1 + t * t) for t in lt]
    ly = [a * t * (1 - t * t) / (1 + t * t) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def ovoide(a):
    n = 200
    lt = [10 * k / n for k in range(-n, n + 1)]
    lx = [a / (1 + t * t) ** 2 for t in lt]
    ly = [a * t / (1 + t * t) ** 2 for t in lt]
    plt.plot(lx, ly)
    plt.show()


def lemniscate(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * sin(t) / (1 + cos(t) ** 2) for t in lt]
    ly = [a * sin(t) * cos(t) / (1 + cos(t) ** 2) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def folium(a):
    n = 200
    lt = [10 * k / n for k in range(1, n + 1)]
    lx = [a * t / (1 + t ** 3) for t in lt]
    ly = [a * t ** 2 / (1 + t ** 3) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def lemniscate_g(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * sin(t) for t in lt]
    ly = [a * sin(t) * cos(t) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def cardioide(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * (2 * cos(t) + cos(2 * t)) for t in lt]
    ly = [a * (2 * sin(t) + sin(2 * t)) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def nephroide(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * (3 * cos(t) - cos(3 * t)) for t in lt]
    ly = [a * (3 * sin(t) - sin(3 * t)) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()


def tractrice(a):
    n = 200
    lt = [10 * k / n for k in range(-n, n + 1)]
    lx = [a * (t - tanh(t)) for t in lt]
    ly = [a * 1 / cosh(t) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def trisectrice(a):
    n = 200
    lt = [2 * k * pi / n for k in range(-n, n + 1)]
    lx = [a * (2 * cos(t) + cos(3 * t)) for t in lt]
    ly = [a * (sin(3*t)) for t in lt]
    plt.plot(lx, ly)
    plt.title("TRISECTRICE")
    plt.axis('equal')
    plt.show()


def ellipse_bis(p, e):
    n = 200
    lt = [4* k / n for k in range(-n, n + 1)]
    lx = [p*cos(t)/(1+e*cos(t)) for t in lt]
    ly = [p*sin(t)/(1+e*cos(t)) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def parabole(p):
    n = 200
    lt = [k / n for k in range(-n, n + 1)]
    lx = [p * cos(t) / (1 +  cos(t)) for t in lt]
    ly = [p * sin(t) / (1 +  cos(t)) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def hyperbole_c(p, e):
    n = 200
    lt = [k / n for k in range(-n, n + 1)]
    lx = [p * cos(t) / (1 + e * cos(t)) for t in lt]
    ly = [p * sin(t) / (1 + e * cos(t)) for t in lt]
    plt.plot(lx, ly)
    plt.show()

def mystere_1(d):
    n = 200
    lt = [4 * k / n for k in range(-n, n + 1)]
    lx = [d for t in lt]
    ly = [d*tan(t) for t in lt]
    plt.plot(lx, ly)
    plt.show()


def mystere_2(d):
    n = 200
    lt = [4 * k / n for k in range(-n, n + 1)]
    lx = [d*cos(t)**2 for t in lt]
    ly = [d *sin(t)* cos(t) for t in lt]
    plt.plot(lx, ly)
    plt.axis('equal')
    plt.show()

# ellipse(2, 1)
# parabole(1)
# hyperbole(1,1)
# cycloide(1)
# astroide(1)
# cissoide(1)
# strophoide(1)
# ovoide(1)
# folium(1)
# lemniscate(1)
# lemniscate_g(1)
# cardioide(1)
# nephroide(1)
# tractrice(1)
# trisectrice(1)
# ellipse_bis(2, 0.8)
# parabole(1)
# hyperbole_c(1, 2)
# hyperbole_c(1, sqrt(2))
# mystere_1(1)
mystere_2(1)

# ajouter axes, afficher la courbe pour plusieurs valeurs de a, changer couleurs
