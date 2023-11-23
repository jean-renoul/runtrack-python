L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def produit():
    resultat = 1
    for valeur in L:
        if 25 < valeur < 90:
            resultat = valeur * resultat
    return resultat

print (produit())