#! usr/bin/env python3
def demande_entier():
    return int(input("Entrer un entier\n"))
def demande_chaine():
    return input("Entrer un message\n")
def teste_module():
    """Teste les fonctions du module"""
    entier1 = demande_entier()
    entier2 = demande_entier()
    print("la somme vaut", entier1 + entier2)
teste_module()
print("__name__ =", __name__)
if __name__ == "__main__":
    teste_module()