liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def length(une_liste):
    count = 0
    for i in une_liste:
        count += 1
    return count

def arrondi(nombre):
    return nombre + 0.5 - (nombre + 0.5) % 1


def trier(lst):
    plage = length(lst)
    i = 0
    while i < plage:
        j = 0
        while j < plage - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1

def arrondir(nombres):
    i = 0
    while i < length(nombres):
        nombres[i] = arrondi(nombres[i])
        i += 1

arrondir(liste)
trier(liste)
print (liste)  