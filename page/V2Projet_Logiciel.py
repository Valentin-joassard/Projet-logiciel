from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont

#---------------------------#
      #Variable Globale#
#---------------------------#
  

bx=0
by=5
dx = 0
dy = -5
x=5
Var1=0
Var2=0
var3=0
fin=3
score=0
vitessechute=1000
vitesseapparition=2000
gauche = -25
droite = 25
piece=0
gain=0
meilleur_score = 0
anticheat=0
anticheat1=0
anticheat2=0

#-------------------------------#
    #Enregistrement/chargement#
#-------------------------------#

def enregistrer():
    global meilleur_score, piece
    var = str(meilleur_score)
    var1 = str(piece)
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write(var)
    mon_fichier.write("\n")
    mon_fichier.write(var1)
    mon_fichier.close()

def charger():
    global meilleur_score, piece
    with open("fichier.txt", "r") as fichier:
        meilleur_score, piece = [int(elt) for elt in fichier.readlines()]

#-------------------------#
      # Affichage #
#-------------------------#

def afficherpiece(piece):
    Coin=Label(fenetre,image=coin,bg="#404040")
    Coin.place(x=1250, y =100)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    Credit.config(text='Pieces : ' + str(piece), font=fontStyle)
    Credit.place(x=1300, y =100)

def gagnerpiece():
    global piece,gain
    gain+=1
    if gain==10:
        piece+=1
        gain=0
    afficherpiece(piece)


def affichagescore():
    Explosion=Label(fenetre,image=explosion,bg="#404040")
    Explosion.place(x=120, y =200)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    Resultat.config(text='  Score : ' + str(score), font=fontStyle)
    Resultat.place(x=150, y =200)


def affichage_meilleur_score(): 
    global meilleur_score
    Coupe=Label(fenetre,image=coupe,bg="#404040")
    Coupe.place(x=1200, y =195)
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    
    MeilleurScore.config(text='Meilleur score : ' + str(meilleur_score), font=fontStyle)
    MeilleurScore.place(x=1250, y =200)


ok=0

def affichervie(Nvie1,Nvie2,Nvie3):
    global fin,ok
    
    
    if ok==0:
       
        Nvie1.place(x=165, y =100)
        Nvie2.place(x=225, y =100)
        Nvie3.place(x=285, y =100)
        ok=ok+1
    if fin==2 and ok==1:
        Nvie3.place_forget()
        ok=ok+1
    if fin==1 and ok==2:
        Nvie2.place_forget()
        ok=ok+1
    if fin==0 and ok==3:
        Nvie1.place_forget()
        ok=ok+1
    fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
    Vie.config(text=' Vie : ', font=fontStyle)
    Vie.place(x=100, y =100)


#---------------------------------------------#
      #Création et déplacement des bricks#
#---------------------------------------------#

#Accélère la vitesse de chute des blocs en fonctions du temps
def vitesse_chute():
    global vitessechute
    if vitessechute>850:
        vitessechute=vitessechute-70
    if vitessechute>750 and vitessechute<851:
        vitessechute=vitessechute-50
    if vitessechute>500 and vitessechute<751:
        vitessechute=vitessechute-20
    if vitessechute>80 and vitessechute<501:
        vitessechute=vitessechute-1

#Accélère la vitesse d'apparition des blocs en fonctions du temps
def vitesse_apparition():
    global  vitesseapparition
    if vitesseapparition>1500:
        vitesseapparition=vitesseapparition-50
    if vitesseapparition>1000 and vitesseapparition<1501:
        vitesseapparition=vitesseapparition-10
    if vitesseapparition>800 and vitesseapparition<1001:
        vitesseapparition=vitesseapparition-5
    if vitesseapparition>750 and vitesseapparition<801:
        vitesseapparition=vitesseapparition-1

#Défini un type de bloc et l'affiche
def create_brick():
    global brick,x1,x2,var3
    proba = randint(0,100)
    x1 = randint(80,700)
    x2 = x1 + 30
    if (proba >=0 and proba<=70):
        type = 0
        brick = canvas.create_rectangle(x1,100,x2,130,fill="red")
    if (proba >70 and proba<=80):
        type = 1
        brick = canvas.create_rectangle(x1,100,x2,130,fill="blue")
    if (proba >80 and proba<=90):
        type = 2
        brick = canvas.create_rectangle(x1,100,x2,130,fill="green")
    if (proba >90 and proba<=100):
        type = 3
        brick = canvas.create_rectangle(x1,100,x2,130,fill="yellow")
    
    BRICK.append([brick,type])
    vitesse_apparition()
    fenetre.after(vitesseapparition,create_brick)

#Déplacement du tir vers le haut
def deplacement():
    global dx, dy, Var1, Var2,x
    if Var1==0:
        canvas.move(shot,dx,dy)
        destroy_bloc(shot)
        fenetre.after(x,deplacement)
        Var1 = 1
        Var2 = 0
        if canvas.coords(shot) != []:
            Var1 = 0
            Var2 = 1
            if canvas.coords(shot)[1]<50:
                canvas.delete(shot)
                Var1=1
                Var2=0

#Déplacement des blocs vers le bas
def descente():
    global bx,by,fin
    if fin!=0:
        nb = -1

        while(nb<len(BRICK)-1):
            if (canvas.coords(BRICK[nb][0])[1]==500):
                canvas.delete(BRICK[nb][0])
                del BRICK[nb]
                nb+=1
                if fin>0:
                    fin-=1
                affichervie(Nvie1,Nvie2,Nvie3)
                lose(fin)
            else:
                canvas.move(BRICK[nb][0],bx,by)
                nb +=1
        vitesse_chute()
        fenetre.after(vitessechute,descente)

#--------------------------------#
    # Destruction des bricks #
#--------------------------------#

#Destruction des blocs s'ils touchent un tir

def destroy_bloc(shot):
    global Var1,Var2,score,x,by
    midShot = (canvas.coords(shot)[0] + canvas.coords(shot)[2])/2
    nb = -1
    bug=0     
    if(len(BRICK)!=0):
        while(nb<len(BRICK)-1) and bug==0:
            bug=1
            if canvas.coords(shot)!=[] :
                bug=0 
                if( canvas.coords(shot)[1]<=canvas.coords(BRICK[nb][0])[3] and canvas.coords(shot)[1]>=canvas.coords(BRICK[nb][0])[1] and canvas.coords(BRICK[nb][0])[0]-20<=midShot and midShot<=canvas.coords(BRICK[nb][0])[2]+20):
                    canvas.delete(shot)
                    canvas.delete(BRICK[nb][0])
                    if(BRICK[nb][1]==1):
                        nerf_vit_tir()
                    if(BRICK[nb][1]==2):
                        up_vit_dep()
                    if(BRICK[nb][1]==3):
                        up_vit_defil()
                    del BRICK[nb]
                    nb +=1
                    Var1= 0
                    Var2=0
                    score=score+1
                    affichagescore()
                    gagnerpiece()
                else:
                    nb+=1
                    Var1 =0
                    Var2=0

#---------------------------#
      # Bonus - Malus #
#---------------------------#

def up_vit_tir():
    global x
    x = 2
    fenetre.after(10000,restat_up_vit_tir)

def restat_up_vit_tir():
    global x
    x=5

def up_vit_defil():
    global vitessechute,anticheat1
    Up_chute1.place(x=200,y=303)
    if anticheat1==1:
        Up_chute2.place(x=250,y=303)

    if anticheat1<2:
        anticheat1+=1
        vitessechute-=20        
        fenetre.after(10000,restat_up_vit_defil)

def restat_up_vit_defil():
    global anticheat1,vitessechute
    anticheat1-=1
    vitessechute+=20
    if anticheat1==1:
        Up_chute2.place_forget()
    if anticheat1==0:
        Up_chute1.place_forget()
    
def nerf_vit_tir():
    global x,anticheat2
    
    Down.place(x=200,y=463)
    if anticheat2==1:
        Down3.place(x=250,y=463)

    if anticheat2<2:
        anticheat2+=1
        x+=5
        fenetre.after(10000,restat_nerf_vit_tir)

def restat_nerf_vit_tir():
    global x,anticheat2
    anticheat2-=1
    x-=5
    if anticheat2==1:
        Down3.place_forget()
    if anticheat2==0:
         Down.place_forget()

def up_vit_dep():
    global gauche, droite,anticheat
    Up_vit1.place(x=200,y=383)
    if anticheat==1:
        Up_vit2.place(x=250,y=383)
    if anticheat<2:        
        anticheat+=1
        gauche -=15
        droite +=15
        fenetre.after(10000,restat_up_vit_dep)

def restat_up_vit_dep():
    global gauche, droite,anticheat
    anticheat-=1
    gauche+=15
    droite-=15
    if anticheat==1:
        Up_vit2.place_forget()
    if anticheat==0:
        Up_vit1.place_forget()

#---------------------------#
        # Défaite #
#---------------------------#

def lose(fin):
    global meilleur_score, score
    if fin == 0:
        fontStyle = tkFont.Font(family="Arial Black", size=50)
        Fin = Label(fenetre, fg ='red',bg='#074e6c')
        Fin.config(text='      GAME OVER      \nTon score: ' + str(score)+" ", font=fontStyle)
        Fin.place(x=410, y =150)
        if meilleur_score < score :
            Champion = Label(fenetre, fg ='red',bg='#074e6c')
            Champion.config(text='     NEW RECORD     ', font=fontStyle)
            Champion.place(x=405, y =400)
            meilleur_score = score
        enregistrer()

#-------------------------------#
     # Déplacement du joueur #
#-------------------------------#

#Fonction pour aller à gauche, droite ou tirer
def clavier(event):
    global coords, shot, Var1, Var2, gauche, droite
    move = event.keysym
    if move == "Right" and coords[0]<700 :
        coords = (coords[0] + droite, coords[1])
        canvas.move(player, droite, 0)
    elif move == "Left" and coords[0]>80:
        coords = (coords[0] + gauche, coords[1])
        canvas.move(player, gauche, 0)
    elif move == "Up":
        Var1=0
        if Var2==0:
            shot = canvas.create_oval(coords[0]-15,coords[1]+45,coords[0]+15,coords[1]+10,fill='red')
            Var2=1
            deplacement()
        fenetre.update()
    
#---------------------------#
       #Code principal#
#---------------------------#

fenetre = Tk() 
charger()
BRICK= []

#---------------------------#
         #Images#
#---------------------------#

coin=PhotoImage(file='image/coin.png')
coupe=PhotoImage(file='image/coupe.png')
explosion=PhotoImage(file='image/epee.png')
p=PhotoImage(file='image/rocket1.png')
f=PhotoImage(file='image/coeur.png')
image=PhotoImage(file='image/espace5.png')
titre=PhotoImage(file='image/titre.png')
images=PhotoImage(file='image/espace5.png')
down=PhotoImage(file='image/down.png')
up=PhotoImage(file='image/up.png')
bg=PhotoImage(file='image/espace3.png')

#---------------------------#
      #Affichage-label#
#---------------------------#

fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)
fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)
MeilleurScore = Label(fenetre, fg ='#FFD700',bg="#404040")
Vie = Label(fenetre, fg ='#0c136d',bg='#404040')
Resultat = Label(fenetre, fg ='#0c136d',bg='#404040')
Credit=Label(fenetre, fg= "#FFD700",bg='#404040')
Titre=Label(fenetre,image=titre,bg="black")
Nvie1=Label(fenetre,image=f,bg="#404040")
Nvie2=Label(fenetre,image=f,bg="#404040")
Nvie3=Label(fenetre,image=f,bg="#404040")
Up_chute1=Label(fenetre,image=up,bg="black")
Up_chute2=Label(fenetre,image=up,bg="black")
Up_vit1=Label(fenetre,image=up,bg="black")
Up_vit2=Label(fenetre,image=up,bg="black")
Down=Label(fenetre,image=down,bg="black")
Down3=Label(fenetre,image=down,bg="black")
Down2=Label(fenetre,fg='#0c136d',bg="#404040")
Down2.config(text="       tir       ", font=fontStyle)
Down2.place(x=50,y=460)
Up2=Label(fenetre,fg='#0c136d',bg="#404040")
Up2.config(text="   vitesse   ", font=fontStyle)
Up2.place(x=50,y=380)
Up3=Label(fenetre,fg='#0c136d',bg="#404040")
Up3.config(text="    chute    ", font=fontStyle)
Up3.place(x=50,y=300)
Titre.place(x=400, y =620)

affichervie(Nvie1,Nvie2,Nvie3)
affichagescore()
afficherpiece(piece)
affichage_meilleur_score()

#--------------------------------#
    #Création du cadre jouable#
#--------------------------------#

canvas =Canvas(fenetre, width=768, height=576, bg="ivory")
coords = (390,520)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

#---------------------------#
    #Fond d'écran - Skin#
#---------------------------#

background= canvas.create_image(370,250,image=bg)
player =  canvas.create_image(390,520,image=p)

#---------------------------#
    #Lancement du jeu#
#---------------------------#

create_brick()
descente()

#---------------------------#
          #Boutons#
#---------------------------#

bouton_quitter=Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="bottom")
bouton_accueil=Button(fenetre,text="Accueil")
bouton_accueil.pack(side="bottom")
bouton_accueil.configure( width=15, height=3,  )
bouton_quitter.configure( width=15, height=3,  )
cadre = Frame(fenetre)
cadre.pack(side="bottom", fill=BOTH)

#---------------------------#

fenetre.attributes('-fullscreen', True)
fenetre.mainloop()
enregistrer()