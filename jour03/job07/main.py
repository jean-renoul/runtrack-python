def fonction_langage(langage):
    if langage == "JavaScript":
        return "tu es un développeur web"
    elif langage == "python":
        return "tu es un développeur IA"
    elif langage == "java":
        return "tu es un développeur logiciel"
    elif langage == "reactjs":
        return "tu es un développeur mobile"
    else:
        return 'un jour, je serai le meilleur développeur'
    
print (fonction_langage("python"))