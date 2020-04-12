import os
import pickle
os.chdir("c:/Users/Maxence CROSSE/Desktop/ProjetLogiciel/Projet-logiciel/Projet-logiciel/fonction_test")
with open('fichier.txt', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    
x= 10
y = 15
def enregistrement(x,y):
    stats = {
        x,
        y,
    }
    with open('fichier.txt', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(stats)

enregistrement(x,y)
