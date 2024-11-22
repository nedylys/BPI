#!/usr/bin/env python3
import sys
import approximate_pi
import subprocess

def draw_pi_text(color_data, pi, taille):
    # Define a color map for digits of Pi
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

    # Remove decimal point from pi and get the digits as a string
    pi_digits = str(pi).replace('.', '')  # Remove the decimal point

    # Image center coordinates
    center_x, center_y = taille // 2, taille // 2
    text_index = 0  # To track which digit of Pi we're drawing
    digit_spacing = 15  # Space between digits

    # Loop over a small area around the center to place Pi digits
    for i in range(center_y - 10, center_y + 10):
        for j in range(center_x - 60, center_x + 60, digit_spacing):
            if text_index < len(pi_digits):  # Ensure we're not out of Pi digits
                char = pi_digits[text_index]
                if char in digit_colors:
                    color = digit_colors[char]
                    if i >= 0 and i < taille and j >= 0 and j < taille:
                        color_data[i][j] = color  # Place the color at (i, j)
                text_index += 1

    return color_data

def generate_ppm_file():
    taille = int(sys.argv[1])  # Image size (width and height)
    nbr_virgule = int(sys.argv[3])  # Number of decimal places for Pi
    inside_circle = '255 0 0 '  # Red color for inside circle
    out_circle = '0 255 0 '     # Green color for outside circle
    background = '255 255 255 '  # White background

    sys.argv[2] = int(sys.argv[2])  # Number of points for Monte Carlo approximation
    tmp = sys.argv[2]
    tmp_2 = sys.argv[2] // 10
    sys.argv[2] = tmp_2

    cpt = 1
    ppm_files = []

    while cpt <= 10:
        # Initialize the color data with the background color
        color_data = [[background for _ in range(taille)] for _ in range(taille)]
        
        # Approximate Pi using the Monte Carlo method
        pi, points = approximate_pi.main()
        
        # Format the Pi value to the specified number of decimal places
        pi = f"{pi:.{nbr_virgule}f}"
        
        # Split the integer and decimal parts of Pi for the filename
        L = pi.split('.')
        name_file = f'image{cpt}_{L[0]}-{L[1]}.ppm'
        
        with open(name_file, "w") as f:
            ppm_files.append(name_file)
            
            # Write the PPM header
            f.write("P3\n")
            f.write(f'{taille} {taille}\n')
            f.write("255\n")
            
            # Fill the PPM image with color data based on the Monte Carlo points
            for elt in points:
                x, y, indice = elt
                px = int((x + 1) / 2 * (taille - 1))
                py = int((y + 1) / 2 * (taille - 1))
                if indice:
                    color_data[px][py] = inside_circle
                else:
                    color_data[px][py] = out_circle
            
            # Draw the approximate Pi value in the center of the image
            color_data = draw_pi_text(color_data, pi, taille)
            
            # Write the pixel data to the PPM file
            for i in range(taille):
                for j in range(taille):
                    f.write(color_data[i][j])
                f.write("\n")
        
        # Update the number of points for the next iteration
        sys.argv[2] += tmp_2
        cpt += 1

    # Create an animation GIF from the generated PPM files
    subprocess.run(["convert", "-delay", "100", "-loop", "0", *ppm_files, "animation.gif"])
    print("Animation GIF créée : animation.gif")

generate_ppm_file()
