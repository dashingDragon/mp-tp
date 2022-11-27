def divisible(n, p):
    if n % p == 0:
        return n // p
    else:
        return 0


def jour_fevriers(a):
    if a % 400 == 0 or (a % 4 == 0 and not (a % 100 == 0)) and a > 0:
        return 29
    else:
        return 28


def ordonne(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def coupe_list(l):
    if len(l) == 0:
        return [], []
    elif len(l) > 1:
        return l[len(l) // 2:], l[:len(l) // 2]


def signe(j, m):
    liste = ["bélier", "taureau", "gémeaux", "cancer", "lion", "vierge", "balance", "scorpion", "sagittaire",
             "capricorne", "verseau", "poisson"]
    if j <= 21:
        return liste[m]
    else:
        return liste[m + 1]


def teste_date(j, m, a):
    if 0 < m < 13:
        nombre_jours = jour_fevriers(a)
        if 0 < j < nombre_jours:
            return True
    else:
        return False

