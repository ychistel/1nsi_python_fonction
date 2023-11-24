"""
1/ On veut calculer pour un nombre n choisi
la somme:
1+2+3+ ... + n
2/ On calcule la somme des carrés
1^2+2^2+3^23...+n^2
"""

def somme_arithm(n):
    s = 0 # la somme est 0 au début
    for i in range(1,n+1):
        # n+1 car s'arête à n dans le range
        s = s+i
    return s

def somme_carre(n):
    s = 0 # la somme est 0 au début
    for i in range(1,n+1):
        # n+1 car s'arête à n dans le range
        s = s+i**2
    return s

# calcul de 1+2+3+4+5 -> 15
s5 = somme_arithm(5) 
print(s5)
# calcul de 1+2+3+4+5+6+7+8+9+10 -> 55
s10 = somme_arithm(10)
print(s10)
# calcul de 1²+2²+3²+4²+5² -> 55
sc5 = somme_carre(5) 
print(sc5)
# calcul de 1²+2²+3²+...+9²+10² -> 385
sc10 = somme_carre(10) 
print(sc10)
