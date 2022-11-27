# Exercice 11
def div_xor(a, b, c):
    if type(a) == int and type(b) == int and type(c) == int:
        if a % b == 0 and a % c == 0:
            return "FALSE. a est divisible par b et c."
        if (a % b == 0 or a % c == 0):
            return "TRUE. a est divisible par b ou par c."
        else:
            return "FALSE. a n'est pas divisible par b ni c."
    else:
        return "Les entrées ne sont pas du bon type."


print(div_xor(1, 2, 3))
print(div_xor(15, 5, 3))
print(div_xor(14, 2, 3))

# Exercice 12
from math import *


def volume_sphere(r):
    return (4 / 3) * pi * r ** 3


print(volume_sphere(5))


# Exercice 13
def surface_sphere(r):
    return 4 * pi * (r) ** 2


print(surface_sphere(5))


# Exercice 14
def info_sphere(r):
    return r, surface_sphere(r), volume_sphere(r)


print(info_sphere(5))


# Exercice 15
def est_bissextile(a):
    if a % 4 == 0 and not (a % 100 == 0):
        return "L'année " + str(a) + " est bissextile."
    else:
        return "L'année " + str(a) + " n'est pas bissextile."


print(est_bissextile(2000))
print(est_bissextile(1945))
print(est_bissextile(1362))
print(est_bissextile(1348))
