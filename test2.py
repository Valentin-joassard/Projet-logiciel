from tkinter import *
from tkinter import Tk ,Canvas
from random import randint

#---------------------------#
      #Variable Globale#
#---------------------------#

x=0
y=5
dx = 0
dy = -5
Var1=0
Var2=0
var3=0
fin=0

#---------------------------#
         #fonctions#
#---------------------------#

def create_brick():
    global brick,x1,x2,var3
    if var3!=10:
        x1 = randint(80,700)
        x2 = x1 + 30
        brick = canvas.create_rectangle(x1,100,x2,130,fill="red")
        BRICK.append(brick)
        fenetre.after(8000,create_brick)
        
        var3 +=1

def deplacement():

    global dx, dy, Var1, Var2
    x=5

    #if (canvas.coords(shot)[1]!=0):
        #print("oui")
    if Var1==0:
        canvas.move(shot,dx,dy)
        destroy_bloc(shot)
        fenetre.after(x,deplacement)
        #On deplace la balle :
        if canvas.coords(shot)[1]<50:
            canvas.delete(shot)
            Var1=1
            Var2=0
            #On repete cette fonction

def destroy_bloc(shot):
    nb = -1
    while(nb<len(BRICK)-1):
        print(canvas.coords(shot)[1])
        #if (canvas.coords(shot)[0]>canvas.coords(BRICK[nb])[0] and canvas.coords(BRICK[nb])[0]> canvas.coords(shot)[2] and canvas.coords(shot)[1]==canvas.coords(BRICK[nb])[3]):
        if(canvas.coords(shot)[1]==canvas.coords(BRICK[nb])[1]):
            canvas.delete(shot)
            canvas.delete(BRICK[nb])
            del BRICK[nb]
            nb +=1
        else:
            nb+=1

    #fenetre.after(1,destroy_bloc(shot))

def descente():
    global x,y,fin
    nb = -1

    while(nb<len(BRICK)-1):
        #print(canvas.coords(BRICK[nb])[1])
        if (canvas.coords(BRICK[nb])[1]==500):
            #print(canvas.coords(BRICK[nb])[1])
            canvas.delete(BRICK[nb])
            del BRICK[nb]
            nb+=1
            fin+=1
            lose(fin)
        else:
            canvas.move(BRICK[nb],x,y)
            nb +=1
    
    #canvas.move(BRICK[nb],x,y)
    fenetre.after(1000,descente)
    #print(BRICK)

def supprimer_bloc(BLOC,num_list_del):
    del BLOC[num_list_del]
    return BLOC

def lose(fin):
    print(fin)
    if fin == 3:
        print("perdu")
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
    global coords, shot, Var1, Var2
    gauche = -25
    droite = 25
    move = event.keysym
    if move == "Right" and coords[0]<700 :
        coords = (coords[0] + 25, coords[1])
        canvas.move(player, droite, 0)
    elif move == "Left" and coords[0]>80:
        coords = (coords[0] -25, coords[1])
        canvas.move(player, gauche, 0)
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
TIR =[]
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
#fenetre.attributes('-fullscreen', True)
fenetre.mainloop()

