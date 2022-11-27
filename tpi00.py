def respect():
    print("bonjour maître!")


def conjuge():
    i = input("Saississez un verbe du deuxième groupe : ")
    rad = i[:-2]
    print(rad + "is")
    print(rad + "is")
    print(rad + "i")
    print(rad + 'issons')
    print(rad + "issez")
    print(rad + "issent")


def valabs(x):
    if x < 0:
        return -x
    return x


def signe(x):
    if x == 0:
        return x
    elif x < 0:
        return -1
    return 1


def pair(x):
    if x % 2 == 0:
        return True
    return False


def calendrier():
    for i in range(1965, 2017):
        if i % 4 == 0:
            continue
        print(i)


def somme(t):
    s = 0
    for e in t:
        s += e
    return s


def produit(t):
    p = 1
    for e in t:
        p *= e
    return p


def appartient(x, t):
    if x in t:
        return True
    return False


def occurences(x, t):
    o = 0
    for e in t:
        if x == e:
            o += 1
    return o


def PremOcc(x, t):
    for i in range(len(t)):
        if t[i] == x:
            return i
    return -1


def DernOcc(x, t):
    for i in range(len(t) - 1, -1, -1):
        if t[i] == x:
            return i
    return -1


def constante(t):
    for i in range(1, len(t)):
        if t[i] != t[i - 1]:
            return False
    return True


def croissante(t):
    for i in range(1, len(t)):
        if t[i] < t[i - 1]:
            return False
    return True


def decroissante(t):
    for i in range(1, len(t)):
        if t[i] > t[i - 1]:
            return False
    return True


def monotone(t):
    if croissante(t) or decroissante(t):
        return True
    return False


def strictementcroissante(t):
    for i in range(1, len(t)):
        if t[i] <= t[i - 1]:
            return False
    return True


def strictementdecroissante(t):
    for i in range(1, len(t)):
        if t[i] >= t[i - 1]:
            return False
    return True


def strictementmonotone(t):
    if strictementcroissante(t) or strictementdecroissante(t):
        return True
    return False


def injective(t):
    while len(t) > 0:
        last = t.pop()
        if last in t:
            return False
    return True


def injectivebis(t):
    return len(set(t)) == len(t)


respect()
conjuge()
print("valabs(-1) renvoie", valabs(-1), "|valabs(1) renvoie", valabs(1))
print("signe(-2) renvoie", signe(-2), "signe(3) renvoie", signe(3), "signe(0) renvoie", signe(0))
calendrier()
print("somme([1, -22, 3]) renvoie", somme([1, -22, 3]))
print("produit([2, -22, 3]) renvoie",produit([2, -22, 3]))
print("appartient(1, [2, 3, 4]) renvoie", appartient(1, [2, 3, 4]), "| appartient(2, [2, 3, 4]) renvoie", appartient(2, [2, 3, 4]))
print(occurences(1, [2, 3, 5, 4, 1, 2, 1, 3, 2, 1]))
print(PremOcc(1, [2, 3, 5, 4, 1, 2, 1, 3, 2, 1]))
print(DernOcc(1, [2, 3, 5, 4, 1, 2, 1, 3, 2, 1]))
print(constante([1, 1, 1, 1, 1, 2, 1]), constante([1, 1, 1, 1, 1, 1, 1]))
print(croissante([1, 2, 3, 4, 5, 6]), croissante([1, 2, 3, 4, 7, 6]))
print(decroissante([6, 5, 4, 3, 2, 1]), decroissante([6, 7, 3, 2, 1]))
print(monotone([1, 1, 1, 1, 1, 2, 1]), monotone([1, 1, 1, 1, 1, 2, 3]), monotone([6, 5, 4, 3, 2, 1]))
print(strictementcroissante([1, 2, 3, 4, 5]), strictementcroissante([1, 1, 3, 4, 5]))
print(strictementdecroissante([5, 4, 3, 2, 1]), strictementdecroissante([5, 4, 3, 1, 1]))
print(strictementmonotone([2, 1]), strictementmonotone([1, 2, 3]), strictementmonotone([2, 2, 1]))
print(injective([1, 1, 2, 3, 4, 5]), injective([1, 6, 2, 3, 4, 5]))
print(injectivebis([1, 1, 2, 3, 4, 5]), injectivebis([1, 6, 2, 3, 4, 5]))


# serge.bouju@gmail.com
