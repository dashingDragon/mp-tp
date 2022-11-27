import random
import stack


# 1.a)
def Echanger(t, i, j):
    t[i], t[j] = t[j], t[i]


liste = [3, 1, 4, 1, 5, 9, 2, 6]
Echanger(liste, 1, 2)
print(liste)


# 1.b)
def Ranger(t, k):
    n = k
    while n > 0 and t[n] < t[n - 1]:
        Echanger(t, n, n - 1)
        n -= 1


liste = [1, 2, 3, 5, 6, 4]
Ranger(liste, 5)
print(liste)


# 1.c)
def Rangerbis(t, k):
    aux = t[k]
    n = k
    while n > 0 and aux < t[n - 1]:
        t[n] = t[n - 1]
        n -= 1
    t[n] = aux


liste = [1, 2, 3, 5, 6, 4]
Ranger(liste, 5)
print(liste)


# 1.d)
def TrierParInsertion(t):
    n = len(t)
    for k in range(n):
        Ranger(t, k)


print("Tri par insertion")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParInsertion(liste)
print(liste)
liste2 = [random.randint(0, 1000) for i in range(1000)]
print(liste2)
TrierParInsertion(liste2)
print(liste2)
print(sorted(liste2) == liste2)


# 2.a)
def IndiceDuMinimum(t, a, b):
    im = a
    for k in range(a + 1, b):
        if t[k] < t[im]:
            im = k
    return im


liste = [3, 1, 4, 1, 5, 9, 2, 6]
print(IndiceDuMinimum(liste, 4, 7))


# 2.b)
def TrierParSelection(t):
    n = len(t)
    for j in range(n):
        i = IndiceDuMinimum(t, j, n)
        if i != j:
            Echanger(t, i, j)


print("Tri par sélection")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParSelection(liste)
print(liste)


# 2.c)
def IndiceDuMaximum(t, a, b):
    im = a
    for k in range(a + 1, b):
        if t[k] > t[im]:
            im = k
    return im


liste = [3, 1, 4, 1, 5, 9, 2, 6]
print(IndiceDuMaximum(liste, 4, 7))


# 2.d)
def TrierParSelectionBis(t):
    n = len(t)
    for j in range(n - 1, -1, -1):
        i = IndiceDuMaximum(t, 0, j + 1)
        if i != j:
            Echanger(t, i, j)


liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParSelectionBis(liste)
print(liste)


# 3.a)
def TrierParInsertionBis(t):
    def Echanger(i, j):
        t[i], t[j] = t[j], t[i]

    def Ranger(k):
        n = k
        while n > 0 and t[n] < t[n - 1]:
            Echanger(n, n - 1)
            n -= 1

    n = len(t)
    for k in range(n):
        Ranger(k)


print("Tri par insertion bis")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParInsertionBis(liste)
print(liste)


# 3.b)
def TrierParInsertionTer(t):
    n = len(t)
    for k in range(n):
        n = k
        while n > 0 and t[n] < t[n - 1]:
            t[n], t[n - 1] = t[n - 1], t[n]
            n -= 1


print("Tri par insertion Ter")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParInsertionTer(liste)
print(liste)


# 4.a)
def TPI(t):
    n = len(t)
    ne = 0
    nc = 0
    for k in range(n):
        n = k
        boucle = True
        while n > 0 and boucle:
            nc += 1
            if t[n] < t[n - 1]:
                t[n], t[n - 1] = t[n - 1], t[n]
                ne += 1
                n -= 1
            else:
                boucle = False
    return nc, ne


print("TPI")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
print(TPI(liste))
print(liste)
liste2 = [random.randint(0, 1000) for i in range(1000)]
print(liste2)
TPI(liste2)
print(liste2)
print(sorted(liste2) == liste2)


# 4.b)
def TPS(t):
    n = len(t)
    ne = 0
    nc = 0
    for j in range(n):
        im = j
        for k in range(j + 1, n):
            nc += 1
            if t[k] < t[im]:
                im = k
        i = im
        if i != j:
            Echanger(t, i, j)
            ne += 1
    return nc, ne


print("TPS")
liste = [3, 1, 4, 1, 5, 9, 2, 6]
print(TPS(liste))
print(liste)
liste2 = [random.randint(0, 1000) for i in range(1000)]
print(liste2)
TPS(liste2)
print(liste2)
print(sorted(liste2) == liste2)


# 5.a)
def RangerRec(t, k):
    if k == 0:
        return
    imax = IndiceDuMaximum(t, 0, k + 1)
    Echanger(t, imax, k)
    RangerRec(t, k - 1)


print("Ranger Rec")
liste = [1, 2, 3, 5, 6, 4]
RangerRec(liste, 5)
print(liste)


# 5.b)
def TrierParInsertionRec(t):
    n = len(t)
    if n == 0:
        return
    RangerRec(t, n - 1)
    TrierParInsertionRec(t[:n - 1])


print("Tri par insertion Rec")
liste = [1, 2, 3, 5, 6, 4]
TrierParInsertionRec(liste)
print(liste)


# 5.c)
def TrierParInsertionRec(t):
    def RangerRec(k):
        if k == 0:
            return
        imax = IndiceDuMaximum(t, 0, k + 1)
        Echanger(t, imax, k)
        RangerRec(k - 1)

    n = len(t)
    if n == 0:
        return
    RangerRec(n - 1)
    TrierParInsertionRec(t[:n - 1])


print("Tri par insertion Rec version interne")
liste = [1, 2, 3, 5, 6, 4]
TrierParInsertionRec(liste)
print(liste)


# 6)
def Trier(p):
    def Bulle(p):  # dans l'idée, on parcourt chaque couple en descendant la pile, on échange les deux éléments selon
        # leur ordre
        a = p.Pop()
        if p.IsEmpty():
            p.Push(a)
            return
        b = p.Pop()
        if a < b:
            p.Push(a)
            Bulle(p)
            p.Push(b)
        else:
            p.Push(b)
            Bulle(p)
            p.Push(a)

    def TailleStack(p):
        a = p.Pop()
        if p.IsEmpty():
            p.Push(a)
            return 0
        n = 1 + TailleStack(p)
        p.Push(a)
        return n

    for i in range(TailleStack(p)):  # peut être optimisé, je répète Bulle autant de fois qu'il y a d'élément dans le
        # stack afin d'être certain que si le maximum est au début, il "remontera" en haut de la pile
        Bulle(p)


print("Tri en utilisant des stacks")
stack1 = stack.Stack()
stack1.Push(3)
stack1.Push(1)
stack1.Push(4)
stack1.Push(1)
stack1.Push(5)
stack1.Push(9)
stack1.Push(2)
stack1.Push(6)
stack1.Print()
Trier(stack1)
stack1.Print()
