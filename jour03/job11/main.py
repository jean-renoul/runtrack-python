def time_to_text(a):
    if a != int(a) or a < 0:
        print ("le nombre doit être entier et positif")
    else:
        print (f"{a//60:.0f} heures et {a%60} minutes")

time_to_text(10)