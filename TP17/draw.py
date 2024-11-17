#! usr/bin/env pyhton3
import sys
import approximate_pi
def genrerate_ppm_file():
    taille=int(sys.argv[2])
    nbr_virgule=sys.argv[3]
    sys.argv[2]=int(sys.argv[2])
    nbr_virgule=sys.argv[3]
    tmp=sys.argv[2]
    tmp_2=sys.argv[2]//10
    sys.argv[2]=tmp_2
    cpt=0
    while sys.argv[2]<=tmp:
      pi,points,bon_points=approximate_pi.main()
      pi=f"{pi:.{nbr_virgule}f}"
      L=pi.split('.')
      f=open(f'image{cpt}_{L[0]}-{L[1]}.pmp',"w")
      f.write("P3\n")
      f.write(f'{taille} {taille}\n')
      f.write("255\n")
      
      for _ in points:
         f.write(" 255 255 255 ")
      for _ in bon_points:
         f.write(" 0 0 0 ")
      f.write("\n")    
      sys.argv[2]+=tmp_2
      cpt+=1
      f.close()
genrerate_ppm_file()

