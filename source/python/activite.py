from turtle import *

# --------------------------------
# préparation environnement Turtle
# --------------------------------

# fond gris
bgcolor('lightgray')

# initialisation des dimensions de la fenêtre
setworldcoordinates(-20,-20,400,200)

# ----------------------
# Les fonctions
# ----------------------

def deplacer(x,y):
    up()
    goto(x,y)
    down()
    
def rectangle(x,y,l,h,couleur):
    deplacer(x,y)
    begin_fill()
    color(couleur)
    for i in range(2):
        forward(l)
        left(90)
        forward(h)
        left(90)
    end_fill()

# ----------------------
# Le programme principal
# ----------------------

# Hauteur et Largeur des drapeaux
H = 120
L = 180

# ---------------------------
# Drapeau de la France:
# ---------------------------

# rectangle bleu
rectangle(0,0,L//3,H,"blue")
# rectangle blanc
rectangle(L//3,0,L//3,H,"white")
# rectangle rouge
rectangle(2*L//3,0,L//3,H,"red")

# ---------------------------
# Drapeau des Pays-Bas:
# ---------------------------

# rectangle bleu
rectangle(200,0,L,H//3,"blue")
# rectangle blanc
rectangle(200,H//3,L,H//3,"white")
# rectangle rouge
rectangle(200,2*H//3,L,H//3,"red")

hideturtle()