def Fact(n):
    if n == 0:
        return 1
    liste = [None] * n
    liste[0] = 1
    for i in range(0, n - 1):
        liste[i + 1] = (i + 2) * liste[i]
    return liste[n - 1]


print(Fact(0), Fact(1), Fact(7))


def Fact(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


print(Fact(0), Fact(1), Fact(7))


def Fact(n):
    if n == 0:
        return 1
    else:
        return n * Fact(n - 1)


print(Fact(0), Fact(1), Fact(7))


def ProdFact(a, n):
    if n == 0:
        return a
    liste = [None] * n
    liste[0] = 1
    for i in range(0, n - 1):
        liste[i + 1] = (i + 2) * liste[i]
    return a * liste[n - 1]


print(ProdFact(13, 0), ProdFact(13, 1), ProdFact(13, 5))


def ProdFact(a, n):
    p = a
    for i in range(1, n + 1):
        p *= i
    return p


print(ProdFact(13, 0), ProdFact(13, 1), ProdFact(13, 5))


def ProdFact(a, n):
    if n == 0:
        return a
    else:
        return n * ProdFact(a, n - 1)


print(ProdFact(13, 0), ProdFact(13, 1), ProdFact(13, 5))


def ProdFact(a, n):
    if n == 0:
        return a
    else:
        return a * ProdFact(n, n - 1)  # a * n * ProdFact(1, n-1) fonctionne également


print(ProdFact(13, 0), ProdFact(13, 1), ProdFact(13, 5))


def ProdFact(a, n):
    return a * Fact(n)


print(ProdFact(13, 0), ProdFact(13, 1), ProdFact(13, 5))


def ProdFact(a, n):  # On reprend la définition de ProdFact sans Fact

    if n == 0:
        return a
    else:
        return a * n * ProdFact(1, n - 1)


def Fact(n):
    return ProdFact(1, n)


print(Fact(0), Fact(1), Fact(7))


def Fibo(n):
    liste = [None]*(n+1)
    liste[0], liste[1] = 0, 1
    for i in range(2, n+1):
        liste[i] = liste[i-1] + liste[i-2]
    return liste[n]


print(Fibo(10))


def Fibo(n):
    a = 0
    b = 1
    for i in range(n-1):
        b, a = b+a, b
    return b


print(Fibo(10))


def Fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)


print(Fibo(10))


def FiboGene(a, b, n):
    liste = [None] * (n+1)
    liste[0], liste[1] = a, b
    for i in range(2, n+1):
        liste[i] = liste[i - 1] + liste[i - 2]
    return liste[n]


print(FiboGene(5, 7, 5))


def FiboGene(a, b, n):
    x = a
    y = b
    for i in range(n - 1):
        y, x = x+y, y
    return y


print(FiboGene(5, 7, 5))


def FiboGene(a, b, n):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return FiboGene(a, b, n-1) + FiboGene(a, b, n-2)


print(FiboGene(5, 7, 5))


def FiboGene(a, b, n):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return FiboGene(b, a+b, n-1)


print(FiboGene(5, 7, 5))


def ChiffresDix(n):
    q = n
    while q > 0:
        q, r = divmod(q, 10)
        print(r)


ChiffresDix(1789)


def ChiffresDix(n):
    if n > 0:
        print(n%10)
        ChiffresDix(n//10)


ChiffresDix(1789)


def NombreDix(l):
    n = 0
    for i in range(len(l)):
        n += l[i]*10**i
    return n


print(NombreDix([9, 8, 7, 1]))


#def NombreDix(l):
#    if len(l) != 0:
#        return l[0]+NombreDix(l[1:])*10**len(l)
#
#print(NombreDix([9, 8, 7, 1]))
