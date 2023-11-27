liste = [] # Déclaration d'une liste vide

def my_sort(liste):
    plage = len(liste) # Longueur de la liste
    i = 0 # Initialisation de la variable i
    nombre_coups = 0 # Initialisation du compteur de coups nécessaires pour le tri
    
    while i < plage:
        j = 0 # Initialisation de la variable i
        while j < plage - i - 1:
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j] # Si l'élément actuel est plus grand que l'élément suivant, les échange pour les trier
                nombre_coups += 1 # Incrémentation du nombre de coups nécessaires
            j += 1
        else:
            j += 1
        i += 1
    print ("Liste triée : ", liste,)
    print ("Le nombre de coups nécessaire est de : ", nombre_coups)


my_sort([9,8,7,11,10])