from turtle import *

n = 100
r = 150
angle = (180-360/n)

circle(r)
left(90)
for i in range(n):
    forward(r)
    right(angle)
    forward(r)
    left(180)
hideturtle()



def angle(n):
    return 180-360/n

def roue(r,n):
    circle(r)
    left(90)
    for i in range(n):
        forward(r)
        a = angle(n)
        right(a)
        forward(r)
        left(180)
        
roue(100,20)
hideturtle()
