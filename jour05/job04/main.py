def tapis(n):
    hauteur_tapis = 0
    print ("+" + "-" * (n+1) + "+")
    while hauteur_tapis <= n:
        ligne = "|"
        for colonne in range(n+1):
            if n - hauteur_tapis == colonne:
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print (ligne)
        hauteur_tapis += 1

    print ("+" + "-" * (n+1) + "+")

    
tapis(4)

