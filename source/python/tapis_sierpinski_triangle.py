from turtle import *
from math import sqrt

def carre(x,y,cote,color="black"):
    deplacer(x,y)
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(cote)
        left(90)
    end_fill()

def triangle(x,y,cote,angle,color="black"):
    deplacer(x,y)
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(cote)
        left(angle)
    end_fill()
    
def deplacer(x,y):
    up()
    goto(x,y)
    down()

def motif_tapis(x,y,cote):
    triangle(x,y,cote,120)
    triangle(x+cote/4,y+cote*sqrt(3)/4,cote//2,-120,"white")


def tapisser(x,y,cote):
    motif_tapis(x,y,cote)
    motif_tapis(x+cote,y,cote)
    motif_tapis(x+cote/2,y+cote*sqrt(3)/2,cote)
    
if __name__ == '__main__':
    speed("fastest")
    cote=360
    n=3
    motif_tapis(0,0,cote)
    tapisser(0,0,cote/2)
    
    x,y = 0,0
    c = cote/2
    for i in range(2):
        tapisser(x,y,c/2)
        x = x +c
    tapisser(c/2,y+c*sqrt(3)/2,c/2)
    
    x,y = 0,0
    c = cote/4
    for i in range(2):
        tapisser(x,y,c/2)
        x = x +c
    tapisser(c/2,y+c*sqrt(3)/2,c/2)
    
    x,y = cote/2,0
    c = cote/4
    for i in range(2):
        tapisser(x,y,c/2)
        x = x +c
    tapisser(cote/2+c/2,y+c*sqrt(3)/2,c/2)
    
    x,y = cote/4,cote*sqrt(3)/4
    c = cote/4
    for i in range(2):
        tapisser(x,y,c/2)
        x = x +c
    tapisser(cote/4+c/2,y+c*sqrt(3)/2,c/2)
    hideturtle()