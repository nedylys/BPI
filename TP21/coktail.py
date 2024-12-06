#!/usr/bin/env python3
"""
Partie "exercices" : le tri cocktail (programme principal et tests).
"""

import sys

from coktail_tab import init_tab, trier_tab

from coktail_liste import Liste, afficher_liste, remplir_liste, trier_liste


def verifier(liste, tab, ref):
    """
    Vérifie que le tableau tab contient les mêmes éléments et dans le même ordre que le
        tableau de référence ref (qui est trié par ordre croissant).
    Vérifie que la liste contient les mêmes éléments et dans le même ordre que le
        tableau de référence.
    On fait un 2ème passage en sens inverse pour vérifier les chaînages.
    """
    assert tab == ref, "\nErreur dans le tri du tableau !"
    tab = ["T"] + ref + ["Q"]
    cour = liste.tete
    idx = 0
    while cour is not None:
        assert cour.val == tab[idx], "\nErreur dans le tri de la liste !"
        cour = cour.suiv
        idx += 1
    cour = liste.queue
    while cour is not None:
        cour = cour.prec


def test_visuel():
    """
    Test visuel avec des tableaux et listes de petites tailles.
    """
    for taille in range(11):
        print(f"*** Taille = {taille} ***")
        tab = init_tab(taille)
        print("Tableau initial :", tab)
        liste = Liste()
        remplir_liste(liste, tab)
        print("Liste initiale  : ", end="")
        afficher_liste(liste)
        trier_tab(tab)
        print("Tableau trié    :", tab)
        trier_liste(liste)
        print("Liste triée     : ", end="")
        afficher_liste(liste)
        print()


def test_brut():
    """
    Test brut sur beaucoup de tableaux et listes de "grandes" tailles.
    """
    for taille in range(101):
        print(f"\rTest en cours : {taille}%", end="")
        for _ in range(500):
            ref = init_tab(taille)
            tab = ref[:]
            trier_tab(tab)
            liste = Liste()
            remplir_liste(liste, ref)
            trier_liste(liste)
            verifier(liste, tab, sorted(ref))
    print("\r100% des tests validés !\n")


def main():
    """
    Programme principal.
    """
    if len(sys.argv) == 1:
        test_visuel()
    elif len(sys.argv) == 2 and sys.argv[1] == "--test":
        test_brut()
    else:
        print(f"usage : {sys.argv[0]} [--test]")


if __name__ == "__main__":
    main()