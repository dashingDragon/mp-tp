#Exercice 23
def remplace_premier(list, n):
    list[0] = n
list = [2,3,45,65,98]
remplace_premier(list, 100)
print(list)

#Exercice 24
def debut_1(list, p):
    return list[0:p]
print(debut_1(list, 3))
print(debut_1(list, 5))
print(debut_1(list, 6))

#Exercice 25
def fin_1(list, p):
    if(len(list) <= p):
        return list
    return list[len(list)-p: len(list)]
print(fin_1(list, 3))
print(fin_1(list, 5))
print(fin_1(list, 6))

#Exercice 26
def coupe_en_deux(list):
    if(len(list)%2 == 0):
        i = int(len(list)/2)
    else:
       i = int((len(list)+1)/2)
    return (list[0:i-1], list[i:len(list)])
print(coupe_en_deux([0,25,26,14,25,46,58,57]))
print(coupe_en_deux([0,25,26,14,25,46,58,57,56,1,2,5,4,58,59,64,98,81,23,45]))

#Exercice 27
def remplace_n(list, n, p):
    list[n] = p**2
list_bis = [1,2,3,4,5]
remplace_n(list_bis, 3, 6)
print(list_bis)