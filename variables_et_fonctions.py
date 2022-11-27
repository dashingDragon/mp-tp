#Exercice 4
def xor(a,b): return not(a and b)
print(xor(True, False))
print(xor(True, True))
print(xor(False, False))

#Exercice 5 (On définit 0 comme FALSE et 1 comme TRUE)
#Retourne 1 si les nombres comparés sont égaux
def et_entier(a,b):
    if(a==b):
        return 1;
    else:
        return 0;
print(et_entier(1,0))
print(et_entier(1,1))

#Retourne 1 si l'un des deux nombres au moins vaut 1
def ou_entier(a,b):
    if(a==1 or b==1):
        return 1
    else:
        return 0
print(ou_entier(1,0))
print(ou_entier(0,0))

#Retourne 0 si l'un des deux nombres au moins vaut 1
def non_entier(a,b):
    if(a==1 or b==1):
        return 0
    else:
        return 1
print(non_entier(1,0))
print(non_entier(0,0))

#Retourne 1 si les nombres comparés sont différents
def xor_entier(a,b):
    if(a==b):
        return 0
    else:
        return 1
print(xor_entier(1,0))
print(xor_entier(1,1))