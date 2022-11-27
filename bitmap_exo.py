import numpy as np


def valeur(fichier, debut, longueur):
    """Traduit les 4 octets en base 256"""
    fichier.seek(debut)
    v = 0
    p = 0
    for b in fichier.read(longueur):
        v += b * 256 ** p
        p += 1
    return v


def valeur_inv(dec):
    """Traduit un nombre décimal en 4 octets en base 256"""
    l_octets = [0, 0, 0, 0]
    p = 3
    while p >= 0:
        l_octets[p] += dec // (256**p)
        dec %= (256**p)
        p -= 1
    return l_octets


def cree_liste(fichier, debut, longueur):
    """Met en liste les valeurs des pixels"""
    fichier.seek(debut)
    liste_retour = list()
    for e in fichier.read(longueur):
        liste_retour.append(e)
    return liste_retour


def sup4(n):
    """Retourne le plus petit entier divisible par 4 supérieur ou égal à n."""
    m = n
    while m % 4 != 0:
        m += 1
    return m


def matrice_pixels(fichier):
    """Affiche les pixels dans un tableau"""
    nl = valeur(fichier, 22, 4)
    nc = valeur(fichier, 18, 4)
    ncm = sup4(nc)
    offset = valeur(fichier, 10, 4)
    taille = valeur(fichier, 34, 4)
    fichier.seek(offset)
    liste_pixels = list()
    for i in fichier.read(taille):
        liste_pixels.append(i)
    A = np.zeros([nl, ncm], int)
    i = nl - 1
    j = 0
    for e in liste_pixels:
        if j > nc:
            A[i][j] = 0
        else:
            A[i][j] = e
        j += 1
        if j + 1 > ncm:
            j = 0
            i -= 1
    return A


def liste_entete(fichier):
    """Retourne sous forme de liste les parties du fichier"""
    t_fic = valeur(fichier, 2, 4)
    offset = valeur(fichier, 10, 4)
    print("### Entête du fichier ###\r\n"
          "Taille du fichier : {0} octets.\r\n"
          "Offset : {1} octets.".format(t_fic, offset))
    t_ent = valeur(fichier, 14, 4)
    nl = valeur(fichier, 22, 4)
    nc = valeur(fichier, 18, 4)
    t_im = valeur(fichier, 34, 4)
    print("### Entête de l'image ###\r\n"
          "Taille de l'entête : {0} octets.\r\n"
          "Largeur : {1} colonnes.\r\n"
          "Hauteur : {2} lignes.\r\n"
          "Taille de l'image : {3} octets.".format(t_ent, nc, nl, t_im))
    pal = cree_liste(fichier, 54, 1024)
    return pal


def cree_liste_pixels(B):
    """Passe d'une matrice à une liste de pixels"""
    hauteur, largeur = np.shape(B)
    liste_pixels = list()
    for i in range(hauteur - 1, -1, -1):
        for j in range(largeur):
            liste_pixels.append(int(B[i][j]))
    return liste_pixels


def get_padding(M):
    """Donne le padding d'une matrice numpy"""
    h, l = np.shape(M)
    boucle = True
    c = l - 1
    while boucle:
        for i in range(l):
            if M[i][c] != 0:
                boucle = False
                break
            c -= 1
    return l - c - 1


def remove_padding(M, padding):
    """Retire le padding d'une matrice numpy"""
    SM = M.copy()
    for i in range(padding):
        SM = np.delete(SM, np.shape(SM)[1] - 1, 1)
    return SM


def add_padding(M, padding):
    """Ajoute un padding à une matrice numpy"""
    N = M.copy()
    h, l = np.shape(N)
    liste_zeros = np.zeros([h, padding])
    return np.concatenate((N, liste_zeros), axis=1).astype(int)


def miroir_vertical(M):
    """Applique un miroir vertical à une matrice numpy"""
    padding = get_padding(M)
    N = remove_padding(M, padding)
    h, l = np.shape(N)
    R = np.zeros([h, l], int)
    for i in range(h):
        for j in range(l):
            R[i][j] = N[i][l - 1 - j]
    return add_padding(R, padding)


def miroir_horizontal(M):
    """Applique un miroir horizontal à une matrice numpy"""
    h, l = np.shape(M)
    R = np.zeros([h, l], int)
    for i in range(h):
        for j in range(l):
            R[i][j] = M[h - 1 - i][j]
    return R


def rotation(M):
    """Fait tourner une matrice numpy de 90° dans le sens trigo"""
    N = remove_padding(M, get_padding(M))
    N = np.rot90(N)
    h, l = np.shape(N)
    if sup4(l) - l != 0:
        liste_zeros = np.array([h, sup4(l) - l])
        N = np.concatenate((N, liste_zeros), axis=1)
    return N.astype(int)


def miroir_vertical_image(fichier, nom):
    """Crée une copie nommée nom contenant l'image en miroir vertical"""
    with open(fichier, 'rb') as f:
        data = f.read()
        M = matrice_pixels(f)
        N = miroir_vertical(M)
        offset = valeur(f, 10, 4)
        f.close()

    with open(nom, 'wb') as copie:
        copie.write(data)
        copie.seek(offset)
        copie.write(bytearray(cree_liste_pixels(N)))
        copie.close()


def miroir_horizontal_image(fichier, nom):
    """Crée une copie nommée nom contenant l'image en miroir horizontal"""
    with open(fichier, 'rb') as f:
        data = f.read()
        M = matrice_pixels(f)
        N = miroir_horizontal(M)
        offset = valeur(f, 10, 4)
        f.close()

    with open(nom, 'wb') as copie:
        copie.write(data)
        copie.seek(offset)
        copie.write(bytearray(cree_liste_pixels(N)))
        copie.close()


def rotation_image(fichier, nom):
    """Crée une copie nommée nom contenant l'image en rotation 90° dans le sens trigo"""
    with open(fichier, 'rb') as f:
        offset = valeur(f, 10, 4)
        f.seek(0)
        data = f.read(offset)
        M = matrice_pixels(f)
        N = rotation(M)
        f.close()

    with open(nom, 'wb') as copie:
        copie.write(data)
        t_im = np.shape(N)[0] * np.shape(N)[1]
        t_fic = offset + t_im

        copie.seek(2)
        copie.write(bytearray(valeur_inv(t_fic)))
        copie.seek(22)
        copie.write(bytearray(valeur_inv(np.shape(N)[0])))
        copie.seek(18)
        copie.write(bytearray(valeur_inv(np.shape(N)[1])))
        copie.seek(34)
        copie.write(bytearray(valeur_inv(t_im)))
        copie.seek(offset)
        copie.write(bytearray(cree_liste_pixels(N)))
        copie.close()


miroir_vertical_image('mon_image.bmp', 'copie_verticale.bmp')
miroir_horizontal_image('mon_image.bmp', 'copie_horizontale.bmp')
rotation_image('mon_image.bmp', 'copie_rotation.bmp')