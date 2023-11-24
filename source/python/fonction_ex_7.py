# Somme des carrés de 2 nombres
def somme_carre(a,b):
    return a**2+b**2

# double produit de deux nombres
def double_produit(a,b):
    return 2*a*b

# identité remarquable (a+b)^2 = a^2 + 2ab + b^2
def id_rem(a,b):
    r = somme_carre(a,b)+double_produit(a,b)
    return r

# programme principal
a=7
b=3
# calculer (a+b)^2=(7+3)^2=10^2=100
resultat = id_rem(a,b)
carres = somme_carre(a,b)
double_p = double_produit(a,b)
print(resultat)
print(carres)
print(double_p)