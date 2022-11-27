def multiples(p, n):
    liste = [1]
    index = 2
    while index <= n:
        if p % index == 0:
            liste.append(index)
        index += 1
    return liste


def multiple(p, n):
    liste = [1]
    for index in range(2, n + 1):
        if p % index == 0:
            liste.append(index)
    return liste


def pow_max(n, m):
    p = 1
    while n ** p <= m:
        p += 1
    return p - 1


def divisions(p, n):
    nb_div = 0
    while n % p == 0:
        n //= p
        nb_div += 1
    return nb_div


def somme_carres(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i ** 2
    return somme


def somme_maj(m):
    p = 1
    somme = 0
    while somme <= m:
        somme += p
        p += 1
    return p - 1


def nb_char(s):
    s = str(s)
    s = s.lower()
    liste_voyelles = ["a", "e", "i", "o", "u", "y"]
    nombre_voyelles = 0
    for index_lettre in range(len(s)):
        for index_voyelle in range(len(liste_voyelles)):
            if liste_voyelles[index_voyelle] == s[index_lettre]:
                nombre_voyelles += 1
    return nombre_voyelles, len(s) - nombre_voyelles


def nb_char(s):
    s = str(s)
    s = s.lower()
    liste_voyelles = ["a", "e", "i", "o", "u", "y"]
    nombre_voyelles = 0
    for index in range(len(s)):
        if liste_voyelles.__contains__(s[index]):
            nombre_voyelles += 1
    return nombre_voyelles, len(s) - nombre_voyelles


def dernier_index(s, p):
    for index in range(len(s) - 1, -1, -1):
        if s[index] == p:
            return index
    return -1


def palindrome(s):
    for index in range(len(s) // 2):
        print(index)
        if s[index] != s[len(s) - 1 - index]:
            return False
    return True


def retourne(s):
    new = str()
    for letter in range(len(s) - 1, -1, -1):
        new += s[letter]
    return new


def retourne_liste(l):
    new_list = []
    for i in range(len(l) - 1, -1, -1):
        new_list.append(l[i])
    return new_list


def retourne_nombre(n):
    new = int()
    for i in range(nombre_chiffres(n)):
        unite = n % 10
        new *= 10
        new += unite
        n = n // 10
    return new


def nombre_chiffres(n):
    counter = 0
    while n >= 1:
        n = n // 10
        counter += 1
    return counter


def fichier_ext(s):
    dot = dernier_index(s, '.')
    return s[:dot], s[dot + 1:]


def nombres_multiples(l, p):
    count = 0
    for i in l:
        if i % p == 0:
            count += 1
    return count
