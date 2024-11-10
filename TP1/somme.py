#! usr/bin/env python3

def somme():
    
    def demande_entier():
      entier=int(input("Entrer un entier:\n"))
      return entier
    entier1=demande_entier()
    entier2=demande_entier()
    return entier1+entier2
print(somme())