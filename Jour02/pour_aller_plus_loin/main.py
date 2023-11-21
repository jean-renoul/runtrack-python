longueur1 = int(input("entrez la longueur du premier coté:"))
longueur2 = int(input("entrez la longueur du deuxième coté:"))
longueur3 = int(input("entrez la longueur du troisième coté:"))

if (longueur1 + longueur2 >= longueur3) and (longueur1 + longueur3 >= longueur2) and (longueur3 + longueur2 >= longueur1):
    print ("Il est possible de construire un triangle")

    if (longueur1==longueur2==longueur3):
        print ("Ce triangle est équilatéral")
    elif (longueur1==longueur2!=longueur3) or (longueur3==longueur2!=longueur1) or (longueur1==longueur3!=longueur2):
        if (longueur1**2==(longueur2**2+longueur3**2)) or (longueur3**2==(longueur2**2+longueur1**2)) or (longueur2**2==(longueur1**2+longueur3**2)):
            print ("Ce triangle sera isocèle-rectangle")
        else:
            print ("Ce triangle est isocèle")
    elif (longueur1**2==(longueur2**2+longueur3**2)) or (longueur3**2==(longueur2**2+longueur1**2)) or (longueur2**2==(longueur1**2+longueur3**2)):
        print ("Ce triangle est rectangle")
    else:
        print ("Ce triangle est quelconque")

else:
    print ("Il n'est pas possible de construire un triangle")