def fonction_triangle(hauteur):
    hauteur_triangle = 0
    print (" " * (hauteur - 1) + "/" + "\\")
    hauteur_triangle +=1
    while hauteur_triangle < hauteur - 1:
        print (" " * (hauteur - (hauteur_triangle+1)) + "/" + " " * (hauteur_triangle * 2) + "\\")
        hauteur_triangle +=1
    print ("/" + ((hauteur - 1) * 2 ) * "_" + "\\")
fonction_triangle(5)