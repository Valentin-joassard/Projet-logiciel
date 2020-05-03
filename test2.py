from tkinter import *
from tkinter import Tk ,Canvas
from random import randint

def deplacement():

    global dx, dy, Var1, Var2
    x=5


    #if (canvas.coords(shot)[1]!=0):
        #print("oui")
    if Var1==0:
        canvas.move(shot,dx,dy)
        fenetre.after(x,deplacement)
        #On deplace la balle :
        if canvas.coords(shot)[1]<50:
            canvas.delete(shot)
            Var1=1
            Var2=0
            #On repete cette fonction
        


def create_brick():
    global brick

    brick = canvas.create_rectangle

def descente():
    global x,y

    canvas.move(brick,x,y)
    fenetre.after(20,descente)
x=0
y=5
def supprimer_bloc(BLOC,num_list_del):
    del BLOC[num_list_del]
    return BLOC

def lose(BLOC,fin):
    nbr_list_max=len(BLOC)
    nbr_list = 0
    while nbr_list!=nbr_list_max:
        if  BLOC [nbr_list][0]==0:
            fin=fin+1
        nbr_list= nbr_list + 1
        if fin == 3:
            print("perdu")
    return fin


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
dx = 0
dy = -5
Var1=0
Var2=0
fenetre = Tk()
TIR =[]
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

