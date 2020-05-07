import os
import pickle
os.chdir("c:/Users/Maxence CROSSE/Desktop/ProjetLogiciel/Projet-logiciel/Projet-logiciel/fonction_test")
score = {
  "joueur 1":    5,
  "joueur 2":   35,
  "joueur 3":   20,
  "joueur 4":    2,
    }
with open('fichier.txt', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open('fichier.txt', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)



