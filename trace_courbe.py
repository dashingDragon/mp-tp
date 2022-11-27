# ce fichier est à copier dans le dossier de travail courant (celui où se situe votre fichier python
# on en importe le contenu en écrivant en première ligne from trace_courbe import * et en éxécutant le fichier comme un script (Ctrl+shift+E
# trace prend comme argument deux listes de même dimension
# trace multi prend comme arguments une liste de taille n et une liste de listes de taille n (pour faire plusieurs courbes
# NE PAS MODIFIER CE FICHIER


from matplotlib import pyplot as plt


def trace(liste_x, liste_y, log=False):
    fig = plt.figure()
    if (log):
        plt.semilogx()
    plt.plot(liste_x, liste_y)
    fig.show()


def trace_multi(liste_x, listes_y, log=False):
    fig = plt.figure()
    if (log):
        plt.semilogx()
    for liste_y in listes_y:
        plt.plot(liste_x, liste_y)
    fig.show()
