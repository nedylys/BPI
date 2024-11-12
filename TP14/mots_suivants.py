#!/usr/bin/env python3
"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour générer des phrases aléatoires.
"""
import sys
from re import finditer
from random import choice, random
from os import system


def get_mots(nom_fichier):
    """Renvoie un tableau dynamique sur tous les mots du fichier.

    Elimine au passage tout ce qui n'est pas une lettre.
    """
    mots = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                mots.append(mot.group(0))
    return mots


def get_couples(tableau):
    """Renvoie un un tableau dynamique des couples.

    Le tableau dynamique renvoyé contient tous les couples d'elements
    successifs du tableau donné.
    """
    couples = []
    valeur_precedente = tableau[0]
    for valeur in tableau[1:]:
        couples.append((valeur_precedente, valeur))
        valeur_precedente = valeur
    return couples


def analyse_texte():
    """Analyse le fichier donné en argument.

    L'analyse parcours les mots du fichier et dessine le graphe
    des mots suivants.

    Ensuite, une phrase aléatoire est générée à partir du dictionnaire
    des mots.
    """

    # Parcours
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    genere_graphe(suivants)

    # Génération d'une petite phrase aleatoire.
    mot_depart = choice(list(suivants.keys()))
    phrase = [mot_depart]
    for _ in range(10):
        phrase.append(get_suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def compte_mots_suivants(nom_fichier):
    """Renvoie le dictionnaire des mots suivants.

    Renvoie un dictionnaire associant a chaque mot m1 du fichier
    un dictionnaire associant a chaque mot m2 suivant m1 dans le
    fichier le nombre de fois ou m2 apparait apres m1.
    """
    dico={}
    mots=get_mots(nom_fichier)
    for elt in mots:
        dico[elt]={}
    couples=get_couples(mots)
    n=len(couples)
    for i in range(n):
       for elt in couples[i]:
           if couples[i][1] in dico[couples[i][0]]:
               dico[couples[i][0]][couples[i][1]]+=1
           else:
               dico[couples[i][0]][couples[i][1]]=1
    return dico

def genere_graphe(suivants):
    """Genere le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe
    with open("mots-suivants.dot", "w") as fichier_dot:
          fichier_dot.write('digraph  {'+'\n')
          for elt in suivants:
              mot=elt
              for mots in suivants[elt]:
                  mot_suiv=mots
                  fichier_dot.write(f'{mot} -> {mot_suiv} [label={suivants[elt][mots]}]'+'\n')
          fichier_dot.write('}') 
    # On utilise l'outil dot pour convertir le fichier .dot en image
    system("dot -Tpng mots-suivants.dot -o mots-suivants.png")


def get_suivant_aleatoire(mot, suivants):
    """Tire aléatoirement un suivant du mot donné.

    Le tirage aléatoire doit être pondéré par le nombre d'occurrences.
    Si le mot donne n'a pas de suivant, retourne un mot aléatoire.
    """
    L=[]
    if suivants[mot]=={}:
        return mot
    else:
        for elt in suivants[mot]:
            nbr=suivants[mot][elt]
            for _ in range(nbr):
                L.append(elt)
        mot_choisi=choice(L)
        return mot_choisi


if __name__ == "__main__":
    analyse_texte()