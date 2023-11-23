L = [1,2,3,4,5]

def liste_numeros():
    L[3] = L[2]+L[4]
    return L


print (L[1])
print (liste_numeros())
print (L[4])