import math
from PIL import Image

# chemin_image = 'LeEnLogo.png'
image = Image.open('D:\GITHUB\LearnEngine\Learn.ai\pages\LeEnLogo.png')

largeur, hauteur = image.size
total_R, total_G, total_B = 0, 0, 0

for x in range(largeur):
    for y in range(hauteur):
        pixel = image.getpixel((x, y))
        total_R += pixel[0]
        total_G += pixel[1]
        total_B += pixel[2]

nombre_pixels = largeur * hauteur
moyenne_R = total_R // nombre_pixels
moyenne_G = total_G // nombre_pixels
moyenne_B = total_B // nombre_pixels

couleur_moyenne = (moyenne_R, moyenne_G, moyenne_B)
print("Couleur moyenne (RVB) :", couleur_moyenne)
