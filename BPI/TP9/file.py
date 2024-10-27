#!/usr/bin/env python3
"""
Implantation d'une file bornée en utilisant un tableau statique
"""

CAPACITE = 5

def creer():
    """
    Crée une file de capacité donnée, sous la forme d'un tuple de trois éléments :
    - l'indice de l'élément le plus ancien de la file ;
    - le nombre d'éléments dans la file ;
    - le tableau contenant les valeurs, initialisé avec une valeur non-significative.
    """
    return (0, 0, ['@' for _ in range(CAPACITE)])

def afficher(tab, ix_ancien, nbr_elem):
    """
    Affiche le contenu de la file
    """
    print(f"(indice du plus ancien = {ix_ancien}, nombre d'éléments = {nbr_elem}, tableau = {tab})")

def inserer(tab,ix_ancien,nbr_elem,val):
    if nbr_elem==CAPACITE:
        raise ValueError("la file est pleine")
    else:
        i_nouveau=(ix_ancien+nbr_elem)%CAPACITE
        tab[i_nouveau]=val
        nbr_elem+=1
    return nbr_elem
def retirer(tab,ix_ancien,nbr_elem):
    if nbr_elem==0:
        raise ValueError("la file est vide")
    else:
        valeur_ancienne=tab[ix_ancien]
        tab[ix_ancien]='@'
        ix_ancien=(ix_ancien+1)%CAPACITE
        nbr_elem=nbr_elem-1
    return ix_ancien,nbr_elem,valeur_ancienne

def test_inserer(tab, ix_ancien, nbr_elem, vals):
    """
    Test d'insertions
    """
    print("\nJe vais faire des insertions...")
    for val in vals:
        print("Valeur à insérer :", val)
        try:
            nbr_elem = inserer(tab, ix_ancien, nbr_elem, val)
        except AssertionError as exc:
            print(exc)
            print("=> file non modifiée")
        else:
            print("=> ", end="")
            afficher(tab, ix_ancien, nbr_elem)
    return ix_ancien, nbr_elem

def test_retirer(tab, ix_ancien, nbr_elem, nbr):
    """
    Test de suppressions
    """
    print("\nJe vais faire des extractions...")
    for _ in range(nbr):
        try:
            ix_ancien, nbr_elem, val = retirer(tab, ix_ancien, nbr_elem)
        except AssertionError as exc:
            print(exc)
            print("=> file non modifiée")
        else:
            print(f"Valeur retirée = {val}")
            print("=> ", end="")
            afficher(tab, ix_ancien, nbr_elem)
    return ix_ancien, nbr_elem

def main():
    """
    Programme principal
    """
    print("Creation d'une file vide...")
    ix_ancien, nbr_elem, tab = creer()
    print("=> ", end="")
    afficher(tab, ix_ancien, nbr_elem)
    ix_ancien, nbr_elem = test_retirer(tab, ix_ancien, nbr_elem, 1)
    ix_ancien, nbr_elem = test_inserer(tab, ix_ancien, nbr_elem, (1, 2, 3))
    ix_ancien, nbr_elem = test_retirer(tab, ix_ancien, nbr_elem, 2)
    ix_ancien, nbr_elem = test_inserer(tab, ix_ancien, nbr_elem, (4, 5, 6, 7, 8))
    ix_ancien, nbr_elem = test_retirer(tab, ix_ancien, nbr_elem, 1)
    ix_ancien, nbr_elem = test_inserer(tab, ix_ancien, nbr_elem, (8, 9))

main()
