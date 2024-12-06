#!/usr/bin/env python3
"""
Partie "exercices" : le tri cocktail (version liste).
"""

# Cette ligne sert à désactiver un message inutile de pylint :
# pylint: disable=too-few-public-methods


class Cellule:
    """
    Une cellule est constituée :
    - d'une valeur ;
    - d'un pointeur vers la cellule précédente ;
    - d'un pointeur vers la cellule suivante.
    """

    def __init__(self, val, prec, suiv):
        """
        Constructeur d'une cellule.
        """
        self.val = val
        self.prec = prec
        self.suiv = suiv

    def __str__(self):
        """
        Afficheur d'une cellule.
        """
        return f"{self.val}"


class Liste:
    """
    La classe représentant les listes doublement chaînées.
    """

    def __init__(self):
        """
        Crée une liste doublement chaînée avec éléments fictifs en tête et en queue.
        """
        self.tete = Cellule("T", None, None)
        self.queue = Cellule("Q", None, None)
        self.tete.suiv = self.queue
        self.queue.prec = self.tete


def remplir_liste(liste, tab):
    """
    Remplit la liste avec les mêmes éléments que le tableau et dans le même ordre.
    On ne renvoie rien car les références vers la tête et la queue ne changent pas.
    """
    for val in tab:
        nouv = Cellule(val, liste.queue.prec, liste.queue)
        liste.queue.prec.suiv = nouv
        liste.queue.prec = nouv


def afficher_liste(liste):
    """
    Affiche le contenu de la liste (y compris les sentinelles).
    """
    cour = liste.tete
    while cour is not None:
        print(cour, end="" if cour.suiv is None else " <-> ")
        cour = cour.suiv
    print()


def echanger_cellules(cell):
    """
    Échange cell avec cell.suiv puis renvoie le pointeur mis à jour.
    Pré-condition : cell et cell.suiv sont des cellules significatives
      (c.a.d ni la tête ni la queue) de la liste.
    """
    prec = cell.prec
    cour = cell
    suiv = cell.suiv
    suiv_suiv = suiv.suiv
    prec.suiv = suiv
    cour.prec = suiv
    cour.suiv = suiv_suiv
    suiv.prec = prec
    suiv.suiv = cour
    suiv_suiv.prec = cour
    return suiv


def liste_vide_ou_singleton(liste):
    """
    Renvoie True ssi la liste ne contient aucun ou qu'un seul élément significatif
      (hors sentinelles).
    """
    cour=liste.tete.suiv
    if cour.suiv is None or cour.suiv==liste.queue:
        return True
    return False
    


def parcourir_echanger_liste(liste, inv=False):
    """
    Parcours la liste et échange deux à deux les éléments désordonnés.
    On parcourt la liste de la tête à la queue ssi inv est faux, et de la queue
      à la tête sinon.
    Pré-condition : la liste contient au moins deux cellules significatives.
    Cette fonction renvoie un booléen valant True ssi il y a eu au moins un
      échange pendant le parcours.
    """
    modif=False
    val_queue="Q"
    val_tete="T"
    if not inv:
     cour=liste.tete.suiv
     while cour.suiv.val is not val_queue:
        if cour.val > cour.suiv.val:
            cour=echanger_cellules(cour)
            modif=True
        cour=cour.suiv
    else:
        cour=liste.queue.prec
        while cour.prec.val is not val_tete:
            if cour.val<cour.prec.val:
                cour=echanger_cellules(cour.prec)
                modif=True
            else:
              cour=cour.prec
    return modif
    

def trier_liste(liste):
    """
    Trie la liste par ordre croissant selon l'algorithme du cocktail shaker.
    On ne renvoie rien car les références vers la tête et la queue ne changent pas.
    """
    vide=liste_vide_ou_singleton(liste)
    if not vide:
      modif=parcourir_echanger_liste(liste)
      inv=True
      while modif:
        inv=not(inv)
        modif=parcourir_echanger_liste(liste,inv)
if __name__=='__main__':
    liste=Liste()
    remplir_liste(liste,[0,1,7,8,9,0,6,4,3,9])
    afficher_liste(liste)
    trier_liste(liste)
    afficher_liste(liste)