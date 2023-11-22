def fruits_saison(type:str ,saison:str):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        return "poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine, navet"
    
print (fruits_saison("fruits","hiver"))
print (fruits_saison("fruits","ete"))
print (fruits_saison("legume","hiver"))
print (fruits_saison("legume","ete"))