from tkinter import *
from tkinter import Tk ,Canvas

menu = Tk()
menu_fenetre = Canvas(menu, width=768, height=576, bg="white")



fenetre = Tk()
canvas = Canvas(fenetre, width=768, height=576, bg="ivory")
# coordonnées initiales
#coords = (0, 0)
# création du rectangle
bg=PhotoImage(file='../image/espace1.png')
background= canvas.create_image(370,250,image=bg)
p=PhotoImage(file='../image/rocket.png')
player =  canvas.create_image(490,520,image=p)
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas


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


def clavier(event):
    global coords
    gauche = -25
    droite = 25

    move = event.keysym
    if move == "Right":
        #coords = (coords[0] + 2, coords[1])
        canvas.move(player, droite, 0)
    elif move == "Left":
        #coords = (coords[0] -2, coords[1])
        canvas.move(player, gauche, 0)
    
    fenetre.update()


def play():
    canvas.pack()
    fenetre.pack()






bouton_play=Button(menu, text="Jouer", command=play)
bouton_play.pack()
 
bouton_tuto=Button(menu, text="Tutoriel")#, command=tuto)
bouton_tuto.pack()
 
bouton_quit=Button(menu, text="Quitter")#, command=menu.destroy)
bouton_tuto.pack()

menu_fenetre.pack()
menu_fenetre.mainloop()