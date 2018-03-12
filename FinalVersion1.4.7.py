import PIL
from PIL import Image
from PIL import ImageDraw

imageFile = "BBB.jpg"
im1=Image.open(imageFile)

# Opening the file BBB.jpg
imageFile = "BBB.jpg"
im1=Image.open(imageFile)

# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
draw.text((140, 180),"B_B_B_Big_Baller_Brand",(255,105,180,))
draw = ImageDraw.Draw(im1)

# Save the image with a new name
im1.save("BBB.jpg")




# Changes the color of the shirt to black and white. And then it will create a copy and save.
image1 = Image.open('BBB.jpg')
image1.convert(mode='L').save('BBB_mod.jpg') # Saves the new modified image of BBB.jpg




# Changes the color of the shirt to a static black and white color. And then it will create a copy and save.
image1 = Image.open('BBB.jpg')
image1.convert(mode='1').save('BBB_mod2.jpg') # Saves the new modified image of BBB.jpg



# Opens the image BBB.jpg
old_im = Image.open('BBB.jpg')
old_size = old_im.size

# Creates a frame 600 by 600 around the new image of BBB.jpg, with the color black
new_size = (600, 600)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
# Displays image
new_im.show()
# new_im.save('BBB.jpg') 



# opens the BBB_mod.jpg img
old_im = Image.open('BBB_mod.jpg')
old_size = old_im.size

# Creates a frame 600 by 600 for img BBB_mod.jpg, with the color black
new_size = (600, 600)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
# Displays image
new_im.show()
# new_im.save('BBB.jpg') 



 # opens the BBB_mod2.jpg img
old_im = Image.open('BBB_mod2.jpg')
old_size = old_im.size

# Creates a frame 600 by 600 for img BBB_mod2.jpg, with the color black
new_size = (600, 800)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
# Displays image
new_im.show()
# new_im.save('BBB.jpg')       