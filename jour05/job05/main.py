import string
string.ascii_lowercase


def chiffrage(mot, decalage):
    mot_code = ""
    for i in mot:
        i = ord(i)
        if 96 < i:
            i += decalage
            if i > 122:
                i -= 26
        mot_code += chr(i)
    print (mot_code)

chiffrage("je m'appelle jean", 3)