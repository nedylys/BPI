#! usr/bin/env python3
#!/usr/bin/env python3

"""Listes simplement chaînées + quelques operations."""

#import traceur

class Cellule:
    """Une cellule d'une liste."""
    def __init__(self,val,suiv=None):
      self.val=val
      self.suiv=suiv


class ListeSimplementChainee:
    """Une liste simplement chaînée."""
    def __init__(self,range):
        self.taille=len(range)
        self.tete=Cellule("?")
        cour=self.tete
        for elt in range:
            cour.suiv=Cellule(elt)
            cour=cour.suiv
        self.queue=cour
        self.tete=self.tete.suiv
    def __str__(self):
        chaine=""
        cour=self.tete
        while cour is not None:
            chaine+= str(cour.val)+' -> '
            cour=cour.suiv
        chaine+="FIN"
        return chaine


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tête."""
    liste_chainee.taille+=1
    liste_chainee.tete=Cellule(valeur,liste_chainee.tete)
    if liste_chainee.queue is None:
        liste_chainee.queue=liste_chainee.tete

def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    liste_chainee.taille+=1
    if liste_chainee is not None:
      liste_chainee.queue.suiv=Cellule(valeur,None)
      liste_chainee.queue=liste_chainee.queue.suiv    
    else:
        liste_chainee.queue,liste_chainee.tete=Cellule(valeur,None),Cellule(valeur,None)

def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la première cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    cour=liste_chainee.tete
    while cour is not None:
        if cour.val==valeur:
            return cour
        cour=cour.suiv
    return None    

def supprime(liste_chainee, valeur):
    """Supprime la premiere cellule contenant la valeur donnée."""
    ajoute_en_tete(liste_chainee,"?")
    cour=liste_chainee.tete.suiv
    prec=liste_chainee.tete
    while cour is not None:
        if cour.val==valeur:
            prec.suiv=cour.suiv
            liste_chainee.taille-=1
            break
        prec=cour
        cour=cour.suiv
    liste_chainee.tete=liste_chainee.tete.suiv
    if cour==liste_chainee.queue:
        liste_chainee.queue=prec


def teste_listes():
    """On teste les operations de base, dans différentes configurations."""
    liste_chainee = ListeSimplementChainee(range(6))
    # traceur.display_instance(
    #     liste_chainee, visualize=False, image_name="liste_chainee_0"
    # )
    ajoute_en_tete(liste_chainee, 3)
    print(liste_chainee)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    # traceur.display_instance(
    #     liste_chainee, visualize=False, image_name="liste_chainee_1"
    # )
    print("recherche : ", recherche(liste_chainee, 3).val)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    # traceur.display_instance(
    #     liste_chainee, visualize=False, image_name="liste_chainee_2"
    # )
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    # traceur.display_instance(
    #     liste_chainee, visualize=False, image_name="liste_chainee_3"
    # )
if __name__=='__main__':
    teste_listes()