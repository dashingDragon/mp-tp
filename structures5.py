def rang(i, l):
    a = 0
    b = 0
    for y in range(len(l)):
        if l[y] < l[i]:
            a += 1
        elif l[y] == l[i]:
            b += 1
    return a, b


def l_zeros(l):
    list = []
    for i in range(len(l)):
        list.append(0)
    return list


def tri_naif(l):
    liste_retour = l_zeros(l)  # crée la liste remplie de 0
    for i in range(len(l)):
        nb_avant, nb_idtq = rang(i, l)  # récupère les deux informations sur l'élément l[i]
        for x in range(nb_idtq):  # effectue autant de boucles qu'il y a d'occurence de l[i] dans l
            liste_retour[nb_avant + x] = l[i]  # remplit liste_retour par l[i]
    return liste_retour


def cherche(x, l):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1


def maximum(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max


def minimum(l):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min


def maximum_bis(l):
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    index = 0
    while l[index] != max:
        index += 1
    return max, index + 1


print(maximum_bis([51, 6, 684, 4, 684, 65, 46, 4, 31, 3, 21, 35, 46, 87, 98, 4, 651, 6, 51, 3, 584, 684]))
