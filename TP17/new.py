#!/usr/bin/env python3
import sys
import approximate_pi
import subprocess

def generate_ppm_file():
    taille = int(sys.argv[1])
    nbr_virgule = int(sys.argv[3])
    inside_circle = '255 0 0 '  # Red for points inside the circle
    out_circle = '0 255 0 '     # Green for points outside the circle
    background = '255 255 255 ' # White background

    sys.argv[2] = int(sys.argv[2])
    tmp = sys.argv[2]
    tmp_2 = sys.argv[2] // 10
    sys.argv[2] = tmp_2
    cpt = 0
    ppm_files = []

    while cpt <= 10:
        # Initialize color data for the PPM file
        color_data = [[background for _ in range(taille)] for _ in range(taille)]
        
        # Calculate Pi approximation
        pi, points = approximate_pi.main()
        pi_value = f"{pi:.{nbr_virgule}f}"
        
        # Split the Pi value into integer and fractional parts for naming the file
        L = pi_value.split('.')
        name_file = f'image{cpt}_{L[0]}-{L[1]}.ppm'
        ppm_files.append(name_file)

        # Create the header for the PPM file
        ppm_header = f"P3\n{taille} {taille}\n255\n"
        
        # Convert Pi value into text blocks and place them on the image
        # We'll treat each character as a block of pixels in a grid
        x_offset = 10  # Start position for the Pi value text on the X-axis
        y_offset = 10  # Start position for the Pi value text on the Y-axis
        text_color = "0 0 0 "  # Black color for the text

        # Convert Pi value to list of characters
        for i, char in enumerate(pi_value):
            if char != ".":
                # Convert each character to a simple block of pixels
                for dx in range(5):  # 5x5 grid for each character
                    for dy in range(5):
                        if 0 <= x_offset + dx < taille and 0 <= y_offset + dy < taille:
                            color_data[y_offset + dy][x_offset + dx] = text_color
                # Move the X position to the next character
                x_offset += 6  # 5 pixels for the character and 1 for spacing
        
        # Add the points (inside circle: red, outside circle: green)
        for elt in points:
            x, y, indice = elt
            px = int((x + 1) / 2 * (taille - 1))
            py = int((y + 1) / 2 * (taille - 1))
            if indice:
                color_data[px][py] = inside_circle
            else:
                color_data[px][py] = out_circle

        # Write the PPM file
        with open(name_file, 'w') as f:
            f.write(ppm_header)
            for i in range(taille):
                for j in range(taille):
                    f.write(color_data[i][j])
                f.write("\n")

        # Update the counter and arguments
        sys.argv[2] += tmp_2
        cpt += 1

    # Create the GIF using ImageMagick's convert
    subprocess.run(["convert", "-delay", "100", "-loop", "0", *ppm_files, "animation.gif"])
    print("Animation GIF created: animation.gif")

# Call the function to generate the PPM files and GIF
generate_ppm_file()