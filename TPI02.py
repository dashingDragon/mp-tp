def fact(n):  # 1.i)
    def aux(a, k):
        if k == 0:
            return a
        else:
            return aux(a * k, k - 1)

    return aux(1, n)


print(fact(0), fact(3))


# 1.ii) On effectue n multiplications : une mult entre a et 1 et n-1 mult entre 1 et n. n soustractions.


def c(n):  # 1.iii)
    def aux(a, k):
        if k == 0:
            return 0
        else:
            return 1 + aux(a * k, k - 1)

    return aux(1, n)


print(c(0), c(10), c(100))


def binomial(n, p):  # 1.iv)
    return fact(n) // (fact(p) * fact(n - p))


print(binomial(5, 3))


#  1.v) Il y a n + p + (n-p) = 2n multiplications, et 2n soustractions


def binomialrec(n, p):  # 2.i)
    if p == 0 or p == n:
        return 1
    else:
        return binomialrec(n - 1, p) + binomialrec(n - 1, p - 1)


print(binomialrec(5, 3))


def c(n, p):  # 2.ii)
    def aux(n, p):
        if p == 0 or p == n:
            return 0
        else:
            return 2 + aux(n - 1, p) + aux(n - 1, p - 1)

    return aux(n, p)


print(c(5, 3))


def binomrec(n, p):  # 3.i)
    if p == 0:
        return 1
    else:
        return int(n / p * binomrec(n - 1, p - 1))


print(binomrec(5, 3))


# 3.ii) On dénombre p divisions et p multiplications, 2p soustractions


def binomrec2(n, p):  # 3.iii)
    if p == 0:
        return 1
    else:
        return int((n - p + 1) / p * binomrec2(n, p - 1))


print(binomrec2(5, 3))


# 3.iv) On a p multiplications, 2p soustractions, p additions


def binomite(n, p):  # 4.i) On choisit la première car le produit comporte un terme en moins et donc est moins lourd
    # en calculs
    produit = 1
    for k in range(p):
        produit *= (n - k) / (p - k)
    return int(produit)


print(binomite(5, 3))


#  4.ii) p multiplications, p divisions, 2p soustractions


def trianglePascal(n):  # 5.i)
    triangle = [[1]]
    for i in range(1, n):  # i va de 1 à n-1
        ligne = [1]
        for j in range(0, i - 1):  # j va de 0 à i-2
            ligne.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        ligne.append(1)
        triangle.append(ligne)
    return triangle


print(trianglePascal(10))


# 5.ii) Pour n = 0, 1, on ne fait aucune addition et aucune soustraction. Pour tout n>=2, le nombre d'addition est
# (n-1)(n-2)/2


def coeffBinomial(n, p):  # 5.iii)
    return trianglePascal(n + 1)[n][p - 1]


print(coeffBinomial(5, 3))


def trianglePascal2(n, p):  # 5.iv)
    triangle = [[1]]
    for i in range(1, n + 1):  # i va de 1 à n-1
        ligne = [1]
        for j in range(0, min(p, i - 1)):  # j va de 0 à i-2
            ligne.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        if p >= i:
            ligne.append(1)
        triangle.append(ligne)
    return triangle


print("5.iv)")
print(trianglePascal2(9, 5))


# 5.v) Je ne sais pas ... mais moins que la fonction trianglePascal() !


def coeffBinomial2(n, p):  # 5.vi)
    return trianglePascal2(n, p).pop().pop()


print("5.vi)")
print(coeffBinomial2(5, 3))


def trianglePascal3(n, p):  # 5.vii)
    liste_bis = [1, 1]
    if n < 2:
        return 1
    compteur = 2
    while compteur <= n:
        liste = liste_bis
        liste_bis = [1]
        for i in range(1, len(liste)):
            liste_bis.append(liste[i - 1] + liste[i])
        liste_bis.append(1)
        compteur += 1
    return liste_bis[:p + 1]


print("5.vii)")
print(trianglePascal3(9, 5))
