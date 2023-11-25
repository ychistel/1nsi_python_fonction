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
    
def rectangle(l,h,couleur):
    begin_fill()
    color(couleur)
    for i in range(2):
        forward(l)
        left(90)
        forward(h)
        left(90)
    end_fill()

def dessiner_drapeau(x,y,largeur,hauteur,pays,position):
    for couleur in pays:
        deplacer(x,y)
        if position == 'h':
            rectangle(largeur//3,hauteur,couleur)
            x = x + largeur//3
        else:
            rectangle(largeur, hauteur//3, couleur)
            y = y + hauteur//3

# ----------------------
# Le programme principal
# ----------------------

# Hauteur et Largeur des drapeaux
H = 120
L = 180

# ---------------------------
# Drapeau de la France:
# ---------------------------

fr = ['blue','white','red']
dessiner_drapeau(0,0,L,H,fr,'h')

# ---------------------------
# Drapeau de l'Allemagne:
# ---------------------------

al = ['yellow','red','black']
dessiner_drapeau(200,0,L,H,al,'v')

# on cache la tortue
hideturtle()
# on met fin à la boucle d'exécution du module
mainloop()