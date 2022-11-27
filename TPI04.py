# 1.a)
def Echanger(t, i, j):
    t[i], t[j] = t[j], t[i]


liste = [3, 1, 4, 1, 5, 9, 2, 6]
Echanger(liste, 1, 2)
print(liste)


# 1.b)
def Ranger(t, k):
    n = k
    while t[n] < t[n - 1]:
        Echanger(t, n, n - 1)
        n -= 1


liste = [1, 2, 3, 5, 6, 4]
Ranger(liste, 5)
print(liste)


# 1.c)
def Rangerbis(t, k):
    aux = t[k]
    n = k
    while aux < t[n - 1]:
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
        i = k
        while i > 0 and t[i] < t[i - 1]:
            Echanger(t, i, i - 1)
            i -= 1


liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParInsertion(liste)
print(liste)


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
    for j in range(n-1, -1, -1):
        i = IndiceDuMaximum(t, 0, j+1)
        if i != j:
            Echanger(t, i, j)


liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParSelectionBis(liste)
print(liste)


# 3.a)
def TrierParInsertionBis(t):
    def Echanger(i, j):
        t[i], t[j] = t[j], t[i]
    n = len(t)
    for k in range(n):
        i = k
        while i > 0 and t[i] < t[i - 1]:
            Echanger(i, i - 1)
            i -= 1


liste = [3, 1, 4, 1, 5, 9, 2, 6]
TrierParInsertionBis(liste)
print(liste)