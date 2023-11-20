nom = "merguez"
prix = 2
quantite_en_stock = 120
print (nom,prix,"$",quantite_en_stock)
quantite_achetee = int(input ("combien voulez vous de merguez ? "))

quantite_en_stock -= quantite_achetee
print ("il reste : ",quantite_en_stock,"merguez")

prix *= 1.10

print ("le prix des merguez est passé à : " ,prix,"$")