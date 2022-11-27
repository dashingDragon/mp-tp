def sommes_partielles(l):
    list = []
    for liste in l:
        sum = 0
        for integer in liste:
            sum += integer
        list.append(sum)
    return list


def tnp_alea(n, p):
    if n < 1 or p < 1:
        return []
    tnp = []
    from random import randint
    for i in range(n):
        ligne = []
        for j in range(p):
            ligne.append(randint(1, 10))
        tnp.append(ligne)
    return tnp


def diagonale(n):
    """Retourne un tableau contenant des zéros partout sauf en sa diagonale"""
    if n < 1:
        return []
    tnp = []  # crée le tableau
    from random import randint
    for i in range(n):  # parcourt les lignes
        ligne = []  # exemple pour 10 colonnes, la première ligne sera [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(n):  # parcourt les cases de ma ligne
            if i == j:  # cas où on est sur la diagonale
                ligne.append(randint(1, 10))  # ou ligne.append(1)
            else:
                ligne.append(0)
        tnp.append(ligne)  # met la ligne dans le tableau
    return tnp  # [ [1,0...], [0, 1, 0... ], [0, 0, 1, 0..] .... ]


def somme_ligne(t):
    """Retourne la liste des sommes des lignes"""
    list_ligne = []  # liste des lignes
    for i in range(len(t)):  # parcourt les lignes
        sum = 0  # variable contenant la somme des valeurs
        for j in range(len(t[i])):  # parcourt les cases
            sum += t[i][j]  # ajoute la valeur de la case à la somme
        list_ligne.append(sum)  # ajoute la somme à la liste des sommes
    return list_ligne


def somme_colonne(t):
    list_colonne = list([0]*len(t[0]))
    #  ou bien
    list_colonne = []
    for i in range(len(t[0])):
        list_colonne.append(0)
    #  puis
    for i in range(len(t)):
        for j in range(len(t[i])):
            list_colonne[j] += t[i][j]
    return list_colonne


def trace(t):
    sum = 0
    for i in range(len(t)):
        sum += t[i][i]
    return sum


def det22(t):
    somme1 = 1
    somme2 = 1
    for i in range(len(t)):
        somme1 *= t[i][i]
        somme2 *= t[len(t)-1-i][i]
    return somme1 - somme2

