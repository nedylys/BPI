#! usr/bin/env python3
import random
def prix(val):
    entier=int(input("Proposer un entier:\n"))
    while entier!=val:
      if entier>val:
          print("L'entier est trop grand")
          entier=int(input())
      elif entier<val:
         print("L'entier est trop petit")
         entier=int(input())
    print("Bravo vous avez devine")
val=random.randint(0,10)
prix(val)