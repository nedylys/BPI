#! usr/bin/env python3
import random
def pivote(tab,indice):
    pivot=tab[indice]
    del(tab[indice])
    tab_sup=[]
    tab_inf=[]
    n=len(tab)
    for elt in tab:
        if elt>pivot:
            tab_sup.append(elt)
        else:
            tab_inf.append(elt)
    return tab_sup,tab_inf,pivot   
def pivote_en_place_2(tab,indice):
    pivot=tab[indice]
    tab[0],tab[indice]=tab[indice],tab[0]
    n=len(tab)
    i_droite=n-1
    i_gauche=1
    while i_droite!=i_gauche:
        if tab[i_gauche]>pivot:
            tab[i_gauche],tab[i_droite]=tab[i_droite],tab[i_gauche]
            i_droite-=1
        else:
            i_gauche+=1
L=[3,7,8,6,5,9]
pivote_en_place_2(L,3)
print(L)
print(__name__)
             
                     
        