import random
from math import sqrt
def distance(L1,L2):
    return sqrt((L1[0]-L2[0])**2+(L1[1]-L2[1])**2)
def pgm():
    largeur=int(input())
    hauteur=int(input())
    print("P2\n")
    print(f'{largeur} {hauteur}\n')
    print(255)
    rayon_min = int(min(largeur * 0.2, hauteur * 0.2))
    centre_1 = (
        random.randint(rayon_min, largeur - rayon_min),
        random.randint(rayon_min, hauteur - rayon_min),
    )
    centre_2 = (
        random.randint(rayon_min, largeur - rayon_min),
        random.randint(rayon_min, hauteur - rayon_min),
    )
    rayon_max_1 = int(min(largeur - centre_1[0], centre_1[0], hauteur - centre_1[1], centre_1[1]))
    rayon_max_2 = int(min(largeur - centre_2[0], centre_2[0], hauteur - centre_2[1], centre_2[1]))
    rayon_1=random.randint(rayon_min, rayon_max_1)
    rayon_2= random.randint(rayon_min, rayon_max_2)
    for i in range(hauteur):
        for j in range(largeur):
              if distance([i,j],centre_1)>=rayon_1 or distance([i,j],centre_2)>=rayon_2:
                print(255, end=" ")
              else:
                   print(random.randint(0,255),end=" ")
pgm()
