#!/usr/bin/env python

from gimpfu import *
import os.path

def save_as_jpg_image(image, drawable):
    # Save the image as JPEG
    pdb.gimp_message("Saving...")
    file_path = pdb.gimp_image_get_filename(image)
    if file_path:
        file_dir, file_name = os.path.split(file_path)
        file_name, file_ext = os.path.splitext(file_name)
        if file_ext.lower() != ".jpg":
            file_ext = ".jpg"
        pdb.gimp_message("Save as "+file_name+file_ext)
        new_file_path = os.path.join(file_dir, file_name + file_ext)
        pdb.file_jpeg_save(image, drawable, new_file_path, new_file_path, 1.0, 0, 1, 1, "", 0, 1, 0, 2)


register(
    "python_fu_autosave_as_jpg",
    "Save as JPG",
    "Save as JPG on source folder",
    "Alex Lytvynenko",
    "Alex Lytvynenko",
    "2023",
    "<Image>/File/Export as JPEG (silent)",
    "*",
    [],
    [],
    save_as_jpg_image)

main()
