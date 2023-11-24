from turtle import *

# Les fonctions

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

# Fond gris
bgcolor('lightgray')

# Hauteur et Largeur des drapeaux
H = 120
L = 180
# Drapeau de la France:
x = -L
y = 0
rectangle(x,y,L//3,H,"blue")
x = x + L//3
rectangle(x,y,L//3,H,"white")
x = x + L//3
rectangle(x,y,L//3,H,"red")

# Drapeau des Pays-Bas:
x = 50
y = 0
rectangle(x,y,L,H//3,"blue")
y = y + H//3
rectangle(x,y,L,H//3,"white")
y = y + H//3
rectangle(x,y,L,H//3,"red")

hideturtle()