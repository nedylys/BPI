#!/usr/bin/env python3
"""Mini projet Images PGM"""
from random import randint, seed


def contient(disque, point):
    """Fonction qui determine si un point est contenu dans un disque"""
    difference_abscisses = point[0] - disque[0][0]
    difference_ordonnees = point[1] - disque[0][1]
    distance_carree = (
        difference_abscisses * difference_abscisses
        + difference_ordonnees * difference_ordonnees
    )
    return distance_carree <= disque[1] * disque[1]


def tire_disque(largeur, hauteur):
    """Tire aléatoirement un disque complètement inclus dans une image de la taille donnée"""

    # On veut un cercle avec un rayon minimum de 20% de la
    # plus petite dimension de l'image.
    rayon_min = min(largeur * 0.2, hauteur * 0.2)

    # On tire le centre
    centre = (
        randint(rayon_min, largeur - rayon_min),
        randint(rayon_min, hauteur - rayon_min),
    )

    # On tire ensuite le rayon
    rayon_max = min(largeur - centre[0], centre[0], hauteur - centre[1], centre[1])
    rayon = randint(rayon_min, rayon_max)

    return (centre, rayon)


def affiche_entete(largeur, hauteur):
    """Affichage de l'entête pgm sur stdout"""
    print("P2")
    print(f"{largeur} {hauteur}")
    print("255")


def affiche_pixels(disque1, disque2, largeur, hauteur):
    """Calcul des pixels aléatoires et affichage sur stdout"""
    for ligne in range(hauteur):
        for colonne in range(largeur):
            point = (colonne, ligne)
            if contient(disque1, point) or contient(disque2, point):
                print(randint(0, 255), end=" ")
            else:
                print(255, end=" ")
        print()


def main():
    """Point d'entrée du programme"""
    # À dé-commenter pour de l'aléatoire "contrôlé"
    # seed(41)

    # On demande à l'utilisateur la taille de l'image
    larg = int(input())
    haut = int(input())

    # On tire deux disque aléatoires
    d1 = tire_disque(larg, haut)
    d2 = tire_disque(larg, haut)

    # On affiche l'image
    affiche_entete(larg, haut)
    affiche_pixels(d1, d2, larg, haut)


main()