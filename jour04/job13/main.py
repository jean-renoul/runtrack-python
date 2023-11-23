liste = [10,20,30,20,10,50,60,40,80,50,40]

def length(une_liste):
    count = 0
    for i in une_liste:
        count += 1
    return count
    

liste_sans_doublon = []

for i in liste:
    if i not in liste_sans_doublon:
        liste_sans_doublon += [i]

liste = liste_sans_doublon

print(liste)