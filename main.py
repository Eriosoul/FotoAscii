from PIL import Image
Image.open('fen.png')

import pywhatkit
pywhatkit.image_to_ascii_art('fen.png', 'MyArt')
read_file = open('MyArt.txt', 'r')
print(read_file.read())