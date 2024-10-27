#! usr/bin/env python3
import random
def extremum1(prec,cour,suiv):
    if prec<cour>suiv or prec>cour<suiv:
        return True
def extremum(list):
    if len(list)<3:
        raise ValueError
    nbr=0
    n=len(list)
    for i in range(1,n-1):
        if extremum1(list[i-1],list[i],list[i+1]):
            nbr+=1
    print(nbr)
L=[random.randint(0,100) for i in range(20)]
extremum(L)
