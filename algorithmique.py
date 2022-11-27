import math


def maximum(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] >= max:
            max = l[i]
    return max


def nbmax(l):
    max = maximum(l)
    c = 0
    for i in range(len(l)):
        if l[i] == max:
            c += 1
    return c


def nb_occurences(l):
    """Fonction qui retourne une liste donnant le nombre d'occurences de chaque entier d'une liste d'entiers relatifs"""
    max = l[0]  # faisable en 4 lignes avec les fonctions préprogrammées max et min
    min = l[0]
    for i in range(len(l)):
        if l[i] >= max:
            max = l[i]
        elif l[i] <= min:
            min = l[i]
    length = max - min + 1
    l_retour = [0 for i in range(length)]  # [0]*(max-min+1)
    for i in range(len(l)):
        l_retour[l[i] - min] += 1
    return l_retour


print(nb_occurences([1, 2, 3, 1, 3, 68, 46, 514, 31, 351, 65, 465, 13, 21, 354, 68, 46, 1, 31, 3, 545, 43, 51, 351, 351]))


def classement(l):
    """Fonction qui associe à chaque score d'une liste ordonnée son rang"""
    temp = [0 for i in range(l[len(l) - 1])]
    for i in range(len(l)):
        temp[l[i] - 1] += 1
    print(temp)
    retour = [0 for i in range(len(l))]
    print(retour)
    c = 0
    for i in range(len(l)):
        retour[i] = len(l) - temp[l[i] - 1] + 1 - c
    return retour


print(classement([1, 2, 2, 3, 4, 5, 5]))


def max_c(l):
    return l[len(l) - 1]


def nb_max_c(l):
    for i in range(len(l)):
        if l[len(l) - 1 - i] != l[len(l) - 2 - i]:
            return i + 1
    return len(l)


def stats(l):
    dico = {"max": 0, "min": 0, "moy": 0, "ect": 0, "med": 0}
    max = l[0]
    min = l[0]
    for i in range(len(l)):
        if l[i] >= max:
            max = l[i]
        elif l[i] <= min:
            min = l[i]
    dico["max"] = max
    dico["min"] = min
    somme = 0
    for i in range(len(l)):
        somme += l[i]
    dico["moy"] = somme / len(l)
    somme2 = 0
    for i in range(len(l)):
        somme2 += (l[i] - dico["moy"])**2
    dico["ect"] = math.sqrt(somme2/len(l))
    from exercices.structures5 import tri_naif
    triee = tri_naif(l)
    dico["med"] = triee[int(len(l)/2)]
    return dico


def statsnn(t):
    liste = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            liste.append(t[i][j])
    return stats(liste)


def dizaines(l):
    """Fonction qui retourne le nombre qui a le plus grand chiffre des dizaines"""
    l_dizaines = []  # liste contenant les dizaines des nombres de l
    for i in range(len(l)):  # boucle qui remplit la liste des dizaines
        n = l[i]
        n //= 10
        n %= 10
        l_dizaines.append(n)
    for i in range(len(l)):
        if l_dizaines[i] == maximum(l_dizaines):  # si le nombre des dizaines correspond au plus grand nombre des
            # dizaines, alors la condition est remplie et on connait l'indice du nombre dans l: i
            return l[i]


print(dizaines([1, 2, 3, 1, 3, 68, 46, 514, 31, 351, 65, 465, 13, 21, 354, 68, 46, 1, 31, 3, 545, 43, 51, 351, 351]))

