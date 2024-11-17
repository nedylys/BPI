#!/usr/bin/env python3
"""
  Tableau de listes chaînées
"""

from random import randint

class Cellule:
    def __init__(self,val,suiv=None):
        self.val=val
        self.suiv=suiv
class Liste:
    def __init__(self,fictif):
        self.tete=Cellule(fictif)
        self.nombre=0
        self.suiv=self.tete.suiv
    def __str__(self):
        chaine=""
        cour=self.tete.suiv
        while cour is not None:
                chaine+=str(cour.val) + " ->"
                cour=cour.suiv
        if chaine=="":
            return "La liste est vide"
        return chaine
    
class TableauListe:
    def __init__(self,len):
        self.len=len
        self.list=[Liste("?") for _ in range(len)]
        self.nbr_elem=0
    def hash(self,val):
        return val%self.len
    def insere(self,val):
        pos=self.hash(val)
        cour=self.list[pos].tete
        while cour.suiv is not None:
            cour=cour.suiv
        cour.suiv=Cellule(val)
        self.list[pos].nombre+=1
        self.nbr_elem+=1
    def est_presente(self,val):
        L=self.list
        for i in range(self.len):
            if L[i].nombre !=0:
                cour=L[i].tete.suiv   
                while cour is not None:
                    if cour.val==val:
                        return True
                    cour=cour.suiv
        return False
    def supprimer(self,val):
        L=self.list
        for i in range(self.len):
            if L[i].nombre !=0:
                cour=L[i].tete.suiv
                prec=L[i].tete   
                while cour is not None:
                    if cour.val==val:
                        prec.suiv=cour.suiv
                        L[i].nombre-=1
                        self.nbr_elem-=1
                        return True
                    prec=cour
                    cour=cour.suiv
        return False
    def __str__(self):
        L=self.list
        chaine=""
        for elt in L:
            if str(elt)!="La liste est vide":
              chaine+=str(elt)+'\n'
        if chaine=="":
            return "Le tableau est vide"
        return chaine

       
def main():
    """
    Fonction principale
    """
    struct = TableauListe(4)
    print(struct)
    for _ in range(10):
        val = randint(0, 9)
        print("\nAjout de la valeur", val)
        struct.insere(val)
        print(struct)
    print()
    for val in range(5):
        if struct.est_presente(val):
            print(f"{val} est presente dans la structure")
        else:
            print(f"{val} est absente de la structure")
    print()
    print(struct)
    print(struct.nbr_elem)
    while struct.nbr_elem> 0:
        val = randint(0, 9)
        if struct.supprimer(val):
            print("\nSuppression de la valeur", val)
            print(struct)


main()

