#! usr/bin/env python3
class Cellule:
    """Une cellule d'une liste."""
    def __init__(self,val,suiv=None):
      self.val=val
      self.suiv=suiv
    def __str__(self):
        return str(self.val)


class ListeSimplementChainee:
    """Une liste simplement chaînée."""
    def __init__(self,range):
        self.taille=len(range)
        self.tete=Cellule("?")
        cour=self.tete
        for elt in range:
            cour.suiv=Cellule(elt)
            cour=cour.suiv
        self.queue=cour
        self.tete=self.tete.suiv
        if self.tete is None:
            self.queue=self.tete
    def __str__(self):
        chaine=""
        cour=self.tete
        while cour is not None:
            chaine+= str(cour.val)+' -> '
            cour=cour.suiv
        chaine+="FIN"
        return chaine

def recupere_cellules(liste_chainee):
    cour=liste_chainee.tete
    while cour is not None:
        yield cour
        cour=cour.suiv
def remplace_valeurs(liste_chainee,transforme):
   cour=liste_chainee.tete
   while cour is not None:
    valeur=cour.val
    cour.val=transforme(valeur)
    cour=cour.suiv
def filtre_cellules(liste_chainee,filtre):
    cour=liste_chainee.tete
    while cour is not None:
        if not isinstance(filtre(cour.val),bool):
            raise ValueError("La fonction filtre est mal implementée")
        if filtre(cour.val):
            yield cour
        cour=cour.suiv
def supprime_cellules(liste_chainee,filtre):
    iter=list(filtre_cellules(liste_chainee,filtre))
    liste_chainee.tete=Cellule("?",liste_chainee.tete)
    prec=liste_chainee.tete
    cour=liste_chainee.tete.suiv
    while cour is not None:
        if cour not in iter:
            prec.suiv=cour.suiv
        if cour.suiv is not None and prec.suiv!=cour.suiv:
            prec=cour
        cour=cour.suiv
    liste_chainee.tete=liste_chainee.tete.suiv
    if liste_chainee.queue is None:
        liste_chainee.queue=prec
def decoupe(liste_chainee,fonction):
    L1=[]
    L2=[]
    iter=filtre_cellules(liste_chainee,fonction)
    cour=liste_chainee.tete
    while cour is not None:
        if cour in iter:
            L1.append(cour.val)
        else:
            L2.append(cour.val)
        cour=cour.suiv
    liste1=ListeSimplementChainee(L1)
    liste2=ListeSimplementChainee(L2)
    return liste1,liste2
def concatene(liste1,liste2):
    def f(elt,liste1,liste2):
        iter1=recupere_cellules(liste1)
        iter2=recupere_cellules(liste2)
        return not(elt in list(iter1) and elt in list(iter2))
    if liste1.tete is None:
        liste1,liste2=liste2,liste1
    cour=liste1.queue
    iter=recupere_cellules(liste2)
    for elt in iter:
        cour.suiv=Cellule(elt.val)
        cour=cour.suiv
        supprime_cellules(liste2,f)
    liste1.queue=cour
def multiplie_par_deux(val):
    return 2*val
def est_multiple_de_deux(val):
    return val%2==0
def est_multiple_de_trois(val): 
    return val%3==0
def teste_fonctions():
    """Teste les fonctions ci-dessus"""

    # Teste le constructeur
    liste_chainee_vide = ListeSimplementChainee(range(1, 1))
    print("une liste vide :", liste_chainee_vide)
    liste_chainee = ListeSimplementChainee(range(42, 42 + 8))
    print("une liste à 7 éléments :", liste_chainee)

    # Teste la transformation
    remplace_valeurs(liste_chainee_vide, multiplie_par_deux)
    print(
        "une liste vide après remplacement des valeurs par multiplication par deux :",
        liste_chainee_vide,
    )
    remplace_valeurs(liste_chainee, multiplie_par_deux)
    print(
        "une liste à 7 éléments après remplacement des valeurs par multiplication par deux :",
        liste_chainee,
    )

    # Teste le filtre
    filtrees = filtre_cellules(liste_chainee_vide, est_multiple_de_trois)
    print("filtrage multiple de trois sur liste vide :", *filtrees)
    filtrees = filtre_cellules(liste_chainee, est_multiple_de_trois)
    # l'étoile ici est nécessaire pour que les cellules soient passées
    # en argument à `print` et non pas l'itérateur `filtrees`
    print("filtrage multiple de trois sur liste à 7 éléments :", *filtrees)
    # Teste de l'exception
    # filtrees = filtre_cellules(liste_chainee, multiplie_par_deux)
    # print(*filtrees)

    # Teste la suppression
    supprime_cellules(liste_chainee_vide, est_multiple_de_trois)
    print("supression sur liste vide :", liste_chainee_vide)
    supprime_cellules(liste_chainee, est_multiple_de_trois)
    print(
        "supression des non-multiple de trois sur liste à 7 éléments :", liste_chainee
    )

    # On teste tous les cas "limites" pour la concaténation
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)

    # Teste trie pairs / impairs
    # Ici on utilise des lambdas : c'est à dire
    # des fonctions anonyme créées directement
    # dans un appel de fonction.
    liste_chainee = ListeSimplementChainee(range(0))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    impairs, pairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)
    liste_chainee = ListeSimplementChainee(range(11))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    impairs, pairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)


if __name__ == "__main__":
    teste_fonctions()       