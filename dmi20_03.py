def smul(n, l):
    r = l[:]
    for i in range(len(l)):
        r[i] *= n
    return r

print(smul(4, [1,2,3]))

def vsom(l1, l2):
    assert len(l1) == len(l2)
    r = len(l1)*[0]
    for i in range(len(r)):
        r[i] = l1[i] + l2[i]
    return r

print(vsom([4,5,6], [6,5,4]))


def vdif(l1, l2):
    assert len(l1) == len(l2)
    r = len(l1) * [0]
    for i in range(len(r)):
        r[i] = l1[i] - l2[i]
    return r

print(vdif([1,2,3], [4,5,6]))

def f(x):
    return x

def verlet(n, h, y0, z0):
    y = [y0]
    z = [z0]
    for i in range(n):
        y.append(y[i] + h*f(y[i]) + h**2/2*f(y[i]))
        z.append(z[i] + h/2*(f(y[i]) + f(y[i+1])))
    return y, z


print(verlet(10, 2, 1, 1))
#Partie IV.A
# SELECT DISTINCT masse FROM corps

#SELECT count(*) FROM corps H


# On sélectionne le nombre de corps où datem est inférieur à tmin()

# SELECT DISTINCT id_corps, count(datem) FROM etat WHERE datem <= tmin()


# IV.B.2)
#
