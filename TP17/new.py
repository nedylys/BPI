#! usr/bin/env python3
import sys
import subprocess
from math import sqrt
import approximate_pi
from random import uniform

def generate_ppm_file(taille, nbr_virgule, n, points, bon_points, cpt):
    # Calculating the current approximation of pi
    pi, _, _ = approximate_pi.main()
    pi = f"{pi:.{nbr_virgule}f}"
    L = pi.split('.')  # Split the approximation into integer and decimal parts

    # Write to PPM file
    with open(f'image{cpt}_{L[0]}-{L[1]}.ppm', "w") as f:
        f.write("P3\n")
        f.write(f'{taille} {taille}\n')
        f.write("255\n")  # Max value for RGB
        
        # Image dimensions
        center_x, center_y = taille // 2, taille // 2
        radius = taille // 2
        
        # Fill the image with points
        for y in range(taille):
            for x in range(taille):
                # Convert pixel coordinates to normalized coordinates [-1, 1]
                nx = (x - center_x) / radius
                ny = (y - center_y) / radius
                
                # Determine if the point is inside the circle
                if nx**2 + ny**2 <= 1:
                    if (nx, ny) in bon_points:
                        f.write("0 0 0 ")  # Black for points inside the circle
                    else:
                        f.write("255 255 255 ")  # White for points outside the circle
                else:
                    f.write("255 255 255 ")  # White for points outside the circle
        
        f.write(f"# π ≈ {pi}\n")  # Adding the value of pi as a comment

def main():
    # Check if we have the correct number of arguments
    if len(sys.argv) != 4:
        raise ValueError("Usage: python draw.py <taille_image> <nombre_points> <precision_pi>")

    # Get the command line arguments
    try:
        taille = int(sys.argv[1])  # Image size
        n = int(sys.argv[2])  # Number of points
        nbr_virgule = int(sys.argv[3])  # Precision of π
    except ValueError:
        raise ValueError("All arguments must be integers and valid.")

    if taille < 100 or n < 100 or nbr_virgule < 1 or nbr_virgule > 5:
        raise ValueError("Arguments are out of bounds: taille >= 100, n >= 100, and 1 <= nbr_virgule <= 5")

    # Generate points using approximate_pi
    cpt = 0
    for i in range(1, n + 1):
        pi, points, bon_points = approximate_pi.main()
        
        # Generate an image every 10% of points
        if i % (n // 10) == 0:
            generate_ppm_file(taille, nbr_virgule, n, points, bon_points, cpt)
            cpt += 1

    # Create the GIF using ImageMagick
    subprocess.run(["convert", "-delay", "10", "-loop", "0", "*.ppm", "animation.gif"])

if __name__ == "__main__":
    main()