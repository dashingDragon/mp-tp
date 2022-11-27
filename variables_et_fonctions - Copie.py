#Exercice 4
def xor(a,b):
    return (a or b) and not((a and b))

#Exercice 5
def et_entier(a,b):
    return a*b
def ou_entier(a,b):
    return a+b - a*b
def non_entier(a,b):
    return  1 - (a+b - a*b)
def xor_entier(a,b):
    return (a+b)*(a-b)**2

#Exercice 7
def div(a,b):
    return (a%b==0)

#Exercice 8
def div_rev(a,b):
    return (a%b==0 or b%a==0)

#Exercice 9
def div_ou(a,b,c):
    return (a%b==0 and a%c==0)

#Exercice 10
def div_ou(a,b,c):
    return (a%b==0 or a%c==0)

#Exercice 11
def div_xor(a,b,c):
    return ((a%b==0 or a%c==0) and (not(a%b==0 and a%c==0)))