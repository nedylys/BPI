#! usr/bin/env python3
"""
  Programme pour manipuler des listes simplement chaînées basiques.
"""

from random import randint

# TODO implantez les fonctions suivantes :
#   - inverse
#   - insere_triee
#   - trie_max


class Cellule:
    """
    Une cellule est composée d'une valeur et d'une référence vers la
      cellule suivante (ou None s'il n'y a pas de suivant)
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, val, suiv):
        """
        Constructeur
        """
        self.val = val
        self.suiv = suiv

    def __str__(self):
        """
        Afficheur
        """
        return f"{self.val} -> "


def est_vide(lsc):
    """
    Teste si la liste chaînée est vide
    """
    return lsc is None


def insere_tete(lsc, val):
    """
    Insère une cellule de valeur val en tête de la liste chaînée
    """
    return Cellule(val, lsc)


def affiche(lsc):
    """
    Affiche la liste chaînée
    """
    cour = lsc
    while cour is not None:
        print(cour, end="")
        cour = cour.suiv
    print("FIN")


def init_liste_chainee(vals=None):
    """
    Initialise une liste chaînée pour tester.
    Renvoie la liste chaînée
    """
    lsc = None
    if vals is None:  # on insère 10 chiffres aléatoires
        for _ in range(10):
            lsc = insere_tete(lsc, randint(0, 9))
    else:  # on insère les valeurs passées en argument en ordre inverse
        for val in vals:
            lsc = insere_tete(lsc, val)
    return lsc

def inverse(lsc):
    cour=lsc.suiv
    lsc.suiv=None
    while cour is not None:
           tmp=cour.suiv
           cour.suiv=lsc
           lsc=cour
           cour=tmp
    return lsc

def insere_triee(lsc,val):
    cour=lsc
    if lsc is None:
        return Cellule(val,None)
    else:
        while cour.suiv is not None and cour.suiv.val < val:
          cour=cour.suiv
        tmp=cour.suiv
        cour.suiv=Cellule(val,tmp)
        return lsc
C1=Cellule(6,None)
C2=Cellule(4,C1)
C3=Cellule(2,C2)
lsc=Cellule(1,C3)
affiche(lsc)

def supr_cellule(lsc,Cellule):
    cour=lsc
    if Cellule is lsc:
        lsc=lsc.suiv
    else:
        while cour is not None and cour.suiv is not Cellule:
           cour=cour.suiv  
        cour.suiv=Cellule.suiv
def trie_max(lsc):
    cour=lsc
    max=lsc.val
    i_max=lsc
    lsc_triee=None
    while lsc is not None:
       while cour is not None:
         if cour.suiv is not None and cour.suiv.val > max:
             max=cour.suiv.val
             i_max=cour.suiv
         cour=cour.suiv
       supr_cellule(lsc,i_max)
       lsc_triee=Cellule(lsc_triee,i_max.val)
    return lsc_triee

       



        
        

def main():
    """
    Fonction principale
    """
    print("Liste chaînée initiale  : ", end="")
    lsc = init_liste_chainee((2, 2, 4, 6, 6, 8))
    affiche(lsc)
    print("Liste chaînée inversée  : ", end="")
    lsc = inverse(lsc)
    affiche(lsc)
    print("Insertion triée : ", end="")
    for val in (1, 3, 3, 5, 7, 9, 9):
        lsc = insere_triee(lsc, val)
    affiche(lsc)
    print("Liste chaînée aléatoire : ", end="")
    lsc = init_liste_chainee()
    affiche(lsc)
    print("Tri (maximum)   : ", end="")
    lsc = trie_max(lsc)
    affiche(lsc)


main()
