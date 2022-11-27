#Exercice 28
# fonction est_vide renvoie un booléen, prend comme argument une liste
# fonction pile_vide renvoie une liste
# procédure push , prend comme argument une liste
# fonction pop renvoie une liste, prend comme argument une liste

def est_vide(list):
    return (len(list) == 0)
print(est_vide([1]))
print(est_vide([]))

def pile_vide():
    return []
print(pile_vide())

# push et pop existent déjà dans la bibliothèque python