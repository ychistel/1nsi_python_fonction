tableau = [7,13,20]

def effet_de_bord(t):
    for i in range(3):
        t[i] = t[i] * 2
    return t

double = effet_de_bord(tableau)
