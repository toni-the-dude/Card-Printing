# Card Printing

<p>Short script to help align playing cards with their card backs for the sake of printing.</p>

<p>The program starts with a <b>blank A4 canvas</b> and fills the empty space in a <b>predetermined</b> manner.<br> I estimated <b>9 cards</b> to be able to comfortably fit within this specific canvas.<br> The program will <b>not</b> check if more than 9 cards will be added since they will likely be off-screen.</p>

<p>It proceeds to look for images within the "images" folder which SHOULD be within the current directory (must be created if missing). It then iterates through each image and asks the user how many copies of each should be added to the canvas, aligning them according to a hardcoded offset and limiting <b>3 per row.</b> All the found images get <b>resized to the same parameters</b> that have also been hardcoded.</p>

<p>Finally, the result is saved within the root directory.</p>
