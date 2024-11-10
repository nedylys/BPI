"""Module d'encodage/décodage par rotation"""
import string 

def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est soit une lettre majuscule
         soit une lettre minuscule.
    """
    alphabet=list(string.ascii_letters)
    indice=ord(lettre)
    if indice>96:
        indice=(indice-97)%25
        print(alphabet[indice+decalage])
    else:
        indice=(indice-65)%25
        print(alphabet[indice+decalage+26])
rot(2,'Z')
def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
   