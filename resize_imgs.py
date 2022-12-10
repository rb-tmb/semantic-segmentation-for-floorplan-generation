#!/usr/bin/python
from PIL import Image
import os
import glob

path = "/home/roshanbalutmb/Documents/Perception Project/segmentation/semantic-segmentation-for-floorplan-generation/"
#path_inp = path+"Input_images"
path_inp = path+"rgb/rgb"
path_resize = path+"Resized_images"
#dirs = os.listdir( path )

def convert_to_jpg():
    for filename in glob.glob(path_resize+'/*.png'):
        print("Running.....")
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save('{}{}{}'.format(path_resize,'/',os.path.split(filename.replace('.png','.jpg'))[1]))
def resize_imgs():
    # change path to your path
    for filename in glob.glob(path_inp+'/*.png'): #path of raw images
        #print(filename)
        img = Image.open(filename).resize((525,600))
        #create directory if it doesn't exist
        if not os.path.exists(path_resize):
            os.makedirs(path_resize)
            print("The new directory for resized images is created!")
        # save resized images to new folder with existing filename
        img.save('{}{}{}'.format(path_resize,'/',os.path.split(filename)[1]))


resize_imgs()
convert_to_jpg()