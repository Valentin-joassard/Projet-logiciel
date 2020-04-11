from tkinter import *
from tkinter import Tk ,Canvas

fenetre = Tk()

def clavier(event):
    global coords
    gauche = -25
    droite = 25

    move = event.keysym
    #if move == "Up" and 
        #coords = (coords[0], coords[1] - 2)
        #canvas.move(player, 0, -5)
    #elif move == "Down":
        #coords = (coords[0], coords[1] + 2)
        #canvas.move(player, 0, 5)
    if move == "Right":
        #coords = (coords[0] + 2, coords[1])
        canvas.move(player, droite, 0)
    elif move == "Left":
        #coords = (coords[0] -2, coords[1])
        canvas.move(player, gauche, 0)
    # changement de coordonnées pour le rectangle
    #print(coords)
    #canvas.coords(Image2, coords[0], coords[1], coords[0]+25, coords[1]+25)
    
    fenetre.update()
# création du canvas
canvas = Canvas(fenetre, width=768, height=576, bg="ivory")
# coordonnées initiales
#coords = (0, 0)
# création du rectangle
bg=PhotoImage(file='image/espace1.png')
background= canvas.create_image(370,250,image=bg)
p=PhotoImage(file='image/rocket.png')
player =  canvas.create_image(490,520,image=p)
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
fenetre.attributes('-fullscreen', True)
fenetre.mainloop()


