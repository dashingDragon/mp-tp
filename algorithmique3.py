def test_chaine(s1, s2, n):
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True


print(test_chaine("Bonjour à tous !", "Bonjour les gens", 8))
print(test_chaine("Bonjour à tous !", "Bonjour les gens", 9))


def recherche_chaine(s, t):
    n = len(s)
    liste_positions = []
    for i in range(len(t) - n):
        if test_chaine(s, t[i:i + n], n):
            liste_positions.append(i)
    return liste_positions


print(recherche_chaine("Ceci", "Ceci est un test pour voir si Ceci détecte le mot 'Ceci'"))


def recherche_hashtag(s, t):
    n = len(s)
    liste_positions = []
    for i in range(len(t)):
        if test_chaine("#" + s, t[i:i + n], n):
            liste_positions.append(i)
    return liste_positions


print(recherche_hashtag("Ceci", "Ceci est un test pour voir si #Ceci détecte le mot 'Ceci'"))


def recherche_mot(s, t):
    char = ["'", '.', ',', ';', ':', '!', '?', ' ', '&', '(', ')', '[', ']', '{', '}', '-', '_', '@', '#']
    n = len(s)
    liste_positions = []
    for i in range(len(t)):
        if test_chaine(s, t[i:i + n], n) and (t[i - 1] in char or i - 1 < 0) and (t[i + n] in char or i + n > len(t)):
            liste_positions.append(i)
    return liste_positions


print(recherche_mot("Ceci", "Ceci est un test pour voir si #Ceci détecte le mot 'Ceci'"))
