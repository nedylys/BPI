#!/usr/bin/env python3

"""Listes simplement chaînées, triées, circulaires et avec sentinelle."""

# Décommentez si vous souhaitez utiliser le traceur
#import traceur
from math import inf

class Cellule:
    """Une cellule possède une valeur et un suivant."""

    def __init__(self, valeur, suivant=None):
        self.val=valeur
        self.suiv=suivant


class ListeSimplementChaineeTriee:
    """Listes simplement chaînées, triées, circulaires et avec sentinelle."""

    def __init__(self, valeur_sentinelle, nombres=None):
        """Construit la liste avec le range de nombres donné.

        `valeur_sentinelle` precise la valeur de la cellule sentinelle.
        pre-condition: le range de nombres donné est trié si il est
                       différent de None.
        Si le range est différent de None, on créera directement les cellules
        ici dans le constructeur. Autrement dit, on n'utilisera pas la fonction
        ajoute.
        """
        if nombres is not None:
            tmp=Cellule(valeur_sentinelle)
            self.tete=tmp
            nombres=list(nombres)
            self=Cellule(nombres.pop(),tmp)
            for i in nombres[::-1]:
             self=Cellule(i,self)
            tmp.suiv=self
        else:
            self.tete=Cellule(valeur_sentinelle)
    def __str__(self):
        """Renvoie la chaîne de caractères "val1 --> val2 --> val3 ..." """
        val=self.tete.val
        cour=self.tete.suiv
        chaine=""
        if cour is not None:
           while cour.val != val:
             chaine+= str(cour.val)+ " -->"
             cour=cour.suiv
           chaine+= "FIN"
        else:
            chaine="La liste est vide"
        return chaine

def ajoute(liste_chainee, valeur):
    """Ajoute la valeur donnée à la bonne place dans la liste chaînée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    valeur_senti=liste_chainee.tete.val
    if valeur==valeur_senti:
        raise ValueError("La valeur est mauvaise")
    cour=liste_chainee.tete.suiv
    tmp=liste_chainee.tete
    if cour is not None:
        while cour.val != valeur_senti:
         if cour.val > valeur:
            tmp.suiv=Cellule(valeur,cour)
            break
         tmp=cour
         cour=cour.suiv
        if cour.val==valeur_senti:
          tmp.suiv=Cellule(valeur,liste_chainee.tete)
    else:
        liste_chainee.tete.suiv=Cellule(valeur,tmp)

def supprime(liste_chainee, valeur):
    """Supprime la première cellule de la liste chaînée avec la valeur donnée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    valeur_senti=liste_chainee.tete.val
    if valeur==valeur_senti:
        raise ValueError("La valeur est mauvaise")
    cour=liste_chainee.tete.suiv
    tmp=liste_chainee.tete
    if cour is not None:
        while cour.val != valeur_senti:
         if cour.val==valeur:
            tmp.suiv=cour.suiv
            break
         tmp=cour
         cour=cour.suiv

def decoupe(liste_chainee):
    """Découpe la liste chaînée en deux, une cellule sur 2.

    Par exemple (1,2,3,4,5) produit (1,3,5) et (2,4).
    Renvoie les deux nouvelles listes.
    Aucune nouvelle cellule n'est créée hormis les sentinelles
    des deux nouvelles listes.
    En sortie `liste_chainee` est vide.
    """
    val_senti=liste_chainee.tete.val
    lsc_1=ListeSimplementChaineeTriee(val_senti)
    lsc_2=ListeSimplementChaineeTriee(val_senti)
    cour=liste_chainee.tete.suiv
    i=0
    while cour.val != val_senti:
        if i==0:
            ajoute(lsc_1,cour.val)
            supprime(liste_chainee,cour.val)
            i=1
        else:
            ajoute(lsc_2,cour.val)
            supprime(liste_chainee,cour.val)
            i=0
        cour=cour.suiv
    return lsc_1,lsc_2
def test():
    """Tests simples des différentes fonctions (à compléter)"""

    # On crée une liste simplement chaînée triée circulaire et l'on affiche
    liste_chainee = ListeSimplementChaineeTriee(float("inf"), range(1, 6))
    print("liste_chainee :", liste_chainee)

    # On ajoute et on supprime puis on affiche
    ajoute(liste_chainee, 0)
    ajoute(liste_chainee, 7)
    ajoute(liste_chainee, 6)
    ajoute(liste_chainee, 5)
    supprime(liste_chainee, 5)
    ajoute(liste_chainee, 8)
    supprime(liste_chainee, 8)
    print("liste_chainee :", liste_chainee) 

    # On trace notre liste
    # Décommentez si vous souhaitez utiliser le traceur
    # liste_chainee_variable = traceur.Variable("liste_chainee", liste_chainee)
    # traceur.display_vars(
    #     liste_chainee_variable, visualize=False, image_name="liste_chainee_0_a_7"
    # )

    # On découpe notre liste
    resultat_decoupe = decoupe(liste_chainee)
    pairs, impairs = resultat_decoupe  # ce qu'on fait ici s'appelle du unpacking

    # On trace le résultat de la découpe
    # Décommentez si vous souhaitez utiliser le traceur
    # resultat_decoupe_variable = traceur.Variable("res_decoupe", resultat_decoupe)
    # traceur.display_vars(
    #     resultat_decoupe_variable, visualize=False, image_name="resultat_decoupe"
    # )

    # On affiche
    print("pairs   :", pairs)
    print("impairs :", impairs)
    print("liste_chainee :", liste_chainee)

    # On refait quelques suppressions et ajouts pour le plaisir
    # puis on affiche
    supprime(pairs, 4)
    supprime(pairs, 0)
    supprime(pairs, 2)
    supprime(pairs, 6)
    ajoute(impairs, 6)
    ajoute(impairs, 0)
    print("impairs après ajout de 6 et 0 :", impairs)
    print("pairs après suppression de tous les éléments :", pairs)

if __name__ == "__main__":
    test()
