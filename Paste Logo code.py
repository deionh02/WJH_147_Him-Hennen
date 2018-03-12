import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path
import PIL.ImageDraw


def paste_logo(original_image, logo_size, logo):
    logo = PIL.image.open("/Users/229480/Desktop/download.jpg")
    
    #set the radius of the rounded crners
    logo_size = .3
    width, height = original_image.size
    position = int(logo_size * min(width, height))
    
    rlogo = logo.resize((position, position))
    
    result = original_image.copy()
    result.paste(rlogo, (0,0), rlogo)
    return result 
    
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

def paste_logo_for_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
      # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'logo1')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed   
        
    #load all the images
    image_list, file_list = get_images(directory) 
    logo = PIL.Image.open("/Users/229480/Desktop/download.jpg")
    logo_size = .3
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        #round the corners with radius = 30% of short side
        new_image = paste_logo(image_list[n],logo_size, logo)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
     
