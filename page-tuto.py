from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont
from winsound import *
import subprocess
def menus():
    fenetre.destroy()
    subprocess.run('python page-accueil.py')

def Quitter():
    command=fenetre.quit()    

def son(n):
    global piece,Unlock1,type_image,Unlock2
    musique_bouton = PlaySound("son/souris_bouton.wav", SND_ASYNC)
    if n==1:
        fenetre.after(1000,menus())
    if n==0:
        fenetre.after(1000,Quitter())
        
fenetre = Tk() 



titre=PhotoImage(file='image/titre.png')
images=PhotoImage(file='image/espace5.png')
fonds=Label(fenetre,image=images)
fonds.place(x=-205, y =-300)

#fenetre.configure()
canvas =Canvas(fenetre, width=768, height=576, bg="ivory")

# coordonnées initiales

fontStyle = tkFont.Font(family="Eras Demi ITC", size=20)

Titre=Label(fenetre,image=titre,bg="black")
Titre.place(x=400, y =620)
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
brick = canvas.create_rectangle(20,100,50,130,fill="red")
brick = canvas.create_rectangle(20,150,50,180,fill="green")
brick = canvas.create_rectangle(20,190,50,220,fill="yellow")
brick = canvas.create_rectangle(20,230,50,260,fill="blue")
canvas.pack()
FontBouton= tkFont.Font(family="Arial Black",size=15)
fenetre.attributes('-fullscreen', True)


bouton_quitter=Button(fenetre, text="Quitter",bg='#404040',fg='grey',command=lambda n=0: son(n))
bouton_quitter.configure( width=20, height=2,font=FontBouton )
bouton_quitter.place(x=930, y=750)

bouton_accueil=Button(fenetre,text="Accueil",bg='#404040',fg='grey',command=lambda n=1: son(n))
bouton_accueil.configure( width=20, height=2,font=FontBouton )
bouton_accueil.place(x=330, y =750)

fenetre.mainloop()