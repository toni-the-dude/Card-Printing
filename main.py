import os
from os import listdir
from PIL import Image

# The cards should all be 63mm x 88mm or 2.5 x 3.5 inch according to reddit.
# There is a slight difference when converting; decided to use 240 x 336 pixels.
# A4 paper size in pixels is 1123 x 794 pixels for 96 DPI. Settled on 96 by chance.

images = "./images/"
# filename = "./images/Diamond_Cutter.webp"
canvas = Image.new("RGB", (1123, 794), (255, 255, 255)) # Blank A4 canvas
canvas.save("empty-canvas.png")
print(os.listdir(images))

for image in os.listdir(images):

    filename = "./images/" + image

    with Image.open(filename) as img:

        img.load

        print(type(img), img.format, img.size)

# img.show()