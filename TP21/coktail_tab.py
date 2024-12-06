#!/usr/bin/env python3
"""
Partie "exercices" : le tri cocktail (version tableau).
"""

from random import randint


def init_tab(taille):
    """
    Initialise et renvoie un tableau de taille chiffres aléatoires.
    """
    return [randint(0, 9) for _ in range(taille)]


def parcourir_echanger_tab(tab, inv=False):
    """
    Parcours le tableau et échange deux à deux les éléments désordonnés.
    On parcourt le tableau du début à la fin ssi inv est faux, et de la fin au début
      sinon.
    Pré-condition : le tableau contient au moins deux éléments.
    On renvoie True s'il y a eu au moins un échange et False sinon.
    """
    n=len(tab)
    ech=False
    if not inv: 
     for i in range(n-1):
        if tab[i]>tab[i+1]:
            tab[i],tab[i+1]=tab[i+1],tab[i]
            ech=True
    else:
       for i in range(n-1,1,-1):
        if tab[i]<tab[i-1]:
            tab[i],tab[i-1]=tab[i-1],tab[i]
            ech=True
    return ech


def trier_tab(tab):
    """
    Tri le tableau selon l'algorithme du cocktail shaker.
    """
    ech=True
    inv=True
    while ech:
       inv=not(inv)
       ech=parcourir_echanger_tab(tab,inv)
if __name__=='__main__':
  tab=init_tab(8)
  print(tab)
  trier_tab(tab)
  print(tab)