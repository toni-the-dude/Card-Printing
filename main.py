import os
from os import listdir
from PIL import Image

# The cards should all be 63mm x 88mm or 2.5 x 3.5 inch according to reddit.
# There is a slight difference when converting; decided to use 240 x 336 pixels.
# A4 paper size in pixels is 1123 x 794 pixels for 96 DPI. Settled on 96 by chance.

images = "./images/" # Folder where the program looks for images
canvas = Image.new("RGB", (794, 1123), (255, 255, 255)) # Create blank A4 canvas
# canvas.save("empty-canvas.png") # Testing
print(os.listdir(images)) # Verifying "images" folder contents

offset_x = 16 # (A4 width - 3 * card width) / 4
offset_y = 28  # (A4 length - 3 * card length) / 4
location = (offset_x, offset_y) # Coordinates for top-left corner of each card
cards_per_row = 3

for image in os.listdir(images): # Parsing contents of "images"

    filename = "./images/" + image # Provide full path for safety sake
    copies = int(input("How many copies of {0} do you want?\n".format(image))) # How many of the same image to print

    while copies < 1 or copies > 9:
        copies = int(input("Invalid input. Try 1-9.\n"))

    with Image.open(filename) as img:

        while copies != 0:

            img.load

            canvas.paste(
                img.resize((240, 336)), # Image being pasted in also gets resized
                location # Where to place top-left corner of the image
            )

            if cards_per_row == 1: # Last card for current row
                location = (offset_x, location[1] + 336 + offset_y) # Go to the next row within the canvas
                cards_per_row = 3
            else: # Not last card for current row
                location = (location[0] + 240 + offset_x, location[1]) # Update location for next image
                cards_per_row -= 1

            copies -= 1

canvas.save("DLC.png") # Save the final product