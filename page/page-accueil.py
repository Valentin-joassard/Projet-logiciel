from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont
from winsound import *
import subprocess

#---------------------------#
      #Variable Globale#
#---------------------------#

meilleur_score = 0
piece=0
type_image=1
Unlock1=0
Unlock2=0
BonusTir=0
BonusDescente=0
BonusDeplacement=0

#---------------------------#
        #Affichage#
#---------------------------#

def afficherpiece(piece):
    Coin=Label(fenetre,image=coin,bg="#404040")
    Coin.place(x=1250, y =100)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    Credit.config(text='Pieces : ' + str(piece), font=fontStyle)
    Credit.place(x=1300, y =100)

def affichage_meilleur_score(): 
    global meilleur_score
    Coupe=Label(fenetre,image=coupe,bg="#404040")
    Coupe.place(x=1200, y =195)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    
    MeilleurScore.config(text='Meilleur score : ' + str(meilleur_score), font=fontStyle)
    MeilleurScore.place(x=1250, y =200)


def charger():
    global meilleur_score, piece,type_image,Unlock1,Unlock2,BonusTir,BonusDescente,BonusDeplacement
    with open("fichier.txt", "r") as fichier:
        meilleur_score, piece,type_image,Unlock1,Unlock2,BonusTir,BonusDescente,BonusDeplacement = [int(elt) for elt in fichier.readlines()]

#---------------------------#
    #Changement de pages#
#---------------------------#

def Quitter():
    command=fenetre.quit()


def perso():    
    fenetre.destroy()
    subprocess.run('python page/page-perso.py')


def play(): 
    fenetre.destroy()
    subprocess.run('python page/page-jouer.py')


def tuto(): 
    fenetre.destroy()
    subprocess.run('python page/page-tuto.py')


#---------------------------#
        #Son bouton#
#---------------------------#

def son(n):
    musique_bouton = PlaySound("son/souris_bouton.wav", SND_ASYNC)
    if n==0:
        fenetre.after(1000,Quitter())
    if n==1:
        fenetre.after(1000,play())
    if n==2:
        fenetre.after(1000,tuto())
    if n==3:
        fenetre.after(1000,perso())        
fenetre = Tk() 
charger()

#---------------------------#
      #Création images#
#---------------------------#

coin=PhotoImage(file='image/coin.png')
coupe=PhotoImage(file='image/coupe.png')

titre=PhotoImage(file='image/titre.png')
images=PhotoImage(file='image/espace5.png')
fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)

canvas =Canvas(fenetre, width=768, height=576, bg="ivory")

fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
MeilleurScore = Label(fenetre, fg ='#FFD700',bg="#404040")
Credit=Label(fenetre, fg= "#FFD700",bg='#404040')
Titre=Label(fenetre,image=titre,bg="black")
Titre.place(x=400, y =620)
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
canvas.pack()
fenetre.attributes('-fullscreen', True)

#---------------------------#
      #Création bouton#
#---------------------------#

bouton_quitter=Button(fenetre, text="Quitter",bg='#404040',fg='#0c136d', command=lambda n=0: son(n))
bouton_play=Button(fenetre, text="Jouer",bg='#404040',fg='#0c136d', command=lambda n=1: son(n))
bouton_tuto=Button(fenetre, text="Tuto",bg='#404040',fg='#0c136d', command=lambda n=2: son(n))
bouton_perso=Button(fenetre, text="Perso",bg='#404040',fg='#0c136d', command=lambda n=3: son(n))
FontBouton= tkFont.Font(family="Arial Black",size=15)

bouton_quitter.configure( width=20, height=2,font=FontBouton )
bouton_play.configure( width=20, height=2,font=FontBouton )
bouton_tuto.configure( width=20, height=2,font=FontBouton )
bouton_perso.configure( width=20, height=2,font=FontBouton )

bouton_quitter.place(x=625, y =460)
bouton_play.place(x=625, y =40)
bouton_tuto.place(x=625, y =180)
bouton_perso.place(x=625, y =320)


charger()
affichage_meilleur_score()
afficherpiece(piece)
musique_menu = PlaySound("son/accueil.wav", SND_ASYNC)
fenetre.mainloop()
