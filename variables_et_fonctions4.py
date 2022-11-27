#Exercice 16
def secondes(h,m,s):
    t = 3600*h + 60*m + s
    return t

print(secondes(21,55,45))

#Exercice 17
def heures(sec):
    h = sec//3600
    sec -= 3600*h
    min = sec//60
    sec -= 60*min
    sec = sec%60
    return (h,min,sec)
print(heures(3661))
print(heures(4857))

#Exercice 18
from math import *
def test_racine(n):
    return (sqrt(n**2) == abs(n))

print(test_racine(1))
print(test_racine(-1))
print(test_racine(100000))
print(test_racine(10000000000000000000000))
print(test_racine(100000000000000000000000)) #au bout de 24 chiffres (23 zéros ici)

#Exercice 19
def delta(a,b,c):
    return b**2 - (4*a*c)

def racines_0(a,b,c):
    if(delta(a,b,c) < 0):
        return []
    if(delta(a,b,c) == 0):
        return -b/2*a
    if(delta(a,b,c) > 0):
        return ((-b-sqrt(delta(a,b,c)))/2*a , (-b+sqrt(delta(a,b,c)))/2*a)

print(racines_0(2,5,6))
print(racines_0(2,5,-6))
print(racines_0(1,2,1))
print(racines_0(1,10**10,1)) #le résultat est faux: (-10000000000.0, 0.0) 0 n'est évidemment pas solution

def racines(a,b,c):
    if(delta(a,b,c) < 0):
        return []
    if(delta(a,b,c) == 0):
        return -b/2*a
    if(delta(a,b,c) > 0):
        z = (-b-sqrt(delta(a,b,c)))/2*a
        return (z, -c/a*z)
print(racines(1,10**10,1))