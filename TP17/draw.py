#! usr/bin/env pyhton3
import sys
import approximate_pi
import subprocess
def draw_pi_text(color_data, pi, center_x, center_y, taille):
    # Colors for each digit of pi
    digit_colors = {
        '0': "255 255 255 ",  # White for 0
        '1': "255 0 0 ",       # Red for 1
        '2': "0 255 0 ",       # Green for 2
        '3': "0 0 255 ",       # Blue for 3
        '4': "255 255 0 ",     # Yellow for 4
        '5': "255 0 255 ",     # Magenta for 5
        '6': "0 255 255 ",     # Cyan for 6
        '7': "128 128 128 ",   # Gray for 7
        '8': "255 165 0 ",     # Orange for 8
        '9': "0 128 0 "        # Dark Green for 9
    }

    # Convert Pi to a string and split into digits
    pi_digits = str(pi).replace('.', '')  # Remove the decimal point
    text_index = 0

    # Loop to draw each digit in the center of the image
    for i in range(center_y - 10, center_y + 10):
        for j in range(center_x - 30, center_x + 30):
            if text_index < len(pi_digits):
                char = pi_digits[text_index]
                if char in digit_colors:
                    color = digit_colors[char]
                    color_data[i][j] = color
                text_index += 1
    return color_data
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
    cpt=1
    ppm_files=[]
    while cpt<=10:
      color_data=[[background for _ in range(taille)]for _ in range(taille)]
      pi,points=approximate_pi.main()
      pi=f"{pi:.{nbr_virgule}f}"
      L=pi.split('.')
      name_file=f'image{cpt}_{L[0]}-{L[1]}.ppm'
      f=open(name_file,"w")
      ppm_files.append(name_file)
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
      center_x,center_y=taille//2,taille//2
      color_data=draw_pi_text(color_data,pi,center_x,center_y,taille)
      for i in range(taille):
         for j in range(taille-1):
            f.write(color_data[i][j])
         f.write(color_data[i][j]+'\n')
      f.write("\n")    
      sys.argv[2]+=tmp_2
      cpt+=1
      f.close()
    subprocess.run(["convert", "-delay", "100", "-loop", "0", *ppm_files, "animation.gif"])
    print("Animation GIF créée : animation.gif")
genrerate_ppm_file()


