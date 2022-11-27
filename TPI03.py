import stack

s = stack.Stack()
print(s.IsEmpty())
print(s.Push(1))
print(s.IsEmpty())
print(s.Push(2))
print(s.Pop())
print(s.Pop())


#  print(s.Pop())  donne une erreur de type EmptyStack


def InitPile():
    return stack.Stack()


def EstVide(p):
    return p.IsEmpty()


def Empile(p, x):
    p.Push(x)


def Depile(p):
    assert not EstVide(p)
    return p.Pop()


def AffichePile(p):
    p.Print()


p = InitPile()
print(EstVide(p))
print(Empile(p, 1))
print(EstVide(p))
print(Empile(p, 2))
print(Depile(p))
print(Depile(p))


#  print(Depile(p))  renvoie une erreur de type assertion error


# 3.a)
def Sommet(p):
    a = Depile(p)
    Empile(p, a)
    return a


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)

print("Question 3.a)")
print(Sommet(Pi))
AffichePile(Pi)


# 3.b)
def Echange(p):
    a = Depile(p)
    b = Depile(p)
    Empile(p, a)
    Empile(p, b)


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
print("Question 3.b)")
AffichePile(Pi)
Echange(Pi)
AffichePile(Pi)


# 3.c)
def DesempileSousSousSommet(p):
    a = Depile(p)
    b = Depile(p)
    c = Depile(p)
    Empile(p, b)
    Empile(p, a)
    return c


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 3.c)")
AffichePile(Pi)
print(DesempileSousSousSommet(Pi))
AffichePile(Pi)


# 4)
def Hauteur(p):
    if EstVide(p):
        return 0
    a = Depile(p)
    h = 1 + Hauteur(p)
    Empile(p, a)
    return h


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 4)")
AffichePile(Pi)
print(Hauteur(Pi))
AffichePile(Pi)


# 5.a)
def Base(p):
    p2 = InitPile()
    while not (EstVide(p)):
        Empile(p2, Depile(p))
    b = Depile(p2)
    Empile(p, b)
    while not (EstVide(p2)):
        Empile(p, Depile(p2))
    return b


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 5.a)")
AffichePile(Pi)
print(Base(Pi))
AffichePile(Pi)


# 5.b)
def BaseRec(p):
    a = Depile(p)
    if EstVide(p):
        Empile(p, a)
        return a
    else:
        retour = BaseRec(p)
        Empile(p, a)
    return retour


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 5.b)")
AffichePile(Pi)
print(BaseRec(Pi))
AffichePile(Pi)


# 6.a)
def ExtraireBase(p):
    p2 = InitPile()
    while not (EstVide(p)):
        Empile(p2, Depile(p))
    b = Depile(p2)
    while not (EstVide(p2)):
        Empile(p, Depile(p2))
    return b


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 6.a)")
AffichePile(Pi)
print(ExtraireBase(Pi))
AffichePile(Pi)


# 6.b)
def ExtraireBaseRec(p):
    a = Depile(p)
    if EstVide(p):
        return a
    else:
        retour = ExtraireBaseRec(p)
        Empile(p, a)
    return retour


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 6.b)")
AffichePile(Pi)
print(ExtraireBaseRec(Pi))
AffichePile(Pi)


# 7.a)
def InsererBase(p, a):
    p2 = InitPile()
    while not (EstVide(p)):
        Empile(p2, Depile(p))
    Empile(p2, a)
    while not (EstVide(p2)):
        Empile(p, Depile(p2))


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 7.a)")
AffichePile(Pi)
InsererBase(Pi, 0)
AffichePile(Pi)


# 7.b)
def InsererBaseRec(p, e):
    a = Depile(p)
    if EstVide(p):
        Empile(p, e)
        Empile(p, a)
    else:
        InsererBaseRec(p, e)
        Empile(p, a)


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 7.b)")
AffichePile(Pi)
InsererBaseRec(Pi, 0)
AffichePile(Pi)


# 8.a)
def EnfonceSommet(p):
    s = Sommet(p)
    InsererBase(p, s)
    Depile(p)


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 8.a)")
AffichePile(Pi)
EnfonceSommet(Pi)
AffichePile(Pi)


# 8.b)
def EnfonceSommet(p):
    s = Depile(p)
    p2 = InitPile()
    while not (EstVide(p)):
        Empile(p2, Depile(p))
    Empile(p2, s)
    while not (EstVide(p2)):
        Empile(p, Depile(p2))


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 8.b)")
AffichePile(Pi)
EnfonceSommet(Pi)
AffichePile(Pi)


# 8.c)
def EnfonceSommetRec(p):
    Echange(p)
    a = Depile(p)
    if not EstVide(p):
        b = Depile(p)
        if not EstVide(p):
            Empile(p, b)
            EnfonceSommetRec(p)
        else:
            Empile(p, b)
    Empile(p, a)


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 8.c)")
AffichePile(Pi)
EnfonceSommetRec(Pi)
AffichePile(Pi)


# 9.a)
def Renverser(p):
    p2 = InitPile()
    p3 = InitPile()
    while not EstVide(p):
        Empile(p2, Depile(p))
    while not EstVide(p2):
        Empile(p3, Depile(p2))
    while not EstVide(p3):
        Empile(p, Depile(p3))


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 9.a)")
AffichePile(Pi)
Renverser(Pi)
AffichePile(Pi)


# 9.b)
def RenverserRec(p):
    a = Depile(p)
    if EstVide(p):
        InsererBase(p, a)
        return
    RenverserRec(p)
    InsererBase(p, a)


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 9.b)")
AffichePile(Pi)
RenverserRec(Pi)
AffichePile(Pi)


# 10.a)
def Terme(p, n):
    pr = 1
    p2 = InitPile()
    while pr < n:
        Empile(p2, Depile(p))
        pr += 1
    elt = Depile(p)
    Empile(p, elt)
    while not EstVide(p2):
        Empile(p, Depile(p2))
    return elt


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 10.a)")
AffichePile(Pi)
print(Terme(Pi, 1))
print(Terme(Pi, 2))
print(Terme(Pi, 3))
print(Terme(Pi, 4))
AffichePile(Pi)


# 10.b)
def TermeRec(p, n):
    if n == 1:
        elt = Depile(p)
        Empile(p, elt)
        return elt
    a = Depile(p)
    b = TermeRec(p, n - 1)
    Empile(p, a)
    return b


Pi = InitPile()
Empile(Pi, 1)
Empile(Pi, 2)
Empile(Pi, 3)
Empile(Pi, 4)
print("Question 10.b)")
AffichePile(Pi)
print(TermeRec(Pi, 1))
print(TermeRec(Pi, 2))
print(TermeRec(Pi, 3))
print(TermeRec(Pi, 4))
AffichePile(Pi)


# 11)
def Hanoi(i, j, k):  # i, j, k sont des piles
    if EstVide(i):
        return
    else:
        print(AffichePile(i), "--->", AffichePile(j))
        b = ExtraireBaseRec(i)  # On sélectionne les disques supérieurs au premier disque de i
        Hanoi(i, k, j)  # On envoie les disques supérieurs sur la pile k
        Empile(j, b)  # On pose le disque de i sur j


A = InitPile()
B = InitPile()
C = InitPile()
Empile(A, 3)
Empile(A, 2)
Empile(A, 1)
print("Question 11)")
Hanoi(A, B, C)
