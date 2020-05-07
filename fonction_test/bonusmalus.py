def enregistrer(score,piece):
    global score, piece
    var = str(score)
    var1 = str(piece)
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write(var)
    mon_fichier.write("\n")
    mon_fichier.write(var1)
    mon_fichier.close()

def charger():
    global score, piece
    with open("fichier.txt", "r") as fichier:
        score, piece = [int(elt) for elt in fichier.readlines()]



