from turtle import *

def carre(x,y,cote,color="black"):
    deplacer(x,y)
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(cote)
        left(90)
    end_fill()

def triangle(x,y,cote,color="black"):
    deplacer(x,y)
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(cote)
        left(120)
    end_fill()
    
def deplacer(x,y):
    up()
    goto(x,y)
    down()

def motif_tapis(x,y,cote):
    carre(x,y,cote)
    carre(x+cote//3,y+cote//3,cote//3,"white")


def tapisser(x,y,cote):
    motif_tapis(x,y,cote)
    motif_tapis(x+cote,y,cote)
    motif_tapis(x+2*cote,y,cote)
    motif_tapis(x,y+cote,cote)
    #motif_tapis(x+cote,y+cote,cote)
    motif_tapis(x+2*cote,y+cote,cote)
    motif_tapis(x,y+2*cote,cote)
    motif_tapis(x+cote,y+2*cote,cote)
    motif_tapis(x+2*cote,y+2*cote,cote)
    
if __name__ == '__main__':
    speed("fastest")
    cote=360
    n=3
    motif_tapis(0,0,cote)
    tapisser(0,0,cote/3)
    x,y = 0,0
    cote = cote/3
    for i in range(3):
        tapisser(x,y,cote/3)
        x = x +cote
    tapisser(0,cote,cote/3)
    tapisser(2*cote,cote,cote/3)
    x,y = 0,2*cote
    for i in range(3):
        tapisser(x,y,cote/3)
        x = x +cote
    