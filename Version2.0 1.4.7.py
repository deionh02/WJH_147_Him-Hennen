import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  
from PIL import Image
from PIL import ImageFont
import textwrap  

          

def frame(original_image, color):
    """ Put frame around a PIL.image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with a frame, where
    0 < frame_width < 1
    is the border as a portion of the shorter dimension of original_image
    """
    #create a mask
    ###
    
    #start with transparent mask
    r, g, b = color
    font = ImageFont.truetype("arial",60)
    img= Image.open(original_image)
    draw = PIL.ImageDraw.Draw(img)
    
    draw.text((0,0),"Test", (color),font=font)

    return img
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing
    a list with a PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory 
    """
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list   
   
def round_corners_of_all_images(directory=None, color=(255,0,0), frame_width=0.10):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = "/Users/229480/Desktop/Computer science stuff/Lesson 1.4/Him_1_4_5_frame.py"

        os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split(' . ')
        
        # Round the corners with radius = 30% of short side
        new_image = frame(image_list[n],color,frame_width)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

def text_on_image(image, text, size, line_width, r,g,b):
    '''Font must be one of the following:
        - 'Arial.ttf'
        - More
    '''
    font = ImageFont.truetype("Arial.ttf",size)
    width, height = image.size
    img = Image.new('RGBA', (width,height), (0,0,0,0))
    write = PIL.ImageDraw.Draw(img)
    lines = textwrap.fill(text, width=line_width)
    w,h = font.getsize(lines)
    print w,width,h,height
    write.text((((width-w)/2),((height-h)/2)),lines,(r,g,b),font=font)
    image.paste(img,(0,0),img)
    print 'Image',image,'now has text on it!'
    return image
    
def text_on_all_images(color=(255,0,0), directory=None):
    if directory== None:     
        directory = os.getcwd()
    new_directory = os.path.join(directory, "Images With Text")
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        print n
        new_image = frame(images[n], color)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have text on them!'

    