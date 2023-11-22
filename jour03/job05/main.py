def calcule(a:int ,b:str ,c:int):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c
    elif b == "%":
        return a % c
    else:
        return "ERREUR"

print( calcule(10,"-",20))