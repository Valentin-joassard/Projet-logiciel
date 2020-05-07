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
#---------------------------#
         #fonctions#
#---------------------------#
def afficherpiece(piece):
    Coin=Label(fenetre,image=coin,bg="grey")
    Coin.place(x=1250, y =100)
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    #print(score)
    Credit.config(text='Piece : ' + str(piece), font=fontStyle)
    Credit.place(x=1300, y =100)

def gagnerpiece():
    global piece,gain
    gain+=1
    if gain==10:
        piece+=1
        gain=0
    #print(piece)
    afficherpiece(piece)


def affichagescore():
    Explosion=Label(fenetre,image=explosion,bg="grey")
    Explosion.place(x=120, y =200)
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    
    #print(score)
    Resultat.config(text='Score : ' + str(score), font=fontStyle)
    Resultat.place(x=160, y =200)


def affichage_meilleur_score(): 
    global meilleur_score
    Coupe=Label(fenetre,image=coupe,bg="grey")
    Coupe.place(x=1200, y =195)
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    
    MeilleurScore.config(text='Meilleur score : ' + str(meilleur_score), font=fontStyle)
    MeilleurScore.place(x=1250, y =200)


ok=0

def affichervie(Nvie1,Nvie2,Nvie3):
    global fin,ok
    
    
    if ok==0:
       
        Nvie1.place(x=170, y =90)
        Nvie2.place(x=220, y =90)
        Nvie3.place(x=270, y =90)
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
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    #print(score)
    #Vie.config(text='Vie : ' + str(fin), font=fontStyle)
    Vie.config(text='Vie : ', font=fontStyle)
    Vie.place(x=100, y =100)


def vitesse_chute():
    
    global vitessechute
    if vitessechute>850:
        vitessechute=vitessechute-70
        #vitessechute=vitessechute-800
    if vitessechute>750 and vitessechute<851:
        vitessechute=vitessechute-50
        #vitessechute=vitessechute-100
    if vitessechute>500 and vitessechute<751:
        vitessechute=vitessechute-20
        #vitessechute=vitessechute-100
    if vitessechute>190 and vitessechute<501:
        vitessechute=vitessechute-1
        #print("chute",vitessechute)
        
def vitesse_apparition():
    global  vitesseapparition
    if vitesseapparition>1500:
        vitesseapparition=vitesseapparition-50
    if vitesseapparition>1000 and vitesseapparition<1501:
        vitesseapparition=vitesseapparition-10
    if vitesseapparition>800 and vitesseapparition<1001:
        vitesseapparition=vitesseapparition-5
    if vitesseapparition>700 and vitesseapparition<801:
        vitesseapparition=vitesseapparition-1
        #print(vitesseapparition)
def create_brick():
    global brick,x1,x2,var3
    proba = randint(0,100)
    #print(proba)
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
    
    #brick = canvas.create_rectangle(x1,100,x2,130,fill="red")
    
    #print("apparition",vitesseapparition)
    BRICK.append([brick,type])
    vitesse_apparition()
    fenetre.after(vitesseapparition,create_brick)
        
def up_vit_tir():
    global x
    x = 2
    #print("Vitesse de tir augmente")
    fenetre.after(10000,restat_up_vit_tir)

def restat_up_vit_tir():
    global x
    x=5
    #print("Vitesse de tir reinitialise")

def up_vit_defil():
    global vitessechute
    vitessechute-=50
    #print("Vitesse de defilement augmente")
    fenetre.after(10000,restat_up_vit_defil)

def restat_up_vit_defil():
    global vitessechute
    vitessechute+=50
    #print("Vitesse de defilement reinitialise")

def nerf_vit_tir():
    global x
    x=10
    #print("Vitesse de tir diminue")
    fenetre.after(10000,restat_nerf_vit_tir)

def restat_nerf_vit_tir():
    global x
    x=5
    #print("Vitesse de tir reinitialise")

def up_vit_dep():
    global gauche, droite
    gauche -=15
    droite +=15
    #print("Vitesse de deplacement augmente")
    fenetre.after(10000,restat_up_vit_dep)

def restat_up_vit_dep():
    global gauche, droite
    gauche+=15
    droite-=15
    #print("Vitesse de deplacement reinitialise")


def deplacement():

    global dx, dy, Var1, Var2,x

    #if (canvas.coords(shot)[1]!=0):
        #print("oui")
    if Var1==0:
        canvas.move(shot,dx,dy)
        destroy_bloc2(shot)
        fenetre.after(x,deplacement)
        #print(canvas.coords(shot))
        Var1 = 1
        Var2 = 0
        if canvas.coords(shot) != []:
            Var1 = 0
            Var2 = 1
        #On deplace la balle :
            if canvas.coords(shot)[1]<50:
                canvas.delete(shot)
                Var1=1
                Var2=0
                #On repete cette fonction

def destroy_bloc(shot):
    global Var1,Var2
    nb = -1
    if canvas.coords(shot)!=[]:
        if(len(BRICK)!=0):
            while(nb<len(BRICK)-1):
                #print(canvas.coords(shot)[1])
                if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb])[3]):
                    if (canvas.coords(shot)[2]>=canvas.coords(BRICK[nb])[0] and canvas.coords(BRICK[nb])[2]>= canvas.coords(shot)[2]):
                    #if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb])[3]):
                        canvas.delete(shot)
                        canvas.delete(BRICK[nb])
                        del BRICK[nb]
                        nb +=1
                        Var1= 0
                        Var2=0
                    elif(canvas.coords(BRICK[nb])[0]<=canvas.coords(shot)[0] and canvas.coords(shot)[0] <= canvas.coords(BRICK[nb])[2]):
                        #if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb])[3]):
                        canvas.delete(shot)
                        canvas.delete(BRICK[nb])
                        del BRICK[nb]
                        nb +=1
                        Var1= 0
                        Var2=0
                    else:
                        nb+=1
                        Var1 =0
                        Var2=0

        #fenetre.after(1,destroy_bloc(shot))

def destroy_bloc2(shot):
    global Var1,Var2,score,x,by
    midShot = (canvas.coords(shot)[0] + canvas.coords(shot)[2])/2
    nb = -1
    #print("mid",midShot)
    #print("x1S",canvas.coords(shot)[0])
    #print("x2S",canvas.coords(shot)[2])
    #print("x1B",canvas.coords(BRICK[nb])[0])
    #print("x2B",canvas.coords(BRICK[nb])[2])
    #if canvas.coords(shot)!=[]:
    bug=0
        
    if(len(BRICK)!=0):
        while(nb<len(BRICK)-1) and bug==0:
            #print("nbr",nb)
            #print("len",(len(BRICK)-1))
            bug=1
            if canvas.coords(shot)!=[] :
                bug=0
                #print(canvas.coords(shot)[1])
                #print("shot",canvas.coords(shot))
                #print("Brick",canvas.coords(BRICK))
                if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb][0])[3] and canvas.coords(BRICK[nb][0])[0]-20<=midShot and midShot<=canvas.coords(BRICK[nb][0])[2]+20):
                          
                    #if (canvas.coords(BRICK[nb])[0]<=midShot and midShot<=canvas.coords(BRICK[nb])[2]):
                    canvas.delete(shot)
                    canvas.delete(BRICK[nb][0])
                    if(BRICK[nb][1]==1):
                        #print("type 1")
                        nerf_vit_tir()
                    if(BRICK[nb][1]==2):
                        #print("type 2")
                        up_vit_dep()
                    if(BRICK[nb][1]==3):
                        #print("type 3")
                        up_vit_defil()
                    del BRICK[nb]
                    nb +=1
                    Var1= 0
                    Var2=0
                    score=score+1
                    affichagescore()
                    gagnerpiece()
                    #print("score :", score)
                else:
                    nb+=1
                    Var1 =0
                    Var2=0




def descente():
    global bx,by,fin
    nb = -1

    while(nb<len(BRICK)-1):
        #print(canvas.coords(BRICK[nb])[1])
        if (canvas.coords(BRICK[nb][0])[1]==500):
            #print(canvas.coords(BRICK[nb])[1])
            canvas.delete(BRICK[nb][0])
            del BRICK[nb]
            nb+=1
            fin-=1
            affichervie(Nvie1,Nvie2,Nvie3)
            lose(fin)
        else:
            canvas.move(BRICK[nb][0],bx,by)
            nb +=1
    
    #canvas.move(BRICK[nb],x,y)
    
    #print("chute",vitessechute)
    vitesse_chute()
    fenetre.after(vitessechute,descente)
    #print(BRICK)

def supprimer_bloc(BLOC,num_list_del):
    del BLOC[num_list_del]
    return BLOC

def lose(fin):
    global meilleur_score, score
    #print("une vie en moins ! vie restante: ", fin)
    if fin == 0:
        #print("perdu")
        if meilleur_score < score :
            meilleur_score = score
        enregistrer()
        raise SystemExit



def Descendre_Bloc(BLOC):
    nbr_list_max=len(BLOC)
    nbr_list = 0
	
    while nbr_list!=nbr_list_max:
	    BLOC [nbr_list][1]=BLOC [nbr_list][1] -1
	    nbr_list= nbr_list + 1
    return BLOC

def creer_bloc():
    proba = randint(0,100)
    #print(proba)
    if (proba >=0 and proba<=70):
        type = 0
        valeur = 1
    if (proba >70 and proba<=80):
        type = 1
        valeur = 1
    if (proba >80 and proba<=90):
        type = 2
        valeur = 1
    if (proba >90 and proba<=100):
        type = 3
        valeur = 1
    #print(type)
    #print(valeur)
    return type and valeur

def clavier(event):
    global coords, shot, Var1, Var2, gauche, droite
    move = event.keysym
    if move == "Right" and coords[0]<700 :
        #print(droite)
        coords = (coords[0] + droite, coords[1])
        canvas.move(player, droite, 0)
        #print(coords)
    elif move == "Left" and coords[0]>80:
        #print(gauche)
        coords = (coords[0] + gauche, coords[1])
        canvas.move(player, gauche, 0)
        #print(coords)
    elif move == "Up":

        Var1=0
        
        #t=PhotoImage(file="image/carre.png")
        
        #shot = canvas.create_image(coords[0],coords[1]-25,image=t)
        if Var2==0:
            shot = canvas.create_oval(coords[0]-15,coords[1]+45,coords[0]+15,coords[1]+10,fill='red')
            Var2=1
            deplacement()
            xTir = coords[0]
            yTir = coords[1]
            TIR.append([xTir,yTir])
        #TIR.append(yTir)
        #print(TIR)
    #elif move =="Down":
     #   canvas.coords(shot,coords[0],coords[1]-25)
    #while(yTir!=0):
    #    canvas.coords(shot,coords[0],coords[1]-25)
    #    yTir = coords[1]-25            
         
    #print(coords)
        canvas.coords(p, coords[0], coords[1], coords[0]+25, coords[1]+25)
        
        fenetre.update()


#---------------------------#
       #Code principal#
#---------------------------#
fenetre = Tk() 
charger()
TIR =[]
BRICK= []
# création du canvas
images=PhotoImage(file='image/espace5.png')
fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)

#fenetre.configure()
canvas =Canvas(fenetre, width=768, height=576, bg="ivory")
# coordonnées initiales
coords = (390,520)
MeilleurScore = Label(fenetre, fg ='#FFD700',bg='grey')
Vie = Label(fenetre, fg ='red',bg='grey')
Resultat = Label(fenetre, fg ='red',bg='grey')
Credit=Label(fenetre, fg= "#FFD700",bg='grey')
coin=PhotoImage(file='image/coin.png')
coupe=PhotoImage(file='image/coupe.png')
explosion=PhotoImage(file='image/explosion.png')
p=PhotoImage(file='image/rocket.png')
image=PhotoImage(file='image/espace5.png')

Nvie1=Label(fenetre,image=p,bg="grey")
Nvie2=Label(fenetre,image=p,bg="grey")
Nvie3=Label(fenetre,image=p,bg="grey")


affichervie(Nvie1,Nvie2,Nvie3)
affichagescore()
afficherpiece(piece)
affichage_meilleur_score()
# création du rectangle
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
player =  canvas.create_image(390,520,image=p)

#shot = canvas.create_oval(20,20,40,40,fill='red')
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()
create_brick()
descente()
#destroy_bloc()
champ_label = Label(fenetre, text="Brick shooter")
champ_label.pack()
bouton_quitter=Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="bottom")
bouton_accueil=Button(fenetre,text="Accueil")
bouton_accueil.pack(side="bottom")
bouton_accueil.configure( width=15, height=3,  )
bouton_quitter.configure( width=15, height=3,  )
cadre = Frame(fenetre)
cadre.pack(side="bottom", fill=BOTH)

fenetre.attributes('-fullscreen', True)

fenetre.mainloop()

enregistrer()

