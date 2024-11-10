#!/usr/bin/env python3

"""Programme pour tester le module logo."""

import logo
import svg   


def main():
    """On crée un dessin a l'aide du module logo."""

    # On démarre notre image SVG
    print(svg.genere_balise_debut_image(100, 100))
    # En Python on peut nommer les arguments quand on appelle une
    # fonction. Cela rend le code beaucoup plus lisible en général.
    print(
        svg.genere_balise_debut_groupe(
            couleur_ligne="black", couleur_remplissage="none", epaisseur_ligne=3
        )
    )

    # Position de la tortue
    abscisse = 0.0
    ordonnee = 0.0
    # Angle du regard de la tortue en degrés
    # par rapport à l'horizontale, la tortue
    # regarde donc vers le haut.
    direction = 90.0
    # Si le crayon de la tortue est en bas,
    # celle-ci doit dessiner un trait quand elle
    # avance, et sinon elle doit juste se déplacer
    crayon_en_bas = False

    # On se déplace sans dessiner
    direction = logo.tourne_droite(direction, 180.0)
    # Ici on fait du tuple unpacking : on récupère d'un coup les 2 éléments du tuple.
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.tourne_gauche(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.tourne_gauche(direction, 90.0)

    # On va dessiner un premier truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On dessine un deuxième truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_gauche(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 10.0)

    # On dessine un troisième truc
    crayon_en_bas = True
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)

    # On termine l'image SVG
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


main()
def genere_segment(dep, arr):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr qui sont tous les deux
    des tuples de deux nombres.
    """
    
    