from tkinter import *
from tkinter import Tk ,Canvas
from random import randint
import tkinter.font as tkFont
from winsound import *
import subprocess


        
fenetre = Tk() 
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

Titre=Label(fenetre,image=titre,bg="black")
Titre.place(x=400, y =620)
bg=PhotoImage(file='image/espace3.png')
background= canvas.create_image(370,250,image=bg)
canvas.pack()
fenetre.attributes('-fullscreen', True)
bouton_quitter=Button(fenetre, text="Quitter",bg='#404040',fg='grey',command=fenetre.quit)
bouton_quitter.pack(side="bottom")
fenetre.mainloop()