def verif (a):
    if a == int(a):
        if a > 0:
            if a % 2 == 0:
                print ("ce nombre est pair")
            else:
                print ("ce nombre est impair")
        else:
            print ("le nombre doit être supérieur à 0")
    else:
        print ("le nombre doit être entier")

verif (5.5)