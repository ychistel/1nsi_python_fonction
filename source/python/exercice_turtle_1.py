from turtle import *

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

