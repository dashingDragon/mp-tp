# Q1 On modélise la file de voiture par une liste de booléens, si une case contient une voiture, l'élément de la
# liste correspondant contient la valeur True, sinon elle contient la valeur False


# Q2
A = 11 * [False]
A[0] = True
A[2] = True
A[3] = True
A[10] = True
print(A)


# Q3
def occupe(L, i):
    return L[i] == True


# Q4 C'est un problème de dénombrement : pour constituer chaque file, il y a deux choix possibles pour chaque case,
# et n cases, donc 2^n façons de choisir une file

# Q5
def egal(L1, L2):
    if len(L1) != len(L2):
        return False
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return False
    return True


# Q6 Dans le meilleur des cas, len(L1)!=len(L2) donc on ne fait qu'une comparaison et la complexité est en temps
# constant, sinon, la complexité est linéaire

# Q7 La fonction retourne une valeur de type booléenne

# Q8 avancer(A, False) renvoie la liste B, avancer(B, true) fait avancer chaque voiture d'une case et place une
# voiture sur la case a plus à gauche. Ainsi, avancer(avancer(A, False), True) renvoie la liste [True, False, True,
# False, True, True, False, False, False, False, False]

# Q9
def avancer(L, b):
    R = L[:]
    R[len(R) - 1] = False
    for i in range(len(R) - 1, 0, -1):
        if R[i - 1]:
            R[i] = True
            R[i - 1] = False
    R[0] = b
    return R


L = [True, False, True, False, True, True, False, False, False, False, False]
print("Avancer")
print("L = ", L)
print("L = ", avancer(L, True))


def avancer_fin(L, m):
    R = L[:m] + avancer(L[m:], False)
    return R


print("Avancer fin 4")
print("L = ", L)
print("L = ", avancer_fin(L, 4))

print("Avancer fin 2")
print("L = ", L)
print("L = ", avancer_fin(L, 2))


# Q10
def avancer_debut(L, b, m):
    R = avancer(L[:m], b) + L[m:]
    return R


print("Avancer debut 4")
print("L = ", L)
print("L = ", avancer_debut(L, True, 4))


# Q11
def avancer_debut_bloque(L, b, m):
    R = L[:]
    for i in range(m - 1, 0, -1):
        if not R[i]:
            if R[i - 1]:
                R[i] = True
                R[i - 1] = False
    R[0] = b
    return R


print("Avancer debut bloque 6")
print("L = ", L)
print("L = ", avancer_debut_bloque(L, True, 6))


# Q12
def avancer_files(L1, b1, L2, b2):
    R1 = L1[:]
    R2 = L2[:]
    # étape 1
    m = len(R1) // 2
    R1 = avancer_fin(R1, m)
    R2 = avancer_fin(R2, m)
    # étape 2
    if R1[m - 1]:
        R1 = avancer_debut(R1, b1, m)
        R2 = avancer_debut_bloque(R2, b2, m)
    else:
        R2 = avancer_debut(R2, b2, m)
        R1 = avancer_debut_bloque(R1, b1, m)
    return [R1, R2]


D = [False, True, False, True, False]
E = [False, True, True, False, False]
print("avance files", avancer_files(D, False, E, False))


# Q13 l'appel renvoie [[False, False, True, False, True], [False, True, False, True, False]]

# Q14 Dans le cas où la file L1 est pleine et qu'on ajoute une voiture dans L1 à chaque étape, la file L2 serait
# indéfiniment bloquée car il y aurait toujours une voiture dans L1 prête à traverser l'intersection

# Q15 L1 étant prioritaire, il faut 5 étapes pour faire traverser les 5 voitures initialement dans L1, puis 5 étapes
# pour faire passer les 4 voitures dans L2, et durant les 4 dernières étapes on ajoute une voiture dans L1.
# Finalement on arrive dans la configuration b en 10 étapes au minimum.

# Q16 Supposons que l'on puisse passer de a à c. Dans la configuration c, il y a une voiture dans chaque file après
# l'intersection, donc à l'avant-dernière étape dans chaque file il y avait une voiture dans la case de
# l'intersection, ce qui est impossible. Par l'absurde, on ne peut pas passer de a à c.

# Q17
def elim_double(L):
    R = []
    R.append(L[0])
    for i in range(1, len(L)):
        if L[i] != L[i - 1]:
            R.append(L[i])
    return R


print(elim_double([1, 1, 3, 3, 3, 7]))


# Q18 La fonction récursive renvoie [1, 3, 5]

# Q19 Prenons par exemple la liste non triée [1, 2, 1]. Comme 1!=2, puis comme 2!=1, la fonction doublons renvoie [1,
# 2, 1], donc la fonction n'est pas applicable aux listes non triées.

# Q20 La fonction recherche retourne un booléen. but est une liste de listes de booléens, et espace est une liste de
# listes de listes de booléens. Successeurs retourne une liste (res) de listes (R1 et R2) de listes de booléens.

# Q21 in1 parcourt la liste de droite à gauchen donc est de complexité n tandis que in2 utilise une recherche
# dichotomique sur une liste triée donc est de complexité ln(n).Il est ainsi plus intéressant d'utiliser la fonction
# in2.

# Q22
def versEntier(L):
    s = 0
    n = len(L)
    for i in range(n - 1, -1, -1):
        if L[i]:
            s += 2 ** (n - 1 - i)
    return s


print(versEntier([True, True, False, False, True]))


# Q23 Taille doit valoir au minimum l'exposant de la première puissance de 2 supérieure à n. La condition doit être i
# >= 0

# Q24 On procède par l'absurde. Supposons que la fonction recherche ne se termine jamais. On dispose alors de la
# suite (an) où pour tout entier n, an désigne

# Q25
def recherche(but, init):
    espace = [init]
    stop = False
    c = 0
    while not stop:
        c += 1
        ancien = espace
        espace = espace + successeurs(espace)
        espace.sort()  # permet de trier espace par ordre croissant
        espace = elim_double(espace)
        stop = egal(ancien, espace)  # fonction d ́efinie `a la question 5
        if but in espace:
            print(c)
            return True
    print(c)
    return False


def successeurs(L):
    res = []
    for x in L:
        L1 = x[0]
        L2 = x[1]
        res.append(avancer_files(L1, False, L2, False))
        res.append(avancer_files(L1, False, L2, True))
        res.append(avancer_files(L1, True, L2, False))
        res.append(avancer_files(L1, True, L2, True))
    return res


debut = [5 * [False], 5 * [False]]
fin = [3 * [False] + 2 * [True], 3 * [False] + 2 * [True]]
print(recherche(fin, debut))
debut = [4 * [True] + 5 * [False], 4 * [True] + 5 * [False]]
fin = [5 * [False] + 4 * [True], 4 * [True] + 5 * [False]]
print(recherche(fin, debut))

# Q26 , 27, 28 pour plus tard.
