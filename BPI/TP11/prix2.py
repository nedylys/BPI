#! usr/bin/env python3
import random
def prix(val):
    entier=int(input("Proposer un entier:\n"))  
    while entier!=val:
     if entier<0:
         print("Comment ? Vous me pensez assez tordu pour avoir choisi un prix négatif ???")
         entier=int(input())
         continue  
     elif entier>val:
          print("L'entier est trop grand")
          entier=int(input())
     elif entier<val:
         print("L'entier est trop petit")
         entier=int(input())
    print("Bravo vous avez devine")
val=random.randint(0,100)
prix(val)