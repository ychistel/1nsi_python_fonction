from turtle import *

# --------------------------------
# préparation environnement Turtle
# --------------------------------

# fond gris
bgcolor('lightgray')

# initialisation des dimensions de la fenêtre
setworldcoordinates(-20,-20,400,200)

# -------------------------
# Les fonctions à écrire ici
# --------------------------

def deplacer(x,y):
    up()
    goto(x,y)
    down()

def rectangle(largeur, hauteur, couleur):
    begin_fill()
    color(couleur)
    for i in range(2):
       forward(largeur)
       left(90)
       forward(hauteur)
       left(90)
    end_fill()
# ----------------------------------
# Le programme principal à compléter
# -----------------------------------

# Variables H et L pour la hauteur et Largeur des drapeaux

L = 180
H = 120

# ---------------------------
# Drapeau de la France:
# ---------------------------

# rectangle bleu
x,y = 0,0
couleurs = ['blue','white','red']
for couleur in couleurs:
    deplacer(x,y)
    rectangle(L//3,H,couleur)
    x = x + L//3


# ---------------------------
# Drapeau des Pays-Bas:
# ---------------------------

# dessiner le rectangle bleu

# dessiner le rectangle blanc

# dessiner le rectangle rouge


# A la fin, on cache la tortue!
#hideturtle()