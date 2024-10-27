#! usr/bin/env python3
import sys
STATIONNAIRE = 0
CROISSANTE = 1
DECROISSANTE = -1
def parcours_fichier(nom_fichier):
    fichier=open(nom_fichier,"r")
    nombre_ligne=[]
    for ligne in fichier:
        nombre_ligne=ligne.split()
    print(nombre_ligne)
parcours_fichier(sys.argv[1])
def traite_nombre(suite,type_suite,nombre):
    n=len(suite)-1
    nouveau_type_suite=0
    if suite[n]>nombre:
        nouveau_type_suite=-1
    elif suite[n]<nombre:
        nouveau_type_suite=1
    if nouveau_type_suite==type_suite:
        return(True,nouveau_type_suite)
    else:
        return(False,nouveau_type_suite)
