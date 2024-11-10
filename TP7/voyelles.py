#! usr/bin/env python3
def nbr_voyelles(seq):
    nbr=int(input("Entrer le nombre de voyelles:\n"))
    seq=str.lower(seq)
    liste_voyelle=["a","e","o","u","i"]
    indice=0
    for elt in seq:    
            if elt in liste_voyelle and indice<nbr:
                indice=indice+1
                print(f'"Voyelle : {elt} ({indice}/{nbr})"')
nbr_voyelles("AU REVOIR BONJOUR")