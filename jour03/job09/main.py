a = float(input("première note:"))
b = float(input("deuxième note:"))
c = float(input("troisième note:"))

def moyenne(a,b,c):
    return ((a+b+c)/3)

moyenne_etudiant = moyenne(a,b,c)

print (f"la moyenne de l'étdiant est de :{moyenne_etudiant:.1f}")

if moyenne_etudiant <= 15 and moyenne_etudiant >= 20:
    print ("Très bon élève")
elif moyenne_etudiant <= 11 and moyenne_etudiant >= 14:
    print ("Bon élève")
elif moyenne_etudiant <= 8 and moyenne_etudiant >= 10:
    print ("Elève moyen")
elif moyenne_etudiant <= 0 and moyenne_etudiant >= 7:
    print ("Elève devant faire des efforts")
    