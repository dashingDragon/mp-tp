def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


print(factorielle(0), factorielle(1), factorielle(10))

n = 0
while 1 / ((2 * n + 3) * factorielle(n + 1)) > 10 ** (-6):
    n = n + 1
print(n)


def lagrange(x, y, a):
    s = 0
    for i in range(len(x)):
        li = 1
        for k in range(len(x)):
            if k != i:
                li = li * (a - x[k]) / (x[i] - x[k])
        s = s + y[i] * li
    return s


print(lagrange([-1, 0, 1], [4, 0, 4], 3))
