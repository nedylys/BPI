#!/usr/bin/env python3
"""
  Tableaux d'entiers
"""

from random import randint

# TODO : implantez les fonctions :
#  - cree
#  - indice_prem_occ
#  - echange
#  - inverse
#  - min_et_max

def cree(taille):
    tableau=[randint(1,9) for i in range(taille)]
    return tableau
def indice_prem_occ(tab,val):
    n=len(tab)
    indice=-1
    for i in range(n):
        if tab[i]==val:
            indice=i
            break 
    return indice        
def echange(tab,idx1,idx2):
    tempo=tab[idx1]
    tab[idx1]=tab[idx1]
    tab[idx2]=tempo
def inverse(tab):
    deb=0
    fin=len(tab)-1
    while deb<fin:
        echange(tab,deb,fin)
        deb+=1
        fin-=1
def min_et_max(tab):
    n=len(tab)
    if n==0:
        return (-1,-1)
    else:
      imin,imax=0,0
      min=tab[0]
      max=tab[0]
    for i in range(n):
        if tab[i]>max:
            imax=i
            max=tab[i]
        elif tab[i]<min:
            imin=i
            min=tab[i]
    return (imin,imax)

def main():
    """
    Fonction principale
    """
    for taille in range(6):
        print("-- Taille =", taille, "--")
        tab=cree(taille)
        print("Tableau initial :", tab)
        for idx in range(taille):
            print("Indice de", tab[idx], ":", indice_prem_occ(tab, tab[idx]))
        print("Indice de 10 :", indice_prem_occ(tab, 10))
        inverse(tab)
        print("Tableau inverse :", tab)
        idx_min, idx_max = min_et_max(tab)
        if idx_min == idx_max == -1:
            print("Pas de valeur min ni max dans un tableau vide !")
        else:
            print(f"Valeur minimale {tab[idx_min]} à l'indice {idx_min}")
            print(f"Valeur maximale {tab[idx_max]} à l'indice {idx_max}")
        print()
main()

