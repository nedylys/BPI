#!/usr/bin/env python3
"""
  Manipulations récursives de listes chainees
"""

from random import randint

class Cellule:
    def __init__(self,val,suiv):
        self.val=val
        self.suiv=suiv
    def __str__(self):
        return str(self.val)

def creer(tab):
    """
      Construit la liste en inserant les valeurs du tableau.
      Les elements doivent apparaitre dans le meme ordre.
      Renvoie la liste construite.
      Cas de base :
        - si le tableau est de taille 0 alors la liste renvoyee est vide
      Hypothese de recurrence :
        - si L' est la liste créée à partir de tous les elements du tableau
          sauf le premier alors L est la liste créée en insérant
          le premier element du tableau en tete de L'
    """
    if len(tab) == 0:
        return None
    liste_p = creer(tab[1:])
    return Cellule(tab[0], liste_p)
def afficher(liste):
    if liste is None:
        print("FIN")
    else:
        caract= str(liste)+' ->'
        print(caract,end=" ")
        afficher(liste.suiv)

def separe(liste):
   if liste is None:
      return (None,None,0)
   else:
      l1,l2,i=separe(liste.suiv)
      if i==0:
         liste.suiv=l1
         l1=liste
         i=1
      else:
         liste.suiv=l2
         l2=liste
         i=0
   return (l1,l2,i)

      
liste=creer([0,1,8,9,7])
l2,l3,_=separe(liste)
afficher(l2)
afficher(l3)
def fusionner(liste1,liste2):
    liste=None
    cour1=liste1
    cour2=liste2
    if cour1 is None and cour2 is None:
        return liste
    else:
        if cour1 is None:
         tmp=cour2.val
         cour2.suiv=liste
         liste=cour2
         cour2=tmp
        if cour2 is None:
         tmp=cour1.val
         cour1.suiv=liste
         liste=cour1
         cour1=tmp
        elif cour1.val<cour2.val:
         tmp=cour1.val
         cour1.suiv=liste
         liste=cour1
         cour1=tmp
        else:
         tmp=cour2.val
         cour2.suiv=liste
         liste=cour2
         cour2=tmp
        fusionner(cour1,cour2)
def tri_fusion(liste):
   if liste is None:
      return None
   else:
      liste1,liste2=separer(liste)
      return fusionner(tri_fusion(liste1),tri_fusion(liste2))
def main():
    """
      Fonction principale
    """
    for taille in range(8):
        print(f"-- Taille = {taille} --")
        tab = [randint(0, 9) for _ in range(taille)]
        print("Tableau initial :", tab)
        liste = creer(tab)
        print("Liste initiale  : ", end="")
        afficher(liste)
        liste1, liste2 = separer(liste)
        print("Listes separees :")
        print("  ", end="")
        afficher(liste1)
        print("  ", end="")
        afficher(liste2)
        liste = tri_fusion(creer(tab))
        print("Liste triee     : ", end="")
        afficher(liste)
        print()
    # tests de la fonction fusionner avec des listes deja triees
    tabs = (([], []), ([], [1]), ([2], []), ([1], [2]), ([1, 3], [2]),
            ([3], [2, 4]), ([1, 5, 7], [2, 4, 6, 8]))
    for tab1, tab2 in tabs:
        print(f"Fusion de {tab1} et {tab2} :")
        liste = fusionner(creer(tab1), creer(tab2))
        print("  liste fusionnee : ", end="")
        afficher(liste)
        print()

#main()