import os
from os import listdir
from PIL import Image

# The cards should all be 63mm x 88mm or 2.5 x 3.5 inch according to reddit.
# There is a slight difference when converting; decided to use 240 x 336 pixels.
# A4 paper size in pixels is 1123 x 794 pixels for 96 DPI. Settled on 96 by chance.

images = "./images/" # Folder where the program looks for images
canvas = Image.new("RGB", (794, 1123), (255, 255, 255)) # Create blank A4 canvas
# canvas.save("empty-canvas.png") # Save it for testing
print(os.listdir(images)) # Verifying "images" folder contents

location = (0, 0) # Coordinates

for image in os.listdir(images): # Parsing contents of "images"

    filename = "./images/" + image # Provide full path for safety sake
    
    # Update location for next image

    with Image.open(filename) as img:

        img.load

        canvas.paste(
            img.resize((240, 336)), # Image being pasted in also gets resized
            location # Where to place top-left corner of the image
        )

        location = (location[0] + 240, location[1])

        # print(type(img), img.format, img.size)

canvas.save("DLC.png") # Save final product