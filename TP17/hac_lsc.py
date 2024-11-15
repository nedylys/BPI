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
    def __str__(self):
        chaine=""
        if self.tete.suiv is not None:
            cour=self.tete.suiv
            while cour is not None:
                chaine=str(cour.val) + " ->"
                cour=cour.suiv
        return chaine
    
class TableauListe:
    def __init__(self,len):
        self.len=len
        self.list=[Liste("?") for i in range(len)]
    def hash(self,val):
        return val%self.len
    def insere(self,val):
        pos=self.hash(val)
        for i in range(self.len):
            if i==pos:
                self.list[i].suiv=Cellule(val)
                self.list[i].nombre+=1
    def est_presente(self,val):
        pres=False
        exit=False
        L=self.list
        for i in range(self.len):
            if L[i].nombre !=0:
                cour=L[i]   
                while cour is not None:
                    if cour.val==val:
                        pres=True
                        exit=True
                        break
                    cour=cour.suiv
            if exit==True:
                break
        return pres
    def supprimer(self,val):
        pres=False
        exit=False
        L=self.list
        for i in range(self.len):
            if L[i].nombre !=0:
                cour=L[i].tete.suiv
                prec=L[i].tete   
                while cour is not None:
                    if cour.val==val:
                        pres=True
                        exit=True
                        prec.suiv=cour.suiv
                        break
                    prec=cour
                    cour=cour.suiv
            if exit==True:
                break
        return pres
    def __str__(self):
        L=self.list
        chaine=""
        for elt in L:
            chaine+=str(elt)+'\n'
        return chaine


                
lsc=Liste("?")
        
       

       
              
       
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
    while struct.len> 0:
        val = randint(0, 9)
        if struct.supprimer(val):
            print("\nSuppression de la valeur", val)
            struct.afficher()


#main()
