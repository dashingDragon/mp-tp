def premiers(n):
    i = 2
    l = []
    while i ** 2 <= n:
        if n % i == 0:
            l.append(i)
        i += 1
    return l


def couples(n):
    l = premiers(n)
    c = []
    for p in l:
        v = 0
        while n % p == 0 and n != 1:
            v += 1
            n = n // p
        if v != 0:
            c.append([p, v])
    return c


def decomposition(n):
    c = couples(n)
    s = str(n) + " ="
    for i in c:
        s += " + " + str(i[0]) + "^" + str(i[1])
    return s


print(couples(3500))
print(decomposition(3500))
print(premiers(165798635))
