#!/usr/bin/env python

from gimpfu import *
import os.path

def recrop_to_3_by_2_ratio(image, drawable):
    pdb.gimp_message(str(drawable.width) +'x'+ str(drawable.height)+" -> ")
    # Define aspect ratio
    aspect_ratio = 3.0/2.0
    
    # Get current dimensions of the image plus 7% bezel
    width = int(drawable.width * 1.07)
    height = int(drawable.height * 1.07)

    # Set all dimensions to 10/25 px grade
    if (width % 25 > 0) and (width % 10 > 0):
        if (25 - (width % 25)) < (10 - (width % 10)):
            width = width + (25 - (width % 25))
        else:
            width = width + (10 - (width % 10)) 

    if (height % 25 > 0) and (height % 10 > 0):
        if (25 - (height % 25)) < (10 - (height % 10)):
            height = height + (25 - (height % 25))
        else:
            height = height + (10 - (height % 10)) 
    			
    # Calculate new dimensions with aspect ratio
    if (abs(width/height - aspect_ratio) > 0.0000001):
        new_height = int(width / aspect_ratio)
        new_width = int(height * aspect_ratio)
        if (new_height > height):
            height = int(width / aspect_ratio)
        if (new_width > width):
            width = int(height * aspect_ratio)
    pdb.gimp_message(str(drawable.width) +'x'+ str(drawable.height)+" -> "+str(width) +'x'+ str(height))
            
    pdb.gimp_image_resize(image, width, height, int((width - drawable.width)/2), int((height - drawable.height)/2))
    pdb.gimp_layer_resize(pdb.gimp_image_get_active_layer(image), width, height, int((width - drawable.width)/2), int((height - drawable.height)/2))
    pdb.gimp_layer_flatten(pdb.gimp_image_get_active_layer(image))
    

register(
    "python_fu_recrop_to_ratio",
    "Resize to 3 by 2 ratio",
    "Change canvas size to 3:2 aspect ratio with 10/25 px step scale",
    "Alex Lytvynenko",
    "Alex Lytvynenko",
    "2023",
    "<Image>/Image/Resize to 3 by 2 ratio",
    "*",
    [],
    [],
    recrop_to_3_by_2_ratio)

main()
