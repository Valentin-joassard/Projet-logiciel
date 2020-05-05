from tkinter import *
from tkinter import Tk ,Canvas
from random import randint

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

#---------------------------------------------#
      #Création et déplacement des bricks#
#---------------------------------------------#

#accelere la vitesse de chute des blocs en fonctions du temps
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

#accelere la vitesse d'apparition des blocs en fonctions du temps
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

#definis un type de bloc et l'affiche
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

#depalcement du tir vers le haut
def deplacement():
    global dx, dy, Var1, Var2,x
    if Var1==0:
        canvas.move(shot,dx,dy)
        destroy_bloc2(shot)
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

#deplacement des blocs vers le bas
def descente():
    global bx,by,fin
    nb = -1

    while(nb<len(BRICK)-1):
        if (canvas.coords(BRICK[nb][0])[1]==500):
            canvas.delete(BRICK[nb][0])
            del BRICK[nb]
            nb+=1
            fin-=1
            lose(fin)
        else:
            canvas.move(BRICK[nb][0],bx,by)
            nb +=1
    
    vitesse_chute()
    fenetre.after(vitessechute,descente)

#--------------------------------#
    # Destruction des bricks #
#--------------------------------#

#destruction des blocs si ils touchent un tir
def destroy_bloc2(shot):
    global Var1,Var2,score,x,by
    midShot = (canvas.coords(shot)[0] + canvas.coords(shot)[2])/2
    nb = -1
    bug=0
        
    if(len(BRICK)!=0):
        while(nb<len(BRICK)-1) and bug==0:
            bug=1
            if canvas.coords(shot)!=[] :
                bug=0
                if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb][0])[3] and canvas.coords(BRICK[nb][0])[0]-20<=midShot and midShot<=canvas.coords(BRICK[nb][0])[2]+20):
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
                else:
                    nb+=1
                    Var1 =0
                    Var2=0

#---------------------------#
        # Défaite #
#---------------------------#

# ferme la page lorsque le joueur à perdu ( en attente d'une page game over)
 def lose(fin):
    print("une vie en moins ! vie restante: ", fin)
    if fin == 0:
        print("perdu")
        raise SystemExit

#---------------------------#
      # Bonus - Malus #
#---------------------------#

#augmente la vitesse de tir pendant un certain temps
def up_vit_tir():
    global x
    x = 3
    fenetre.after(2000,restat_up_vit_tir)

#remet la vitesse de tir à la normale
def restat_up_vit_tir():
    global x
    x+=2

#augmente la vitesse de defilement pendant un certain temps
def up_vit_defil():
    global vitessechute
    vitessechute+=20
    fenetre.after(2000,restat_up_vit_defil)

#remet la vitesse de defilement à la normale
def restat_up_vit_defil():
    global vitessechute
    vitessechute-=20

#diminue la vitesse de tir pendant un certain temps
def nerf_vit_tir():
    global x
    x=7
    fenetre.after(2000,restat_nerf_vit_tir)

#remet la vitesse de tir à la normale
def restat_nerf_vit_tir():
    global x
    x-=2

#augmente la vitesse de deplacment pendant un certain temps
def up_vit_dep():
    global gauche, droite
    gauche -=25
    droite +=25
    fenetre.after(2000,restat_up_vit_dep)

#remet la vitesse de deplacement à la normale
def restat_up_vit_dep():
    global gauche, droite
    gauche+=25
    droite-=25

#-------------------------------#
     # Déplacement du joueur #
#-------------------------------#

#fonction pour aller à gauche, droite ou tirer
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

#creation de la fenetre

fenetre = Tk()
BRICK= []
# création du canvas
canvas = Canvas(fenetre, width=768, height=576, bg="ivory")
# coordonnées initiales
coords = (390,520)
# création du rectangle
bg=PhotoImage(file='image/espace1.png')
background= canvas.create_image(370,250,image=bg)
p=PhotoImage(file='image/rocket.png')
player =  canvas.create_image(390,520,image=p)
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()
create_brick()
descente()
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