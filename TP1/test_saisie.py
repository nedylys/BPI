#!/usr/bin/env python3

"""Un programme pour tester le module saisie_utilisateur.py"""

# On importe le module saisie_utilisateur
import saisie_utilisateur

# On appelle la fonction saisie_utilisateur du module saisie_utilisateur
entier = saisie_utilisateur.demande_entier()

# On appelle la fonction demande_chaine du module saisie_utilisateur
chaine = saisie_utilisateur.demande_chaine()

# On affiche le résultat
print(f"{chaine = } et {entier = }")