#!/usr/bin/env python3
import random
"""
  Tris de tableaux
"""

from random import randint


def cree(taille):
    """
    Cree un tableau rempli de valeurs aléatoires
    """
    return [randint(1, 9) for _ in range(taille)]


def trie_nain(tab):
    n=len(tab)
    indice_nain=0
    while indice_nain<n-1:
        if tab[indice_nain]>tab[indice_nain+1]:
            tab[indice_nain+1],tab[indice_nain]=tab[indice_nain],tab[indice_nain+1]
            if indice_nain!=0:
               indice_nain=indice_nain-1
        elif indice_nain==0:
                indice_nain=indice_nain+1
        else:
            indice_nain+=1
def minimum(tab,debut):
    min=tab[debut]
    i_min=debut
    n=len(tab)
    for i in range(debut,n):
        if tab[i]<min:
            min=tab[i]
            i_min=i
    return i_min
def trie_min(tab):
    n=len(tab)
    for i in range(n-1):
        i_min=minimum(tab,i)
        if i_min!=i:
            tab[i],tab[i_min]=tab[i_min],tab[i]

def trie_ins(tab):
    n=len(tab)
    for i in range(1,n):
        x=tab[i]
        j=i
        while j>0 and x<tab[j-1]:
            tab[j-1],tab[j]=tab[j],tab[j-1]
            j=j-1
    

def main():
    """
    Fonction principale
    """
    for taille in range(6):  # on teste sur des tableaux de taille 0 à 5 inclus
        print("-- Taille =", taille, "--")
        tab = cree(taille)
        tab_orig = tab[:]  # copie du CONTENU du tableau
        print("Tableau initial        :", tab)
        trie_nain(tab)
        print("Tri du nain            :", tab)
        tab = tab_orig[:]
        print("Tableau initial        :", tab)
        trie_min(tab)
        print("Tri par sélect. du min :", tab)
        tab = tab_orig[:]
        print("Tableau initial        :", tab)
        trie_ins(tab)
        print("Tri par insertion      :", tab)
        print()
main()