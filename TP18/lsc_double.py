#!/usr/bin/env python3
"""
  Listes doublement chainees
"""

from random import randint
class Cellule:
    def __init__(self,val,prec=None,suiv=None):
        self.val=val
        self.prec=prec
        self.suiv=suiv
        
class ListeDouble:
    def __init__(self):
        C1=Cellule("?")
        C2=Cellule("?")
        C1.prec,C1.suiv=C2,C2
        C2.suiv,C2.prec=C1,C1
        self.tete=C1
        self.queue=C2
    def remplir(self,tab):
       prec=self.tete
       cour=self.queue
       for elt in tab:
           prec.suiv=Cellule(elt,prec,cour)
           prec=prec.suiv
       self.queue.prec=prec
    def afficher(self,inverse=False):
        chaine=""
        if inverse==False:
            chaine+='Tete <-> '
            cour=self.tete.suiv
            while cour!=self.queue:
                chaine+= str(cour.val)+' <-> '
                cour=cour.suiv
            chaine+='Queue'
        else:
            chaine+='Queue <-> '
            cour=self.queue.prec
            while cour !=self.tete:
                chaine+= str(cour.val)+' <-> '
                cour=cour.prec
            chaine+=' Tete '
        print(chaine)
    def trier(self):
        if self.tete.suiv==self.queue:
            raise ValueError("La liste est vide")
        cour=self.tete.suiv
        while cour!=self.queue:
            if cour.val > cour.suiv.val and cour.prec!=self.tete:
                echanger(cour)
                cour=cour.prec
            elif cour.suiv!=self.queue:
                cour=cour.suiv
def echanger(cell):
    if cell.suiv.val=='?':
      raise ValueError("C'est la derniere Celllule")
    tmp=cell.suiv
    tmp.prec=cell.prec
    tmp.suiv=cell
    cell.prec=tmp
    cell.suiv=tmp
    return tmp
liste = ListeDouble()
L=[0,2]
C1=Cellule(2,None,liste.queue)
cell=Cellule(0,liste.tete,C1)
C1.prec=cell
_=echanger(cell)
liste.afficher()
def main():
    """
      Fonction principale
    """
    liste = ListeDouble()
    liste.remplir([randint(0, 9) for _ in range(5)])
    print("Liste initiale  : ", end="")
    liste.afficher()
    print("en sens inverse : ", end="")
    liste.afficher(True)
    cell = liste.tete.suiv
    while cell is not liste.queue.prec:
        echanger(cell)
        print("Test echangerr   : ", end="")
        liste.afficher()
    liste.trier()
    print("Liste triee     : ", end="")
    liste.afficher()
    print("en sens inverse : ", end="")
    liste.afficher(True)

#main()
