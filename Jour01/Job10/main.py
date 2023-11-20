montant_investissement = 10000
taux_rendement = 1.15

print (montant_investissement * taux_rendement - montant_investissement)

montant_investissement += 5000
taux_rendement += 0.02

print (montant_investissement * taux_rendement - montant_investissement)

montant_investissement *= 0.9
taux_rendement -= 0.01

print ("le montant de final de l'investissement est de",montant_investissement)
print ("et le gain final en fonction du taux de rendement est de",montant_investissement * taux_rendement - montant_investissement)
