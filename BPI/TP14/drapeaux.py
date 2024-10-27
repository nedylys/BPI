#! usr/bin/env python3
from random import randint
def echanger(tab,idx1,idx2):
    tmp=tab[idx2]
    tab[idx2]=tab[idx1]
    tab[idx1]=tmp

def drapeau(tab,idx_pivot):
    pivot=tab[idx_pivot]
    echanger(tab,0,idx_pivot)
    i_pivot=0
    i_gauche=1
    i_droite=len(tab)-1
    while i_gauche<=i_droite:
        if tab[i_gauche]<pivot:
            echanger(tab,i_pivot,i_gauche)
            i_pivot+=1
        elif tab[i_gauche]>pivot:
            echanger(tab,i_gauche,i_droite)
            i_droite-=1
        else:
            i_gauche+=1
    return tab,i_pivot,i_gauche-1
L=[randint(0,10) for _ in range(10)]
i_pivot=randint(0,10)
print(L,i_pivot,L[i_pivot])
print(drapeau(L,i_pivot))
