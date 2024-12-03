#! usr/bin/env python3
import sys
from math import cos, sin, sqrt, pi
from random import uniform, randint

def genere_balise_debut_image(largeur, hauteur):
    """Retourne la chaîne de caractères pour la balise ouvrante SVG."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
            f'width="{largeur}" height="{hauteur}">')

def genere_balise_fin_image():
    """Retourne la chaîne de caractères pour la balise fermante SVG."""
    return "</svg>"

def tracer_line(x1, y1, x2, y2):
    """Retourne la chaîne de caractères pour une ligne SVG avec indentation."""
    return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" stroke-width="2"/>'

def distance(x1, y1, x2, y2):
    """Calcul la distance entre deux points (x1, y1) et (x2, y2)."""
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <width> <height>")
        sys.exit(1)

    hauteur = int(sys.argv[1])
    largeur = int(sys.argv[2])
    dmin = 0.5  # Distance minimum to stop recursion

    # Open the SVG file for writing
    with open("fractale.svg", "w") as f:
        # Write the opening SVG tag
        f.write(genere_balise_debut_image(largeur, hauteur))
        f.write('\n')

        # Initial position (center of the canvas)
        x, y = largeur // 2, hauteur * 5e-2

        # Random number of branches (at least 1)
        nbr_branches = randint(1, 4)
        cpt = 0

        # Draw the fractal
        while cpt < nbr_branches:
            tracer_rec(x, y, dmin, f)
            cpt += 1
        
        # Write the closing SVG tag
        f.write('\n')
        f.write(genere_balise_fin_image())

def tracer_rec(x, y, dmin, f):
    """Fonction récursive pour tracer les branches du fractal."""
    alpha = uniform(-pi, pi)  # Random angle for rotation
    x1 = x * cos(alpha) - y * sin(alpha)  # Corrected rotation formula
    y1 = x * sin(alpha) + y * cos(alpha)  # Corrected rotation formula

    if distance(x, y, x1, y1) < dmin:
        return False
    else:
        # Draw the line between (x, y) and (x1, y1) with proper indentation
        caract = tracer_line(x, y, x1, y1)
        f.write(caract)
        f.write('\n')

        # Recurse to draw the next part of the fractal
        tracer_rec(x1, y1, dmin, f)

if __name__ == "__main__":
    main()

