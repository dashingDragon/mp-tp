def jour_fevriers(a):
    if a % 400 == 0 or (a % 4 == 0 and not (a % 100 == 0)):
        return 29
    else:
        return 28


def nb_jours_mois(a):
    l_retour = []
    for i in range(12):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
            l_retour.append(31)
        elif i == 1:
            l_retour.append(jour_fevriers(a))
        else:
            l_retour.append(30)
    return l_retour


def teste_date(j, m, a):
    if 0 < m < 13:
        nombre_jours = 31
        if m == 2:
            nombre_jours = jour_fevriers(a)
        if 0 < j < nombre_jours + 1:
            return True
    else:
        return False


def nb_jours(j, m, a):
    if teste_date(j, m, a):
        mois = nb_jours_mois(a)
        nb_jours = j
        for i in range(m - 1):
            nb_jours += mois[i]
        return nb_jours


def monnaie(p):
    """Fontion qui retourne la décomposition en monnaie la plus simple d'une somme d'argent"""
    liste_prix = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    d = []
    for i in range(len(liste_prix)):
        nb = 0
        while p - liste_prix[i] >= 0.01:  # tente de retirer la valeur du billet/pièce au montant restant
            p -= liste_prix[i]  # réduit le montant de la valeur de la pièce/billet
            nb += 1  # ajoute 1 à la quantité de pièce/billet
        if nb != 0:  # ne fait rien si le nombre de pièce/billet est nul
            d.append((liste_prix[i], nb))  # ajoute le tuple à la liste de retour
    return d


def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nombre_chiffres(n):
    counter = 0
    while n > 0:
        n = n // 10
        counter += 1
    return counter


def retourne_nombre(n):
    new = int()
    for i in range(nombre_chiffres(n) - 1, -1, -1):
        unite = n % 10
        new *= 10
        new += unite
        n = n // 10
    return new


def test_1():
    for i in range(2, 11):
        a = i*99
        b = retourne_nombre(a)
        if a+b != 1089:
            return False
    return True

