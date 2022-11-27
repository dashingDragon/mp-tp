#Exercice 20
def heures(sec):
    h = sec//3600
    sec -= 3600*h
    min = sec//60
    sec -= 60*min
    sec = sec%60
    return (h,min,sec)

def format_heure(tuple):
    print("{0}:{1}:{2}".format(tuple[0],tuple[1],tuple[2]))

format_heure(heures(4580))

#Exercice 21
def concat_n(a, n):
    return str(a)*n

print(concat_n('Lala', 5))

#Exercice 22
def tiers_s(a):
    if(len(a) < 3):
        return
    while(len(a)%3 != 0):
        a += " ";
    tiers1 = int(len(a)/3-1)
    tiers2 = int(2*len(a)/3-1)
    return (a[0:tiers1], a[tiers1:tiers2], a[tiers2: int(len(a))])
print(tiers_s(concat_n('Lalala', 3)))
print(tiers_s('baobaobaobaobaoba'))