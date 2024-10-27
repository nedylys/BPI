def fact(val):
    facto=1
    for i in range(1,val+1):
        facto=i*facto
    return facto
def factorielle():
    entier=int(input("Entrer un entier:"))
    if entier<0:
        raise ValueError("l'entier saisi doit être positif ou nul !")
    return fact(entier) 
print(factorielle())