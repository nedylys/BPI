#! usr/bin/env python3
import os
os.chdir("/user/8/.base/mountash/home/BPI/TP12")
import sys
def main():
    fichier=open(sys.argv[2],"r")
    if sys.argv[1]=='-c':
        fichier.readline()
        l=fichier.readline().rstrip()
        print(l)
        indice_prec=0
        somme=0
        for ligne in fichier.readlines():
            ligne=ligne.rstrip()
            while ligne!="":
                ligne,indice_cour,nbr=noir_blanc(ligne,indice_prec)
                somme=somme+nbr
                if indice_cour!=indice_prec:
                       print(somme)
                       somme=0
                indice_prec=indice_cour
    elif sys.argv[1]=='-d':
         f=open("decompress.pbm","w")
         fichier=open(sys.argv[2],"r")
         f.write("P1\n")
         ligne=fichier.readline()
         f.write(ligne)
         c=False
         indice=0
         for ligne in fichier.readlines():
             caract=str(int(c))
             ligne=ligne.rstrip()
             nbr=int(ligne)
             for _ in range(nbr):
                 f.write(caract)
             c=not(c)
         if indice > 0:
            f.write('\n')
                            
         fichier.close()
         f.close()
                

def noir_blanc(str,indice):
    nbr=0
    if indice==0:
        for elt in str:
            if elt=='0':
                nbr=nbr+1
                str=str.replace(elt,'')
            else:
                indice=1
                break
    else:
        for elt in str:
            if elt=='1':
                nbr+=1
                str=str.replace(elt,'')
            else:
                indice=0
                break
    return str,indice,nbr 
        
main()
