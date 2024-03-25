import os
from os import listdir
from PIL import Image

images = "./images/"
# filename = "./images/Diamond_Cutter.webp"

print(os.listdir(images))

for image in os.listdir(images):

    filename = "./images/" + image

    with Image.open(filename) as img:

        img.load

        print(type(img), img.format, img.size)

# img.show()