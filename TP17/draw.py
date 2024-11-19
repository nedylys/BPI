#! usr/bin/env pyhton3
import sys
import approximate_pi
import subprocess
def genrerate_ppm_file():
    taille=int(sys.argv[1])
    nbr_virgule=sys.argv[3]
    inside_cirle='255 0 0 '
    out_circle='0 255 0 '
    background='255 255 255 '
    sys.argv[2]=int(sys.argv[2])
    nbr_virgule=sys.argv[3]
    tmp=sys.argv[2]
    tmp_2=sys.argv[2]//10
    sys.argv[2]=tmp_2
    cpt=0
    color_data=[[background for _ in range(taille)]for _ in range(taille)]
    print(len(color_data[0]))
    while sys.argv[2]<=tmp:
      pi,points=approximate_pi.main()
      pi=f"{pi:.{nbr_virgule}f}"
      L=pi.split('.')
      f=open(f'image{cpt}_{L[0]}-{L[1]}.pmp',"w")
      f.write("P3\n")
      f.write(f'{taille} {taille}\n')
      f.write("255\n")
      for elt in points:
         x,y,indice=elt
         px=int((x+1)/2*(taille-1))
         py=int((y+1)/2*(taille-1))
         if indice:
            color_data[px][py]=inside_cirle
         else:
            color_data[px][py]=out_circle
      for i in range(taille):
         for j in range(taille-1):
            f.write(color_data[i][j])
         f.write(color_data[i][j]+'\n')
      f.write("\n")    
      sys.argv[2]+=tmp_2
      cpt+=1
      f.close()
    subprocess.run(["convert", "-delay", "10", "-loop", "0", ".ppm", "animation.gif"])
    print("Animation GIF créée : animation.gif")
genrerate_ppm_file()


