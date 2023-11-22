def time_to_text(a):
    if a == int(a):
        return  (f"{a//60:.0f} heures et {a%60} minutes")
    else:
        print ("le nombre doit être entier")

print (time_to_text(105))