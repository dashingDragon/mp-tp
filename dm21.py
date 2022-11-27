from math import floor


def flotVersTern(n,x):
    l= []
    for i in range(1, n+1):
        l.append(floor(3**n*x)-3*floor(3**(n-1)*x))
    return l

print(flotVersTern(4, 0.5))


def ternVersFlot(l):
    s = 0
    for i in range(1, len(l)+1):
        s += l[i-1] / (3**i)
    return s


print(ternVersFlot([1,1,1,1]))

def ajout(l):
    s=0
    r = l[:]
    for i in range(len(r)):
        s += r[i]
    if s%2==0:
        r.append(-1)

    else:
        r.append(-2)
    return r

print(ajout([1,0,2,1,0]))


def verif(l):
    s=0
    r = l[:]
    for i in range(len(r)-1):
        s+= r[i]
    print(s)
    if s%2==0:
        return r[len(r)-1]==-1
    else:
        return r[len(r)-1]==-2


print(verif([1,0,2,1,0,-2]))