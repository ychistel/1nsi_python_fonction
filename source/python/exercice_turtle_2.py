from turtle import *
"""
def carre(c):
    for i in range(4):
        forward(c)
        left(90)

def triangle(t):
    for i in range(3):
        forward(t)
        left(120)
    
def hexagone(c):
    for i in range(6):
        forward(c)
        left(60)
        
carre(120)
triangle(120)
hexagone(120)
"""

def polygone(c,n):
    for i in range(n):
        forward(c)
        left(360/n)
"""        
polygone(120,4)
polygone(120,3)
polygone(120,6)
"""
for i in range(3,11):
    polygone(120,i)