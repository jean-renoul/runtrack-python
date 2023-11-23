liste = [12, 45, 11, 22, 48, 31]

def length(une_liste):
    count = 0
    for i in une_liste:
        count += 1
    return count
    
print (length(liste))


def trieur(lst):
    plage = length(lst)
    i = 0
    
    while i < plage:
        j = 0
        while j < plage - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1

trieur(liste)
print (liste)