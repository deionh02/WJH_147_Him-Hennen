from PIL import Image
import os.path
import matplotlib.pyplot as plt # single use of plt is commented out
import PIL.ImageDraw

image1 = Image.open('BBB1.jpg')
image1.convert(mode='L').save('BBB_mod.jpg')


image2 = Image.open('blue.jpg')
image2.convert(mode='L').save('blue_mod.jpg')

image3 = Image.open('hood.jpg')
image3.convert(mode='L').save('hood_mod.jpg')

image4 = Image.open('zo.jpg')
image4.convert(mode='L').save('zo_mod.jpg')


