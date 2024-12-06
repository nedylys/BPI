#!/usr/bin/env python3
"""
Partie "miniprojets" : génération de poèmes.
"""

import sys
fichier=sys.argv[1]
def lire_paquets_mots(nom_fichier):
    """
    Cette fonction lit le fichier dont le nom est passé en paramètre et renvoye un dictionnaire :
    - dont chaque clé est un entier représentant le numéro du paquet (0, 1, 2, ...) ;
    - dont chaque valeur est un paquet de mots, représenté par un tableau dynamique dont chaque
      case contient une ligne du paquet.
    """
    fichier=open(nom_fichier,"r")
    dico={}
    cpt=0
    dico[0]=[]
    for ligne in fichier.readlines():
        if len(ligne)!=1:
            dico[cpt].append(ligne.strip())
        else:
            cpt+=1
            dico[cpt]=[]
    return dico




def generer_poemes_3_vers(paquet0, paquet1, paquet2):
    """
    Renvoie un tableau dynamique contenant tous les poèmes de trois vers
      créés à partir des 3 paquets passés en paramètres.
    Chaque élément du tableau dynamique renvoyé est un tuple composé de trois vers :
    - le premier vers appartenant au premier paquet paquet0 ;
    - le deuxième vers appartenant au deuxième paquet paquet1 ;
    - et le troisième vers appartenant au troisième paquet paquet2.
    """
    


def poeme_aleatoire(poemes):
    """
    Choisit et renvoie un poeme tiré aléatoirement parmi tous les poèmes passés en paramètre.
    """
    # TODO
    ...



def generer_indices(indices_max):
    """
    Produit des tuples contenant toutes les combinaisons de valeurs inférieures aux maximums
      contenus dans le tableau dynamique passé en paramètre `indices_max`.
    """
    # TODO
    ...


def tous_les_poemes(paquets):
    """
    Construit et renvoie un tableau dynamique contenant tous les poèmes possibles :
    - chaque poème est construit en prenant un vers de chaque paquet de mots et stocké dans un
      tableau dynamique ;
    - on renvoie donc un tableau dynamique de tableaux dynamiques de vers.
    """
    # TODO
    ...


def main():
    """
    Programme principal.
    """
    nom_fichier = "poemes1.txt"
    if len(sys.argv) == 1:
        ...
    elif len(sys.argv) == 2:
        nom_fichier = sys.argv[1]
    else:
        print(f"usage : {sys.argv[0]} [nom du fichier .txt]")
        sys.exit(1)
    print(f"On travaille avec le fichier {nom_fichier}")
    print("\n*** Question 1 ***")
    paquets_de_mots = lire_paquets_mots(nom_fichier)
    print(f"=> les paquets de mots : {paquets_de_mots}")
    print("\n*** Question 2 ***")
    poemes_de_3_vers = generer_poemes_3_vers(
        paquets_de_mots[0], paquets_de_mots[1], paquets_de_mots[2]
    )
    print("=> tous les poèmes de trois vers :")
    for poeme in poemes_de_3_vers:
        print(poeme)
    print("\n*** Question 3 ***")
    print(
        f"=> un poème de trois vers tiré au hasard : {poeme_aleatoire(poemes_de_3_vers)}"
    )
    print("\n*** Question 4 ***")
    indices_max = [2, 1, 0]
    print(f"=> la séquence d'indices inférieurs à {indices_max} :")
    for indices in generer_indices(indices_max):
        print(indices)
    print("\n*** Question 5 ***")
    for poeme in tous_les_poemes(paquets_de_mots):
        print(poeme)
    print()


#if __name__ == "__main__":
    #main()