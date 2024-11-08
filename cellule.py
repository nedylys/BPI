#! usr/bin/env python3
from random import randint
class Cellule:
    def __init__(self,val,suiv):
        self.val=val
        self.suiv=suiv

def est_vide(liste):
    if liste is None:
        return True
    else:
        return False
def insere_tete(liste, val):
    return Cellule(val,liste)
def insere_queue(liste, val):
    cour=liste
    if liste is None:
        return Cellule(val,None)
    else:
        while cour.suiv is not None:
            cour=cour.suiv
        cour.suiv=Cellule(val,None)
        return liste
def afficher(liste):
    cour=liste
    if liste is None:
        print(None)
    else:
      while cour.suiv is not None:
        caract=str(cour.val)
        print(caract+' ->' , end=" ")
        cour=cour.suiv
      caract=str(cour.val)
      print(caract+' ->'+' FIN')

def supprime(lsc, val):
    """
    Supprime la premiere occurrence de val dans lsc (version naive sans fictif).
    La fonction renvoie la liste chaînée (éventuellement) modifiée et un booléen supp qui vaut True
      ssi il y a bien eu une suppression (c'est à dire si la liste chaînée initiale contenait au
      moins une occurrence de val).
    """
    supp = False
    if est_vide(lsc):
        pass
    elif lsc.val == val:
        lsc = lsc.suiv
        supp = True
    else:
        prec = lsc
        while prec.suiv is not None and prec.suiv.val != val:
            prec = prec.suiv
        if prec.suiv is not None:
            prec.suiv = prec.suiv.suiv
            supp = True
    return lsc, supp

def main():
    """
    Fonction principale
    """
    lsc = None  # creation d'une liste simplement chaînée vide
    print("Liste chaînée initiale vide : ", end="")
    afficher(lsc)
    print("est vide =", est_vide(lsc))
    for _ in range(10):
        ins_en_tete = randint(0,1) == 1
        val = randint(0, 5)
        if ins_en_tete:
            print(f"Insertion en tête de {val}  : ", end="")
            lsc = insere_tete(lsc, val)
        else:
            print(f"Insertion en queue de {val} : ", end="")
            lsc = insere_queue(lsc, val)
        afficher(lsc)
    print("est vide =", est_vide(lsc))
        # Ajouter ce bout de code à la fin de la fonction main de l'exercice précédent
    print("\nListe initiale   : ", end="")
    afficher(lsc)
    while not est_vide(lsc):
        val = randint(0, 5)
        print(f"Suppression de {val} : ", end="")
        lsc, supp = supprime(lsc, val)
        if supp:
            afficher(lsc)
        else:
            print("valeur absente")

main()
