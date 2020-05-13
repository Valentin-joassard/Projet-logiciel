from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont
from winsound import *
import subprocess
def menus():
    fenetre.destroy()
    subprocess.run('python page/page-accueil.py')

def Quitter():
    command=fenetre.quit()
    
def son(n):
    global piece,Unlock1,type_image,Unlock2
    musique_bouton = PlaySound("son/souris_bouton.wav", SND_ASYNC)
    if n==0:
        fenetre.after(1000,Quitter())
    if n==1:
        fenetre.after(1000,menus())
        
fenetre = Tk() 

titre=PhotoImage(file='image/titre.png')
images=PhotoImage(file='image/espace5.png')
fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)

#fenetre.configure()
canvas =Canvas(fenetre, width=768, height=576, bg="ivory")

fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)

Titre=Label(fenetre,image=titre,bg="black")
Titre.place(x=400, y =620)
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
left = PhotoImage(file="image/flechegauche.png")
right = PhotoImage(file="image/flechedroite.png")
tir = PhotoImage(file="image/flechehaute.png")

FontBouton= tkFont.Font(family="Arial Black",size=15)

brick1 = canvas.create_rectangle(30,450,60,480,fill="red")
brick2 = canvas.create_rectangle(30,510,60,540,fill="blue")
brick3 = canvas.create_rectangle(400,450,430,480,fill="yellow")
brick4 = canvas.create_rectangle(400,510,430,540,fill="green")

roleTouche=Label(fenetre,fg='#0c136d',bg="#404040")
roleTouche.config(text="Les commandes", font=fontStyle)
roleTouche.place(x=390,y=20)

Goleft=Label(fenetre,image=left,bg="#404040")
Goleft.place(x=500,y=100)

goLeft=Label(fenetre,fg='#0c136d',bg="#404040")
goLeft.config(text="Gauche", font=fontStyle)
goLeft.place(x=475,y=200)

Goright=Label(fenetre,image=right,bg="#404040")
Goright.place(x=675, y =100)

goRight=Label(fenetre,fg='#0c136d',bg="#404040")
goRight.config(text="Droite", font=fontStyle)
goRight.place(x=660,y=200)

Shoot=Label(fenetre,image=tir,bg="#404040")
Shoot.place(x=950, y =100)

shoot=Label(fenetre,fg='#0c136d',bg="#404040")
shoot.config(text="Tirer", font=fontStyle)
shoot.place(x=945,y=200)

roleBrick=Label(fenetre,fg='#0c136d',bg="#404040")
roleBrick.config(text="Bonus / Malus des bricks", font=fontStyle)
roleBrick.place(x=390,y=350)

Brick1=Label(fenetre,fg='#0c136d',bg="#404040")
Brick1.config(text="Neutre", font=fontStyle)
Brick1.place(x=450,y=450)

Brick2=Label(fenetre,fg='#0c136d',bg="#404040")
Brick2.config(text="Nerf vitesse de tir", font=fontStyle)
Brick2.place(x=450,y=510)

Brick3=Label(fenetre,fg='#0c136d',bg="#404040")
Brick3.config(text="Up vit. de défilement", font=fontStyle)
Brick3.place(x=830,y=450)

Brick4=Label(fenetre,fg='#0c136d',bg="#404040")
Brick4.config(text="Up vit. de déplacement", font=fontStyle)
Brick4.place(x=830,y=510)





canvas.pack()
fenetre.attributes('-fullscreen', True)


bouton_quitter=Button(fenetre, text="Quitter",bg='#404040',fg='grey',command=lambda n=0: son(n))
bouton_quitter.configure( width=20, height=2,font=FontBouton )
bouton_quitter.place(x=930, y =750)

bouton_accueil=Button(fenetre,text="Accueil",bg='#404040',fg='grey',command=lambda n=1: son(n))
bouton_accueil.configure( width=20, height=2,font=FontBouton )
bouton_accueil.place(x=330, y =750)
fenetre.mainloop()