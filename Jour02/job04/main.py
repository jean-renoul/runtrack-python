N = int(input("entrez un nombre:"))
print ("La table de multiplication de :",N,"est:")
for i in range (1,11):
    if N > 0:
        print(i,"x",N,"=",i*N)
    else:
        print ("ERREUR")