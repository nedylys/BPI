#! usr/bin/env python3
import random
possible=["ciseaux","pierre","feuille"]
def gagne(seq1,seq2):
   if seq1==seq2:
      return 0
   if seq1==possible[0] and seq2==possible[1] :
        return 2
   elif seq1==possible[1] and seq2==possible[2]:
      return 2
   elif seq1==possible[2] and seq2==possible[0]:
      return 2
   else:
      return 1
def chifoumi():
    while True:
      jeu_1=input("pierre ou feuille ou ciseaux: \n")
      if jeu_1!=possible[0] and jeu_1!=possible[1] and jeu_1!=possible[2] :
        raise ValueError
      random.seed("ciseaux")
      jeu_2=random.choice(possible)
      a=gagne(jeu_1,jeu_2)
      if a==2:
         print("L'ordinateur a gagne")
      elif a==1:
         print("L'utilisateur a gagne")
      else:
         print("Personne n a gagne")
chifoumi()

    