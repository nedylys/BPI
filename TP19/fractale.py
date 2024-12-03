#! usr/bin/env python3
import sys
from math import cos,sin,sqrt,pi
from random import uniform,randint
def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    return(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1"'
          f'width="{largeur}" height="{hauteur}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    return("</svg>")


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return (
        f'<g stroke="{couleur_ligne}" fill="{couleur_remplissage}" '
        f'stroke-width="{epaisseur_ligne}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    return"</g>"
def tracer_line(x1,y1,x2,y2):
    return f'   <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="white" stroke-width="2"/>'
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type tuple de deux nombres, et rayon
    un nombre de pixels indiquant le rayon du cercle.
    """
    return f'<circle cx="{centre[0]}" cy="{centre[1]}" r="{rayon}" />'
def genere_polygone(points):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableau de points qui
    sont eux mêmes des tuples de deux nombres.
    """
    print("<polygon points=",end="")
    print('"',end="")
    n=len(points)
    for i in range(n):
        print(points[i][0],end="");print(',',end="");print(points[i][1],end=" ")
    print('/>')
def main():
    f=open("fractale.svg","w")
    hauteur=int(sys.argv[1])
    largeur=int(sys.argv[2])
    dmin=0.1
    f.write(genere_balise_debut_image(largeur,hauteur))
    f.write('\n')
    x,y=largeur//2,hauteur*5e-2
    nbr_branches=randint(1,4)
    cpt=0
    d=3
    while cpt<nbr_branches:
        while True:
          tracer_rec(x,y,d,dmin,f)
        cpt+=1
    f.write(genere_balise_fin_image())
def tracer_rec(x,y,d,dmin,f):
   alpha=uniform(-pi,pi)
   x1=cos(alpha)*x-y*sin(alpha)
   y1=sin(alpha)*x+y*cos(alpha)
   d1=distance(x,y,x1,y1)
   while d1!=d//2:
     alpha=uniform(-pi,pi)
     x1=cos(alpha)*x-y*sin(alpha)
     y1=sin(alpha)*x+y*cos(alpha)
     d1=distance(x,y,x1,y1)
   d=d1
   if distance(x,y,x1,y1)<dmin:
       return False
   else: 
      f.write(tracer_line(x,y,x1,y1))
      f.write('\n')
      tracer_rec(x1,y1,d,dmin,f)
main()
      