from PIL import Image

filename = "./images/Diamond_Cutter.webp"

with Image.open(filename) as img:
    img.load

print(type(img), img.format, img.size)

