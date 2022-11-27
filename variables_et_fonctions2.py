#Exercice 6
#mux(0,y,z) = y
#mux(1,y,z) = z
#Pour 0, la fonction renvoie le second paramètre
#Pour 1, la fonction renvoie le troisième paramètre


#Exercice 7 ET 8
def div(a,b):
    if(type(a) == int and type(b) == int):
        if(a == b):
            return "a et b sont égaux !"
        if(a%b == 0):
            return "a est divisible par b."
        if(b%a == 0):
            return "b est divisible par a."
        else:
            return "Aucune division n'est possible."
    else:
        return "Les entrées ne sont pas du bon type."
print(div(5,2))
print(div(2,5))
print(div(5,5))
print(div(5,15))
print(div(5.0,5))
print(div("a",2))

#Exercice 9
def div_et(a,b,c):
    if(type(a) == int and type(b) == int and type(c) == int):
        if(a%b == 0 and a%c == 0):
            return "a est divisible par b et par c."
        else:
            return "a n'est pas divisible par b et c."
    else:
        return "Les entrées ne sont pas du bon type."

print(div_et(1,2,3))
print(div_et(15,5,3))

#Exercice 10
def div_ou(a,b,c):
    if(type(a) == int and type(b) == int and type(c) == int):
        if(a%b == 0 or a%c == 0):
            return "a est divisible par b ou par c."
        else:
            return "a n'est pas divisible par b ni c."
    else:
        return "Les entrées ne sont pas du bon type."

print(div_ou(1,2,3))
print(div_ou(15,5,3))
print(div_ou(14,2,3))