L = [1,2,3,4,5]

print (L)

def liste_numeros():
    numero1 = L[0]
    L[0] = L[-1]
    L[-1] = numero1
    return L

print (liste_numeros())