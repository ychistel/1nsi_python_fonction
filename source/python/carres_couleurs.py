import turtle
from random import randint

turtle.colormode(255)
turtle.speed("fastest")

def carre(cote, couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(cote)
        turtle.left(90)
    turtle.end_fill()
        

if __name__ == '__main__':
    n=30
    cote=10
    for i in range(n):
        couleur=(randint(0,255),randint(0,255),randint(0,255))
        carre(cote*(n-i),couleur)
    turtle.ht()
