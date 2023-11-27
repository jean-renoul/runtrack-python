liste_note = []
def skywalker(liste_note):
    for note in liste_note:
        note_arrondie = 0
        if note < 40:
            print ("Test échoué : ", note, "/100")
        elif note >= 40:
            if (note + 1) % 5 == 0:
                note_arrondie = note +1
            elif (note + 2) % 5 == 0:
                note_arrondie = note + 2
                print ("Test réussi : ", note_arrondie, "/100")
            else:
                print ("Test réussi : ", note, "/100")

skywalker([50, 37, 42, 43, 92, 93])