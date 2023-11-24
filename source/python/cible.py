from turtle import *

def cercle(rayon,couleur):
    fillcolor(couleur)
    begin_fill()
    circle(rayon)
    end_fill()
    
def deplacer(rayon):
    up()
    goto(0, -rayon)
    down()
    
if __name__ == '__main__':
    setup()
    n = 10
    rayon = 200
    ecart = rayon/(n*2)
    for i in range(n):
        deplacer(rayon)
        cercle(rayon,"red")
        rayon = rayon - ecart
        deplacer(rayon)
        cercle(rayon,"white")
        rayon = rayon - ecart

    up()
    home()
    ht()
    exitonclick()