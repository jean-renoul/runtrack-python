def length(une_liste):
    count = 0
    for i in une_liste:
        count += 1
    return count

def my_longword(nombre, string):
    resultat = ""
    mot = ""
    est_un_mot = False

    for lettre in string:
        if ('a' <= lettre <= 'z') or ('A' <= lettre <= 'Z'):
            mot += lettre
            est_un_mot = True
        elif est_un_mot:
            est_un_mot = False
            if len(mot) > nombre:
                resultat += mot + " "
            mot = ""

    if est_un_mot and len(mot) > nombre:
        resultat += mot

    return resultat

print (my_longword(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))