from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont
from winsound import *
import subprocess

meilleur_score = 0
piece=0
type_image=1
Unlock1=0
Unlock2=0
one=0
n=-1
Bonus=0

def menus():
    fenetre.destroy()
    subprocess.run('python page-accueil.py')

def Quitter():
    command=fenetre.quit()

def Play():
    fenetre.destroy()
    subprocess.run('python test4.py')

def son(n):
    global piece,Unlock1,type_image,Unlock2,Bonus
    musique_bouton = PlaySound("son/souris_bouton.wav", SND_ASYNC)
    if n==6:
        fenetre.after(1000,Play())
    if n==0:
        fenetre.after(1000,Quitter())
    if n==1:
        fenetre.after(1000,menus())
    if n==2:
        if piece>=100:
            if Unlock1==0:
                Unlock1=1
                piece=piece-100
                afficherpiece(piece)
                choisir_image(Unlock1,Unlock2,Bonus)
        if Unlock1==1:
            type_image=2 
    if n==3:
        if piece>=500:
            if Unlock2==0:
                Unlock2=1
                piece=piece-500
                afficherpiece(piece)
                choisir_image(Unlock1,Unlock2,Bonus)
        if Unlock2==1:
            type_image=3 
    if n==4:
        type_image=1
    if n==5 and Bonus<3 and piece>=250:
        piece=piece-250
        Bonus=Bonus+1
        afficherpiece(piece)
        choisir_image(Unlock1,Unlock2,Bonus)

    enregistrer()

def choisir_image(Unlock1,Unlock2,Bonus):
    global p1,p2,p3,Bonus1,Bonus2,Bonus3
    #200 pixel
    Image1=Label(fenetre,image=p1,bg="#404040")
    Image1.place(x=660, y =50)
    Image3=Label(fenetre,image=p3,bg="#404040")
    Image3.place(x=905, y =50)
    Image2=Label(fenetre,image=p2,bg="#404040")
    Image2.place(x=415, y =50)
    FontBouton= tkFont.Font(family="Arial Black",size=15)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    
    bouton_image1=Button(fenetre,text="Choisir",bg='#404040',fg='grey',command=lambda n=4: son(n))
    bouton_image1.configure( width=10, height=2,font=FontBouton )
    bouton_image1.place(x=685, y =280)

    Up=Label(fenetre,fg='#0c136d',bg="#404040")
    Up.config(text="   vitesse de tir   ", font=fontStyle)
    Up.place(x=655,y=390)
    bouton_up=Button(fenetre,text="Augmenter",bg='#404040',fg='grey',command=lambda n=5: son(n))
    bouton_up.configure( width=10, height=2,font=FontBouton )
    bouton_up.place(x=685, y =480)

    if Unlock1==1:
        bouton_image1=Button(fenetre,text="Choisir",bg='#404040',fg='grey',command=lambda n=2: son(n))
        bouton_image1.configure( width=10, height=2,font=FontBouton )
        bouton_image1.place(x=930, y =280)

    if Unlock1==0:
        bouton_image1=Button(fenetre,text="Acheter",bg='#404040',fg='grey',command=lambda n=2: son(n))
        bouton_image1.configure( width=10, height=2,font=FontBouton )
        bouton_image1.place(x=930, y =280)

    if Unlock2==1:
        bouton_image2=Button(fenetre,text="Choisir",bg='#404040',fg='grey',command=lambda n=3: son(n))
        bouton_image2.configure( width=10, height=2,font=FontBouton )
        bouton_image2.place(x=440, y =280)

    if Unlock2==0:
        bouton_image2=Button(fenetre,text="Acheter",bg='#404040',fg='grey',command=lambda n=3: son(n))
        bouton_image2.configure( width=10, height=2,font=FontBouton )
        bouton_image2.place(x=440, y =280)
    if Bonus>=1:
        bonus1=Label(fenetre,image=Bonus1,bg="#404040")
        bonus1.place(x=855, y =520)
    if Bonus>=2:
        bonus2=Label(fenetre,image=Bonus2,bg="#404040")
        bonus2.place(x=910, y =502)
    if Bonus==3:
        bouton_up=Button(fenetre,text="Max",bg='#404040',fg='grey',command=lambda n=5: son(n))
        bouton_up.configure( width=10, height=2,font=FontBouton )
        bouton_up.place(x=685, y =480)
        bonus3=Label(fenetre,image=Bonus3,bg="#404040")
        bonus3.place(x=980, y =489)

def afficherpiece(piece):
    Coin=Label(fenetre,image=coin,bg="#404040")
    Coin.place(x=1250, y =100)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    #print(score)
    Credit.config(text='Pieces : ' + str(piece), font=fontStyle)
    Credit.place(x=1300, y =100)

def affichage_meilleur_score(): 
    global meilleur_score
    Coupe=Label(fenetre,image=coupe,bg="#404040")
    Coupe.place(x=1200, y =195)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    
    MeilleurScore.config(text='Meilleur score : ' + str(meilleur_score), font=fontStyle)
    MeilleurScore.place(x=1250, y =200)

def enregistrer():
    global meilleur_score, piece,type_image,Unlock1,Unlock2
    var = str(meilleur_score)
    var1 = str(piece)
    var2= str(type_image)
    var3=str(Unlock1)
    var4=str(Unlock2)
    var5=str(Bonus)
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write(var)
    mon_fichier.write("\n")
    mon_fichier.write(var1)
    mon_fichier.write("\n")
    mon_fichier.write(var2)
    mon_fichier.write("\n")
    mon_fichier.write(var3)
    mon_fichier.write("\n")
    mon_fichier.write(var4)
    mon_fichier.write("\n")
    mon_fichier.write(var5)
    mon_fichier.close()

def charger():
    global meilleur_score, piece,type_image,Unlock1,Unlock2,Bonus
    with open("fichier.txt", "r") as fichier:
        meilleur_score, piece,type_image,Unlock1,Unlock2,Bonus = [int(elt) for elt in fichier.readlines()]
        
fenetre = Tk() 

charger()

TIR =[]
BRICK= []

coin=PhotoImage(file='image/coin.png')
coupe=PhotoImage(file='image/coupe.png')

titre=PhotoImage(file='image/titre.png')
images=PhotoImage(file='image/espace5.png')
fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)

#fenetre.configure()
canvas =Canvas(fenetre, width=768, height=576, bg="ivory")
# coordonnées initiales

fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)

Prix1=Label(fenetre,fg='#FFD700',bg="#404040")
Prix1.config(text="   Prix 250   ", font=fontStyle)
Prix1.place(x=680,y=425)

Prix2=Label(fenetre,fg='#FFD700',bg="#404040")
Prix2.config(text="   Prix 500  ", font=fontStyle)
Prix2.place(x=445,y=10)

Prix3=Label(fenetre,fg='#FFD700',bg="#404040")
Prix3.config(text="   Prix 100   ", font=fontStyle)
Prix3.place(x=930,y=10)



MeilleurScore = Label(fenetre, fg ='#FFD700',bg="#404040")
Credit=Label(fenetre, fg= "#FFD700",bg='#404040')
Titre=Label(fenetre,image=titre,bg="black")
Titre.place(x=400, y =620)
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
canvas.pack()
fenetre.attributes('-fullscreen', True)
p1=PhotoImage(file='image/rocket1.png')
p2=PhotoImage(file='image/rocket.png')
affichage_meilleur_score()
afficherpiece(piece)

p3=PhotoImage(file='image/Drocket1.png')
p1=PhotoImage(file='image/Drocket.png')
p2=PhotoImage(file='image/Drocket2.png')
Bonus1=PhotoImage(file='image/Bonus1.png')
Bonus2=PhotoImage(file='image/Bonus2.png')
Bonus3=PhotoImage(file='image/Bonus3.png')

choisir_image(Unlock1,Unlock2,Bonus)
bouton_play=Button(fenetre, text="Play",bg='#404040',fg='#0c136d', command=lambda n=6: son(n))
bouton_quitter=Button(fenetre, text="Quitter",bg='#404040',fg='grey', command=lambda n=0: son(n))
bouton_accueil=Button(fenetre,text="Accueil",bg='#404040',fg='grey',command=lambda n=1: son(n))
FontBouton= tkFont.Font(family="Arial Black",size=15)
bouton_play.configure( width=20, height=2,font=FontBouton )
bouton_accueil.configure( width=20, height=2,font=FontBouton )
bouton_quitter.configure( width=20, height=2,font=FontBouton )
bouton_quitter.place(x=930, y =750)
bouton_accueil.place(x=330, y =750)
bouton_play.place(x=630, y =750)


fenetre.mainloop()
enregistrer()