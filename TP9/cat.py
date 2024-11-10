import sys
def main(nom_fichier):
  if len(sys.argv)!=2:
    print("Donner un nom de fichier")
  else: 
     fichier=open(nom_fichier,"r")
     for ligne in fichier:
       print(ligne,end=" ")
main(sys.argv[1])
