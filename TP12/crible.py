#!/usr/bin/env python3
"""
Crible d'Ératosthène
"""
from math import sqrt,floor

def init_tab(taille):
    L=[True for _ in range(taille)]
    L[0]=False
    return L

def filtre(les_premiers, prem):
    n=len(les_premiers)
    for i in range(2*prem-1,n,prem):
        if les_premiers[i]==True:
            les_premiers[i]=False


def affiche(les_premiers, val_max):
    print(f'Les nombres premiers inférieurs ou égaux à {val_max} sont:', end=" ")
    n=len(les_premiers)
    for i in range(1,n):
        if les_premiers[i]==True:
            print(i+1,end=" ")

def main():
    val_max=int(input("Entrer la valeur:\n"))
    if val_max<2:
        raise ValueError("L'entier doit etre superieur ou égal à 2")
    les_premiers=init_tab(val_max)
    print(les_premiers)
    val=floor(sqrt(val_max))+1
    for i in range(2,val):
        filtre(les_premiers,i)
    affiche(les_premiers,val_max)

if __name__ == "__main__":
    main()
