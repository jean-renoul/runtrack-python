a = float(input("première note:"))
b = float(input("deuxième note:"))
c = float(input("troisième note:"))

def moyenne(a,b,c):
    return ((a+b+c)/3)

moyenne_etudiant = moyenne(a,b,c)

print (f"la moyenne de l'étudiant est de :{moyenne_etudiant:.1f}")

if 15 <= moyenne_etudiant <=  20:
    print ("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print ("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print ("Elève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print ("Elève devant faire des efforts")
    