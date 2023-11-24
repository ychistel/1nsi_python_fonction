from turtle import *

def polygone(c,n):
    for i in range(n):
        forward(c)
        left(360/n)
    
c = 100
n = 4
for i in range(3,n+3):
    polygone(c,i)
    left(180-360/i)

    
